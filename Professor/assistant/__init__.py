from . import *
from telethon import Button, custom

from Professor import bot

from Professor import *
OWNER_NAME = "{d3vil_mention}"
OWNER_ID = bot.uid


D3VIL_USER = bot.me.first_name
d3krish = bot.uid

d3vil_mention = f"[{D3VIL_USER}](tg://user?id={d3krish})"

d3vil_logo = "./resources/Pics/d3vilkrish_logo.jpg"
d3vil_logo1 = "./resources/Pics/d3vilkrish_logo.jpg"
d3vil_logo2 = "./resources/Pics/d3vilbot_logo.jpg"
d3vil_logo3 = "./resources/Pics/d3vilbot_logo.jpg"
d3vil_logo4 = "./resources/Pics/d3vilkrish_logo.jpg"
D3VILversion = "2.𝙾"

perf = "[ 𝚃𝙷𝙴 𝙳3𝚅𝙸𝙻𝙱𝙾𝚃 ]"


DEVLIST = [
    "1676629806"
]

async def setit(event, name, value):
    try:
        event.set(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    button = [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
    return button
