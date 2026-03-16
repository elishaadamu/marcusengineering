import os
import re

posts_dir = r"c:\Users\user\Documents\marcusengineering\_posts"

def process_posts():
    for filename in os.listdir(posts_dir):
        if not filename.endswith(".markdown") and not filename.endswith(".md"):
            continue
            
        filepath = os.path.join(posts_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check if it has front matter
        if not content.startswith("---"):
            continue
            
        parts = content.split("---", 2)
        if len(parts) < 3:
            continue
            
        front_matter = parts[1]
        body = parts[2]
        
        # Remove permalink
        new_front_matter = re.sub(r'^permalink:.*$', '', front_matter, flags=re.MULTILINE)
        
        # Ensure categories exist
        if 'categories:' not in new_front_matter and 'category:' not in new_front_matter:
            new_front_matter += "\ncategories: ['Engineering']\n"
            
        # Clean up double newlines in front matter
        new_front_matter = re.sub(r'\n\s*\n', '\n', new_front_matter)
        
        new_content = "---" + new_front_matter + "---" + body
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Processed {filename}")

if __name__ == "__main__":
    process_posts()
