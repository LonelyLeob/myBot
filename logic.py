from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from tokens import TOKEN

storage = MemoryStorage()


#bot+dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
