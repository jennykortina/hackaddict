---
author: kortina
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-5861367461931805529
blogger_orig_url: https://www.hackaddict.net/2008/03/fix-broken-arrow-keys-and-backspace-in.html
date: '2008-03-06T01:06:00.003-05:00'
layout: post
modified_time: '2008-03-13T14:31:28.213-04:00'
redirect_from: /2008/03/fix-broken-arrow-keys-and-backspace-in.html
tags:
- nix
- tip
thumbnail: '{{ site.url }}/assets/images/thumbnails/2008-03-06-image-0000.png'
title: Fix broken arrow keys and backspace in vi / vim for Solaris (on Joyent)
---

I am setting up a new development server for all my testing.  <a href-"http:="" joyent.com"="">Joyent</a> had a good deal, so I'm giving them a try.  They seem great so far, but I had major issues with <b>vi</b>.



Here's how I fixed them.  From my home dir:

<b># vim .vimrc</b>



Add these lines

<pre>filetype plugin on

filetype indent on

syntax on

set bs=2</pre>



Just make sure to use <b>vim</b> instead of <b>vi</b> and your arrow keys and backspace should work as expected. Plus, you'll have syntax highlighting!





tips via google search that brought me here: <a href="http://www.tjansson.dk/?p=68">http://www.tjansson.dk/?p=68</a>







** UPDATE **

If you're using iterm in OS X, make sure you have your Terminal Profile <b>Type</b> set to <b>linux</b>.  Or you can add the following line to your .vimrc:



set term=linux





<img alt="" border="0" id="BLOGGER_PHOTO_ID_5177295089549465570" src="{{ site.url }}/assets/images/posts/2008-03-06-image-0000.png" style="display:block; margin:0px auto 10px; text-align:center; "/>