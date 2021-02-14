---
author: kortina
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-1638413504523017710
blogger_orig_url: https://www.hackaddict.net/2007/01/my-essential-os-x-setup-for-web.html
date: '2007-01-22T19:49:00.000-05:00'
layout: post
modified_time: '2007-01-22T20:31:03.610-05:00'
redirect_from: /2007/01/my-essential-os-x-setup-for-web.html
tags:
- mac
title: My Essential OS X Setup (for web developers)
---

When my iBook died a few days ago, I got a loner laptop from work to use until I have enough money to buy one for myself again.  Getting a loner laptop that you know you are only going to use for a few months is like getting a sublet.  When I moved into my sublet apartment on January 1, I knew I was only going to be staying there until the end of March.  Knowing that I would have to move all my stuff twice, I sold everything I possibly could on Craiglist and donated or threw out anything else I didn't absolutely need.  My roommate did the same, and we were able to move all of our essentials (minus two or three small boxes we stored at a friend's place) in a Hyundai Elentra.



I'm setting up the new laptop with the minimum number of installs I need to use this laptop for programming (ruby, php, mysql), using the internet, and doing my day to day stuff like blogging and watching/listening-to/recording video and audio.  Here are my essentials:



<h4>Essential OS X apps</h4>

<ol>

 <li>iLife - comes bundled with OS X</li>

 <li> <a href="http://macromates.com/">textmate</a> for writing code, posts, or just about anything</li>

 <li><a href="http://quicksilver.blacktree.com/">quicksilver</a> for launching things quickly</li>

 <li><a href="http://getfirefox.com">firefox</a>: do the <a href="http://gettinghighongettingby.blogspot.com/2007/01/essential-firefox-setup.html">essential firefox setup</a>

 </li>

 <li><a href="http://www.jungledisk.com/download.shtml">JungleDisk</a> for backups on <a href="http://www.amazon.com/gp/browse.html?node=16427261">Amazon S3</a></li>

 <li><a href="http://growl.info/downloads.php">growl</a></li>

 <li><a href="http://www.versiontracker.com/dyn/moreinfo/macosx/182">stuffit</a> -- get it from version tracker so you don't have to enter your email</li>

 <li><a href="http://metissian.com/projects/macosx/subversion/">svn</a> for file synchronization</li>

 <li><a href="http://www.apple.com/downloads/dashboard/business/backpack.html">the backpack widget</a> for todos and reminders on backpack</li>

 <li>What about ftp?  I use svn, <a href="http://www.eos.ncsu.edu/remoteaccess/man/scp.html">scp</a>, and torrents for all my file transfers now.  If I used ftp, it would be either <a href="http://www.panic.com/transmit/">transmit</a> or <a href="http://cyberduck.ch/">cyberduck</a>.</li>

 <li><a href="http://sarwat.net/bittorrent/">tomato torrent</a>, a simple bit torrent app</li>

 <li><a href="http://www.flip4mac.com/wmv_download.htm">flip4mac wmv player</a></li>

</ol>

<h4>Some personal tweaks I like to setup:</h4>

<ol>

 <li>Enable full keyboard access: <b>System Preferences &gt; Keyboard and Mouse &gt; Keyboard Shortcuts &gt; Full Keyboard Access &gt; All Controls</b></li>

 <li>open terminal: set your color preference and under emulation, set _Option click to position cursor_</li>

 <li>Right click on the desktop, <b>Show view options</b>.  Icon size: 28x28, Text size: 10pt, Label position: right, Show item info, Show icon preview, Keep arranged by: name.  This will keep your desktop nice and clean.</li>

 <li>Set mouse sensitivity in <b>System Preferences &gt; Keyboard and Mouse &gt; Trackpad (or mouse)</b></li>

 <li>edit bash profile ( ~/.bash_profile ):

<pre>

alias ls='ls -G'

alias e='mate'

export PATH="/usr/local/bin:/usr/local/sbin:/usr/local/mysql/bin:$PATH"

</pre>

 </li>

 <li>from home directory in terminal:

<pre>

$ touch todo.txt

$ ln -s ~/todo.txt ~/Desktop/todo

</pre>

 This is going to be used for plaintext todos stored on the local machine as described <a href="http://www.lifehacker.com/software/text/geek-to-live-list-your-life-in-txt-166299.php">in this lifehacker article</a>.  I use plaintext todos when I'm offline or don't feel like posting to my BackPack.  The second line I do is if you also want a desktop shortcut. (you will have to relaunch Finder to see the shortcut appear.)  

 </li>

</ol>

<h4>Essentials for Web Development</h4>

<ol>

 <li><a href="http://developer.apple.com/tools/xcode/">Xcode</a></li>

 <li><a href="http://hivelogic.com/articles/2005/12/01/ruby_rails_lighttpd_mysql_tiger">Hivelogic's Ruby, Rails, and Mysql install tutorial</a></li>

</ol>

<h4>Very Useful (but not essential) Apps</h4>

<ol>

 <li><a href="http://www.markspace.com/downloads.html">the missing sync</a>, to sync my blackjack with my mac</li>

 <li>Microsoft Office or Open Office.  I prefer MS Office.</li>

 <li>Adobe Photoshop or <a href="http://www.gimp.org/macintosh/">the GIMP</a> and Adobe Illustrator</li>

 <li><a href="http://www.versiontracker.com/dyn/moreinfo/macosx/31606">wget</a></li>

</ol>



What are your essential apps / tweaks?