---
author: kortina
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-570849457066673987
blogger_orig_url: https://www.hackaddict.net/2007/10/my-new-google-calendar-setup-quick-add.html
date: '2007-10-17T21:12:00.000-04:00'
layout: post
modified_time: '2007-10-17T21:28:05.107-04:00'
redirect_from: /2007/10/my-new-google-calendar-setup-quick-add.html
tags:
- nix
- mac
- tip
thumbnail: '{{ site.url }}/assets/images/thumbnails/2007-10-17-image-0000.png'
title: My New Google Calendar Setup -- Quick Add from Command Line or SMS
---

As soon as I saw the new <a href="http://code.google.com/p/gcalcli/" title="gcalcli - Google Code">Google Calendar command line interface</a> I decided to give Google Calendar another chance.  Previously, I had ditched it in favor of <a href="http://www.backpackit.com/" title="Get organized and stay organized: Backpack">Backpack</a>--I tried using both for sending myself timely SMS reminders and found that the <a href="http://www.apple.com/downloads/dashboard/business/backpack.html" title="Apple - Downloads - Dashboard Widgets - Backpack">Backpack Dashboard Widget</a> made entry easier.  I like not having to go to a web page to do something like create a reminder for myself if I can help it.



One thing I found annoying about the Backpack widget was the way you set the time for the reminder using a dropdown. (I also like not using my mouse if I can help it.)

<img alt="" border="0" id="BLOGGER_PHOTO_ID_5122482031111842562" src="{{ site.url }}/assets/images/posts/2007-10-17-image-0000.png" style="display:block; margin:0px auto 10px; text-align:center; "/>

I went back to give Google Calendar another shot when the command line interface came out because I knew it had an awesome "Quick Add" feature which allows you to enter reminders like "7:30pm tomorrow get a beer with EJ"--much faster than using dropdown menus.  I got everything setup nicely, and I have to say that capturing reminders is even easier than with the Basecamp widget.



Here's my setup:<h4>Calendar Settings</h4>One of the first things I tweaked before I even started messing with <b>gcalcli</b> was my Google Calendar notification settings.  Go to Google Calender and click the dropdown next to your default calendar in the left pane and choose <b>Notifications</b> to change your reminder settings.  I chose to have events default to sending me an Email and SMS 5 minutes before an event occurs, as well as a popup notification an hour before the event.

<img alt="" border="0" id="BLOGGER_PHOTO_ID_5122481043269364466" src="{{ site.url }}/assets/images/posts/2007-10-17-image-0001.png" style="display:block; margin:0px auto 10px; text-align:center; "/><h4>Setting up gcalcli on OS X</h4>Getting <b>gcalcli</b> working on OS X was a bit of a pain in the ass.  The first thing I recommend doing is making sure the <b>python</b> command in your PATH points to the latest version of Python.  For some reason <b>python</b> on my machine was version 2.4 and this caused me problems, so I installed the latest version of Python and did the following to make sure the <b>python</b> command used this version:<pre>sudo rm /usr/bin/python

sudo ln -s /Library/Frameworks/Python.framework/Versions/2.5/bin/python /usr/bin/python</pre>Once you have the latest version of Python, you need to get the GData Python module, ElementTree Python module, and dateutil Python module.  Links for all these are <a href="http://code.google.com/p/gcalcli/" title="gcalcli - Google Code">here</a>.



After installing all the pre-requisites, get <b>gcalcli</b> from <a href="http://code.google.com/p/gcalcli/downloads/list" title="gcalcli - Google Code">the gcalcli project page on google code</a>.  I put <b>gcalcli</b> in <b>~/Documents/scripts/gcalcli</b>.  You'll also want to edit this file, entering your login information (email, password).



A few other optional things I did to make using gcalcli easier were:

<h4>Add gcalcli to $PATH</h4>This allows you to call gcalcli no matter what directory you're currently working in in the terminal.  Add this line to your <b>~/.bash_profile</b>: <pre>export PATH="~/Documents/scripts/:$PATH"</pre><h4>Create an alias for gcalcli quick add</h4>Add this line to your <b>~/.bash_profile</b> if you want to be able to type <b>q '7:30 barber'</b> instead of <b>gcalcli quick '7:30 barber'</b>: <pre>alias q="~/Documents/scripts/gcalcli quick"</pre>



With all this stuff setup, creating a reminder for myself is super easy: I just hit <b>⌘ Shift i</b> to open iTerm (see <a href="/search?q=trigger" title="hackaddict.net: Search results for trigger">Setup Global Keyboard Shortcuts to Open Any App with Quicksilver</a>), then type <b>q '9pm write blog post about gcal'</b> and I have captured the thought and can get it out of my mind and focus on whatever task is at hand.<h4>Enable SMS Quick Add to Google Calendar</h4>One final addition I just made to my Gcal setup is making SMS Quick Add events easy.  If you have Google Calendar setup with your mobile phone, you can text <b>9pm write blog post about gcal</b> to <b>48368</b> to quick add an event / reminder.  I added <b>48368</b> to my phonebook under "Google Calendar" to make adding reminders from my phone almost as easy as doing it from my computer.





The problem I've had with most reminder / todo software in the past is that it's too hard to enter tasks or reminders; hence, I'd always give up on using them and revert to pencil and paper.  My new Gcal setup makes capturing ideas super easy, so I think I'm gonna stick with it for a while.