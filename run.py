import discord
import random
import os.path
from discord.ext import commands
from discord.utils import get
client = commands.Bot(command_prefix='!')
#client = discord.Client()

messages = tester = 0
file = "testernum.txt"
if os.path.isfile(file):
    f = open(file, 'r')
    line = f.readline()
    tester = int(line)
    f.close()
    print('Succesfully Read Testernum')
else :
    print("I can't read Testernum")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command(name="테스터", pass_context=True)
async def _TesterRole(ctx, member: discord.Member=None):
    global tester
    member = ctx.message.author
    membername = member.nick
    if membername:
        if membername.lower().count("테스터") > 0:
            await ctx.channel.send(f"게이야 테스터 역할이 하나면 충분하지 뭘 더 원하노?")
        else:
            await member.add_roles(get(ctx.guild.roles, name="테스터"))
            await ctx.channel.send(f"{member.mention} 에게 테스터 역할이 적용되었습니다.")
            tester += 1
            await member.edit(nick="테스터" + str(tester))
            f = open(file, 'w')
            f.write(str(tester))
            f.close()
    else:
        await member.add_roles(get(ctx.guild.roles, name="테스터"))
        await ctx.channel.send(f"{member.mention} 에게 테스터 역할이 적용되었습니다.")
        tester += 1
        await member.edit(nick="테스터" + str(tester))
        f = open(file, 'w')
        f.write(str(tester))
        f.close()

@client.command(name="테스터숫자", pass_context=True)
async def _TesterRole(ctx, member: discord.Member=None):
    global tester
    await ctx.channel.send(str(tester) + "명의 테스터들이 존재합니다.")

@client.event
async def on_message(message):
    await client.process_commands(message)

    if message.author == client.user:
        return

    if message.content.startswith('!Hello'):
        await message.channel.send('Hello, World!')



client.run(DISCORD_TOKEN)
