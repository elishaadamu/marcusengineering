---
layout: default
title: Industries Served | Marcus Engineering Design Expertise
description: Marcus Engineering provides specialized engineering for Medical Devices, Aerospace, Defense, Energy, Solar, and Industrial Automation.
---

<section class="py-32 bg-transparent">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="mx-auto max-w-2xl lg:text-center mb-24">
            <h2 class="text-base font-black leading-7 text-brand uppercase tracking-[0.3em] mb-4">Specialized Engineering</h2>
            <p class="mt-2 text-4xl font-extrabold tracking-tight text-slate-900 sm:text-7xl font-display uppercase leading-none">Industries We <span class="text-brand">Serve</span></p>
            <p class="mt-8 text-xl leading-8 text-slate-600 font-medium">
                We bring deep technical expertise to complex industries, ensuring compliance, reliability, and innovation in every project.
            </p>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {% assign industry_nav = site.data.navigation | where: "title", "Industries" | first %}
            {% for item in industry_nav.dropdown %}
            <a href="{{ item.url | relative_url }}" class="group relative flex flex-col items-start bg-white p-10 rounded-[2.5rem] border border-slate-200 hover:border-brand/40 hover:shadow-[0_0_50px_-12px_rgba(255,207,0,0.2)] transition-all duration-500">
                <div class="h-14 w-14 rounded-2xl bg-brand/10 text-brand flex items-center justify-center mb-10 group-hover:bg-brand group-hover:text-white transition-all duration-500 border border-brand/20">
                    <svg class="h-7 w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>
                </div>
                <h3 class="text-2xl font-bold text-slate-900 group-hover:text-brand transition-colors font-display uppercase tracking-tighter mb-4 leading-tight">{{ item.title }}</h3>
                <p class="text-slate-500 leading-relaxed mb-10 font-medium">Engineering specialized and high-reliability solutions for the leading {{ item.title }} sector.</p>
                <span class="mt-auto text-[10px] font-black text-brand uppercase tracking-[0.2em] flex items-center gap-3 transition-all group-hover:gap-5">Explore Sector <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" /></svg></span>
            </a>
            {% endfor %}
        </div>
    </div>
</section>
