import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
import asyncio
import time
import lxml
from gtts import gTTS
import os
bot = commands.Bot(command_prefix='~')

@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online, activity=None)

@bot.command()
async def 설명서(ctx):
    await ctx.send("~tts 할말 - 봇이 할말을 대신말해줍니다\n~out - 봇을 음성채팅방에서 내보냅니다")
    

@bot.command(name="tts")
async def tts(ctx, *args):
    text = " ".join(args)
    user = ctx.message.author
    if user.voice != None:
        try:
            global vc
            global entireText
            vc = await ctx.message.author.voice.channel.connect()
        except:
            vc = ctx.voice_client
            
        sound = gTTS(text=text, lang="ko", slow=False)
        sound.save("tts-audio.mp3")
        if vc.is_playing():
            vc.stop()
            
        vc.play(discord.FFmpegPCMAudio("tts-audio.mp3"))
    else:
        await ctx.send("없는 명령어 입니다")
@bot.command()
async def out(ctx):
    try:
        await vc.disconnect()
    except:
        await ctx.send("이미 채널에서 나가있습니다")
        
access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
