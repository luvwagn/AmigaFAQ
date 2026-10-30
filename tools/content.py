# AmigaFAQ content. ASCII only: use &amp; entities for special characters.
CONTENT = {}

CONTENT["getting-started"] = ("New to the Amiga, or coming back after many years? Start here.", [
("What is the Amiga?", """
The Amiga is a family of personal computers sold by Commodore from 1985 to 1994. Thanks to a set of
custom chips that handled graphics, sound and memory access on their own, it could show more colours,
play sampled stereo sound and multitask far beyond most home computers of its day.

It became especially popular in Europe for games, and around the world for video, animation, music
and the demoscene. A dedicated community still uses, repairs and develops for it today.
"""),
("Which Amiga model should I get?", """
It depends on what you want to do. For classic games, the <b>Amiga 500</b> is the most compatible
choice, since most late-1980s and early-1990s games were written for it.

For the widest range of software and the most upgrade options, the <b>Amiga 1200</b> is the best
all-rounder: it has the enhanced AGA graphics chipset, a built-in hard disk interface and a large
range of modern accelerators. The big-box models (A2000, A3000, A4000) offer expansion slots but are
larger, rarer and usually more expensive. See <a href="hardware-general.html#what-amiga-models-were-made">Hardware: General</a> for a model list.
"""),
("What do I need besides the computer itself?", """
At minimum: a power supply, a mouse, a way to connect a display, and some software. Original power
supplies are now decades old, so many owners use a modern replacement built for the Amiga.

The display is often the trickiest part. Amigas output a 15kHz RGB signal that most modern monitors
cannot show directly. See <a href="hardware-general.html#how-do-i-connect-an-amiga-to-a-modern-monitor-or-tv">connecting to a modern monitor</a>.
"""),
("What should I check on an old Amiga before switching it on?", """
Look for a leaking clock battery. The Amiga 500 trapdoor memory expansion (A501) and the big-box
models have a small battery that can leak and corrode the board. If you find one, remove it before
using the machine.

Many later models (including the A600, A1200, A3000, A4000 and CD32) use small surface-mounted
capacitors that can leak with age. Replacing them ("recapping") is a common and worthwhile repair.
"""),
("How do I get software onto a real Amiga?", """
There are several options. A <b>Gotek</b> floppy emulator replaces the floppy drive and loads disk
images (ADF files) from a USB stick. A <b>CompactFlash or SD card</b> on an IDE adapter can serve as
a fast, silent hard drive on the A600, A1200 and A4000, and can be prepared on a modern PC using an
emulator.

You can also write real floppy disks from images using a USB floppy controller such as Greaseweazle
connected to a PC.
"""),
("What are PAL and NTSC, and do they matter?", """
PAL Amigas (sold in most of Europe and Australia) run their display at 50Hz, and NTSC Amigas (sold
in North America) at 60Hz. Many European games were written for PAL and may run too fast, or have
the bottom of the screen cut off, on an NTSC machine.

Some Amigas can be switched between modes, and emulators let you pick either one.
"""),
])

CONTENT["hardware-general"] = ("Models, chipsets, memory, video and upgrades.", [
("What Amiga models were made?", """
These are the main Commodore models, with their release years. Select a model to see its key
specifications as shipped (many were later upgraded by their owners).

{{MODELS}}
"""),
("What are OCS, ECS and AGA?", """
These are the three generations of the Amiga custom chipset. <b>OCS</b> (Original Chip Set) shipped
in the A1000, early A500s and A2000s. It can display up to 32 colours from a palette of 4,096, or all
4,096 at once in the special HAM mode.

<b>ECS</b> (Enhanced Chip Set) added more memory addressing and new screen modes, mainly useful for
productivity. <b>AGA</b> (Advanced Graphics Architecture), in the A1200, A4000 and CD32, raised the
palette to 16.8 million colours with up to 256 on screen at once (and far more in HAM8 mode).
"""),
("What is the difference between Chip RAM and Fast RAM?", """
<b>Chip RAM</b> is memory the custom chips can reach directly, so it holds graphics and sound data.
The processor has to share it with the chips. <b>Fast RAM</b> can only be used by the processor, so
programs run faster from it because they never wait for the custom chips.

Adding Fast RAM is one of the most noticeable upgrades for an A500 or A1200.
"""),
("Which processors did Amigas use?", """
All Amigas use Motorola 68000-family processors. The A500, A600 and A1000 use a 68000 at about
7MHz. The A1200 and CD32 use a 68EC020 at 14MHz, the A3000 a 68030, and the A4000 either a 68EC030
or a 68040.

Accelerator cards can add a faster 68030, 68040 or 68060. Some modern accelerators use FPGA or
Raspberry Pi technology instead of an original Motorola chip.

In the late 1990s, Phase 5's PowerUP accelerators, the Blizzard PPC for the A1200 and the CyberStorm
PPC for the A3000 and A4000, added a PowerPC processor alongside a 68k one, so software written for
PowerPC could run on classic Amigas. Later, PowerPC became the main processor for newer Amiga-compatible
computers such as the AmigaOne range, which run AmigaOS 4.

For more technical background on the 680x0 family:

<ul>
<li><a href="https://en.wikipedia.org/wiki/Motorola_68000_series">Motorola 68000 series</a> (Wikipedia) -
an overview of the whole family, from the 68000 to the 68060, with the differences between each chip.</li>
<li><a href="https://en.wikipedia.org/wiki/Motorola_68000">Motorola 68000</a> (Wikipedia) - the
original chip's design, registers and instruction set in detail.</li>
<li><a href="https://www.nxp.com/docs/en/reference-manual/M68000PRM.pdf">M68000 Family Programmer's
Reference Manual</a> (NXP, PDF) - the official instruction set reference, from the company that
took over Motorola's chip business.</li>
<li><a href="https://thechipletter.substack.com/p/motorolas-68000-series-its-rise-in">Motorola's 68000
Series: Its Rise in Ten Computers</a> (The Chip Letter) - the family's history through the computers
that used it, including the Amiga.</li>
</ul>
"""),
("How do I connect an Amiga to a modern monitor or TV?", """
Amigas output 15kHz analog RGB through a 23-pin video port. Classic Commodore monitors such as the
1084S display this directly, but most modern monitors and TVs do not.

Common solutions are a <b>scan doubler or flicker fixer</b> (fitted inside the Amiga) or an external
<b>upscaler</b> that converts the RGB signal to VGA or HDMI. The A500 and A2000 also have a
composite output, but it is monochrome; the A1000, A600 and A1200 have colour composite output, though
the picture quality is lower than RGB.
"""),
("What floppy disks does the Amiga use?", """
Standard Amiga drives use 3.5-inch double-density disks, formatted to 880KB, more than a PC fits on
the same disk. High-density drives (in some A3000 and A4000 models) store 1.76MB.

From Workbench 2.1 onward, the CrossDOS tool lets an Amiga read and write PC-formatted disks.
"""),
("Can I still upgrade an Amiga today?", """
Yes, and more options exist now than ever. The community produces memory expansions, accelerators,
IDE and network adapters, floppy emulators, video upgrades and replacement parts such as power
supplies and cases.

Popular modern examples include Raspberry Pi based accelerators like the PiStorm, open-source
accelerator designs, and FPGA-based boards. Check that an upgrade suits your exact model and board
revision before buying.
"""),
])

CONTENT["software"] = ("Kickstart, Workbench, AmigaOS versions and where to find programs.", [
("What is the difference between Kickstart and Workbench?", """
<b>Kickstart</b> is the core of the operating system, stored in ROM chips on the motherboard (except
on the A1000, which loads it from disk). It handles booting, multitasking, graphics and hardware.

<b>Workbench</b> is the graphical desktop and set of tools loaded from floppy or hard disk. The two
are versioned together, so Workbench 3.1 expects Kickstart 3.1. Many games boot straight from
Kickstart and never load Workbench at all.
"""),
("Which AmigaOS versions exist?", """
Commodore released versions 1.0 to 1.3 (1985-1988), 2.0 (1990), 3.0 (1992) and 3.1 (1993). After
Commodore, other companies released 3.5 and 3.9, and later Hyperion Entertainment released 3.1.4 and
3.2, which still run on classic 68k Amigas.

AmigaOS 4 is a separate line for PowerPC hardware. AROS and MorphOS are related operating systems
inspired by AmigaOS.
"""),
("Which Kickstart version is best for games?", """
Kickstart 1.3 is the most compatible with older games, since most titles from the 1980s and early
1990s were written for it. Some of those games fail on Kickstart 2.0 and later.

Using WHDLoad (see below) on a hard disk avoids most of these problems, and some owners fit a
Kickstart switcher to choose between two ROMs.
"""),
("What is WHDLoad?", """
WHDLoad is a system for installing floppy-based games and demos onto a hard disk. Each game gets a
small installer and patch so it runs from the hard disk, quits back to Workbench, and works on
faster Amigas that would otherwise break it. It is the standard way to play a large game collection
on an A1200 or in an emulator.
"""),
("What are ADF, HDF and IPF files?", """
An <b>ADF</b> (Amiga Disk File) is an image of an Amiga floppy disk. An <b>HDF</b> is an image of a
hard disk or partition. An <b>IPF</b> is a preservation-quality floppy image that also captures
original copy protection, so the game behaves exactly like the original disk. Emulators, floppy
emulators and disk-writing tools all work with these formats.
"""),
("Where can I find Amiga software?", """
<b>Aminet</b> (aminet.net) has been the main archive of freely distributable Amiga software since
the early 1990s, with tens of thousands of programs, tools, demos and modules. Many developers have
also released their old commercial games for free, and new Amiga games and tools are still being
made and sold by the community today.
"""),
("Are Kickstart ROMs and Workbench disks free to download?", """
No. Kickstart and Workbench are still copyrighted. You can buy licensed copies, for example through
the Amiga Forever package or from resellers of the newer AmigaOS 3.x releases. Owning a real Amiga
also lets you make your own copy of its ROM for use in an emulator.

AROS provides a free, open-source replacement ROM that runs many, but not all, Amiga programs.
"""),
("Why is it called a Guru Meditation?", """
"Guru Meditation" is the Amiga's name for a serious system error, shown as a flashing red box with an
error code. The name comes from an in-house joke at Amiga: staff played a game on a board you stood
on, the "Joyboard", in which you had to sit perfectly still like a meditating guru. An error code
starting with 8 means the system cannot recover and must restart.
"""),
("How do I reset an Amiga or reach the boot menu?", """
Hold down <b>Ctrl</b> together with both <b>Amiga</b> keys to reset the computer. On Kickstart 2.0
and later, holding down <b>both mouse buttons</b> while the machine starts opens the Early Startup
menu, where you can choose a boot drive or turn off features for better compatibility with old
software.
"""),
])

CONTENT["emulation"] = ("Running Amiga software on modern computers and devices.", [
("Can I run Amiga software on a modern computer?", """
Yes. Amiga emulators recreate the hardware in software, accurately enough to run nearly all games,
demos and applications. You will need an emulator, a Kickstart ROM (or the free AROS replacement)
and the software you want to run, usually as ADF or WHDLoad files.
"""),
("Which emulator should I use?", """
<b>WinUAE</b> (Windows) is the most accurate and complete Amiga emulator and the reference that
others are measured against. <b>FS-UAE</b> runs on Windows, macOS and Linux. <b>Amiberry</b> is
designed for Linux devices such as the Raspberry Pi. <b>vAmiga</b> is a macOS emulator focused on
accuracy for the A500, A1000 and A2000. <b>Copperline</b> is a newer, free and open-source emulator for
Windows, macOS and Linux that aims for cycle-accurate emulation of OCS, ECS and AGA machines.

Amiga emulation is also available inside RetroArch through a libretro core.
"""),
("Where do I get a Kickstart ROM for an emulator?", """
The easiest legal route is a licensed package such as Amiga Forever, which includes ROMs and
Workbench. If you own a real Amiga, you can also copy its ROM yourself with a transfer tool. AROS
offers a free replacement ROM, which works well for many programs but is less compatible with
games than the original.
"""),
("What is the A500 Mini?", """
The A500 Mini is a small plug-and-play replica of the Amiga 500 released in 2022 by Retro Games Ltd.
It connects by HDMI, comes with a mouse and gamepad and a selection of built-in games, and can load
additional games from a USB stick. It runs on emulation rather than original Amiga hardware.
"""),
("Can an emulator help me with a real Amiga?", """
Yes. Many owners use an emulator such as WinUAE to set up and install software onto a CompactFlash
or SD card, then move the card into their real Amiga. Emulators are also handy for testing a game or
setup before committing to it on original hardware.
"""),
])

CONTENT["history"] = ("Where the Amiga came from and what happened to it.", [
("Who created the Amiga?", """
The Amiga began at a small California company founded in 1982, originally called Hi-Toro and soon
renamed Amiga Corporation. Its chipset was designed by a team led by Jay Miner, who had earlier
worked on Atari's home computer chips. The prototype was code-named "Lorraine".
"""),
("What does the name Amiga mean?", """
"Amiga" is Spanish for a female friend. The founders wanted a friendly name, and it also conveniently
appeared ahead of Apple and Atari in alphabetical listings.
"""),
("How did Commodore end up owning the Amiga?", """
Amiga Corporation ran short of money while developing its chipset and took funding from Atari, which
came with strings attached. In 1984 Commodore stepped in and bought Amiga Corporation outright,
leading to a legal dispute with Atari. Commodore launched the first model, the Amiga 1000, in 1985.
"""),
("How was the Amiga launched?", """
The Amiga 1000 was unveiled in July 1985 at a gala event at Lincoln Center in New York. In one of the
best-remembered moments, artist Andy Warhol created a digital portrait of singer Debbie Harry live
on stage using the new computer.

Read more: <a href="https://computerhistory.org/blog/warhol-the-computer/">Warhol &amp; The Computer</a>
(Computer History Museum).
"""),
("What was the Amiga used for?", """
At home, especially in Europe, the Amiga was one of the leading games machines of the late 1980s and
early 1990s, with studios such as Psygnosis, DMA Design, Team17 and Sensible Software making
landmark titles. It also became a creative tool: NewTek's Video Toaster made the Amiga 2000 a
low-cost video production system used in television, including for visual effects in early
Babylon 5. The Amiga was also central to the demoscene and to tracker music.
"""),
("What happened to Commodore?", """
Commodore struggled in the early 1990s as PC and console competition grew, and it filed for
bankruptcy in 1994. The Amiga rights then passed through several owners, starting with the German
company Escom, which itself went bankrupt in 1996, and later Gateway.

Development of the operating system continued through other companies, and the community has kept
the platform alive with new hardware, software and updated versions of AmigaOS.
"""),
("Further reading: what are some good books on Amiga history?", """
These books cover the Amiga's story from different angles:

<ul>
<li><b>The Future Was Here: The Commodore Amiga</b> by Jimmy Maher (MIT Press, 2012) - a thoughtful
history of the hardware design, the culture around the machine, and why it mattered. Maher also
covers the Amiga in his long-running blog, <a href="https://www.filfre.net">The Digital Antiquarian</a>.</li>
<li><b>Commodore: The Amiga Years</b> by Brian Bagnall - a detailed, interview-driven account of the
people and company politics behind the Amiga at Commodore.</li>
<li><b>Commodore Amiga: a visual Commpendium</b> (Bitmap Books) - a large, beautifully designed art
book of Amiga games and graphics.</li>
<li><b>The Story of the Commodore Amiga in Pixels</b> by Chris Wilkins - a game-focused history built
around developer interviews and screenshots.</li>
<li><b>Freax: The Brief History of the Computer Demoscene</b> by Tamas Polgar - the story of the
demoscene, in which the Amiga played a central part.</li>
</ul>
"""),
])

ABOUT_INTRO = "AmigaFAQ is a free, community-minded collection of answers about the Commodore Amiga."

ABOUT = [
("What is this site?", """
AmigaFAQ gathers clear, practical answers to the questions people most often ask about the Amiga:
choosing and caring for hardware, understanding the software, running Amiga programs today, and the
history of the platform. It aims to be a friendly first stop for newcomers and returning owners alike.
"""),
("Why does it look like Workbench?", """
The design is a tribute to AmigaOS 3.1 Workbench, with its grey screen, blue title bars and raised
3D gadgets. Underneath, the pages are kept deliberately simple, using plain HTML and a table layout,
so they can be read on real Amiga web browsers such as AWeb and IBrowse as well as on modern
computers and phones.

The site is available over plain HTTP as well as HTTPS, so older machines that cannot handle modern
encryption can still reach it.
"""),
("Can I help or suggest a correction?", """
Yes, please. Suggestions, corrections and new questions are welcome through the project's
<a href="https://github.com/luvwagn/AmigaFAQ">GitHub repository</a>, where you can open an issue
or propose a change.
"""),
("Can I reuse the content?", """
Yes. The text of this site is licensed under the
<a href="https://creativecommons.org/licenses/by-sa/4.0/" rel="license">Creative Commons
Attribution-ShareAlike 4.0</a> licence. You may copy, adapt and share it, including commercially, as
long as you credit AmigaFAQ with a link to amigafaq.org and share your version under the same licence.
"""),
("Credits", """
Titles and headings use the Topaz typeface, as recreated in TrueType form by dMG/t!s^dS! in the
<a href="https://github.com/rewtnull/amigafonts">Multi Platform Amiga Fonts</a> collection, released
under the GNU GPL with font exception. Topaz is (c) Amiga Inc.

The mouse pointer comes from <a href="https://dkb-amiga.com">dkb-amiga.com</a> and is used with the
kind permission of Stefan Reinauer.

Amiga, AmigaOS and Workbench are trademarks of their respective owners. AmigaFAQ is an independent
fan site and is not affiliated with any of them.
"""),
]

# Model list for the Hardware page. Specs are the standard configuration as shipped.
# PAL machines run slightly slower than NTSC ones (7.09 vs 7.16MHz for the 68000).
MODELS = [
("Amiga 1000", "1985", "the original, which loaded its Kickstart firmware from floppy disk.",
 [("Form factor", "Desktop"),
  ("CPU", "Motorola 68000 at 7.16MHz (NTSC) / 7.09MHz (PAL)"),
  ("Chip RAM", "256KB (512KB with the front-panel expansion)"),
  ("Chipset", "OCS"),
  ("Hard drive interface", "n/a")]),
("Amiga 500", "1987", "the best-selling home model.",
 [("Form factor", "Wedge (computer in the keyboard)"),
  ("CPU", "Motorola 68000 at 7.16MHz (NTSC) / 7.09MHz (PAL)"),
  ("Chip RAM", "512KB"),
  ("Chipset", "OCS (some late units shipped with an ECS Agnus)"),
  ("Hard drive interface", "n/a")]),
("Amiga 2000", "1987", "a desktop \"big box\" with expansion slots.",
 [("Form factor", "Desktop"),
  ("CPU", "Motorola 68000 at 7.16MHz (NTSC) / 7.09MHz (PAL)"),
  ("Chip RAM", "512KB (1MB on later revisions)"),
  ("Chipset", "OCS (ECS on later revisions)"),
  ("Hard drive interface", "None built in; added with a Zorro II card such as the A2091 (SCSI)")]),
("Amiga 3000", "1990", "a 68030-based workstation with the ECS chipset.",
 [("Form factor", "Desktop"),
  ("CPU", "Motorola 68030 at 16MHz or 25MHz"),
  ("Chip RAM", "1MB (up to 2MB)"),
  ("Chipset", "ECS"),
  ("Hard drive interface", "SCSI (built in)")]),
("CDTV", "1991", "a CD-based multimedia player built on Amiga hardware.",
 [("Form factor", "Audio (hi-fi component style)"),
  ("CPU", "Motorola 68000 at 7.16MHz (NTSC) / 7.09MHz (PAL)"),
  ("Chip RAM", "1MB"),
  ("Chipset", "OCS (with the 1MB ECS Agnus)"),
  ("Hard drive interface", "n/a (CD-ROM drive)")]),
("Amiga 500 Plus", "1991", "an updated A500 with ECS and Kickstart 2.",
 [("Form factor", "Wedge (computer in the keyboard)"),
  ("CPU", "Motorola 68000 at 7.16MHz (NTSC) / 7.09MHz (PAL)"),
  ("Chip RAM", "1MB"),
  ("Chipset", "ECS"),
  ("Hard drive interface", "n/a")]),
("Amiga 3000T", "1991", "a tower version of the A3000, with more room for drives and Zorro III expansion cards.",
 [("Form factor", "Tower"),
  ("CPU", "Motorola 68030 at 25MHz"),
  ("Chip RAM", "1MB (up to 2MB)"),
  ("Chipset", "ECS"),
  ("Hard drive interface", "SCSI (built in)")]),
("Amiga 600", "1992", "a compact model with IDE and PCMCIA.",
 [("Form factor", "Wedge (compact, no numeric keypad)"),
  ("CPU", "Motorola 68000 at 7.16MHz (NTSC) / 7.09MHz (PAL)"),
  ("Chip RAM", "1MB (up to 2MB)"),
  ("Chipset", "ECS"),
  ("Hard drive interface", "IDE (44-pin, for 2.5-inch drives)")]),
("Amiga 1200", "1992", "the AGA home computer.",
 [("Form factor", "Wedge (computer in the keyboard)"),
  ("CPU", "Motorola 68EC020 at 14MHz"),
  ("Chip RAM", "2MB"),
  ("Chipset", "AGA"),
  ("Hard drive interface", "IDE (44-pin, for 2.5-inch drives)")]),
("Amiga 4000", "1992", "the AGA desktop flagship.",
 [("Form factor", "Desktop"),
  ("CPU", "Motorola 68040 at 25MHz (A4000/040) or 68EC030 at 25MHz (A4000/030)"),
  ("Chip RAM", "2MB"),
  ("Chipset", "AGA"),
  ("Hard drive interface", "IDE (40-pin, for 3.5-inch drives)")]),
("CD32", "1993", "a 32-bit CD games console based on the A1200.",
 [("Form factor", "Console"),
  ("CPU", "Motorola 68EC020 at 14MHz"),
  ("Chip RAM", "2MB"),
  ("Chipset", "AGA"),
  ("Hard drive interface", "n/a (CD-ROM drive)")]),
("Amiga 4000T", "1994", "a tower version of the A4000, one of Commodore's last machines. Escom later re-released it, including a 68060 version.",
 [("Form factor", "Tower"),
  ("CPU", "Motorola 68040 at 25MHz (Escom also offered a 68060 at 50MHz)"),
  ("Chip RAM", "2MB"),
  ("Chipset", "AGA"),
  ("Hard drive interface", "SCSI and IDE (both built in)")]),
]

CONTENT["web-sites"] = ("Useful Amiga web sites for software, games, hardware, emulation and community.", [
("Where can I download Amiga software?", """
<ul>
<li><a href="https://aminet.net/">Aminet</a> - the largest archive of freely distributable Amiga
software, running since the early 1990s.</li>
<li><a href="https://www.whdload.de/">WHDLoad</a> - the official home of WHDLoad, with installers for
running floppy games and demos from a hard disk.</li>
</ul>
"""),
("Where can I look up Amiga games?", """
<ul>
<li><a href="https://amiga.abime.net/">Hall of Light</a> - a very detailed database of Amiga games,
with screenshots, credits and scanned manuals.</li>
<li><a href="https://www.lemonamiga.com/">Lemon Amiga</a> - a popular game database with user
reviews and ratings.</li>
<li><a href="https://amr.abime.net/">Amiga Magazine Rack</a> - scans of classic Amiga magazines,
cross-referenced with the Hall of Light.</li>
</ul>
"""),
("Where can I find demos and music?", """
<ul>
<li><a href="https://www.pouet.net/">Pouet</a> - the main database of demoscene productions,
including thousands of Amiga demos.</li>
<li><a href="https://amp.dascene.net/">Amiga Music Preservation</a> - an archive of Amiga music
modules and the musicians who made them.</li>
</ul>
"""),
("Where can I look up Amiga hardware?", """
<ul>
<li><a href="https://bigbookofamigahardware.com/">Big Book of Amiga Hardware</a> - a huge reference
of Amiga computers, expansion cards, accelerators and peripherals, with photos and details.</li>
<li><a href="https://amiga.resource.cx/">Amiga Hardware Database</a> - specifications and photos of
Amiga models and expansion cards, with install disks, benchmark results and search by manufacturer,
chipset or autoconfig ID.</li>
<li><a href="https://wiki.amigaos.net/">AmigaOS Documentation Wiki</a> - developer and technical
documentation for AmigaOS.</li>
</ul>
"""),
("Where can I get Amiga emulators?", """
<ul>
<li><a href="https://www.winuae.net/">WinUAE</a> - the most accurate Amiga emulator, for Windows.</li>
<li><a href="https://fs-uae.net/">FS-UAE</a> - an emulator for Windows, macOS and Linux.</li>
<li><a href="https://amiberry.com/">Amiberry</a> - an emulator designed for Linux devices such as the
Raspberry Pi.</li>
<li><a href="https://github.com/dirkwhoffmann/vAmiga">vAmiga</a> - an accuracy-focused emulator for
macOS.</li>
<li><a href="https://github.com/CopperlineHQ/Copperline">Copperline</a> - a newer, free and
open-source emulator for Windows, macOS and Linux, focused on cycle-accurate hardware emulation.</li>
<li><a href="https://www.amigaforever.com/">Amiga Forever</a> - a licensed package of Kickstart ROMs,
Workbench and emulation software.</li>
</ul>
"""),
("Where can I talk with other Amiga users?", """
<ul>
<li><a href="https://eab.abime.net/">English Amiga Board</a> - one of the largest and most active
Amiga forums, covering hardware, software, games and emulation.</li>
<li><a href="https://www.amigalove.com/">AmigaLove</a> - a friendly forum and community, plus
in-depth game reviews and articles.</li>
<li><a href="https://www.a1k.org/">A1K</a> - a large German-language Amiga community.</li>
<li><a href="https://www.amiga-news.de/">amiga-news.de</a> - long-running Amiga news, in English and
German.</li>
</ul>
"""),
("Where can I get the current AmigaOS?", """
<ul>
<li><a href="https://www.hyperion-entertainment.com/">Hyperion Entertainment</a> - the developer of
AmigaOS 3.2 for classic Amigas and AmigaOS 4 for PowerPC systems.</li>
</ul>
"""),
("Which web sites work on a real Amiga web browser?", """
Most modern sites are too heavy for classic Amiga browsers, and many need encryption they cannot
handle. A few sites are built for old computers:

<ul>
<li><a href="http://frogfind.com/">FrogFind</a> - a search engine that turns web pages into simple
text-only versions that vintage browsers can show.</li>
<li><a href="http://68k.news/">68k.news</a> - a news site made for vintage computers and browsers.</li>
<li><a href="http://amigafaq.org/">AmigaFAQ</a> - this site, which works over plain HTTP on classic
Amiga browsers.</li>
</ul>
"""),
])

# Glossary: (term, definition). Grouped by first letter on the Glossary page.
GLOSSARY = [
("ADF", "Amiga Disk File: an image of an Amiga floppy disk, used by emulators and floppy emulators."),
("Agnus", "The OCS/ECS custom chip that controls memory access (DMA) and contains the Copper and the Blitter. Later versions, Fat Agnus and Super Agnus, can reach more Chip RAM. Its AGA equivalent is Alice."),
("AGA", "Advanced Graphics Architecture: the third-generation chipset, in the A1200, A4000 and CD32, with a 24-bit palette and up to 256 colours on screen."),
("Alice", "The AGA chip that replaced Agnus."),
("AmigaDOS", "The disk operating system part of AmigaOS, which handles files, drives and the command-line tools."),
("Aminet", "The largest archive of freely distributable Amiga software, online since the early 1990s."),
("ARexx", "A scripting language built into AmigaOS from version 2.0. Programs that offer an ARexx port can be controlled and linked together by scripts."),
("Autoconfig", "The Amiga's plug-and-play system: expansion cards identify themselves and are set up automatically at boot, with no jumpers or drivers needed for basic setup."),
("Bitplane", "The way Amiga graphics are stored: each bit of a pixel's colour number lives in a separate plane of memory. More bitplanes mean more colours, for example 5 bitplanes give 32 colours."),
("Blitter", "Part of Agnus (or Alice) that copies and combines blocks of memory very quickly, used heavily for drawing graphics and moving objects in games."),
("Chip RAM", "Memory shared by the processor and the custom chips. Graphics, sound and floppy data must be in Chip RAM."),
("CIA", "Complex Interface Adapter: two 8520 chips that handle the keyboard, floppy control signals, the parallel port, joysticks and timers."),
("CLI / Shell", "The Amiga command line, where commands such as Dir, Copy and Assign are typed. The Shell is the improved version from Workbench 1.3 onward."),
("Copper", "A simple co-processor in Agnus (or Alice) that changes hardware settings in step with the video beam. It produces effects like the colourful gradients known as copper bars."),
("Cracktro", "A short intro added to a pirated game by the group that removed its copy protection. Cracktros were a starting point for the demoscene."),
("Demoscene", "A creative community making real-time audiovisual productions (demos) that push hardware to its limits. The Amiga was one of its most important platforms."),
("Denise", "The OCS/ECS video chip that turns bitplanes and sprites into the picture on screen. Its AGA equivalent is Lisa."),
("Drawer", "Workbench's name for a folder or directory."),
("ECS", "Enhanced Chip Set: the second-generation chipset, adding more addressable Chip RAM and new screen modes."),
("EHB", "Extra Half-Brite: a screen mode showing 64 colours, where the extra 32 are half-brightness copies of the first 32."),
("Exec", "The multitasking kernel at the heart of AmigaOS."),
("Fast RAM", "Memory used only by the processor. Programs run faster from it because they never wait for the custom chips."),
("FFS / OFS", "Fast File System and Old (original) File System: the Amiga's disk formats. FFS, introduced with AmigaOS 1.3, is quicker and stores more data."),
("Flicker fixer / scan doubler", "A video upgrade that converts the Amiga's 15kHz picture into a VGA-style signal for modern monitors. A flicker fixer also removes the flicker of interlaced modes."),
("Gadget", "The Amiga term for a user interface control, such as a button, slider, or a window's close and depth gadgets."),
("Gotek", "A floppy drive replacement that loads disk images (ADF files) from a USB stick, widely used on real Amigas."),
("Guru Meditation", "The Amiga's name for a serious system error, shown as a flashing red box with an error code."),
("HAM", "Hold-And-Modify: a screen mode that shows far more colours by building each pixel from its neighbour: 4,096 colours in HAM6, and 262,144 in AGA's HAM8."),
("HDF", "An image of an Amiga hard disk or partition, used by emulators."),
("Info file", "A file ending in .info that stores a Workbench icon and settings for a program, project or drawer."),
("Interlace", "A screen mode that doubles vertical resolution by drawing alternate lines on each frame, which flickers on a normal monitor."),
("Intuition", "The AmigaOS library that provides screens, windows, menus and gadgets."),
("IPF", "A preservation-quality floppy image that also captures the original copy protection."),
("Kickstart", "The core of AmigaOS, stored in ROM (or, on the A1000, loaded from disk), which boots the machine."),
("Lisa", "The AGA video chip that replaced Denise."),
("Module (MOD)", "A music file made with a tracker, containing both instrument samples and note patterns. The format began on the Amiga."),
("OCS", "Original Chip Set: the first-generation chipset, in the A1000, early A500s and A2000s."),
("Paula", "The custom chip that plays 4-channel, 8-bit sampled sound and also handles floppy data, the serial port and interrupts."),
("PCMCIA", "The credit-card-sized expansion slot on the A600 and A1200, used for memory, network cards and CompactFlash adapters."),
("RDB", "Rigid Disk Block: the area at the start of an Amiga hard disk that records its partitions and file systems."),
("Requester", "The Amiga term for a dialogue box, such as an About box or a file requester."),
("Screen", "In AmigaOS, programs can open their own screens, each with its own resolution and colours. Screens can be dragged down to reveal the ones behind them."),
("Slow RAM", "Extra memory, such as the A500 trapdoor expansion, that sits on the custom chips' bus. Only the processor uses it, but it is no faster than Chip RAM."),
("Startup-sequence", "The script in the S: drawer that runs when an Amiga boots from disk."),
("Tracker", "A music program that arranges samples in a vertical grid of patterns. Ultimate Soundtracker on the Amiga started the format."),
("Trapdoor", "The expansion slot underneath the A500 and A1200, used for memory and, on the A1200, accelerator cards."),
("WHDLoad", "A system that lets floppy-based games and demos be installed and run from a hard disk."),
("Workbench", "The Amiga's graphical desktop and its set of tools."),
("Zorro", "The expansion bus in the big-box Amigas: 16-bit Zorro II in the A2000, and 32-bit Zorro III in the A3000 and A4000."),
]

def _glossary_groups():
    groups = {}
    for term, definition in sorted(GLOSSARY, key=lambda t: t[0].lower()):
        letter = term[0].upper()
        groups.setdefault(letter, []).append((term, definition))
    out = []
    for letter in sorted(groups):
        items = "\n".join("<dt>%s</dt>\n<dd>%s</dd>" % td for td in groups[letter])
        out.append((letter, '<dl class="gloss">\n%s\n</dl>' % items))
    return out

CONTENT["glossary"] = ("Amiga terms and jargon, explained.", _glossary_groups())

# ---- Hardware sub-topics ----
CONTENT["hardware"] = ("Amiga hardware, from the models and chipsets to sound, video and third-party upgrades.", [])

CONTENT["hardware-audio"] = ("The Amiga's sound hardware and how to get the best from it.", [
("What sound hardware does the Amiga have?", """
Sound comes from the Paula custom chip, which plays four channels of 8-bit sampled sound at the same
time, two on the left and two on the right. Because it plays real recorded samples rather than
synthesized tones, the Amiga could produce music and effects far more realistic than most home
computers of the 1980s.
"""),
("Why does Amiga sound seem muffled at times?", """
Most Amigas have a built-in low-pass audio filter that softens high frequencies. On many models it is
linked to the power LED: when software switches the filter off, the power light dims. Some programs
and games turn the filter on or off, which is why the same machine can sound brighter or duller.
"""),
("How do I connect an Amiga to speakers or an amplifier?", """
Most Amigas have two RCA (phono) sockets, one for the left channel and one for the right, carrying a
line-level signal. Connect them to powered speakers, a stereo amplifier or a mixer using an ordinary
RCA cable, with an RCA-to-3.5mm adapter if your speakers need one.
"""),
("Can an Amiga play higher-quality sound?", """
Yes. Expansion sound cards add 16-bit audio, and the AHI system lets programs use them in a standard
way. AHI can also combine Paula's channels in software to get better than 8-bit quality from the
built-in hardware.
"""),
("Can I use MIDI with an Amiga?", """
Yes. A MIDI interface plugs into the Amiga's serial port, letting it control synthesizers and other
MIDI instruments with sequencer software.
"""),
])

CONTENT["hardware-video"] = ("Video outputs, screen modes, graphics cards and video production.", [
("What video outputs does the Amiga have?", """
Every Amiga has a 23-pin analog RGB port, which gives the best picture on a compatible monitor. The
A500 and A2000 also have a monochrome composite output. The A1000 has a colour composite output, and
the A600 and A1200 have colour composite plus a built-in RF output for connecting to a TV. The A500
can also use an RF modulator plugged into its RGB port.

For connecting to modern screens, see <a href="hardware-general.html#how-do-i-connect-an-amiga-to-a-modern-monitor-or-tv">connecting
to a modern monitor or TV</a>.
"""),
("What screen modes can an Amiga display?", """
The standard modes are low resolution (320 pixels wide) and high resolution (640 pixels wide), with
256 lines on PAL machines and 200 on NTSC. Interlace doubles the number of lines, at the cost of
flicker on an ordinary monitor.

ECS and AGA machines add productivity modes, such as 640x480 without flicker, but these need a
monitor that can handle higher scan rates.
"""),
("What are flicker fixers and scan doublers?", """
Both convert the Amiga's 15kHz picture into a higher-frequency signal that VGA-style monitors can
show. A flicker fixer also removes the flicker of interlaced modes. The A3000 has one built in;
for other models it is an upgrade fitted inside the computer.
"""),
("What are graphics cards (RTG) on the Amiga?", """
Graphics cards plug into the expansion slots of big-box Amigas and add high resolutions and many
more colours than the built-in chipset. Software systems such as Picasso96 and CyberGraphX, often
called RTG (retargetable graphics), let Workbench and programs use these cards.
"""),
("What is a genlock?", """
A genlock synchronizes the Amiga's picture with an outside video source, so Amiga graphics can be
overlaid on live video. It made the Amiga popular for titles and effects in video production.
"""),
])

CONTENT["hardware-third-party"] = ("Upgrades and add-ons made by companies other than Commodore.", [
("What is third-party Amiga hardware?", """
Third-party hardware is anything made by companies other than Commodore: accelerators, memory
expansions, hard disk controllers, graphics and sound cards, network cards, and video production
equipment. Much of the Amiga's long life comes from this hardware.
"""),
("Which companies made classic Amiga upgrades?", """
<ul>
<li><b>GVP (Great Valley Products)</b> - accelerators and hard disk controllers.</li>
<li><b>Phase 5</b> - the Blizzard and CyberStorm accelerators and CyberVision graphics cards.</li>
<li><b>Village Tronic</b> - the Picasso graphics cards.</li>
<li><b>NewTek</b> - the Video Toaster video production system for the A2000.</li>
</ul>
"""),
("Is new Amiga hardware still being made?", """
Yes. Companies and hobbyists still make accelerators, memory, network and USB adapters, video
upgrades and replacement parts. Examples include Individual Computers, the open-source PiStorm
project, Terrible Fire's open-source accelerators and the Apollo Team's FPGA-based Vampire boards.
"""),
("Where can I look up a particular expansion card?", """
The <a href="https://bigbookofamigahardware.com/">Big Book of Amiga Hardware</a> and the
<a href="https://amiga.resource.cx/">Amiga Hardware Database</a> both catalogue thousands of
expansion cards and peripherals, with photos and specifications.
"""),
])
