from create_bot import bot
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router
from aiogram import F
import init_data
import config
import create_bot
import inspect

router = Router()


@router.message(Command(commands=["stat"]), F.from_user.id == config.Owner_id)
async def command_stat(msg: Message = None):
    try:
        if msg is None:
            msg_chat_id = config.Support_chat_id
        else:
            msg_chat_id = msg.chat.id
        all_users = init_data.db.count_reg_user()[0][0]
        await bot.send_message(msg_chat_id, f"how_much_users_used_bot: {all_users}\n")
        return
    except Exception as e:
        await create_bot.send_error_message(__name__, inspect.currentframe().f_code.co_name, e)
