---
author: jenny
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-4301871854065942977
blogger_orig_url: https://www.hackaddict.net/2007/07/reset-os-x-password-without-os-x-cd.html
date: '2007-07-11T09:40:00.000-04:00'
layout: post
modified_time: '2007-07-12T08:58:52.154-04:00'
redirect_from: /2007/07/reset-os-x-password-without-os-x-cd.html
tags:
- tutorial
- mac
- tip
title: Reset OS X Password Without an OS X CD
---

So you and your friends have a wild party and you wake up in the morning to realize someone has changed the admin password on your beloved mac and you can no longer access your computer.  No problem, you can just pop in the OS X DVD that came with your computer and reset the password....but wait, that's missing too.



Here's how to reset your OS X password without an OS X CD.  You need to enter terminal and create a new admin account:

<ol> 
<li>Reboot

 </li>
 
<li>Hold apple + s down after you hear the chime.

 </li>
 
<li>When you get text prompt enter in these terminal commands to create a brand new admin account (hitting return after each line):

 

<ul> 
<li>mount -uw / </li>
 
<li>rm /var/db/.AppleSetupDone </li>
 
<li>shutdown -h now </li>
</ul> </li>
 
<li>After rebooting you should have a brand new admin account.  When you login as the new admin you can simply delete the old one and you're good to go again!

 </li>
</ol>