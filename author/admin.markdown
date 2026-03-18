---
layout: default
title: Authors | Engineering Minds at Marcus Engineering
description: Meet the engineering experts and visionaries behind Marcus Engineering's technical insights and industrial innovations.
permalink: /author/admin/
---

<div class="authors-page-bg"></div>

<div class="authors-page-container">
    <div class="authors-page-header">
        <div class="inline-flex items-center gap-3 px-4 py-2 bg-brand/10 border border-brand/20 rounded-full mb-6">
            <span class="w-2 h-2 bg-brand rounded-full animate-pulse"></span>
            <span class="text-[10px] font-black text-brand uppercase tracking-[0.3em]">The Visionaries</span>
        </div>
        <h1 class="text-5xl md:text-7xl font-black text-slate-900 font-display uppercase tracking-tight leading-none">
            Meet Our <span class="text-brand">Authors</span>
        </h1>
        <div class="h-1 w-24 bg-brand mx-auto mt-8 rounded-full"></div>
    </div>

    <!-- Featured Leader Section -->
    {% assign all_authors = site.pages | where: "layout", "author" %}
    {% assign president = all_authors | where: "author_id", "patrick-marcus" | first %}
    {% if president %}
    <div class="featured-leader-section mb-20">
        <a href="{{ president.permalink | relative_url }}" class="author-card featured group transition-all duration-500 hover:border-brand/40 hover:shadow-2xl hover:shadow-brand/5" id="{{ president.author_id }}">
            <div class="author-image-wrapper">
                <div class="author-image-box">
                    <img src="{{ president.image | relative_url }}" alt="{{ president.title }}">
                </div>
            </div>
            <div class="author-info">
                <div class="flex items-center gap-4 mb-2">
                    <span class="px-3 py-1 bg-brand text-white text-[9px] font-black uppercase tracking-widest rounded-md">President</span>
                </div>
                <h2 class="author-name-title group-hover:text-brand transition-colors">About <span class="highlight-name">{{ president.title }}</span></h2>
                <div class="author-description line-clamp-3">
                    {% if president.content != "" %}
                    {{ president.content | markdownify }}
                    {% else %}
                    <p class="italic opacity-60">Team member profile pending...</p>
                    {% endif %}
                </div>
                
                <div class="mt-8 flex items-center justify-between">
                    <div class="author-social flex gap-4">
                        {% if president.linkedin and president.linkedin != "" and president.linkedin != "#" %}
                        <div  class="linkedin-link text-slate-400 hover:text-brand transition-colors">
                            <svg class="w-10 h-10 border rounded-xl p-2.5" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                        </div>
                        {% endif %}
                    </div>

                    <span class="inline-flex items-center gap-3 text-xs font-black uppercase tracking-[0.2em] text-brand group-hover:translate-x-3 transition-transform">
                        View Profile Articles
                        <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="3"><path stroke-linecap="round" stroke-linejoin="round" d="M13 7l5 5m0 0l-5 5m5-5H6" /></svg>
                    </span>
                </div>
            </div>
        </a>
    </div>
    {% endif %}

    <!-- Others Section -->
    <div class="authors-grid">
        {% assign others = all_authors | where_exp: "item", "item.author_id != 'patrick-marcus'" %}
        {% for author in others %}
        <a href="{{ author.permalink | relative_url }}" class="author-card group transition-all duration-500 hover:border-brand/40 hover:shadow-2xl hover:shadow-brand/5" id="{{ author.author_id }}">
            <div class="author-image-wrapper">
                <div class="author-image-box">
                    <img src="{{ author.image | relative_url }}" alt="{{ author.title }}">
                </div>
            </div>
            <div class="author-info">
                <h2 class="author-name-title group-hover:text-brand transition-colors">About <span class="highlight-name">{{ author.title }}</span></h2>
                <div class="author-description line-clamp-3">
                    {% if author.content != "" %}
                    {{ author.content | markdownify | truncatewords: 30 }}
                    {% else %}
                    <p class="italic opacity-60">Team member profile pending...</p>
                    {% endif %}
                </div>
                
                <div class="mt-6 flex items-center justify-between">
                    <div class="author-social flex gap-4">
                        {% if author.linkedin and author.linkedin != "" and author.linkedin != "#" %}
                        <div class="linkedin-link text-slate-400 hover:text-brand transition-colors">
                            <svg class="w-8 h-8 border rounded-lg p-2" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                        </div>
                        {% endif %}
                    </div>
                    
                    <span class="inline-flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-brand group-hover:translate-x-2 transition-transform">
                        View Articles
                        <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="3"><path stroke-linecap="round" stroke-linejoin="round" d="M13 7l5 5m0 0l-5 5m5-5H6" /></svg>
                    </span>
                </div>
            </div>
        </a>
        {% endfor %}
    </div>
</div>
