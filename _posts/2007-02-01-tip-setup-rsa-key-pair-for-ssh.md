---
author: kortina
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-3650963273908452
blogger_orig_url: https://www.hackaddict.net/2007/02/tip-setup-rsa-key-pair-for-ssh.html
date: '2007-02-01T23:03:00.000-05:00'
layout: post
modified_time: '2007-02-01T23:07:40.782-05:00'
redirect_from: /2007/02/tip-setup-rsa-key-pair-for-ssh.html
tags:
- mac
- tip
title: 'Tip: Setup an RSA Key Pair for SSH Authentication and Save Your Passphrase
  Using SSH-Agent in Mac OS X'
---

If you use command line tools like ssh, scp, and svn a lot (I do), you may get sick of typing in your password every time you use one of these tools.  If your svn repository authenticates using ssh, you can save yourself some time by generating an RSA key to authenticate with all of these tools (scp uses ssh authentication, as does ssh--duh).  <a href="http://berserk.org/2005/10/08/textmate-and-a-remote-editing-workaround/">This tutorial</a> explains how to generate an RSA key pair, plus it has a cool tip on how to use <a href="http://macromates.com/">Textmate</a> to save files directly to your web server.<br/><br/>Once you have a working RSA key pair, the next step is to write a little script to get ssh-agent running.  I found one called check_ssh_agent.sh that I got from <a href="http://mactechnotes.blogspot.com/2005/09/ssh-agent-on-mac-os-x.html">here</a>.  (This site also has some details about how to do a setup similar to the one I'm describing here, but he does things a little differently.)  I put the script in my home directory here: <b>~/Documents/scripts/check_ssh_agent.sh</b>.<br/><br/>Make sure the file is executable:<br/><pre>chmod 700 ~/Documents/scripts/check_ssh_agent.sh</pre><br/><br/>Finally, you need to add an environment variable called <b>SSH_AUTH_SOCK</b> which points to the socket that ssh-agent uses.  You also need to add the scripts folder to your PATH and add a line to launch the check_ssh_agent.sh script when you login.  To do this, edit your bash profile:<br/><pre>mate ~/.bash_profile</pre><br/>Add the following:<br/><pre>export PATH="/usr/local/bin:~/Documents/scripts/:$PATH"<br/>export SSH_AUTH_SOCK='/Users/kortina/tmp/ssh/ssh-agent.socket'<br/>~/Documents/scripts/check_ssh_agent.sh</pre><br/><br/>(note: if your path has other stuff, leave it and just insert the scripts directory, separating it from other directories using :'s)<br/><br/>Relaunch terminal.  Then, before you do your next ssh authentication, do:<br/><pre>ssh-add ~/.ssh/id_rsa</pre><br/><br/>This will add your private key and you won't have to type your passhrase again until you reboot.