import discord
from discord.ext import commands
from Utilities import DataAccess

class EventsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_ready")
    async def getMembers(self):
        for member in self.bot.get_all_members():
            if not member.bot and DataAccess.getPersonByID(member.id) == None:
                DataAccess.addPersonByID(member.id)

    @commands.command(aliases=["p"], help="Pay Balance")
    async def pay(self, ctx, member : discord.Member):
        if member is not ctx.author:
            person = DataAccess.getPersonByID(member.id)
            person2 = DataAccess.getPersonByID(ctx.author.id)

        DataAccess.addBalanceToPerson(person, 10)
        DataAccess.removeBalanceFromPerson(person2, 10)
    
    