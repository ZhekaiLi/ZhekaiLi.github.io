---
layout: page
title: About
description: 打码改变世界
keywords: About
comments: false
menu: About
permalink: /about/
---

I'm Zhekai Li.

Junior CEE student in ZJUI.

Love coding.

## Contact

<ul>
{% for website in site.data.social %}
<li>{{website.sitename }}：<a href="{{ website.url }}" target="_blank">@{{ website.name }}</a></li>
{% endfor %}
</ul>
