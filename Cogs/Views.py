import discord
from discord.ext import commands
from Utilities import DataAccess

class ViewsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["bal"], help="Show Balance")
    async def showBalance(self, ctx, member : discord.Member=None):
        if member is not None:
            person = DataAccess.getPersonByID(member.id)
        else:
            person = DataAccess.getPersonByID(ctx.author.id)

        sa = "Balance is: "
        sb = str(person.getBalance())
        s = sa + sb

        await ctx.send(s) 
        