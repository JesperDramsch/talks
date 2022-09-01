---
marp: true
theme: dramsch
paginate: true
_paginate: false
title: Increase citations, ease review & collaboration – Making machine learning in research reproducible
header: EuroScipy 2022
footer: by Jesper Dramsch
---

<!-- _class: invert lead -->

# Increase Citations<br>Ease Review & Collaboration
## Making machine learning in research reproducible <!--fit-->

Jesper Dramsch

---

<!-- _class:  lead -->


🤷 Why, tho?
<br><br>
amplt.de/euroscipy22

---

## Outline

* Model Evaluation
* Benchmarking
* Model Sharing
* Testing
* Interpretability
* Ablation Studies





---

## Model Evaluation<!--fit-->

* Ensure valid results
* Reviewer should reject bad evaluation
* Reduce impact of dependence
* i.e. time-series, spatial, spatio-temporal

![bg right](evaluation.jpg)


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

<!-- _class: invert lead -->

# Make it Easy to Use

## People might use it!