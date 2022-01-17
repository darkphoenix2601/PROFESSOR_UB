import asyncio
import base64
import os

from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from . import *

SUDO_WALA = Config.SUDO_USERS
lg_id = Config.LOGGER_ID

@bot.on(d3vil_cmd(pattern="spam (.*)"))
@bot.on(sudo_cmd(pattern="spam (.*)", allow_sudo=True))
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[6:8])
        spam_message = str(e.text[8:])
        await asyncio.wait([e.respond(spam_message) for i in range(counter)])
        await e.delete()
        await e.client.send_message(
            lg_id, f"#SPAM \n\nSpammed  `{counter}`  messages!!"
        )


@bot.on(d3vil_cmd(pattern="bigspam"))
@bot.on(sudo_cmd(pattern="bigspam", allow_sudo=True))
async def bigspam(d3vil):
    if not d3vil.text[0].isalpha() and d3vil.text[0] not in ("/", "#", "@", "!"):
        d3vil_msg = d3vil.text
        d3vilbot_count = int(d3vil_msg[9:13])
        reply_msg = await d3vil.get_reply_message()
        if reply_msg:
            d3vil_spam = reply_msg
        else:
            d3vil_spam = str(d3vil.text[13:])
        for i in range(1, d3vilbot_count):
            await d3vil.respond(d3vil_spam)
        await d3vil.delete()
        await d3vil.client.send_message(
                lg_id, f"#BIGSPAM \n\nBigspammed  `{d3vil_count}`  messages !!"
        )


@bot.on(d3vil_cmd("dspam (.*)"))
@bot.on(sudo_cmd(pattern="dspam (.*)", allow_sudo=True))
async def spammer(e):
    if e.fwd_from:
        return
    input_str = "".join(e.text.split(maxsplit=1)[1:])
    spamDelay = float(input_str.split(" ", 2)[0])
    counter = int(input_str.split(" ", 2)[1])
    spam_message = str(input_str.split(" ", 2)[2])
    await e.delete()
    for _ in range(counter):
        await e.respond(spam_message)
        await asyncio.sleep(spamDelay)


@bot.on(d3vil_cmd(pattern="uspam ?(.*)"))
@bot.on(sudo_cmd(pattern="uspam ?(.*)", allow_sudo=True))
async def _(event):
    reply_msg = await event.get_reply_message()
    d3vil = event.pattern_match.group(1)
    if reply_msg:
        input_str = reply_msg
    else:
        input_str = d3vil
    await bot.send_message(lg_id, f"#UNLIMITED_SPAM \n\nStarted Unlimited Spam. Will spam till floodwait. Do `{hl}restart` to stop.")
    x = 0
    while x < 69:
        await bot.send_message(event.chat_id, input_str)


# Special Break Spam Module For D3vilBot Made By Chirag Bhargava. & Hellbot owner
# Team D3vilBot
@bot.on(d3vil_cmd(pattern="bspam ?(.*)"))
@bot.on(sudo_cmd(pattern="bspam ?(.*)", allow_sudo=True))
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[7:11])
        reply_msg = await e.get_reply_message()
        if reply_msg:
            spam_message = reply_msg
        else:
            spam_message = str(e.text[12:])
        rd = int(counter % 100)
        tot = int((counter - rd )/100)
        a = 30
        for q in range(tot):
            for p in range(100):
                await asyncio.wait([e.respond(spam_message)])
            a = a + 2
            await asyncio.sleep(a)

        await e.delete()
        await e.client.send_message(
            lg_id, f"#BREAK_SPAM \n\nSpammed  {counter}  messages!!"
        )


@bot.on(d3vil_cmd(pattern="mspam (.*)"))
@bot.on(sudo_cmd(pattern="mspam (.*)", allow_sudo=True))
async def tiny_pic_spam(e):
    sender = await e.get_sender()
    me = await e.client.get_me()
    try:
        await e.delete()
    except:
        pass
    try:
        counter = int(e.pattern_match.group(1).split(" ", 1)[0])
        reply_message = await e.get_reply_message()
        if (
            not reply_message
            or not e.reply_to_msg_id
            or not reply_message.media
            or not reply_message.media
        ):
            return await e.edit("```Reply to a pic/sticker/gif/video message```")
        message = reply_message.media
        for i in range(1, counter):
            await e.client.send_file(e.chat_id, message)
    except:
        return await e.reply(
            f"**Error**\nUsage `{hl}mspam <count> reply to a sticker/gif/photo/video`"
        )


CmdHelp("spam").add_command(
  "spam", "<number> <text>", "Sends the text 'X' number of times.", "spam 99 Hello"
).add_command(
  "mspam", "<reply to media> <number>", "Sends the replied media (gif/ video/ sticker/ pic) 'X' number of times", "mspam 100 <reply to media>"
).add_command(
  "dspam", "<delay> <spam count> <text>", "Sends the text 'X' number of times in 'Y' seconds of delay", "dspam 5 100 Hello"
).add_command(
  "uspam", "<reply to a msg> or <text>", "Spams the message unlimited times until you get floodwait error.", "uspam Hello"
).add_command(
  "bspam", "<count> <text or reply>", "Spams the message X times without floodwait. Breaks the spam count to avoid floodwait.", "bspam 9999 Hello"
).add_command(
  "bigspam", "<count> <text>", "Sends the text 'X' number of times. This what hellbot iz known for. The Best BigSpam Ever", "bigspam 5000 Hello"
).add()
