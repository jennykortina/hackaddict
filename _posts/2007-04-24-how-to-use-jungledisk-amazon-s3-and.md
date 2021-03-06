---
author: kortina
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-2239848718210182883
blogger_orig_url: https://www.hackaddict.net/2007/04/how-to-use-jungledisk-amazon-s3-and.html
date: '2007-04-24T21:16:00.001-04:00'
layout: post
modified_time: '2007-04-27T10:11:12.003-04:00'
redirect_from: /2007/04/how-to-use-jungledisk-amazon-s3-and.html
tags:
- nix
- mac
- tip
thumbnail: '{{ site.url }}/assets/images/thumbnails/2007-04-24-image-0000.jpg'
title: How to Use JungleDisk, Amazon S3, and rsync to Backup Your OS X Home Directory
---

<p>  In January, my iBook died; a week ago, my friend Iqram's MacBook died after an OS X Security Update; two days ago my friend Dave's iBook hard drive failed.  Iqram and I managed to recover our data; Dave did not.  At the moment, I don't have the greatest faith in Apple products, so I decided to backup all my data. </p> <p>  I used to use an external USB hard drive for backups, but my 160 GB external has been acting up of late and sometimes needs to be restarted 2 or 3 times before my computer recognizes it, so about 2 months ago I started playing with Amazon S3 and JungleDisk. </p> <p>Amazon S3 (Simple Storage Service) is basically an infinite hard drive you can by on a pay per usage basis, and JungleDisk is a utility that allows you to mount S3 as a hard drive on any OS.  JungleDisk has a backup tool built in, but right now the tool does not provide mirroring--ie, if you backup a folder on your computer and then delete some stuff locally, that stuff will not be deleted remotely.  So if you start moving stuff around, you'll end up with duplicate copies of your data.  Redundant data annoys me, so I decided to finally learn how to use the <code>rsync</code> command line utility to mirror folders.  Here's how I setup a backup of my home directory using Amazon S3, JungleDisk, and rsync.</p> <h4>Get Amazon S3</h4> <p>Signup for <a href="http://www.amazon.com/gp/browse.html?node=16427261">Amazon Simple Storage Service</a>.  Here's how the pricing works, according to Amazon's website:</p>  

<ul>  
<li>Pay only for what you use. There is no minimum fee, and no start-up cost. </li>
  
<li>$0.15 per GB-Month of storage used. </li>
  
<li>$0.20 per GB of data transferred. </li>
 </ul> <h4>Download JungleDisk</h4> <p><a href="http://jungledisk.com/download.shtml">JungleDisk</a> is free and available for Linux, Windows, and OS X.</p> <h4>Setup JungleDisk</h4> <p>JungleDisk is pretty easy to setup on OS X.  You just download the <a href="http://downloads.jungledisk.com/jungledisk/JungleDiskBeta.dmg">JungleDisk dmg</a>, open it, and drap the <code>.app</code> file to your <b>Applications</b> Folder.  Then you open it and enter your Amazon access keys, which you can find by going to <a href="https://aws-portal.amazon.com/gp/aws/developer/account/index.html?action=access-key">this page</a> on Amazon.  You will also need to choose a bucket name that you want JungleDisk to use on your S3 account.  I used <b>kortina</b>.</p> <img alt="" border="0" id="BLOGGER_PHOTO_ID_5057166169665782930" src="{{ site.url }}/assets/images/posts/2007-04-24-image-0000.jpg" style="display:block; margin:0px auto 10px; text-align:center; "/> <p>When you configure JungleDisk, you can choose to have it auto-mount as a Volume on your computer whenever you start the JungleDisk app. (this is the default setting.)  If you need to mount JungleDisk manually, open <b>Finder</b>, hit <b>⌘ k</b>, and enter <b>http://localhost:2667/</b> as the host name.  You can find more instructions on configuring JungleDisk on <a href="http://jungledisk.com/macinstall.shtml">this page</a> on their official site.</p> <img alt="" border="0" id="BLOGGER_PHOTO_ID_5057166474608460962" src="{{ site.url }}/assets/images/posts/2007-04-24-image-0001.png" style="display:block; margin:0px auto 10px; text-align:center; "/> <img alt="" border="0" id="BLOGGER_PHOTO_ID_5057167870472832178" src="{{ site.url }}/assets/images/posts/2007-04-24-image-0002.png" style="display:block; margin:0px auto 10px; text-align:center; "/> <h4>Run rsync to Mirror Your Home Directory to Jungle Disk</h4> <p> <code>   rsync \

 -avvz   --size-only   --delete  \

 --exclude .svn --exclude .Trash --exclude Library/Caches --exclude "*.log"  \

/Users/kortina  /Volumes/JungleDisk  </code> </p> <h4>How this rsync Script Works</h4> <p>  The <code>rsync</code> command takes a bunch of options and then a source directory and  destination directory  as arguments.  In this case the source is <code>/Users/kortina</code>, my home directory, and the destination is the mounted JungleDisk drive at <code style="color:#666;">/Volumes/JungleDisk</code>.  Since there is no trailing <code>/</code> after <code style="color:#666;">/Volumes/JungleDisk</code>, a directory named <code>kortina</code> will be created on the JungleDisk drive.  To copy the contents of your home directory directly to JungleDisk without enclosing them in a folder with your username, simply add a trailing slash: <code style="color:#666;">/Volumes/JungleDisk/</code>. </p> <p>  Here's what the options I've used do: </p>  

<ul>  
<li><code style="color:red;">-a</code>: This runs <code>rsync</code> in archive mode, which is equivalent to running it with <code>-rlptgoD</code>.  The main thing important here is <code>-r</code>, which will recurse into directories, and in fact many of these other options bundled in <code>-a</code> are irrelevant because of the way S3 treats file meta data. </li>
  
<li><code style="color:red;">-v or -vv</code>: Run in verbose or very verbose mode.  Verbose mode will print the name of each file copied or deleted, and very verbose mode will additionally print the names of files that are skipped.  I like to run in <code style="color:red;">-vv</code> because I can see progress more easily. </li>
  
<li><code style="color:red;">-z</code>: this option will compress file data and make things a bit faster. </li>
  
<li><code style="color:green;">--size-only</code>: usually, rsync will compare the size and last modified date of each file to determine whether it is out of date and needs to be copied.  Because of the way S3 handles file metadata, however, the last-modified-date of each file you upload to S3 will always be the date it was uploaded.  This will screw up rsync, so you need to use the --size-only option to make this backup script work. </li>
  
<li><code style="color:orange;">--delete</code>: (delete files that don't exist on sender) this is another important part of my backup script.  The reason I didn't want to use JungleDisk's built in backup utility was because it didn't support mirroring.  <code style="color:orange;">--delete</code> is the option that makes rsync to a mirror instead of a simple copy. </li>
  
<li><code style="color:purple;">--exclude</code>: (exclude files matching PATTERN) this option allows you to ignore file patterns like <b>*.log</b> or directory names like <b>Movies</b>. </li>
 </ul> <p>Once you setup S3 and Jungledisk, if you want to keep the same options I use, just copy and paste the code below, subsitute <b>your_username</b> for <b>kortina</b>, open a terminal and run the command.</p> <p> <code>   rsync  -avvz   --size-only   --delete   --exclude .svn --exclude .Trash --exclude Library/Caches --exclude "*.log"  /Users/<b>kortina</b>  /Volumes/JungleDisk  </code> </p>