---
author: kortina
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-4854642631592530077
blogger_orig_url: https://www.hackaddict.net/2007/02/obfuscate-email-address-for-display-on.html
date: '2007-02-22T11:38:00.000-05:00'
layout: post
modified_time: '2007-02-22T11:16:29.514-05:00'
redirect_from: /2007/02/obfuscate-email-address-for-display-on.html
tags:
- website
- tip
title: Obfuscate an Email Address for Display on a Web Page and Prevent Robots from
  Spamming You
---

There are lots of times I want to put an email address on a web page, but I always fear the spam bots that harvest email addresses and clog your inbox with tons of shit about drugs and mortgages.  A lot of times you'll see people do things like write jenn<span>y</span> <span> </span>[[[ <span> a<span>t</span> </span>]]] hack<span>addict</span> ((( dott ))) <span>ne</span>t<br /><br />The thing with this is that I think most robots are smart enough to figure out that's an email address, because there are only so many brackets and 'at' and 'dot' combinations that are commonly used.  If I have to do something like that (viz. if I don't have access to javascript), I put a bunch of garbage tags in the HTML to obscure things as much as possible:<br /><code><br />jenn&lt;span&gt;y&lt;/span&gt; &lt;span&gt; &lt;/span&gt;[[[ &lt;span&gt; a&lt;span&gt;t&lt;/span&gt; &lt;/span&gt;]]] hack&lt;span&gt;addict&lt;/span&gt; ((( dott ))) &lt;span&gt;ne&lt;/span&gt;t<br /></code><br /><br />That's still not an ideal solution because it's not much harder to parse and it looks like crap to the human user.  The user can't just click on the email to send a message since there's no mailto: link.  Furthermore, the user can't even copy and paste the email address because of all the brackets and reformatting.<br /><br />My ideal solution uses javascript to create a link that is human readable, obscured pretty nicely to prevent spam robots from harvesting it, and clickable with a mailto: link.  The basic idea is to mix up the email address itself in a really convoluted order, but concatenate a string in javascript that evaluates to the correct address.<br /><br /><code><br />&lt;script type="text/javascript"&gt;<br />var e = "hackaddic";<br />e = "@" + e;<br />e += "t.net";<br />e = "jenny" + e;<br />var nspm = "mailto";<br />nspm =  nspm + ":" + e;<br />nspm = "&lt;a href='" + nspm +"' title='Send Questions or Comments to'&gt;Contact&lt;/a&gt;";<br />document.onload += document.write(nspm);<br />&lt;/script&gt;<br /></code><br /><br />The above code works fine in a blogger template, a feat which took a little work to accomplish because of the way blogger checks for matching tags when it compiles your template.  You can see an example of this code at the top of the page.