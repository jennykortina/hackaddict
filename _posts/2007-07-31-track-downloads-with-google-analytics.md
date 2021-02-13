---
layout: post
title: Track Downloads with Google Analytics
date: '2007-07-31T00:06:00.000-04:00'
author: kortina
tags:
- tip
modified_time: '2007-07-31T09:30:19.523-04:00'
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-8703736589574225790
blogger_orig_url: https://www.hackaddict.net/2007/07/track-downloads-with-google-analytics.html
---

I am building a few Firefox extensions ( coming soon ) and I was trying to figure out the best way to track the number of downloads once I post them.  In my search, I found 2 great posts about some of the more advanced features of Google Analytics:<br /><br /><a href="http://www.blogstorm.co.uk/blog/advanced-google-analytics/">Advanced Use of Google Analyics</a><br /><br /><a href="http://www.blogstorm.co.uk/blog/google-analytics-tutorial/">Google Analytics Tutorial Part 2</a><br /><br />Here's how you would track a download, by the way:<br /><pre><br />&lt;a href=&quot;http://www.example.co.uk/files/map.pdf&quot;<br />onClick=&quot;javascript:urchinTracker (&apos;/downloads/map&apos;); &quot;&gt;<br /></pre>