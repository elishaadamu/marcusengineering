---
layout: post
title: "Part 4 - Microcontroller Tips"
date: 2023-10-17 14:20:36 
categories: ['Electronics', 'Business', 'Low Power Design Series']
thumbnail: "/assets/images/thumbnails/part4.webp"
author: kyle-cerniglia
---

<!-- wp:heading -->
<h2>Power Reduction Modes</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>On many microcontrollers (MCU), there will be a selection of low-power modes to choose from. Some may be more appealing than others, but careful consideration must be made on power consumption sources and the speed at which modules may resume operation. Do note that not all of these power reduction modes are available for all MCUs. Care should be taken for the initial parts selection to ensure that you have the features that you may need down the road.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6586,"sizeSlug":"large","linkDestination":"none","className":"is-style-default"} -->
<figure class="wp-block-image size-large is-style-default"><img src="/assets/images/posts/image-3-550x380.webp" alt="" class="wp-image-6586"/></figure>
<!-- /wp:image -->

<!-- wp:heading -->
<h2>Doze Mode</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Doze mode will reduce the clock multiplier on the CPU core, thus decreasing the processor's power consumption and speed. This is useful if you need the core activities to handle a less important task but can afford a lower processing speed. This is also useful if you need to maintain full clock speed for the system peripherals.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Idle Mode</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Idle mode is similar to doze mode, where the peripheral clock still functions. However, the clock to the core ceases to operate. This is useful for saving core power while waiting for an external or peripheral interrupt to fire. Since the CPU merely is idling, the processor may resume operation immediately upon an interrupt.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Sleep Mode</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Sleep mode drastically reduces power consumption by halting the system clock, effectively shutting down the CPU core and most peripheral functions. Interrupts, pin-change interrupts, and some externally clocked peripherals will typically still be functional. The tradeoff between this and Idle mode is that sleep mode takes a more extended amount of time to exit upon receiving an interrupt wakeup due to the system clock's startup time.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Deep Sleep Mode</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Deep Sleep mode is the lowest operating mode that some MCUs have to offer. Like Sleep mode, the system clock is shut down, but power is also severed from additional systems, most notably SRAM. When the processor wakes, it will resume operation as if a Power-On Reset had occurred, all temporary data stored in SRAM will be lost. Some MCUs, including the PIC24FJ64GA202, keep a limited number of general-purpose registers powered during deep sleep mode, enough to allow the software to set custom flags to alert itself as to what has happened before entering Deep Sleep.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Processor Startup and Crystal Selection</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>At first glance, crystal selection choice may seem simple: pick higher speeds for maximum performance and slower speeds for power savings. However, once you dig into the issue further, the answer is not linear.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Constant Operation</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>For applications involving the MCU core's continuous operation, the most straightforward answer to this problem is to look at the power consumption in terms of uA/MHz. The lower the number, the higher your efficiency. </p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":6585,"sizeSlug":"large","linkDestination":"none","className":"is-style-default"} -->
<figure class="wp-block-image size-large is-style-default"><img src="/assets/images/posts/image-2-550x313.webp" alt="" class="wp-image-6585"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>For example, we can see the maximum current consumption for different operating modes by pulling data from Tables 32-4 of the PIC24FJ64GA202 datasheet. Assuming that we are operating at +25°C and 3.3V, we can see that if a 31kHz crystal is used, the MCU is consuming 2580uA/MHz. Let's instead look at the highest speed clock usable, 32MHz. With this crystal, the PIC is consuming only 237.5uA/MHz.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>After seeing this data, if you expect your processor to be active a significant amount of the time the system is powered, a faster clock speed is actually more power efficient. The system enters a power-saving mode while the processor is not in use. But let's say that you need the processor to be always available to process small amounts of data immediately. In this case, it would be better to use a slower clock speed if you cannot utilize power-saving modes.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Cycled Operation</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Some designs will involve an MCU that spends most of its time in sleep mode, wakes up at regular intervals to complete a task, or takes a measurement. In this scenario, another issue comes into effect; startup times.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>When a microcontroller turns on or wakes from a sleep mode, a certain amount of time is spent powering up system clocks and waiting for them to stabilize. Generally, the slower that a clock source is, the longer it will take to stabilize. While the system is starting up, it will typically consume power at levels matching a fully active CPU at its given clock speed. While this does not affect designs that continuously stay, it can consume a considerable amount of your power budget if the power-on time is a significant portion of your total active time. While this will vary wildly from application to application, the total power consumed by a device needs to be carefully analyzed to find a clock speed that best balances a fast startup time without consuming too much power in the process. For one low power design, this was experimentally determined to be 8MHz, out of a range of 31kHz-32MHz, but it will change for every application.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Peripheral Selection</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Another powerful tool at your disposal is the ability to enable and disable the system clock to specific peripherals on many MCUs. Your design will frequently have a long list of unused peripherals that simply idle, wasting power while the processor is active. By disabling these new peripherals, 32.4uA of wasted active current was reduced from the design. Peripherals that typically have high current consumption include ADC and serial modules.</p>
<!-- /wp:paragraph -->
