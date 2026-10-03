import nextcord

import asyncio
import os

from nextcord.ext import commands
from dotenv import load_dotenv

from componentsv2 import NextcordAPIWrapperV2 as Wrapper

intents = nextcord.Intents.default()
intents.message_content = True

load_dotenv()
token = os.getenv("TOKEN")

bot = commands.Bot(intents=intents)
wrapper = Wrapper(bot)

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user.name}. Ready to handle scams! >:3")

async def main():
    try:
        await bot.start(token)
    finally:
        if not bot.is_closed():
            await bot.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Successfully terminated bot - going offline.")