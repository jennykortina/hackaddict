---
author: kortina
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-4683084925530178244
blogger_orig_url: https://www.hackaddict.net/2007/07/skip-to-next-or-previous-word-in-iterm.html
date: '2007-07-10T09:45:00.000-04:00'
layout: post
modified_time: '2007-07-10T09:51:43.320-04:00'
redirect_from: /2007/07/skip-to-next-or-previous-word-in-iterm.html
tags:
- tutorial
- nix
- keyboard
- mac
thumbnail: '{{ site.url }}/assets/images/thumbnails/2007-07-10-image-0000.png'
title: Skip to Next or Previous Word in iTerm Using Alt / Option + Left or Right Arrow
  Keys
---

I recently decided to give <a href="http://iterm.sourceforge.net/" title="iTerm">iTerm</a> another try after one of my friends recommended it to me.  I had tried it several times before, and never quite gotten used to it.  I always seemed to prefer <a href="http://docs.blacktree.com/visor/visor?DokuWiki=77deb4ed41f242810e2c1a43e3f4c6f7" title="visor:visor [docs]">Visor</a> + Terminal for some reason or other, but since I've setup a <a href="/2007/07/setup-global-keyboard-shortcuts-to-open.html" title="hackaddict.net: Setup Global Keyboard Shortcuts to Open Any App with Quicksilver">global keyboard shortcut to focus / open iTerm</a>, I've been enjoying having a tabbed terminal.



One of the things that was fairly easy to setup in Terminal that took me several days to figure out in iTerm was how to navigate Forward and Backword across whole words using the keyboard.  ( <a href="http://macromates.com/blog/2006/word-movement-in-terminal/" title="TextMate Blog » Word Movement in Terminal">This article on the Textmate blog</a> explains how to set this up in the regular terminal. )



I tried doing all sorts of things to setup something similar in iTerm, like using a <b>.inputrc</b> file, until I finally figured out how to do it.



Open iterm.

Go to <b>Bookmarks &gt; Manage Profiles</b>

Choose <b>Keyboard Profiles</b> on the left and edit the <b>Global</b> Profile



<img alt="" border="0" id="BLOGGER_PHOTO_ID_5085564513604521714" src="{{ site.url }}/assets/images/posts/2007-07-10-image-0000.png" style="display:block; margin:0px auto 10px; text-align:center; "/>



<h5>Map Alt + Left Arrow to Backword / Previous Word</h5>

Next to Mapping, click the <b>+</b> sign.

For <b>Key</b>, choose cursor <b>left</b>.

For <b>Modifier</b>, check the <b>Option</b> Box

For <b>Action</b>, choose <b>send escape sequence</b>

Write <b>b</b> in the input field.

I also checked <b>High interception priority</b> for good measure.



<h5>Map Alt + Right Arrow to Forward / Next Word</h5>

Next to Mapping, click the <b>+</b> sign.

For <b>Key</b>, choose cursor <b>right</b>.

For <b>Modifier</b>, check the <b>Option</b> Box

For <b>Action</b>, choose <b>send escape sequence</b>

Write <b>f</b> in the input field.

I also checked <b>High interception priority</b> here for good measure.



<img alt="" border="0" id="BLOGGER_PHOTO_ID_5085564389050470114" src="{{ site.url }}/assets/images/posts/2007-07-10-image-0001.png" style="display:block; margin:0px auto 10px; text-align:center; "/>



Now you have some sweet keyboard navigation action.



<b>Bonus:</b>

Beginning of Line: <b>Ctrl + a</b>

End of Line: <b>Ctrl + e</b>