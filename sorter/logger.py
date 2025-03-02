import logging
from pathlib import Path

# Створення каталогу для логів, якщо він не існує
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# Налаштування логування з правильним кодуванням UTF-8
logging.basicConfig(
    filename=LOG_DIR / "sorter.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8"  # Додаємо кодування UTF-8
)

logger = logging.getLogger(__name__)

def log_error(message: str):
    """Логування помилок"""
    logger.error(message)

def log_info(message: str):
    """Логування інформаційних повідомлень"""
    logger.info(message)
