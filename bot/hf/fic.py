from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)


def func(flt, client: Client, message: Message):
    if message.reply_to_message:
        if (
            message.reply_to_message.from_user
            and message.reply_to_message.from_user.is_self
        ):
            return True
        if message.chat.type == "channel":
            # i really don't know,
            # how to correctly handle it
            return True
    return False


vhkzuoi_repliz_handler = filters.create(func)
