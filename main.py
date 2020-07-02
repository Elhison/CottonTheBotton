#!/usr/bin/env python

import discord
import random
import datetime
import time
import os
# import newuser

from discord.ext import commands, tasks
from itertools import cycle

bot = commands.Bot(command_prefix=commands.when_mentioned_or('69'))
bot.remove_command("help")

status = cycle([' with your little sister', ' with your brother', ' with your mom',
                ' with myself', ' with my stepsister', ' with my step brother'])

print("Booting...")


@bot.event
async def on_ready():
    change_status.start()
    print(f'Logged in at {time.ctime()}')
    print('------')


@bot.event
async def on_member_join(member):

    # Add more welcome stuff
    welcomes = (f'Bienvenue, {member.mention}! Amusez-vous bien! 😘',
                f'Bienvenu, {member.mention} ! Amusez-vous bien! 😘',
                f'Welcome, {member.mention}! Enjoy your stay. ☺️',
                f'Wilkommen, {member.mention}!',
                f'Välkommen, {member.mention}!',
                f'Tervetuloa, {member.mention}!',
                f'Bine ai venti, {member.mention}! Să te simți bine aici! 😜',
                f'어서오세요, {member.mention}! 여기서 잘 지내세요. 😙',
                f'Benvenuto, {member.mention}. Goditi la permanenza nel gruppo',
                f'नमस्ते ,{member.mention}. मज़े करो!')

    guild = member.guild
    unverified_role = discord.utils.get(guild.roles, name="Unverified")
    channel = bot.get_channel(705295704251301899)
    rules_channel = bot.get_channel(705296662914138215)
    roles_list_channel = bot.get_channel(712521240052498444)
    print(f'{member} has joined.')

    embed = discord.Embed(title="Welcome to the server! uwu", description="| (• ◡•)|   (❍ᴥ❍ʋ)")
    embed.add_field(name="Please read the rules, master. Thank you :3", value=f"{rules_channel.mention}", inline=True)
    embed.add_field(name="Ask any of the Cardinals, the Pope, or Pyrocynical's Brother to give you the \"Carbon-based life form role.\"", value="I chose not to have an automatic verification system because it's vulnerable to bot raids. Thank you for your patience.", inline=True)
    
    
    await member.send(embed=embed)
    await member.add_roles(unverified_role)
    await channel.send(f"{random.choice(welcomes)}")

    # embed = discord.Embed(title="Congrats! You're not a robot!", description="Here are some features that you now have access to:")
    # embed.add_field(name="You can now assign yourself some awesome roles!", value=f"{roles_list_channel.mention}", inline=True)

@bot.event
async def on_member_remove(member):
    # Add more farewells
    channel = bot.get_channel(713995293833822208)
    farewells = (f'Goodbye, {member.mention}/{member.id}. We will miss you! :(',
                 f'Auf Wiedersehen, {member.mention}/{member.id}. :(',
                 f'Farväl, {member.mention}/{member.id}. :(',
                 f'Jäähyväiset, {member.mention}/{member.id}. :(',
                 f'La revedere, {member.mention}/{member.id}. O să te lipsim.',
                 f'잘 가세요, {member.mention}. 우리는 당신이 그리울 거예요:(',
                 f'अलविदा {member.mention}/{member.id}, हम आपको याद करेंगे')

    print(f'{member} has left.')
    await channel.send(random.choice(farewells))


@bot.event
async def on_message(message):

    bad_words = ('dumb', 'stupid', 'ugly')
    if not message.author.bot:

        if message.content.startswith("69"):
            await message.channel.send("nice.")

        elif "hamburger" in message.content.lower():

            await message.channel.send("https://youtu.be/El1BhIQFMfs")

        elif message.content.startswith("Josh") or message.content.startswith("josh"):

            await message.channel.send("hi")

        elif "turtles" in message.content.lower() or "turtle" in message.content.lower():

            emoji = "\U0001F422"
            await message.add_reaction(emoji)

        elif message.content.startswith(f"turtles are {bad_words}"):

            await message.channel.send("no u")

        elif message.content.startswith("fuck you") or message.content.startswith("Fuck you"):

            await message.channel.send("No thanks :p")

        elif message.content.startswith("fuck") or message.content.startswith("Fuck"):

            await message.channel.send("you.")

        elif "shit" in message.content.lower():

            await message.add_reaction("\U0001F4A9")

        elif "linux" in message.content.lower():

            await message.channel.send("i use arch, btw")

        elif "bitch" in message.content.lower():

            await message.add_reaction("♀")
            await message.add_reaction("🐕")

        elif "motherfucker" in message.content.lower():

            await message.channel.send("I will fuck your mother too!")

        elif "rasengan" in message.content.lower():

            await message.channel.send("Chidori!")

        elif "chidori" in message.content.lower():

            await message.channel.send("Rasengan!")

        else:
            pass

    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):

    user_id = bot.get_user(354568022977019906)
    suggestion_channel = bot.get_channel(709728865467105281)

    await ctx.channel.purge(limit=1)

    if isinstance(error, commands.CommandNotFound):
        await ctx.send("CommandNotFound error. I don't know how to do that yet :/")
        await ctx.send(f"If you have any suggestions, you can do so in the {suggestion_channel.mention} channel :p")
        print(error)

    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("MissingRequiredArgument error. Are you sure you're using the command correctly?")
        print(error)

    else:
        await ctx.send(f"An error probably occurred. Ask @{user_id} for any errors or shit.")
        print(error)
        


# Tasks!!!


# Tasks!!!


@tasks.loop(seconds=60)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))


# Cogs!!!


# Cogs!!!


@bot.command()
@commands.has_any_role('Big pp')
async def load(ctx, extension):

    bot.load_extension(f'cogs.{extension}')


@bot.command()
@commands.has_any_role('Big pp')
async def unload(ctx, extension):

    bot.unload_extension(f'cogs.{extension}')


@bot.command()
@commands.has_any_role('Big pp')
async def reload(ctx, extension):

    await ctx.channel.purge(limit=1)
    
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    print(f"{extension} cog reloaded!")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


@bot.command()
async def test(ctx):

    await ctx.send("How'd you discover this? :P")

bot.run('NzEwMDYxMDAzNjY0MjYxMjAx.Xv0raw.AtFldn0QCjBu2KgRxz9-1YrLYe8')
