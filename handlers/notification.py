import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.chat.id
    await bot.send_message(chat_id=chat_id, text="Окс")


async def geek():
    await bot.send_message(chat_id=chat_id, text="Курсы")


async def finish():
    video = open("Media/rage.mp4", "rb")
    await bot.send_video(chat_id=chat_id, video=video, caption="Домой!")


async def scheduler():
    aioschedule.every().friday.at("15:30").do(geek)
    aioschedule.every().friday.at("20:00").do(finish)
    # aioschedule.every().second.do(go_to_sleep)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'Курсы' in word.text)
