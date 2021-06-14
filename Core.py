import os
import discord

from dotenv import load_dotenv
from discord.ext import commands
from Utilities.DataAccess import getPeople
from Utilities.DataAccess import addBalanceToPerson

## IMPORT COGS ##
from Cogs.Events import EventsCog
from Cogs.Views import ViewsCog
from Cogs.Minigames import MinigamesCog

## INTENTS ##
intents = discord.Intents.default()
intents.members = True

## INITIALIZE BOT ##
bot = commands.Bot(command_prefix="$", intents=intents)

## ADD COGS ##
bot.add_cog(EventsCog(bot))
bot.add_cog(ViewsCog(bot))
bot.add_cog(MinigamesCog(bot))

## RUN BOT ##
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)
