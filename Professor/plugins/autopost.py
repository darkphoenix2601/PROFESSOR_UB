from telethon import events

from Professor.sql.autopost_sql import add_post, get_all_post, is_post, remove_post
from . import *

@bot.on(d3vil_cmd(pattern="autopost ?(.*)"))
@bot.on(sudo_cmd(pattern="autopost ?(.*)", allow_sudo=True))
async def _(event):
    if (event.is_private or event.is_group):
        return await eod(event, "AutoPost Can Only Be Used For Channels.")
    d3vl_ = event.pattern_match.group(1)
    if str(d3vl_).startswith("-100"):
        kk = str(d3vl_).replace("-100", "")
    else:
        kk = d3vl_
    if not kk.isdigit():
        return await eod(event, "**Please Give Channel ID !!**")
    if is_post(kk , event.chat_id):
        return await eor(event, "This Channel Is Already In AutoPost Database.")
    add_post(kk, event.chat_id)
    await eor(event, f"**✔︎ Started AutoPosting from** `{d3vl_}`")


@bot.on(d3vil_cmd(pattern="rmautopost ?(.*)"))
@bot.on(sudo_cmd(pattern="rmautopost ?(.*)", allow_sudo=True))
async def _(event):
    if (event.is_private or event.is_group):
        return await eod(event, "AutoPost Can Only Be Used For Channels.")
    d3vl_ = event.pattern_match.group(1)
    if str(d3vl_).startswith("-100"):
        kk = str(d3vl_).replace("-100", "")
    else:
        kk = d3vl_
    if not kk.isdigit():
        return await eod(event, "**Please Give Channel ID !!**")
    if not is_post(kk, event.chat_id):
        return await eod(event, "I don't think this channel is in AutoPost Database.")
    remove_post(kk, event.chat_id)
    await eor(event, f"**✔︎ Stopped AutoPosting From** `{d3vl_}`")

@bot.on(events.NewMessage())
async def _(event):
    if event.is_private:
        return
    chat_id = str(event.chat_id).replace("-100", "")
    channels_set  = get_all_post(chat_id)
    if channels_set == []:
        return
    for chat in channels_set:
        if event.media:
            await event.client.send_file(int(chat), event.media, caption=event.text)
        elif not event.media:
            await bot.send_message(int(chat), event.message)


CmdHelp("autopost").add_command(
  "autopost", "<channel id>", "Auto Posts every new post from targeted channel to your channel.", "autopost <channelid> [in your channel]"
).add_command(
  "rmautopost", "<channel id>", "Stops AutoPost from targeted autoposting channel."
).add()
