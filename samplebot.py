import os

import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
if __name__ == '__main__':
    bot = commands.Bot(command_prefix='/', allowed_mentions=discord.AllowedMentions.none())
    bot.load_extension('dpy_peper')

    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user}.")

    @bot.event
    async def on_voice_channel_connect(member, channel):
        await discord.utils.get(member.guild.text_channels, name="vc-log").send(f"{member.mention} joined {channel.name}")

    @bot.event
    async def on_voice_channel_disconnect(member, channel):
        await discord.utils.get(member.guild.text_channels, name="vc-log").send(f"{member.mention} left {channel.name}")

    @bot.event
    async def on_voice_channel_move(member, before, after):
        await discord.utils.get(member.guild.text_channels, name="vc-log").send(f"{member.mention} moved {after.name} from {before.name}")

    @bot.event
    async def on_voice_mute_enable(member):
        await discord.utils.get(member.guild.text_channels, name="vc-log").send(f"{member.mention} enabled mute.")

    @bot.event
    async def on_voice_mute_disable(member):
        await discord.utils.get(member.guild.text_channels, name="vc-log").send(f"{member.mention} disabled mute.")

    @bot.event
    async def on_voice_deaf_enable(member):
        await discord.utils.get(member.guild.text_channels, name="vc-log").send(f"{member.mention} enabled deaf.")

    @bot.event
    async def on_voice_deaf_disable(member):
        await discord.utils.get(member.guild.text_channels, name="vc-log").send(f"{member.mention} disabled deaf.")

    @bot.event
    async def on_voice_stream_start(member):
        await discord.utils.get(member.guild.text_channels, name="vc-log").send(f"{member.mention} started stream at {member.voice.channel.name}.")

    @bot.event
    async def on_voice_stream_end(member):
        await discord.utils.get(member.guild.text_channels, name="vc-log").send(f"{member.mention} ended stream at {member.voice.channel.name}.")

    bot.run(os.getenv('token'))
