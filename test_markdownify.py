import os
import re

def markdownify_content(content):
    # Remove Gutenberg comment blocks
    content = re.sub(r'<!-- /?wp:.*? -->', '', content)
    
    # Headers
    content = re.sub(r'<h1.*?>(.*?)</h1>', r'# \1\n', content, flags=re.IGNORECASE | re.DOTALL)
    content = re.sub(r'<h2.*?>(.*?)</h2>', r'## \1\n', content, flags=re.IGNORECASE | re.DOTALL)
    content = re.sub(r'<h3.*?>(.*?)</h3>', r'### \1\n', content, flags=re.IGNORECASE | re.DOTALL)
    content = re.sub(r'<h4.*?>(.*?)</h4>', r'#### \1\n', content, flags=re.IGNORECASE | re.DOTALL)
    
    # Bold / Italic
    content = re.sub(r'<(?:strong|b).*?>(.*?)</(?:strong|b)>', r'**\1**', content, flags=re.IGNORECASE | re.DOTALL)
    content = re.sub(r'<(?:em|i).*?>(.*?)</(?:em|i)>', r'*\1*', content, flags=re.IGNORECASE | re.DOTALL)
    
    # Links
    # Note: This is simplified, might catch too much if target contains ">"
    content = re.sub(r'<a [^>]*?href=["\'](.*?)["\'][^>]*?>(.*?)</a>', r'[\2](\1)', content, flags=re.IGNORECASE | re.DOTALL)
    
    # Images
    # Try to catch simple img tags first
    # <img ... src="..." alt="..." />
    def img_repl(match):
        attrs = match.group(0)
        src_match = re.search(r'src=["\'](.*?)["\']', attrs)
        alt_match = re.search(r'alt=["\'](.*?)["\']', attrs)
        src = src_match.group(1) if src_match else ""
        alt = alt_match.group(1) if alt_match else ""
        return f"![{alt}]({src})"
    
    content = re.sub(r'<img [^>]*?/>', img_repl, content, flags=re.IGNORECASE)
    content = re.sub(r'<img [^>]*?>', img_repl, content, flags=re.IGNORECASE)

    # Paragraphs - replace with newlines
    content = re.sub(r'<p.*?>(.*?)</p>', r'\1\n\n', content, flags=re.IGNORECASE | re.DOTALL)
    
    # Lists
    # This is tricky without a real parser, but let's try for simple ones
    content = re.sub(r'<li.*?>(.*?)</li>', r'- \1', content, flags=re.IGNORECASE | re.DOTALL)
    content = re.sub(r'</?(?:ul|ol).*?>', '', content, flags=re.IGNORECASE)
    
    # Divs / Spans / Figures - just strip the tags
    content = re.sub(r'</?(?:div|span|figure|figcaption|header|footer|article|section).*?.*?>', '', content, flags=re.IGNORECASE)
    
    # Br tags
    content = re.sub(r'<br\s*/?>', '\n', content, flags=re.IGNORECASE)
    
    # Cleanup extra whitespace or weird artifacts
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content.strip()

posts_dir = r"c:\Users\user\Documents\marcusengineering\_posts"
test_file = "2011-06-02-solar-oven-design.markdown"
filepath = os.path.join(posts_dir, test_file)

with open(filepath, 'r', encoding='utf-8') as f:
    full_content = f.read()

# Split front matter
parts = full_content.split('---', 2)
if len(parts) >= 3:
    header = parts[0] + '---' + parts[1] + '---'
    body = parts[2]
    new_body = markdownify_content(body)
    print("--- NEW BODY PREVIEW ---")
    print(new_body[:500])
    print("------------------------")
else:
    print("Could not find front matter")
