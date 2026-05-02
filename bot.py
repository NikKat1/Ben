import os
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

    answers = ["Ес", "Ноу"]

    results = []

    for i, ans in enumerate(answers):
        results.append(
            InlineQueryResultArticle(
                id=str(i),
                title=ans,
                description=text,
                input_message_content=InputTextMessageContent(
                    message_text=f"{text}\n\n<b>{ans}</b>",
                    parse_mode="HTML"
                )
            )
        )

    await query.answer(results, cache_time=5)


async def main():
    print("✅ Бот запущен")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
