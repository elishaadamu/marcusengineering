---
layout: default
title: Success | Marcus Engineering
description: Your message has been successfully sent to Marcus Engineering.
mouse_effect: true
---

<section class="min-h-[80vh] flex items-center justify-center relative overflow-hidden py-32">
    <!-- Success Particle Background (Static version of the mouse effect) -->
    <div class="absolute inset-0 -z-10 opacity-30">
        <div class="absolute inset-0 bg-dotted-grid pointer-events-none"></div>
    </div>

    <div class="max-w-3xl mx-auto px-6 text-center relative z-10">
        <!-- Glowing Success Icon -->
        <div class="mb-12 relative inline-block group">
            <div class="absolute inset-0 bg-brand/20 blur-3xl rounded-full animate-pulse group-hover:bg-brand/40 transition-all duration-1000"></div>
            <div class="relative h-32 w-32 rounded-full bg-white border border-brand/20 shadow-2xl flex items-center justify-center">
                <svg class="h-16 w-16 text-brand" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
                </svg>
            </div>
            <!-- Smaller floating orbs -->
            <div class="absolute -top-4 -right-4 h-8 w-8 bg-emerald-400/20 blur-xl rounded-full animate-bounce"></div>
            <div class="absolute -bottom-6 -left-8 h-12 w-12 bg-brand/10 blur-xl rounded-full animate-pulse" style="animation-delay: 1s;"></div>
        </div>

        <h1 class="text-5xl font-extrabold text-slate-900 font-display uppercase tracking-tight sm:text-7xl mb-8 leading-none">
            Mission <span class="text-brand">Accomplished</span>
        </h1>
        
        <p class="text-xl text-slate-600 mb-12 font-medium max-w-xl mx-auto leading-relaxed">
            Your message has been successfully transmitted. Our engineering team is reviewing your inquiry and will be in contact shortly.
        </p>

        <div class="flex flex-col sm:flex-row items-center justify-center gap-6">
            <a href="{{ '/' | relative_url }}" class="btn btn-primary min-w-[200px]">
                Return Home
            </a>
            <a href="{{ '/blog/' | relative_url }}" class="btn btn-secondary min-w-[200px]">
                Read Insights
            </a>
        </div>
        
        <!-- System ID / Confirmation Footer -->
        <div class="mt-24 pt-8 border-t border-slate-100">
            <p class="text-[10px] font-black uppercase tracking-[0.5em] text-slate-300">
                System Status: Online | Reference: {{ "now" | date: "%Y%m%d%H%M" }}
            </p>
        </div>
    </div>
</section>
