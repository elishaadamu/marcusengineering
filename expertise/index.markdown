layout: default
title: Our Expertise | Marcus Engineering Specialist Services
description: Explore our core engineering competencies including Analog/Mixed-Signal, Firmware, FPGA, PCB Design, and more.
---

<section class="py-32 bg-transparent">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="mx-auto max-w-2xl lg:text-center mb-24">
            <h2 class="text-base font-black leading-7 text-brand uppercase tracking-[0.3em] mb-4">Technical Mastery</h2>
            <p class="mt-2 text-4xl font-extrabold tracking-tight text-slate-900 sm:text-7xl font-display uppercase leading-none">Our <span class="text-brand">Expertise</span></p>
            <p class="mt-8 text-xl leading-8 text-slate-600 font-medium">
                Core competencies that define our engineering excellence. Precision, performance, and decades of experience.
            </p>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {% assign exp_nav = site.data.navigation | where: "title", "Expertise" | first %}
            {% for item in exp_nav.dropdown %}
            <a href="{{ item.url | relative_url }}" class="group relative flex flex-col items-start bg-white p-10 rounded-[2.5rem] border border-slate-200 hover:border-brand/40 hover:shadow-[0_0_50px_-12px_rgba(255,207,0,0.2)] transition-all duration-500">
                <div class="h-14 w-14 rounded-2xl bg-brand/10 text-brand flex items-center justify-center mb-10 group-hover:bg-brand group-hover:text-white transition-all duration-500 border border-brand/20">
                    <svg class="h-7 w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011-1v5m-4 0h4" /></svg>
                </div>
                <h3 class="text-2xl font-bold text-slate-900 group-hover:text-brand transition-colors font-display uppercase tracking-tighter mb-4 leading-tight">{{ item.title }}</h3>
                <p class="text-slate-500 leading-relaxed mb-10 font-medium">Deep domain knowledge and industry-leading specialized solutions in {{ item.title }}.</p>
                <span class="mt-auto text-[10px] font-black text-brand uppercase tracking-[0.2em] flex items-center gap-3 transition-all group-hover:gap-5">Explore Specialist <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" /></svg></span>
            </a>
            {% endfor %}
        </div>
    </div>
</section>
