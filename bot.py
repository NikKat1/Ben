import os
import random
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN не найден в переменных окружения")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message()
async def yes_no_handler(message: Message):
    if not message.text:
        return

    # Проверяем, есть ли упоминание
    if not message.entities:
        return

    mentions = []
    for entity in message.entities:
        if entity.type == "mention":
            mention_text = message.text[entity.offset:entity.offset + entity.length]
            mentions.append(mention_text)

    if not mentions:
        return

    # Убираем упоминания
    question = message.text
    for m in mentions:
        question = question.replace(m, "").strip()

    if not question:
        return

    # Только если вопрос
    if "?" not in question:
        return

    answer = random.choice(["Yes", "No"])

    response = f"{question}\n\n<b>{answer}</b>"

    await message.reply(response, parse_mode="HTML")


async def main():
    print("✅ Бот запущен")
    await dp.start_polling(bot)


if name == "main":
    asyncio.run(main())
