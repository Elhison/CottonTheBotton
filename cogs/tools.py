import discord
from random import choice, randint
from discord.ext import commands


class Tools(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['randomnumber', 'rdmnum'])
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


def setup(bot):
    bot.add_cog(Tools(bot))
