import os
import random
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN не найден")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.inline_query()
async def inline_handler(query: InlineQuery):
    text = query.query.strip()

    if not text:
        return

    # Рандомный ответ
    answer = random.choice(["Ес", "Ноу"])

    result = InlineQueryResultArticle(
        id="1",
        title="🎱 Ответ Бена",
        description="Нажми чтобы узнать",
        input_message_content=InputTextMessageContent(
            message_text=f"{text}\n\n<b>{answer}</b>",
            parse_mode="HTML"
        )
    )

    await query.answer([result], cache_time=1)


async def main():
    print("✅ Бот запущен")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
