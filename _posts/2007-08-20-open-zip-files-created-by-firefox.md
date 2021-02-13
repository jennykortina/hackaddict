---
author: kortina
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-7530913604041896376
blogger_orig_url: https://www.hackaddict.net/2007/08/open-zip-files-created-by-firefox.html
date: '2007-08-20T09:03:00.000-04:00'
layout: post
modified_time: '2007-08-21T10:50:43.841-04:00'
redirect_from: /2007/08/open-zip-files-created-by-firefox.html
tags:
- firefox
- tip
title: Open Zip Files created By the Firefox Extension Wizard in OS X
---

I'm working on a few Firefox extensions, and I came across a pretty slick tool that generates a skeleton for your extension:<br /><br /><a href="http://ted.mielczarek.org/code/mozilla/extensionwiz/" title="Firefox/Thunderbird Extension Wizard">Firefox / Thunderbird Extension Generator</a><br /><br />You put in some basic info about your extension and it generates a zip file with the skeleton for your extension.  For some reason, whenever I double-clicked this zip in OS X and Stuff-it tried to expand the zip, I got this error:<br /><br /><b>An error occurred attempting to expand 'extension.zip'.  Format error.  Error #17540.</b><br /><br />After about 15 minutes of frustrating attempts to rebuild the extension all resulting in the same error, I just tried opening the file from the command line:<br /><br /><pre>$ cd downloads</pre><br /><pre>$ unzip extension.zip</pre><br /><br />This did the trick.