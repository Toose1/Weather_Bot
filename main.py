import asyncio
import logging
import ipinfo

from dataclasses import dataclass

from typing import Callable

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown
from aiogram.enums import ParseMode





router = Dispatcher()


@router.message(CommandStart())
async def handler_command_start(mess: types.Message):
    if mess.from_user:
        await mess.reply(text=f"Hey {mess.from_user.first_name}")


@router.message(Command("help"))
async def handler_command_help(mess: types.Message):
    await mess.reply(text=f"*I'm* _remote_ ||__controler bot__||", parse_mode=ParseMode.MARKDOWN_V2)

# @router.message(F.photo)
# async def echo_message(mess: types.Message):
#     await mess.reply(text=f"sry {mess.from_user.full_name}, i cant see it {mess}", parse_mode=ParseMode.MARKDOWN_V2)

@router.message()
async def echo_message(mess: types.Message):
    if mess.text:
        await mess.reply(text=mess.text, parse_mode=ParseMode.MARKDOWN_V2)
    else:
        await mess.send_copy(chat_id=mess.chat.id)


# async def main():
#     token = "6490268843:AAFhVQsynDjNZRKvDPofkz41_aFV4UodBBo"
#     bot = Bot(token)
#     logging.basicConfig(level=logging.INFO)
#     await router.start_polling(bot)

def main() -> None:
    token = "9ec17a2c13b818"
    
    



if __name__ == "__main__":
    main()
