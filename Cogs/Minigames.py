import random
import discord
from discord.ext import commands
from Utilities import DataAccess

class MinigamesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["cf"], help="Flip a coin")
    async def coinflip(self, ctx, member : discord.Member, amount):
        Paymentamount = int(amount)
        
        if member is not ctx.author:
            person = DataAccess.getPersonByID(member.id)
            person2 = DataAccess.getPersonByID(ctx.author.id)
        
            if Paymentamount < int(person.getBalance()) and Paymentamount < int(person2.getBalance()) and Paymentamount > int(0):
                coin = ['Heads', 'Tails']
                result = random.choice(coin)
                print(result)
                if result == 'Heads':
                    winner = member
                    DataAccess.addBalanceToPerson(person, Paymentamount)
                    DataAccess.removeBalanceFromPerson(person2, Paymentamount)

                if result == 'Tails':
                    winner = ctx.author
                    DataAccess.addBalanceToPerson(person2, Paymentamount)
                    DataAccess.removeBalanceFromPerson(person, Paymentamount)
 
        embed = discord.Embed(title = "The winner is", description = str(winner), colour = discord.Colour.purple())
        embed.set_author(name=str(winner.display_name), icon_url=winner.avatar_url)
        embed.set_thumbnail(url="https://media.giphy.com/media/6jqfXikz9yzhS/giphy.gif")
        embed.add_field(name=("They got " + result), value='\u200b', inline=True)
        await ctx.send(embed=embed)
