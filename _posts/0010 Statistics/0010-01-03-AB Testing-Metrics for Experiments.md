---
layout: post
title: A/B Testing - Metrics for Experiments
categories: Statistics
description: Personal Notes
keywords:
mathjax: true
---


<center>

# A/B Testing - Metrics for Experiments
</center>

# 1. Define
## 1.1 High level metric: customer funnel

<img src="/images/2022-12/Snipaste_2023-01-07_20-55-06.png" width="90%">

## 1.2 Expand on the funnel
The layers in the funnel above are too generall, we need to make them more detailed:

<img src="/images/2022-12/Snipaste_2023-01-07_20-56-25.png" width="80%">

After expending, we could try to find some **metrics** directly from funnel:
- **The number of each stage** could be metric. But in general, we only need to choose some more meaningful layers, such as #homepage visits, and #enrollment
- **Rates or probabilities**, which is division of two stages


<img src="/images/2022-12/Snipaste_2023-01-07_20-59-50.png" width="90%">

## 1.3 Choose Metrics
<img src="/images/2022-12/Snipaste_2023-01-08_11-28-57.png" width="90%">

For different experiments, we have to choose different metrics (one or more):
- Update a description on the course list page
  Metric 3: <u>Probability of progressing from course list to course page</u>
- Increase size of "Start Now" button
  Metric 1: <u>Click-through-rate on "Start Now" Button</u>
- Explain benefits of paid service
  Metric 5: <u>Probability that enrolled student pays for coaching</u> (in funnel, it's equal to #coaching use / #enrollments)


## 1.4 Difficult Metrics
Reasons for difficult metrics
- Don't have access to data
- Takes too long time

Examples:
- Rate of returning for 2nd course = (#who start 2nd)/(#who complete 1st)
  <u>have data, but too long time</u> (maybe months between taking two course)
- Average happiness of shoppers
  <u>no data</u>
- Probability of finding information via search
  <u>no data</u>

## 1.5 Other Techs to Define Metris
- **(1) External Data**
Use external data for comparsion
- **(2) User Experience Research (UER)**
low participants, deep depth
- **(3) Focus Groups** (like group discussion)
medium participants, medium depth
- **(4) Surveys**
high participants, shallow depth
- **(5) Retrospective Analysis 回顾分析**
A retrospective analysis or retrospective study is a **research method that is used when the outcome of an event is already known**. For example, medical researchers might study the records of patients who suffered from a particular disease to determine what factors may have led to their illness or death.
- **(6) Experiments**

<img src="/images/2022-12/Snipaste_2023-01-08_12-33-13.png" width="90%">

### 1.5.1 Apply other techs
<img src="/images/2022-12/Snipaste_2023-01-08_12-25-10.png" width="90%">

<img src="/images/2022-12/Snipaste_2023-01-08_12-27-27.png" width="90%">

# 2. Build Intuition

# 3. Characterize




<img src="/images/2022-12/.png" width="60%">
<img src="/images/2022-12/.png" width="60%">
<img src="/images/2022-12/.png" width="60%">

<img src="/images/2022-12/.png" width="60%">
<img src="/images/2022-12/.png" width="60%">
<img src="/images/2022-12/.png" width="60%">
<img src="/images/2022-12/.png" width="60%">

