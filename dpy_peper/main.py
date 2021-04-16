from discord.ext import commands


class VoiceWrapper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        self._multi_dispatch("!voice_state_update", member, before, after)
        if before.channel != after.channel:
            self._multi_dispatch("voice_channel_update", member, before.channel, after.channel)
            if before.channel is None:
                self._multi_dispatch("voice_channel_connect", member, after.channel)
            elif after.channel is None:
                self._multi_dispatch("voice_channel_disconnect", member, before.channel)
                if len(before.channel.members) == 1:
                    self._multi_dispatch("voice_channel_alone", member, before.channel)
            else:
                self._multi_dispatch("voice_channel_move", member, before.channel, after.channel)
            if after.afk:
                self._multi_dispatch("voice_afk", member, before.channel)
        if before.self_mute != after.self_mute:
            self._multi_dispatch("voice_mute_update", member)
            self._multi_dispatch("voice_self_mute_update", member)
            if after.self_mute:
                self._multi_dispatch("voice_mute_enable", member)
                self._multi_dispatch("voice_self_mute_enable", member)
            else:
                self._multi_dispatch("voice_mute_disable", member)
                self._multi_dispatch("voice_self_mute_disable", member)
        if before.mute != after.mute:
            self._multi_dispatch("voice_mute_update", member)
            self._multi_dispatch("voice_guild_mute_update", member)
            if after.mute:
                self._multi_dispatch("voice_mute_enable", member)
                self._multi_dispatch("voice_guild_mute_enable", member)
            else:
                self._multi_dispatch("voice_mute_disable", member)
                self._multi_dispatch("voice_guild_mute_disable", member)
        if before.self_deaf != after.self_deaf:
            self._multi_dispatch("voice_deaf_update", member)
            self._multi_dispatch("voice_self_deaf_update", member)
            if after.self_deaf:
                self._multi_dispatch("voice_deaf_enable", member)
                self._multi_dispatch("voice_self_deaf_enable", member)
            else:
                self._multi_dispatch("voice_deaf_disable", member)
                self._multi_dispatch("voice_self_deaf_disable", member)
        if before.deaf != after.deaf:
            self._multi_dispatch("voice_deaf_update", member)
            self._multi_dispatch("voice_guild_deaf_update", member)
            if after.deaf:
                self._multi_dispatch("voice_deaf_enable", member)
                self._multi_dispatch("voice_guild_deaf_enable", member)
            else:
                self._multi_dispatch("voice_deaf_disable", member)
                self._multi_dispatch("voice_guild_deaf_disable", member)
        if before.self_stream != after.self_stream:
            self._multi_dispatch("voice_stream_update", member)
            if after.self_stream:
                self._multi_dispatch("voice_stream_start", member)
            else:
                self._multi_dispatch("voice_stream_end", member)
        if before.self_video != after.self_video:
            self._multi_dispatch("voice_video_update", member)
            if after.self_video:
                self._multi_dispatch("voice_video_start", member)
            else:
                self._multi_dispatch("voice_video_end", member)

    def _multi_dispatch(self, name, member, *args, **kwargs):
        if name.startswith("!"):
            name = name.lstrip("!")
        else:
            self.bot.dispatch(name, member, *args, **kwargs)

        if member.bot:
            self.bot.dispatch(name + "_bot", member, *args, **kwargs)
            if member == self.bot.user:
                self.bot.dispatch(name + "_me", *args, **kwargs)
            else:
                self.bot.dispatch(name + "_other_bot", member, *args, **kwargs)
        else:
            self.bot.dispatch(name + "_user", member, *args, **kwargs)
