---
layout: default
title: Engineering Insights Blog | Marcus Engineering Lab
description: Technical deep dives, project updates, and engineering news from the Marcus Engineering team. Stay informed on AI, embedded systems, and hardware design.
pagination: 
  enabled: true
---

<section class="py-32 bg-transparent min-h-screen">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="mx-auto max-w-2xl lg:text-center mb-24">
            <h2 class="text-base font-black leading-7 text-brand uppercase tracking-[0.3em] mb-4">Innovation Lab</h2>
            <p class="mt-2 text-4xl font-extrabold tracking-tight text-slate-900 sm:text-7xl font-display uppercase leading-none">Engineering <span class="text-brand">News</span></p>
            <p class="mt-8 text-xl leading-8 text-slate-600 font-medium">
                A decade of engineering knowledge, project updates, and technical deep dives from the Marcus Engineering team.
            </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {% for post in paginator.posts %}
                {% include post-card.html post=post %}
            {% endfor %}
        </div>
        
        <!-- Premium Responsive Pagination -->
        {% if paginator.total_pages > 1 %}
        <nav class="blog-pagination" aria-label="Pagination">
            <div class="pagination-container">
                {% if paginator.previous_page %}
                    <a href="{{ paginator.previous_page_path | relative_url }}" class="pagination-btn prev" title="Previous Page">
                        <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M12.79 5.23a.75.75 0 01-.02 1.06L8.832 10l3.938 3.71a.75.75 0 11-1.04 1.08l-4.25-4a.75.75 0 010-1.08l4.25-4a.75.75 0 011.06.02z" clip-rule="evenodd" /></svg>
                    </a>
                {% else %}
                    <div class="pagination-btn disabled">
                        <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M12.79 5.23a.75.75 0 01-.02 1.06L8.832 10l3.938 3.71a.75.75 0 11-1.04 1.08l-4.25-4a.75.75 0 010-1.08l4.25-4a.75.75 0 011.06.02z" clip-rule="evenodd" /></svg>
                    </div>
                {% endif %}

                <div class="pagination-numbers">
                    {% for trail in paginator.page_trail %}
                        <a href="{{ trail.path | relative_url }}" 
                           class="pagination-number {% if paginator.page == trail.num %}active{% endif %}"
                           {% if paginator.page == trail.num %}aria-current="page"{% endif %}>
                            {{ trail.num }}
                            {% if paginator.page == trail.num %}
                                <span class="pagination-active-dot"></span>
                            {% endif %}
                        </a>
                    {% endfor %}
                </div>

                {% if paginator.next_page %}
                    <a href="{{ paginator.next_page_path | relative_url }}" class="pagination-btn next" title="Next Page">
                        <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M7.21 14.77a.75.75 0 01.02-1.06L11.168 10 7.23 6.29a.75.75 0 111.04-1.08l4.25 4a.75.75 0 010 1.08l-4.25 4a.75.75 0 01-1.06-.02z" clip-rule="evenodd" /></svg>
                    </a>
                {% else %}
                    <div class="pagination-btn disabled">
                        <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M7.21 14.77a.75.75 0 01.02-1.06L11.168 10 7.23 6.29a.75.75 0 111.04-1.08l4.25 4a.75.75 0 010 1.08l-4.25 4a.75.75 0 01-1.06-.02z" clip-rule="evenodd" /></svg>
                    </div>
                {% endif %}
            </div>

            <!-- Enhanced Status Indicator -->
            <div class="pagination-status">
                <div class="pagination-line"></div>
                <div class="pagination-label">
                    <span>Section</span>
                    <span class="current">{{ paginator.page }}</span>
                    <span>/</span>
                    <span class="total">{{ paginator.total_pages }}</span>
                </div>
                <div class="pagination-line"></div>
            </div>
        </nav>
        {% endif %}
        
        {% if site.posts.size == 0 %}
            <div class="text-center py-32 bg-white rounded-[2.5rem] border border-dashed border-slate-200">
                <p class="text-slate-500 font-display uppercase tracking-widest text-sm">No insights found. Engineering lab is busy...</p>
            </div>
        {% endif %}
    </div>
</section>
