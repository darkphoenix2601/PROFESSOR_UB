import asyncio
from collections import deque

from . import *

@bot.on(d3vil_cmd(pattern=r"boxs$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"boxs$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, "`boxs...`")
    deq = deque(list("🟥🟧🟨🟩🟦🟪🟫⬛⬜"))
    for _ in range(999):
        await asyncio.sleep(0.3)
        await event.edit("".join(deq))
        deq.rotate(1)

CmdHelp("animation").add_command(
  'boxs', None, 'Use and see'
).add_command(
  'kiler', '<text>', 'Cool killing animation with name'
).add_command(
  'eye', None, 'Use and see'
).add_command(
  'thinking', None, 'Use and see'
).add_command(
  'snake', None, 'Use and see'
).add_command(
  'human', None, 'Use and see'
).add_command(
  'mc', None, 'Use and see'
).add_command(
  'virus', None, 'Use and see'
).add_command(
  'repe', None, 'Use and see'
).add_command(
  'nikal', None, 'Use and see'
).add_command(
  'music', None, 'Use and see'
).add_command(
  'squ', None, 'Use and see'
).add_command(
  'rain', None, 'Use and see'
).add()
