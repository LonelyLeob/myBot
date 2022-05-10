import sqlite3
from aiogram import Dispatcher, types
from db import *
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.dispatcher import FSMContext

class FSMAuth(StatesGroup):
    pwd = State()


async def send_welcome(message: types.Message):
    """Welcome"""
    await message.reply(
        f'Приветствуем вас в агреггаторе документов DocsManagement!\n\n'
        'Чтобы перейти к работе, используйте команды:\n\n'
        '/reg - чтобы зарегистироваться в системе\n\n'
        '/auth - чтобы войти в существующий аккаунт\n\n'
        'С уважением, админ DocsManagement.', reply=False)


async def reg_user(message: types.Message):
    '''Generate new user'''
    us_name = message.from_user.username
    us_id = message.from_user.id

    try:
        newus_pwd = gen_pwd()
        add_user(us_id, us_name, newus_pwd)
        await message.answer(f'Ваш новый пароль: {newus_pwd}')
    except sqlite3.IntegrityError:       
        await message.answer('Вы уже зарегистрированы в системе. Перейдите на вкладку входа и введите пароль.')


async def auth_user(message: types.Message):
    """Authentification user"""

    await message.answer('Введите пароль:')
    await FSMAuth.pwd.set()


async def check_pwd(message: types.Message, state: FSMContext):
    """Checking for user and pwd"""
    us_id = message.from_user.id
    async with state.proxy() as data:
        data['pwd'] = message.text

    is_valid = get_auth(us_id, data['pwd'])
    
    if is_valid == True:
        await message.answer('Поздравляем, вы успешно вошли!')
        await message.answer('Теперь вам доступны следующие команды:\n/docs - работа с документами\n/info - контактная информация\n/profile - ваш профиль\n/weather - погода в Калуге\n\n/quit - выйти из системы')
        await state.finish()
    elif is_valid == False:
        await message.answer('Вы не зарегистрированы или ввели неверный пароль. Попробуйте ввести команду /reg.')
        await state.finish()

async def quit(message: types.Message):
    msg_id = message.from_user.id
    session_state(False, msg_id)
    await message.answer('Вы успешно вышли из системы!')


def registers_handlers_auth(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])
    dp.register_message_handler(reg_user, commands=['reg'])
    dp.register_message_handler(auth_user, commands=['auth'], state=None)
    dp.register_message_handler(check_pwd, state=FSMAuth.pwd)
    dp.register_message_handler(quit, commands=['quit'])