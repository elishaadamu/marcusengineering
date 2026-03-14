---
layout: post
title: "Part 2 – Low Power Design Battery Limitations"
date: 2023-09-07 15:36:38 
categories: ['Electronics', 'Engineering', 'Low Power Design Series']
permalink: /part-2-low-power-design-battery-limitations/
thumbnail: ""
---

<!-- wp:paragraph {"align":"left","fontSize":"medium"} -->
<p class="has-text-align-left has-medium-font-size"><strong>Battery Chemistries </strong></p>
<!-- /wp:paragraph -->

<!-- wp:group -->
<div class="wp-block-group"><div class="wp-block-group__inner-container"><!-- wp:paragraph {"align":"left"} -->
<p class="has-text-align-left">When searching for a battery for an application, a myriad of choices are at your feet. One of the first choices is battery chemistry. The question you must ask is, after consideration of your challenging requirements, what option is the best for my specific application?</p>
<!-- /wp:paragraph --></div></div>
<!-- /wp:group -->

<!-- wp:paragraph {"fontSize":"medium"} -->
<p class="has-medium-font-size"><strong>Alkaline</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Alkaline cells run the mill consumer battery, used in everything from consumer goods to instruments. Ease of purchase and low cost has led to this being the most commonly used primary cell. Deficiencies include a low voltage, small temperature range, and poor self-discharge rates, leading to it being a poor choice for long-term applications. </p>
<!-- /wp:paragraph -->

<!-- wp:columns -->
<div class="wp-block-columns"><!-- wp:column {"width":"50%"} -->
<div class="wp-block-column" style="flex-basis:50%"><!-- wp:group -->
<div class="wp-block-group"><div class="wp-block-group__inner-container"><!-- wp:image {"align":"center","width":80,"height":209,"className":"is-style-rounded"} -->
<div class="wp-block-image is-style-rounded"><figure class="aligncenter is-resized"><img src="/assets/images/posts/image.webp" alt="This image has an empty alt attribute; its file name is image.png" width="80" height="209"/></figure></div>
<!-- /wp:image --></div></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column {"width":"50%"} -->
<div class="wp-block-column" style="flex-basis:50%"><!-- wp:paragraph -->
<p>• Low voltage (1.5V)<br>• High pulse current (750mA)<br>• Narrow temperature range (-18°C to +55°C)<br>• Moderate discharge rate (3% annually)<br>• High capacity (3,000 mAh in AA package)<br>• It does not contain hazardous materials</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:paragraph {"fontSize":"medium"} -->
<p class="has-medium-font-size"><strong>Lithium Manganese Dioxide</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>LiMg2O¬4 is everyday chemistry for large coin cell batteries. More potent than Silver-Oxide batteries, Lithium Manganese has an output voltage of 3V and an impressively low self-discharge rate. The main downside of this chemistry is its lower overall capacity compared to other options. This battery is optimal for ultra-low power designs with strict mechanical restrictions, as there is a large selection of standardized coin cell packages for this battery type. </p>
<!-- /wp:paragraph -->

<!-- wp:columns -->
<div class="wp-block-columns"><!-- wp:column {"width":"100%"} -->
<div class="wp-block-column" style="flex-basis:100%"><!-- wp:columns {"verticalAlignment":"center"} -->
<div class="wp-block-columns are-vertically-aligned-center"><!-- wp:column {"verticalAlignment":"center","width":"50%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:50%"><!-- wp:group -->
<div class="wp-block-group"><div class="wp-block-group__inner-container"><!-- wp:paragraph {"align":"left"} -->
<p class="has-text-align-left">• Moderate voltage (3.0V)<br>• Low pulse current (5-10mA)<br>• Moderate temperature range (-30°C to +60°C)<br>• Low discharge rate (1% annually)<br>• Moderate capacity (2,000 mAh in AA package) </p>
<!-- /wp:paragraph --></div></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column {"verticalAlignment":"center","width":"50%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:50%"><!-- wp:image {"align":"center","id":6541,"width":155,"height":125,"className":"is-style-default"} -->
<div class="wp-block-image is-style-default"><figure class="aligncenter is-resized"><img src="/assets/images/posts/image-1.webp" alt="" class="wp-image-6541" width="155" height="125"/></figure></div>
<!-- /wp:image --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:paragraph {"fontSize":"medium"} -->
<p class="has-medium-font-size"><strong>Lithium Thionyl Chloride</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Li/SOCl2 is a less common industrial battery chemistry oriented towards long-life applications. With a low self-discharge rate, high capacity, and wide temperature range, this battery is suited for any application requiring low power levels for multiple decades. High-quality batteries designed with low discharge rates can have shelf lives of up to 40 years. </p>
<!-- /wp:paragraph -->

<!-- wp:columns {"verticalAlignment":"center"} -->
<div class="wp-block-columns are-vertically-aligned-center"><!-- wp:column {"verticalAlignment":"center","width":"50%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:50%"><!-- wp:image {"align":"center","id":6542,"width":95,"height":188,"sizeSlug":"large","linkDestination":"none","className":"is-style-default"} -->
<div class="wp-block-image is-style-default"><figure class="aligncenter size-large is-resized"><img src="/assets/images/posts/image-2.webp" alt="" class="wp-image-6542" width="95" height="188"/></figure></div>
<!-- /wp:image --></div>
<!-- /wp:column -->

<!-- wp:column {"verticalAlignment":"center","width":"50%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:50%"><!-- wp:columns {"verticalAlignment":"center"} -->
<div class="wp-block-columns are-vertically-aligned-center"><!-- wp:column {"verticalAlignment":"center","width":"100%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:100%"><!-- wp:group -->
<div class="wp-block-group"><div class="wp-block-group__inner-container"><!-- wp:paragraph {"align":"left"} -->
<p class="has-text-align-left">• Moderate voltage (3.6V)<br>• Moderate pulse current (5-20mA)<br>• Wide temperature range (-55°C to +85°C)<br>• Low discharge rate (1% annually)<br>• High capacity (2,400 mAh in AA package)</p>
<!-- /wp:paragraph --></div></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:paragraph -->
<p>Here is where your selection can run into mechanical limitations. You may have effectively unlimited space for one device, allowing you to choose the battery with the most features you want. Sometimes a small package size will limit your options. For one device, it was impossible to fit a Lithium Thionyl Chloride cell into the desired form factor, unlike its predecessors. Instead, smaller Lithium Manganese Dioxide coin cells were chosen, which still met the capacity and current requirements. The tradeoff? A voltage level 0.6V lower than the Thionyl batteries could supply. This was able to be worked around but required a redesign of the power circuitry.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"medium"} -->
<p class="has-medium-font-size"><strong>Lithium Passivation</strong></p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"right","id":6543,"width":303,"height":221,"sizeSlug":"large","linkDestination":"none","className":"is-style-default"} -->
<div class="wp-block-image is-style-default"><figure class="alignright size-large is-resized"><img src="/assets/images/posts/image-3-550x401.webp" alt="" class="wp-image-6543" width="303" height="221"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>While sitting on the shelf, primary Lithium batteries, especially Lithium Thionyl Chloride cells, form an insulating layer over their internal anode called a solid electrolyte interphase (SEI).  This passivation layer reduces the cell's self-discharge, allowing for extremely long shelf lives, ranging from 10 to 40 years. Unfortunately, this oxide layer does have a downside. If the layer has been building up for a long time, it will take a high current discharge to wear it down and resume regular operation. Until that point, the instantaneous current of the batteries will be relatively low. To combat this, frequent but brief high current discharges will prevent any heavy buildup of an oxide layer. Typically a couple of milliamps is enough to counteract this effect.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This phenomenon not only affects your cell operation but can also affect your component sourcing. A batch of Devices was recently put into production using Lithium Thionyl Chloride cells. These purchased batteries were unknowingly manufactured 12 years prior. Not only had they lost a portion of their capacity, but they were heavily passivated and had issues supplying even low currents in the milliamp range. Ultimately, the cells could be de-passivated by applying high loads to the cells for an extended time. Still, a significant portion of their capacity would be spent in the process. In the end, sourcing newly manufactured cells became an important task when requesting information from distributors and vendors before assembly.</p>
<!-- /wp:paragraph -->