---
author: jenny
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-8711855552048983216
blogger_orig_url: https://www.hackaddict.net/2007/07/mobile-app-tutorial-create-shortcuts-to.html
date: '2007-07-02T11:57:00.000-04:00'
layout: post
modified_time: '2007-07-02T12:07:47.466-04:00'
redirect_from: /2007/07/mobile-app-tutorial-create-shortcuts-to.html
tags:
- tutorial
- mobile
title: 'Mobile App Tutorial: Create Shortcuts to Specific Midlets (ie. google mail)'
---

When skinning my windows mobile phone to look like an iPhone I ran into the problem to launch specific midlets.  I could launch the midlet manager, but not a specific program until I found <a href="http://forum.xda-developers.com/showthread.php?t=258141">this article at the xda development forums</a>.



To make the shorcuts you need acess to the apps .jar or .jad file on your computer.  Then you open the file and grab the needed info as described in their article.



Basically you end up launching the midlet browser and then the program.<b><suite><vendor><name><suite><vendor><name><n>

</n></name></vendor></suite></name></vendor></suite></b>

So Opera mini is: \Windows\jmm.exe -r"Opera Mini","Opera Software ASA","Opera Mini"

<b><suite><vendor><name><suite><vendor><name><n>

</n></name></vendor></suite></name></vendor></suite></b>The full explanation is wonderflul so head <a href="http://forum.xda-developers.com/showthread.php?t=258141">to the article for a full description</a>.<b>

</b>