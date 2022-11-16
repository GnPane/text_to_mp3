import asyncio, shutil, os
from pathlib import Path

from aiogram import Bot, Dispatcher, executor, filters, types
from aiogram.types import ContentTypes, Message

import text_to_mp3


API_TOKEN = '5613480569:AAGr2XMpjxDng0-fMqFPJO_0p1s27UHMHSI'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(content_types=ContentTypes.DOCUMENT)
async def doc_handler(message: Message):
    # Change method
    # await message.document.download(
    #             destination_dir="",
    #             destination_file="file.txt",
    #         )
    if document := message.document:
        file_name = message.document.file_name
        await document.download(
            destination_dir="",
            destination_file=file_name,
        )
    text_to_mp3.main(Path.cwd()/file_name)

    await message.reply_audio(open(f'text.mp3', 'rb'))
    os.remove(Path.cwd()/f'{file_name}')
    os.remove(Path.cwd()/f'{file_name[0:-4]}.mp3')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
