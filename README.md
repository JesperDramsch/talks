# Talks by Jesper Dramsch

## All Talks






<!-- TALKS -->
### A Year of "AI" Shenanigans - SSI Fellows Update

| Event         | Location           | Date       | Link                                | Video | Slides |
| ------------- | ------------------ | ---------- | ----------------------------------- | ----- | ------ |
| PyCon Germany | Darmstadt, Germany | 2025-04-24 | https://2025.pycon.de/talks/WMBDJ8/ |       | [Slides](2025-04-24%20PyCon%20Germany/) |

What does it take to go from "ML will never work in weather forecasting" to running AI models in production at weather agencies? This talk chronicles the journey of Anemoi, a framework that evolved from research code to an operational ML weather forecasting system - and the technical challenges we faced along the way.

Starting as experimental code and notebooks by a small team of four, Anemoi grew into a robust ecosystem supporting 40+ developers across multiple international weather agencies. I'll share our experience of scaling both the team and codebase, including the interesting challenge of conducting weekly code tours for new team members while maintaining development velocity.

The technical evolution of Anemoi mirrors many challenges in scaling ML systems. We'll explore how the codebase transformed from research artifacts and notebooks into a structured mono-package with proper separation of concerns. Then, how we split this into an ecosystem of specialized packages - only to later realize that some components were too tightly coupled and needed reunification. This journey offers valuable lessons about when to split packages and when to maintain unified codebases.

Configuration management evolved alongside our architecture. I'll demonstrate how we leveraged Hydra to tame over 300 configuration options into a hierarchical system that enables component composition without sacrificing usability. This system now powers everything from dataset creation to model inference, with full traceability of configurations and artifacts throughout the ML lifecycle.

A unique aspect of developing ML systems at ECMWF is integrating with decades of expertise in weather forecast validation. We'll look at how we connected modern ML tooling like MLFlow with traditional meteorological evaluation systems, creating a bridge between ML innovation and established meteorological practices.

The talk will cover practical challenges that every growing ML system faces:

-   Making model components truly configurable and replaceable
-   Implementing model sharding for global weather predictions
-   Supporting flexible grids for regional weather services
-   Managing CI/CD across multiple packages
-   Streamlining release processes with modern tools
-   The eternal struggle with changelog management

Throughout the presentation, I'll share real examples of what worked, what didn't, and why - including our experiments with AI coding assistants and where they fell short. You'll walk away with concrete patterns for scaling Python ML systems, strategies for managing growing complexity, and insights into balancing research flexibility with production requirements.

Whether you're scaling an ML system, managing a growing Python codebase, or interested in how weather forecasting is being transformed by AI, this talk offers practical lessons from the frontier of operational ML systems.

### A Year of "AI" Shenanigans - SSI Fellows Update

| Event | Location | Date | Link | Video | Slides |
| ----- | -------- | ---- | ---- | ----- | ------ |
| SSI Fellows Community Call | Online | 2023-05-30 |  | | [Slides](2023-05-30%20SSI%20Fellows%20Update/) |

This presentation provides a summary of the Fellows Update presented by Jesper Dramsch as part of the SSI Fellows Community Call.

Jesper Dramsch, a member of the 2022 Cohort, discusses tackling the looming reproducibility crisis in science that uses machine learning. The focus is on addressing the challenges in a world consumed by AI hype.

The plan for 2022 includes the following activities:

- Participating in the community
- Creating a workshop
- Sharing content on YouTube
- Writing articles
- Giving talks

The workshop materials live here: [realworld-ml.xyz](https://realworld-ml.xyz)

A website called "ml.recipes" is introduced, which aims to make tutorials on machine learning accessible and appealing. It utilizes Jupyter Book, provides extra content, is visually appealing, and optimized for search engines.
[ML.Recipes](https://ml.recipes)

Highlights of various accomplishments and activities, including:

- Applying reproducible ML at work
- Teaching a MOOC to 7,000 people
- Offering Skillshare courses on ethical and reproducible AI with a total of 6,500 students
- Writing 5 SSI and personal blog posts
- Creating 20 YouTube videos with 1.4 million impressions
- Being a guest on multiple podcasts
- Delivering multiple talks and guest lectures

Also!

I'm building an inclusive machine learning community, with a focus on being LGBTQ+-friendly and neurodivergent. The goal is to strive for excellence in all other aspects of inclusivity as well.

[The Latent Space](https://latent.club)

"The Latent Space" is a platform introduced to have fun with the fellowship experience.
Have fun with your Fellowship

**Embrace the chaos and enjoy the fellowship experience.**
### How to find your people actually


| Event | Location | Date | Link | Video | Slides |
| ----- | -------- | ---- | ---- | ----- | ------ |
| SSI Community Building Group | Online | 2023-04-19 |  | | [Slides](2023-04-19%20Community%20Talk/) |

A guide on how to find and build a community that is welcoming, diverse, and aligned with your beliefs. 

The author, Jesper Dramsch, shares their personal experience of participating in various communities, including queer munches, gaming discords, and professional communities, and highlights the issues that led to their departure, such as lack of diversity and recognition, questionable ethics, and personality cults. 

The talk offers strategies for building a successful community, including creating a common belief system, defining values, using icons and tokens, establishing rituals, having a common language, recruiting mentors, and sharing superpowers. Where I also emphasize the importance of strong moderation, easy access, and being welcoming to everyone.


### Real-world Perspectives to Avoid the Worst Mistakes using Machine Learning in Science


| Event | Location | Date | Link | Video | Slides |
| ----- | -------- | ---- | ---- | ----- | ------ |
| Pydata Global 2022 | Online | 2022-12-02 | [Pydata](https://global2022.pydata.org/cfp/talk/Y9VFDD/) | [Youtube](https://youtu.be/I1st7eeyo2k) | [Slides](2022-12-02%20Pydata%20Global/) |

> Numerous scientific disciplines have noticed a reproducibility crisis of published results. While this important topic was being addressed, the danger of non-reproducible and unsustainable research artefacts using machine learning in science arose. The brunt of this has been avoided by better education of reviewers who nowadays have the skills to spot insufficient validation practices. However, there is more potential to further ease the review process, improve collaboration and make results and models available to fellow scientists. This workshop will teach practical lessons that can be directly applied to elevate the quality of ML applications in science by scientists.

The overview talk serves to set the scene and present different areas where researchers can increase the quality of their research artefacts that use ML. These increases in quality are achieved by using existing solutions to minimize the impact these methods take on researcher productivity.

This talk loosely covers the topics Jesper discussed in their Euroscipy tutorial which will be used for the interactive session here:

https://github.com/JesperDramsch/ml-for-science-reproducibility-tutorial

Topics covered:

- Why make it reproducible?
- Model Evaluation
- Benchmarking
- Model Sharing
- Testing ML Code
- Interpretability
- Ablation Studies

These topics are used as examples of “easy wins” researchers can implement to disproportionately improve the quality of their research output with minimal additional work using existing libraries and reusable code snippets.

### Increase citations, ease review & collaboration – Making machine learning in research reproducible

| Event | Location | Date | Link | Video | Slides |
| ----- | -------- | ---- | ---- | ----- | ------ |
| Euroscipy 2022 | Basel, Switzerland | 2022-09-01 | [Euroscipy](https://pretalx.com/euroscipy-2022/talk/8RAJX7/) | | [Slides](2022-09-01%20Euroscipy/) |

> Every scientific conference has seen a massive uptick in applications that use some type of machine learning. Whether it’s a linear regression using scikit-learn, a transformer from Hugging Face, or a custom convolutional neural network in Jax, the breadth of applications is as vast as the quality of contributions.
>
> This tutorial aims to provide easy ways to increase the quality of scientific contributions that use machine learning methods. The reproducible aspect will make it easy for fellow researchers to use and iterate on a publication, increasing citations of published work. The use of appropriate validation techniques and increase in code quality accelerates the review process during publication and avoids possible rejection due to deficiencies in the methodology. Making models, code and possibly data available increases the visibility of work and enables easier collaboration on future work.
>
> This work to make machine learning applications reproducible has an outsized impact compared to the limited additional work that is required using existing Python libraries.
### Application to Software Sustainability Institute Fellowship 2022

| Event | Location | Date | Link | Video | Slides |
| ----- | -------- | ---- | ---- | ----- | ------ |
| SSI Fellowship 2022 | Online | 2021-10-30 | [SSI](https://dramsch.net/ssi) | [Video](https://youtu.be/wxMZxbui4Bg) | [Slides](2021-10-31%20SSI%20Fellowship%20Application/) |

##### 🔁 THE REPRODUCIBILITY CRISIS
Machine learning can do amazing feats. BUT time and time again, we see problems reproducing the findings.

Why?

- Randomness of neural networks
- Software versions
- Different hardware
- Proprietary data
- Proprietary labels

##### 💥 SUSTAINABLE MACHINE LEARNING APPLICATIONS
Let's educate researchers not in ML on how to make their awesome experiments using ML reproducible.

The plan from the video: 🛠️ Create a workshop for ML applications 🎥 Keep going with YouTube ✒️ Write more articles 📣 More Talks

##### 🛠️ THE WORKSHOP
What does Workshop for Sustainable Machine Learning applications in Research look like?

Open to ideas, here's a start

- fix random seeds
- provide software versions
- use best practices
- interpretable and explainable AI

Maybe PyData will have me?

#### CONCLUSION

For this Software Sustainability Institute 2022 fellowship I plan to:

- Create a workshop for ML applications
- Keep going with YouTube
- Write more articles
- Give More Talks

### How to Guarantee No One Understands What You Did in Your Machine Learning Project

| Event | Location | Date | Link | Video | Slides |
| ----- | -------- | ---- | ---- | ----- | ------ |
| Pydata Global 2021 | Online | 2021-10-30 | [Pydata](https://pydata.org/global2021/schedule/presentation/112/how-to-guarantee-no-one-understands-what-you-did-in-your-machine-learning-project/) | [Video](https://www.youtube.com/watch?v=ucgCGGb088E) | [Slides](2021-10-28%20Pydata%20Global/) |

> Data science and machine learning can be a lot of fun. Freshly out of university, a bootcamp, or through the grinder of a Kaggle competition, we learned all the neat technical tricks. Suddenly that's only a basic requirement to get a job or even make anyone interested in your machine learning project. Let's dissect that.
>
> Working on a model for a few days, researching the architecture, perfecting all the tweaks and fixing all the leakage can make us forget that we're the only one that deep into the material. I sure do. But technobabble will not get us anywhere. The problem is that no one else is that deep into it or necessarily even cares. Depending on the company you keep, it may even be worse. I'm originally a geophysicist. Among physicists, you have a large number of people highly sceptical of machine learning. Talking too much about the specifics of the machine learning model may be actively detrimental. Funnily, sometimes we have the completely opposite problem, like I do at my new job. I'm amongst people who run circles around me on the topic of classic statistics. Yet, and this may come as a surprise, they know less than me about machine learning.
>
> So how do we fix that? How do we scale that gap? (And how do we make this into an interesting Talk?)
>
> Communicating machine learning and data science means building trust with your stakeholders. (Be they your job interviewer, grant coordinator, colleagues, or management at a job.)
>
> There's a specific time and place for talking shop, and that's when you're with other mechanics. In this talk, I will dive into the more abstract understanding of setting expectations around machine learning with stakeholders in the beginning. Then we'll progress into tools and strategies to communicate machine learning results to people who don't necessarily care about machine learning.
>
> We'll explore specific tools from machine learning explainability, interpretability and touch on causality. We'll talk about ethical considerations. We'll explore helpful visualizations and tools for interactivity. Finally, we talk about model validation specific to different expert domains and tie it all together.
<!-- //TALKS -->







## Tech

Marp based: https://marp.app/#get-started


## License

[![CC BY 4.0][cc-by-image]][cc-by]

Text, slides, arrangement and ideas communicated are licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

Images are often from Unsplash and do not fall under this license.
