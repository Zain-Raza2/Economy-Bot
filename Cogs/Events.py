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
    async def pay(self, ctx, member : discord.Member, amount):
    
        Paymentamount = int(amount)
        if member is not ctx.author:
            person = DataAccess.getPersonByID(member.id)
            person2 = DataAccess.getPersonByID(ctx.author.id)
            
        if isPaymentValid(person2.getBalance(), Paymentamount) is True:
            DataAccess.addBalanceToPerson(person, Paymentamount)
            DataAccess.removeBalanceFromPerson(person2, Paymentamount)
        
        embed = discord.Embed(title = "New balance is", description = str(person.getBalance()), colour = discord.Colour.purple())
        embed.set_author(name=str(member.display_name), icon_url=member.avatar_url)
        embed.set_thumbnail(url="https://tenor.com/view/money-countingmoney-gif-6053223")
            
        await ctx.send(embed=embed)
