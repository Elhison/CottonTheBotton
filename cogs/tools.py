import discord
import datetime

from random import choice, randint
from discord.ext import commands


class Tools(commands.Cog):


    def __init__(self, bot):
        self.bot = bot
    

    @commands.command()
    async def poll(self, ctx, *, message):

        embed = discord.Embed(color=0xffff00)
        channel = self.bot.get_channel(717715772268609589)
        emoji_0 = '👍'
        emoji_1 = '👎'
        turtle = "%B %d, %Y"
        embed.add_field(name=f"Poll created by {ctx.author} on {datetime.date.today().strftime(turtle)}",
                        value=f"{message}")

        embed_id = await channel.send(embed=embed)
        await ctx.channel.purge(limit=1)
        await embed_id.add_reaction(emoji_0)
        await embed_id.add_reaction(emoji_1)

    @commands.command(aliases=["r/"])
    async def subreddit(self, ctx, message):
        await ctx.channel.purge(limit=1)
        await ctx.send(f"https://www.reddit.com/r/{message}")
        await ctx.send("Hey! Reddit sucks now. It's biased, pro-CCP, and anti-freespeech. Switch to Ruqqus!")
        await ctx.send("What's Ruqqus? Type `69whatisruqqus` to know what Ruqqus is!")

    @commands.command(aliases=['randomnumber', 'rdmnum', 'randomnum'])
    async def random_number(self, ctx, num1: int, num2: int):

        value = str(randint(num1, num2)) + "\n"

        await ctx.channel.purge(limit=1)
        await ctx.send(value)

    @commands.command()
    async def sort_alphabetically(self, ctx, *messages):

        msgs = list(messages)
        await ctx.channel.purge(limit=1)
        for entry in sorted(msgs):
            await ctx.send(entry)

    @commands.command()
    async def sort_alphabetically_error(self, ctx, error):

        await ctx.channel.purge(limit=1)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You forgot to tell me the words you want to sort alphabetically. -,-")

    @commands.command()
    async def reverse(self, ctx, *, message):

        await ctx.channel.purge(limit=1)
        msg = ctx.message.content
        message = msg[10:]
        await ctx.send(message[::-1])

    @reverse.error
    async def reverse_error(self, ctx, error):

        await ctx.channel.purge(limit=1)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You forgot to tell me what word you want to reverse. -,-")

    @commands.command()
    async def user_info(self, ctx, member: discord.Member):

        embed = discord.Embed(title=" ")
        embed.add_field(name="Username", value=f"{member.name}", inline=True)
        embed.add_field(name="User ID", value=f"{member.id}", inline=True)
        embed.add_field(name="Join Date", value=f"{member.joined_at}", inline=True)
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)
    
    @user_info.error
    async def user_info_error(self, ctx, error):

        await ctx.channel.purge(limit=1)

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Who do you want to know more about?")

        elif isinstance(error, discord.NotFound):
            await ctx.send("Member not found!")

    @commands.command()
    async def whatisruqqus(self, ctx):

        pass


def setup(bot):
    bot.add_cog(Tools(bot))
