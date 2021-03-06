---
author: kortina
blogger_id: tag:blogger.com,1999:blog-5518298822864690168.post-1749652901388954205
blogger_orig_url: https://www.hackaddict.net/2007/12/201-inspirational-videos-from-ted.html
date: '2007-12-20T16:32:00.001-05:00'
layout: post
modified_time: '2007-12-20T16:46:10.844-05:00'
redirect_from: /2007/12/201-inspirational-videos-from-ted.html
tags:
- nix
title: 201 Inspirational Videos (from TED)
---

I was doing my usual thing at lunch today (watching a <a href="http://ted.com">TED</a> talk as I ate) and noticed the url said `http://www.ted.com/talks/view/id/201`.  I have been watching a lot of these videos lately, and I decided I might as well watch them in order.  I wrote a quick ruby / <a href="http://rubyforge.org/projects/mechanize/">Mechanize</a> script (<a href="#code_source">source below</a>) to loop through videos 1-201 and fetch the titles for each.  Some of the titles did not have the speaker/topic, but most did. Here they are:



<ol> 
<li><a href="http://www.ted.com/talks/view/id/1">TED | Talks | Al Gore: 15 ways to avert a climate crisis (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/2">TED | Talks | Amy Smith: Simple designs that could save millions of childrens' lives (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/3">TED | Talks | Ashraf Ghani: How to fix broken states (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/4">TED | Talks | Burt Rutan: Entrepreneurs are the future of space flight (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/5">TED | Talks | Chris Bangle: Great cars are Art (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/6">TED | Talks | Craig Venter: A voyage of DNA, genes and the sea (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/7">TED | Talks | David Pogue: When it comes to tech, simplicity sells (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/8">TED | Talks | David Rockwell: Building the Ground Zero viewing platform (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/9">TED | Talks | Dean Kamen: Rolling along, helping students and the third world (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/10">TED | Talks | Dr. Dean Ornish: The world now eats (and dies) like Americans (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/11">TED | Talks | Jane Goodall: What separates us from the apes? (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/12">TED | Talks | Eva Vertes: My dream about the future of medicine (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/13">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/14">TED | Talks | Golan Levin: The truly soft side of software (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/15">TED | Talks | Gregory Colbert: Gorgeous video from "Ashes and Snow" (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/16">TED | Talks | Helen Fisher: The science of love, and the future of women (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/17">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/18">TED | Talks | Janine Benyus: 12 sustainable design ideas from nature (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/19">TED | Talks | Kevin Kelly: How does technology evolve? Like we did (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/20">TED | Talks | Malcolm Gladwell: What we can learn from spaghetti  sauce (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/21">TED | Talks | Mena Trott: Building a friendlier world through blogs (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/22">TED | Talks | Michael Shermer: Why people believe strange things (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/23">TED | Talks | Peter Gabriel: Fighting injustice with a videocamera (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/24">TED | Talks | Pilobolus: A performance merging dance and biology (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/25">TED | Talks | Richard Baraniuk: Goodbye, textbooks; hello, open-source learning (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/26">TED | Talks | Rives: "If I controlled the Internet" (a poem) (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/27">TED | Talks | Ross Lovegrove: The power and beauty of organic design (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/28">TED | Talks | Seth Godin: Sliced bread and other marketing delights (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/29">TED | Talks | Steven Levitt: Why do crack dealers still live with their moms? (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/30">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/31">TED | Talks | Thom Mayne: Architecture is a new way to connect to the world (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/32">TED | Talks | Vik Muniz: Art with wire, thread, sugar, chocolate (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/33">TED | Talks | Thomas Barnett: The Pentagon's new map for war and peace (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/34">TED | Talks | Phil Borges: Documenting our endangered cultures (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/35">TED | Talks | James Watson: The double helix and today's DNA mysteries (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/36">TED | Talks | Robert Neuwirth: The "shadow cities" of the future (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/37">TED | Talks | Jimmy Wales: How a ragtag band created Wikipedia (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/38">TED | Talks | Ray Kurzweil: How technology's accelerating power will transform us (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/39">TED | Talks | Aubrey de Grey: Why we age and how we can avoid it (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/40">TED | Talks | Frans Lanting: A lyrical view of life on Earth (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/41">TED | Talks | Nicholas Negroponte: The vision behind One Laptop Per Child (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/42">TED | Talks | Sir Martin Rees: Earth in its final century? (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/43">TED | Talks | Paul Bennett: Design is in the details (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/44">TED | Talks | Nick Bostrom: Humanity's biggest problems aren't what you think they are (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/45">TED | Talks | Sirena Huang: Dazzling set by 11-year-old violinist (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/46">TED | Talks | Jennifer Lin: Magical improv from 14-year-old pianist (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/47">TED | Talks | David Deutsch: What is our place in the cosmos? (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/48">TED | Talks | Saul Griffith: Hardware solutions to everyday problems (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/49">TED | Talks | Joshua Prince-Ramus: Designing the Seattle Central Library (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/50">TED | Talks | Stefan Sagmeister: Yes, design can make you happy (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/51">TED | Talks | Amory Lovins: We must win the oil endgame (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/52">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/53">TED | Talks | Majora Carter: Greening the ghetto (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/54">TED | Talks | Cameron Sinclair: TED Prize wish: Open-source architecture to house the world (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/55">TED | Talks | Jehane Noujaim: TED Prize wish: Unite the world on Pangea Day, a global day of film (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/56">TED | Talks | Edward Burtynsky: TED Prize wish: Share the story of Earth's manufactured landscapes (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/57">TED | Talks | Robert Fischell: TED Prize wish: Finding new cures for migraine, depression, malpractice (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/58">TED | Talks | Larry Brilliant: TED Prize wish: Help stop the next pandemic (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/59">TED | Talks | Bono: TED Prize wish: Join my call to action on Africa (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/60">TED | Talks | Anna Deavere Smith: Four American characters (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/61">TED | Talks | Steven Johnson: A guided tour of the Ghost Map (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/62">TED | Talks | Bjorn Lomborg: Our priorities for saving the world (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/63">TED | Talks | Charles Leadbeater: The rise of the amateur professional (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/64">TED | Talks | Eve Ensler: Finding happiness in body and soul (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/65">TED | Talks | Jeff Han: Unveiling the genius of multi-touch interface design (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/66">TED | Talks | Sir Ken Robinson: Do schools kill creativity? (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/67">TED | Talks | Peter Donnelly: How juries are fooled by statistics (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/68">TED | Talks | Robert Wright: How cooperation (eventually) trumps conflict (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/69">TED | Talks | Wade Davis: Cultures at the far edge of the world (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/70">TED | Talks | Richard St. John: Secrets of success in 8 words, 3 minutes (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/71">TED | Talks | Rick Warren: Living a life of purpose (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/72">TED | Talks | Chris Anderson: Technology's Long Tail (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/73">TED | Talks | Carl Honore: Slowing down in a world built for speed (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/74">TED | Talks | Alex Steffen: Inspired ideas for a sustainable future (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/75">TED | Talks | Sasa Vucinic: A new way to invest in press freedom (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/76">TED | Talks | Susan Savage-Rumbaugh: Apes that write, start fires and play Pac-Man (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/77">TED | Talks | Sheila Patek: Measuring the fastest animal on earth (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/78">TED | Talks | Al Seckel: Your brain is badly wired -- enjoy it!  (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/79">TED | Talks | Iqbal Quadir: The power of the mobile phone to end poverty (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/80">TED | Talks | Juan Enriquez: Decoding the future with genomics (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/81">TED | Talks | Nora York: "What I Want" (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/82">TED | Talks | Dean Kamen: New prosthetic arm for veterans (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/83">TED | Talks | E.O. Wilson: TED Prize wish: Help build the Encyclopedia of Life (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/84">TED | Talks | James Nachtwey: TED Prize wish: Share a vital story with the world (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/85">TED | Talks | Bill Clinton: TED Prize wish: Let's build a health care system in Rwanda (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/86">TED | Talks | Julia Sweeney: "Letting Go of God" (an excerpt) (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/87">TED | Talks | Ze Frank: What's so funny about the Web? (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/88">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/89">TED | Talks | Ben Saunders: Three things to know before you ski to the North Pole (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/90">TED | Talks | Neil Gershenfeld: The beckoning promise of personal fabrication (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/91">TED | Talks | Jacqueline Novogratz: Investing in Africa's own solutions (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/92">TED | Talks | Hans Rosling: Debunking third-world myths with the best stats you've ever seen (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/93">TED | Talks | Barry Schwartz: The paradox of choice (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/94">TED | Talks | Dan Dennett: A secular, scientific rebuttal to Rick Warren (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/95">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/96">TED | Talks | Tony Robbins: Why we do what we do, and how we can do it better (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/97">TED | Talks | Dan Gilbert: Why are we happy? Why aren't we happy? (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/98">TED | Talks | Richard Dawkins: The universe is queerer than we can suppose (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/99">TED | Talks | Jill Sobule: A happy song about global warming (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/100">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/101">TED | Talks | Caroline Lavelle: A cello performance that casts a spell (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/102">TED | Talks | Dan Dennett: Can we know our own minds? (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/103">TED | Talks | Evelyn Glennie: How to listen to music with your whole body (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/104">TED | Talks | William McDonough: The wisdom of designing Cradle to Cradle (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/105">TED | Talks | Jeff Bezos: After the gold rush, there's innovation ahead (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/106">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/107">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/108">TED | Talks | Rives: A mockingbird remix of TED2006 (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/109">TED | Talks | Eddi Reader, Thomas Dolby: "What You Do With What You've Got" (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/110">TED | Talks | Eddi Reader: "Kiteflyer's Hill" (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/111">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/112">TED | Talks | Rev. Tom Honey: How could God have allowed the tsunami? (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/113">TED | Talks | Richard Dawkins: An atheist's call to arms (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/114">TED | Talks | Tom Rielly: A comic send-up of TED2006 (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/115">TED | Talks | Thomas Dolby: With Rachelle Garniez, "La Vie en Rose" (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/116">TED | Talks | Dan Dennett: Ants, terrorism, and the awesome power of memes (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/117">TED | Talks | Natalie MacMaster, Thomas Dolby: Fiddling in reel time (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/118">TED | Talks | Sergey Brin and Larry Page: Inside the Google machine (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/119">TED | Talks | Stew: "Black Men Ski" (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/120">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/121">TED | Talks | James Howard Kunstler: The tragedy of suburbia (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/122">TED | Talks | David Kelley: The future of design is human-centered (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/123">TED | Talks | Stewart Brand: Why squatter cities are a good thing (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/124">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/125">TED | Talks | Jeff Hawkins: Brain science is about to fundamentally change computing (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/126">TED | Talks | Tierney Thys: Swim with giant sunfish in the open ocean (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/127">TED | Talks | Ngozi Okonjo-Iweala: How to help Africa? Do business there (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/128">TED | Talks | John Doerr: Seeking salvation and profit in greentech (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/129">TED | Talks | Blaise Aguera y Arcas: Jaw-dropping Photosynth demo (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/130">TED | Talks | Bob Thurman: Becoming Buddha -- on the Web (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/131">TED | Talks | Anand Agarawala: BumpTop desktop is a beautiful mess (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/132">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/133">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/134">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/135">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/136">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/137">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/138">TED | Talks | Ethel: "Blue Room" (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/139">TED | Talks | Stephen Lawler: Look! Up in the sky! It's Virtual Earth! (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/140">TED | Talks | Hans Rosling: New insights on poverty and life around the world (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/141">TED | Talks | Bill Stone: Journey to the center of the Earth ... and beyond! (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/142">TED | Talks | Alan Russell: Why can't we grow new body parts? (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/143">TED | Talks | Emily Oster: What do we really know about the spread of AIDS? (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/144">TED | Talks | Jonathan Harris: The Web's secret stories (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/145">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/146">TED | Talks | Will Wright: Toys that make worlds (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/147">TED | Talks | David Bolinsky: Fantastic voyage inside a cell (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/148">TED | Talks | Rives: Is 4 a.m. the new midnight? (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/149">TED | Talks | Allison Hunt: How I got my new hip (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/150">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/151">TED | Talks | George Ayittey: Cheetahs vs. Hippos for Africa's future (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/152">TED | Talks | Ngozi Okonjo-Iweala: Let's have a deeper discussion on aid (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/153">TED | Talks | William Kamkwamba: How I built my family a windmill (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/154">TED | Talks | Euvin Naidoo: Africa as an investment (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/155">TED | Talks | Chris Abani: Learning the stories of Africa (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/156">TED | Talks | Patrick Awuah: Educating a new generation of African leaders (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/157">TED | Talks | Jacqueline Novogratz: Tackling poverty with "patient capital" (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/158">TED | Talks | Vusi Mahlasela: "Thula Mama" (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/159">TED | Talks | Andrew Mwenda: Let's take a new look at African aid (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/160">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/161">TED | Talks | Erin McKean: Redefining the dictionary (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/162">TED | Talks | Theo Jansen: The art of creating creatures (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/163">TED | Talks | Steven Pinker: A brief history of violence (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/164">TED | Talks | Steven Pinker: The stuff of thought (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/165">TED | Talks | Hod Lipson: Robots that are "self-aware" (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/166">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/167">TED | Talks | Stephen Petranek: 10 ways the world could end (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/168">TED | Talks | Zeresenay Alemseged: Finding the origins of humanity (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/169">TED | Talks | Vusi Mahlasela: "Woza" (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/170">TED | Talks | Jeff Skoll: Making movies that make change (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/171">TED | Talks | Deborah Scranton: Scenes from "The War Tapes" (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/172">TED | Talks | John Maeda: Simplicity patterns (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/173">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/174">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/175">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/176">TED | Talks | Paul MacCready: Flying on solar wings (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/177">TED | Talks | Larry Brilliant: The case for informed optimism (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/178">TED | Talks | Carolyn Porco: Fly me to the moons of Saturn (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/179">TED | Talks | Kenichi Ebina: Hip-hop dance and a little magic (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/180">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/181">TED | Talks | Richard Branson: Life at 30,000 feet (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/182">TED | Talks | Maira Kalman: The illustrated woman (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/183">TED | Talks | Paul Rothemund: Casting spells with DNA (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/184">TED | Talks | Vilayanur Ramachandran: A journey to the center of your mind (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/185">TED | Talks | Eleni Gabre-Madhin: Building a commodities market in Ethiopia (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/186">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/187">TED | Talks | Larry Lessig: How creativity is being strangled by the law (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/188">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/189">TED | Talks | Sherwin Nuland: My history of electroshock therapy (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/190">TED | Talks | Jan Chipchase: Our cell phones, ourselves (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/191">TED | Talks | Matthieu Ricard: Habits of happiness (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/192">TED | Talks | David Keith: A surprising idea for "solving" climate change (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/193">TED | Talks | Juan Enriquez: Why can't we grow new energy? (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/194">TED | Talks | Murray Gell-Mann: Beauty and truth in physics (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/195">TED | Talks | Robert Full: Secrets of movement, from geckos and roaches (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/196">TED | Talks</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/197">TED | Talks | Philippe Starck: Why design? (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/198">TED | Talks | Ron Eglash: African fractals, in buildings and braids (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/199">TED | Talks | Arthur Benjamin: Lightning calculation and other "Mathemagic" (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/200">TED | Talks | Daniel Goleman: Why aren’t we all Good Samaritans?  (video)</a> </li>
 
<li><a href="http://www.ted.com/talks/view/id/201">TED | Talks | Lakshmi Pratury: The lost art of letter-writing (video)</a> </li>
</ol>





<a name="code_source">Quick and dirty ruby code:</a>

<pre><code>

#!/usr/bin/env ruby



require 'rubygems'

require 'mechanize'



html = "&lt;ol&gt;"



agent = WWW::Mechanize.new



201.times do |i|

  url = "http://www.ted.com/talks/view/id/#{i+1}"

  begin

    page = agent.get url

    line = "&lt;li&gt;&lt;a href='#{url}'&gt;#{page.title}&lt;/a&gt;&lt;/li&gt;"

  rescue Exception =&gt; e

    line = "&lt;li&gt;Couldn't fetch #{i+1}&lt;/li&gt;"

  end

  html += line

  puts line # show me where you are

end



html += "&lt;/ol&gt;"



o = File.open('ted.html', "w")

o.write(html)

o.close

</code></pre>



( I was looking in the rdoc for a way to do a HEAD request instead of a GET to save some time, but couldn't find out how.  Didn't feel like messing with curl, so I just stuck with the GET. )