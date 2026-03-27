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
*   **Output File**: `assets/css/main.css`

### 2. Jekyll Preview Server (Ruby)
This hosts the site. The Admin Panel is built into this process.
From the project root:
```bash
bundle exec jekyll serve
```
*   **Main Site**: `http://localhost:4000`
*   **Admin Panel**: `http://localhost:4000/admin`

---

## 🎨 Professional Design System (Recent Updates)

The site features a premium, modern B2B engineering aesthetic built for precision and trust.

### 1. Reusable Grid Infrastructure
To ensure visual consistency and code efficiency, we use the `listing-grid` layout for all major service-related directories:
*   **Pages**: `expertise/`, `industries/`, `applications/`.
*   **Mechanism**: These pages now only contain metadata (titles, icons, and navigation keys). The layout handles all complex styling, background patterns, and grid logic.

### 2. Interactive Components
*   **Animated Hero**: Features a dynamic typing animation that cycles through core services and specializations.
*   **Performance-Aware Video**: The hero video uses an `IntersectionObserver` to pause when off-screen and resume instantly when visible, conserving user CPU/Battery.
*   **Smart Testimonials**: 
    *   **Mobile-First**: Supports natural touch-drag (swipe) gestures.
    *   **75/25 Desktop Split**: Optimized wide-screen layout that balances testimonial text with high-impact partner logos.
    *   **Autoplay**: Automatically cycles through clients but pauses when the user hovers or scrolls away.

### 3. Visual Language
*   **Signature Grid**: Every major section (Hero, Trusted, Expertise, Bring) uses the **Square Grid** background to reinforce the engineering discipline.
*   **Premium Cards**: Cards use semi-transparent glassmorphism (`backdrop-blur`), subtle brand-colored orbs for depth, and large decorative SVG watermarks.

---

## 📝 Content Management Guide

### 📂 1. Adding a Blog Post
Blog posts go in the `_posts/` directory.
**Standard YAML Header**:
```yaml
---
layout: post
title: "Your Descriptive Title"
date: YYYY-MM-DD HH:MM:SS
categories: ['Category1', 'Category2']
thumbnail: "/assets/images/thumbnails/your-image.webp" 
author: author-id-from-authors-yml
---
```

### 📂 2. Adding an Author
Authors are no longer managed in a central YAML database. To add a new author:
1.  **Create Profile**: Create a new file in `author/author-id.markdown`.
2.  **Define Frontmatter**: Include `author_id`, `title`, `image`, and `linkedin`.
3.  **Content**: Place the author's biography directly in the body of the Markdown file.
4.  **Auto-Integration**: The site automatically maps blog posts to authors via the `author_id` field.

---

## ⚙️ YAML Configuration Hub
The site's global data is centralized in the `_data/` directory.

| File | Purpose |
| :--- | :--- |
| `navigation.yml` | Powers the header dropdowns and main menu. |
| `hero.yml` | Controls hero video, typing lines, and CTA buttons. |
| `testimonials.yml` | Database of client feedback, logos, and authors. |
| `social.yml` | Global social media links used in the footer. |
| `blog_section.yml` | Controls heading and button labels for the home page blog grid. |

---

## ⚙️ Recent Refinements (March 2026)

### 🧪 Hybrid Script Handling (Jekyll + JS)
To resolve "Declaration or statement expected" errors caused by Liquid tags inside `<script>` blocks, we now use **String Wrapping**:
- **Logic**: `const value = parseInt('{{ jekyll.variable }}') || 0;`
- **Benefit**: Prevents IDE/Linter confusion while maintaining dynamic functionality.

### 🎭 Responsive Enhancements
- **Dynamic Blogs**: The home page `blog-section.html` now supports specific author filtering (e.g., Patrick Marcus) with a strictly enforced 3-post limit using `limit: 3` in the Liquid loop.
- **Tactile Buttons**: Responsive "Read Insights" buttons use scaling fonts (`text-[9px]` to `11px`) and hover-staggered icons to improve mobile UX.

---

## 🌐 Hosting & BaseURL Configuration

The site is configured to handle different deployment environments (e.g., GitHub Pages subdirectories vs. Custom Domains) using Jekyll's `baseurl` and `relative_url` systems.

### 1. GitHub Pages (Subdirectory)
If hosting at `https://marcus-engineering.github.io/marcusengineering.com/`:
- **`_config.yml`**:
  ```yaml
  baseurl: "/marcusengineering.com"
  url: "https://marcus-engineering.github.io"
  ```

### 2. Custom Domain (TLD)
If hosting at `https://www.marcusengineering.com/`:
- **`_config.yml`**:
  ```yaml
  baseurl: ""
  url: "https://www.marcusengineering.com"
  ```

### 🛠 Implementation Rule
**Never hardcode absolute paths** like `<a href="/about/">`. Always use the `relative_url` filter:
- **HTML**: `<a href="{{ "/about/" | relative_url }}">`
- **Images**: `<img src="{{ "/assets/logo.png" | relative_url }}">`

This ensures all CSS, JS, and image links resolve correctly regardless of the hosting environment.

---

## 🚀 Production Deployment
1. Run Tailwind build: `npm run build`
2. Run Jekyll build: `bundle exec jekyll build`
3. Deploy the `_site/` directory.
