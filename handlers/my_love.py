from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text


def auth_mylove(func):
    async def wrapper(message):
        if message['from']['id'] != 1056558564:
            return await message.reply('Доступ запрещён!', reply=False)
        return await func(message)

    return wrapper


@auth_mylove
async def menu(message: types.Message):
    start_btn = ['❤️ Не слушай кнопку справа, кликай меня!!!', '❌ Хотим кликнуть?']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_btn)
    

    await message.answer('Выбери:', reply_markup=keyboard)


@auth_mylove
async def bad_ans(message: types.Message):
    await message.answer('')


@auth_mylove
async def good_ans(message: types.Message):
    await message.answer('')


def registers_handlers_love(dp: Dispatcher):
    dp.register_message_handler(menu, commands=['жду'])
    dp.register_message_handler(bad_ans, Text(equals='❌ Кликай!!!'))
    dp.register_message_handler(good_ans, Text(equals='❤️ Не кликай!!!'))