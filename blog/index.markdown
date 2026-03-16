---
layout: default
title: Engineering Insights Blog | Marcus Engineering Lab
description: Technical deep dives, project updates, and engineering news from the Marcus Engineering team. Stay informed on AI, embedded systems, and hardware design.
image: /assets/images/marketing folder/insightmedi-app-medical_t20_LQy1aY.webp
pagination: 
  enabled: true
---

<div x-data="{ view: 'latest' }">
    <!-- Premium Image Hero -->
    <section class="relative pt-20 flex items-center min-h-screen overflow-hidden bg-slate-900 border-b border-brand/20">
        <!-- Background Image with Overlay -->
        <div class="absolute inset-0 z-0">
            <img src="{{ page.image | relative_url }}" 
                 alt="Medical Engineering Insight" 
                 class="w-full h-full object-cover opacity-60">
            <div class="absolute inset-0 bg-slate-900/30 backdrop-blur-[2px]"></div>
        </div>

        <div class="relative z-10 mx-auto max-w-7xl px-6 lg:px-8 w-full">
            <div class="mx-auto max-w-3xl lg:text-center">
                <h2 class="text-xs font-black leading-7 text-brand uppercase tracking-[0.5em] mb-6">Innovation Lab</h2>
                <p class="text-4xl font-extrabold tracking-tight text-white sm:text-7xl font-display uppercase leading-none mb-8">
                    Engineering <span class="text-brand">Insights</span>
                </p>
                <div class="h-1.5 w-24 bg-brand mx-auto mb-10"></div>
                <p class="text-xl leading-8 text-white font-medium drop-shadow-sm">
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
                <div class="grid grid-cols-1 lg:grid-cols-[1fr_320px] gap-12">
                    <!-- Main Content -->
                    <div class="space-y-12">
                        <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-8">
                            {% for post in paginator.posts %}
                                {% include post-card.html post=post %}
                            {% endfor %}
                        </div>

                        <!-- Minimal Pagination -->
                        {% if paginator.total_pages > 1 %}
                        <nav class="blog-pagination mt-12! pt-8!" aria-label="Pagination">
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

                    <!-- Sidebar -->
                    <aside class="space-y-12">
                        <!-- Recent Posts -->
                        <div>
                            <h4 class="text-xs font-black text-slate-400 uppercase tracking-[0.3em] mb-8 flex items-center gap-4">
                                Recent Insights
                                <span class="h-px flex-1 bg-slate-100"></span>
                            </h4>
                            <div class="space-y-6">
                                {% for recent in site.posts limit:5 %}
                                    <a href="{{ recent.url | relative_url }}" class="group flex items-start gap-4">
                                        <div class="shrink-0 w-12 h-12 rounded-xl bg-slate-100 overflow-hidden">
                                            {% assign recent_image = recent.thumbnail | default: recent.image %}
                                            {% if recent_image %}
                                                <img src="{{ recent_image | relative_url }}" class="w-full h-full object-cover transition-transform group-hover:scale-110">
                                            {% endif %}
                                        </div>
                                        <div class="flex-1">
                                            <span class="text-[9px] font-black text-brand uppercase tracking-wider mb-1 block">{{ recent.date | date: "%b %d, %Y" }}</span>
                                            <h5 class="text-xs font-bold text-slate-900 group-hover:text-brand transition-colors leading-tight">{{ recent.title }}</h5>
                                        </div>
                                    </a>
                                {% endfor %}
                            </div>
                        </div>

                        <!-- Categories -->
                        <div>
                            <h4 class="text-xs font-black text-slate-400 uppercase tracking-[0.3em] mb-8 flex items-center gap-4">
                                Categories
                                <span class="h-px flex-1 bg-slate-100"></span>
                            </h4>
                            <div class="flex flex-wrap gap-2">
                                {% assign categories = site.categories | sort %}
                                {% for category in categories %}
                                    <a href="{{ '/category/' | append: (category[0] | slugify) | append: '/' | relative_url }}" 
                                            class="px-4 py-2 bg-slate-50 hover:bg-brand hover:text-white rounded-lg text-[10px] font-bold text-slate-600 transition-all uppercase tracking-wider">
                                        {{ category[0] }}
                                    </a>
                                {% endfor %}
                            </div>
                        </div>

                        <!-- Tags Cloud -->
                        <div>
                            <h4 class="text-xs font-black text-slate-400 uppercase tracking-[0.3em] mb-8 flex items-center gap-4">
                                Popular Tags
                                <span class="h-px flex-1 bg-slate-100"></span>
                            </h4>
                            <div class="flex flex-wrap gap-x-4 gap-y-2">
                                {% assign tags = site.tags | sort %}
                                {% for tag in tags limit:20 %}
                                    <span class="text-[10px] font-medium text-slate-400 hover:text-brand cursor-default">#{{ tag[0] | upcase }}</span>
                                {% endfor %}
                            </div>
                        </div>
                    </aside>
                </div>
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
                    <div class="year-header mt-12 mb-12" id="year-{{ year.name }}">
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
                <div class="year-header mt-12 mb-12">
                    <h2>Topics</h2>
                    <span>Archive / Categorized</span>
                </div>

                {% assign categories = site.categories %}
                
                <!-- Topic Selector Dropdown -->
                <div class="year-selector-wrap">
                    <span class="year-selector-label">Jump to Topic:</span>
                    <select class="year-select" @change="const el = document.getElementById('topic-' + $event.target.value.toLowerCase().replace(/[^a-z0-0]/g, '-')); if(el) el.scrollIntoView({ behavior: 'smooth' })">
                        <option value="" disabled selected>Select Topic</option>
                        {% for category in categories %}
                            <option value="{{ category[0] }}">{{ category[0] }}</option>
                        {% endfor %}
                    </select>
                </div>
                
                <div class="space-y-20">
                    {% for category in categories %}
                        <div class="py-12 topic-section" id="topic-{{ category[0] | slugify }}">
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
                                                <a href="{{ '/category/' | append: (category[0] | slugify) | append: '/' | relative_url }}" class="ml-auto text-[10px] font-black text-brand uppercase tracking-widest hover:underline">View All {{ category[0] }}</a>
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
