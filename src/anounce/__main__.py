# Third Party Stuff
from telebot import TeleBot

# My Stuff
from src.anounce.anounce_view import AnounceView

anounce_bot = TeleBot("6491041620:AAERWwTDeFA31DM_FPLrd3Dsd8nFdNTZCLU")
anounce_view = AnounceView()


if __name__ == "__main__":
    message_text = anounce_view.get()

    anounce_bot.send_message(
        chat_id="-1002366288749",
        text=message_text,
        parse_mode="HTML",
    )
