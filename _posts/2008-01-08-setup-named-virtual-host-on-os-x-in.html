---
layout: post
title: Setup a Named Virtual Host on OS X in Apache
date: '2008-01-08T18:26:00.000-05:00'
author: kortina
tags:
- mac
modified_time: '2008-01-08T18:36:02.777-05:00'
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-4142229594836375176
blogger_orig_url: https://www.hackaddict.net/2008/01/setup-named-virtual-host-on-os-x-in.html
---

Today, in order to make some testing easier, I wanted to setup a named virtual host in Apache.  Here's how I did it.<br /><br />In terminal,<br /><pre>mate /etc/hosts # open hosts file in textmate</pre><br /><br />Add this line:<br /><br /><pre>127.0.0.1 www.layersix.dev</pre><br /><br />This tells your browser (or whatever) to look on your personal webserver for any requests to www.layersix.dev.  In terminal, do<br /><pre>lookupd -flushcache</pre><br />to make sure you clear your cache of dns names.<br /><br />In terminal,<br /><pre>mate /etc/httpd/httpd.conf</pre><br /><br />This is the apache settings file.  Look for "NameVirtualHost" and make sure the line reads<br /><br /><pre>NameVirtualHost *:80</pre><br /><br />Make sure there is no <b>#</b> before this.<br /><br />Add the following:<br /><pre><br /><VirtualHost *:80><br /> DocumentRoot /Library/WebServer/Documents/layersix.dev<br /> ServerName www.layersix.dev<br /></VirtualHost><br /></pre><br /><br />Go to <b>/Library/WebServer/Documents/</b> and make a folder called layersix.dev (or whatever). Make a file called <b>index.html</b> and put some text in it.  I did <b>echo 'hi' > layersix.dev/index.html</b>.  Restart your webserver in <b>System Preferences > Sharing</b>.  Go to www.layersix.dev in Firefox or whatever browser you use.  You should now see your index.html file.<br /><br />This post was helpful in figuring this out:<br /><a href="http://www.macosxhints.com/article.php?story=20010423075959611">http://www.macosxhints.com/article.php?story=20010423075959611</a>