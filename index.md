---
layout: default
title: home
---

{% assign posts = site.posts | sort: 'date' | reverse %}{% for post in posts %}<article class="home-page"><h3><a class="post-title" href="{{site.url}}{{ post.url }}">{{ post.title }}</a></h3><div class="post-date">{{post.date | date: "%A, %B %-d, %Y"}}<span class="backslash-spacer">/</span><span>{{post.author}}</span></div><div class="post-preview">{{post.content}}</div><a class="read-more" href="{{site.url}}{{ post.url }}">Read More</a></article>{% endfor %}
