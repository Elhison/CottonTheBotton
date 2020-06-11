import discord
import time

from random import choice
from discord.ext import commands


class Roles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def send_roles_list(self, ctx):

        embed = discord.Embed(title="List of Server Roles", description="(Sorted alphabetically)", color=0x0000ff)
        embed.add_field(name="Math", value="""
            • Algebra
            • Arithmetic
            • Calculus
            • Combinatorics
            • Discrete
            • Game Theory
            • Geometry
            • Number Theory
            • Statistics
            • Topology
            • Trigonometry""", inline=True)

        embed.add_field(name="Science", value="""
            • Astronomy
            • Biology
            • Botany
            • Chemistry
            • Computer Science
            • Ecology
            • Geology
            • Medicine
            • Meteorology
            • Mycology
            • Oceanography
            • Physics
            • Psychology
            • Witchcraft
            • Zoology""", inline=True)

        embed.add_field(name="Technology", value="""
            • Programming""", inline=True)

        embed.add_field(name="Humanities", value="""
            • Anthropology
            • Archaeology
            • Classics
            • History
            • Linguistics
            • Law
            • Music
            • Politics
            • Literature
            • Philosophy
            • Religion
            • Performing Arts
            • Visual Arts""", inline=True)

        embed.add_field(name="Languages", value="""
            • English
            • Finnish
            • French
            • German
            • Italian
            • Japanese
            • Swedish""", inline=True)

        embed.set_footer(text=f"Last updated: {time.ctime()}")
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Roles(bot))

