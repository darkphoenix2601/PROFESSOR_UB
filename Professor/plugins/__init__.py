import datetime
from Professor import *
from Professor.config import Config
from Professor.helpers import *
from Professor.utils import *
from Professor.random_strings import *
from Professor.version import __d3vil__
from telethon import version


D3VIL_USER = bot.me.first_name
d3krish = bot.uid
d3vil_mention = f"[{D3VIL_USER}](tg://user?id={d3krish})"
d3vil_logo = "./resources/Pics/d3vilkrish_logo.jpg"
cjb = "./resources/Pics/cjb.jpg"
restlo = "./resources/Pics/rest.jpeg"
shuru = "./resources/Pics/shuru.jpg"
hl = Config.HANDLER
shl = Config.SUDO_HANDLER
d3vil_ver = __d3vil__
tel_ver = version.__version__
update_logo = "https://telegra.ph/file/252f9c8a46b29ee1bca1e.jpg"

async def get_user_id(ids):
    if str(ids).isdigit():
        userid = int(ids)
    else:
        userid = (await bot.get_entity(ids)).id
    return userid

sudos = Config.SUDO_USERS
if sudos:
    is_sudo = "True"
else:
    is_sudo = "False"

abus = Config.ABUSE
if abus == "ON":
    abuse_m = "Enabled"
else:
    abuse_m ="Disabled"

START_TIME = datetime.datetime.now()
uptime = f"{str(datetime.datetime.now() - START_TIME).split('.')[0]}"
my_channel = Config.MY_CHANNEL or "D3VIL_BOT_OFFICIAL"
my_group = Config.MY_GROUP or "D3VIL_BOT_SUPPORT"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

chnl_link = "https://t.me/D3VIL_BOT_OFFICIAL"
d3vil_channel = f"[тнε ᗪ3vιℓ υρ∂αтεs]({chnl_link})"
grp_link = "https://t.me/D3VIL_BOT_SUPPORT"
d3vil_grp = f"[тнε ᗪ3vιℓ cнαт]({grp_link})"

WELCOME_FORMAT = """**Use these fomats in your welcome note to make them attractive.**
  {mention} :  To mention the user
  {title} : To get chat name in message
  {count} : To get group members
  {first} : To use user first name
  {last} : To use user last name
  {fullname} : To use user full name
  {userid} : To use userid
  {username} : To use user username
  {my_first} : To use my first name
  {my_fullname} : To use my full name
  {my_last} : To use my last name
  {my_mention} : To mention myself
  {my_username} : To use my username
"""
# will add more soon


