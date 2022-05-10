from aiogram import executor
from logic import *
from db import add_db
from handlers import my_love, reg_auth, body

async def startup(_):
    print('Старт выполнен успешно')
    add_db()

#регистр хэндлеров
my_love.registers_handlers_love(dp)
reg_auth.registers_handlers_auth(dp)
body.registers_handlers_body(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=startup)