
"""Plugin for mafiaBot Repo
\nCode by @D3_krish
type '.mafiabot' to get mafiaBot repo
"""

from . import *

@borg.on(admin_cmd(pattern="mafiabot ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Click [here](https://github.com/MafiaBotOP/MafiaBot) to open this 🔥**Lit AF!!**🔥 **𝐌𝐀𝐅𝐈𝐀𝐁𝐎𝐓** Repo.. Join channel :- @MafiaBot_Support Repo Uploaded By D3VIL_BOT_OFFICIAL")
    
        
