import asyncio
import datetime

from . import *

PING_PIC = Config.ALIVE_PIC

#@bot.on(d3vil_cmd(pattern="ping$"))
#@bot.on(sudo_cmd(pattern="ping$", allow_sudo=True))
#async def pong(d3vil):
#    if d3vil.fwd_from:
#        return
#    start = datetime.datetime.now()
#    event = await eor(d3vil, "`·.·★ ℘ıŋɠ ★·.·´")
#    end = datetime.datetime.now()
#    ms = (end - start).microseconds / 1000    
#    await event.edit(
#        f"█▀█ █▀█ █▄░█ █▀▀ █\n█▀▀ █▄█ █░▀█ █▄█  ▄\n\n ⚘ ριиg: {ms}\n**⚘ 𝙼𝙰𝚂𝚃𝙴𝚁:** {d3vil_mention}"
#    )

@bot.on(admin_cmd(pattern="ping$", outgoing=True))
@bot.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.datetime.now()
    event = await eor(event, "__**❝❄ᑭ♨ɳց…!❄❞__**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    if PING_PIC:
        d3vil_caption = f"__**〘 ♕ ᑭσɳց! ♕ 〙__**\n\n   ⚘ {ms}\n   ⚘ __**𝙼𝚢**__ __**𝙼𝚊𝚜𝚝𝚎𝚛**__⟿{d3vil_mention}"
        await event.client.send_file(
            event.chat_id, PING_PIC, caption=d3vil_caption
        )
        await event.delete()

CmdHelp("ping").add_command(
  "ping", None, "Checks the ping speed of your 𝔇3𝔳𝔦𝔩𝔅𝔬𝔱"
).add()


