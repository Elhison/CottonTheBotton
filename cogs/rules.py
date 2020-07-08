import discord
import time
from discord.ext import commands


class Rules(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def first_rule(self, ctx):
        embed = discord.Embed(title=" ", color=0xffff66)
        embed.add_field(name="Rule #1:",
                        value="You can joke about anything as long as you don't offend other people. If you do offend someone, apologize.",
                        inline=False)

        await ctx.channel.purge(limit=3)
        await ctx.send(embed=embed)

    @commands.command()
    async def second_rule(self, ctx):
        embed = discord.Embed(title=" ", color=0xffff66)
        embed.add_field(name="Rule #2", value="NSFW content is allowed in the appropriate channels.",
                        inline=False)

        await ctx.channel.purge(limit=3)
        await ctx.send(embed=embed)

    @commands.command()
    async def third_rule(self, ctx):
        embed = discord.Embed(title=" ", color=0xffff66)
        embed.add_field(name="Rule #3",
                        value="Bestiality, child porn, torture, etc. are not allowed and will result in an immediate ban.",
                        inline=False)

        await ctx.channel.purge(limit=3)
        await ctx.send(embed=embed)

    @commands.command()
    async def fourth_rule(self, ctx):
        embed = discord.Embed(title=" ", color=0xffff66)
        embed.add_field(name="Rule #4",
                        value="We are all equal and we accept everyone — regardless of race, gender, or sexuality.",
                        inline=False)

        await ctx.channel.purge(limit=3)
        await ctx.send(embed=embed)

    @commands.command()
    async def fifth_rule(self, ctx):
        embed = discord.Embed(title=" ", color=0xffff66)
        embed.add_field(name="Rule #5",
                        value="You can only advertise your works (video, project, product, etc.) in the advertisement channel.",
                        inline=False)
        await ctx.channel.purge(limit=3)
        await ctx.send(embed=embed)

    @commands.command()
    async def sixth_rule(self, ctx):
        embed = discord.Embed(title=" ", color=0xffff66)
        embed.add_field(name="Rule #6", value="Swearing is allowed as long as you don't offend anyone.",
                        inline=False)

        await ctx.channel.purge(limit=3)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_any_role('Big pp')
    async def send_rules_list(self, ctx):
        nsfw_channel = self.bot.get_channel(713952790971678812)
        await ctx.channel.purge(limit=2)

        embed = discord.Embed(title="Server Rules:", color=0xffff66)
        embed.add_field(name="Rule #1",
                        value="You can joke about anything as long as you don't offend other people. If you do offend someone, apologize.",
                        inline=False)

        embed.add_field(name="Rule #2", value="NSFW content is allowed in the appropriate channels.",
                        inline=False)

        embed.add_field(name="Rule #3",
                        value="Bestiality, child porn, torture, etc. are not allowed and will result in an immediate ban.",
                        inline=False)

        embed.add_field(name="Rule #4",
                        value="We are all equal and we accept everyone — regardless of race, gender, or sexuality.",
                        inline=False)

        embed.add_field(name="Rule #5",
                        value="You can only advertise your works (video, project, product, etc.) in the advertisement channel.",
                        inline=False)

        embed.add_field(name="Rule #6", value="Swearing is allowed as long as you don't offend anyone.",
                        inline=False)

        embed.add_field(name="Rule #7", value="Nationalism is strictly banned.",
                        inline=False)

        embed.add_field(name="Rule #8", value=f"Sex-related content go to {nsfw_channel.mention}.",
                        inline=False)

        embed.set_footer(text=f"Rules are bound to change. We will notify you.\nLast updated: {time.ctime()}")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Rules(bot))
