import os
import discord

from dotenv import load_dotenv
from discord.ext import commands
from Utilities.DataAccess import getPeople
from Utilities.DataAccess import addBalanceToPerson

## IMPORT COGS ##
from Cogs.Events import EventsCog
from Cogs.Views import ViewsCog

## INTENTS ##
intents = discord.Intents.default()
intents.members = True

## INITIALIZE BOT ##
bot = commands.Bot(command_prefix="$", intents=intents)

## ADD COGS ##
bot.add_cog(EventsCog(bot))
bot.add_cog(ViewsCog(bot))

## RUN BOT ##
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# people = getPeople()
# firstPerson = people[0]
# print(firstPerson.data)
# print(firstPerson.getBalance())
# print(firstPerson.addBalance(10))
# print(firstPerson.getBalance())
# print(addBalanceToPerson(firstPerson, 10))
# print(firstPerson.getBalance())
bot.run(TOKEN)
