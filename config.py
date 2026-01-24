import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

# معلومات المطور (غيّرها لمعلوماتك)
OWNER = getenv("OWNER", "idseno")  # معرفك بدون @
OWNER_ID = int(getenv("OWNER_ID", "641799099"))  # معرفك الرقمي

# الدعم
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "senovip")  # قناتك بدون @
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Sourceseno")  # مجموعتك بدون @

# معلومات البوت
BOT_NAME = getenv("BOT_NAME", "سورس ميوزك سينو")
BOT_USERNAME = getenv("BOT_USERNAME", "SenoMusicbot")  # بدون @

# باقي الإعدادات...
API_ID = int(getenv("API_ID", "0"))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
STRING_SESSION = getenv("STRING_SESSION", "")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "0"))

# اللغة الافتراضية
LANGUAGE = getenv("LANGUAGE", "ar")

class Config:
    def __init__(self):
        self.API_ID = API_ID
        self.API_HASH = API_HASH
        self.BOT_TOKEN = BOT_TOKEN
        self.MONGO_DB_URI = MONGO_DB_URI
        self.STRING_SESSION = STRING_SESSION
        self.OWNER_ID = OWNER_ID
        self.LOG_GROUP_ID = LOG_GROUP_ID
        
    def check(self):
        """التحقق من المتغيرات المطلوبة"""
        if not self.API_ID:
            raise ValueError("API_ID مطلوب!")
        if not self.API_HASH:
            raise ValueError("API_HASH مطلوب!")
        if not self.BOT_TOKEN:
            raise ValueError("BOT_TOKEN مطلوب!")
        if not self.MONGO_DB_URI:
            raise ValueError("MONGO_DB_URI مطلوب!")
        if not self.STRING_SESSION:
            raise ValueError("STRING_SESSION مطلوب!")
        if not self.OWNER_ID:
            raise ValueError("OWNER_ID مطلوب!")
