import streamlit as st
import streamlit.components.v1 as components

from pathlib import Path
import base64
import mimetypes
import html


# ============================================================
# STREAMLIT CONFIG
# ============================================================

st.set_page_config(
    page_title="A Little Surprise 💙",
    page_icon="💙",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# PERSONAL DETAILS
# ============================================================

HER_NAME = "🎀DHANUSRI🎀"

# ------------------------------------------------------------
# IMPORTANT:
# Enter her birthday as DDMMYYYY.
#
# Example:
# 25 August 2004
# = 25082004
# ------------------------------------------------------------

BIRTHDAY_PASSWORD = "12092005"


# ============================================================
# SONG TITLE
# ============================================================

SONG_TITLE = "💙முதல் தோழி💙"


# ============================================================
# FINAL DESCRIPTION
# ============================================================

HER_DESCRIPTION = """
Some people come into our lives✨ and slowly become
a beautiful part of our story💙.

You are one of those people.

Your smile😊, your kindness, your laughter,
your craziness, your little habits and all
the memories we have created together make
you truly special🫂.

Thank you for being there through the good days💙,
the bad days, the silly conversations,
the random laughs and all those unforgettable
moments✨.

I am genuinely lucky to have a best friend like you❤️‍🩹.

I hope this birthday brings you happiness😘,
peace, success, beautiful memories and everything
your heart💙 wishes for.

Never stop smiling🤗.

Never stop being yourself💫.

And always remember that you are someone
very special💎 to me Mchaaaa🫂🎀.

Happy Birthday, my best Machaa. 💙♾️
"""


# ============================================================
# PROJECT PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

ASSETS_DIR = BASE_DIR / "assets"

# Create assets folder automatically
ASSETS_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# FIND IMAGES
# ============================================================

IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp"
}

AUDIO_EXTENSIONS = {
    ".mp3",
    ".mpeg",
    ".mp4",
    ".wav",
    ".ogg",
    ".m4a"
}


image_files = sorted(
    [
        file
        for file in ASSETS_DIR.iterdir()
        if file.is_file()
        and file.suffix.lower() in IMAGE_EXTENSIONS
    ],
    key=lambda x: x.name.lower()
)


audio_files = sorted(
    [
        file
        for file in ASSETS_DIR.iterdir()
        if file.is_file()
        and file.suffix.lower() in AUDIO_EXTENSIONS
    ],
    key=lambda x: x.name.lower()
)


# ============================================================
# FILE TO BASE64
# ============================================================

def file_to_base64(file_path):

    with open(
        file_path,
        "rb"
    ) as file:

        return base64.b64encode(
            file.read()
        ).decode("utf-8")


# ============================================================
# LOAD PHOTOS
# ============================================================

photos = []

for image_file in image_files:

    try:

        encoded = file_to_base64(
            image_file
        )

        mime_type, _ = mimetypes.guess_type(
            image_file.name
        )

        if not mime_type:
            mime_type = "image/jpeg"

        photos.append(
            {
                "src":
                    f"data:{mime_type};base64,{encoded}",

                "name":
                    image_file.stem
            }
        )

    except Exception:
        continue


# ============================================================
# LOAD SONG
# ============================================================

audio_source = ""

if audio_files:

    selected_audio = audio_files[0]

    try:

        encoded_audio = file_to_base64(
            selected_audio
        )

        extension = selected_audio.suffix.lower()

        mime_type_map = {
            ".mp3": "audio/mpeg",
            ".mpeg": "audio/mpeg",
            ".wav": "audio/wav",
            ".ogg": "audio/ogg",
            ".m4a": "audio/mp4",
            ".mp4": "audio/mp4"
        }

        mime_type = mime_type_map.get(
            extension,
            "audio/mpeg"
        )

        audio_source = (
            f"data:{mime_type};base64,"
            f"{encoded_audio}"
        )

    except Exception:
        audio_source = ""


# ============================================================
# ESCAPE TEXT
# ============================================================

safe_name = html.escape(
    HER_NAME
)

safe_song_title = html.escape(
    SONG_TITLE
)

safe_description = html.escape(
    HER_DESCRIPTION
)


# ============================================================
# MEMORY GALLERY
# ============================================================

memory_captions = [
    "A beautiful memory 💙",
    "One of my favourite moments ✨",
    "Just us being us 😄",
    "A moment worth remembering ☁️",
    "Another chapter of our story 💙",
    "Forever one of my favourites ♾️",
    "A little moment, a big memory ✨",
    "Always worth remembering 💙"
]


memory_html = ""

if photos:

    for index, photo in enumerate(photos):

        caption = memory_captions[
            index % len(memory_captions)
        ]

        memory_html += f"""
        <div class="memory-card">

            <div class="memory-number">
                {index + 1:02d}
            </div>

            <img
                src="{photo['src']}"
                alt="Memory {index + 1}"
            >

            <div class="memory-caption">
                {caption}
            </div>

        </div>
        """

else:

    memory_html = """
    <div class="empty-memory">

        <div class="empty-icon">
            📸
        </div>

        <h3>
            Memories will appear here
        </h3>

        <p>
            Add your photos to the
            <b>assets</b> folder.
        </p>

    </div>
    """


# ============================================================
# AUDIO
# ============================================================

if audio_source:

    audio_html = f"""
    <audio
        id="birthdayAudio"
        preload="metadata"
    >

        <source
            src="{audio_source}"
            type="audio/mpeg"
        >

    </audio>
    """

else:

    audio_html = """
    <audio
        id="birthdayAudio"
        preload="metadata"
    ></audio>
    """


# ============================================================
# COMPLETE HTML
# ============================================================

website = f"""
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width,
             initial-scale=1.0"
>

<title>
    A Little Surprise 💙
</title>


<style>

/* ============================================================
   RESET
============================================================ */

* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

html {{
    scroll-behavior: smooth;
}}

body {{

    font-family:
        "Segoe UI",
        "Trebuchet MS",
        sans-serif;

    background:
        #eafaff;

    color:
        #356579;

    overflow-x: hidden;
}}


/* ============================================================
   MAIN WEBSITE
============================================================ */

#mainWebsite {{

    display:
        none;

    width:
        100%;
}}


/* ============================================================
   LOGIN SCREEN
============================================================ */

#loginScreen {{

    width:
        100%;

    min-height:
        100vh;

    position:
        fixed;

    inset:
        0;

    z-index:
        5000;

    display:
        flex;

    justify-content:
        center;

    align-items:
        center;

    overflow:
        hidden;

    background:

        radial-gradient(
            circle at 15% 20%,
            rgba(255,255,255,.95),
            transparent 25%
        ),

        radial-gradient(
            circle at 85% 80%,
            rgba(255,255,255,.8),
            transparent 25%
        ),

        linear-gradient(
            135deg,
            #9fe3fa,
            #eafaff
        );

    transition:
        opacity .8s ease,
        transform .8s ease;
}}


/* ============================================================
   CLOUDS
============================================================ */

.cloud {{

    position:
        absolute;

    font-size:
        80px;

    opacity:
        .75;

    pointer-events:
        none;

    animation:
        cloudFloat
        6s
        ease-in-out
        infinite;
}}

.cloud1 {{
    left: 4%;
    top: 8%;
}}

.cloud2 {{
    right: 5%;
    top: 17%;
    animation-delay: 1s;
}}

.cloud3 {{
    left: 10%;
    bottom: 8%;
    animation-delay: 2s;
}}

.cloud4 {{
    right: 12%;
    bottom: 10%;
    animation-delay: 3s;
}}

@keyframes cloudFloat {{

    0%, 100% {{
        transform:
            translateX(0)
            translateY(0);
    }}

    50% {{
        transform:
            translateX(30px)
            translateY(-8px);
    }}
}}


/* ============================================================
   LOGIN CONTENT
============================================================ */

.login-content {{

    width:
        min(470px, 92%);

    text-align:
        center;

    position:
        relative;

    z-index:
        10;
}}


/* ============================================================
   PANDA
============================================================ */

.panda-box {{

    position:
        relative;

    display:
        inline-block;

    animation:
        pandaFloat
        2.5s
        ease-in-out
        infinite;
}}

.panda {{

    font-size:
        120px;

    line-height:
        1;
}}

.panda-heart-left,
.panda-heart-right {{

    position:
        absolute;

    font-size:
        35px;

    bottom:
        20px;
}}

.panda-heart-left {{
    left: 0;
    transform: rotate(-20deg);
}}

.panda-heart-right {{
    right: 0;
    transform: rotate(20deg);
}}

@keyframes pandaFloat {{

    0%, 100% {{
        transform:
            translateY(0);
    }}

    50% {{
        transform:
            translateY(-12px);
    }}
}}


/* ============================================================
   LOGIN TITLE
============================================================ */

.login-title {{

    color:
        #087ca8;

    font-size:
        clamp(
            2.5rem,
            8vw,
            4.5rem
        );

    font-weight:
        900;

    margin:
        5px 0 8px;
}}

.login-subtitle {{

    color:
        #62899a;

    font-size:
        1rem;

    margin-bottom:
        25px;
}}


/* ============================================================
   PASSWORD CARD
============================================================ */

.password-card {{

    background:
        rgba(
            255,
            255,
            255,
            .92
        );

    border:
        1px solid
        rgba(
            255,
            255,
            255,
            .95
        );

    border-radius:
        32px;

    padding:
        30px 28px;

    box-shadow:
        0 25px 70px
        rgba(
            22,
            126,
            164,
            .18
        );

    backdrop-filter:
        blur(15px);
}}

.guard-text {{

    color:
        #327b95;

    font-weight:
        800;

    margin-bottom:
        15px;
}}


/* ============================================================
   PASSWORD INPUT
============================================================ */

.password-input {{

    width:
        100%;

    border:
        2px solid
        #b6eaff;

    border-radius:
        16px;

    padding:
        16px;

    outline:
        none;

    text-align:
        center;

    font-size:
        18px;

    color:
        #20586f;

    background:
        white;

    transition:
        .25s;
}}

.password-input:focus {{

    border-color:
        #36b9e7;

    box-shadow:
        0 0 0 4px
        rgba(
            54,
            185,
            231,
            .15
        );
}}


/* ============================================================
   UNLOCK BUTTON
============================================================ */

.unlock-button {{

    width:
        100%;

    border:
        none;

    border-radius:
        16px;

    padding:
        16px;

    margin-top:
        14px;

    background:
        linear-gradient(
            135deg,
            #61cff2,
            #2da9d9
        );

    color:
        white;

    font-size:
        17px;

    font-weight:
        800;

    cursor:
        pointer;

    transition:
        .25s;
}}

.unlock-button:hover {{

    transform:
        translateY(-3px);

    box-shadow:
        0 12px 30px
        rgba(
            30,
            160,
            210,
            .3
        );
}}

.login-error {{

    min-height:
        24px;

    margin-top:
        12px;

    color:
        #dc7180;

    font-size:
        .9rem;
}}

.hint {{

    margin-top:
        10px;

    color:
        #819aa5;

    font-size:
        .84rem;
}}


/* ============================================================
   CELEBRATION
============================================================ */

#celebration {{

    position:
        fixed;

    inset:
        0;

    z-index:
        10000;

    display:
        none;

    pointer-events:
        none;

    overflow:
        hidden;

    background:
        rgba(
            94,
            202,
            237,
            .12
        );
}}

#celebration.show {{
    display:
        block;
}}


/* ============================================================
   BIRTHDAY MESSAGE
============================================================ */

.celebration-text {{

    position:
        absolute;

    top:
        30%;

    left:
        50%;

    width:
        95%;

    transform:
        translateX(-50%);

    text-align:
        center;

    z-index:
        20;
}}

.celebration-text h1 {{

    font-size:
        clamp(
            2.8rem,
            9vw,
            7rem
        );

    font-weight:
        900;

    color:
        white;

    text-shadow:
        0 8px 35px
        rgba(
            15,
            112,
            150,
            .55
        );

    animation:
        birthdayPop
        1s
        ease;
}}

.celebration-text h2 {{

    font-size:
        clamp(
            2rem,
            7vw,
            5rem
        );

    color:
        white;

    margin-top:
        8px;

    text-shadow:
        0 5px 25px
        rgba(
            15,
            112,
            150,
            .45
        );

    animation:
        birthdayPop
        1s
        .15s
        both;
}}

@keyframes birthdayPop {{

    0% {{
        opacity:
            0;

        transform:
            scale(.2);
    }}

    70% {{
        transform:
            scale(1.12);
    }}

    100% {{
        opacity:
            1;

        transform:
            scale(1);
    }}
}}


/* ============================================================
   BALLOONS
============================================================ */

.balloon {{

    position:
        absolute;

    bottom:
        -120px;

    animation:
        balloonRise
        5s
        linear
        forwards;
}}

@keyframes balloonRise {{

    0% {{
        transform:
            translateY(0)
            rotate(-8deg);

        opacity:
            1;
    }}

    100% {{
        transform:
            translateY(-125vh)
            rotate(10deg);

        opacity:
            0;
    }}
}}


/* ============================================================
   CONFETTI
============================================================ */

.confetti {{

    position:
        absolute;

    top:
        -30px;

    width:
        8px;

    height:
        18px;

    animation:
        confettiFall
        3.5s
        linear
        forwards;
}}

@keyframes confettiFall {{

    0% {{
        transform:
            translateY(0)
            rotate(0);
    }}

    100% {{
        transform:
            translateY(120vh)
            rotate(720deg);
    }}
}}


/* ============================================================
   FLYING HEARTS
============================================================ */

.flying-heart {{

    position:
        absolute;

    bottom:
        -70px;

    color:
        #48c4ed;

    animation:
        heartRise
        5s
        ease-out
        forwards;
}}

@keyframes heartRise {{

    0% {{
        opacity:
            0;

        transform:
            translateY(0)
            scale(.4);
    }}

    15% {{
        opacity:
            1;
    }}

    100% {{
        opacity:
            0;

        transform:
            translateY(-120vh)
            scale(1.3);
    }}
}}


/* ============================================================
   COMMON SECTION
============================================================ */

.section {{

    width:
        100%;

    min-height:
        850px;

    padding:
        90px 7%;

    display:
        flex;

    align-items:
        center;

    justify-content:
        center;

    position:
        relative;
}}


.section-inner {{

    width:
        min(
            1100px,
            100%
        );

    margin:
        auto;
}}


/* ============================================================
   HOME
============================================================ */

#home {{

    min-height:
        850px;

    text-align:
        center;

    background:
        linear-gradient(
            180deg,
            #d4f5ff,
            #f9fdff
        );
}}

.home-label {{

    color:
        #36a9d2;

    font-size:
        .85rem;

    font-weight:
        900;

    letter-spacing:
        3px;
}}

.home-title {{

    color:
        #087da9;

    font-size:
        clamp(
            3rem,
            8vw,
            6.5rem
        );

    font-weight:
        900;

    margin:
        18px 0 5px;
}}

.home-name {{

    color:
        #4fc0e8;

    font-size:
        clamp(
            2.2rem,
            6vw,
            4.5rem
        );

    font-weight:
        900;
}}

.home-text {{

    max-width:
        720px;

    margin:
        30px auto;

    color:
        #668a99;

    line-height:
        2;

    font-size:
        1.08rem;
}}

.scroll-hint {{

    color:
        #36acd5;

    margin-top:
        55px;

    font-weight:
        700;

    animation:
        scrollBounce
        2s
        infinite;
}}

@keyframes scrollBounce {{

    0%,100% {{
        transform:
            translateY(0);
    }}

    50% {{
        transform:
            translateY(10px);
    }}
}}


/* ============================================================
   SECTION TITLE
============================================================ */

.section-title {{

    text-align:
        center;

    color:
        #087da9;

    font-size:
        clamp(
            2.3rem,
            6vw,
            4rem
        );

    font-weight:
        900;

    margin-bottom:
        10px;
}}

.section-subtitle {{

    text-align:
        center;

    color:
        #7594a1;

    margin-bottom:
        45px;
}}


/* ============================================================
   MEMORIES
============================================================ */

#memories {{

    min-height:
        850px;

    background:
        #f4fcff;
}}

.memory-grid {{

    display:
        grid;

    grid-template-columns:
        repeat(
            3,
            minmax(
                0,
                1fr
            )
        );

    gap:
        28px;
}}

.memory-card {{

    position:
        relative;

    background:
        white;

    padding:
        10px 10px 18px;

    border-radius:
        14px;

    box-shadow:
        0 18px 45px
        rgba(
            32,
            138,
            174,
            .13
        );

    transition:
        .35s;

    transform:
        rotate(-1deg);
}}

.memory-card:nth-child(even) {{
    transform:
        rotate(1deg);
}}

.memory-card:hover {{

    transform:
        translateY(-10px)
        rotate(0deg);

    box-shadow:
        0 25px 55px
        rgba(
            32,
            138,
            174,
            .2
        );
}}

.memory-card img {{

    width:
        100%;

    aspect-ratio:
        1 / 1;

    object-fit:
        cover;

    border-radius:
        9px;

    display:
        block;
}}

.memory-number {{

    position:
        absolute;

    top:
        20px;

    left:
        20px;

    padding:
        5px 10px;

    border-radius:
        20px;

    background:
        rgba(
            255,
            255,
            255,
            .9
        );

    color:
        #228caf;

    font-size:
        12px;

    font-weight:
        900;
}}

.memory-caption {{

    text-align:
        center;

    color:
        #557b8c;

    margin-top:
        13px;

    font-weight:
        700;
}}

.empty-memory {{

    grid-column:
        1 / -1;

    text-align:
        center;

    padding:
        80px;

    color:
        #71909d;
}}

.empty-icon {{
    font-size:
        70px;

    margin-bottom:
        20px;
}}


/* ============================================================
   GLASS CARD
============================================================ */

.glass-card {{

    background:
        rgba(
            255,
            255,
            255,
            .75
        );

    border:
        1px solid
        white;

    border-radius:
        30px;

    padding:
        40px;

    box-shadow:
        0 20px 55px
        rgba(
            38,
            145,
            181,
            .12
        );

    backdrop-filter:
        blur(15px);
}}


/* ============================================================
   SONG
============================================================ */

#song {{

    min-height:
        850px;

    background:
        linear-gradient(
            180deg,
            #e5faff,
            #ffffff
        );
}}

.song-card {{

    max-width:
        700px;

    margin:
        auto;

    text-align:
        center;
}}

.music-icon {{

    font-size:
        75px;

    animation:
        musicFloat
        2s
        ease-in-out
        infinite;
}}

@keyframes musicFloat {{

    0%,100% {{
        transform:
            translateY(0);
    }}

    50% {{
        transform:
            translateY(-10px);
    }}
}}

.song-title {{

    color:
        #087da9;

    font-size:
        2rem;

    font-weight:
        900;

    margin:
        15px 0;
}}


/* ============================================================
   MUSIC WAVE
============================================================ */

.wave {{

    height:
        55px;

    display:
        flex;

    align-items:
        center;

    justify-content:
        center;

    gap:
        6px;

    margin:
        15px;
}}

.wave span {{

    width:
        5px;

    height:
        10px;

    border-radius:
        10px;

    background:
        #52c7eb;
}}

.wave.playing span {{

    animation:
        musicWave
        .7s
        ease-in-out
        infinite
        alternate;
}}

.wave span:nth-child(1) {{
    animation-delay:
        .05s;
}}

.wave span:nth-child(2) {{
    animation-delay:
        .15s;
}}

.wave span:nth-child(3) {{
    animation-delay:
        .25s;
}}

.wave span:nth-child(4) {{
    animation-delay:
        .35s;
}}

.wave span:nth-child(5) {{
    animation-delay:
        .25s;
}}

.wave span:nth-child(6) {{
    animation-delay:
        .15s;
}}

.wave span:nth-child(7) {{
    animation-delay:
        .05s;
}}

@keyframes musicWave {{

    from {{
        height:
            10px;
    }}

    to {{
        height:
            42px;
    }}
}}


/* ============================================================
   SONG BUTTON
============================================================ */

.song-button {{

    border:
        none;

    border-radius:
        50px;

    padding:
        16px 40px;

    background:
        linear-gradient(
            135deg,
            #5dcef1,
            #2baadc
        );

    color:
        white;

    font-size:
        17px;

    font-weight:
        900;

    cursor:
        pointer;

    transition:
        .25s;
}}

.song-button:hover {{

    transform:
        translateY(-3px);

    box-shadow:
        0 12px 30px
        rgba(
            45,
            174,
            222,
            .3
        );
}}

.song-status {{

    color:
        #7895a3;

    margin-top:
        20px;
}}


/* ============================================================
   MESSAGE
============================================================ */

#message {{

    min-height:
        750px;

    background:
        #f7fcff;
}}

.message-card {{

    max-width:
        800px;

    margin:
        auto;

    text-align:
        center;
}}

.reveal-button {{

    border:
        2px solid
        #55c5eb;

    border-radius:
        50px;

    padding:
        15px 32px;

    background:
        transparent;

    color:
        #258eaf;

    font-size:
        17px;

    font-weight:
        800;

    cursor:
        pointer;

    transition:
        .25s;
}}

.reveal-button:hover {{

    background:
        #e1f8ff;

    transform:
        translateY(-3px);
}}

.hidden-message {{

    display:
        none;

    margin-top:
        30px;

    padding:
        30px;

    border-radius:
        25px;

    background:
        #e2f8ff;

    color:
        #5e7e8c;

    line-height:
        1.9;
}}

.hidden-message.show {{

    display:
        block;

    animation:
        messageReveal
        .8s
        ease;
}}

@keyframes messageReveal {{

    from {{
        opacity:
            0;

        transform:
            translateY(25px);
    }}

    to {{
        opacity:
            1;

        transform:
            translateY(0);
    }}
}}


/* ============================================================
   ABOUT HER
============================================================ */

#about {{

    min-height:
        850px;

    background:
        linear-gradient(
            180deg,
            #ddf7ff,
            #ffffff
        );
}}

.about-card {{

    max-width:
        900px;

    margin:
        auto;

    text-align:
        center;
}}

.about-text {{

    color:
        #5c7e8e;

    font-size:
        1.1rem;

    line-height:
        2;

    white-space:
        pre-line;
}}


/* ============================================================
   FINAL
============================================================ */

#final {{

    min-height:
        700px;

    text-align:
        center;

    background:
        radial-gradient(
            circle,
            #d5f6ff,
            white
        );
}}

.final-heart {{

    font-size:
        80px;

    animation:
        finalHeart
        1.5s
        infinite;
}}

@keyframes finalHeart {{

    0%,100% {{
        transform:
            scale(1);
    }}

    50% {{
        transform:
            scale(1.2);
    }}
}}

.final-title {{

    color:
        #087da9;

    font-size:
        clamp(
            2.8rem,
            7vw,
            5.5rem
        );

    font-weight:
        900;
}}

.final-name {{

    color:
        #50bfe7;

    font-size:
        clamp(
            2rem,
            6vw,
            4rem
        );

    font-weight:
        900;

    margin:
        10px;
}}


/* ============================================================
   TOUCH HEART
============================================================ */

.touch-heart {{

    position:
        fixed;

    pointer-events:
        none;

    z-index:
        999999;

    font-size:
        28px;

    animation:
        touchHeart
        1.2s
        ease-out
        forwards;
}}

@keyframes touchHeart {{

    0% {{

        opacity:
            1;

        transform:
            translate(
                -50%,
                -50%
            )
            scale(.5);
    }}

    100% {{

        opacity:
            0;

        transform:
            translate(
                -50%,
                -160px
            )
            scale(1.35);
    }}
}}


/* ============================================================
   MOBILE
============================================================ */

@media(max-width: 700px) {{

    .section {{

        min-height:
            760px;

        padding:
            70px 5%;
    }}

    #home,
    #memories,
    #song,
    #about {{

        min-height:
            760px;
    }}

    .panda {{
        font-size:
            90px;
    }}

    .password-card {{
        padding:
            25px 18px;
    }}

    .glass-card {{
        padding:
            25px 18px;
    }}

    .memory-grid {{

        grid-template-columns:
            repeat(
                2,
                minmax(
                    0,
                    1fr
                )
            );

        gap:
            14px;
    }}

    .memory-card {{
        padding:
            7px 7px 14px;
    }}

    .memory-caption {{
        font-size:
            .8rem;
    }}

    .cloud {{
        font-size:
            50px;
    }}

}}


/* ============================================================
   VERY SMALL MOBILE
============================================================ */

@media(max-width: 420px) {{

    .memory-grid {{

        grid-template-columns:
            1fr;
    }}

}}

</style>

</head>


<body>


<!-- ==========================================================
     LOGIN
========================================================== -->

<section id="loginScreen">


    <div class="cloud cloud1">
        ☁️
    </div>

    <div class="cloud cloud2">
        ☁️
    </div>

    <div class="cloud cloud3">
        ☁️
    </div>

    <div class="cloud cloud4">
        ☁️
    </div>


    <div class="login-content">


        <div class="panda-box">

            <div class="panda">
                🐼
            </div>

            <div class="panda-heart-left">
                💙
            </div>

            <div class="panda-heart-right">
                💙
            </div>

        </div>


        <h1 class="login-title">
            A Little Surprise
        </h1>


        <p class="login-subtitle">
            A secret little place made especially for you 💙
        </p>


        <div class="password-card">


            <div class="guard-text">
                🐼 Panda is guarding your birthday secret!
            </div>


            <form id="loginForm">


                <input
                    id="passwordInput"
                    class="password-input"
                    type="password"
                    inputmode="numeric"
                    maxlength="8"
                    placeholder="Enter your birthday"
                    autocomplete="off"
                >


                <button
                    class="unlock-button"
                    type="submit"
                >
                    Unlock Your Surprise 💙
                </button>


            </form>


            <div
                id="loginError"
                class="login-error"
            ></div>


            <div class="hint">
                🎂 Hint: It's your special birthday💙
            </div>


        </div>


    </div>

</section>


<!-- ==========================================================
     CELEBRATION
========================================================== -->

<div id="celebration">

    <div class="celebration-text">

        <h1>
            HAPPY BIRTHDAY
        </h1>

        <h2>
            {safe_name} 💙
        </h2>

    </div>

</div>


<!-- ==========================================================
     MAIN WEBSITE
========================================================== -->

<div id="mainWebsite">


    <!-- ======================================================
         HOME
    ======================================================= -->

    <section
        id="home"
        class="section"
    >

        <div class="section-inner">


            <div class="home-label">
                ✨ TODAY IS YOUR SPECIAL DAY RO ✨
            </div>


            <h1 class="home-title">
                Happy Birthday
            </h1>


            <div class="home-name">
                {safe_name} 💙
            </div>


            <p class="home-text">

                Today is all about celebrating you.

                <br><br>

                This little website is filled with
                memories, music, messages and a lot
                of love.

                <br><br>

                Take your time.

                <br>

                Scroll slowly...

                <br><br>

                There is something waiting for you
                at every step. ☁️💙

            </p>


            <div class="scroll-hint">
                ↓ Scroll down to discover your surprise 💙
            </div>


        </div>

    </section>


    <!-- ======================================================
         MEMORIES
    ======================================================= -->

    <section
        id="memories"
        class="section"
    >

        <div class="section-inner">


            <h2 class="section-title">
                📸 Memories✨
            </h2>


            <p class="section-subtitle">
                Little moments that became beautiful memories. 💙
            </p>


            <div class="memory-grid">

                {memory_html}

            </div>


        </div>

    </section>


    <!-- ======================================================
         SONG
    ======================================================= -->

    <section
        id="song"
        class="section"
    >

        <div class="section-inner">


            <h2 class="section-title">
                🎵 A Song For You Macha😁
            </h2>


            <p class="section-subtitle">
                No background music. You decide when it plays. 💙
            </p>


            <div class="song-card glass-card">


                <div class="music-icon">
                    🎵
                </div>


                <div class="song-title">
                    {safe_song_title}
                </div>


                <div
                    id="wave"
                    class="wave"
                >

                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>

                </div>


                <button
                    id="songButton"
                    class="song-button"
                    type="button"
                >
                    ▶ Play Song
                </button>


                {audio_html}


                <div
                    id="songStatus"
                    class="song-status"
                >
                    Tap the button to play your song 🎵
                </div>


            </div>


        </div>

    </section>


    <!-- ======================================================
         MESSAGE
    ======================================================= -->

    <section
        id="message"
        class="section"
    >

        <div class="section-inner">


            <h2 class="section-title">
                💌 A Little Message
            </h2>


            <p class="section-subtitle">
                Panda has one more secret for you...
            </p>


            <div class="message-card glass-card">


                <button
                    id="revealButton"
                    class="reveal-button"
                    type="button"
                >
                    💙 Tap To Reveal
                </button>


                <div
                    id="hiddenMessage"
                    class="hidden-message"
                >

                    Machaa athavathu ennavenrall 🖋️ ni🐼 ennaku life la kedachaa oru unexpected gift 🩵 it about pokkisum💎🫂 ennaa life 🧬 mean 20 yrs  laa ennaa nambunaa 1st madam ji 🤞ni thaa 🫂🙏athu evlo spr laa 😊 aprmm evlo trust uh, aprm na evlo unna hurt pannalum trust ah break pannalum ni enna mannuchi vtaa laa that's you machaaa 🥹🙏,aprm evlo pasaamm 🤭 (rare) ennaayum oru all ah mathuchi pesurulaa athu evlo special ✨ theriyumm ahh,unnaa neraya tym miss panniruvom nu bayanthuku iruken till now 😵‍💫🙃 appaa paathukoo ni ennaku evlo important ♾️🫀 nu  yarum avlooo seekiram nambaa maatangaa laa but ni apdi illa machaaa 🫂🩵🥹😘 aprm ni ennaku oru kollantha maarii 👼 ithu cringe ah koodaa irukatumm but athu tha unmaaa 😄 aprm ellam solluvangaa laa life laa oru vaati kedaikum thollaachirathaa nu ,that u for me daa loosu paiyaa 🫂🩵😘 aprmmm intha ennaku ups down la irunthu evlo help panniruka laaaa u great daa deii 🙏😙 so ni ennaku 💎👼🫀 
                     -by Anbu tholann GP🩵


                    <br><br>

                    Thank you for every laugh,
                    every conversation, every silly
                    moment and every beautiful memory.

                    <br><br>

                    I hope we continue creating
                    many more memories together.

                    <br><br>

                    You & Me — Forever Friends ♾️💙

                </div>


            </div>


        </div>

    </section>


    <!-- ======================================================
         DESCRIPTION
    ======================================================= -->

    <section
        id="about"
        class="section"
    >

        <div class="section-inner">


            <h2 class="section-title">
                💙 Special About You 💫
            </h2>


            <p class="section-subtitle">
                A few words written especially for you.
            </p>


            <div class="about-card glass-card">


                <div
                    style="
                        font-size:50px;
                        margin-bottom:25px;
                    "
                >
                    ☁️ 💙 ♾️ 💙 ☁️
                </div>


                <p class="about-text">
                    {safe_description}
                </p>


                <div
                    style="
                        font-size:50px;
                        margin-top:25px;
                    "
                >
                    💙 ✨ 💙
                </div>


            </div>


        </div>

    </section>


    <!-- ======================================================
         FINAL
    ======================================================= -->

    <section
        id="final"
        class="section"
    >

        <div class="section-inner">


            <div class="final-heart">
                💙
            </div>


            <h1 class="final-title">
                Happy Birthday
            </h1>


            <div class="final-name">
                {safe_name}
            </div>


            <p
                style="
                    max-width:650px;
                    margin:30px auto;
                    color:#638696;
                    font-size:1.1rem;
                    line-height:1.9;
                "
            >

                Keep smiling.

                <br>

                Keep being yourself.

                <br>

                Keep making beautiful memories.

                <br>

                And never forget how special you are.

                💙

            </p>


            <div
                style="
                    margin-top:50px;
                    color:#7197a7;
                    font-weight:700;
                "
            >

                Made with 💙 specially for you

                <br><br>

                Love you Macha🎀😘

                ❤️‍🩹Friends 🫂 Forever ♾️

                <br><br>
                ~By Anbu tholann GP🩵

            </div>


        </div>

    </section>


</div>


<!-- ==========================================================
     JAVASCRIPT
========================================================== -->

<script>


/* ============================================================
   PASSWORD
============================================================ */

const PASSWORD =
    "{BIRTHDAY_PASSWORD}";


/* ============================================================
   ELEMENTS
============================================================ */

const loginForm =
    document.getElementById(
        "loginForm"
    );

const passwordInput =
    document.getElementById(
        "passwordInput"
    );

const loginError =
    document.getElementById(
        "loginError"
    );

const loginScreen =
    document.getElementById(
        "loginScreen"
    );

const celebration =
    document.getElementById(
        "celebration"
    );

const mainWebsite =
    document.getElementById(
        "mainWebsite"
    );


/* ============================================================
   LOGIN
============================================================ */

loginForm.addEventListener(
    "submit",
    function(event) {{

        event.preventDefault();


        const enteredPassword =
            passwordInput.value.trim();


        if (!enteredPassword) {{

            loginError.textContent =
                "Please enter your birthday 💙";

            return;

        }}


        if (
            enteredPassword === PASSWORD
        ) {{

            loginError.textContent =
                "";

            startBirthday();

        }}
        else {{

            loginError.textContent =
                "Panda says that's not the secret! 🐼💙";

            passwordInput.value =
                "";

            passwordInput.focus();

        }}

    }}
);


/* ============================================================
   BIRTHDAY START
============================================================ */

function startBirthday() {{

    celebration.classList.add(
        "show"
    );


    createConfetti();

    createBalloons();

    createHearts();


    loginScreen.style.opacity =
        "0";

    loginScreen.style.transform =
        "scale(1.08)";


    setTimeout(
        function() {{

            loginScreen.style.display =
                "none";


            mainWebsite.style.display =
                "block";


            window.scrollTo(
                0,
                0
            );

        }},
        850
    );


    setTimeout(
        function() {{

            celebration.classList.remove(
                "show"
            );

        }},
        5200
    );

}}


/* ============================================================
   CONFETTI
============================================================ */

function createConfetti() {{

    const symbols = [
        "✦",
        "✧",
        "★",
        "◆",
        "•"
    ];


    for (
        let i = 0;
        i < 130;
        i++
    ) {{

        const piece =
            document.createElement(
                "div"
            );


        piece.className =
            "confetti";


        piece.textContent =
            symbols[
                Math.floor(
                    Math.random()
                    * symbols.length
                )
            ];


        piece.style.left =
            Math.random() * 100 +
            "%";


        piece.style.color =
            [
                "#42bde8",
                "#68d1ef",
                "#9de7f7",
                "#ffffff",
                "#229ac8"
            ][
                Math.floor(
                    Math.random() * 5
                )
            ];


        piece.style.animationDelay =
            Math.random() * 1.2 +
            "s";


        piece.style.fontSize =
            (
                10 +
                Math.random() * 14
            ) +
            "px";


        celebration.appendChild(
            piece
        );


        setTimeout(
            function() {{
                piece.remove();
            }},
            5000
        );

    }}

}}


/* ============================================================
   BALLOONS
============================================================ */

function createBalloons() {{

    for (
        let i = 0;
        i < 16;
        i++
    ) {{

        const balloon =
            document.createElement(
                "div"
            );


        balloon.className =
            "balloon";


        balloon.textContent =
            "🎈";


        balloon.style.left =
            (
                Math.random() * 100
            ) +
            "%";


        balloon.style.fontSize =
            (
                40 +
                Math.random() * 45
            ) +
            "px";


        balloon.style.animationDelay =
            (
                Math.random() * 1.5
            ) +
            "s";


        celebration.appendChild(
            balloon
        );


        setTimeout(
            function() {{
                balloon.remove();
            }},
            6500
        );

    }}

}}


/* ============================================================
   FLYING HEARTS
============================================================ */

function createHearts() {{

    for (
        let i = 0;
        i < 40;
        i++
    ) {{

        const heart =
            document.createElement(
                "div"
            );


        heart.className =
            "flying-heart";


        heart.textContent =
            "💙";


        heart.style.left =
            (
                Math.random() * 100
            ) +
            "%";


        heart.style.fontSize =
            (
                18 +
                Math.random() * 30
            ) +
            "px";


        heart.style.animationDelay =
            (
                Math.random() * 2
            ) +
            "s";


        celebration.appendChild(
            heart
        );


        setTimeout(
            function() {{
                heart.remove();
            }},
            6500
        );

    }}

}}


/* ============================================================
   TOUCH HEART
============================================================ */

document.addEventListener(
    "pointerdown",
    function(event) {{

        if (
            event.target.closest(
                "button"
            )
            ||
            event.target.closest(
                "input"
            )
        ) {{
            return;
        }}


        const heart =
            document.createElement(
                "div"
            );


        heart.className =
            "touch-heart";


        heart.textContent =
            "💙";


        heart.style.left =
            event.clientX +
            "px";


        heart.style.top =
            event.clientY +
            "px";


        document.body.appendChild(
            heart
        );


        setTimeout(
            function() {{
                heart.remove();
            }},
            1200
        );

    }}
);


/* ============================================================
   SONG PLAYER
============================================================ */

const audio =
    document.getElementById(
        "birthdayAudio"
    );

const songButton =
    document.getElementById(
        "songButton"
    );

const songStatus =
    document.getElementById(
        "songStatus"
    );

const wave =
    document.getElementById(
        "wave"
    );


songButton.addEventListener(
    "click",
    function() {{

        if (
            !audio
            ||
            (
                !audio.src
                &&
                !audio.querySelector(
                    "source"
                )
            )
        ) {{

            songStatus.textContent =
                "Song not found in assets 🎵";

            return;

        }}


        if (audio.paused) {{

            audio.play()
                .then(
                    function() {{

                        songButton.textContent =
                            "⏸ Pause Song";

                        wave.classList.add(
                            "playing"
                        );

                        songStatus.textContent =
                            "Now playing: {safe_song_title} 💙";

                    }}
                )
                .catch(
                    function() {{

                        songStatus.textContent =
                            "Please tap Play Song again 🎵";

                    }}
                );

        }}
        else {{

            audio.pause();


            songButton.textContent =
                "▶ Play Song";


            wave.classList.remove(
                "playing"
            );


            songStatus.textContent =
                "Song paused 💙";

        }}

    }}
);


audio.addEventListener(
    "ended",
    function() {{

        songButton.textContent =
            "▶ Play Song";


        wave.classList.remove(
            "playing"
        );


        songStatus.textContent =
            "Song finished 💙";

    }}
);


/* ============================================================
   REVEAL MESSAGE
============================================================ */

const revealButton =
    document.getElementById(
        "revealButton"
    );

const hiddenMessage =
    document.getElementById(
        "hiddenMessage"
    );


revealButton.addEventListener(
    "click",
    function() {{

        hiddenMessage.classList.toggle(
            "show"
        );


        if (
            hiddenMessage.classList.contains(
                "show"
            )
        ) {{

            revealButton.textContent =
                "💙 Message Revealed";

        }}
        else {{

            revealButton.textContent =
                "💙 Tap To Reveal";

        }}

    }}
);

</script>


</body>

</html>
"""


# ============================================================
# RENDER WEBSITE
# ============================================================

# Large enough for all sections.
# The browser will scroll through the complete experience.

components.html(
    website,
    height=6000,
    scrolling=True
)