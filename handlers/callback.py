from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup

from config import bot, dp


# @dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton(
        "NEXT",
        callback_data='button_call_2',
    )
    markup.add(button_call_2)

    question = 'By whom invented Python?'
    answers = [
        "Harry Potter",
        "Putin",
        "Voldemort",
        "Griffin",
        "Linus Torvalds",
        "Guido Van Rossum",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=5,
        explanation="Сам думай",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


# @dp.callback_query_handler(lambda call: call.data == "button_call_2")
async def quiz_3(call: types.CallbackQuery):
    question = 'ОТВЕЧАЙ!!!!'
    answers = [
        '4',
        '8',
        '4, 6',
        '2, 4',
        '5',
    ]

    @dp.message_handler(commands=['mem'])
    async def mem_1(message: types.Message):
        photo = open("Media/mem.jpg", 'rb')
        await bot.send_photo(chat_id=message.chat.id, photo=photo)

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Сам думай",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == "button_call_2")
