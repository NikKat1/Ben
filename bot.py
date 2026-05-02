import os
import random
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.inline_query()
async def inline_handler(query: InlineQuery):
    text = query.query.strip()

    if not text:
        return

    answer = random.choice(["Yes", "No"])

    result = InlineQueryResultArticle(
        id="1",
        title=f"{answer}",
        description=text,
        input_message_content=InputTextMessageContent(
            message_text=f"{text}\n\n<b>{answer}</b>",
            parse_mode="HTML"
        )
    )

    await query.answer([result], cache_time=1)


async def main():
    print("✅ Inline бот запущен")
    await dp.start_polling(bot)


if name == "main":
    asyncio.run(main())
