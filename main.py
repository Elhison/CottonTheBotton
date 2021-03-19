import discord

client = discord.Client()



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="with my pp"))
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

pwd_file = open("bruh.txt")

pwd = pwd_file.readlines()
print(pwd)
client.run(pwd[0])