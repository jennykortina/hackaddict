---
author: jenny
layout: post
title: Use Old Airport Express with Big Sur
---

I am moving soon and want to hook up all my rooms to speakers through Airport Express stations so I can easily stream music anywhere in my house from apple devices.  Coupled with [Airfoil](https://rogueamoeba.com/airfoil/mac/), it's a pretty elegant setup.

I prefer the v1 version of the Airport Express because of it's small form factor.  You can also pick them up very cheap on eBay, I got 3 for $30 shipped.  

<img src="{{ site.url }}/assets/images/posts/2021-02-21-image-0000.jpeg" />

After receiving the Airport Expresses I quickly figured out why I got them so cheap.  When trying to connect to them via wifi in Big Sur I was getting the following error: `This version of AirPort Utility doesn't support this base station.`  

I google around a bit, and a lot of people were saying to download Airport Utility v 5.6.1 and use a custom launcher script from [here](https://bristleconeit.com/freeware/launcher-for-airport-utility-v5-6-1/).  After downloading the script I still couldn't get it to launch, but then I realized the Airport Utility app was being blocked by the system security.  To get around this: 

1. Open terminal
2. Paste `xattr -d com.apple.quarantine` into terminal and put a space after it.
3. Drag the Airport Utility 5.6.1 app in to the Terminal window after the  `xattr -d com.apple.quarantine` command and space – this inserts the app location and name in at the end of the line.
4. Hit return.
5. Terminal will run the command, you won’t see any response.
6. Connect your Airport Express to your computer via ethernet (I am not sure if this step is necessary but I did it).
7. Run the script again by double clicking it in finder and Airport Utility v 5.6.1 should launch!

<img src="{{ site.url }}/assets/images/posts/2021-02-21-image-0001.png" />