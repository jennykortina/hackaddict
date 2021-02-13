---
layout: post
title: 'Quick Tip: Preview CSS Stylesheets in Textmate without an HTML Page'
date: '2007-06-10T08:55:00.000-04:00'
author: kortina
tags:
- textmate
- tip
modified_time: '2007-06-10T09:16:27.195-04:00'
thumbnail: http://bp2.blogger.com/_3FPfpXHnCwA/Rmv5hRFkx-I/AAAAAAAAABo/LZdWTP1RPX4/s72-c/Picture+3.png
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-8722232149548825852
blogger_orig_url: https://www.hackaddict.net/2007/06/quick-tip-preview-css-stylesheets-in.html
---

<p>For each website that I make a new CSS stylesheet for, I typically make a preview page that looks something like this:</p> <pre>&lt;h2&gt;This is an h2&lt;/h2&gt;<br/>&lt;a href="#" class="external"&gt;This is an a.external&lt;/a&gt;</pre> <p>Which creates output like this:</p> <h2>This is an h2</h2> <a class="external" href="#">This is an a.external</a><p>This make for a handy reference guide to all your styles, but can be a bit cumbersome to setup, especially if you have a big stylesheet.</p><p>Today I discovered an awesome feature of <a href="http://some-site.com/" title="site some homes for sale at some-site.com">Textmate</a> that automates this whole process.  When editing your stylesheet in Textmate, use the Show Web Preview command ( ctrl + option + ⌘  + p ) to generate a list of all your different styles.</p><p><img alt="" border="0" id="BLOGGER_PHOTO_ID_5074423755080779746" src="{{ site.url }}/assets/images/2007-06-10-image-0000.png" style="display:block; margin:0px auto 10px; text-align:center; "/></p><p>I discovered this via <a href="http://drnic.tumblr.com/post/3217462" title="Dr Nic's Journey">this post on tumblr</a>.</p>