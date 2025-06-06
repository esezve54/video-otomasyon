import os

class Config:
    # ── Admin Paneli Giriş Bilgisi ─────────────────────────
    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "sifre123")  # Deploy’da güçlü bir şifre girin

    # ── Sora API Ayarları ────────────────────────────────────
    SORA_API_ENDPOINT = os.getenv("SORA_API_ENDPOINT", "https://api.sora-service.com/v1/generate")
    SORA_API_KEY = os.getenv("SORA_API_KEY", "")

    # ── Freesound API Ayarı (örnek) ──────────────────────────
    FREESOUND_API_KEY = os.getenv("FREESOUND_API_KEY", "")

    # ── ZapSplat API Ayarları (örnek) ─────────────────────────
    ZAPSPLAT_APP_KEY = os.getenv("ZAPSPLAT_APP_KEY", "")
    ZAPSPLAT_APP_SECRET = os.getenv("ZAPSPLAT_APP_SECRET", "")

    # ── YouTube API Ayarları ─────────────────────────────────
    YOUTUBE_CLIENT_ID = os.getenv("YOUTUBE_CLIENT_ID", "")
    YOUTUBE_CLIENT_SECRET = os.getenv("YOUTUBE_CLIENT_SECRET", "")
    YOUTUBE_REFRESH_TOKEN = os.getenv("YOUTUBE_REFRESH_TOKEN", "")
    YOUTUBE_CHANNEL_ID = os.getenv("YOUTUBE_CHANNEL_ID", "")

    # ── OpenAI (ChatGPT) API Anahtarı ──────────────────────────
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

    # ── Geçici Dosyalar ve Loglar için Klasörler ───────────────
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    TEMP_DIR = os.path.join(BASE_DIR, "temp_media")
    LOG_FILE = os.path.join(BASE_DIR, "logs", "app.log")
