import os
import re

posts_dir = r"c:\Users\user\Documents\marcusengineering\_posts"
images_dir = r"c:\Users\user\Documents\marcusengineering\assets\images\posts"

# Map local filenames (without extension) to their webp path
local_images = {}
for f in os.listdir(images_dir):
    if f.endswith('.webp'):
        base = os.path.splitext(f)[0]
        local_images[base.lower()] = f

print(f"Loaded {len(local_images)} local webp images.")

# Regex to find external image URLs
url_regex = re.compile(r'http[s]?://[^\s"\']+\.(?:jpg|jpeg|gif|png|webp|svg)', re.IGNORECASE)

updated_count = 0

for filename in os.listdir(posts_dir):
    if filename.endswith(".markdown") or filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        urls = url_regex.findall(content)
        
        for url in set(urls):
            # Get basename from URL
            url_path = url.split('/')[-1]
            url_base = os.path.splitext(url_path)[0].lower()
            
            if url_base in local_images:
                local_path = f"/assets/images/posts/{local_images[url_base]}"
                content = content.replace(url, local_path)
        
        # Also catch any internal relative paths if they were already there but pointed to non-webp
        # (Though we just reverted, so they should be external)
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            updated_count += 1
            # print(f"Updated {filename}")

print(f"Done. Updated {updated_count} files.")
