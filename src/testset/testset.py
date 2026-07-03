test_set = [
    # --- Type / Sensor / Lens ---
    {"question": "What type of camera is the Nikon D3300?", "answer": "Single-lens reflex digital camera"},
    {"question": "What lens mount does the Nikon D3300 use?", "answer": "Nikon F mount (with AF contacts)"},
    {"question": "What is the effective angle of view of the D3300 relative to FX format lenses?", "answer": "approx. 1.5× that of lenses with FX format angle of view"},
    {"question": "What is the effective pixel count of the Nikon D3300?", "answer": "24.2 million"},
    {"question": "What is the total pixel count of the Nikon D3300 image sensor?", "answer": "24.78 million"},
    {"question": "What is the size of the Nikon D3300 image sensor?", "answer": "23.5 × 15.6 mm"},
    {"question": "What type of image sensor does the Nikon D3300 use?", "answer": "CMOS sensor"},
    {"question": "What dust-reduction system does the D3300 use?", "answer": "Image sensor cleaning, Image Dust Off reference data"},

    # --- Storage ---
    {"question": "What is the image size in pixels for Large images in modes other than easy panorama?", "answer": "6000 × 4000"},
    {"question": "What is the image size in pixels for Medium images in modes other than easy panorama?", "answer": "4496 × 3000"},
    {"question": "What is the image size in pixels for Small images in modes other than easy panorama?", "answer": "2992 × 2000"},
    {"question": "What is the image size for a normal, horizontal easy panorama?", "answer": "4800 × 1080"},
    {"question": "What is the image size for a normal, vertical easy panorama?", "answer": "1632 × 4800"},
    {"question": "What is the image size for a wide, horizontal easy panorama?", "answer": "9600 × 1080"},
    {"question": "What is the image size for a wide, vertical easy panorama?", "answer": "1632 × 9600"},
    {"question": "What bit depth is used for NEF (RAW) files on the D3300?", "answer": "12 bit, compressed"},
    {"question": "What compression ratio does JPEG fine quality use on the D3300?", "answer": "approx. 1 : 4"},
    {"question": "What compression ratio does JPEG normal quality use on the D3300?", "answer": "approx. 1 : 8"},
    {"question": "What compression ratio does JPEG basic quality use on the D3300?", "answer": "approx. 1 : 16"},
    {"question": "What Picture Control options are available on the D3300?", "answer": "Standard, Neutral, Vivid, Monochrome, Portrait, Landscape"},
    {"question": "What types of memory cards does the D3300 support?", "answer": "SD (Secure Digital) and UHS-I compliant SDHC and SDXC memory cards"},
    {"question": "What file system standards does the D3300 support?", "answer": "DCF 2.0, DPOF, Exif 2.3, PictBridge"},

    # --- Viewfinder ---
    {"question": "What type of viewfinder does the D3300 have?", "answer": "Eye-level pentamirror single-lens reflex viewfinder"},
    {"question": "What is the frame coverage of the D3300 viewfinder?", "answer": "Approx. 95% horizontal and 95% vertical"},
    {"question": "What is the magnification of the D3300 viewfinder?", "answer": "Approx. 0.85×"},
    {"question": "What is the eyepoint of the D3300 viewfinder?", "answer": "18 mm (–1.0 m–1)"},
    {"question": "What is the diopter adjustment range of the D3300 viewfinder?", "answer": "–1.7–+0.5 m–1"},
    {"question": "What type of focusing screen does the D3300 use?", "answer": "Type B BriteView Clear Matte Mark VII screen"},
    {"question": "What type of reflex mirror does the D3300 use?", "answer": "Quick return"},
    {"question": "What lenses can be used with the D3300's electronic rangefinder?", "answer": "lenses that have a maximum aperture of f/5.6 or faster"},
    {"question": "Which lens types support autofocus on the D3300?", "answer": "AF-S, AF-P, and AF-I lenses"},

    # --- Shutter / Release ---
    {"question": "What type of shutter does the D3300 have?", "answer": "Electronically-controlled vertical-travel focal-plane shutter"},
    {"question": "What is the shutter speed range of the D3300?", "answer": "1/4000 – 30 s in steps of 1/3 EV; Bulb; Time"},
    {"question": "What is the flash sync speed of the D3300?", "answer": "X= 1/200 s"},
    {"question": "What is the maximum continuous shooting frame advance rate of the D3300?", "answer": "Up to 5 fps"},
    {"question": "What self-timer durations are available on the D3300?", "answer": "2 s, 5 s, 10 s, 20 s; 1–9 exposures"},
    {"question": "What does pressing the I (E/#) button let you choose?", "answer": "the release mode (how the shutter is released)"},
    {"question": "What happens in Single frame release mode?", "answer": "Camera takes one photograph each time shutter-release button is pressed"},
    {"question": "What happens in Continuous release mode?", "answer": "The camera takes photographs while the shutter-release button is pressed"},
    {"question": "How is Quiet shutter release different from single-frame release?", "answer": "Camera noise is reduced"},
    {"question": "How long after pressing the shutter-release button is the shutter released in self-timer mode?", "answer": "about 10 seconds"},
    {"question": "When using delayed remote (ML-L3), how long after the remote button is pressed is the shutter released?", "answer": "2 s"},

    # --- Exposure / Metering ---
    {"question": "How many pixels does the D3300's RGB sensor use for TTL exposure metering?", "answer": "420-pixel RGB sensor"},
    {"question": "What metering system is used for matrix metering with type G, E, and D lenses on the D3300?", "answer": "3D color matrix metering II"},
    {"question": "What weight is given to the 8-mm circle in center-weighted metering on the D3300?", "answer": "75%"},
    {"question": "What percentage of the frame does spot metering meter on the D3300?", "answer": "about 2.5% of frame (3.5-mm circle)"},
    {"question": "What is the exposure range for matrix or center-weighted metering on the D3300?", "answer": "0–20 EV"},
    {"question": "What is the exposure range for spot metering on the D3300?", "answer": "2–20 EV"},
    {"question": "What is the exposure compensation range on the D3300?", "answer": "–5 – +5 EV in increments of 1/3 EV"},
    {"question": "What button locks exposure on the D3300?", "answer": "A (L) button"},
    {"question": "What is the ISO sensitivity range of the D3300?", "answer": "ISO 100 – 12800 in steps of 1 EV"},
    {"question": "What is the maximum extended ISO sensitivity equivalent on the D3300?", "answer": "approx. 1 EV (ISO 25600 equivalent) above ISO 12800"},
    {"question": "What Active D-Lighting settings are available on the D3300?", "answer": "On, off"},

    # --- Focus ---
    {"question": "What autofocus sensor module does the D3300 use?", "answer": "Nikon Multi-CAM 1000 autofocus sensor module"},
    {"question": "How many focus points does the D3300 autofocus system have?", "answer": "11 focus points (including one cross-type sensor)"},
    {"question": "What is the AF-assist illuminator range on the D3300?", "answer": "approx. 0.5–3 m/1 ft 8 in.–9 ft 10 in."},
    {"question": "What is the autofocus detection range of the D3300?", "answer": "–1 – +19 EV (ISO 100, 20 °C/68 °F)"},
    {"question": "What autofocus lens servo modes are available on the D3300?", "answer": "Single-servo AF (AF-S); continuous-servo AF (AF-C); auto AF-S/AF-C selection (AF-A)"},
    {"question": "What AF-area modes are available on the D3300?", "answer": "Single-point AF, dynamic-area AF, auto-area AF, 3D-tracking (11 points)"},
    {"question": "How is focus locked on the D3300 in single-servo AF?", "answer": "by pressing shutter-release button halfway"},

    # --- Flash ---
    {"question": "What flash modes are available with the i, k, p, n, o, S, T, U, g, and ' modes on the D3300?", "answer": "Auto flash with auto pop-up"},
    {"question": "How is the built-in flash activated in P, S, A, and M modes on the D3300?", "answer": "Manual pop-up with button release"},
    {"question": "What is the Guide Number of the D3300's built-in flash?", "answer": "Approx. 12/39 (m/ft, ISO 100, 20 °C/68 °F)"},
    {"question": "What flash control system does the D3300 use with the built-in flash and compatible Speedlights?", "answer": "i-TTL flash control using 420-pixel RGB sensor"},
    {"question": "Which Speedlights support i-TTL flash control with the D3300's built-in flash?", "answer": "SB-910, SB-900, SB-800, SB-700, SB-600, SB-400, or SB-300"},
    {"question": "What flash modes are available on the D3300?", "answer": "Auto, auto with red-eye reduction, auto slow sync, auto slow sync with red-eye reduction, fill-flash, red-eye reduction, slow sync, slow sync with red-eye reduction, rear-curtain with slow sync, rear-curtain sync, off"},
    {"question": "What is the flash compensation range on the D3300?", "answer": "–3 – +1 EV in increments of 1/3 EV"},
    {"question": "What type of accessory shoe does the D3300 have?", "answer": "ISO 518 hot-shoe with sync and data contacts and safety lock"},
    {"question": "What Speedlights can act as a master flash for the Nikon Creative Lighting System on the D3300?", "answer": "SB-910, SB-900, SB-800, or SB-700"},
    {"question": "What sync terminal adapter is available for the D3300?", "answer": "AS-15 sync terminal adapter"},

    # --- White balance / Live view ---
    {"question": "What white balance options are available on the D3300?", "answer": "Auto, incandescent, fluorescent (7 types), direct sunlight, flash, cloudy, shade, preset manual"},
    {"question": "What lens servo options are available in live view on the D3300?", "answer": "Single-servo AF (AF-S); full-time-servo AF (AF-F)"},
    {"question": "What AF-area modes are available in live view on the D3300?", "answer": "Face-priority AF, wide-area AF, normal-area AF, subject-tracking AF"},
    {"question": "What type of autofocus detection is used in live view on the D3300?", "answer": "Contrast-detect AF anywhere in frame"},

    # --- Movie ---
    {"question": "What metering system is used for movies on the D3300?", "answer": "TTL exposure metering using main image sensor"},
    {"question": "What is the maximum movie frame size on the D3300?", "answer": "1920 × 1080"},
    {"question": "What frame rates are available at 1920 × 1080 on the D3300?", "answer": "60p (progressive)/50p/30p/25p/24p"},
    {"question": "What frame rates are available at 1280 × 720 on the D3300?", "answer": "60p/50p"},
    {"question": "What frame rates are available at 640 × 424 on the D3300?", "answer": "30p/25p"},
    {"question": "What is the actual frame rate when 30p is selected with NTSC video mode on the D3300?", "answer": "29.97 fps"},
    {"question": "What is the actual frame rate when 60p is selected with NTSC video mode on the D3300?", "answer": "59.94 fps"},
    {"question": "What is the actual frame rate when 24p is selected on the D3300?", "answer": "23.976 fps"},
    {"question": "What file format does the D3300 use for movies?", "answer": "MOV"},
    {"question": "What video compression format does the D3300 use for movies?", "answer": "H.264/MPEG-4 Advanced Video Coding"},
    {"question": "What audio recording format does the D3300 use?", "answer": "Linear PCM"},
    {"question": "What audio recording devices does the D3300 support?", "answer": "Built-in monaural or external stereo microphone"},
    {"question": "What is the ISO sensitivity range for movies on the D3300?", "answer": "ISO 100–12800"},

    # --- Monitor / Playback ---
    {"question": "What is the size of the D3300 monitor?", "answer": "7.5-cm (3-in.)"},
    {"question": "How many dots does the D3300 monitor have?", "answer": "approx. 921k-dot (VGA)"},
    {"question": "What is the viewing angle of the D3300 monitor?", "answer": "170°"},
    {"question": "What frame coverage does the D3300 monitor provide?", "answer": "approx. 100% frame coverage"},
    {"question": "What playback options are available on the D3300?", "answer": "Full-frame and thumbnail (4, 9, or 72 images or calendar) playback with playback zoom, movie and panorama playback, photo and/or movie slide shows, histogram display, highlights, auto image rotation, picture rating, and image comment"},
    {"question": "How many characters can an image comment contain on the D3300?", "answer": "up to 36 characters"},

    # --- Interface / Power ---
    {"question": "What USB standard does the D3300 support?", "answer": "Hi-Speed USB"},
    {"question": "What video output standards does the D3300 support?", "answer": "NTSC, PAL"},
    {"question": "What type of HDMI connector does the D3300 have?", "answer": "Type C mini-pin HDMI connector"},
    {"question": "What wireless remote controllers are supported via the D3300's accessory terminal?", "answer": "WR-1, WR-R10"},
    {"question": "What remote cord is supported via the D3300's accessory terminal?", "answer": "MC-DC2"},
    {"question": "What GPS units are supported via the D3300's accessory terminal?", "answer": "GP-1/GP-1A"},
    {"question": "What is the audio input jack size on the D3300?", "answer": "3.5mm diameter (stereo mini-pin jack)"},
    {"question": "What battery does the D3300 use?", "answer": "One rechargeable Li-ion EN-EL14a battery"},
    {"question": "What AC adapter is compatible with the D3300?", "answer": "EH-5b AC adapter"},
    {"question": "What power connector is required to use the EH-5b AC adapter with the D3300?", "answer": "EP-5A power connector"},
    {"question": "What tripod socket standard does the D3300 use?", "answer": "1/4 in. (ISO 1222)"},

    # --- Dimensions / Environment ---
    {"question": "What are the dimensions of the D3300 (W × H × D)?", "answer": "Approx. 124 × 98 × 75.5 mm (4.9 × 3.9 × 3 in.)"},
    {"question": "What is the weight of the D3300 with battery and memory card but without body cap?", "answer": "Approx. 460 g (1 lb 0.2 oz)"},
    {"question": "What is the weight of the D3300 camera body only?", "answer": "Approx. 410 g/14.5 oz"},
    {"question": "What is the operating temperature range of the D3300?", "answer": "0 °C–40 °C (+32 °F–104 °F)"},
    {"question": "What is the maximum operating humidity for the D3300?", "answer": "85% or less (no condensation)"},

    # --- Kit lens ---
    {"question": "What is the filter-attachment size of the AF-S DX NIKKOR 18-55mm kit lens?", "answer": "52 mm (P=0.75 mm)"},
    {"question": "What are the dimensions of the AF-S DX NIKKOR 18-55mm kit lens?", "answer": "Approx. 66 mm diameter × 59.5 mm"},
    {"question": "What is the weight of the AF-S DX NIKKOR 18-55mm kit lens?", "answer": "Approx. 195 g (6.9 oz)"},

    # --- Battery life ---
    {"question": "How many shots can be taken with a fully-charged EN-EL14a battery in single-frame release mode (CIPA standard)?", "answer": "Approximately 700 shots"},
    {"question": "How many shots can be taken with a fully-charged EN-EL14a battery in continuous release mode (Nikon standard)?", "answer": "Approximately 2500 shots"},
    {"question": "How long can movies be recorded with a fully-charged EN-EL14a battery at 1080/60p and 1080/50p?", "answer": "Approximately 55 minutes"},
    {"question": "What is the capacity of the EN-EL14a battery?", "answer": "1230 mAh"},
    {"question": "What is the maximum length or size for an individual movie recorded on the D3300?", "answer": "up to 20 minutes in length or 4 GB in size"},
    {"question": "Name three factors that can reduce battery life on the D3300.", "answer": "Using the monitor, keeping the shutter-release button pressed halfway, repeated autofocus operations (also: taking NEF (RAW) photographs, slow shutter speeds, using a GPS unit, using an Eye-Fi card, using a WU-1a wireless mobile adapter, using VR mode, repeatedly zooming with an AF-P lens)"},
    {"question": "About how long does it take to fully charge an exhausted EN-EL14a battery?", "answer": "about an hour and 50 minutes"},
    {"question": "What temperature range is recommended for charging the battery indoors on the D3300?", "answer": "5 °C–35 °C (41 °F–95 °F)"},
    {"question": "Below what temperature will the EN-EL14a battery not charge?", "answer": "below 0 °C (32 °F)"},
    {"question": "Above what temperature will the EN-EL14a battery not charge?", "answer": "above 60 °C (140 °F)"},

    # --- Buttons / Controls ---
    {"question": "What does pressing the R button display on the D3300?", "answer": "The information display"},
    {"question": "What does pressing the G button display on the D3300?", "answer": "The camera menus"},
    {"question": "What does pressing the P button allow you to change on the D3300?", "answer": "Settings shown at the bottom of the information display (white balance, image size, image quality, flash mode, ISO sensitivity, exposure compensation, etc.)"},
    {"question": "What is the function of the W (Q) button when a help icon is displayed?", "answer": "It displays a description of the currently selected option or menu while pressed"},
    {"question": "How long after no operations are performed will the D3300 monitor turn off automatically?", "answer": "about 8 seconds"},
    {"question": "What menu setting controls how long the monitor remains on?", "answer": "Auto off timers option in the setup menu"},
    {"question": "What button is used to lock exposure or autofocus on the D3300?", "answer": "A (L) button"},
    {"question": "What does the Fn button allow on the D3300?", "answer": "Custom function assignment (configurable via the setup menu)"},
    {"question": "How is the number of exposures remaining over 1000 displayed on the D3300?", "answer": "Shown in thousands, indicated by the letter \"k\""},

    # --- Mode dial ---
    {"question": "What does the g mode on the D3300 mode dial provide?", "answer": "Take, view, and edit pictures and adjust settings with the help of an on-screen guide"},
    {"question": "What are the auto modes available on the D3300 mode dial?", "answer": "i Auto and j Auto (flash off)"},
    {"question": "What are the four full-control exposure modes on the D3300 mode dial?", "answer": "P (Programmed auto), S (Shutter-priority auto), A (Aperture-priority auto), M (Manual)"},
    {"question": "What scene modes are available on the D3300 mode dial?", "answer": "Portrait, Landscape, Child, Sports, Close up, Night portrait"},
    {"question": "What special effects modes are available on the D3300?", "answer": "Night vision, Super vivid, Pop, Photo illustration, Color sketch, Toy camera effect, Miniature effect, Selective color, Silhouette, High key, Low key, HDR painting, Easy panorama"},

    # --- Menus ---
    {"question": "What menu items are found in the D3300's Playback Menu?", "answer": "Delete, Playback folder, Playback display options, Image review, Rotate tall, Slide show, DPOF print order, Rating, Select to send to smart device"},
    {"question": "What menu items are found in the D3300's Shooting Menu?", "answer": "Reset shooting menu, Image quality, Image size, White balance, Set Picture Control, Auto distortion control, Color space, Active D-Lighting, Noise reduction, ISO sensitivity settings, AF-area mode, Built-in AF-assist illuminator, Metering, Flash cntrl for built-in flash, Optical VR, Movie settings"},
    {"question": "What menu items are found in the D3300's Setup Menu?", "answer": "Reset setup options, Format memory card, Monitor brightness, Info display format, Auto info display, Clean image sensor, Lock mirror up for cleaning, Image Dust Off ref photo, Flicker reduction, Time zone and date, Language, Auto image rotation, Image comment, Auto off timers, Self-timer, Remote on duration, Beep, Rangefinder, File number sequence, Buttons, Slot empty release lock, Print date, Storage folder, Accessory terminal, Video mode, HDMI, Wireless mobile adapter, Eye-Fi upload, Firmware version"},
    {"question": "What menu items are found in the D3300's Retouch Menu?", "answer": "D-Lighting, Red-eye correction, Trim, Monochrome, Filter effects, Color balance, Image overlay, NEF (RAW) processing, Resize, Quick retouch, Straighten, Distortion control, Fisheye, Color outline, Photo illustration, Color sketch, Perspective control, Miniature effect, Selective color, Edit movie, Side-by-side comparison"},
    {"question": "How many settings does the Recent Settings menu list on the D3300?", "answer": "the twenty most recently used settings"},
    {"question": "When is the Side-by-side comparison option available in the Retouch Menu?", "answer": "Only if the retouch menu is displayed by pressing P and selecting Retouch in full-frame playback when a retouched image or original is displayed"},
    {"question": "What button is used to exit menus and return to shooting mode on the D3300?", "answer": "Press the shutter-release button halfway"},

    # --- Package contents / setup ---
    {"question": "What items are included in the D3300 package contents?", "answer": "DK-25 rubber eyecup, BF-1B body cap, D3300 camera, EN-EL14a rechargeable Li-ion battery, MH-24 battery charger, AN-DC3 strap, UC-E17 USB cable, EG-CP14 audio/video cable, ViewNX 2 CD-ROM, User's Manual, Warranty"},
    {"question": "What is required to view manuals using the Nikon Manual Viewer 2 app?", "answer": "An Internet connection"},
    {"question": "What battery charger is included with the D3300?", "answer": "MH-24 battery charger"},
    {"question": "What strap is included with the D3300?", "answer": "AN-DC3 strap"},
    {"question": "What USB cable is included with the D3300?", "answer": "UC-E17 USB cable"},
    {"question": "What languages are not supported on cameras purchased in Japan?", "answer": "Languages other than English and Japanese"},
    {"question": "What should always be done before inserting or removing batteries or memory cards on the D3300?", "answer": "Always turn the camera off"},
    {"question": "How is the battery inserted into the D3300?", "answer": "In the orientation shown, using the battery to keep the orange battery latch pressed to one side"},
    {"question": "How is a memory card inserted into the D3300?", "answer": "Slide the memory card in until it clicks into place"},
    {"question": "What must be done before taking pictures after attaching a lens to the D3300?", "answer": "Remove the lens cap"},
    {"question": "How is the D3300 turned on?", "answer": "Rotate the power switch"},
    {"question": "What is displayed the first time the D3300 is turned on?", "answer": "A language-selection dialog"},
    {"question": "What clock format does the D3300 use?", "answer": "A 24-hour clock"},
    {"question": "How is the D3300 viewfinder focused?", "answer": "Rotate the diopter adjustment control until the focus points are in sharp focus"},

    # --- ViewNX 2 / software ---
    {"question": "What software is supplied with the D3300 for viewing and editing photographs and movies?", "answer": "ViewNX 2"},
    {"question": "Why should the latest version of ViewNX 2 be used with the D3300?", "answer": "Earlier versions that do not support the D3300 may fail to transfer NEF (RAW) images correctly"},
    {"question": "What CPU is recommended on Windows for viewing 1280×720 30fps-or-above movies in ViewNX 2?", "answer": "Pentium D 2 GHz or better; Intel Core i5 or better recommended"},

    # --- Troubleshooting / Errors ---
    {"question": "What should you do if the subject is too dark and shooting in S mode on the D3300?", "answer": "Lower shutter speed"},
    {"question": "What should you do if the subject is too bright and shooting in A mode on the D3300?", "answer": "Choose a smaller aperture (higher f-number)"},
    {"question": "What focal length is required to shoot panoramas on the D3300?", "answer": "55 mm or less"},
    {"question": "What should be done if a metering error occurs on the D3300?", "answer": "Release shutter; if error persists or appears frequently, consult a Nikon-authorized service representative"},
    {"question": "What causes the message 'Folder contains no images' on the D3300?", "answer": "The folder selected for playback contains no images"},
    {"question": "What is recommended if the internal circuits are too warm to resume live view or movie recording?", "answer": "Wait for the internal circuits to cool"},
    {"question": "Why might images created with other devices not be retouchable on the D3300?", "answer": "Because the camera cannot retouch images created with other devices"},

    # --- Trademarks / misc ---
    {"question": "Who holds the trademark for HDMI on devices like the D3300?", "answer": "HDMI Licensing LLC"},
    {"question": "Where was the D3300 User's Manual printed (per the manual provided)?", "answer": "Thailand"},
    {"question": "Who is the author/publisher of the D3300 manual?", "answer": "Nikon Corporation"},
]