import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 24753274
API_HASH = "625668050f7e193a994e2f5ddc4aafe5"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7743484569:AAG1ZogTHH3ZbLAgaRicEZ35JW2b3n1pu_Q"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://gxinfinity742:gxinfinity742@cluster0.4crk9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002385742084

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 7135072912

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/gxinfinity_support"
SUPPORT_GROUP = "https://t.me/infinitygx_bot_support"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "STRING_SESSION"
STRING2 = getenv("STRING_SESSION2", BQF5tHoAxQsgmZVJjuTBN8cvp2eMk3X8RX2RJn5IuKxBB0BT8KNN7A7YGUKAzByFMlCtfz9DFu1Kk_6bQFdMbS_ev_Iq0BDTPOHrfGJejhzdr0dpm97a-NhkPktS0ifTx7vmozUfEQmcNNIAwdhpbNexb0ZnmuG0LZy7NBg3_21juYHtKgMSLy3l4q3szV2lAyRlBR0sqJlFRr7RFDFy5kNb7hnPKQqFDmf-HmutiQW5dmEowa2hA_Fu-GYeR5Ezkx3H72yZKD_uqmQE-nHgQR1eyj5gzZrJYOa_gd5IFp8EPk5PoweOR8OCrK7vLHaU7pJtmbXY3WLX-QDnEyjl8SUZuREv8AAAAAGpSJKQAA)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/b644be14d2e7560dcfc42-90b7349d2f5692e885.jpg"

PING_IMG_URL = "https://graph.org/file/6900af1a59c35ac504327-92b43578532cf5a9d0.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/b644be14d2e7560dcfc42-90b7349d2f5692e885.jpg"
STATS_IMG_URL = "https://graph.org/file/b644be14d2e7560dcfc42-90b7349d2f5692e885.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/b644be14d2e7560dcfc42-90b7349d2f5692e885.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/b644be14d2e7560dcfc42-90b7349d2f5692e885.jpg"
STREAM_IMG_URL = "https://graph.org/file/b644be14d2e7560dcfc42-90b7349d2f5692e885.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/b644be14d2e7560dcfc42-90b7349d2f5692e885.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/b644be14d2e7560dcfc42-90b7349d2f5692e885.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/b644be14d2e7560dcfc42-90b7349d2f5692e885.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/b644be14d2e7560dcfc42-90b7349d2f5692e885.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/b644be14d2e7560dcfc42-90b7349d2f5692e885.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
