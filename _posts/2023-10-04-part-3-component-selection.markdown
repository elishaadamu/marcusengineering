---
layout: post
title: "Part 3 - Component Selection"
date: 2023-10-04 15:37:32 
categories: ['Business', 'Electronics', 'Low Power Design Series', 'Uncategorized']
thumbnail: "/assets/images/thumbnails/PCB-Small-940x708.webp"
author: kyle-cerniglia
---

<!-- wp:heading -->
<h2><strong>Power Supply</strong></h2>
<!-- /wp:heading -->

<p>A consistent but highly efficient voltage regulator is crucial in power design. While there are many regulators to choose from, each comes with its own set of tradeoffs that must be accounted for.</p>

<!-- wp:heading -->
<h2><strong>Linear Regulators</strong></h2>
<!-- /wp:heading -->

<!-- wp:columns -->
<div class="wp-block-columns"><!-- wp:column {"verticalAlignment":"top","width":"100%"} -->
<div class="wp-block-column is-vertically-aligned-top" style="flex-basis:100%"><!-- wp:group -->
<div class="wp-block-group"><div class="wp-block-group__inner-container"><!-- wp:group -->
<div class="wp-block-group"><div class="wp-block-group__inner-container"><!-- wp:freeform -->
<p><img class="alignright" src="/assets/images/posts/image.webp" alt="This image has an empty alt attribute; its file name is image.png" width="166" height="167" /><span style="font-size: inherit;">Linear regulators may appear to be a low cost and cheap solution at first glance but are flawed by their inherent design. They act as a variable resistor at their base, wasting excess power in the form of heat. For an application that saves every microwatt of power, they are not a good selection for low power design. </span></p>
<p>If you require a stable voltage reference, consider using dedicated low power voltage reference modules, as opposed to a voltage regulator.</p>
<!-- /wp:freeform --></div></div>
<!-- /wp:group --></div></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:group -->
<div class="wp-block-group"><div class="wp-block-group__inner-container"><!-- wp:heading -->
<h2><strong>Switching Regulator</strong></h2>
<!-- /wp:heading --></div></div>
<!-- /wp:group -->

<p></p>

<!-- wp:paragraph -->
</p>
<p>Switching regulators can be used to produce highly efficient designs at the cost of increased circuit complexity. Typically, these devices require additional passive components to program the device and provide energy storage sources.</p>
<p>
<!-- /wp:paragraph -->

<!-- wp:group -->
<div class="wp-block-group"><div class="wp-block-group__inner-container"><!-- wp:group -->
<div class="wp-block-group"><div class="wp-block-group__inner-container"><!-- wp:group -->
<div class="wp-block-group"><div class="wp-block-group__inner-container"><!-- wp:group -->
<div class="wp-block-group"><div class="wp-block-group__inner-container"><!-- wp:paragraph {"align":"left"} -->
<p class="has-text-align-left"><img class="wp-image-6562 alignright" src="/assets/images/posts/image-1.webp" alt="">Not all switching regulators are created equal. While many are highly efficient at moderate or high loads, most will suffer from very low efficiency at currents below a few milliamps. A subset of these devices is designed with ultra-low power design in mind and efforts to reduce quiescent current and boost regulation efficiency at very low currents. Typically, the maximum current output will suffer as a tradeoff, ensuring your system peak currents are not violated. Otherwise, additional bulk capacitors will be needed to supply your capacity for instantaneous currents.</p>
<!-- /wp:paragraph --></div></div>
<!-- /wp:group --></div></div>
<!-- /wp:group --></div></div>
<!-- /wp:group --></div></div>
<!-- /wp:group -->

<p></p>

<!-- wp:heading -->
<h2><strong>Power Switches</strong></h2>
<!-- /wp:heading -->

<p>Typically, within a device, many circuits are left idling and unused at any given time, wasting precious power with their quiescent current consumption. Digital power switches and power supplied over I/O lines are the solution to this but could have unintended consequences.</p>
<p>Load switches can be used to disconnect ICs from various power rails on your device. In addition, many will allow you to switch voltages that are higher or lower than your logic voltage, enabling your processor to have full control over your power distribution. With proper selection, switches with standby currents of 10-100nA are possible. Considering that each of the devices you are disconnecting could have quiescent currents ranging in the microamps, this method can allow for substantial power savings.</p>
<p>An alternate method of power switching for designs with a single voltage level can achieve the same level of power savings with no additional components. Microcontroller I/O pins can be used to power devices directly instead of using a switch as a middleman.</p>
<p>Enabling and disabling power rails can be useful, but some careful design choices must be considered. Suppose you have a master and a slave device communicating over an I2C bus. Typically, the I2C lines are pulled high to VCC to allow for open-drain communication. Now consider the implications of removing power to the slave device while keeping the I2C bus pulled high. Depending on the internal design of your slave device, it could potentially attempt to source its power from the I2C lines! Not only would this defeat the purpose of the power switch, but it could cause the slave to have a brownout if it cannot source enough current from the bus. Options to combat this scenario are to have additional control over the bus pullup resistors, be it another external switch that supplies them or control internal pullups integral to your microcontroller.</p>

<!-- wp:heading -->
<h2><strong>Real-Time Clock</strong></h2>
<!-- /wp:heading -->

<p>Some battery-powered devices may require accurate timekeeping to timestamp records or trigger critical time-sensitive alarms. Many times, microcontrollers contain internal Real-Time Clocks (RTCs), which allow for easy implementation without adding more components. Typically only an external crystal and accompanying capacitors are required if a higher clock accuracy is needed.</p>
<p>Unfortunately, using this internal RTC may not be the best choice if you must trim every bit of power consumption possible. Looking at the datasheet for the PIC24FJ64GA202 microcontroller, the RTCC consumes an additional 1uA of power if enabled, regardless of whether it uses an internal crystal or an external crystal.</p>
<p>Another option is to use an external RTC optimized for low power consumption. The AB0815-T3 RTC is capable of operation currents as low as 55nA while using an external crystal. If accuracy can be sacrificed for power savings, its current consumption can drop to as low as 14nA when its internal oscillator is used without autocalibration. These RTC’s are usually packed with features, including external interrupt alarms to wake up other devices and general-purpose memory storage.</p>