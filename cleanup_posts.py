import os
import re

jekyll_posts_dir = r"c:\Users\user\Documents\marcusengineering\_posts"

files = os.listdir(jekyll_posts_dir)
# Group by YYYY-MM-DD-slug
# Files are like 2022-09-27-all-that-jazz.markdown, 2022-09-27-all-that-jazz-46.markdown, etc.

post_map = {}

for f in files:
    if not f.endswith('.markdown'): continue
    
    # Try to find the base name without the numeric suffix and extension
    # Pattern: YYYY-MM-DD-slug(-suffix)?
    match = re.match(r'^(\d{4}-\d{2}-\d{2}-.*?)(?:-\d+)?\.markdown$', f)
    if match:
        base = match.group(1)
        if base not in post_map:
            post_map[base] = []
        post_map[base].append(f)

for base, variants in post_map.items():
    if len(variants) > 1:
        # Keep the one that is exactly {base}.markdown if it exists
        original = f"{base}.markdown"
        to_keep = original if original in variants else variants[0]
        
        for v in variants:
            if v != to_keep:
                path = os.path.join(jekyll_posts_dir, v)
                os.remove(path)
                print(f"Removed duplicate: {v}")

print("Cleanup complete.")
