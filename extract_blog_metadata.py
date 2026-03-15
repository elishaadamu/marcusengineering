
import os
import re
import json

posts_dir = r"c:\Users\user\Documents\marcusengineering\_posts"
posts = os.listdir(posts_dir)

data = {
    "years": set(),
    "categories": set(),
    "tags": set()
}

def extract_list(text, key):
    match = re.search(f"{key}:\\s*\\[?(.*?)\\]?$", text, re.MULTILINE)
    if match:
        content = match.group(1).strip()
        if not content: return []
        # Handle quoted or unquoted items
        items = re.findall(r"['\"]([^'\"]*)['\"]|([^,]+)", content)
        result = []
        for q, u in items:
            val = (q or u).strip()
            if val: result.append(val)
        return result
    return []

for post_file in posts:
    path = os.path.join(posts_dir, post_file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        if content.startswith('---'):
            parts = content.split('---')
            if len(parts) >= 3:
                fm = parts[1]
                
                # Year from filename
                year = post_file.split('-')[0]
                data["years"].add(year)
                
                # Categories
                for c in extract_list(fm, 'categories'):
                    data["categories"].add(c)
                        
                # Tags
                for t in extract_list(fm, 'tags'):
                    data["tags"].add(t)

print(json.dumps({
    "years": sorted(list(data["years"]), reverse=True),
    "categories": sorted(list(data["categories"])),
    "tags": sorted(list(data["tags"]))
}, indent=2))
