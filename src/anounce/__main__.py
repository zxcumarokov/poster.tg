# Standard Library
import os
from datetime import (
    datetime,
    timedelta,
    timezone,
)
from logging import (
    FileHandler,
    Formatter,
    basicConfig,
    getLogger,
)

# Third Party Stuff
from dotenv import load_dotenv
from telebot import TeleBot

# My Stuff
from src.anounce.anounce_view import AnounceView
from src.anounce.ride.implementations import (
    CreateRide,
    RequestRide,
)
from src.anounce.route.implementations import (
    CreateRoute,
    ParseRouteData,
)

from .send_anounce import SendAnounce

# Загрузка переменных окружения
load_dotenv()

# Настройка логирования
log_file = os.path.join("logs", "bot.log")
basicConfig(
    level="DEBUG",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        FileHandler(log_file),
    ],  # Записываем в файл
)
logger = getLogger(__name__)

# Инициализация бота
anounce_bot = TeleBot(os.getenv("BOT_TOKEN", ""))
if not anounce_bot:
    logger.error("BOT_TOKEN не установлен или пуст.")
    raise ValueError("BOT_TOKEN не установлен или пуст.")

calendar_url = os.getenv("CALENDAR_URL")
calendar_id = os.getenv("CALENDAR_ID")
url = f"{calendar_url}{calendar_id}"
token = os.getenv("NOTION_TOKEN")
if not token:
    logger.error("NOTION_TOKEN не установлен или пуст.")
    raise ValueError("NOTION_TOKEN не установлен или пуст.")

notion_version = "2022-02-22"
current_date = datetime.now(timezone.utc)
next_day = current_date + timedelta(days=1)

notion_token = os.getenv("NOTION_TOKEN")
if not notion_token:
    logger.error("NOTION_TOKEN не установлен или пуст.")
    raise ValueError("NOTION_TOKEN не установлен или пуст.")

notion_base_url = os.getenv("NOTION_BASE_URL")
if not notion_base_url:
    logger.error("NOTION_BASE_URL не установлен или пуст.")
    raise ValueError("NOTION_BASE_URL не установлен или пуст.")

anounce_view = AnounceView()
create_ride = CreateRide()
parse_ride = RequestRide(url=url, token=token, notion_version=notion_version)
create_route = CreateRoute()
parse_route = ParseRouteData(notion_base_url=notion_base_url, notion_token=notion_token)

send_anounce = SendAnounce(
    anounce_bot=anounce_bot,
    anounce_view=anounce_view,
    create_ride=create_ride,
    parse_ride=parse_ride,
    create_route=create_route,
    parse_route=parse_route,
)

if __name__ == "__main__":
    try:
        logger.info("Запуск бота...")
        # Отправляем данные на следующий день
        send_anounce.send(date=next_day)
        logger.info(f"Данные успешно отправлены на {next_day}.")
    except Exception as e:
        logger.exception("Произошла ошибка при выполнении бота.")
