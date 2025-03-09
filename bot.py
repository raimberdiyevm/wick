import logging
from aiogram import Bot, Dispatcher, types
import os
from dotenv import load_dotenv

# .env faylini yuklash
load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")  # Telegram botning tokeni

# Logging sozlamalari
logging.basicConfig(level=logging.INFO)

# Bot va Dispatcher yaratish
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Salom! Botga xush kelibsiz.")

@dp.message_handler(commands=['check'])
async def check_info(message: types.Message):
    # Shtrix kodi va saqlash muddati kiritilishi kerak
    text = "Botni ishlatish uchun shtrix kodi va saqlash muddati oxirgi kunini yuboring."
    await message.reply(text)

if __name__ == '__main__':
    # Eski 'executor.start_polling(dp, skip_updates=True)' kodini o'zgartirmay davom ettiring
    dp.start_polling(skip_updates=True)
