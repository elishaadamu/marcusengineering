---
layout: service
title: "Advanced Secure Systems: Guarding Intellectual Property and Ensuring Trust"
category: Defence & Security
catchy_phrase: "Guarding Intellectual Property and Ensuring Trust."
short_blurb: "Marcus Engineering specializes in the design and fortification of secure hardware systems. From limited-life medical devices to robust embedded systems, we prioritize safety, trust, and the highest levels of security."
capabilities:
  - Secure Hardware Systems
  - Disposable Medical Device Security
  - Proprietary Code Protection
  - Defensive vs. Offensive Security Techniques
  - Side Channel Attack Prevention
  - Secure Chain of Trust
  - ISO/IEC, CWE, CVSS Standards
hero_image: "/assets/images/industries-images/Defensive Security Image 2.png"
---

Marcus Engineering has deep background in secure hardware systems, used in a wide range of applications from limited life medical devices to secure embedded systems that go to untrusted users. Marcus Engineering works with you to develop secure products form the ground up as well as securing your existing products from unauthorized users and attackers.

Whether your product is a Disposable Medical device or a hardened embedded system running your proprietary code Marcus Engineering can work with you to create a secure system that can keep attackers out. Marcus Engineering works with you to identify the likely resources that an attacker can throw at your system and can work with you to craft a secure environment that matches your needs and keeps your product and IP safe.

Development for a Secure System is very different from normal product development. When developing a secure system, it requires a paradigm shift in thinking from “how will this system function?” to “how can this function be abused?” Systems developed without Security at the forefront of thought will often include interfaces and systems that make development and troubleshooting easer and promote the “golden path” where users interact with the system the way it is designed.

Crafting a secure system requires defense in layers so there is no single point of failure. Commercial attackers who are attacking a system are embarking on an uncertain journey as they work to defeat the security on your system. By defending in layers, you prevent yourself from revealing a single weak point of failure, as well as preventing your attackers from fully scoping the effort needed to attack your system. As attackers work on your system you want to have high uncertainty in the effort required to defeat your system.

Marcus Engineering works to keep customers appraised of the latest developments in Defensive security techniques as well as Offensive security techniques used to break them. This can help you be proactive not reactive with respect to system attackers. The costs and complexity of advanced attacks like Decapping ICs to bypass read protections, Differential Power Analysis, and Glitching are lower than you might think and can cause your entire security strategy to come down.

Protecting from Side Channel attacks, is unlike any traditional security or product development activity, it breaks assumptions used in the design of, cryptographic algorithms as well as assumptions about that is easy and what is hard to develop. One great example of this is RSA, if the bit for a key is 1 then an additional operation is completed, if it’s a zero it’s skipped. By just looking at the timing of the bits you can read out the secret key from a single power trace. Another attack on RSA involves injecting a fault into the calculation of a multiplication, when encrypting a message, and comparing the output. This allows calculating the value of the secret key.

Secure systems require a secure chain of trust throughout your system, foe example if you have a limited life medical device and a console that uses it, you may have the most secure scheme in the word for marking that a device is used but if your console is unsecured an attacker can modify it so that it simply bypasses that check. Everything in your system should be signed and verified all the way back to your root of trust in the hardware of your system, to make the complexity and cost of attacking the system as high as possible.

A common security hole that designers of secure systems make is using a single shared key for all there devices that is used in all of there systems, even in a secure element the cost of retrieving the key from a secure element can be amortized across the benefits of exploiting the system. There should never be any secret information in the hands of users that is common across your entire system. If you need to send secret data into the field then it should be unique per device so compromising it does not break your entire system.

## Notes

Useful Standards

*   **ISO/IEC 19790:2012:** The security requirements for a cryptographic module utilised within a security system protecting sensitive information in computer and telecommunication systems.
*   **ISO/IEC 17825:2016:** Specifies the non-invasive attack mitigation test metrics for determining conformance to the requirements specified in ISO/IEC 19790 for Security Levels 3 and 4.
*   **ISO/IEC 15408-1:2009:** Establishes the general concepts and principles of IT security evaluation and specifies the general model of evaluation given by various parts of ISO/IEC 15408 which in its entirety is meant to be used as the basis for evaluation of security properties of IT products.
*   **CWE - Common Weakness Scoring System (CWSS)**
*   **Common Vulnerability Scoring System (CVSS)**
*   **Joint Interpretation Library**
*   **CC Common Criteria Scoring system / Evaluation Assurance Level:** ([Common Criteria Portal](https://www.commoncriteriaportal.org/cc/), [NIAP-CCEVS](https://www.niap-ccevs.org/Documents_and_Guidance/cctls.cfm))
*   **NIST Handbook 150:** NVLAP Procedures and General Requirements;
*   **NIST Handbook 150-20:** NVLAP Information Technology Security Testing - Common Criteria;
*   **US Government Protection Profile**