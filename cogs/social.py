import discord
import time
import random

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

    @commands.command()
    async def battle(self, ctx, member: discord.Member):
        
        await ctx.send(f"{ctx.author.mention} has challenged {member.mention} in a duel!")
        time.sleep(2)
        if random.randint(0,100) <= 50:
            await ctx.send(f"And... {ctx.author.mention} lost. How humiliating! Never start a fight that you can't end, dipshit.")
        else:
            await ctx.send(f"And... {member.mention} lost. At least you tried :3")

def setup(bot):
    bot.add_cog(Social(bot))
