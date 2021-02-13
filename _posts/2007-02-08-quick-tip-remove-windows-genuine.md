---
layout: post
title: 'Quick Tip: Remove Windows Genuine Advantage'
date: '2007-02-08T16:05:00.000-05:00'
author: jenny
tags:
- windows
- tip
modified_time: '2007-02-08T16:06:09.973-05:00'
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-3457881781934037793
blogger_orig_url: https://www.hackaddict.net/2007/02/quick-tip-remove-windows-genuine.html
---

I have been reformatting a lot of windows computers lately and this made me remember that "illegal" copies of windows how that annoying windows genuine advantage checker.  Here is how to remove that (I got this from another source a long time ago and can't remember where):<br /><br />"If you're not familiar with how NT ACLs work, here's how you can break file permission inheritance. First of all, let's make sure <span id="st" name="st" class="st">Windows</span> will let you access the ACL dialog from the GUI:<ul><li>In explorer, go to Tools > Folder Options. Then, go to View > Advanced Settings and uncheck "Use simple file sharing". Hit OK.</li></ul> <p>Now, let's change the permissions for WgaLogon:</p><ul><li>In the Address bar, type (without quotes) "%WinDir%\system32" and hit enter. <p> </p></li><li>Scroll down to WgaLogon.dll, right click on it, pick Properties. Go to Security.<p> </p></li><li>Hit the Advanced button, uncheck the Inherit box at the bottom, hit the Copy button, then hit OK.</li></ul>  <p>Now we have a local copy of the ACL which we can modify.</p><ul><li>Go through each listed user/group and remove the "Read &amp; Execute" permission for that file, leaving the "Read" permission as-is.<p> </p></li><li>Hit OK to apply the permission changes and close the file properties dialog.  Restart the machine.</li></ul> <p>You can now turn "Use simple file sharing" back on, if you want." </p>