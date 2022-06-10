from aiogram import types
from aiogram.utils import executor
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup

from config import bot, dp
import logging


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Hello {message.from_user.full_name}")


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "NEXT",
        callback_data='button_call_1',
    )
    markup.add(button_call_1)

    question = 'Who is Martin Luther King?'
    answers = [
        'The president', 'shooter', 'Preacher', 'Scientist'
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Сам думай",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton(
        "NEXT",
        callback_data='button_call_2',
    )
    markup.add(button_call_2)

    question = 'What the SpaceX?'
    answers = [
        "First Variant",
        "Putin",
        "Store",
        "Griffin",
        "SpaceXsenomorphics",
        "Space Exploration Technologies Corporation",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=5,
        explanation="Сам думай",
    )


@dp.message_handler(commands=['mem'])
async def mem_1(message: types.Message):
    photo = open("Media/mem.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)


@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

# if __name__ == "__main__":
#     executor.start_polling(dp, skip_updates=True)
