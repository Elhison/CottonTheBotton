import discord
from random import choice
from discord.ext import commands


class Social(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def affection(self, ctx):

        hugs = ['༼ つ ◕_◕ ༽つ', '(づ｡◕‿‿◕｡)づ', '(づ￣ ³￣)づ', '༼ つ  ͡° ͜ʖ ͡° ༽つ', '😘',
                '(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ✧ﾟ･: *ヽ(◕ヮ◕ヽ)', '♥‿♥', '😽', '😙', '😚', '\u2665', '\u2764']

        await ctx.channel.purge(limit=1)
        await ctx.send(choice(hugs))


def setup(bot):
    bot.add_cog(Social(bot))
