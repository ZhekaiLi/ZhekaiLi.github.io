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
## 2.1 Define Metrics
<span style="background-color: yellow; color: black;">Define metrics is to turn a high-level metric to a well-defined metric</font>

In previous example, we use **Click-through-probability** as the high-level metric:
$$\text{click-through-probability}=\frac{\#\text{users who click}}{\#\text{users who visit}}$$

**How to identify user?** Cookies or Pageviews

### 2.1.1 Three well-defined metrics
> **Def #1: Use cookies**, calculate
$$\frac{\#\text{cookies that click}}{\#\text{cookies in <time interval>}}$$

For example, for one cookie:
- per minute: $2/3$, there are 3 valid minutes, two of them have click event
  <img src="/images/2022-12/Snipaste_2023-01-09_21-08-52.png" width="90%">
- per hour: $1/2$, there are 2 valid hours, one of them has click event
  <img src="/images/2022-12/Snipaste_2023-01-09_21-11-54.png" width="90%">
- per day: $1$

> **Def #2: Use pageviews**, calculate
$$\frac{\#\text{pageviews result2 click within <time interval>}}{\#\text{pageviews}}$$

For example:
<img src="/images/2022-12/Snipaste_2023-01-09_21-24-42.png" width="60%">

use Def #1 in minite, we get $1/1$; use Def #2 in minute, we get $1/2$

> **Def #3: click-through-rate**
$$\frac{\#\text{clicks}}{\#\text{pageviews}}$$

### 2.1.2 Problems of three metrics
**Problem 1: double click**: def #3, click-through-rate will be greatly influcence (用户频繁随意双击)

**Problem 2: back button cashes page** (通过返回键返回的界面一般是已经缓存了，不会二次刷新，因此就不会被当作 new pageview，但其实应该算) def #2 & #3 will be influenced because they are related to the number of pageviews

## 2.2 Summerize Metrics
There are different ways to summerize metrics:

> **(1) Sum and counts**

e.g. \#users who visited page

> **(2) Means, medians, and percentiles**

e.g. mean age of users who complete a course, median latency of page load

> **(3) Probability and rates**

probability is from [0, 1], while rates [0, infty)

> **(4) Ratio**

ratio = probability A / probability B

e.g. P(revenue-generating click) / P(any click)

# 3. Characterize






<img src="/images/2022-12/.png" width="60%">
<img src="/images/2022-12/.png" width="60%">
<img src="/images/2022-12/.png" width="60%">
<img src="/images/2022-12/.png" width="60%">

