#!/usr/bin/python

import asyncio
import discord
import random

from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix='69')
client.remove_command("help")

status = cycle([' with your little sister',' with my stepsister', ' with your mom', ' with myself'])

print("Booting...")

@client.event
async def on_ready():
    channel = client.get_channel(709669976390500422)
    change_status.start()
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await channel.send("I'm online!")


@client.event
async def on_member_join(member):
    # Add more welcome stuff
    roleID = member.Guild.get_role(705295866495500339)
    channel = client.get_channel(705295704251301899)
    welcomes = (f'Bienvenue, {member.mention} !',
                f'Bienvenu, {member.mention} !',
                f'Welcome, {member.mention}! Enjoy your stay. ☺️',
                f'Wilkommen, {member.mention}!',
                f'Välkommen, {member.mention}!',
                f'Tervetuloa, {member.mention}')


    print(f'{member} has joined.')
    await channel.send(random.choice(welcomes))
    await member.add_roles(roleID)


@client.event
async def on_member_remove(member):
    # Add more farewells
    channel = client.get_channel(713995293833822208)
    farewells = (f'Goodbye, {member.mention}. We will miss you! :(',
                 f'Auf Wiedersehen, {member.mention}. :(',
                 f'Farväl, {member.mention}. :(',
                 f'Jäähyväiset, {member.mention}. :(')


    print(f'{member} has left.')
    await channel.send(random.choice(farewells))


@client.event
async def on_message(message):
    bad_words = ('dumb','stupid','ugly')

    if message.content.startswith("69"):
        await message.channel.send("nice.")

    elif "turtles" in message.content.lower() or "turtle" in message.content.lower():
        emoji = "\U0001F422"
        await message.add_reaction(emoji)

    elif message.content.startswith(f"turtles are {bad_words}"):
        await message.channel.send("no u")

    elif message.content.startswith("fuck you") or message.content.startswith("Fuck you"):
        await message.channel.send("No thanks :p")


    else:
        pass


    await client.process_commands(message)


# Tasks!!!

# Tasks!!!


@tasks.loop(seconds=60)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))



# Commands!!!

# Commands!!!


@client.command()
async def whoami(ctx):
    await ctx.send(f'{ctx.author} / {ctx.author.mention} / {ctx.author.nickname}')


@client.command()
async def members_list(message):
    id = client.get_guild(693377457243553873)
    await message.channel.send(f"There are {id.member_count-2} virgins on this server.")


@client.command(aliases=['8ball'])
async def eightball(ctx, *, question):
    answer = ["Yes", "Maybe", "No"]

    if question == "":
        print("Empty!")
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(answer)}')


@client.command()
async def botping(ctx):
    await ctx.send(f'{client.latency * 1000}ms')


@client.command()
async def role(message):
    # Assigns roles
    roles_list = ('Math','Science')
    if message.content.startswith(f'role {roles_list}'):
        message.send('Gave you x!')


@client.command()
async def love(message):
    emojiChoice = ['\u2665','\u2764']
    emoji = random.choice(emojiChoice)
    await message.add_reaction(emoji)


@client.command()
async def affection(ctx):
    hugs = ['༼ つ ◕_◕ ༽つ', '(づ｡◕‿‿◕｡)づ','(づ￣ ³￣)づ','༼ つ  ͡° ͜ʖ ͡° ༽つ','😘',
            '(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ✧ﾟ･: *ヽ(◕ヮ◕ヽ)','♥‿♥','😽','😙','😚']
    await ctx.send(random.choice(hugs))


@client.command(aliases=['rdmnumber','randomnumber','rdmnum','randomnum'])
async def random_number(ctx):

    await ctx.send()


# client.run(INSERT_TOKEN_HERE)
