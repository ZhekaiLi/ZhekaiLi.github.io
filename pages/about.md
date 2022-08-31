---
layout: page
title: About
description: 打码改变世界
keywords: Zhuang Ma, 马壮
comments: true
menu: 关于
permalink: /about/
---

<div style="display: flex;justify-content: center;align-items: top;">
<img src="/images/2022-08/Snipaste_2022-08-30_22-39-34.png" width="21%" height="21%" style="vertical-align:down;">&nbsp;&nbsp;&nbsp;&nbsp;
<span> <a href="https://www.linkedin.com/in/zeka-li-a949a2236/" target="_blank" title="Go to LinkedIn">LinkedIn</a>, Email: zli3125@gatech.edu<br>Hi, I'm Zeka(Zhekai) Li, a graduate student in <b>MS Supply Chain Engineering</b> at the Georgia Institute of Technology. I'll graduate in December 2023 and I'm currently looking for a <b>2023 summer internship in supply chain analysis</b><br> </span>
<span></span>
</div>
<br>
I have finished 3 research projects about <b>modeling, machine learning, and programming</b>. As an assistant researcher, I developed a metric to evaluate the vulnerability of a metro network and applied its utility through a case study; I exploited different clustering methods, and modified DBSCAN(a density-based clustering algorithm) to fit the dataset from road failure detection; I designed a python class and created a workflow to extract geometric information from 3D point cloud data.

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
