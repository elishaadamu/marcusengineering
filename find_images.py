import os
import re

posts_dir = r"c:\Users\user\Documents\marcusengineering\_posts"
output_dir = r"c:\Users\user\Documents\marcusengineering\assets\images\posts"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Regex to find images in <img> tags or markdown ![]() syntax
img_tag_regex = re.compile(r'<img[^>]+src=["\'](http[s]?://[^"\']+\.(?:jpg|jpeg|gif|png|webp|svg))["\']', re.IGNORECASE)
md_img_regex = re.compile(r'!\[.*?\]\((http[s]?://[^)]+\.(?:jpg|jpeg|gif|png|webp|svg))\)', re.IGNORECASE)

all_images = set()

for filename in os.listdir(posts_dir):
    if filename.endswith(".markdown") or filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            tags = img_tag_regex.findall(content)
            mds = md_img_regex.findall(content)
            all_images.update(tags)
            all_images.update(mds)

print(f"Found {len(all_images)} unique images.")
for img in sorted(list(all_images)):
    print(img)
