import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject
from aiogram import F
from aiogram.types import FSInputFile

jokes=[
    "-Пап! -Что -Я попал камнем в лексус -Мальчик что тебе надо",
    "-Как называют ворону которая села на оголенные провода? -Электрокар",
    "Повзрослел-это когда у стоматолога боишься не боли а цены",

]
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6601762989:AAHQ7DbOsTKS-K-Ii5WqX6zyVWlaouSSVbg")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message, command: CommandObject):
    if command.args is None:
        await message.answer("Привет!")
        return
    else:
        await message.answer(f"Привет, {command.args}")
        return

@dp.message(F.text.lower() == "привет")
async def cmd_start(message: types.Message):
    await message.answer("Привет я бот meat,меня создал супер мега дупер пупер Мегамозг,я написан на языке Python")

@dp.message(Command("image"))
async def cmd_start(message: types.Message):
    imagebot = FSInputFile("1.jpg")
    await message.answer_photo(imagebot,
                                caption="Фотка")

# @dp.message(Command("image_group"))
# async def cmd(message: types.Message):
#     albom_builder = MediaGroupBuilder(caption="фотки")
#     imagebot = FSInputFile("1.jpg")
#     imagebot2 = FSInputFile("1.jpg")
#     albom_builder.add_photo(media=imagebot)
#     albom_builder.add_photo(media=imagebot2)
#     await message.answer_media_group(media=albom_builder.build())
@dp.message(Command("joke"))
async def cmd_start(message: types.Message, command: CommandObject):
    imagebot = FSInputFile("photo_5382208142538040602_x.jpg")
    if command.args is None:
        await message.answer("Ошибка номер шутки!")
        return
    elif command.args == "1":
        await message.answer_photo(imagebot, caption="-Пап! -Что -Я попал камнем в лексус -Мальчик что тебе надо")
        return
    elif command.args == "2":
        await message.answer_photo(imagebot, caption="-Как называют ворону которая села на оголенные провода? -Электрокар")
        return
    elif command.args =="3":
        await message.answer_photo(imagebot, caption="-Какую песню не поют на кладбище -Забери меня собой")
        return
    elif command.args =="4":
        await message.answer_photo(imagebot, caption="-Почему в загсе не когда не моют окна -Остаются разводы")
        return
    elif command.args == "5":
        await message.answer_photo(imagebot, caption="Повзрослел-это когда у стоматолога боишься не боли а цены")
        return
    elif command.args == "6":
        await message.answer_photo(imagebot, caption="Курить по три пачки в день эьо тежелый путь -Но,разве нам нужны легкие!")
        return
    else:
        await message.answer(f"Ошибка неверный ввод")
        return
async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())

