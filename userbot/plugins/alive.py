"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "WTF Noob! Couldn't even set ALIVE_NAME into Heroku Config. Who TF even gave you my Repo :V"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**`You Thought I Was Gonna DIE? PFFFTTTTTTT! Surprise MotherF*cker`**\n\n"
                    "`******Al3x Priv8 Userbot - Final Edition******`\n\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\n`"
                     "`Database Status: Databases functioning normally!\n\nAlways with you, my master!\n`"
                     f"`My peru owner`: {DEFAULTUSER}\n\n"
                     "`Newly Added Features:\n`"
                     "`- Ncell Bomber:\n`"
                     "`- NTC Bomber\n`"
                     "`- NTC Bomber\n\n`"
                     "`- Temp-Mail\n`"
                     "`- Torlink and\n`"
                     "`- Magnet link\n\n`"
                     "Special Thanks To @Dr34m_C4t and @scifidemon For Scripts.\n")
