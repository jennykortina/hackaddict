---
author: kortina
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-4954263465432580687
blogger_orig_url: https://www.hackaddict.net/2007/12/javascript-bookmarklet-to-get-referral.html
date: '2007-12-30T20:20:00.000-05:00'
layout: post
modified_time: '2007-12-30T20:49:25.614-05:00'
redirect_from: /2007/12/javascript-bookmarklet-to-get-referral.html
tags:
- tip
title: Javascript Bookmarklet to Get a Referral Code for an Amazon Product Page you
  are Viewing
---

I frequently find myself needing an amazon product link and needing to jump through all sorts of hoops to get a product referral link.  What usually ends up happening is that after locating the correct link type (usually plain) and trying to search for the product through the this page:<br/><br/><img src="http://content.screencast.com/media/b7b90b33-fa07-42ad-ac29-def1b0ec1c32_5e452931-40a1-4238-bb2d-fdbc01f61523_static_0_0_00000057.png"/><br/><br/>This search never seems to work as well as the regular search on <a href="http://amazon.com/">amazon.com</a>, so I end up going there, searching for the product, copying the ASIN out of the url, going bakc to the affiliates search page, and pasting the ASIN in there.<br/><br/>This bookmarklet automates all that.  Just find the product for which you want a link on amazon, click the bookmarklet, and it will take you to the amazon associates 'build link' page for that product.<br/><br/>Drag this bookmarklet into your bookmarks toolbar to use it:<br/><br/><blockquote><a href="javascript:var%20re%3D%2F%5C%2F%28%5B0-9A-Z%5D%7B10%2C10%7D%29%5B%5C%2F%5C%3F%5D%3F%2Fi%3B%20var%20m%20%3D%20location.toString%28%29.match%28re%29%3B%20if%20%28m%20%21%3D%20null%29%20%7B%20location%20%3D%20%27http%3A%2F%2Fassociates.amazon.com%2Fgp%2Fassociates%2Fnetwork%2Fbuild-links%2Findividual%2Fget-html.html%3Fasin%3D%27%2Bm%5B1%5D%2B%27%26linkType%3Dstatic-text%27%3B%20%7D%20else%20%7Balert%28%22Could%20not%20parse%20ASIN%22%29%3B%20%7D">getASIN</a></blockquote><br/><br/>Here's a link I made for a book I highly recommend:<br/><a href="http://www.amazon.com/gp/product/0307353133?ie=UTF8&amp;tag=kortina-grease-20&amp;linkCode=as2&amp;camp=1789&amp;creative=9325&amp;creativeASIN=0307353133">The 4-Hour Workweek: Escape 9-5, Live Anywhere, and Join the New Rich</a><img alt="" border="0" height="1" src="http://www.assoc-amazon.com/e/ir?t=kortina-grease-20&amp;l=as2&amp;o=1&amp;a=0307353133" style="border:none !important; margin:0px !important;" width="1"/>