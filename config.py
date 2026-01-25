from os import getenv
from dotenv import load_dotenv

load_dotenv()

# ═══════════════════════════════════════════════════════════
# إعدادات بوت الموسيقى العربي
# المطور: @idseno | القناة: @senovip
# © 2026 - جميع الحقوق محفوظة
# ═══════════════════════════════════════════════════════════

class Config:
    def __init__(self):
        # ═══════════════════════════════════════
        # المتغيرات الأساسية (مطلوبة)
        # ═══════════════════════════════════════
        
        self.API_ID = int(getenv("API_ID", 0))
        self.API_HASH = getenv("API_HASH")
        self.BOT_TOKEN = getenv("BOT_TOKEN")
        
        # قاعدة البيانات
        self.MONGO_URL = getenv("MONGO_URL") or getenv("MONGO_DB_URI")
        
        # معرف مجموعة السجلات
        self.LOGGER_ID = int(getenv("LOGGER_ID", getenv("LOG_GROUP_ID", 0)))
        
        # معرف المالك
        self.OWNER_ID = int(getenv("OWNER_ID", 0))
        
        # ═══════════════════════════════════════
        # الجلسات (Sessions)
        # ═══════════════════════════════════════
        
        self.SESSION1 = getenv("SESSION", None) or getenv("STRING_SESSION", None)
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)
        
        # ═══════════════════════════════════════
        # معلومات المطور والدعم
        # ═══════════════════════════════════════
        
        self.OWNER = getenv("OWNER", "idseno")
        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "senovip")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "Sourceseno") or getenv("SUPPORT_GROUP", "Sourceseno")
        
        # ═══════════════════════════════════════
        # الحدود والقيود
        # ═══════════════════════════════════════
        
        # مدة التشغيل (بالدقائق - يتم تحويلها لثواني)
        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 999)) * 60
        
        # حد قائمة الانتظار
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        
        # حد قوائم التشغيل
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))
        
        # ═══════════════════════════════════════
        # الإعدادات التلقائية
        # ═══════════════════════════════════════
        
        # إنهاء تلقائي عند انتهاء القائمة
        self.AUTO_END = self._parse_bool(getenv("AUTO_END", "False"))
        
        # مغادرة تلقائية بعد الانتهاء
        self.AUTO_LEAVE = self._parse_bool(getenv("AUTO_LEAVE", "False"))
        
        # تفعيل تشغيل الفيديو
        self.VIDEO_PLAY = self._parse_bool(getenv("VIDEO_PLAY", "True"))
        
        # ═══════════════════════════════════════
        # الكوكيز (للتحميل من YouTube)
        # ═══════════════════════════════════════
        
        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        
        # ═══════════════════════════════════════
        # الصور والثيمات
        # ═══════════════════════════════════════
        
        # صورة افتراضية للأغاني
        self.DEFAULT_THUMB = getenv(
            "DEFAULT_THUMB", 
            "https://telegra.ph/file/c0e014ff34f34d1c4c0b5.jpg"
        )
        
        # صورة أمر Ping
        self.PING_IMG = getenv(
            "PING_IMG", 
            "https://telegra.ph/file/c0e014ff34f34d1c4c0b5.jpg"
        )
        
        # صورة رسالة البداية
        self.START_IMG = getenv(
            "START_IMG", 
            "https://telegra.ph/file/c0e014ff34f34d1c4c0b5.jpg"
        )
        
        # ═══════════════════════════════════════
        # اللغة
        # ═══════════════════════════════════════
        
        self.LANGUAGE = getenv("LANGUAGE", "ar")
    
    def _parse_bool(self, value):
        """تحويل النص إلى Boolean"""
        if isinstance(value, bool):
            return value
        return str(value).lower() in ("true", "1", "yes", "نعم")
    
    def check(self):
        """التحقق من المتغيرات المطلوبة"""
        
        required_vars = {
            "API_ID": self.API_ID,
            "API_HASH": self.API_HASH,
            "BOT_TOKEN": self.BOT_TOKEN,
            "MONGO_URL": self.MONGO_URL,
            "LOGGER_ID": self.LOGGER_ID,
            "OWNER_ID": self.OWNER_ID,
            "SESSION1": self.SESSION1
        }
        
        missing = [
            var_name
            for var_name, var_value in required_vars.items()
            if not var_value or var_value == 0
        ]
        
        if missing:
            print("\n" + "="*50)
            print("❌ خطأ: المتغيرات التالية مفقودة!")
            print("="*50)
            for var in missing:
                print(f"  • {var}")
            print("="*50)
            print("📝 يرجى إضافة هذه المتغيرات في ملف .env أو في Koyeb")
            print("="*50 + "\n")
            raise SystemExit(f"❌ المتغيرات المفقودة: {', '.join(missing)}")
        
        print("\n" + "="*50)
        print("✅ جميع المتغيرات المطلوبة موجودة!")
        print("="*50)
        print(f"🤖 البوت: {self.BOT_TOKEN[:20]}...")
        print(f"👨‍💻 المطور: @{self.OWNER}")
        print(f"📢 القناة: @{self.SUPPORT_CHANNEL}")
        print(f"💬 المجموعة: @{self.SUPPORT_CHAT}")
        print(f"🌐 اللغة: {self.LANGUAGE}")
        print("="*50 + "\n")


# ═══════════════════════════════════════════════════════════
# تصدير المتغيرات للاستخدام المباشر (للتوافق)
# ═══════════════════════════════════════════════════════════

config = Config()

# المتغيرات الأساسية
API_ID = config.API_ID
API_HASH = config.API_HASH
BOT_TOKEN = config.BOT_TOKEN
MONGO_URL = config.MONGO_URL
MONGO_DB_URI = config.MONGO_URL  # للتوافق
LOGGER_ID = config.LOGGER_ID
LOG_GROUP_ID = config.LOGGER_ID  # للتوافق
OWNER_ID = config.OWNER_ID

# الجلسات
SESSION1 = config.SESSION1
STRING_SESSION = config.SESSION1  # للتوافق
SESSION2 = config.SESSION2
SESSION3 = config.SESSION3

# الدعم
OWNER = config.OWNER
SUPPORT_CHANNEL = config.SUPPORT_CHANNEL
SUPPORT_CHAT = config.SUPPORT_CHAT
SUPPORT_GROUP = config.SUPPORT_CHAT  # للتوافق

# الإعدادات
DURATION_LIMIT = config.DURATION_LIMIT
QUEUE_LIMIT = config.QUEUE_LIMIT
PLAYLIST_LIMIT = config.PLAYLIST_LIMIT
AUTO_END = config.AUTO_END
AUTO_LEAVE = config.AUTO_LEAVE
VIDEO_PLAY = config.VIDEO_PLAY
LANGUAGE = config.LANGUAGE

# الصور
DEFAULT_THUMB = config.DEFAULT_THUMB
PING_IMG = config.PING_IMG
START_IMG = config.START_IMG

# الكوكيز
COOKIES_URL = config.COOKIES_URL
AUDIO_QUALITY = "128k" 
