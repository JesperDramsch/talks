---
marp: true
theme: dramsch
paginate: true
_paginate: false
title: Why and how make ML reproducible?
header: Pydata Global 2022
footer: by Jesper Dramsch
---

<!-- _class: invert lead -->

# Why and how make ML reproducible? <!--fit-->

Jesper Dramsch

---

<!-- _class:  lead -->


🤷 Why, tho?


---

# Why Reproducibility<!--fit-->

* Make an Impact
* Scientific Results
* Human Progress
* Ethical Work
* Funding Bodies
* Easy to Reuse
* Gift to ourselves

![bg right](together.jpg)

---


<!-- _class: invert lead -->

# Bad ML and bad science hurt people. <!--fit-->

---

<!-- _class:  lead -->

🤷 How, tho?

---

## Model Evaluation<!--fit-->

* Ensure valid results
* Reviewer should reject bad evaluation
* Reduce impact of dependence
* Adress real-world class distribution

![bg left](evaluation.jpg)

---

## How hard is that?<!--fit-->

<br><br><br>Medium hard...<br>dramsch.net/books

![bg left](understanding-ml-validation-e-book-thumbnail.jpg)

---

## Benchmarking

* Collaboration
* Dummy Classifiers
* Domain solutions
* Benchmark Datasets
* Simple models
* i.e. Random Forest, Linear Models

![bg right](bench.jpg)


---

## Model Sharing

* Export & Share model checkpoints
* Fix sources of randomness
* Linting & Formatting
* Docstrings
* Dependencies
* Docker

![bg left](sharing.jpg)

---

# Testing

* Deterministic Tests
* Data Sample Tests
* Docstrings for Tests
* Input Data Validation

![bg left](test.jpg)

---

# Interpretability <!--fit-->

* Scikit-Learn Tools
* Shap Explainability
* Model Inspection
* Communicate Results
* Build Intuition

![bg right](interp.jpg)

---

## Ablation Studies <!--fit-->

* Building ML is iterative
* Remove components of solution
* Shows the impact on final pipeline

![bg right](ablation.jpg)

---

<!-- _class:  lead -->

🤷 Where, tho?

* realworld-ml.xyz

--- 

<!-- _class: invert lead -->

# Make it Easy to Use

## People might use it!