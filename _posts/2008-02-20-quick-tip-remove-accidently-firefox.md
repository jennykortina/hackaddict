---
author: jenny
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-4039229600054737171
blogger_orig_url: https://www.hackaddict.net/2008/02/quick-tip-remove-accidently-firefox.html
date: '2008-02-20T11:36:00.001-05:00'
layout: post
modified_time: '2008-02-21T19:07:30.030-05:00'
redirect_from: /2008/02/quick-tip-remove-accidently-firefox.html
tags:
- tip
title: 'Quick Tip: Remove Accidently Added Firefox Dictionary Words'
---

I accidentally added a word to my Firefox dictionary today, and after a quick Google Search I found <a href="http://provisionit.blogspot.com/2007/05/edit-firefox-custom-dictionary.html">this article</a>.



Basically you need to find the persdict.dat.  It can be found here in the following operating systems:



Windows XP



C:\Documents and Settings\[User Name]\Application Data\Mozilla\Firefox\Profiles\xxxxxxxx.default\



Windows Vista



C:\users\[User Name]\AppData\Roaming\Mozilla\Firefox\Profiles\xxxxxxxx.default\



Mac OS X



~/Library/Application Support/Firefox/Profiles/xxxxxxxx.default/



Linux



~/.mozilla/firefox/xxxxxxxx.default/



After you have located persdict.dat, open it in your favorite text editor and simply remove the misspelled word.