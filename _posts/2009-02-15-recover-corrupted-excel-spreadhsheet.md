---
author: jenny
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-7050003286329585500
blogger_orig_url: https://www.hackaddict.net/2009/02/recover-corrupted-excel-spreadhsheet.html
date: '2009-02-15T20:33:00.007-05:00'
layout: post
modified_time: '2009-02-15T21:58:41.180-05:00'
redirect_from: /2009/02/recover-corrupted-excel-spreadhsheet.html
tags:
- tutorial
thumbnail: '{{ site.url }}/assets/images/thumbnails/2009-02-15-image-0000.png'
title: Recover Corrupted Excel Spreadhsheet Files Using Only Excel for Free
---

My mom sent me an .xls file this evening that she had spent hundreds of hours working on and managed corrupt within a matter of minutes.  After a quick Google search I found lots of pay for programs to recover the file, but nothing quick and free.



 Things to note:

  

<ul> 
<li>This method can be time consuming if you have an Excel file with tons of individual workbooks. </li>
 
<li>We are only recovering the data, this method cannot recover the forumlas from cells.  Sorry! </li>
</ul> To recover a damaged Excel .xls File using only Excel: 

<ol> 
<li>Open a new blank Excel sheet </li>
 
<li>In cell A1 paste the following formula (without the quotes): " =  FileName  !A1 "  Make sure you replace the  FileName  with the name of your original document. </li>
 
<li>A window should pop up with the names of all your worksheets. Select the name of your first worksheet.  Click "Ok"<img alt="" border="0" id="BLOGGER_PHOTO_ID_5303204845101251794" src="{{ site.url }}/assets/images/posts/2009-02-15-image-0000.png" style="margin: 0px auto 10px; display: block; text-align: center;  width: 320px; height: 229px;"/> </li>
 
<li>The first cell of your original damaged worksheet should now appear in cell A1 of your new worksheet. Highlight cell A1 in your new workbook </li>
 
<li>Move your mouse into the lower right hand corner of cell A1 until the mouse pointer turns into a crosshair.  When the pointer turns into a crosshair click and hold moving your mouse down and right, filling the spreadhsheet up.   Continue to drag the mouse until you have selected area that is approximately the same size as the range of cells that contain the data in your original file.

<object class="BLOG_video_class" contentid="d1a357473f65698d" height="266" id="BLOG_video-d1a357473f65698d" width="320"></object> </li>
 
<li>After you have all of your data, highlight all the cells with data and select Edit&gt;Copy </li>
 
<li>Open a new worksheet </li>
 
<li>Select: Edit&gt;Paste Special&gt;Values  This step removes references to the damaged file and only leaves the data. </li>
 
<li>Repeat the above procedure for all worksheets in the workbook. </li>
</ol>There you have it, recover a damaged Excel file using only Excel!  Have fun!