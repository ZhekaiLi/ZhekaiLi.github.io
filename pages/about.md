---
layout: page
title: About
description: 打码改变世界
keywords: Zhuang Ma, 马壮
comments: true
menu: 关于
permalink: /about/
---

Hi, I'm a graduate student in **MS Supply Chain Engineering** at the Georgia Institute of Technology. I'll graduate in December 2023 and I'm currently looking for a **2023 summer internship in supply chain analysis**. 

I have finished 3 research projects about **modeling, machine learning, and programming**. As an assistant researcher, I developed a metric to evaluate the vulnerability of a metro network and applied its utility through a case study; I exploited different clustering methods, and modified DBSCAN(a density-based clustering algorithm) to fit the dataset from road failure detection; I designed a python class and created a workflow to extract geometric information from 3D point cloud data.

Moreover, I have 2 months of internship as a structure designer at a local design institute. From this experience, I practiced my knowledge from school into real work and learned some basic principles with colleagues and bosses.

## Contact

<ul>
{% for website in site.data.social %}
<li>{{website.sitename }}：<a href="{{ website.url }}" target="_blank">@{{ website.name }}</a></li>
{% endfor %}
</ul>


## Skill Keywords

{% for skill in site.data.skills %}
### {{ skill.name }}
<div class="btn-inline">
{% for keyword in skill.keywords %}
<button class="btn btn-outline" type="button">{{ keyword }}</button>
{% endfor %}
</div>
{% endfor %}
