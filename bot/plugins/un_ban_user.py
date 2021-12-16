from pyrogram import (
    Client,
    filters
)
from pyrogram.errors.exceptions import UserIsBlocked
from pyrogram.types import (
    Message
)
from bot import (
    OWNER_ID,
    BOT_WS_BLOCKED_BY_USER,
    COMMM_AND_PRE_FIX,
    IS_UN_BANED_MESSAGE_TEXT,
    REASON_DE_LIMIT_ER,
    UN_BAN_COMMAND
)
from bot.hf.fic import vhkzuoi_repliz_handler
from bot.hf.flifi import uszkhvis_chats_ahndler
from bot.hf.stuf import get_tle_mof_t
from bot.sql.users_sql import get_user_id
from bot.sql.blacklist_sql import rem_user_from_bl


@Client.on_message(
    filters.command(UN_BAN_COMMAND, COMMM_AND_PRE_FIX) &
    uszkhvis_chats_ahndler([OWNER_ID]) &
    vhkzuoi_repliz_handler
)
async def un_ban_command(client: Client, message: Message):
    user_id, reply_message_id = get_user_id(
        message.reply_to_message.message_id
    )
    if not user_id:
        return
    _, unban_reason = get_tle_mof_t(message.text)
    rem_user_from_bl(user_id)
    black_list_message = IS_UN_BANED_MESSAGE_TEXT.format(
        reason=unban_reason
    )
    if not unban_reason:
        black_list_message = black_list_message.split(
            REASON_DE_LIMIT_ER
        )[0]
    try:
        await client.send_message(
            chat_id=user_id,
            text=black_list_message,
            disable_web_page_preview=True,
            reply_markup=message.reply_markup,
            disable_notification=True,
            reply_to_message_id=reply_message_id
        )
    except UserIsBlocked:
        await message.reply_text(
            BOT_WS_BLOCKED_BY_USER
        )
    await message.reply_text(
        f"<a href='tg://user?id={user_id}'>"
        "user"
        "</a> <b>unbanned</b>."
    )
