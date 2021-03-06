---
author: jenny
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-6057025414693724022
blogger_orig_url: https://www.hackaddict.net/2008/10/track-craigslist-page-views.html
date: '2008-10-22T08:00:00.002-04:00'
layout: post
modified_time: '2008-10-22T08:55:13.796-04:00'
redirect_from: /2008/10/track-craigslist-page-views.html
tags:
- tutorial
- website
- craigslist
thumbnail: '{{ site.url }}/assets/images/thumbnails/2008-10-22-image-0000.png'
title: Track Craigslist Page Views
---

<img alt="" border="0" id="BLOGGER_PHOTO_ID_5259727251907338690" src="{{ site.url }}/assets/images/posts/2008-10-22-image-0000.png" style="margin: 0px auto 10px; display: block; text-align: center; "/>I saw <a href="http://benperove.com/howto/track-page-views-on-craigslist/">this article</a> a while back <a href="http://lifehacker.com/software/how-to/track-page-views-on-craigslist-288618.php">(thanks to lifehacker)</a> which explained how to track page views on Craigslist.  I loved the idea but did not love the implementation: it required hosting your own image and using either a third party web application (but did not describe the process) or using a shell script to list the number of times the server loaded the image.  Today I am going to explain a much easier way to track your Craigslist page views which does not involve hosting your image or using complicated scripts (my mom could use this method).<ol> 
<li>Create a regular Craigslist ad making sure you include at least one image </li>
 
<li>Publish your Craigslist ad and go to the link Craigslist provides to "View your ad"

 </li>
 
<li>Right click on your image and select "Copy Image Location"<img alt="" border="0" id="BLOGGER_PHOTO_ID_5259717780393607298" src="{{ site.url }}/assets/images/posts/2008-10-22-image-0001.png" style="margin: 0px auto 10px; display: block; text-align: center; "/> </li>
 
<li>We are done on Craiglist for now.  Open a separate browser window and navigate to www.bit.ly </li>
 
<li>Create a new account.  After you successfully create your account you will be automatically logged in. </li>
 
<li>Paste your link that we copied from Craigslist into the "Enter Web Address (URL) Here" box<img alt="" border="0" id="BLOGGER_PHOTO_ID_5259710592659056034" src="{{ site.url }}/assets/images/posts/2008-10-22-image-0002.png" style="margin: 0px auto 10px; display: block; text-align: center; "/> </li>
 
<li>Click the "Shorten" button </li>
 
<li>You will be provided with a new, shortened URL.  Click the "Copy" button. </li>
 
<li>Now navigate back to your Craigslist page, and choose the edit my ad option. </li>
 
<li>Go to the images section and remove the image that we turned into a Bit.ly link (whatever image you right clicked on earlier and selected "Copy Image Location"). </li>
 
<li>Click "Make Changes" (This is an important step, you MUST save it without the image for this to work) </li>
 
<li>A preview of your ad should pop up and your picture should be gone.  If your picture is gone, click the "Edit" button again

 </li>
 
<li>Go to the bottom of your ad and insert this code:<img alt="" border="0" id="BLOGGER_PHOTO_ID_5259718802725674722" src="{{ site.url }}/assets/images/posts/2008-10-22-image-0003.png" style="margin: 0px auto 10px; display: block; text-align: center; "/> </li>
 
<li>Click "Make Changes" to save the image

 </li>
 
<li>Finally, navigate back to your bit.ly account and look for you image link (it will be at the top of the "Recent" list).  Click the "Info" button to see your link stats.<img alt="" border="0" id="BLOGGER_PHOTO_ID_5259712810860388498" src="{{ site.url }}/assets/images/posts/2008-10-22-image-0004.png" style="margin: 0px auto 10px; display: block; text-align: center; "/> </li>
</ol>