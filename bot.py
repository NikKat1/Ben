import os
import random
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

# Токен из переменных окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN не найден в переменных окружения")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.inline_query()
async def inline_handler(query: InlineQuery):
    text = query.query.strip()

    # если ничего не написано — не отвечаем
    if not text:
        return

    # генерируем ответ
    answer = random.choice(["Yes", "No"])

    result = InlineQueryResultArticle(
        id="1",
        title=f"Ответ: {answer}",
        description=text,
        input_message_content=InputTextMessageContent(
            message_text=f"{text}\n\n<b>{answer}</b>",
            parse_mode="HTML"
        )
    )

    # отправляем результат
    await query.answer([result], cache_time=1)


async def main():
    print("✅ Inline бот запущен")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
