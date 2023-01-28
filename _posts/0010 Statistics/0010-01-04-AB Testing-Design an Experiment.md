---
layout: post
title: A/B Testing - Design an Experiment
categories: Statistics
description: Personal Notes
keywords:
mathjax: true
---


<center>

# A/B Testing - Design an Experiment
</center>

# 1. Choose "subject"
## 1.1 Unit of Diversion
Severl ways to define a "person":
- Commonly used
  - **User id**: stable, unchanging; personally identifiable
  - **Anonymous id (cookie)**: change when switch brower or device; user can clear cookies
  - **Event**: no consistant experience; <span style="background-color: yellow; color: black;">use only for non-user-visibale changes</span> (例如像是改变一个按钮的颜色或者大小这种明显的就不行，而像是更改推荐电影的排序这种不明显的就可以)
- Less common:
  - **Device id**: only available for mobile, tied to specific device; personally identifiable
  - **IP address**: changes when location changes

**Example**: for a person who
1. use desktop browser to visit the homepage of an education website
2. sign in, visit a course page, and watch an video for a while
3. switch to mobile app, auto sign in
4. keep watch the vieo

||desktop homepage| sign| visit course| watch| mobile sign| keep watch|
|-|-|-|-|-|-|-|
|user-id|$\times$|$\checkmark$|-|-|-|-|
|cookie|$\checkmark$|?|?|?|?|?|
|event|$\checkmark$|$\checkmark$|$\checkmark$|$\checkmark$|$\checkmark$|$\checkmark$|
|device-id|$\times$|$\times$|$\times$|$\times$|$\checkmark$|-|
|IP address|$\checkmark$|?|?|?|?|?|

- $\checkmark$: change happen
- $-$: no change
- $\times$: not applicable
- $?$: unknown

## 1.2 Choose Diversion
There are 3 main considerations in selecting an appropriate unit of diversion:
- Consisitancy
- Ethical
- Variability

### 1.2.1 Consistancy
Different experiment require different levels of consistancy, and therefore could use different diversions:
- **Event**: low consistancy
- **Cookie**: medium consistancy (browser consistant)
- **User**: high consistancy (cross-device consistant)

Examples:

|Experiment| Event| Cookie| User-id|Reason|
|-|-|-|-|-|
|Change reducing video load time|$\checkmark$|-|-|Users probably won't notice|
|Change button color|-|$\checkmark$|-|Distracting if button changes on reload; Different look on diff devices OK|
|Change order of search result|$\checkmark$|-|-|Users probably won't notice|
|Add instructor's notes before quizzes|-|-|$\checkmark$|Users will notice; **cross-device consistancy** important

### 1.2.2 Variability
**Variability is higher when it's calculated empirically** (unit of diversion as denominator) than when calculated analytically (unit of analysis as denominator)

That's because the unit of analysis should be **always smaller or equal to** the unit of diversion

For example, for an experiment whose:
- **Metric**: Coverage = (\#queries with ad)/(#queries)
- **Unit of analysis**: query (a kind of event)
- **Unit of diversion**: query or cookie
- Binomial: $SE=\sqrt{p(1-p)/N}$

(1) When unit of diversion = unit of analysis, empirical variabliliy will be similar.
(2) When unit of diversion > unit of analysis, empirical variability will be higher because the denominator is smaller and therefore the value of metric will increasek, as well as variability.

<img src="/images/2022-12/Snipaste_2023-01-14_10-35-01.png" width="50%">

# 2. Choose "population"
## 2.1 Target Population
If we can identify **what population will be affected by our experiment, we have to target that traffic** (and avoid selecting either control group or experimental group from the population that will not be affected)

For example, for an experiment that will only affect users in New Zealand, from New Zealand users:
- Have $N_{cont},N_{exp},X_{cont},X_{exp}$
- Calculate difference $\hat d=\hat p_{count}-\hat p_{exp}$
- Calculate $\hat p_{pool}\to SE_{pool}$, and than calculate margin of significant $m=1.96SE$
- Find that $\|\hat d\|>m$, which means **change is significant** and might should be appliced

However, when we also include users from other countries that will not be affected by the expirment, we will find $\hat d\downarrow$, and therefore change might not be significant anymore

## 2.2 Cohort vs. Population
**Cohort is a subset of population.** After choosing an appropriate population, we might also need to choose a corhort further

For example, if we want to change the structure of an online course, we choose the population as the users who have taken that course.
<img src="/images/2022-12/Snipaste_2023-01-14_11-56-01.png" width="90%">

However, users registered in different times, as shown in the blue points in the pic above. Therefore, out **cohort should be the users registered after the start of experiment** (in red cycle)

# 3. Size
## 3.1 Variability Affect Size
According to different unit of diversion, the varaibility($SE$) is different.

To prove significance, we need to compare $d$ and $m=1.96SE$, and for **binomial** $SE$:
$$SE=\sqrt\frac{\hat p(1-\hat p)}{N} \sim 1/\sqrt{N}$$

For example, we determine a $d_{min}=0.02$, to reach that minimum, for different unit of diversion (cookie and query):
- sample size of query should be large
- sample size of cookie could be relatively small

<img src="/images/2022-12/Snipaste_2023-01-14_10-35-01.png" width="50%">


# 4. Duration
## 4.1 Duration
For example, we require:
- Size of an experiment: 1 million pageviews
- Average traffic per day: 0.5 million pageviews

**Does that means we have to run experiments for 2 days? No!**
- From the pic below, pageviews different in weekdays and weekends
- Selecting Sat and Sun cannot meet the size requirement
- We can:
  (1) run a mix of weekend and weekday days for 3 days
  (2) run longer(7 days) with less traffic

<img src="/images/2022-12/Snipaste_2023-01-15_17-23-11.png" width="60%">

## 4.2 Exposure
<u>**When to limit exposure**</u>

Which experiments are risky enough that we might have to limit the number of users exposed?
- $\checkmark$ Change database
  If this goes wrong, effects will be huge
- $\times$ Chnage color of a button
  Low risk
- $\checkmark$ Allows facebook login
  New function might not be well prepared


<img src="/images/2022-12/.png" width="60%">
<img src="/images/2022-12/.png" width="60%">
<img src="/images/2022-12/.png" width="60%">
<img src="/images/2022-12/.png" width="60%">
