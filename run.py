import discord
#import github
import random
import os.path
from discord.ext import commands
from discord.utils import get
#intents = discord.Intents.default()
#intents.members = True
#client = commands.Bot(command_prefix='+', intents=intents)
client = commands.Bot(command_prefix='+')
TOKEN = os.getenv("DISCORD_TOKEN")
#USERNAME = os.getenv("DISCORD_USERNAME")
#PASSWORD = os.getenv("DISCORD_PASSWORD")
##client = discord.Client()
#messages = tester = 0
#file = "testernum.txt"
#if os.path.isfile(file):
#    f = open(file, 'r')
#    line = f.readline()
#    tester = int(line)
#    f.close()
#    print('Succesfully Read Testernum')
#else :
#    print("I can't read Testernum")
#
#g = github.Github(USERNAME, PASSWORD)
#repo = g.get_user().get_repo("DiscordBot_ImperatorRome")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('discord' + discord.__version__)
    await client.change_presence(activity=discord.Game(name='부서진 마천루 | ++help'))

@client.event
async def on_member_join(member):
    embed=discord.Embed(title= f"안녕하세요. 부서진 마천루에 오신것을 환영합니다.", description=f"", color=0xf3bb76)
    embed.add_field(name=f"해당 질문에 답변해 주시길 바랍니다.",value=f"1.들어온 경로를 말씀해주세요.\n2.들어온 이유를 말씀해주세요.\n",inline=False)
    embed.add_field(name=f"모딩 관전을 위한 안내사항",value=f"모딩 관전 목적으로 오셨다면 `+관전`을 입력하여 자동적으로 관전 역할을 받을수 있습니다.\n",inline=False)
    #embed.add_field(name=f"모드 테스트를 위한 안내사항",value=f"모드 테스트 목적으로 오셨다면 `+테스터`를 입력하여 자동으로 테스터 역할을 받을수 있습니다.\n",inline=False)
    #embed.add_field(name=f"#테스터-안내사항",value=f"모드 설치 방법",inline=True)
    #embed.add_field(name=f"#테스트팀",value=f"다른 테스터들과 대화 또는 게임상황 공유",inline=True)
    #embed.add_field(name=f"#버그-건의, #좆같은점, #그래픽문제들",value=f"문제점 건의나 버그 제보",inline=False)
    await client.get_channel(643113605990055946).send(embed=embed)
    await client.get_channel(643113605990055946).send(f"{member.mention} 관전을 하고 싶으시다면 `+관전` 을 입력해 주세요.")
    print("New member joined")
    
#@client.command(name="테스터", pass_context=True)
#async def _TesterRole(ctx, member: discord.Member=None):
#    global tester
#    member = member or ctx.message.author
#    membername = member.nick
#    if membername:
#        if membername.lower().count("테스터") > 0 or membername.lower().count("코더") > 0 or membername.lower().count("설정") > 0 or membername.lower().count("임시") > 0 or membername.lower().count("일러") > 0 or membername.lower().count("감사") > 0 or membername.lower().count("완장") > 0 or membername.lower().count("프린터") > 0 or membername.lower().count(".إلله") > 0 or membername.lower().count("번역기") or membername.lower().count("관전") > 0 or membername.lower().count("포트레잇") > 0:
#            await ctx.channel.send("닉네임에 `테스터`, `코더`, `설정`, `임시`, `일러`, `감사`, `완장`, `프린터`, `.إلله`, `번역기`, `관전`, `포트레잇` 중 하나가 있으면 테스터 역할을 추가로 얻을 수 없습니다.")
#        else:
#            await member.add_roles(get(ctx.guild.roles, name="테스터"))
#            await ctx.channel.send(f"{member.mention} 에게 테스터 역할이 적용되었습니다.")
#            tester += 1
#            await member.edit(nick="테스터" + str(tester))
#            f = open(file, 'w')
#            f.write(str(tester))
#            f.close()
#            contents = repo.get_contents("testernum.txt", ref="blob")
#            repo.update_file(contents.path, "auto commit", str(tester), contents.sha, branch="master")
#    else:
#        await member.add_roles(get(ctx.guild.roles, name="테스터"))
#        await ctx.channel.send(f"{member.mention} 에게 테스터 역할이 적용되었습니다.")
#        tester += 1
#        await member.edit(nick="테스터" + str(tester))
#        f = open(file, 'w')
#        f.write(str(tester))
#        f.close()
#        contents = repo.get_contents("testernum.txt", ref="master")
#        repo.update_file(contents.path, "auto commit", str(tester), contents.sha, branch="master")

#@client.command(name="테스터숫자", pass_context=True)
#async def _TesterRole(ctx, member: discord.Member=None):
#    global tester
#    await ctx.channel.send(str(tester) + "명의 테스터들이 존재합니다.")

@client.command(name="관전", pass_context=True)
async def _ObserverRole(ctx, member: discord.Member=None):
    member = member or ctx.message.author
    membername = member.nick
    if membername:
        if membername.lower().count("테스터") > 0 or membername.lower().count("코더") > 0 or membername.lower().count("설정") > 0 or membername.lower().count("임시") > 0 or membername.lower().count("일러") > 0 or membername.lower().count("감사") > 0 or membername.lower().count("완장") > 0 or membername.lower().count("프린터") > 0 or membername.lower().count(".إلله") > 0 or membername.lower().count("번역기") or membername.lower().count("관전") > 0 or membername.lower().count("포트레잇") > 0:
            await ctx.channel.send("닉네임에 `테스터`, `코더`, `설정`, `임시`, `일러`, `감사`, `완장`, `프린터`, `.إلله`, `번역기`, `관전`, `포트레잇` 중 하나가 있으면 관전 역할을 추가로 얻을 수 없습니다.")
        else:
            await member.add_roles(get(ctx.guild.roles, name="관전(역할)"))
            await ctx.channel.send(f"{member.mention} 에게 관전 역할이 적용되었습니다.")
            await member.edit(nick="관전")
    else:
        await member.add_roles(get(ctx.guild.roles, name="관전(역할)"))
        await ctx.channel.send(f"{member.mention} 에게 관전 역할이 적용되었습니다.")
        await member.edit(nick="관전")

@client.command(name="Hello", pass_context=True)
async def _HelloWorld(ctx, member: discord.Member=None):
    await ctx.channel.send("Hello, World!")

@client.command(name="인삿말", pass_context=True)
async def _Notice(ctx, member: discord.Member=None):
    embed=discord.Embed(title= f"안녕하세요. 부서진 마천루에 오신것을 환영합니다.", description=f"", color=0xf3bb76)
    embed.add_field(name=f"해당 질문에 답변해 주시길 바랍니다.",value=f"1.들어온 경로를 말씀해주세요.\n2.들어온 이유를 말씀해주세요.\n",inline=False)
    embed.add_field(name=f"모딩 관전을 위한 안내사항",value=f"모딩 관전 목적으로 오셨다면 `+관전`을 입력하여 자동적으로 관전 역할을 받을수 있습니다.\n",inline=False)
    #embed.add_field(name=f"모드 테스트를 위한 안내사항",value=f"모드 테스트 목적으로 오셨다면 `+테스터`를 입력하여 자동으로 테스터 역할을 받을수 있습니다.\n",inline=False)
    #embed.add_field(name=f"#테스터-안내사항",value=f"모드 설치 방법",inline=True)
    #embed.add_field(name=f"#테스트팀",value=f"다른 테스터들과 대화 또는 게임상황 공유",inline=True)
    #embed.add_field(name=f"#버그-건의, #좆같은점, #그래픽문제들",value=f"문제점 건의나 버그 제보",inline=False)
    await ctx.send(embed=embed)
    member = member or ctx.message.author
    await ctx.channel.send(f"{member.mention} 관전을 하고 싶으시다면 `+관전` 을 입력해 주세요.")

@client.command(name="위키", pass_context=True)
async def _wiki(ctx, member: discord.Member=None):
    embed=discord.Embed(title= f"", description=f"", color=0xf3bb76)
    embed.add_field(name='공식 부서진 마천루 위키', value='\n'+'[%s](<%s>)' % ('위키 주소', 'https://fallenskyscrapper.fandom.com/ko/wiki/%EB%8C%80%EB%AC%B8'), inline=False)
    await ctx.send(embed=embed)

@client.command(name="드라이브", pass_context=True)
async def _drive(ctx, member: discord.Member=None):
    embed=discord.Embed(title= f"", description=f"", color=0xf3bb76)
    embed.add_field(name='부서진 마천루 드라이브', value='\n'+'[%s](<%s>)' % ('드라이브 주소', 'https://drive.google.com/folderview?id=1dwgiw5rz2qMwaPnZ6NW_x3b89SeHH6sn'), inline=False)
    await ctx.send(embed=embed)

@client.command(name="+help", pass_context=True)
async def _help(ctx, member: discord.Member=None):
    embed=discord.Embed(title= f"Imperator Rome Bot", description=f"임페라토르 롬 봇의 명령어를 출력합니다.", color=0xf3bb76)
    embed.set_author(name="Imperator Rome", url="", icon_url="https://upload.wikimedia.org/wikipedia/en/0/04/Imperator_Rome_logo.png")
#    embed.add_field(name=f"+테스터",value=f"테스터 역할을 부여합니다.",inline=True)
#    embed.add_field(name=f"+테스터숫자",value=f"테스터들의 숫자를 출력합니다.",inline=True)
    embed.add_field(name=f"+관전",value=f"관전 역할을 부여합니다.",inline=True)
    embed.add_field(name=f"+인삿말 @유저이름",value=f"안내사항을 출력합니다.",inline=True)
    embed.add_field(name=f"+위키",value=f"공식 위키의 링크를 출력합니다.",inline=True)
    embed.add_field(name=f"+드라이브",value=f"드라이브의 링크를 출력합니다.",inline=True)
    embed.add_field(name=f"+Hello",value=f"Hello, World!를 출력합니다.",inline=True)
    await ctx.send(embed=embed)

if __name__ == "__main__":
    client.run(TOKEN)
