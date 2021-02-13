---
author: kortina
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-2449587177020074480
blogger_orig_url: https://www.hackaddict.net/2008/01/unix-find-command-useful-with-xargs.html
date: '2008-01-10T22:49:00.001-05:00'
layout: post
modified_time: '2008-01-10T22:56:23.029-05:00'
redirect_from: /2008/01/unix-find-command-useful-with-xargs.html
tags: null
title: UNIX find command (useful with xargs)
---

I was having some trouble with a python app and needed to clear some cached, precompiled versions of some of the files in the app.  I had a hunch the <b>find</b> command might be useful, so I looked at the man doc.  Turns out it was very useful.<br/><br/><b>find</b> takes a few arguments.  The first (mandatory) argument is the path to search.  In my case, it was the current directory: <b>.</b> .  I also used an optional argument, an expression to filter out all files other than those ending in pyc.  Here's what I ended up with:<br/><br/><pre>find . -name "*.pyc" | xargs rm</pre><br/><br/>For some reason, I needed to put quotes around the <b>*.pyc</b>, otherwise I got the error:<br/><br/><pre>find: paths must precede expression</pre><br/><br/>Also, I added <b>| xargs rm</b>, piping find's output into xargs, which allows you to apply another method (in this case, rm) to each line.  This basically deletes anything in the current directory or any subdirectories named .pyc.  Be careful!<br/><br/>Finally, a quick google search brought me to this page that has lots of other good examples: <a href="http://www.wagoneers.com/UNIX/FIND/find-usage.html">http://www.wagoneers.com/UNIX/FIND/find-usage.html</a>