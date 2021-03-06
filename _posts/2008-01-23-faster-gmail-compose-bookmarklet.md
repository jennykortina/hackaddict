---
author: kortina
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-6657333396585278173
blogger_orig_url: https://www.hackaddict.net/2008/01/faster-gmail-compose-bookmarklet.html
date: '2008-01-23T15:31:00.001-05:00'
layout: post
modified_time: '2008-06-09T12:57:19.185-04:00'
redirect_from: /2008/01/faster-gmail-compose-bookmarklet.html
tags:
- mail
title: Faster Gmail Compose Bookmarklet
---

I read about making a gmail compose bookmarklet <a href="http://www.lifehack.org/articles/productivity/how-to-make-gmailgcal-rock-your-tasks.html">here</a> but I guess this method works a little differently now that Gmail version 2 is out.  The url I got as a bookmark from following the steps in this article looked like this:


<a href="https://mail.google.com/mail/?ui=2&amp;ik=340ae8adsd673&amp;view=cm&amp;fs=1&amp;tf=1&amp;ver=7fwl31x2aq9vivp2k9w0elmjy#cmid%3D1">
https://mail.google.com/mail/?ui=2&amp;ik=340ae8adsd673&amp;view=cm&amp;fs=1&amp;tf=1&amp;ver=7fwl31x2aq9vivp2k9w0elmjy#cmid%3D1</a>

This version of the bookmarklet takes forever to load for me and sometimes doesn't load at all.  I took off the <b>#cmid%3D1</b> and the loading time got a little faster and the page no longer froze while loading.



I continued removing stuff and changed from <b>ui=2</b> to <b>ui=1</b> and eventually got a significantly faster loading compose window with something that ended up looking like this:


```
https://mail.google.com/mail/?ui=1&amp;view=cm&amp;fs=1&amp;tf=1
```


This is the fastest version of the bookmarklet I could make that retained the auto-complete javacript for recipient fields.  For a super fast version, you could switch to HTML version of gmail and bookmark the compose page, but I  really like having the autocomplete for addresses.



To add my version of the bookmarklet, drag this link into your Bookmarks Toolbar:

<a href="https://mail.google.com/mail/?ui=1&amp;view=cm&amp;fs=1&amp;tf=1">G:</a>


I also made a javascript version of the bookmarklet that opens a new, small window, kind of like the capital-C shortcut works in Gmail.



Here is the javascript, open in new window, version:

```
<a href="javascript:var%20w=window,u='https://mail.google.com/mail/?ui=1&amp;view=cm&amp;fs=1&amp;tf=1',l=document.location;try{{ " {%"="" }}20throw(0);%20}%20catch(z)%20{a%20="function(){if(!w.open(u,'t','toolbar=0,resizable=0,status=1,width=600,height=500'))l.href=u;};if(/Firefox/.test(navigator.userAgent))setTimeout(a,0);else%20a();}void(0)&quot;">G:</a>
```


This javascript bookmarklet is the one I have ended up using.  Enjoy.


**UPDATE**

This appears to be faster now:

<a href="https://mail.google.com/mail/?ui=2&amp;view=cm&amp;fs=1&amp;tf=1">
https://mail.google.com/mail/?ui=2&amp;view=cm&amp;fs=1&amp;tf=1</a>


```
<a href="javascript:var%20w=window,u='https://mail.google.com/mail/?ui=2&amp;view=cm&amp;fs=1&amp;tf=1',l=document.location;try{{ " {%"="" }}20throw(0);%20}%20catch(z)%20{a%20="function(){if(!w.open(u,'t','toolbar=0,resizable=0,status=1,width=600,height=500'))l.href=u;};if(/Firefox/.test(navigator.userAgent))setTimeout(a,0);else%20a();}void(0)&quot;">G:</a>
```