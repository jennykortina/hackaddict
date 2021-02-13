---
layout: post
title: Fix broken arrow keys and backspace in vi / vim for Solaris (on Joyent)
date: '2008-03-06T01:06:00.003-05:00'
author: kortina
tags:
- nix
- tip
modified_time: '2008-03-13T14:31:28.213-04:00'
thumbnail: http://bp3.blogger.com/_3FPfpXHnCwA/R9lydBX4V-I/AAAAAAAAAIA/y6i890bR3xQ/s72-c/linux-iterm.png
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-5861367461931805529
blogger_orig_url: https://www.hackaddict.net/2008/03/fix-broken-arrow-keys-and-backspace-in.html
---

I am setting up a new development server for all my testing.  <a href-"http://joyent.com">Joyent</a> had a good deal, so I'm giving them a try.  They seem great so far, but I had major issues with <b>vi</b>.<br /><br />Here's how I fixed them.  From my home dir:<br /><b># vim .vimrc</b><br /><br />Add these lines<br /><pre>filetype plugin on<br />filetype indent on<br />syntax on<br />set bs=2</pre><br /><br />Just make sure to use <b>vim</b> instead of <b>vi</b> and your arrow keys and backspace should work as expected. Plus, you'll have syntax highlighting!<br /><br /><br />tips via google search that brought me here: <a href="http://www.tjansson.dk/?p=68">http://www.tjansson.dk/?p=68</a><br /><br /><br /><br />** UPDATE **<br />If you're using iterm in OS X, make sure you have your Terminal Profile <b>Type</b> set to <b>linux</b>.  Or you can add the following line to your .vimrc:<br /><br />set term=linux<br /><br /><br /><a onblur="try {parent.deselectBloggerImageGracefully();} catch(e) {}" href="http://bp3.blogger.com/_3FPfpXHnCwA/R9lydBX4V-I/AAAAAAAAAIA/y6i890bR3xQ/s1600-h/linux-iterm.png"><img style="display:block; margin:0px auto 10px; text-align:center;cursor:pointer; cursor:hand;" src="http://bp3.blogger.com/_3FPfpXHnCwA/R9lydBX4V-I/AAAAAAAAAIA/y6i890bR3xQ/s400/linux-iterm.png" border="0" alt=""id="BLOGGER_PHOTO_ID_5177295089549465570" /></a>