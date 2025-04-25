# A Year of "AI" Shenanigans - SSI Fellows Update

| Event         | Location           | Date       | Link                                | Video |
| ------------- | ------------------ | ---------- | ----------------------------------- | ----- |
| PyCon Germany | Darmstadt, Germany | 2025-04-24 | https://2025.pycon.de/talks/WMBDJ8/ |       |

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
