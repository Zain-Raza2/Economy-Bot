import discord
from discord.ext import commands
from Utilities import DataAccess

#bot = commands.Bot(command_prefix='$')

class ViewsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["bal"], help="Show Balance")
    async def showBalance(self, ctx, member : discord.Member=None):
        if member is not None:
            person = DataAccess.getPersonByID(member.id)
        else:
            person = DataAccess.getPersonByID(ctx.author.id)

        embed = discord.Embed(
            title = "Balance is",
            description = str(person.getBalance()),
            colour = discord.Colour.purple()
        )

        embed.set_author(name=str(member.display_name), icon_url=member.avatar_url)

        await ctx.send(embed=embed)