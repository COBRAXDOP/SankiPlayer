import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "LOVExWORD")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/85https://telegra.ph/file/6a5d2596ceff155f74a0d.jpg")
admins = 
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "👑⃝🕊️⃝❂͜͡мя• яαмαи⍣⃟❂͜͡࿐ || αѕѕιѕтαит ||")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "LOVExWORD")
PROJECT_NAME = getenv("PROJECT_NAME", "SankiPlayer")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/mrnitric/SankiPlayer")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
