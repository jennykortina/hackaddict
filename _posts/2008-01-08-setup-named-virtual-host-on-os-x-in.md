---
author: kortina
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-4142229594836375176
blogger_orig_url: https://www.hackaddict.net/2008/01/setup-named-virtual-host-on-os-x-in.html
date: '2008-01-08T18:26:00.000-05:00'
layout: post
modified_time: '2008-01-08T18:36:02.777-05:00'
redirect_from: /2008/01/setup-named-virtual-host-on-os-x-in.html
tags:
- mac
title: Setup a Named Virtual Host on OS X in Apache
---

Today, in order to make some testing easier, I wanted to setup a named virtual host in Apache.  Here's how I did it.



In terminal,

<pre>mate /etc/hosts # open hosts file in textmate</pre>



Add this line:



<pre>127.0.0.1 www.layersix.dev</pre>



This tells your browser (or whatever) to look on your personal webserver for any requests to www.layersix.dev.  In terminal, do

<pre>lookupd -flushcache</pre>

to make sure you clear your cache of dns names.



In terminal,

<pre>mate /etc/httpd/httpd.conf</pre>



This is the apache settings file.  Look for "NameVirtualHost" and make sure the line reads



<pre>NameVirtualHost *:80</pre>



Make sure there is no <b>#</b> before this.



Add the following:

<pre>

<virtualhost *:80="">

 DocumentRoot /Library/WebServer/Documents/layersix.dev

 ServerName www.layersix.dev

</virtualhost>

</pre>



Go to <b>/Library/WebServer/Documents/</b> and make a folder called layersix.dev (or whatever). Make a file called <b>index.html</b> and put some text in it.  I did <b>echo 'hi' &gt; layersix.dev/index.html</b>.  Restart your webserver in <b>System Preferences &gt; Sharing</b>.  Go to www.layersix.dev in Firefox or whatever browser you use.  You should now see your index.html file.



This post was helpful in figuring this out:

<a href="http://www.macosxhints.com/article.php?story=20010423075959611">http://www.macosxhints.com/article.php?story=20010423075959611</a>