---
author: kortina
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-1454892619477690610
blogger_orig_url: https://www.hackaddict.net/2007/06/quick-tip-regular-expressions-for.html
date: '2007-06-28T20:46:00.000-04:00'
layout: post
modified_time: '2007-06-28T20:52:55.533-04:00'
redirect_from: /2007/06/quick-tip-regular-expressions-for.html
tags:
- textmate
- tip
thumbnail: '{{ site.url }}/assets/images/thumbnails/2007-06-28-image-0000.png'
title: 'Quick Tip: Regular Expressions for Everyday Tasks'
---

(Don't miss this <a href="http://www.cuneytyilmaz.com/prog/jrx/" title="JRX: real-time JavaScript RegExp evaluator - cuneytyilmaz.com">totally sweet, find-as-you-type regexp tester</a>!)



Jenny (THE hackaddict) asked me today how to quickly reformat an html document she was editing, and the best solution turned out to be using a regular expression find and replace.  Regexps can look a little scary at first, but they're actually pretty easy to learn, super useful for tedious text-formatting you might do everyday, and they can even actually be kind of fun to write once you get the hang of them.  (I regard them as brainteasers.)



For a simple example of how you might use a regular expression, suppose someone sent you a list of email addresses like this:

<b>

jawn0@gmail.com

jawn1@gmail.com

jawn2@gmail.com

jawn3@gmail.com

jawn4@gmail.com

jawn5@gmail.com

jawn6@gmail.com

jawn7@gmail.com

jawn8@gmail.com

jawn9@gmail.com

</b>

and you wanted to change this list to a comma separate list that you could put in the <b>To:</b> field of your email client like this:

<b>jawn0@gmail.com,jawn1@gmail.com,jawn2@gmail.com,jawn3@gmail.com,jawn4@gmail.com, jawn5@gmail.com,jawn6@gmail.com,jawn7@gmail.com,jawn8@gmail.com,jawn9@gmail.com</b>



If you have only 10 email addresses, it might be fairly easy just to arrow to the end of each line, hit delete, and type a comma, but if you have 20, 100, or 1000 email addresses, that would simply be a waste of time.



A smarter way to do this would be to do a <b>find and replace</b> on end-of-line characters substituting commas.  You could accomplish this with any text-editor that allows regular expression search, such as <a href="http://macromates.com/" title="TextMate — The Missing Editor for Mac OS X">Textmate</a>.  



Open your list in a new document, then open a <b>Find</b> dialogue box.  In the <b>Find:</b> field, enter 

<b>(m)\n</b>



<img alt="" border="0" id="BLOGGER_PHOTO_ID_5081282250821783218" src="{{ site.url }}/assets/images/posts/2007-06-28-image-0000.png" style="display:block; margin:0px auto 10px; text-align:center; "/>

<img alt="" border="0" id="BLOGGER_PHOTO_ID_5081282036073418402" src="{{ site.url }}/assets/images/posts/2007-06-28-image-0001.png" style="display:block; margin:0px auto 10px; text-align:center; "/>



The <b>\n</b> stands for an end-of-line character, and I put a <b>(m)</b> before it because I knew that all of the email address lines ended with the character m.  (Even though this was not absolutely necessary, I did this because there was some other text that I did not want to effect and it also allowed me to demonstrate another facet of regexps.)  The parentheses <b>()</b> around the m capture and save whatever they enclose.  Since there is only one set of parentheses, they are stored in a variable named <b>$1</b> that we can use in the replace field.  (If there were multiple parentheses, they would be stored in variables $2, $3, etc.)



In the <b>Replace:</b> field, I entered 

<b>$1,</b>

This inserts whatever was captured by the first set of parentheses (viz. <b>m</b>) and a comma.  Clicking <b>Replace All</b> converts linebreaks to commas for all lines ending with <b>m</b>.



This is a somewhat trivial example that doesn't do full justice to the power of regular expressions, but if I could recommend one piece of programming knowledge to non-programmers, it would be "learn regular expressions."  I use them constantly to automate tedious tasks and they've saved me countless hours.



<a href="http://www.regular-expressions.info/javascriptexample.html" title="JavaScript RegExp Example: Regular Expression Tester">This page</a> has some great info on how to use regular expressions, and I recently discovered a <a href="http://www.cuneytyilmaz.com/prog/jrx/" title="JRX: real-time JavaScript RegExp evaluator - cuneytyilmaz.com">web-based regular expression tester inspired by the magnificent RX-toolkit in Komodo IDE</a> that is a great place to experiment with regexps.  You can enter in some sample text to search, then try writing regular expressions and watch them match as you type in real time--indispensable!