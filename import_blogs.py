import os
import xml.etree.ElementTree as ET
import re
from datetime import datetime

# Paths
wp_export_dir = r"c:\Users\user\Documents\marcusengineering\wordpress blogs"
jekyll_posts_dir = r"c:\Users\user\Documents\marcusengineering\_posts"

# Ensure output directory exists
if not os.path.exists(jekyll_posts_dir):
    os.makedirs(jekyll_posts_dir)

def clean_content(content):
    if not content:
        return ""
    # Standard WordPress caption shortcode cleaning
    # [caption ...]<img ... /> Caption Text [/caption]
    content = re.sub(r'\[caption.*?\](.*?)\[/caption\]', r'\1', content, flags=re.DOTALL)
    # Remove any stray WordPress shortcodes if found (very basic)
    content = re.sub(r'\[.*?\]', '', content)
    return content

def process_file(file_path):
    print(f"Processing {file_path}...")
    try:
        # We need to handle namespaces in WordPress WXR files
        namespaces = {
            'excerpt': 'http://wordpress.org/export/1.2/excerpt/',
            'content': 'http://purl.org/rss/1.0/modules/content/',
            'wfw': 'http://wellformedweb.org/CommentAPI/',
            'dc': 'http://purl.org/dc/elements/1.1/',
            'wp': 'http://wordpress.org/export/1.2/'
        }
        
        tree = ET.parse(file_path)
        root = tree.getroot()
        channel = root.find('channel')
        
        posts_count = 0
        for item in channel.findall('item'):
            post_type = item.find('wp:post_type', namespaces).text
            status = item.find('wp:status', namespaces).text
            
            if post_type == 'post' and status == 'publish':
                title = item.find('title').text or "Untitled"
                slug = item.find('wp:post_name', namespaces).text
                if not slug:
                    # Fallback to slugified title
                    slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
                
                post_date_str = item.find('wp:post_date', namespaces).text
                try:
                    post_date = datetime.strptime(post_date_str, '%Y-%m-%d %H:%M:%S')
                except:
                    post_date = datetime.now()
                
                content = item.find('content:encoded', namespaces).text or ""
                content = clean_content(content)
                
                categories = []
                tags = []
                for cat in item.findall('category'):
                    domain = cat.get('domain')
                    if domain == 'category':
                        categories.append(cat.text)
                    elif domain == 'post_tag':
                        tags.append(cat.text)
                
                # Format for Jekyll
                filename = f"{post_date.strftime('%Y-%m-%d')}-{slug}.markdown"
                filepath = os.path.join(jekyll_posts_dir, filename)
                
                # Check for duplicates or similar-named files in this run
                if os.path.exists(filepath):
                    filename = f"{post_date.strftime('%Y-%m-%d')}-{slug}-{posts_count}.markdown"
                    filepath = os.path.join(jekyll_posts_dir, filename)

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write("---\n")
                    f.write(f"layout: post\n")
                    f.write(f"title: \"{title.replace('\"', '\\\"')}\"\n")
                    f.write(f"date: {post_date.strftime('%Y-%m-%d %H:%M:%S %z')}\n")
                    if categories:
                        f.write(f"categories: {categories}\n")
                    if tags:
                        f.write(f"tags: {tags}\n")
                    # Preserve original slug in permalink to avoid breaking direct links
                    # WordPress usually has them as /slug/ or /category/slug/
                    # Let's keep it simple as /:title/ (slug)
                    f.write(f"permalink: /{slug}/\n")
                    f.write("---\n\n")
                    f.write(content)
                
                posts_count += 1
        
        print(f"Imported {posts_count} posts from {os.path.basename(file_path)}")
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Process all XML files
for file in os.listdir(wp_export_dir):
    if file.endswith('.xml'):
        process_file(os.path.join(wp_export_dir, file))

# Cleanup the default Jekyll post
welcome_post = os.path.join(jekyll_posts_dir, "2026-03-13-welcome-to-jekyll.markdown")
if os.path.exists(welcome_post):
    os.remove(welcome_post)
    print("Removed default welcome post.")
