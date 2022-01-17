import os

from . import *


@bot.on(d3vil_cmd(pattern="mediainfo$"))
@bot.on(sudo_cmd(pattern="mediainfo$", allow_sudo=True))
async def mediainfo(event):
    D3VIL_MEDIA = None
    reply = await event.get_reply_message()
    if not reply:
        return await eod(event, "Reply to a media to fetch info...")
    if not reply.media:
        return await eod(event, "Reply to a media file to fetch info...")
    d3vil = await eor(event, "`Fetching media info...`")
    D3VIL_MEDIA = reply.file.mime_type
    if not D3VIL_MEDIA:
        return await d3vil.edit("Reply to a media file to fetch info...")
    elif D3VIL_MEDIA.startswith(("text")):
        return await d3vil.edit("Reply to a media file to fetch info ...")
    d3vl_ = await mediadata(reply)
    file_path = await reply.download_media(Config.TMP_DOWNLOAD_DIRECTORY)
    out, err, ret, pid = await runcmd(f"mediainfo '{file_path}'")
    if not out:
        out = "Unknown Format !!"
    paster = f"""
<h2>📃 MEDIA INFO 📃</h2>
<code>
{d3vl_}
</code>
<h2>🧐 MORE DETAILS 🧐</h2>
<code>
{out} 
</code>"""
    paste = await telegraph_paste(f"{D3VILL_MEDIA}", paster)
    await d3vil.edit(f"📌 Fetched  Media Info Successfully !! \n\n**Check Here :** [{D3VIL_MEDIA}]({paste})")
    os.remove(file_path)

CmdHelp("mediainfo").add_command(
  "mediainfo", "<reply to a media>", "Fetches the detailed information of replied media."
).add()
