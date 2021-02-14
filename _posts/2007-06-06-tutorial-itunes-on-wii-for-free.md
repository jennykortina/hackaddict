---
author: jenny
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-1148599944492015331
blogger_orig_url: https://www.hackaddict.net/2007/06/tutorial-itunes-on-wii-for-free.html
date: '2007-06-06T20:24:00.000-04:00'
layout: post
modified_time: '2007-07-08T17:16:04.182-04:00'
redirect_from: /2007/06/tutorial-itunes-on-wii-for-free.html
tags:
- windows
- freeware
- mac
thumbnail: '{{ site.url }}/assets/images/thumbnails/2007-06-06-image-0000.jpg'
title: 'Tutorial: iTunes on the Wii!!!'
---

UPDATE:  THE MYTUNESSRSS SOFTWARE HAS BEEN UPDATED.  PLEASE <a href="/2007/06/update-stream-itunes-on-wii.html">CLICK HERE</a> TO READ MORE ABOUT THE UPDATE AND DOWNLOAD THE SPECIAL PACKAGE.



This tutorial will show you how to stream your iTunes music library to your Wii through the Opera browser.  The Opera browser can be download to your Wii for free from the "Wii Shop Channel."  This tutorial will work with both a Mac and a PC.



Things you'll need:

*Nintendo Wii with Opera Browser Installed (free from the shop channel)

*iTunes

*<a href="http://www.codewave.de/products/mytunesrss/">MyTunesRss (once free, but now they are charging $22).</a>



Let's get started:<ol> 
<li>Make sure you have the latest version of <a href="http://www.apple.com/itunes/download/">iTunes</a> installed on your computer. </li>
 
<li>Make sure you have the latest version of the Opera browser installed on your Wii. </li>
 
<li>Download and install <a href="http://www.codewave.de/products/mytunesrss/">MyTunesRss</a> (select your operating system on the right hand side of the page and the download will begin). </li>
</ol>Configuring MyTunes RSS (from their page):<ol> 
<li>  When you start MyTunesRSS for the first   time, it automatically starts searching a file   named "iTunes Music Library.xml" in all   direc  tories   ins  ide your user home. You can cancel this process in case you want to select the file manually or you don't use iTunes at   all.  </li>
 
<li> To get started you need to configure at least one   data source, i.e. either the "iTunes Music Library.xml" or   at least one watch folder. The previously found   "iT  unes Music Library.xml" (if any was found) is already configured.   To select your own music library source clic  k the "Directories" tab and under the iTunes box click the "..." button.  From here browse to where ever your Library.xml is   sto  red on your computer.  I also configured a watch folder.  To do so click the "+" button next "Watch Folders" box.  Point that window to look at your iTunes music folder. 



<img alt="" border="0" id="BLOGGER_PHOTO_ID_5073134287060948610" src="{{ site.url }}/assets/images/posts/2007-06-06-image-0000.jpg" style="margin: 0px auto 10px; display: block; text-align: center; "/>

 </li>
 
<li> Then you need to do at least on  e initial   database   update  .   Under   the "Database" tab you   can trigger this update manually or   you will have to check the option for doing this automatically when the server starts. You can   also configure automatic updates at fixed   intervals while the server is running.



 <img alt="" border="0" id="BLOGGER_PHOTO_ID_5073134613478463122" src="{{ site.url }}/assets/images/posts/2007-06-06-image-0001.jpg" style="margin: 0px auto 10px; display: block; text-align: center; "/>

 </li>
 
<li> Now you need at least one user. Go to the user   management tab and create a new user.   Enter a username and password and check the   permissions for the use  r. You should start with a user with all permissions and no download and zip archive limit.   (You will not be able to download music or videos to your Wii...I already tried)

  </li>
 
<li> After creating the user you can start the serv  er. The server is started and MyTunesRSS checks if it is reachable and if there are any tracks in the database. If your server is up and running, you can test the web interface.



 <img alt="" border="0" id="BLOGGER_PHOTO_ID_5073135377982641826" src="{{ site.url }}/assets/images/posts/2007-06-06-image-0002.jpg" style="margin: 0px auto 10px; display: block; text-align: center; "/>

 </li>
 
<li> Open a web browser on the same computer that is running MyTunesRSS and enter "http://127.0.0.1:8080" in the address line. After a few seconds you should see the login page. Enter the username and password for the user you just created and click the login button. You should see the portal page. My  TunesRSS is working correctly now.



 <img alt="" border="0" id="BLOGGER_PHOTO_ID_5073133586981279346" src="{{ site.url }}/assets/images/posts/2007-06-06-image-0003.jpg" style="margin: 0px auto 10px; display: block; text-align: center; "/> 

  </li>
 
<li> Before you leave MyTunesRss click the "Server" tab once more.  Next click on the "Server Info" button.  When the pop window appears look in the "Internal Addresses" window.  Write one of them down (in my case it will be "http://192.168.10.147:8080" - see picture below). <img alt="" border="0" id="BLOGGER_PHOTO_ID_5073127848904971810" src="{{ site.url }}/assets/images/posts/2007-06-06-image-0004.jpg" style="margin: 0px auto 10px; display: block; text-align: center; "/> </li>
</ol>

Configuring the Wii:

<ol> 
<li>Load the "Internet Channel" </li>
 
<li>Click on the "WWW" icon </li>
 
<li>Enter in the IP address you wrote down in step 8 of "Configuring MyTunes RSS "   into the address bar.  In my case it was   "http://192.168.10.147:8080"  </li>
 
<li> Enter the username and password for the user you created earlier and click the log in button (I also clicked "Remember Me").  You should see a portal page.  Congratulations you can now stream your iTunes music to your Wii!!!  </li>
</ol>*I also saved the ip address " http://192.168.10.147:8080  " to my favorites and renamed it "iTunes" for easier access.  If you chose to remember your username and password earlier, every time you click on your new iTunes favorite item you will be automatically logged into your iTunes library for instant browsing.



 <a href="/2007/06/update-stream-itunes-on-wii.html">UPDATE: Making MyTunesRSS more Wii Friendly</a>