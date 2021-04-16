<p style="font-size: 2rem">English/<a href="https://github.com/sevenc-nanashi/dpy-peper/blob/main/README_ja.md">Japanese</a></p>

[![PyPI - Version](https://img.shields.io/pypi/v/dpy-peper?style=flat-square)](https://pypi.org/project/dpy-peper) [![PyPI - Downloads](https://img.shields.io/badge/dynamic/json?style=flat-square&label=downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2Fdpy-peper)](https://pepy.tech/project/dpy-peper/)

# peper

peper = <small>d</small>**p**<small>y-voic</small>**e**<small>-hel</small>**per**  
A wrapper of discord.py's on_voice_state_update.

# How to use

`python3 -m pip install dpy-peper`

## Use as extension

Load with `load_extension`.

```python
from discord.ext import commands

bot = commands.Bot(command_prefix='/')
bot.load_extension('dpy_peper')
# or
# bot.load_extension('discord.ext.peper')
bot.run("Th1sIsN0tT0k3n.B3cause.1fiShowB0tWillG3tH4cked")
```

## Use as cog

Import `VoiceWrapper` from module.

```python
from discord.ext import commands
from dpy_peper import VoiceWrapper
# or
# from discord.ext.peper import VoiceWrapper
bot = commands.Bot(command_prefix='/')
bot.add_cog(VoiceWrapper(bot))
bot.run("Th1sIsN0tT0k3n.B3cause.1fiShowB0tWillG3tH4cked")
```

# Events

|Name|Description|Arguments|
|----|-----------|---------|
| `voice_channel_update` | fires on when someone connected/moved/disconnected VC. | member, before_channel, after_channel |
| `voice_channel_connect` | fires on when someone connected VC. | member, channel |
| `voice_channel_move` | fires on when someone moved VC. | member, before_channel, after_channel |
| `voice_channel_disconnect` | fires on when someone disconnected VC. | member, channel |
| `voice_channel_afk` | fires on when someone connected AFK VC. | member, before_channel |
| `voice_channel_alone` | fires on when someone disconnected VC and only 1 user is remaining. | member, channel |
| `voice_mute_update` | fires on when someone enabled/disabled self-mute/guild-mute. | member |
| `voice_mute_enable` | fires on when someone enabled self-mute/guild-mute. | member |
| `voice_mute_disable` | fires on when someone disabled self-mute/guild-mute. | member |
| `voice_self_mute_update` | fires on when someone self-muted/self-unmuted. | member |
| `voice_self_mute_enable` | fires on when someone enabled self-mute. | member |
| `voice_self_mute_disable` | fires on when someone disabled self-mute. | member |
| `voice_guild_mute_update` | fires on when someone guild-muted/guild-unmuted. | member |
| `voice_guild_mute_enable` | fires on when someone enabled guild-mute. | member |
| `voice_guild_mute_disable` | fires on when someone disabled guild-mute. | member |
| `voice_deaf_update` | fires on when someone enabled/disabled self-deaf/guild-deaf. | member |
| `voice_deaf_enable` | fires on when someone enabled self-mute/guild-mute. | member |
| `voice_deaf_disable` | fires on when someone disabled self-mute/guild-mute. | member |
| `voice_self_deaf_update` | fires on when someone enabled/disabled self-deaf. | member |
| `voice_self_deaf_enable` | fires on when someone enabled self-deaf. | member |
| `voice_self_deaf_disable` | fires on when someone disabled self-deaf. | member |
| `voice_guild_deaf_update` | fires on when someone enabled/disabled guild-deaf. | member |
| `voice_guild_deaf_enable` | fires on when someone enabled guild-deaf. | member |
| `voice_guild_deaf_disable` | fires on when someone disabled guild-deaf. | member |
| `voice_stream_update` | fires on when someone started/ended stream. | member |
| `voice_stream_start` | fires on when someone started stream. | member |
| `voice_stream_end` | fires on when someone ended stream. | member |
| `voice_video_update` | fires on when someone started/ended video. | member |
| `voice_video_start` | fires on when someone started video. | member |
| `voice_video_end` | fires on when someone ended video. | member |

## Suffixes

`(event)_me`: when client did. member argument will be ignored.  
`(event)_bot`: when bot did.  
`(event)_other_bot`: when bot did(without client).  
`(event)_user`: when user did(not bot).
