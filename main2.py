import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject
from aiogram import F
from aiogram.types import FSInputFile
import sqlite3

con = sqlite3.connect("sss.db")
cursor = con.cursor()
cursor.execute("SELECT * FROM Jokes")
data = cursor.fetchall()
jokes = [i[2] for i in data]
names = [i[1] for i in data]

def generate_keyboard():
    kb =[]
    for i in names:
        kb.append([types.KeyboardButton(text=i)])
    keyboard=types.ReplyKeyboardMarkup(keyboard=kb,
                                       resize_keyboard=True,
                                      )

    return keyboard
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6601762989:AAHQ7DbOsTKS-K-Ii5WqX6zyVWlaouSSVbg")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer('Нажмите кнопку с названием Joke чтобы появилась шутка',reply_markup=generate_keyboard())


@dp.message(Command("image"))
async def cmd_start(message: types.Message):
    imagebot = FSInputFile("1.jpg")
    await message.answer_photo(imagebot,
                                caption="Фотка")

@dp.message(F.text)
async def cmd_start(message: types.Message):
    imagebot = FSInputFile("photo_5382208142538040602_x.jpg")
    for i in range(10):
        if message.text == names[i]:
            await message.answer_photo(imagebot, caption=jokes[i])
async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())

