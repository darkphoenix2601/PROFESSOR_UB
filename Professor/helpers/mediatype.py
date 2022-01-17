from .progress import humanbytes
from .formats import yaml_format


async def mediadata(e_media):
    d3vil = ""
    if e_media.file.name:
        d3vil += f"📍 𝙽𝙰𝙼𝙴 :  {e_media.file.name}<br>"
    if e_media.file.mime_type:
        d3vil += f"📍 𝙼𝙸𝙼𝙴 𝚃𝚈𝙾𝙴 :  {e_media.file.mime_type}<br>"
    if e_media.file.size:
        d3vil += f"📍 𝚂𝙸𝚉𝙴 :  {humanbytes(e_media.file.size)}<br>"
    if e_media.date:
        d3vil += f"📍 𝙳𝙰𝚃𝙴 :  {yaml_format(e_media.date)}<br>"
    if e_media.file.id:
        d3vil += f"📍 𝙸𝙳 :  {e_media.file.id}<br>"
    if e_media.file.ext:
        d3vil += f"📍 𝙴𝚇𝚃𝙴𝙽𝚂𝙸𝙾𝙽 :  '{e_media.file.ext}'<br>"
    if e_media.file.emoji:
        d3vil += f"📍 𝙴𝙼𝙾𝙹𝙸 :  {e_media.file.emoji}<br>"
    if e_media.file.title:
        d3vil += f"𖣔 𝚃𝙸𝚃𝙻𝙴 :  {e_media.file.title}<br>"
    if e_media.file.performer:
        d3vil += f"𖣔 𝙿𝙴𝚁𝙵𝙸𝚁𝙼𝙴𝚁 :  {e_media.file.performer}<br>"
    if e_media.file.duration:
        d3vil += f"𖣔 𝙳𝚄𝚁𝙰𝚃𝙸𝙾𝙽 :  {e_media.file.duration} seconds<br>"
    if e_media.file.height:
        d3vil += f"𖣔 𝙷𝙴𝙸𝙶𝙷𝚃 :  {e_media.file.height}<br>"
    if e_media.file.width:
        d3vil += f"𖣔 𝚆𝙸𝙳𝚃𝙷 :  {e_media.file.width}<br>"
    if e_media.file.sticker_set:
        d3vil += f"𖣔 𝚂𝚃𝙸𝙲𝙺𝙴𝚁 𝚂𝙴𝚃 :\
            \n {yaml_format(e_media.file.sticker_set)}<br>"
    try:
        if e_media.media.document.thumbs:
            d3vil += f"𖣔 𝚃𝙷𝚄𝙼𝙱  :\
                \n {yaml_format(e_media.media.document.thumbs[-1])}<br>"
    except Exception as e:
        LOGS.info(str(e))
    return d3vil


def media_type(message):
    if message and message.photo:
        return "Photo"
    if message and message.audio:
        return "Audio"
    if message and message.voice:
        return "Voice"
    if message and message.video_note:
        return "Round Video"
    if message and message.gif:
        return "Gif"
    if message and message.sticker:
        return "Sticker"
    if message and message.video:
        return "Video"
    if message and message.document:
        return "Document"
    return None
