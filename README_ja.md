<p style="font-size: 2rem"><a href="https://github.com/sevenc-nanashi/dpy-peper/blob/main/README.md">English</a>/Japanese</p>

[![PyPI - Version](https://img.shields.io/pypi/v/dpy-peper?style=flat-square)](https://pypi.org/project/dpy-peper) [![PyPI - Downloads](https://img.shields.io/badge/dynamic/json?style=flat-square&label=downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2Fdpy-peper)](https://pepy.tech/project/dpy-peper/)

# peper

peper = <small>d</small>**p**<small>y-voic</small>**e**<small>-hel</small>**per**  
discord.pyのon_voice_state_updateのラッパー。

# 使い方

`python3 -m pip install dpy-peper`

## extensionとして使う

`load_extension`で読み込んで下さい。

```python
from discord.ext import commands

bot = commands.Bot(command_prefix='/')
bot.load_extension('dpy_peper')
# または
# bot.load_extension('discord.ext.peper')
bot.run("Th1sIsN0tT0k3n.B3cause.1fiShowB0tWillG3tH4cked")
```

## Cogとして使う

`VoiceWrapper`をインポートして下さい。

```python
from discord.ext import commands
from dpy_peper import VoiceWrapper
# または
# from discord.ext.peper import VoiceWrapper
bot = commands.Bot(command_prefix='/')
bot.add_cog(VoiceWrapper(bot))
bot.run("Th1sIsN0tT0k3n.B3cause.1fiShowB0tWillG3tH4cked")
```

# イベント

|名前|説明|引数|
|----|-----------|---------|
| `voice_channel_update` | 誰かがVCに接続/移動/切断したときに発火します。 | member, before_channel, after_channel |
| `voice_channel_connect` | 誰かがVCに接続したときに発火します。 | member, channel |
| `voice_channel_move` | 誰かがVCに移動したときに発火します。 | member, before_channel, after_channel |
| `voice_channel_disconnect` | 誰かがVCから切断したときに発火します。 | member, channel |
| `voice_channel_afk` | 誰かがAFKのVCに接続したときに発火します。 | member, before_channel |
| `voice_channel_alone` | 誰かがVCから切断し、1人だけが残っているときに発火します。 | member, channel |
| `voice_mute_update` | 誰かのミュート状態が変わったときに発火します。（サーバーミュート含む） | member |
| `voice_mute_enable` | 誰かがミュートしたときに発火します。（サーバーミュート含む） | member |
| `voice_mute_disable` | 誰かがミュートを解除したときに発火します。（サーバーミュート含む） | member |
| `voice_self_mute_update` | 誰かのミュート状態が変わったときに発火します。（サーバーミュート以外） | member |
| `voice_self_mute_enable` | 誰かがミュートしたときに発火します。（サーバーミュート以外） | member |
| `voice_self_mute_disable` | 誰かがミュートを解除したときに発火します。（サーバーミュート以外） | member |
| `voice_guild_mute_update` | 誰かのサーバーミュート状態が変わったときに発火します。 | member |
| `voice_guild_mute_enable` | 誰かがサーバーミュートされたときに発火します。 | member |
| `voice_guild_mute_disable` | 誰かのサーバーミュートが解除されたときに発火します。 | member |
| `voice_deaf_update` | 誰かのスピーカーミュート状態が変わったときに発火します。（サーバー側スピーカーミュート含む） | member |
| `voice_deaf_enable` | 誰かがスピーカーミュートしたときに発火します。（サーバー側スピーカーミュート含む） | member |
| `voice_deaf_disable` | 誰かのスピーカーミュートが解除されたときに発火します。（サーバー側スピーカーミュート含む） | member |
| `voice_self_deaf_update` | 誰かのスピーカーミュート状態が変わったときに発火します。（サーバー側スピーカーミュート以外） | member |
| `voice_self_deaf_enable` | 誰かがスピーカーミュートしたときに発火します。（サーバー側スピーカーミュート以外） | member |
| `voice_self_deaf_disable` | 誰かのスピーカーミュートが解除されたときに発火します。（サーバー側スピーカーミュート以外） | member |
| `voice_guild_deaf_update` | 誰かのサーバー側スピーカーミュート状態が変わったときに発火します。 | member |
| `voice_guild_deaf_enable` | 誰かがサーバー側スピーカーミュートされたときに発火します。 | member |
| `voice_guild_deaf_disable` | 誰かのサーバー側スピーカーミュートが解除されたときに発火します。 | member |
| `voice_stream_update` | 誰かが配信を開始/終了したときに発火します。 | member |
| `voice_stream_start` | 誰かが配信を開始したときに発火します。 | member |
| `voice_stream_end` | 誰かが配信を終了したときに発火します。 | member |
| `voice_video_update` | 誰かがビデオ共有を開始/終了したときに発火します。 | member |
| `voice_video_start` | 誰かがビデオ共有を開始したときに発火します。 | member |
| `voice_video_end` | 誰かがビデオ共有を終了したときに発火します。 | member |

## 追加イベント

`(event)_me`: クライアントが発火させたとき。（member引数は省略されます。）  
`(event)_bot`: Botが発火させたとき。  
`(event)_other_bot`: クライアント以外のBotが発火させたとき。  
`(event)_user`: ユーザーが発火させたとき。
