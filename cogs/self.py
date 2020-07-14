import discord
from discord.ext import commands


class Self(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def role(self, ctx, *, role_name):

        guild = discord.utils.get(self.bot.guilds, name="Cotton's Den")
        role_id = discord.utils.get(guild.roles, name=role_name)
        await ctx.channel.purge(limit=1)
        if role_name == "KGB spy" or role_name == "Cardinal" or role_name == "Small pp" or role_name == "Big pp" or role_name == "Pope (entshuldigung)" or role_name == "Pyrocynical's Brother" or role_name == "God" or role_name == "Jesus Christ" or role_name == "Science Teacher" or role_name == "Programming Teacher" or role_name == "Math Teacher" or role_name == "Counsellor" or role_name == "Business Teacher" or role_name == "Linguistics Teacher" or role_name == "Music Teacher" or role_name == "Carbon-based life form" or role_name == "Unverified" or role_name == "Peasant Bot" or role_name == "@everyone" or role_name == "@@everyone" or role_name == "Counsellor":
            ctx.send("Nice try.")
        else:
            await ctx.send(f"Gave {ctx.author} a {role_id} role!")
            await ctx.author.add_roles(role_id)

    @commands.command()
    async def whoami(self, ctx):

        await ctx.send(f'{ctx.author.mention}/{ctx.author.id}')


def setup(bot):
    bot.add_cog(Self(bot))
