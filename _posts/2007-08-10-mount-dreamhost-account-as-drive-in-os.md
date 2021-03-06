---
author: jenny
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-1555473201897978726
blogger_orig_url: https://www.hackaddict.net/2007/08/mount-dreamhost-account-as-drive-in-os.html
date: '2007-08-10T10:23:00.000-04:00'
layout: post
modified_time: '2007-08-10T14:06:14.134-04:00'
redirect_from: /2007/08/mount-dreamhost-account-as-drive-in-os.html
tags:
- tutorial
- freeware
- mac
thumbnail: '{{ site.url }}/assets/images/thumbnails/2007-08-10-image-0000.jpg'
title: 'Tutorial: Mount a Dreamhost Account as a Drive in OS X'
---

<img alt="" border="0" id="BLOGGER_PHOTO_ID_5096479279037235330" src="{{ site.url }}/assets/images/posts/2007-08-10-image-0000.jpg" style="margin: 0px auto 10px; display: block; text-align: center; "/>

Mounting your Dreamhost webservice as a drive in OS X makes SSH'ing into a breeze (literally drag and drop).  If you do not have a Dreamhost account, and would like one click on <a href="http://www.dreamhost.com/">this link</a> and use the referral code "HACKADDICT" to recieve $50 off any hosting package.



Now that you have a Dreamhost account you need 3 more things (and these are free and can be downloaded <a href="http://code.google.com/p/macfuse/">here</a>):<ol> 
<li><a href="http://code.google.com/p/macfuse/">MacFuse</a> </li>
 
<li><a href="http://code.google.com/p/macfuse/">SSHFS</a> </li>
 
<li><a href="http://www.sccs.swarthmore.edu/users/08/mgorbach/MacFusionWeb/">Macfusion</a> </li>
</ol>Setting up your Dreamhost drive is literally a breeze:

<ol> 
<li>Install MacFuse, SSHFS, and MacFusion </li>
 
<li>Go to Dreamhost and click on "Users - Manage Users." Then click "edit user" on the only user in the list.  You will then be able to find the following information which you need to be able to ssh into you account: </li>
<ol> 
<li> username:  my is jennykortina and underlined in red in the picture </li>
 
<li> server:  listed next your user name on the edditing user line.  mine is bazooka and is underlined in red in the picture

 </li>
 
<li> home directory:  my is /home/jennykortina and is circled in red in the picture

 </li>
 
<li>account type should be set to "shell account"<img alt="" border="0" id="BLOGGER_PHOTO_ID_5096478866720374882" src="{{ site.url }}/assets/images/posts/2007-08-10-image-0001.jpg" style="margin: 0px auto 10px; display: block; text-align: center; "/> </li>
</ol> 
<li>Now that you have the info you need, fire up MacFusion.  It should be an icon in your menu bar.  Click on the icon, scrol down to favorites, and click edit.<img alt="" border="0" id="BLOGGER_PHOTO_ID_5097064519870922898" src="{{ site.url }}/assets/images/posts/2007-08-10-image-0002.jpg" style="margin: 0px auto 10px; display: block; text-align: center; "/> </li>
 
<li>Click the "Plus" button in the bottom left hand corner of the new window that pops up.  Then select the "SSH" option </li>
 
<li>In the new window that pops up fill out each box accordingly: </li>
<ol> 
<li> Name:  name it whatever you want your drive to be called, I chose dreamhost </li>
 
<li> Server:  use the server name that we got earlier from dreamhost and use the following format: server.dreamhost.com (so mine is bazooka.dreamhost.com) </li>
 
<li> Port:  leave alone </li>
 
<li> Server Path:  use your home directory path from dreamhost (mine is /home/jennykortina) </li>
 
<li> Username:  use the username we got earlier from dreamhost (mine is jennykortin) </li>
 
<li> Authentication:  "Password" </li>
 
<li> Extra Options:  leave alone

<img alt="" border="0" id="BLOGGER_PHOTO_ID_5097071039631278242" src="{{ site.url }}/assets/images/posts/2007-08-10-image-0003.jpg" style="margin: 0px auto 10px; display: block; text-align: center; "/>

 </li>
</ol> 
<li>Click the "OK" button.  You should be back to the window with the plus and minus buttons in the botton corner and your new account should be there.  Check the "Auto" box next to the server name (this makes the server automount whenever you run macfusion). </li>
 
<li>Click "Mount."  Congratulations! Your Dreamhost drive should now appear as a drive in your finder windows! </li>
</ol>I have my Dreamhost drive only mount when I'm at home using a free program called <a href="http://metaquark.de/homezone/">Home Zone</a>.  To see a tutorial on location based mounting please check out <a href="/2007/06/tutorial-automount-samba-drive-when-at.html">this article.</a><a href="/2007/06/tutorial-automount-samba-drive-when-at.html">

</a>