from math import ceil
from re import compile
import asyncio
import html
import os
import re
import sys

from telethon import Button, custom, events, functions
from telethon.tl.functions.users import GetFullUserRequest
from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ExportChatInviteRequest

from . import *

d3vil_row = Config.BUTTONS_IN_HELP
d3vil_emoji = Config.EMOJI_IN_HELP
d3vil_pic = Config.PMPERMIT_PIC or "https://telegra.ph/file/ad8abbfbcb2f93f91b10f.jpg"
cstm_pmp = Config.CUSTOM_PMPERMIT
ALV_PIC = Config.ALIVE_PIC

PM_WARNS = {}
PREV_REPLY_MESSAGE = {}

mybot = Config.BOT_USERNAME
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"
LOG_GP = Config.LOGGER_ID
mssge = (
    str(cstm_pmp)
    if cstm_pmp
    else "**𝖸𝗈𝗎 𝖧𝖺𝗏𝖾 𝖳𝗋𝖾𝗌𝗉𝖺𝗌𝗌𝖾𝖽 𝖳𝗈 𝖬𝗒 𝖬𝖺𝗌𝗍𝖾𝗋'𝗌 𝖯𝖬!\n𝖳𝗁𝗂𝗌 𝖨𝗌 𝖨𝗅𝗅𝖾𝗀𝖺𝗅 𝖠𝗇𝖽 𝖱𝖾𝗀𝖺𝗋𝖽𝖾𝖽 𝖠𝗌 𝖢𝗋𝗂𝗆𝖾.**"
)

USER_BOT_WARN_ZERO = "𝖸𝗈𝗎 𝗐𝖾𝗋𝖾 𝗌𝗉𝖺𝗆𝗆𝗂𝗇𝗀 𝗆𝗒 𝗌𝗐𝖾𝖾𝗍 𝗆𝖺𝗌𝗍𝖾𝗋'𝗌 𝗂𝗇𝖻𝗈𝗑, 𝗁𝖾𝗇𝖼𝖾𝖿𝗈𝗋𝗍𝗁 𝗒𝗈𝗎 𝗁𝖺𝗏𝖾 𝖻𝖾𝖾𝗇 𝖻𝗅𝗈𝖼𝗄𝖾𝖽 𝖻𝗒 𝗆𝗒 𝗆𝖺𝗌𝗍𝖾𝗋'𝗌 𝖣3𝗏𝗂𝗅𝖡𝗈𝗍.**\n__𝖭𝗈𝗐 𝖦𝖳𝖥𝖮, 𝗂'𝗆 𝖻𝗎𝗌𝗒**"

D3VIL_FIRST = (
    "**Hello, 𝖳𝗁𝗂𝗌 𝗂𝗌 ᗪ3ᏉᎥᏝᏰᎧᏖ 𝖴𝗅𝗍𝗋𝖺 𝖯𝗋𝗂𝗏𝖺𝗍𝖾 𝖲𝖾𝖼𝗎𝗋𝗂𝗍𝗒 𝖯𝗋𝗈𝗍𝗈𝖼𝗈𝗅⚠️ **\n 𝖳𝗁𝗂𝗌 𝗂𝗌 𝗍𝗈 𝗂𝗇𝖿𝗈𝗋𝗆 𝗒𝗈𝗎 𝗍𝗁𝖺𝗍 "
    "{} 𝗂𝗌 𝖼𝗎𝗋𝗋𝖾𝗇𝗍𝗅𝗒 𝗎𝗇𝖺𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾. 𝖳𝗁𝗂𝗌 𝗂𝗌 𝖺𝗇 𝖺𝗎𝗍𝗈𝗆𝖺𝗍𝖾𝖽 𝗆𝖾𝗌𝗌𝖺𝗀𝖾.\n\n"
    "{}\n\n**𝖯𝗅𝖾𝖺𝗌𝖾 𝖢𝗁𝗈𝗈𝗌𝖾 𝖶𝗁𝗒 𝖸𝗈𝗎 𝖠𝗋𝖾 Inbox 👇!!**".format(d3vil_mention, mssge))

alive_txt = """
**⚜️ 𝐃3𝐕𝐈𝐋𝐁𝐎𝐓 𝐈𝐒 𝐎𝐍𝐋𝐈𝐍𝐄 ⚜️**
{}
**↼𝗠𝗔𝗦𝗧𝗘𝗥⇀   :**     **『{}』**
**╔══════════════════╗
**╠➳➠ 𝗧𝗲𝗹𝗲𝘁𝗵𝗼𝗻 :**  `{}`
**╠➳➠ 𝗗3𝗩𝗜𝗟𝗕𝗢𝗧  :**  **{}**
**╠➳➠ 𝗨𝗽𝘁𝗶𝗺𝗲   :**  `{}`
**╠➳➠ 𝗔𝗯𝘂𝘀𝗲    :**  **{}**
**╠➳➠ 𝗦𝘂𝗱𝗼      :**  **{}**
**╚══════════════════╝
"""

def button(page, modules):
    Row = d3vil_row
    Column = 3

    modules = sorted([modul for modul in modules if not modul.startswith("_")])
    pairs = list(map(list, zip(modules[::3], modules[1::3])))
    if len(modules) % 2 == 1:
        pairs.append([modules[-1]])
    max_pages = ceil(len(pairs) / Row)
    pairs = [pairs[i : i + Row] for i in range(0, len(pairs), Row)]
    buttons = []
    for pairs in pairs[page]:
        buttons.append(
            [
                custom.Button.inline(f"{d3vil_emoji} " + pair + f" {d3vil_emoji}", data=f"Information[{page}]({pair})")
                for pair in pairs
            ]
        )

    buttons.append(
        [
            custom.Button.inline(
               f"☜︎︎︎ 𝙱𝙰𝙲𝙺༆ {d3vil_emoji}", data=f"page({(max_pages - 1) if page == 0 else (page - 1)})"
            ),
            custom.Button.inline(
               f"• ✘ •", data="close"
            ),
            custom.Button.inline(
               f"{d3vil_emoji} ༆𝙽𝙴𝚇𝚃 ☞︎︎︎", data=f"page({0 if page == (max_pages - 1) else page + 1})"
            ),
        ]
    )
    return [max_pages, buttons]


    modules = CMD_HELP
if Config.BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query == "d3vilbot_d3vlp":
            rev_text = query[::-1]
            veriler = button(0, sorted(CMD_HELP))
            apn = []
            for x in CMD_LIST.values():
                for y in x:
                    apn.append(y)
            result = await builder.article(
                f"Hey! Only use .help please",
                text=f"**『{d3vil_mention}』**\n\n📜 __No.of Plugins__ : `{len(CMD_HELP)}` \n🗂️ __Commands__ : `{len(apn)}`\n🗒️ __Page__ : 1/{veriler[0]}",
                buttons=veriler[1],
                link_preview=False,
            )
        elif event.query.user_id == bot.uid and query.startswith("fsub"):
            hunter = event.pattern_match.group(1)
            d3vil = hunter.split("+")
            user = await bot.get_entity(int(d3vil[0]))
            channel = await bot.get_entity(int(d3vil[1]))
            msg = f"**👋 𝗐𝖾𝗅𝖼𝗈𝗆𝖾** [{user.first_name}](tg://user?id={user.id}), \n\n** 𝖸𝗈𝗎 𝗇𝖾𝖾𝖽 𝗍𝗈 𝖩𝗈𝗂𝗇** {channel.title} **𝗍𝗈 𝖼𝗁𝖺𝗍 𝗂𝗇 𝗍𝗁𝗂𝗌 𝗀𝗋𝗈𝗎𝗉.**"
            if not channel.username:
                link = (await bot(ExportChatInviteRequest(channel))).link
            else:
                link = "https://t.me/" + channel.username
            result = [
                await builder.article(
                    title="force_sub",
                    text = msg,
                    buttons=[
                        [Button.url(text="Channel", url=link)],
                        [custom.Button.inline("🔓 𝖴𝗇𝗆𝗎𝗍𝖾 𝖬𝖾", data=unmute)],
                    ],
                )
            ]

        elif event.query.user_id == bot.uid and query == "alive":
            kr_ish = alive_txt.format(Config.ALIVE_MSG, d3vil_mention, tel_ver, d3vil_ver, uptime, abuse_m, is_sudo)
            alv_btn = [
                [Button.url(f"{D3VIL_USER}", f"tg://openmessage?user_id={d3krish}")],
                [Button.url("𝖬𝗒 𝖢𝗁𝖺𝗇𝗇𝖾𝗅", f"https://t.me/{my_channel}"), 
                Button.url("𝖬𝗒 𝖦𝗋𝗈𝗎𝗉", f"https://t.me/{my_group}")],
            ]
            if ALV_PIC and ALV_PIC.endswith((".jpg", ".png")):
                result = builder.photo(
                    ALV_PIC,
                    text=kr_ish,
                    buttons=alv_btn,
                    link_preview=False,
                )
            elif ALV_PIC:
                result = builder.document(
                    ALV_PIC,
                    text=kr_ish,
                    title="D3vilBot Alive",
                    buttons=alv_btn,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    text=kr_ish,
                    title="D3vilBot Alive",
                    buttons=alv_btn,
                    link_preview=False,
                )

        elif event.query.user_id == bot.uid and query == "pm_warn":
            d3vl_l = D3VIL_FIRST.format(d3vil_mention, mssge)
            result = builder.photo(
                file=d3vil_pic,
                text=d3vl_l,
                buttons=[
                    [
                        custom.Button.inline("🚫 𝖲𝗉𝖺𝗆/𝖲𝖼𝖺𝗆 🚫", data="teamd3"),
                        custom.Button.inline("💬 𝖢𝗁𝖺𝗍 💬", data="chat"),
                    ],
                    [custom.Button.inline("📝 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 📝", data="req")],
                    [custom.Button.inline("𝖢𝗎𝗋𝗂𝗈𝗎𝗌 ❓", data="pmclick")],
                ],
            )

        elif event.query.user_id == bot.uid and query == "repo":
            result = builder.article(
                title="Repository",
                text=f"**[⚜️ 𝙻𝙴𝙶𝙴𝙽𝙳𝙰𝚁𝚈 𝙰𝙵 𝚃𝙴𝙰𝙼 𝙳3𝚅𝙸𝙻 ⚜️](https://t.me/D3VIL_BOT_OFFICIAL)**",
                buttons=[
                    [Button.url("📑 𝖱𝖾𝗉𝗈 📑", "https://github.com/TEAM-D3VIL/D3vilBot")],
                    [Button.url("🚀 𝖣𝖾𝗉𝗅𝗈𝗒 🚀", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FTEAM-D3VIL%2FD3vilBot&template=https%3A%2F%2Fgithub.com%2FTEAM-D3VIL%2FD3vilBot")],
                    [Button.url("✵ 𝖮𝗐𝗇𝖾𝗋 ✵", "https://t.me/D3_krish")],
                ],
            )

        elif query.startswith("http"):
            part = query.split(" ")
            result = builder.article(
                "File uploaded",
                text=f"**𝖥𝗂𝗅𝖾 𝗎𝗉𝗅𝗈𝖺𝖽𝖾𝖽 𝗌𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒 𝗍𝗈 {part[2]} site.\𝗇𝖴𝗉𝗅𝗈𝖽𝖾𝖽 𝖳𝗂𝗆𝖾 : {part[1][:3]} 𝗌𝖾𝖼𝗈𝗇𝖽\n[‏‏‎ ‎]({part[0]})",
                buttons=[[custom.Button.url("URL", part[0])]],
                link_preview=True,
            )

        else:
            result = builder.article(
                "D3VIL_BOT_OFFICIAL",
                text="""**𝖧𝖾𝗒! 𝖳𝗁𝗂𝗌 𝗂𝗌 [✘•𝙳3𝚅𝙸𝙻𝙱𝙾𝚃•✘](https://t.me/D3VIL_OP_BOLTE)  \𝗇𝖸𝗈𝗎 𝖼𝖺𝗇 𝗄𝗇𝗈𝗐 𝗆𝗈𝗋𝖾 𝖺𝖻𝗈𝗎𝗍 𝗆𝖾 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝗅𝗂𝗇𝗄𝗌 𝗀𝗂𝗏𝖾𝗇 𝖻𝖾𝗅𝗈𝗐 👇**""",
                buttons=[
                    [
                        custom.Button.url("🔥 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 🔥", "https://t.me/D3VIL_BOT_OFFICIAL"),
                        custom.Button.url(
                            "⚡ 𝙶𝚁𝙾𝚄𝙿 ⚡", "https://t.me/D3VIL_BOT_SUPPORT"
                        ),
                    ],
                    [
                        custom.Button.url(
                            "✨ 𝚁𝙴𝙿𝙾 ✨", "https://github.com/D3KRISH/D3vilBot"),
                        custom.Button.url
                    (
                            "🔰 𝙾𝚆𝙽𝙴𝚁 🔰", "https://t.me/D3_krish"
                    )
                    ],
                ],
                link_preview=False,
            )
        await event.answer([result] if result else None)


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"pmclick")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "𝖳𝗁𝗂𝗌 𝗂𝗌 𝖿𝗈𝗋 𝖮𝗍𝗁𝖾𝗋 𝖴𝗌𝖾𝗋𝗌..."
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f" 𝖳𝗁𝗂𝗌 𝗂𝗌 ᗪ3ᏉᎥᏝᏰᎧᏖ𝖯𝗆 𝖲𝖾𝖼𝗎𝗋𝗂𝗍𝗒 𝖿𝗈𝗋 {d3vil_mention} 𝗍𝗈 𝗄𝖾𝖾𝗉 𝖺𝗐𝖺𝗒 𝗎𝗇𝗐𝖺𝗇𝗍𝖾𝖽 𝗋𝖾𝗍𝖺𝗋𝖽𝗌 𝖿𝗋𝗈𝗆 𝗌𝗉𝖺𝗆𝗆𝗂𝗇𝗀 𝖯𝖬..."
            )

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"req")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "𝖳𝗁𝗂𝗌 𝗂𝗌 𝖿𝗈𝗋 𝗈𝗍𝗁𝖾𝗋 𝗎𝗌𝖾𝗋𝗌!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"✅ **𝖱𝖾𝗊𝗎𝖾𝗌𝗍 𝖱𝖾𝗀𝗂𝗌𝗍𝖾𝗋𝖾𝖽** \n\n{d3vil_mention} 𝗐𝗂𝗅𝗅 𝗇𝗈𝗐 𝖽𝖾𝖼𝗂𝖽𝖾 𝗍𝗈 𝗅𝗈𝗈𝗄 𝖿𝗈𝗋 𝗒𝗈𝗎𝗋 𝗋𝖾𝗊𝗎𝖾𝗌𝗍 𝗈𝗋 𝗇𝗈𝗍.\n😐 𝖳𝗂𝗅𝗅 𝗍𝗁𝖾𝗇 𝗐𝖺𝗂𝗍 𝖺𝗇𝖽 𝖽𝗈𝗇'𝗍 𝗌𝗉𝖺𝗆!!"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            ok = event.query.user_id
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"**👀 𝖧𝖾𝗒 {d3vil_mention} !!** \n\n⚜️ 𝖸𝗈𝗎 𝖦𝗈𝗍 𝖠 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 𝖥𝗋𝗈𝗆 [{first_name}](tg://user?id={ok}) 𝖨𝗇 𝖯𝗆!!"
            await bot.send_message(LOG_GP, tosend)


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"chat")))
    async def on_pm_click(event):
        event.query.user_id
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "𝖳𝗁𝗂𝗌 𝗂𝗌 𝖿𝗈𝗋 𝗈𝗍𝗁𝖾𝗋 𝗎𝗌𝖾𝗋𝗌!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"𝖠𝗁𝗁!! 𝖸𝗈𝗎 𝗁𝖾𝗋𝖾 𝗍𝗈 𝖽𝗈 chat!!\𝗇𝖯𝗅𝖾𝖺𝗌𝖾 𝗐𝖺𝗂𝗍 𝖿𝗈𝗋 {d3vil_mention} 𝗍𝗈 𝖼𝗈𝗆𝖾. 𝖳𝗂𝗅𝗅 𝗍𝗁𝖾𝗇 𝗄𝖾𝖾𝗉 𝗉𝖺𝗍𝗂𝖾𝗇𝖼𝖾 𝖺𝗇𝖽 𝖽𝗈𝗇'𝗍 𝗌𝗉𝖺𝗆."
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            ok = event.query.user_id
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"**👀 𝖧𝖾𝗒 {d3vil_mention} !!** \n\n⚜️ 𝖸𝗈𝗎 𝖦𝗈𝗍 𝖠 𝖯𝖬 𝖿𝗋𝗈𝗆  [{first_name}](tg://user?id={ok})  𝖿𝗈𝗋 𝗋𝖺𝗇𝖽𝗈𝗆 𝖼𝗁𝖺𝗍𝗌!!"
            await bot.send_message(LOG_GP, tosend)


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"teamd3")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "𝖳𝗁𝗂𝗌 𝗂𝗌 𝖿𝗈𝗋 𝗈𝗍𝗁𝖾𝗋 𝗎𝗌𝖾𝗋𝗌!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"🥴 **𝖭𝗂𝗄𝖺𝗅 𝗆𝖺𝖽𝖾𝗋𝖼𝗁𝗈𝖽\n𝖯𝖾𝗁𝗅𝗂 𝖿𝗎𝗋𝗌𝖺𝗍 𝗆𝖾 𝗇𝗂𝗄𝖺𝗅**"
            )
            await bot(functions.contacts.BlockRequest(event.query.user_id))
            target = await event.client(GetFullUserRequest(event.query.user_id))
            ok = event.query.user_id
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            first_name = html.escape(target.user.first_name)
            await bot.send_message(
                LOG_GP,
                f"**𝖡𝗅𝗈𝖼𝗄𝖾𝖽**  [{first_name}](tg://user?id={ok}) \n\𝗇𝖱𝖾𝖺𝗌𝗈𝗇:- 𝖲𝗉𝖺𝗆",
            )


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"unmute")))
    async def on_pm_click(event):
        hunter = (event.data_match.group(1)).decode("UTF-8")
        d3vil = hunter.split("+")
        if not event.sender_id == int(d3vil[0]):
            return await event.answer("𝖳𝗁𝗂𝗌 𝖠𝗂𝗇'𝗍 𝖥𝗈𝗋 𝖸𝗈𝗎!!", alert=True)
        try:
            await bot(GetParticipantRequest(int(d3vil[1]), int(d3vil[0])))
        except UserNotParticipantError:
            return await event.answer(
                "You need to join the channel first.", alert=True
            )
        await bot.edit_permissions(
            event.chat_id, int(d3vil[0]), send_message=True, until_date=None
        )
        await event.edit("𝖸𝖺𝗒! 𝖸𝗈𝗎 𝖼𝖺𝗇 𝖼𝗁𝖺𝗍 𝗇𝗈𝗐 !!")


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"reopen")))
    async def reopn(event):
            if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
                current_page_number=0
                simp = button(current_page_number, CMD_HELP)
                veriler = button(0, sorted(CMD_HELP))
                apn = []
                for x in CMD_LIST.values():
                    for y in x:
                        apn.append(y)
                await event.edit(
                    f"**『{d3vil_mention}』**\n\n📜 __No.of Plugins__ : `{len(CMD_HELP)}` \n🗂️ __Commands__ : `{len(apn)}`\n🗒️ __Page__ : 1/{veriler[0]}",
                    buttons=simp[1],
                    link_preview=False,
                )
            else:
                reply_pop_up_alert = "𝖧𝗈𝗈 𝗀𝗒𝖺 𝖺𝗉𝗄𝖺. 𝖪𝖺𝖻𝗌𝖾 𝗍𝖺𝗉𝖺𝗋 𝗍𝖺𝗉𝖺𝗋 𝖽𝖺𝖻𝖺𝖾 𝗃𝖺𝖺 𝗋𝗁𝖾 𝗁. 𝗄𝗁𝗎𝖽𝗄𝖺 𝖻𝗇𝖺 𝗅𝗈 𝗇𝖺 𝖺𝗀𝗋 𝖼𝗁𝗂𝗒𝖾 𝗍𝗂. © ᗪ3ᏉᎥᏝᏰᎧᏖ™"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            veriler = custom.Button.inline(f"{d3vil_emoji} Re-Open Menu {d3vil_emoji}", data="reopen")
            await event.edit(f"**⚜️ ᗪ3vιℓвσт 𝖬êñû 𝖯𝗋õ𝗏î𝖽ê𝗋 ì𝗌 ñô𝗐 Ç𝗅ö𝗌ë𝖽 ⚜️**\n\n**𝖬𝖺𝗌𝗍𝖾𝗋 :**  {d3vil_mention}\n\n        [©️ ᗪ3ᏉᎥᏝᏰᎧᏖ™️]({chnl_link})", buttons=veriler, link_preview=False)
        else:
            reply_pop_up_alert = "𝖧𝖾𝗅𝗅𝗈 𝗍𝗁𝖾𝗋𝖾 𝖣𝖾𝗉𝗅𝗈𝗒 𝗒𝗈𝗎𝗋 𝗈𝗐𝗇 𝖣3𝖵𝖨𝖫𝖡𝖮𝖳 𝖺𝗇𝖽 𝗎𝗌𝖾. © ᗪ3ᏉᎥᏝᏰᎧᏖ™"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
   

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"page\((.+?)\)")))
    async def page(event):
        page = int(event.data_match.group(1).decode("UTF-8"))
        veriler = button(page, CMD_HELP)
        apn = []
        for x in CMD_LIST.values():
            for y in x:
                apn.append(y)
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            await event.edit(
                f" **『{d3vil_mention}』**\n\n📜 __No.of Plugins__ : `{len(CMD_HELP)}` \n🗂️ __Commands__ : `{len(apn)}`\n🗒️ __Page__ : 1/{veriler[0]}",
                buttons=veriler[1],
                link_preview=False,
            )
        else:
            return await event.answer(
                "𝖧𝖾𝗅𝗅𝗈 𝗍𝗁𝖾𝗋𝖾 𝖣𝖾𝗉𝗅𝗈𝗒 𝗒𝗈𝗎𝗋 𝗈𝗐𝗇 𝖣3𝖵𝖨𝖫𝖡𝖮𝖳 𝖺𝗇𝖽 𝗎𝗌𝖾. © ᗪ3ᏉᎥᏝᏰᎧᏖ™",
                cache_time=0,
                alert=True,
            )


    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"Information\[(\d*)\]\((.*)\)"))
    )
    async def Information(event):
        page = int(event.data_match.group(1).decode("UTF-8"))
        commands = event.data_match.group(2).decode("UTF-8")
        try:
            buttons = [
                custom.Button.inline(
                    "✘ " + cmd[0] + " ✘", data=f"commands[{commands}[{page}]]({cmd[0]})"
                )
                for cmd in CMD_HELP_BOT[commands]["commands"].items()
            ]
        except KeyError:
            return await event.answer(
                "𝖭𝗈 𝖣𝖾𝗌𝖼𝗋𝗂𝗉𝗍𝗂𝗈𝗇 𝗂𝗌 𝗐𝗋𝗂𝗍𝗍𝖾𝗇 𝖿𝗈𝗋 𝗍𝗁𝗂𝗌 𝗉𝗅𝗎𝗀𝗂𝗇", cache_time=0, alert=True
            )

        buttons = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]
        buttons.append([custom.Button.inline(f"{d3vil_emoji} Main Menu {d3vil_emoji}", data=f"page({page})")])
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            await event.edit(
                f"**📗 𝖥𝗂𝗅𝖾 :**  `{commands}`\n**🔢 𝖭𝗎𝗆𝖻𝖾𝗋 𝗈𝖿 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌 :**  `{len(CMD_HELP_BOT[commands]['commands'])}`",
                buttons=buttons,
                link_preview=False,
            )
        else:
            return await event.answer(
                "𝖧𝖾𝗅𝗅𝗈 𝗍𝗁𝖾𝗋𝖾 𝖣𝖾𝗉𝗅𝗈𝗒 𝗒𝗈𝗎𝗋 𝗈𝗐𝗇 𝖣3𝖵𝖨𝖫𝖡𝖮𝖳 𝖺𝗇𝖽 𝗎𝗌𝖾. © ᗪ3ᏉᎥᏝᏰᎧᏖ™",
                cache_time=0,
                alert=True,
            )


    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"commands\[(.*)\[(\d*)\]\]\((.*)\)"))
    )
    async def commands(event):
        cmd = event.data_match.group(1).decode("UTF-8")
        page = int(event.data_match.group(2).decode("UTF-8"))
        commands = event.data_match.group(3).decode("UTF-8")
        result = f"**📗 𝖥𝗂𝗅𝖾 :**  `{cmd}`\n"
        if CMD_HELP_BOT[cmd]["info"]["info"] == "":
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**⚠️ 𝖶𝖺𝗋𝗇𝗂𝗇𝗀 :**  {CMD_HELP_BOT[cmd]['info']['warning']}\n\n"
        else:
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**⚠️ 𝖶𝖺𝗋𝗇𝗂𝗇𝗀 :**  {CMD_HELP_BOT[cmd]['info']['warning']}\n"
            result += f"**ℹ️ 𝖨𝗇𝖿𝗈 :**  {CMD_HELP_BOT[cmd]['info']['info']}\n\n"
        command = CMD_HELP_BOT[cmd]["commands"][commands]
        if command["params"] is None:
            result += f"**🛠 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 :**  `{HANDLER[:1]}{command['command']}`\n"
        else:
            result += f"**🛠 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 :**  `{HANDLER[:1]}{command['command']} {command['params']}`\n"
        if command["example"] is None:
            result += f"**💬 𝖤𝗑𝗉𝗅𝖺𝗇𝖺𝗍𝗂𝗈𝗇 :**  `{command['usage']}`\n\n"
        else:
            result += f"**💬 𝖤𝗑𝗉𝗅𝖺𝗇𝖺𝗍𝗂𝗈𝗇 :**  `{command['usage']}`\n"
            result += f"**⌨️ 𝖥𝗈𝗋 𝖤𝗑𝖺𝗆𝗉𝗅𝖾 :**  `{HANDLER[:1]}{command['example']}`\n\n"
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            await event.edit(
                result,
                buttons=[
                    custom.Button.inline(f"{d3vil_emoji} Return {d3vil_emoji}", data=f"Information[{page}]({cmd})")
                ],
                link_preview=False,
            )
        else:
            return await event.answer(
                "𝖧𝖾𝗅𝗅𝗈 𝗍𝗁𝖾𝗋𝖾 𝖣𝖾𝗉𝗅𝗈𝗒 𝗒𝗈𝗎𝗋 𝗈𝗐𝗇 𝖣3𝖵𝖨𝖫𝖡𝖮𝖳 𝖺𝗇𝖽 𝗎𝗌𝖾. © ᗪ3ᏉᎥᏝᏰᎧᏖ™",
                cache_time=0,
                alert=True,
            )



