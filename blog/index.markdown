---
layout: default
title: Engineering Insights Blog | Marcus Engineering Lab
description: Technical deep dives, project updates, and engineering news from the Marcus Engineering team. Stay informed on AI, embedded systems, and hardware design.
pagination: 
  enabled: true
---

<div x-data="{ view: 'latest' }">
    <!-- Simple Static Header -->
    <section class="pt-40 pb-20 bg-white border-b border-slate-100">
        <div class="mx-auto max-w-7xl px-6 lg:px-8">
            <div class="mx-auto max-w-3xl lg:text-center">
                <h2 class="text-xs font-black leading-7 text-brand uppercase tracking-[0.4em] mb-6">Innovation Lab</h2>
                <p class="text-4xl font-extrabold tracking-tight text-slate-900 sm:text-6xl font-display uppercase leading-none mb-8">Engineering <span class="text-brand">Insights</span></p>
                <div class="h-1 w-20 bg-brand mx-auto mb-8"></div>
                <p class="text-lg leading-8 text-slate-500 font-medium">
                    A decade of engineering knowledge, project updates, and technical deep dives from the Marcus Engineering team.
                </p>
            </div>
        </div>
    </section>

    <section class="pb-32 bg-transparent">
        <div class="mx-auto max-w-7xl px-6 lg:px-8">
            <!-- Blog Filter Navigation -->
            <div class="blog-filter-tabs">
                <button @click="view = 'latest'" :class="{ 'active': view === 'latest' }" class="filter-tab">Latest Entries</button>
                <button @click="view = 'year'" :class="{ 'active': view === 'year' }" class="filter-tab">Browse by Year</button>
                <button @click="view = 'topic'" :class="{ 'active': view === 'topic' }" class="filter-tab">Explore Topics</button>
            </div>

            <!-- LATEST VIEW (Default Cards) -->
            <div x-show="view === 'latest'" x-transition:enter="transition-opacity duration-300" x-transition:enter-start="opacity-0" x-transition:enter-end="opacity-100">
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    {% for post in paginator.posts %}
                        {% include post-card.html post=post %}
                    {% endfor %}
                </div>
                
                <!-- Minimal Pagination -->
                {% if paginator.total_pages > 1 %}
                <nav class="blog-pagination" aria-label="Pagination">
                    <div class="pagination-container">
                        {% if paginator.previous_page %}
                            <a href="{{ paginator.previous_page_path | relative_url }}" class="pagination-btn">
                                <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M12.79 5.23a.75.75 0 01-.02 1.06L8.832 10l3.938 3.71a.75.75 0 11-1.04 1.08l-4.25-4a.75.75 0 010-1.08l4.25-4a.75.75 0 011.06.02z" clip-rule="evenodd" /></svg>
                            </a>
                        {% endif %}

                        {% for trail in paginator.page_trail %}
                            <a href="{{ trail.path | relative_url }}" class="pagination-number {% if paginator.page == trail.num %}active{% endif %}">
                                {{ trail.num }}
                            </a>
                        {% endfor %}

                        {% if paginator.next_page %}
                            <a href="{{ paginator.next_page_path | relative_url }}" class="pagination-btn">
                                <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M7.21 14.77a.75.75 0 01.02-1.06L11.168 10 7.23 6.29a.75.75 0 111.04-1.08l4.25 4a.75.75 0 010 1.08l-4.25 4a.75.75 0 01-1.06-.02z" clip-rule="evenodd" /></svg>
                            </a>
                        {% endif %}
                    </div>
                </nav>
                {% endif %}
            </div>

            <!-- BY YEAR VIEW (List) -->
            <div x-show="view === 'year'" x-cloak x-transition:enter="transition-opacity duration-300" x-transition:enter-start="opacity-0" x-transition:enter-end="opacity-100">
                {% assign postsByYear = site.posts | group_by_exp: "post", "post.date | date: '%Y'" %}
                
                <!-- Year Selector Dropdown -->
                <div class="year-selector-wrap">
                    <span class="year-selector-label">Jump to:</span>
                    <select class="year-select" @change="document.getElementById('year-' + $event.target.value).scrollIntoView({ behavior: 'smooth' })">
                        <option value="" disabled selected>Select Year</option>
                        {% for year in postsByYear %}
                            <option value="{{ year.name }}">{{ year.name }}</option>
                        {% endfor %}
                    </select>
                </div>

                {% for year in postsByYear %}
                    <div class="year-header mt-24 mb-12" id="year-{{ year.name }}">
                        <h2>{{ year.name }}</h2>
                        <span>Vault / {{ year.name }}</span>
                    </div>
                    <div class="blog-list-container">
                        {% for post in year.items %}
                            <div class="blog-list-item">
                                <div class="blog-list-date">
                                    {{ post.date | date: "%B %d" }}
                                </div>
                                <div class="blog-list-content">
                                    <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
                                    <p class="blog-list-description">{{ post.excerpt | strip_html | truncate: 200 }}</p>
                                    <div class="blog-list-meta">
                                        <span class="meta-label">Category:</span>
                                        {% for cat in post.categories %}
                                            <span class="meta-pill">{{ cat }}</span>
                                        {% endfor %}
                                        {% if post.tags.size > 0 %}
                                            <span class="meta-label ml-4">Tags:</span>
                                            {% for tag in post.tags %}
                                                <span class="meta-pill">{{ tag }}</span>
                                            {% endfor %}
                                        {% endif %}
                                    </div>
                                </div>
                            </div>
                        {% endfor %}
                    </div>
                {% endfor %}
            </div>

            <!-- BY TOPIC VIEW (List) -->
            <div x-show="view === 'topic'" x-cloak x-transition:enter="transition-opacity duration-300" x-transition:enter-start="opacity-0" x-transition:enter-end="opacity-100">
                <div class="year-header mt-24 mb-12">
                    <h2>Topics</h2>
                    <span>Archive / Categorized</span>
                </div>
                
                {% assign categories = site.categories %}
                <div class="space-y-20">
                    {% for category in categories %}
                        <div class="py-12">
                            <h3 class="text-2xl font-black text-slate-800 uppercase tracking-tight mb-8 border-l-4 border-brand pl-6">
                                {{ category[0] }}
                            </h3>
                            <div class="blog-list-container">
                                {% for post in category[1] %}
                                    <div class="blog-list-item">
                                        <div class="blog-list-date">{{ post.date | date: "%Y" }}</div>
                                        <div class="blog-list-content">
                                            <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
                                            <p class="blog-list-description">{{ post.excerpt | strip_html | truncate: 160 }}</p>
                                            <div class="blog-list-meta">
                                                <span class="meta-label">Tags:</span>
                                                {% for tag in post.tags %}
                                                    <span class="meta-pill">{{ tag }}</span>
                                                {% endfor %}
                                            </div>
                                        </div>
                                    </div>
                                {% endfor %}
                            </div>
                        </div>
                    {% endfor %}
                </div>
            </div>

            {% if site.posts.size == 0 %}
                <div class="text-center py-32">
                    <p class="text-slate-400 font-display uppercase tracking-widest text-sm">No engineering insights found.</p>
                </div>
            {% endif %}
        </div>
    </section>
</div>
