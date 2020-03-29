"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 18)

    input_str = event.pattern_match.group(1)

    if input_str == "call":

        await event.edit(input_str)

        animation_chars = [
        
            "`Connecting To Telegram Headquarters...`",
            "`Call Connected.`",
            "`Telegram: Hello This is Telegram HQ. Who is this?`",
            "`Me: Yo this is` Alex Marz ,`I need instant access to Telegram call centre`",
            "`OK sir! Let me verify you first. `User Authorised.`",
            "`Private  Call Connected...`",
            "`Me: Hello Sir, Please Ban This Telegram Account.`",    
            "`Telegram Headquarters: May I Know Who Is This?`",
            "`Me: It's me Alex Marz! Your DAD ",
            "`Telegram Headquarters: Excuse me sir! You can't use that type of language here`",
            "`Me: Do i look like a Motherfucker that gives a DAMN?`",
            "`Telegram Headquarters: Sorry sir! but if you keep using such words we've  to disconnect you`",
            "`Me: Teri MAA KA BHOSDA, TERI BHEN KO CHOD CHOD K CHUTTAD LAL KARUNGA BETICHOD RANDI KA BACHA`",
            "`BEEP BEEP BEEP!!!!`",
            "`Private Call Disconnected.`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 18])
