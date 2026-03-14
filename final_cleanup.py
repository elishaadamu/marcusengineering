import os
import re

def final_cleanup(content):
    # Convert <hr> to ---
    content = re.sub(r'<hr.*?>', '\n---\n', content, flags=re.IGNORECASE)
    # Convert remaining common tags if any missed
    content = re.sub(r'</?(?:section|article|header|footer|div|span|figure|figcaption).*?>', '', content, flags=re.IGNORECASE)
    return content.strip()

posts_dir = r"c:\Users\user\Documents\marcusengineering\_posts"
for f in os.listdir(posts_dir):
    if f.endswith('.markdown') or f.endswith('.md'):
        path = os.path.join(posts_dir, f)
        with open(path, 'r', encoding='utf-8') as file:
            full_text = file.read()
        parts = full_text.split('---', 2)
        if len(parts) >= 3:
            header = '---' + parts[1] + '---\n'
            body = parts[2]
            new_body = final_cleanup(body)
            with open(path, 'w', encoding='utf-8') as file:
                file.write(header + '\n' + new_body + '\n')

print("Final cleanup done.")
