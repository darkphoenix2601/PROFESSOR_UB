from telethon import events
from . import *
#from d3vilbot import YOUR_NAME
from Professor import bot

D3VIL_USER = bot.me.first_name
d3krish = bot.uid
d3vil_mention = f"[{D3VIL_USER}](tg://user?id={d3krish})"

d3vil_pic = Config.ALIVE_PIC or "https://telegra.ph/file/5abfcff75e1930dcdfaf3.mp4"
pm_caption = "  __**🔥🔥𝗗3𝗩𝗜𝗟 𝗔𝗦𝗦𝗜𝗦𝗧𝗔𝗡𝗧 𝗜𝗦 𝗔𝗟𝗜𝗩𝗘🔥🔥**__\n\n"

pm_caption += f"**━━━━━━━━━━━━━━━━━━━━**\n\n"
pm_caption += (
    f"                 ↼𝗠𝗔𝗦𝗧𝗘𝗥⇀\n  **『 {d3vil_mention} 』**\n\n"
)
pm_caption += f"╔══════════════════╗\n"
pm_caption += f"╠•➳➠ `𝖳𝖾𝗅𝖾𝗍𝗁𝗈𝗇:` `1.23.0` \n"
pm_caption += f"╠•➳➠ `𝖵𝖾𝗋𝗌𝗂𝗈𝗇:` `2.0.5`\n"
pm_caption += f"╠•➳➠ `𝖢𝗁𝖺𝗇𝗇𝖾𝗅:` [𝙹𝗈𝗂𝗇](https://t.me/D3VIL_SUPPORT)\n"
pm_caption += f"╠•➳➠ `𝖢𝗋𝖾𝖺𝗍𝗈𝗋:` [𝙳3𝙺𝚁𝙸𝚂𝙷](https://t.me/D3_krish)\n"
pm_caption += f"╠•➳➠ `𝖮𝗐𝗇𝖾𝗋:` [𝙳3𝚅𝙸𝙻𝙶𝚄𝙻𝚂𝙷𝙰𝙽](https://t.me/D3VILGULSHAN)\n"
pm_caption += f"╚══════════════════╝\n"
pm_caption += " [⚡REPO⚡](https://github.com/TEAM-D3VIL/D3vilBot) 🔹 [📜License📜](https://github.com/TEAM-D3VIL/D3vilBot/blob/main/LICENSE)"

@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, d3vil_pic, caption=pm_caption)
