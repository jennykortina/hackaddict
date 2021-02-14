---
author: kortina
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-6411845113982879333
blogger_orig_url: https://www.hackaddict.net/2007/09/quick-tip-count-number-of-files-in.html
date: '2007-09-27T08:44:00.000-04:00'
layout: post
modified_time: '2007-09-27T08:47:08.622-04:00'
redirect_from: /2007/09/quick-tip-count-number-of-files-in.html
tags:
- nix
- mac
- tip
title: 'Quick Tip: Count the Number of Files in a Directory'
---

From the command line (terminal in OS X), go to the directory and execute this line:

<b>ls -1 | wc -l</b>



<b>ls -1</b> will list files 1 per line and piping into <b>wc -l</b> will count the number of lines output.