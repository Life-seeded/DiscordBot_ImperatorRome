import discord
import github
import random
import os.path
from discord.ext import commands
from discord.utils import get
client = commands.Bot(command_prefix='+')
TOKEN = os.getenv("DISCORD_TOKEN")
USERNAME = os.getenv("DISCORD_USERNAME")
PASSWORD = os.getenv("DISCORD_PASSWORD")
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

g = github.Github(USERNAME, PASSWORD)
repo = g.get_user().get_repo("DiscordBot_ImperatorRome")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command(name="테스터", pass_context=True)
async def _TesterRole(ctx, member: discord.Member=None):
    global tester
    member = ctx.message.author
    membername = member.nick
    if membername:
        if membername.lower().count("테스터") > 0 or membername.lower().count("코더") > 0 or membername.lower().count("설정") > 0 or membername.lower().count("임시") > 0 or membername.lower().count("일러") > 0 or membername.lower().count("감사") > 0 or membername.lower().count("완장") > 0 or membername.lower().count("프린터") > 0:
            await ctx.channel.send("닉네임에 `테스터`, `코더`, `설정`, `임시`, `일러`, `감사`, `완장`, `프린터` 중 하나가 있으면 테스터 역할을 추가로 얻을 수 없습니다.")
        else:
            await member.add_roles(get(ctx.guild.roles, name="테스터"))
            await ctx.channel.send(f"{member.mention} 에게 테스터 역할이 적용되었습니다.")
            tester += 1
            await member.edit(nick="테스터" + str(tester))
            f = open(file, 'w')
            f.write(str(tester))
            f.close()
            contents = repo.get_contents("testernum.txt", ref="blob")
            repo.update_file(contents.path, "auto commit", str(tester), contents.sha, branch="master")
    else:
        await member.add_roles(get(ctx.guild.roles, name="테스터"))
        await ctx.channel.send(f"{member.mention} 에게 테스터 역할이 적용되었습니다.")
        tester += 1
        await member.edit(nick="테스터" + str(tester))
        f = open(file, 'w')
        f.write(str(tester))
        f.close()
        contents = repo.get_contents("testernum.txt", ref="master")
        repo.update_file(contents.path, "auto commit", str(tester), contents.sha, branch="master")

@client.command(name="테스터숫자", pass_context=True)
async def _TesterRole(ctx, member: discord.Member=None):
    global tester
    await ctx.channel.send(str(tester) + "명의 테스터들이 존재합니다.")

@client.event
async def on_message(message):
    await client.process_commands(message)

    if message.author == client.user:
        return

    if message.content.startswith('+Hello'):
        await message.channel.send('Hello, World!')


if __name__ == "__main__":
    client.run(TOKEN)
