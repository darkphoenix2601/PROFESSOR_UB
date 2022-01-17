from subprocess import PIPE
from subprocess import run as runapp

import base64

from . import *

@bot.on(d3vil_cmd(pattern="hash (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="hash (.*)", allow_sudo=True))
@errors_handler
async def gethash(hash_q):
    if hash_q.fwd_from:
        return
    event = await eor(hash_q, "Processing...")
    hashtxt_ = hash_q.pattern_match.group(1)
    hashtxt = open("hashdis.txt", "w+")
    hashtxt.write(hashtxt_)
    hashtxt.close()
    md5 = runapp(["md5sum", "hashdis.txt"], stdout=PIPE)
    md5 = md5.stdout.decode()
    sha1 = runapp(["sha1sum", "hashdis.txt"], stdout=PIPE)
    sha1 = sha1.stdout.decode()
    sha256 = runapp(["sha256sum", "hashdis.txt"], stdout=PIPE)
    sha256 = sha256.stdout.decode()
    sha512 = runapp(["sha512sum", "hashdis.txt"], stdout=PIPE)
    runapp(["rm", "hashdis.txt"], stdout=PIPE)
    sha512 = sha512.stdout.decode()
    ans = (
        "Text: `"
        + hashtxt_
        + "`\nMD5: `"
        + md5
        + "`SHA1: `"
        + sha1
        + "`SHA256: `"
        + sha256
        + "`SHA512: `"
        + sha512[:-1]
        + "`"
    )
    if len(ans) > 4096:
        hashfile = open("hashes.txt", "w+")
        hashfile.write(ans)
        hashfile.close()
        await hash_q.client.send_file(
            hash_q.chat_id,
            "hashes.txt",
            reply_to=hash_q.id,
            caption="`It's too big, sending a text file instead. `",
        )
        runapp(["rm", "hashes.txt"], stdout=PIPE)
    else:
        await hash_q.reply(ans)
        await event.delete()


@bot.on(d3vil_cmd(pattern="encode ?(.*)"))
@bot.on(sudo_cmd(pattern="encode (.*)", allow_sudo=True))
async def encod(e):
    match = e.pattern_match.group(1)
    if not match and e.is_reply:
        gt = await e.get_reply_message()
        if gt.text:
            match = gt.text
    if not (match or e.is_reply):
        return await eor(e, "`Give me Something to Encode..`")
    byt = match.encode("ascii")
    et = base64.b64encode(byt)
    atc = et.decode("ascii")
    await eor(e, f"**=>> 𝖤𝗇𝖼𝗈𝖽𝖾𝖽 𝖳𝖾𝗑𝗍 :** `{match}`\n\n**=>> 𝖮𝖴𝖳𝖯𝖴𝖳 :**\n`{atc}`")


@bot.on(d3vil_cmd(pattern="decode ?(.*)"))
@bot.on(sudo_cmd(pattern="decode (.*)", allow_sudo=True))
async def encod(e):
    match = e.pattern_match.group(1)
    if not match and e.is_reply:
        gt = await e.get_reply_message()
        if gt.text:
            match = gt.text
    if not (match or e.is_reply):
        return await eor(e, "`Give me Something to Decode..`")
    byt = match.encode("ascii")
    try:
        et = base64.b64decode(byt)
        atc = et.decode("ascii")
        await eor(e, f"**=>> 𝖣𝖾𝖼𝗈𝖽𝖾𝖽 𝖳𝖾𝗑𝗍 :** `{match}`\n\n**=>> 𝖮𝖴𝖳𝖯𝖴𝖳 :**\n`{atc}`")
    except Exception as p:
        await eor(e, "**ERROR :** " + str(p))


CmdHelp("encode_decode").add_command(
  "hash", "<query>", "Finds the md5, sha1, sha256, sha512 of the string when written into a txt file"
).add_command(
  "encode", "<query>", "Finds the base64 encoding of the given string"
).add_command(
  "decode", "<query>", "Finds the base64 decoding of the given string"
).add()
