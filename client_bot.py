import os
import urllib.request
from time import time

import filetype
import requests
import validators
from telethon import TelegramClient, events

# https://my.telegram.org/
api_id = XXXXXX
api_hash = 'XXXXXXXXXXXXXXXXXXXXXXXXXXX'

# @BotFather (the script work also for a user account, change the code)
bot_token = '123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZAABBCCDDEEFFG'

file_size = 200000000  # In Bytes

with TelegramClient('fichierrapide', api_id, api_hash).start(bot_token=bot_token) as client:
    print("Démarrage terminé")

    async def callback(current, total):
        print('Downloaded', current, 'out of', total,
              'bytes: {:.2%}'.format(current / total))

    @client.on(events.NewMessage(pattern="/start"))
    async def handler(event):
        await event.reply("Hello ! Send me a file, you'll get a direct link :)")


    @client.on(events.NewMessage())
    async def handler(event):

        if event.message.text:
            if validators.url(event.message.text):
                message = await event.reply("Downloading file...")

                try:
                    os.mkdir("files/")
                except OSError as error:
                    print(error)

                a = "files/" + str(time())

                print("Downloading file locally...")
                urllib.request.urlretrieve(event.message.text, a)  # Todo Check file size

                kind = filetype.guess(a)
                if kind is not None:
                    os.rename(a, a + "." + kind.extension)
                    a = a + "." + kind.extension

                await message.edit("Uploading file to Telegram...")
                await client.send_file(event.sender_id, a, force_document=False, reply_to=event.message)
                await client.delete_messages(event.sender_id, [message])
                os.remove(a)

        if event.message.file:
            if event.message.file.size < file_size:
                message_reply = await event.reply("Downloading the file locally...")

                try:
                    os.mkdir("files/")
                except OSError as error:
                    print(error)

                a = "files/" + str(time())

                await event.message.download_media(a, progress_callback=callback)

                files = {
                    'file': (a, open(a, 'rb')),
                }

                await client.edit_message(message_reply, "Uploading the file...")

                response = requests.post('https://0x0.st/', files=files)

                await client.edit_message(message_reply, response.text)

                os.remove(a)
            else:
                await event.reply("Fichier trop lourd, 200Mo maximum, merci ! :)")


    client.run_until_disconnected()
