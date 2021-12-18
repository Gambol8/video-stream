import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "G8_M_L")
ALIVE_NAME = getenv("ALIVE_NAME", "Gambol")
BOT_USERNAME = getenv("BOT_USERNAME", "DJ4bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "D_J_H4")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "MatrixSupport_Official")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "G8_01"乡'")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES","").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/da0213215ffeba1eb3602.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/gambol8/video-stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
