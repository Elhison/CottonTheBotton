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
            • Discrete Math
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
            • Back-end Development
            • C
            • C++
            • Front-end Development
            • Java
            • Python
            
            """, inline=True)

        embed.add_field(name="Humanities", value="""
            • Anthropology
            • Archaeology
            • Arts
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
            • Korean
            • Portuguese
            • Romanian
            • Swedish""", inline=True)

        embed.add_field(name="Classes", value="""
        • History Class
        • Linguistics Class
        • Math Class
        • Programming Class
        • Science Class""")

        embed.add_field(name="Countries", value="""
        • There are a total of 257 countries. 
        • I'm not gonna list all of them here. Lol.
        """)

        embed.set_footer(text=f"Last updated: {time.ctime()}")
        await ctx.channel.purge(limit=2)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Roles(bot))
