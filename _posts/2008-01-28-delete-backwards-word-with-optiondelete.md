---
author: kortina
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-7942737694547143915
blogger_orig_url: https://www.hackaddict.net/2008/01/delete-backwards-word-with-optiondelete.html
date: '2008-01-28T11:35:00.000-05:00'
layout: post
modified_time: '2008-01-28T12:32:59.620-05:00'
redirect_from: /2008/01/delete-backwards-word-with-optiondelete.html
tags:
- nix
- keyboard
- mac
thumbnail: '{{ site.url }}/assets/images/thumbnails/2008-01-28-image-0000.png'
title: Delete Backwards Word with Option+Delete in iTerm
---

I just installed Leopard and after setting up <a href="http://hackaddict.blogspot.com/2007/07/skip-to-next-or-previous-word-in-iterm.html" title="hackaddict.net: Skip to Next or Previous Word in iTerm Using Alt / Option + Left or Right Arrow Keys">option left / right arrow in iTerm</a>, I realized that <b>option+delete</b> did not kill the word to the left of my cursor.  I think this somehow worked in my old pre-leopard setup, although I had done nothing to set it up.<br/><br/>After lots of searching, I could find no easy way to map iTerm keys to backwards-delete-word because iTerm doesn't seem to support multiple key sequence bindings.  There are two ways you can backwards delete a word out of the box with iterm:<br/><b>Ctrl+w</b><br/><b>Esc, Ctrl+h</b> or <b>Esc, Delete</b><br/><br/>Finally, using some unix trickery, I got <b>option+delete</b> working.  First, I used the <b>bind</b> command to map <b>Esc, d</b> to backwards delete word. Edit <b>~/.bash_profile</b> in your favorite text editor and add the line:<br/><br/><b>bind '"\M-d": backward-kill-word'</b><br/><br/>(Make sure you have all those quotes, otherwise it doesn't work.)<br/><br/>Now that you have an escape sequence that doesn't require the <b>Ctrl</b> key, you can map <b>option+delete</b> to it in iTerm.<br/><br/>In iTerm, go to <b>Bookmarks &gt; Manage Profiles</b>.  Choose <b>Keyboard Profiles &gt; Global</b> and click the <b>+</b> button to add a key binding.  Choose <b>delete</b> from the dropdown, check the <b>option</b> checkbox, and then in the <b>Action:</b> dropdown choose <b>escape sequence</b>.  In the text field that appears, type <b>d</b>.  I also checked the <b>High interception priority</b> checkbox for good measure.  <br/><br/><img alt="" border="0" id="BLOGGER_PHOTO_ID_5160570988540647650" src="{{ site.url }}/assets/images/2008-01-28-image-0000.png" style="display:block; margin:0px auto 10px; text-align:center; "/><br/><br/>Hit OK and you'll notice <b>option+delete</b> now deletes the word to the left of your cursor.  Sweet!