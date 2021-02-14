---
author: jenny
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-3866699459698992822
blogger_orig_url: https://www.hackaddict.net/2007/06/tutorial-iphone-windows-mobile-skin.html
date: '2007-06-29T10:35:00.001-04:00'
layout: post
modified_time: '2008-02-21T23:18:36.593-05:00'
redirect_from: /2007/06/tutorial-iphone-windows-mobile-skin.html
tags:
  - tutorial
  - mobile
thumbnail: '{{ site.url }}/assets/images/thumbnails/2007-06-29-image-0000.JPG'
title: 'Tutorial: iPhone Windows Mobile Skin'
---

<img alt="" border="0" id="BLOGGER_PHOTO_ID_5086117423366345314" src="{{ site.url }}/assets/images/posts/2007-06-29-image-0000.JPG" style="margin: 0px auto 10px; display: block; text-align: center; "/>



UPDATE: I've updated the skin so that it now displays number of missed calls and number of new text messages. Have fun!



UPDATE V1.3: The weather icon now displays the current temp (aka the last temp weather watcher retrieved) instead of "73" all the time. That being said, the current version of the skin must have weather watcher mobile installed to work correctly.



UPDATE V1.4: Youtube anyone?



This has been tested and works in both WM5 and WM6.



I read an <a href="http://lifehacker.com/software/hack-attack/turn-your-windows-mobile-phone-into-an-iphone-269055.php">article on Lifehacker</a> recently which described two different methods to skin your windows mobile phone to look like an iPhone. The first method uses a program that constantly runs on your phone to apply the skin, while the second method uses a combination of the mobile aps RL today and wisbar advance to apply the theme.



I started out using the first method because the Lifehacker author recommended it. I must admit it looked awesome, but it was highly unstable and I never got any notification icons for things like missed calls or text messages (they were there but behind the skin). Another major flaw with it was that since it was a program I could accidentally close the skin if I got overzealous while closing other open applications.



<a href="http://www.angelfire.com/planet/iphone/">The second method</a> was harder to set up, and it took me forever to get it look exactly how I wanted; however, many of the headaches and frustrations were caused by inadequate instructions which I amended and added a lot of information to for ya'll. The included background was also causing a problem, so I redid it and included it in the zip. With my instructions this method should only take you about thirty minutes to set up and the results are stunning. You will have a reliable and functional skin in no time.



I started by doing a hard reset on my phone (<a href="http://www.amazon.com/gp/product/B000FENIIW?ie=UTF8&amp;tag=httpkortinnet-20&amp;linkCode=as2&amp;camp=1789&amp;creative=9325&amp;creativeASIN=B000FENIIW">I have a AT&amp;T 8125 Smartphone</a>). Next I installed all of the applications and then I was finally ready for the skin.

<a href="http://www.divshare.com/download/1139147-d61">

</a><a href="http://www.divshare.com/download/1233462-03a">Download the zip file of the skin and the programs used here.</a><a href="http://rapidshare.com/files/40836647/skin.zip.html">

</a>

If you don't already have it get a sync software for your phone here:

<a href="http://www.markspace.com/testing/">Mac - Missing Sync V4.0 Public Beta</a>

<a href="http://www.microsoft.com/windowsmobile/activesync/activesync45.mspx">Windows</a>



Installing the utilities, programs, and skin using sync software:



<span style="font-weight: bold;">Utilities:</span>

<ol><li><a href="http://www.microsoft.com/downloads/details.aspx?familyid=9655156b-356b-4a2c-857c-e62f50ae9a55&amp;displaylang=en">.net Framework</a> - needed to run many of the applications ie Text Message Threader and Weather

</li><ol><li>The cab is located in: iPhone\Programs\netframework.cab

</li><li>Drag the Cab into the "My Documents" folder on your phone using sync software

</li><li>Navigate to the cab on your phone and install it onto your phone by clicking on it</li><li>You must restart your device to complete the installation. Hit ok.

</li></ol><li><a href="http://www.phm.lu/Products/PocketPC/RegEdit/">PHM Registry Editor</a> (optional software that I used to make my phone automatically update it's time using cell towers)

</li><ol><li>Drag the Cab into the "My Documents" folder on your phone using sync software

</li><li>Navigate to the cab on your phone and install it onto your phone by clicking on it</li><li>Open PHM Registry Editor</li><li>Navigate to "HKEY_LOCAL_MACHINE\SOFTWARE\OEM\Phone Setting</li><li>Change the "ShowTimeZone" value from 0 to 1</li><li>Now navigate to Settings\Phone\Time Zones tab. Check the "Automatic change time zone and clock." box. Your phone will now automatically set the time for you.

</li></ol></ol><span style="font-weight: bold;">Programs (In order from top to bottom and left to right):</span>

<ol><li>SMS Icon: <a href="http://benhirashima.com/software/">Text Man</a> - Text Message threader</li><ol><li>The cab is located in: iPhone\Programs\TxtMan.cab</li><li>Drag the Cab into the "My Documents" folder on your phone using sync software

</li><li>Navigate to the cab on your phone and install it onto your phone by clicking on it</li><li>Navigate to the Windows\Startup directory on your phone and delete the "TxtMan.ink" Although it's cool, we don't want TextMan starting every time we turn on our phones.

</li></ol><li>Calendar Icon: Left Alone but going to be Google calendar

</li><li>Photos Icon: Left Alone</li><li>Camera Icon: Left Alone</li><li>Calculator: <a href="http://www.smartphone-freeware.com/download-gcalc-v1-0.html">Gcalc</a>

</li><ol><li>The cab is located in: iPhone\Programs\gCalc\gcalc.CAB</li><li>Drag the Cab into the "My Documents" folder on your phone using sync software

</li><li>Navigate to the cab on your phone and install it onto your phone by clicking on it</li></ol><li>Charts (on my build) - is directed to the "File Explorer" if you want to change the path edit the

</li><li>Maps Icon: Google Maps Mobile

</li><ol><li>Use your built in web browser, ie, to navigate to: www.google.com/gmm </li><li>Select "Download Google Maps"

</li><li>Select "Open File after Download"</li></ol><li>Weather Icon: <a href="http://www.pocketpcfreeware.com/en/index.php?soft=1626">Weather Watcher Mobile</a>

</li><ol><li>The cab is located in: iPhone\Programs\WWM105.cab</li><li>Drag the Cab into the "My Documents" folder on your phone using sync software

</li><li>Navigate to the cab on your phone and install it onto your phone by clicking on it</li></ol><li>Notes: Left Alone

</li><li>Clock Icon: Left Alone</li><li>Settings Icon: Left Alone</li><li><a href="http://ppcgeeks.com/youtube-mobile-a-how-to-for-treo-6700-etc-t6125,highlight,youtube.html">Youtube Icon: </a>Stream Youtube through ie using HTC touch streaming media player.

The files are located in: iPhone\Programs\Youtube

WM5 Users:

<ol><li>Copy contents of the Step 1 folder into your \Windows directory of your phone.

</li><li>Copy Step#2- Streaming_210.cab to your device and install to main memory

</li><li>Soft-reset

</li><li>Copy Step #3-HTC_Streaming_Media.cab to your device and install to main memory</li></ol>WM6 Users:

</li><ol><li>Copy Step #3-HTC_Streaming_Media.cab to your device and install to main memory</li><li>Soft reset</li><li>Enjoy!

</li></ol><li>Phone Icon: <a href="http://www.pocketcm.com/">Contact Manager</a> - Touch Screen Only - Changes your contact list to "Flick and Scroll" menu</li><ol><li><a href="http://www.pocketcm.com/dl/ContactManager-0.10.zip">Download a zip of the program here.</a>

</li><li>Unzip the the downloaded program

</li><li>Drag the ENTIRE Contact Manager folder from your computer to your phone. I put it in the Program Files directory.

</li><li>Make sure that your contacts are stored on your phone and not on your sim card. If they are not on your phone they will not be displayed by iContact.</li><ol><li>On my phone I navigated to Programs\Sim Manager. From there I chose: Tools&gt;Select All, Tools&gt;Copy to Contacts</li></ol></ol><li>Mail Icon: gmail Mobile</li><ol><li>Use your built in web browser, ie, to navigate to: gmail.com/app

</li><li>Select "Download Gmail"</li><li>Install Midlet? "Yes"</li></ol><li>Internet Icon: Opera Mini 4 Beta</li><ol><li>Use your built in web browser, ie, to navigate to: mini.opera.com/beta </li><li>Select "Download Opera Mini"</li><li>Install Midlet? "Yes"</li></ol><li>Ipod Icon: <a href="http://picard.exceed.hu/tcpmp/test/">TCPMP</a><span style="text-decoration: underline;"></span><a href="http://www.videolan.org/vlc/download-wince.html"></a></li><ol><li>The cab is located in: iPhone\Programs\tcpmp.cab</li><li>Drag the Cab into the "My Documents" folder on your phone using sync software

</li><li>Navigate to the cab on your phone and install it onto your phone by clicking on it</li><li>If you ever need codec plugins, ie for divx, you can find them <a href="http://picard.exceed.hu/tcpmp/test/">here</a>.

</li></ol></ol>Now that you have all the programs installed go ahead and do a soft reset and then we will install the skin.



<span style="font-weight: bold;">Installing the Skin:</span>

<ol><li>Today:

</li><ol><li>Start by removing everything from your home screen:</li><ol><li>Settings&gt;Today</li><li>Remove everything from your Today Screen</li></ol><li>Next copy the skin from: iPhone\Skin\black.tsk to your My Documents folder on your phone.</li><li>Go to Settings&gt;Personal&gt;Today and apply the theme.

</li></ol><li>RL Today

</li><ol><li>The cab is located in: iPhone\Skin\rlToday\rlToday.cab</li><li>Drag the Cab into the "My Documents" folder on your phone using sync software</li><li>Navigate to the cab on your phone and install it onto your phone by clicking on it</li><li>Now take the iPhone file and put it in the rlToday file

under Programs.

</li><li>rlToday should now be on the home screen. Click and hold on the home screen until an "Option" button appears. Click on it.</li><li>Select iPhone as your skin and then set up all your programs under the Applications tab, using the pictures in the iPhone folder for the icons. Make sure you skip

the calendar, and phone applications. Those are built into the .xml skin file (they are animated or updated via registry references). So, from top to bottom your programs and icons should be:





<ul><li><span style="font-weight: bold;">SMS:</span> blank.png,

</li><li><span style="font-weight: bold;">Photos:</span> rl_photo.png, \Windows\pimg.exe

</li><li><span style="font-weight: bold;">Camera:</span> rl_cam.png, \Windows\Camera.exe

</li><li><span style="font-weight: bold;">Youtube:</span> rl_youtube.png, \Windows\iexplore.exe Command Line: http://m.youtube.com</li><li><span style="font-weight: bold;">Finder:</span> rl_finder.png, \Windows\fexplore.exe

</li><li><span style="font-weight: bold;">Maps: </span>rl_maps.png, \Program Files\GoogleMaps\GoogleMaps.exe

</li><li><span style="font-weight: bold;">Weather:</span> blank.png, \Program Files\Weather Watcher\WeatherWatcher.exe

</li><li><span style="font-weight: bold;">Calculator:</span> rl_cal.png, \Program Files\gCalc|gCalc.exe</li><li><span style="font-weight: bold;">Notes:</span> rl_notes.png, \Windows\notes.ese

</li><li><span style="font-weight: bold;">Settings:</span> rl_settings.png, \Windows\CommManger.exe (that's a personal preference)

</li><li><span style="font-weight: bold;">Phone:</span> blank.png, \Program Files\Contact Manager-.10\ContactManager.exe

</li><li><span style="font-weight: bold;">Mail:</span> rl_mail.png, \My Documents\My Midlets\Gmail.ink

</li><li><span style="font-weight: bold;">Web:</span> rl_navi.png, \My Documents\My Midlets\Opera.ink</li><li><span style="font-weight: bold;">Media:</span> rl_ipod.png, \Program Files\TCPMP\player.exe





</li></ul></li></ol><li>Get rid of the UGLY scroll bar:</li><ol><li>Windows&gt;Startup

</li><li>Delete/move the battery and connections tray programs.</li></ol><li>Wisbar Advance</li><ol><li>The cab is located in: iPhone\Skin\Wisbar Advance 2\WisbarAdvance2.cab</li><li>Drag the Cab into the "My Documents" folder on your phone using sync software</li><li>Navigate to the cab on your phone and install it onto your phone by clicking on it</li><li>Copy the the included theme from: iPhone\Skin\Wisbar Advance 2\iPhone to: the Wisbar themes folder in Programs&gt;Lakeridge&gt;Wisbar Advance</li><li>Go to Start&gt;Programs&gt;Wisbar Advance and open up the settings. Apply the theme and exit out of the settings manager.</li></ol><li>VJ Toggle - make the softkeys vanish!</li><ol><li>The cab is located in: iPhone\Skin\VJToggleToday\VJToggleToday.cab</li><li>Drag the Cab into the "My Documents" folder on your phone using sync software</li><li>Navigate to the cab on your phone and install it onto your phone by clicking on it</li><li>Probably need to do a soft reset to see results

</li></ol><li>Installing the Dialer:</li><ol><li>The cab is located in: iPhone\Skin\Dialpad\iphone.cab</li><li>Drag the Cab into the "My Documents" folder on your phone using sync software

</li><li>Navigate to the cab on your phone and install it onto your phone by clicking on it</li><li>You must restart your device to complete the installation. Hit ok</li></ol><li>Installing the Keyboard and skin:</li><ol><li>The cab is located in: iPhone\Skin\Keyboard\HappyTappingKeyboard.arm.cab</li><li>Drag the Cab into the "My Documents" folder on your phone using sync software

</li><li>Navigate to the cab on your phone and install it onto your phone by clicking on it</li><li>Copy the Skin folder from: iPhone\Skin\Keyboard\Skin to My Documents on your phone.</li><li>Go to Settings&gt;Personal&gt;Input and select Happy Tapping Keyboard.</li><li>Click Options and locate the QVGA files in KeyboardSkin. P is for Portrait and L is for Landscape.</li></ol></ol><span style="font-weight: bold;">Finally, we're almost done!</span>



Do a soft reset. You will notice that the bottom of the screen has what I like to call a "dead space." To eliminate this eye sore do a search in your windows directory for ".gif" Search through the results until you find a file named something like: "tdywater.gif" (mine was called "tdywater_240_320.gif"). If necessary rename the included "tdywater.gif" file to whatever your search yielded. Drag the included file onto your pocket pc to replace the existing one. Do a soft reset.



<span style="font-weight: bold;">Congratulations: </span>You now have an iPhone skin on your WM5 PDA/Pocket PC!!!




<a href="http://www.amazon.com/gp/product/B000FI73MA/ref=amb_link_6369712_1?pf_rd_m=ATVPDKIKX0DER&amp;pf_rd_s=center-1&amp;pf_rd_r=15908FZGGRFY8ZNBATEV&amp;pf_rd_t=101&amp;pf_rd_p=365511101&amp;pf_rd_i=507846?tag=hack-20" style="font-weight: bold;">If you found this tutorial helpful please take a second and check out our sponsor's new revolutionary wireless reading device: The Kindle.</a>




Thanks!!!!
