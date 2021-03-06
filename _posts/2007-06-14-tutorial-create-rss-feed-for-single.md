---
author: kortina
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-6405072238479240278
blogger_orig_url: https://www.hackaddict.net/2007/06/tutorial-create-rss-feed-for-single.html
date: '2007-06-14T00:23:00.000-04:00'
layout: post
modified_time: '2007-06-14T00:47:06.196-04:00'
redirect_from: /2007/06/tutorial-create-rss-feed-for-single.html
tags:
- tutorial
- reviewed
thumbnail: '{{ site.url }}/assets/images/thumbnails/2007-06-14-image-0000.png'
title: 'Tutorial: Create an RSS Feed For a Single Author of Your Blogger Blog Using
  Yahoo Pipes and Import It into Facebook'
---

One thing I have always found kind of annoying about <a href="http://blogger.com">blogger</a> is that you can't get RSS feeds for a particular label or author.  Today, I wanted to import my <a href="http://hackaddict.net" title="hackaddict.net">hackaddict</a> posts into Facebook Notes, but I didn't want to take credit for my sister's work, so I had to come up with a way to make an RSS Feed of only the posts I authored.



To do this, I used <a href="http://pipes.yahoo.com" title="Pipes: Rewire the web">Yahoo Pipes</a>, a pretty cool tool for mixing / manipulating / mashing up RSS and atom feeds.  First, I made a new Pipe and used the <b>Fetch Feed</b> tool to add as a source the hackaddict feed: <a href="http://feeds.feedburner.com/hackaddict" title="hackaddict.net">http://feeds.feedburner.com/hackaddict</a>.

<img alt="" border="0" id="BLOGGER_PHOTO_ID_5075774805763213330" src="{{ site.url }}/assets/images/posts/2007-06-14-image-0000.png" style="display:block; margin:0px auto 10px; text-align:center; "/>



Then, I piped this through the <b>Filter Operator</b> and blocked out items written by jenny.  (I also could have done the opposite and permitted items only by me.  That's how you would do it if there were more than 2 authors and you wanted only one person's posts.)

<img alt="" border="0" id="BLOGGER_PHOTO_ID_5075774968971970594" src="{{ site.url }}/assets/images/posts/2007-06-14-image-0001.png" style="display:block; margin:0px auto 10px; text-align:center; "/>



Then I just sent this into <b>Pipe Output</b>, Saved, and published everything, and I had an RSS feed of my posts: <a href="http://pipes.yahoo.com/pipes/pipe.info?_id=HLB4uisa3BGDG3tTJphxuA" title="Pipes: kortina's hackaddict posts">http://pipes.yahoo.com/pipes/pipe.info?_id=HLB4uisa3BGDG3tTJphxuA</a>.



(<h4>My thoughts on pipes</h4>

It's pretty cool and powerful, but a bit difficult to figure out.  Also, it would be nice if they provided a way to use the tool programmatically without the GUI.  Definitely worth checking out, but only if you have some time on your hands.

) 



To import into <a href="http://www.facebook.com/" title="Facebook | Incompatible Browser">Facebook</a> Notes, you need to click the Notes Application in your sidebar, then <b>Edit Import Settings</b> under <b>Notes Settings</b> in the right sidebar of the Notes Page.  Once there, you just enter in an RSS feed url, and your blog posts will be imported as Notes on Facebook.

<img alt="" border="0" id="BLOGGER_PHOTO_ID_5075775175130400818" src="{{ site.url }}/assets/images/posts/2007-06-14-image-0002.png" style="display:block; margin:0px auto 10px; text-align:center; "/>

<img alt="" border="0" id="BLOGGER_PHOTO_ID_5075775402763667522" src="{{ site.url }}/assets/images/posts/2007-06-14-image-0003.png" style="display:block; margin:0px auto 10px; text-align:center; "/>

<img alt="" border="0" id="BLOGGER_PHOTO_ID_5075775527317719122" src="{{ site.url }}/assets/images/posts/2007-06-14-image-0004.png" style="display:block; margin:0px auto 10px; text-align:center; "/>