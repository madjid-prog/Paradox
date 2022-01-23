from typing import Dict, List, Union

from venz import BOT_ID, app


def PermissionCheck(mystic):
    async def wrapper(_, message):
        a = await app.get_chat_member(message.chat.id, BOT_ID)
        if a.status != "administrator":
            return await message.reply_text(
                "Saya perlu menjadi admin dengan beberapa izin:\n"
                + "\n- **can_manage_voice_chats:** Untuk mengelola obrolan suara"
                + "\n- **can_delete_messages:** Untuk menghapus Sampah yang Dicari Bot"
                + "\n- **can_invite_users**: Untuk mengundang asisten untuk mengobrol."
            )
        if not a.can_manage_voice_chats:
            await message.reply_text(
                "Saya tidak memiliki izin yang diperlukan untuk melakukan tindakan ini."
                + "\n**Izin:** __KELOLA VOICE CHATS__"
            )
            return
        if not a.can_delete_messages:
            await message.reply_text(
                "Saya tidak memiliki izin yang diperlukan untuk melakukan tindakan ini."
                + "\n**Izin:** __HAPUS PESAN__"
            )
            return
        if not a.can_invite_users:
            await message.reply_text(
                "I don't have the required permission to perform this action."
                + "\n**Izin:** __UNDANG PENGGUNA MELALUI LINK__"
            )
            return
        return await mystic(_, message)

    return wrapper
