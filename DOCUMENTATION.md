---
layout: default
title: Project Documentation | Engineering Support
permalink: /documentation/
---

# Marcus Engineering Project Documentation

## 🚀 Overview
Marcus Engineering is a premier engineering design firm. This project is a high-performance, SEO-optimized website built with **Jekyll**, **Tailwind CSS**, and **Alpine.js**.

---

## 🛠 Development Environment
To work on this project locally, you need two processes running simultaneously.

### 1. Tailwind CSS Compiler (NPM)
Tailwind watches for changes in your HTML/Markdown and recompiles the CSS.
From the project root:
```bash
npm run dev
```
*   **Input File**: `assets/css/input.css`
*   **Output File**: `assets/css/main.css` (This file is ignored by Git usually, but served by Jekyll)

### 2. Jekyll Preview Server (Ruby)
This hosts the site. The Admin Panel is built into this process.
From the project root:
```bash
bundle exec jekyll serve
```
*   **Main Site**: `http://localhost:4000`
*   **Admin Panel**: `http://localhost:4000/admin`

### 3. Local Admin Panel Features
The site uses `jekyll-admin` to provide a GUI for managing content.
- **Visual Editor**: Write and format Markdown posts with a live preview.
- **Metadata Management**: When creating a new post, metadata fields (like `thumbnail`, `author`, and `categories`) are automatically pre-populated from `_config.yml`. You only need to fill in or override these existing fields; you do not need to add the keys manually every time.
- **Data Management**: Edit YAML files in `_data/` without opening a code editor.
- **Ease of Use**: Manage images and static files through the browser.

### 4. Production Editor (Decap CMS)
For editing content in production without a code editor, the site uses **Decap CMS**.
1. **Access**: `https://your-domain.com/admin/`
2. **Requirements**: Your site must be hosted on Netlify with the following enabled in the Netlify Dashboard:
   - **Identity**: Enable "Identity" in your site settings.
   - **Git Gateway**: In "Identity" settings, scroll down to "Services" and enable "Git Gateway".
3. **Features**:
   - Secure login via Netlify Identity (or your GitHub account).
   - Visual web-based editor for blog posts, authors, and data files.
   - Direct commits to your repository without touch code.
4. **Local Development**: To test this CMS on `localhost`:
   - Run `npx decap-cms-proxy-server` in a separate terminal.
   - Access `http://localhost:4000/admin/`.

---

## 📝 Content Management Guide

### 📂 1. Adding a Blog Post
Blog posts go in the `_posts/` directory.

**File Naming**: `YYYY-MM-DD-your-title.markdown` (e.g., `2023-10-17-microcontroller-tips.markdown`).

**Standard YAML Header**:
Every blog post **MUST** have this front matter:
```yaml
---
layout: post
title: "Your Descriptive Title"
date: YYYY-MM-DD HH:MM:SS
categories: ['Category1', 'Category2']
thumbnail: "/assets/images/thumbnails/your-image.webp" # Used for SEO & Cards
author: author-id-from-authors-yml
---
```
*   **SEO Benefit**: The layout automatically truncates the first 45 words of your post to create the social media description (`og:description`).
*   **Categories**: These power the "Explore Topics" filter on the blog page.

---

### 📂 2. Adding an Author
Adding an author is a two-step process to ensure dynamic linking.

**Step A: Update `_data/authors.yml`**
Add the author's metadata:
```yaml
- id: example-author
  name: Example Author
  image: /assets/images/authors/example.webp
  description: "Short professional bio of the author."
  linkedin: "https://linkedin.com/in/..."
```

**Step B: Create the Author Profile Page**
Create a new file: `author/example-author.markdown`.
```markdown
---
layout: author
author_id: example-author
description: "Same bio for SEO consistency."
permalink: /author/example-author/
---
```
This file is used by the `author.html` layout to list all posts by that author.

---

## ⚙️ YAML Configuration Hub
The site's global data is centralized in the `_data/` directory.

| File | Purpose |
| :--- | :--- |
| `authors.yml` | Central database for all blog contributors. |
| `navigation.yml` | Powers the header dropdowns and main menu. |
| `social.yml` | Global social media links used in the footer. |
| `expertise.yml` | Metadata for the technical expertise grids. |

---

## 🔍 Technical Implementation Details

### ⚡ Custom SEO Logic
Located in `_layouts/default.html`. We do not use a standard plugin because:
- **Blog Posts**: Pull the `thumbnail` image for social shares and truncate the post content for the description.
- **Pages**: Use their specific `description` field in the front matter.
- **Defaulting**: If no image is provided, it defaults to the company's large logo.

### 🎨 Design System
- **Tailwind CSS**: Custom color tokens (like `brand: #49A942`) are defined.
- **Alpine.js**: Used for the blog filtering system (`view: 'latest'\|'year'\|'topic'`), search modal, and mobile menu.
- **Markdown Rendering**: We use standard Markdown, but the blog layout supports standard HTML tags for complex elements like `<figure>` or `<h2>`.

---

## 🚀 Production Deployment
To generate a production-ready build with minified CSS:
1. Run Tailwind build: `npm run build`
2. Run Jekyll build: `bundle exec jekyll build`
3. Deploy the `_site/` directory.
