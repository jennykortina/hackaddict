---
author: jenny
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-6381522651580082609
blogger_orig_url: https://www.hackaddict.net/2007/06/tutorial-automount-samba-drive-when-at.html
date: '2007-06-09T08:29:00.000-04:00'
layout: post
modified_time: '2007-06-09T09:39:33.740-04:00'
redirect_from: /2007/06/tutorial-automount-samba-drive-when-at.html
tags:
- tutorial
- freeware
- mac
thumbnail: '{{ site.url }}/assets/images/thumbnails/2007-06-09-image-0000.png'
title: 'Tutorial: Automount a Samba Drive when at Certain Locations ie Home'
---

<img alt="" border="0" id="BLOGGER_PHOTO_ID_5074050094347540162" src="{{ site.url }}/assets/images/posts/2007-06-09-image-0000.png" style="margin: 0pt 10px 10px 0pt; float: left; "/>I have a lot of digital music and movies.  In fact, it's at the point where I decided that I needed a home a media server because my external hard drive was just not cutting it anymore.  I decided to build a Linux box running Xubuntu because of the versatility and stability Linux provides, and I found <a href="http://www.bit-tech.net/bits/2007/06/05/build_your_own_server/1">a how to article</a> a few weeks back on Digg which outlined the entire process.



After the server was up and running I decided that I wanted my computer to auto-mount my Samba drive whenever I was at home.   Using a combination of an AppleScript saved as an application and a free software for OS X, <a href="http://metaquark.de/homezone/">Home Zone</a>, I was able to have my computer identify when I'm at home and only launch my Samba drive when I'm here.



Let's get started:



The first thing I did was searched Google and <a href="http://forums.macosxhints.com/archive/index.php/t-16189.html">found an AppleScript</a> to mount my Samba drive.  <a href="http://www.divshare.com/download/886266-ce9">It can be downloaded as a .txt here</a> (I can't paste it into blogger b/c of errors).



After I replaced the server information with my own I saved the script as an application and dropped it into my applications folder.  If I had a desktop I could just launch the script every time I booted my computer (system preferences -&gt; accounts -&gt; login items), but since I have a laptop I only wanted the drive to mount when I was at home where the drive is.



There are several free location automators for OS X and after trying a few I decided to use <a href="http://metaquark.de/homezone/">Home Zone</a> because it was the easiest to configure:<ol> 
<li>Install and launch Home Zone </li>
 
<li>Click on the Home Zone icon in your menu bar and select "Configure" </li>
 
<li>In the "Zones" section click the plus arrow and name your new zone (Home in my case). </li>
 
<li>In the "Triggers" section click the plus arrow and select the following options: </li>
 

<ul> 
<li>When "all" of the following are available </li>
 
<li>Kind: "Airport Network" </li>
 
<li>Network: "Your wireless Network Name" </li>
 
<li>Check the "Only when connected" box </li>
</ul> 
<li>In the "Actions - Entering the Zone" section click the plus arrow.  Use the following configuration:

 </li>
 

<ul> 
<li>Action: Open File </li>
 
<li>Drag the Samba mounting AppleScript into the space right below the action pull down menu (it should say "Drag any file here")



<img alt="" border="0" id="BLOGGER_PHOTO_ID_5074058409404225250" src="{{ site.url }}/assets/images/posts/2007-06-09-image-0001.jpg" style="margin: 0px auto 10px; display: block; text-align: center; "/> </li>
</ul></ol>That's it...you're done!  Now anytime you are on your home network your samba drive will automount.

<workgroup><user><pwd><server></server></pwd></user></workgroup>