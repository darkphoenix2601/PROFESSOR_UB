# credit goes to Ultroid userbot
#modified by @D3_krish

from telethon.utils import get_input_document
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetID, InputStickerSetShortName

from . import *


@bot.on(d3vil_cmd(pattern="stspam$"))
async def _(e):
    x = await e.get_reply_message()
    if not (x and x.media and hasattr(x.media, "document")):
        return await eod(e, "`Reply To Sticker Only`")
    set = x.document.attributes[1]
    sset = await e.client(
        GetStickerSetRequest(
            InputStickerSetID(
                id=set.stickerset.id,
                access_hash=set.stickerset.access_hash,
            )
        )
    )
    pack = sset.set.short_name
    docs = [
        get_input_document(x)
        for x in (
            await e.client(GetStickerSetRequest(InputStickerSetShortName(pack)))
        ).documents
    ]
    for xx in docs:
        await e.respond(file=(xx))

CmdHelp("stickerspam").add_command(
  "stspam", "sticker/reply ", "it spam the whole stickers in that pack."
).add()
