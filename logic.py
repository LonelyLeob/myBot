from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN = '5312018256:AAEexXeQk3q_fPvam6LUgAoZI8nRfcLiEVw'


#bot+dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
