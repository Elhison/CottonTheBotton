#!/usr/bin/env python

import discord
import random
import datetime
import time
import os

from discord.ext import commands, tasks
from itertools import cycle

bot = commands.Bot(command_prefix=commands.when_mentioned_or('69'))

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

    channel = bot.get_channel(705295704251301899)
    guild = discord.utils.get(bot.guilds, name="Cotton's Nursery")
    role_id = discord.utils.get(guild.roles, name="Carbon-based life form")
    # Add more welcome stuff
    welcomes = (f'Bienvenue, {member.mention}! Amusez-vous bien! 😘',
                f'Bienvenu, {member.mention} ! Amusez-vous bien! 😘',
                f'Welcome, {member.mention}! Enjoy your stay. ☺️',
                f'Wilkommen, {member.mention}!',
                f'Välkommen, {member.mention}!',
                f'Tervetuloa, {member.mention}!',
                f'Bine ai venti, {member.mention}! Să te simți bine aici! 😜')

    print(f'{member} has joined.')
    await channel.send(random.choice(welcomes))
    await member.add_roles(role_id)


@bot.event
async def on_member_remove(member):
    # Add more farewells
    channel = bot.get_channel(713995293833822208)
    farewells = (f'Goodbye, {member.name}/{member.id}. We will miss you! :(',
                 f'Auf Wiedersehen, {member.name}/{member.id}. :(',
                 f'Farväl, {member.name}/{member.id}. :(',
                 f'Jäähyväiset, {member.name}/{member.id}. :(',
                 f'La revedere, {member.name}/{member.id}. O să te lipsim.')

    print(f'{member} has left.')
    await channel.send(random.choice(farewells))


@bot.event
async def on_message(message):
    bad_words = ('dumb', 'stupid', 'ugly')

    if message.content.startswith("69"):

        await message.channel.send("nice.")

    elif "hamburger" in message.content.lower():

        await message.channel.send("https://youtu.be/El1BhIQFMfs")

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

    else:
        pass

    await bot.process_commands(message)


@bot.event
async def on_command_error(ctx, error):

    user_id = bot.get_user(354568022977019906)

    await ctx.channel.purge(limit=1)

    suggestion_channel = bot.get_channel(709728865467105281)
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("I don't know how to do that yet :/")
        await ctx.send(f"If you have any suggestions, you can do so in the {suggestion_channel.mention} channel :p")
    else:
        await ctx.send(f"An error probably occurred. Ask @{user_id} for any errors or shit.")


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

    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


@bot.command()
async def test(ctx):

    await ctx.send("How'd you discover this? :P")

bot.run('NzEwMDYxMDAzNjY0MjYxMjAx.XtcNLA.bAsYY5ngS2OxpoHNrxJDRQHz3TY')
