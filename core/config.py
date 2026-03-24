"""Configuration - Tập trung tất cả cấu hình"""

import os
from pathlib import Path
from datetime import timezone, timedelta

# ─── APP ─────────────────────────────────────────────────────────────
APP_NAME = "FB Reels Poster"
APP_VERSION = "4.2.0"

# ─── PATHS ────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"

DATA_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)

# ─── FILES ────────────────────────────────────────────────────────────
CONFIG_FILE = DATA_DIR / "config.json"
ACCOUNTS_FILE = DATA_DIR / "accounts.json"
HISTORY_FILE = DATA_DIR / "history.json"
VIDEOS_DB = DATA_DIR / "videos.json"
FAILED_JOBS_FILE = DATA_DIR / "failed_jobs.json"
ANALYTICS_FILE = DATA_DIR / "analytics.json"
POST_REGISTRY_FILE = DATA_DIR / "post_registry.json"
WARMUP_FILE = DATA_DIR / "warmup_config.json"
EXCEL_CONFIG_FILE = DATA_DIR / "excel_config.json"
SHEETS_CONFIG_FILE = DATA_DIR / "sheets_config.json"
TELEGRAM_CONFIG_FILE = DATA_DIR / "telegram_config.json"
TOKEN_KEY_FILE = DATA_DIR / ".token_key"

# ─── FACEBOOK ─────────────────────────────────────────────────────────
GRAPH_VERSION = "v22.0"
GRAPH_BASE = f"https://graph.facebook.com/{GRAPH_VERSION}"

# ─── UPLOAD ───────────────────────────────────────────────────────────
MAX_FILE_SIZE_BYTES = 4 * 1024 * 1024 * 1024
SUPPORTED_VIDEO_EXTS = {".mp4", ".mov", ".avi", ".mkv", ".webm", ".m4v"}

# ─── DELAY ────────────────────────────────────────────────────────────
UPLOAD_DELAY_MIN = 300
UPLOAD_DELAY_MAX = 900
WARMUP_DELAY_MIN = 900
WARMUP_DELAY_MAX = 1800

# ─── TIMEZONE ─────────────────────────────────────────────────────────
VN_TZ = timezone(timedelta(hours=7))

# ─── LOGGING ───────────────────────────────────────────────────────────
LOG_LEVEL = "INFO"
LOG_FILE = LOGS_DIR / "app.log"

# ─── GUI ───────────────────────────────────────────────────────────────
WINDOW_WIDTH = 1060
WINDOW_HEIGHT = 740
THEME = "clam"

# Colors
COLOR_PRIMARY = "#1877F2"
COLOR_SUCCESS = "#31A24C"
COLOR_ERROR = "#DC3545"
COLOR_WARNING = "#FFC107"