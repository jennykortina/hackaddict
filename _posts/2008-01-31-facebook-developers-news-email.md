---
author: kortina
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-4837566252169803044
blogger_orig_url: https://www.hackaddict.net/2008/01/facebook-developers-news-email.html
date: '2008-01-31T17:31:00.000-05:00'
layout: post
modified_time: '2008-01-31T17:32:52.421-05:00'
redirect_from: /2008/01/facebook-developers-news-email.html
tags:
- tip
title: Email Subscribe to Important News Feeds
---

Sometimes you want to stay on top of a news feed, and if you're as ruthless with Google Reader as I am, it can be easy to miss posts.<br/><br/>For example, I want to stay informed about changes to the Facebook API, because they can effect my existing code.  I used feedburner to create an email alert I can subscribe to for their developer news blog that has important announcements about the API:<br/><br/><form action="http://www.feedburner.com/fb/a/emailverify" method="post" onsubmit="window.open('http://www.feedburner.com/fb/a/emailverifySubmit?feedId=1608741', 'popupwindow', 'scrollbars=yes,width=550,height=520');return true" style="border: 1px solid #cccccc; padding: 3px; text-align: center" target="popupwindow">Enter your email address: <input name="email" style="width: 140px" type="text"/> <input name="url" type="hidden" value="http://feeds.feedburner.com/~e?ffid=1608741"/> <input name="title" type="hidden" value="Facebook Developers News - Email Subscription"/> <input name="loc" type="hidden" value="en_US"/> <input type="submit" value="Subscribe"/></form><br/><br/>Here is the feed I entered into Feedburner:<br/><a href="http://developers.facebook.com/news.php?blog=1&amp;format=xml"> http://developers.facebook.com/news.php?blog=1&amp;format=xml</a>