import os
import glob
import re

def make_sections_transparent(filepath):
    print(f"Checking {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find <section class="..."> or <article class="..."> and replace bg-white or bg-slate-50
    # but only for these top-level structural tags
    
    def replacer(match):
        attributes = match.group(2)
        attributes = re.sub(r'\bbg-white\b', 'bg-transparent', attributes)
        attributes = re.sub(r'\bbg-slate-50\b', 'bg-transparent', attributes)
        # Ensure bg-transparent doesn't appear multiple times by tracking
        if 'bg-transparent' not in attributes:
            attributes += ' bg-transparent'
        return match.group(1) + attributes + match.group(3)

    new_content = re.sub(r'(<(?:section|article)[^>]*class=")([^"]*)(")', replacer, content)
        
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

if __name__ == "__main__":
    search_path = "c:/Users/user/Documents/marcusengineering/**/*.markdown"
    html_layouts = "c:/Users/user/Documents/marcusengineering/_layouts/*.html"
    for p in [search_path, html_layouts]:
        for file in glob.glob(p, recursive=True):
            if "node_modules" not in file and "_site" not in file:
                make_sections_transparent(file)
    print("Done")
