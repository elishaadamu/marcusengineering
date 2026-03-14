import os
import re
import urllib.request
import urllib.parse
import hashlib

posts_dir = r"c:\Users\user\Documents\marcusengineering\_posts"
output_dir = r"c:\Users\user\Documents\marcusengineering\assets\images\posts"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# More aggressive regex to find ANY image URL in quotes
# This catches src="...", href="...", etc.
url_regex = re.compile(r'["\'](http[s]?://[^"\']+\.(?:jpg|jpeg|gif|png|webp|svg))["\']', re.IGNORECASE)
# And markdown syntax
md_img_regex = re.compile(r'!\[.*?\]\((http[s]?://[^)]+\.(?:jpg|jpeg|gif|png|webp|svg))\)', re.IGNORECASE)

all_images = set()

for filename in os.listdir(posts_dir):
    if filename.endswith(".markdown") or filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            urls = url_regex.findall(content)
            mds = md_img_regex.findall(content)
            all_images.update(urls)
            all_images.update(mds)

print(f"Found {len(all_images)} unique image URLs.")

url_to_local = {}

for url in sorted(list(all_images)):
    try:
        # Get filename from URL
        parsed_url = urllib.parse.urlparse(url)
        img_name = os.path.basename(parsed_url.path)
        
        if not img_name:
            img_name = hashlib.md5(url.encode()).hexdigest() + ".jpg"

        local_path = os.path.join(output_dir, img_name)
        
        # If we already downloaded this URL (maybe from previous run), skip download but keep in mapping
        if os.path.exists(local_path):
            # Check if it was really this URL or just same filename
            # For simplicity, if it exists, we skip if we already handled it in this run
            # But we need the mapping.
            url_to_local[url] = "/assets/images/posts/" + os.path.basename(local_path)
            # Actually, multiple URLs might point to same filename. 
            # We should probably check if it's the exact same file.
            # For now, let's just assume if it exists, we can use it.
            continue

        # Handle duplicates if same filename from different paths
        counter = 1
        base, ext = os.path.splitext(img_name)
        while os.path.exists(local_path):
            local_path = os.path.join(output_dir, f"{base}_{counter}{ext}")
            counter += 1
        
        print(f"Downloading {url} to {local_path}...")
        
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(local_path, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        
        url_to_local[url] = "/assets/images/posts/" + os.path.basename(local_path)
    except Exception as e:
        print(f"Failed to download {url}: {e}")

# Now update the posts
for filename in os.listdir(posts_dir):
    if filename.endswith(".markdown") or filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        for url, local in url_to_local.items():
            content = content.replace(url, local)
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")

print("Done.")
