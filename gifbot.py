import random
import discord
from discord.ext import commands

from core import * 

token = 'NjE0ODc3NjMyMTYwNTk2MDY4.XWF3dg.SjV2sWrBEOLUmguJKsjizZqNtpo'
VERSION = '0.0.4'

bot = commands.Bot(command_prefix = 'gg.')
	
# Events
@bot.event
async def on_ready():
    print(bot.user.name + " - Copyright 2019 Ayush Bardhan Tripathy")
    print("Running on discord.py: ", discord.__version__)
    await bot.change_presence(activity = discord.Game(name = "Searching for awesome gifs..."))

bot.remove_command('help')

# Offical commands
@bot.command()
async def help(msg):
    folder = discord.Embed(title = "gifbot - Help", description = "Prefix is gg.",color = 0xeee657)

    folder.add_field(name = "help", value = "This view", inline = False)
    folder.add_field(name = "info", value = "Info about the bot", inline = False)
    folder.add_field(name = "ping", value = "Ping Pong", inline = False)
    folder.add_field(name = "GIF Command List",  value = "boi, wtf, wow, confused, work, stare, hello, dance, sorry, scared, kirby", inline = False)
    await msg.send(embed = folder)

@bot.command()
async def info(msg):
    folder = discord.Embed(title = "gifbot - Info", type = "rich", color = 0xeee657)
    
    folder.add_field(name = "Info", value = "A simple bot which has gifs for every situation", inline = False)
    folder.add_field(name = "Author", value = "I dont have a nickname#0313")
    folder.add_field(name = "Twitter", value = "@AyushGameDev")
    folder.add_field(name = "Server Count", value = f"{len(bot.guilds)}")
    folder.add_field(name = "Discord", value = "https://discord.gg/A9dTbdG")
    folder.add_field(name = "Invite", value = "<tba>")
    folder.add_field(name = "Website", value = "<tba>")
    folder.add_field(name = "Donate", value = "<tba>")
    folder.add_field(name = "Library", value = "discord.py")
    folder.add_field(name = "Version", value = "{}".format(VERSION))
    folder.add_field(name = "Other", value = "If you want to give feedback, report bug, send gifs or request/suggest features?\nDM me in Discord or contact through Twitter.", inline = False)
    folder.add_field(name = "Legal", value = "All the gifs used in this bot are the preperty of their respective owners.", inline = False)

    await msg.send(embed = folder)

@bot.command(name = 'ping', aliases = ['pong'])
async def ping(msg):
    folder = discord.Embed(title = "gifbot - Pong!", description = f"```{bot.latency}```")
    await msg.send(embed = folder)

# Fun commands
@bot.command(aliases = ['ohboi'])
async def boi(msg): await gif_command(msg, 'boi')

@bot.command(aliases = ['dafaq'])
async def wtf(msg): await gif_command(msg, "wtf")
	
@bot.command(aliases = ['ohwow', 'wowman'])
async def wow(msg): await gif_command(msg, "wow")

@bot.command()
async def confused(msg): await gif_command(msg, "confused")

@bot.command(aliases = ['working', 'lookbusy'])
async def work(msg): await gif_command(msg, "work")

@bot.command()
async def stare(msg): await gif_command(msg, "stare")

@bot.command(aliases = ['hi'])
async def hello(msg): await gif_command(msg, "hello")

@bot.command()
async def dance(msg): await gif_command(msg, "dance")

@bot.command(aliases = ['oksorry'])
async def sorry(msg): await gif_command(msg, "sorry")

@bot.command()
async def scared(msg): await gif_command(msg, "scared")

@bot.command(aliases = ['kirbies'])
async def kirby(msg): await gif_command(msg, "kirby")

@bot.command(aliases = ['gay', 'gayee', 'gey'])
async def thatsgay(msg): await gif_command(msg, "thatsgay")

# Run the bot
bot.run(token)
