---
author: kortina
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-8541874135182322839
blogger_orig_url: https://www.hackaddict.net/2008/04/lookupd-flushcache-in-os-x-leopard.html
date: '2008-04-20T18:41:00.001-04:00'
layout: post
modified_time: '2008-04-20T18:43:53.726-04:00'
redirect_from: /2008/04/lookupd-flushcache-in-os-x-leopard.html
tags:
- nix
- mac
title: lookupd --flushcache in OS X Leopard
---

This is a fairly technical one, but for anyone that's done

<pre>sudo lookupd --flushcache</pre>

in versions of OS X before Leopard, you may have noticed that it doesn't work in Leopard.



The new way to clear your hosts cache is

<pre>sudo dscacheutil -flushcache</pre>



This is useful if you happen to be messing with the <b>/etc/hosts</b> file.