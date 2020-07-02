import discord
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):

        bot_spam_channel = bot.get_channel(709669976390500422)

        await ctx.bot_spam_channel.send("HELP!")


def setup(bot):
    bot.add_cog(Help(bot))