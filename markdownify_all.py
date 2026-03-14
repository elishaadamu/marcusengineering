import os
import re

def markdownify_content(content):
    # Preserve code blocks if any (unlikely in these imports but good practice)
    # Actually, standardizing is safer. 
    
    # 1. Remove Gutenberg comments
    content = re.sub(r'<!-- /?wp:.*? -->', '', content)
    
    # 2. Headers
    content = re.sub(r'<h1.*?>(.*?)</h1>', r'# \1\n\n', content, flags=re.IGNORECASE | re.DOTALL)
    content = re.sub(r'<h2.*?>(.*?)</h2>', r'## \1\n\n', content, flags=re.IGNORECASE | re.DOTALL)
    content = re.sub(r'<h3.*?>(.*?)</h3>', r'### \1\n\n', content, flags=re.IGNORECASE | re.DOTALL)
    content = re.sub(r'<h4.*?>(.*?)</h4>', r'#### \1\n\n', content, flags=re.IGNORECASE | re.DOTALL)
    content = re.sub(r'<h5.*?>(.*?)</h5>', r'##### \1\n\n', content, flags=re.IGNORECASE | re.DOTALL)
    
    # 3. Images in figures or just img tags
    # This pattern catches <figure ...><img src="..."><figcaption>...</figcaption></figure>
    # We'll pull out the src, alt, and maybe title.
    def figure_repl(match):
        body = match.group(0)
        src = re.search(r'src=["\'](.*?)["\']', body)
        alt = re.search(r'alt=["\'](.*?)["\']', body)
        cap = re.search(r'<figcaption.*?>(.*?)</figcaption>', body, flags=re.IGNORECASE | re.DOTALL)
        
        src_val = src.group(1) if src else ""
        alt_val = alt.group(1) if alt else ""
        cap_val = cap.group(1) if cap else ""
        
        if cap_val:
            return f"![{alt_val}]({src_val})\n*({cap_val})*\n\n"
        return f"![{alt_val}]({src_val})\n\n"

    content = re.sub(r'<figure.*?>.*?</figure>', figure_repl, content, flags=re.IGNORECASE | re.DOTALL)
    
    # Lone img tags
    def img_repl(match):
        attrs = match.group(0)
        src = re.search(r'src=["\'](.*?)["\']', attrs)
        alt = re.search(r'alt=["\'](.*?)["\']', attrs)
        src_val = src.group(1) if src else ""
        alt_val = alt.group(1) if alt else ""
        return f"![{alt_val}]({src_val})"

    content = re.sub(r'<img [^>]*?/>', img_repl, content, flags=re.IGNORECASE)
    content = re.sub(r'<img [^>]*?>', img_repl, content, flags=re.IGNORECASE)

    # 4. Links
    content = re.sub(r'<a [^>]*?href=["\'](.*?)["\'][^>]*?>(.*?)</a>', r'[\2](\1)', content, flags=re.IGNORECASE | re.DOTALL)
    
    # 5. Lists
    # First handle nested items by just marking them. Simple 1-level list is easier.
    content = re.sub(r'<li.*?>(.*?)</li>', r'- \1', content, flags=re.IGNORECASE | re.DOTALL)
    content = re.sub(r'</?(?:ul|ol).*?>', '\n', content, flags=re.IGNORECASE)

    # 6. Formatting
    content = re.sub(r'<(?:strong|b).*?>(.*?)</(?:strong|b)>', r'**\1**', content, flags=re.IGNORECASE | re.DOTALL)
    content = re.sub(r'<(?:em|i).*?>(.*?)</(?:em|i)>', r'*\1*', content, flags=re.IGNORECASE | re.DOTALL)
    content = re.sub(r'<del.*?>(.*?)</del>', r'~~\1~~', content, flags=re.IGNORECASE | re.DOTALL)
    
    # 7. Blockquotes
    content = re.sub(r'<blockquote.*?>(.*?)</blockquote>', r'> \1\n\n', content, flags=re.IGNORECASE | re.DOTALL)

    # 8. Paragraphs
    content = re.sub(r'<p.*?>(.*?)</p>', r'\1\n\n', content, flags=re.IGNORECASE | re.DOTALL)
    
    # 9. Strip all remaining common tags but keep content
    content = re.sub(r'</?(?:div|span|header|footer|article|section|aside|main).*?.*?>', '', content, flags=re.IGNORECASE)
    
    # 10. BR and NBSP
    content = re.sub(r'<br\s*/?>', '\n', content, flags=re.IGNORECASE)
    content = content.replace('&nbsp;', ' ')
    
    # 11. Final Cleanup
    # Standardize newlines
    content = re.sub(r'\n{3,}', '\n\n', content)
    # Remove excessive spaces at start of lines
    lines = [line.strip() for line in content.split('\n')]
    content = '\n'.join(lines)
    
    return content.strip()

posts_dir = r"c:\Users\user\Documents\marcusengineering\_posts"

files = os.listdir(posts_dir)
for f in files:
    if f.endswith('.markdown') or f.endswith('.md'):
        path = os.path.join(posts_dir, f)
        with open(path, 'r', encoding='utf-8') as file:
            full_text = file.read()
        
        parts = full_text.split('---', 2)
        if len(parts) >= 3:
            header = '---' + parts[1] + '---\n'
            body = parts[2]
            new_body = markdownify_content(body)
            
            # Write back
            # For consistency, let's use .markdown if that's what was there, or .md
            # Actually, let's just stick to the original filename for now to avoid breaking links if they depend on filenames (unlikely in Jekyll post mapping but possible)
            # Wait, Jekyll permalinks are usually slug-based.
            with open(path, 'w', encoding='utf-8') as file:
                file.write(header + '\n' + new_body + '\n')
            print(f"Processed: {f}")

print("All posts processed.")
