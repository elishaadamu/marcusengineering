---
layout: default
title: Authors
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
    {% assign president = site.data.authors | where: "id", "patrick-marcus" | first %}
    {% if president %}
    <div class="featured-leader-section mb-20">
        <div class="author-card featured" id="{{ president.id }}">
            <div class="author-image-wrapper">
                <div class="author-image-box">
                    <img src="{{ president.image | relative_url }}" alt="{{ president.name }}">
                </div>
            </div>
            <div class="author-info">
                <div class="flex items-center gap-4 mb-2">
                    <span class="px-3 py-1 bg-brand text-white text-[9px] font-black uppercase tracking-widest rounded-md">President</span>
                </div>
                <h2 class="author-name-title">About <span class="highlight-name">{{ president.name }}</span></h2>
                <div class="author-description">
                    {% if president.description != "" %}
                    <p>{{ president.description }}</p>
                    {% else %}
                    <p class="italic opacity-60">Team member profile pending...</p>
                    {% endif %}
                </div>
                <div class="author-social flex gap-4">
                    {% if president.linkedin and president.linkedin != "" and president.linkedin != "#" %}
                    <a href="{{ president.linkedin }}" class="linkedin-link" target="_blank" title="LinkedIn Profile">
                        <svg class="w-10 h-10 border rounded-xl p-2.5" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                    </a>
                    {% endif %}
                </div>
            </div>
        </div>
    </div>
    {% endif %}

    <!-- Others Section -->
    <div class="authors-grid">
        {% assign others = site.data.authors | where_exp: "item", "item.id != 'patrick-marcus'" %}
        {% for author in others %}
        <div class="author-card" id="{{ author.id }}">
            <div class="author-image-wrapper">
                <div class="author-image-box">
                    <img src="{{ author.image | relative_url }}" alt="{{ author.name }}">
                </div>
            </div>
            <div class="author-info">
                <h2 class="author-name-title">About <span class="highlight-name">{{ author.name }}</span></h2>
                <div class="author-description">
                    {% if author.description != "" %}
                    <p>{{ author.description }}</p>
                    {% else %}
                    <p class="italic opacity-60">Team member profile pending...</p>
                    {% endif %}
                </div>
                <div class="author-social flex gap-4">
                    {% if author.linkedin and author.linkedin != "" and author.linkedin != "#" %}
                    <a href="{{ author.linkedin }}" class="linkedin-link" target="_blank" title="LinkedIn Profile">
                        <svg class="w-10 h-10 border rounded-xl p-2.5" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                    </a>
                    {% endif %}
                    {% if author.twitter and author.twitter != "" and author.twitter != "#" %}
                    <a href="{{ author.twitter }}" class="twitter-link" target="_blank" title="Twitter Profile">
                        <svg class="w-10 h-10 border rounded-xl p-2.5" fill="currentColor" viewBox="0 0 24 24"><path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"/></svg>
                    </a>
                    {% endif %}
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
</div>
