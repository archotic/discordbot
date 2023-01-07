from discord.ext.commands import Bot
from discord.ext import commands
import discord
from ip2geotools.databases.noncommercial import DbIpCity
import socket
import random
from socket import gethostbyaddr
import os
import hashlib
import argparse
import nmap3
import zipfile
import os.path
import os
import subprocess
import chess
import stockfish


client = discord.Client()
bot = commands.Bot(command_prefix="./")

@bot.event
async def on_ready():
    print("botisready")
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("with Linux"))

@bot.command(name='text2hash')
async def hash(ctx, arg1, arg2):
    text = arg1
    hashType = arg2
    encoder = text.encode('utf_8')
    myHash = ''
    if hashType.lower() == 'md5':
        myHash = hashlib.md5(encoder).hexdigest()
    elif hashType.lower() == 'sha1':
        myHash = hashlib.sha1(encoder).hexdigest()
    elif hashType.lower() == 'sha224':
        myHash = hashlib.sha224(encoder).hexdigest()
    elif hashType.lower() == 'sha256':
        myHash = hashlib.sha256(encoder).hexdigest()
    elif hashType.lower() == 'sha384':
        myHash = hashlib.sha384(encoder).hexdigest()
    elif hashType.lower() == 'sha512':
        myHash = hashlib.sha512(encoder).hexdigest()
    else:
        await ctx.send('[!] The script does not support this hash type')
        exit(0)
    await ctx.send(myHash)


board = chess.Board()
@bot.command(name='move')
async def scan(ctx, arg):
    board.legal_moves
    chess.Move.from_uci(arg) in board.legal_moves
    board.push_san(arg)
    board.is_checkmate()
    board.is_check()
    if(board.is_check() == True and board.is_checkmate() == False):
        await ctx.send("```Check```")
    await ctx.send("```" + str(board) + "```")
    if(board.is_checkmate() == True):
        await ctx.send("```Checkmate```")


bot.run('MTA1MTkzNzQzOTAzNzU0MjQxMA.GO-GN1.5RGBn1fy6n42wfpMM_S1bgPnvQA2tt7eqMkKHM')
