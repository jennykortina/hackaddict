---
author: kortina
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-2822038850790350964
blogger_orig_url: https://www.hackaddict.net/2007/06/quick-tip-delete-contents-of-file.html
date: '2007-06-13T20:23:00.000-04:00'
layout: post
modified_time: '2007-06-13T20:25:10.637-04:00'
redirect_from: /2007/06/quick-tip-delete-contents-of-file.html
tags:
- nix
- tip
title: 'Quick Tip: Delete the Contents of a File without Removing and Recreating It'
---

I had to clear out some log files on one of the iminlikewithyou servers yesterday, but I didn't want to delete and recreate the files because I thought that might screw up permissions.  I'd been meaning to learn how to zero out a file to empty contents for a while, so I took this opportunity to figure it out.



Do all this from the command line or terminal.



This will create a new file named t whose contents is the word "test":

<b>$ echo "test" &gt; t</b>



<b>more</b> will display the contents of the file:

<b>$ more t</b>

<b>test</b>



Here's the new trick I learned.  <b>cat</b> reads the contents of <b>/dev/null</b> (which contains nothing) and <b>&gt;</b> writes this into <b>t</b>

<b>$ cat /dev/null &gt; t</b>



Now <b>t</b> contains nothing:

<b>$ more t</b>



Get rid of it (don't do this to your logfile)

<b>$ rm t</b>