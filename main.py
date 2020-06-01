#!/usr/bin/env python

import discord
import random

from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix='69')
client.remove_command("help")

status = cycle([' with your little sister', ' with my stepsister',
                ' with your mom', ' with myself'])

print("Booting...")


@client.event
async def on_ready():
    change_status.start()
    hourly_message.start()
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_member_join(member):
    # Add more welcome stuff
    role_id = member.Guild.get_role(705295866495500339)
    channel = client.get_channel(705295704251301899)
    welcomes = (f'Bienvenue, {member.mention} !',
                f'Bienvenu, {member.mention} !',
                f'Welcome, {member.mention}! Enjoy your stay. ☺️',
                f'Wilkommen, {member.mention}!',
                f'Välkommen, {member.mention}!',
                f'Tervetuloa, {member.mention}!')

    print(f'{member} has joined.')
    await channel.send(random.choice(welcomes))
    await member.add_roles(role_id)


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
    bad_words = ('dumb', 'stupid', 'ugly')

    if message.content.startswith("69"):
        await message.channel.send("nice.")

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

    else:
        pass

    await client.process_commands(message)


# Tasks!!!

# Tasks!!!


@tasks.loop(seconds=60)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@tasks.loop(hours=1)
async def hourly_message(ctx):
    hour_messages = ('How is everyone doing?',
                     'Anyone want to chat?',
                     'Joshua Pogchamp once said, "Pog".')
    await ctx.send(random.choice(hour_messages))


# Commands!!!

# Commands!!!


@client.command()
async def whoami(ctx):
    await ctx.send(f'{ctx.author} / {ctx.author.mention} / {ctx.author.nickname}')


@client.command(aliases=['members'])
async def members_list(message):
    guild_id = client.get_guild(693377457243553873)
    await message.channel.send(f"There are {guild_id.member_count-2} virgins on this server.")


@client.command()
async def botping(ctx):
    await ctx.send(f'{client.latency * 1000}ms')


@client.command()
async def role(message):
    # Assigns roles
    roles_list = ('Math', 'Science')
    if message.content.startswith(f'role {roles_list}'):
        message.send('Gave you x!')


@client.command(aliases=['love'])
async def affection(ctx):
    hugs = ['༼ つ ◕_◕ ༽つ', '(づ｡◕‿‿◕｡)づ', '(づ￣ ³￣)づ', '༼ つ  ͡° ͜ʖ ͡° ༽つ', '😘',
            '(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ✧ﾟ･: *ヽ(◕ヮ◕ヽ)', '♥‿♥', '😽', '😙', '😚', '\u2665', '\u2764']
    await ctx.send(random.choice(hugs))


@client.command(aliases=['8ball'])
async def eightball(ctx, *, question):
    answer = ["Yes", "Of course", "Always",
              "Maybe", "Probably",
              "No", "Never", "In your dreams!"]

    if question == "":
        await ctx.send(f'Ask me a question. Lmaoooooo')
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(answer)}')


@client.command(aliases=['rdmnumber', 'randomnumber', 'rdmnum', 'randomnum'])
async def random_number(ctx, num1: int, num2: int, typer):
    value = str(random.uniform(num1, num2)) + "\n"
    value2 = str(random.randint(num1, num2)) + "\n"

    if typer == 'double' or typer == 'float' or typer == 'decimal':
        await ctx.send(value)

    else:
        await ctx.send(value2)


@client.command()
async def ban(ctx, member: discord.Member):

    await ctx.channel.send(f'Banning {member.mention}...')


client.run('')
