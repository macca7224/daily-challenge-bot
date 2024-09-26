#!/usr/bin/python3

import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from daily_challenge import create_daily_challenge

load_dotenv()

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)


async def daily_task():
    channel_id = int(os.getenv('CHANNEL_ID'))
    channel = bot.get_channel(channel_id)

    # Post new challenge
    challenge_id, message = create_daily_challenge()

    await channel.send(f'{message}\nhttps://www.geoguessr.com/challenge/{challenge_id}')


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    await daily_task()
    await bot.close()


bot.run(os.getenv('BOT_TOKEN'))
