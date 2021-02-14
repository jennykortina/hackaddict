---
layout: default
title: 'Notes -- Andrew Kortina'
---

{% assign posts = site.posts | sort: 'date' | reverse %}{% for post in posts %}<article><p><a href="{{site.url}}{{ post.url }}">{{ post.title }}</a></p><p>{{post.date | date: "%A, %B %-d, %Y"}}</p></article>{% endfor %}
