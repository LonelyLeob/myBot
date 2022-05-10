from aiogram import Dispatcher, types
from meta import *
from db import get_user, is_opened
from weather_script import weather_curr


@is_opened
async def collect_menu(message: types.Message):
    """Меню режима работы с документами"""
    #Меню с функциями над документами
    collect_btn = ['📗 Все документы', '🔍 Искать по фильтру', '➕ Добавить документ']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*collect_btn)

    await message.answer('Как работаем?', reply_markup=keyboard)

@is_opened
async def info_menu(message: types.Message):
    """Information from meta.py"""
    await message.answer(f'Информация:\nВерсия: {version}\nПо проблемам: {author_name}')

@is_opened
async def profile(message: types.Message):
    """User info"""
    us_id = message.from_user.id
    us_info = get_user(us_id)
    if us_info[6] == None:
        tel_check = 'Отсутствует'
    else:
        tel_check = us_info[6]
    if us_info[7] == None:
        em_check = 'Отсутствует'
    else:
        em_check = us_info[7]
    await message.answer(f'Ваш ID в системе: {us_info[0]}\n'
                        f'Дата регистрации: {us_info[3]}\n'
                        f'Уровень прав: {us_info[5]}\n'
                        f'Номер телефона: {tel_check}\n'
                        f'Email: {em_check}'
                        )


@is_opened
async def weather(message: types.Message):
    """Get weather in Kaluga"""
    data = weather_curr()
    curr_desc = data.get('desc')
    curr_temp = data.get('temp')
    curr_feel = data.get('feel')

    await message.answer('Погода в городе Калуга\n'
                        f'Статус: {curr_desc}\n'
                        f'Температура на улице: {curr_temp}\n'
                        f'Ощущается как: {curr_feel}'
                        )
    

def registers_handlers_body(dp: Dispatcher):
    dp.register_message_handler(collect_menu, commands=['docs'])
    dp.register_message_handler(info_menu, commands=['info'])
    dp.register_message_handler(profile, commands=['profile'])
    dp.register_message_handler(weather, commands=['weather'])