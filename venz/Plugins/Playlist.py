from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                            KeyboardButton, Message, ReplyKeyboardMarkup,
                            ReplyKeyboardRemove)

from venz import BOT_ID, BOT_USERNAME, MUSIC_BOT_NAME, SUDOERS, app, db_mem
from venz.Database import (_get_playlists, delete_playlist, get_playlist,
                            get_playlist_names, save_playlist)
from venz.Decorators.admins import AdminRightsCheck
from venz.Decorators.assistant import AssistantAdd
from venz.Decorators.checker import checker, checkerCB
from venz.Decorators.permission import PermissionCheck
from venz.Inline import (add_genre_markup, check_genre_markup, check_markup,
                          delete_playlist_markuup, download_markup,
                          others_markup, play_genre_playlist, playlist_markup,
                          third_playlist_markup)

__MODULE__ = "Playlist"
__HELP__ = """


/playplaylist 
- Mulai mainkan Daftar Putar Tersimpan Anda.


/playlist 
- Periksa Daftar Putar Tersimpan Anda Di Server.


/delmyplaylist
- Hapus semua musik yang disimpan di daftar putar Anda


/delgroupplaylist
- Hapus semua musik yang disimpan di daftar putar grup Anda [Memerlukan Hak Admin.]
"""


@app.on_message(filters.command("playplaylist") & filters.group)
@checker
@PermissionCheck
@AssistantAdd
async def play_playlist_cmd(_, message):
    thumb = "Utils/Playlist.jpg"
    await message.delete()
    if not message.reply_to_message:
        if len(message.command) == 2:
            user = message.text.split(None, 2)[1]
            if "@" in user:
                user = user.replace("@", "")
            try:
                user = int(user)
                try:
                    user = await app.get_users(user)
                    userid = user.id
                    third_name = user.first_name
                except:
                    userid = user
                    third_name = "Deleted Account"
            except:
                try:
                    user = await app.get_users(user)
                    userid = user.id
                    third_name = user.first_name
                except Exception as e:
                    return await message.reply_text("User not found")
            user_id = message.from_user.id
            user_name = message.from_user.first_name
            buttons = third_playlist_markup(
                user_name, user_id, third_name, userid, "abcd"
            )
            hmo = await message.reply_photo(
                photo=thumb,
                caption=(
                    f"**{MUSIC_BOT_NAME}'s Fitur Daftar Putar**\nPilih Daftar Putar yang ingin Anda putar!.\in\nAnda juga dapat memutar daftar putar orang lain:-\n- /playplaylist [Username]\n- /playplaylist [USER ID](if user has deleted acc)\n- /playplaylist [Reply to a User]"
                ),
                reply_markup=InlineKeyboardMarkup(buttons),
            )
            return
        else:
            user_id = message.from_user.id
            user_name = message.from_user.first_name
            buttons = playlist_markup(user_name, user_id, "abcd")
            await message.reply_photo(
                photo=thumb,
                caption=(
                    f"**{MUSIC_BOT_NAME}'s Fitur Daftar Putar**\nPilih Daftar Putar yang ingin Anda mainkan!.\n\nAnda juga dapat memutar daftar putar orang lain:-\n- /playplaylist [Username]\n- /playplaylist [USER ID](if user has deleted acc)\n- /playplaylist [Reply to a User]"
                ),
                reply_markup=InlineKeyboardMarkup(buttons),
            )
            return
    else:
        userid = message.reply_to_message.from_user.id
        third_name = message.reply_to_message.from_user.first_name
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        buttons = third_playlist_markup(
            user_name, user_id, third_name, userid, "abcd"
        )
        hmo = await message.reply_photo(
            photo=thumb,
            caption=(
                f"**{MUSIC_BOT_NAME}'s Fitur Daftar Putar**\nPilih Daftar Putar yang ingin Anda mainkan!.\n\nAnda juga dapat memutar daftar putar orang lain:-\n- /playplaylist [Username]\n- /playplaylist [USER ID](if user has deleted acc)\n- /playplaylist [Reply to a User]"
            ),
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        return


@app.on_message(filters.command("playlist") & filters.group)
@checker
@PermissionCheck
@AssistantAdd
async def playlist(_, message):
    thumb = "Utils/Playlist.jpg"
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    buttons = check_markup(user_name, user_id, "abcd")
    await message.reply_photo(
        photo=thumb,
        caption=(
            f"**{MUSIC_BOT_NAME}'s Fitur Daftar Putar**\n\nPilih Daftar Putar, Anda ingin **check!**"
        ),
        reply_markup=InlineKeyboardMarkup(buttons),
    )
    return


options = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "all",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
]

options_Genre = [
    "DJ",
    "Sad",
    "K-POP",
    "LO-FI",
    "INDONESIAN",
    "HIP-HOP",
    "TRAP",
    "POP",
]


@app.on_message(filters.command("delmyplaylist") & filters.group)
async def del_cmd(_, message):
    usage = f"Usage:\n\n/delmyplaylist [Genre] [Numbers between 1-30] ( to delete a particular music in playlist )\n\nor\n\n/delmyplaylist [Genre] all ( to delete whole playlist )\n\n**Genres:-**\n{' | '.join(options_Genre)}"
    if len(message.command) < 3:
        return await message.reply_text(usage)
    genre = message.text.split(None, 2)[1].strip()
    count = message.text.split(None, 2)[2].strip()
    if not count:
        return await message.reply_text(usage)
    if count not in options:
        return await message.reply_text(usage)
    if genre not in options_Genre:
        return await message.reply_text(usage)
    if str(count) == "all":
        buttons = delete_playlist_markuup("Personal", genre)
        return await message.reply_text(
            f"Konfirmasi!!\nAnda yakin ingin menghapus keseluruhan Anda {genre} daftar putar?",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        _playlist = await get_playlist_names(message.from_user.id, genre)
    if not _playlist:
        await message.reply_text(
            f"Anda tidak memiliki Daftar Putar di {MUSIC_BOT_NAME}'s Server"
        )
    else:
        titlex = []
        j = 0
        count = int(count)
        for note in _playlist:
            j += 1
            _note = await get_playlist(message.from_user.id, note, genre)
            if j == count:
                deleted = await delete_playlist(
                    message.from_user.id, note, genre
                )
                if deleted:
                    return await message.reply_text(
                        f"**dihapus {count} musik di daftar putar**"
                    )
                else:
                    return await message.reply_text(
                        f"**Tidak ada musik yang disimpan dalam daftar putar.**"
                    )
        await message.reply_text("Anda tidak memiliki musik seperti itu di Daftar Putar.")


@app.on_message(filters.command("delgroupplaylist") & filters.group)
@AdminRightsCheck
async def delgroupplaylist(_, message):
    usage = f"Usage:\n\n/delgroupplaylist [Genre] [Numbers between 1-30] ( to delete a particular music in playlist )\n\nor\n\n /delgroupplaylist [Genre] all ( to delete whole playlist )\n\n**Genres:-**\n{' | '.join(options_Genre)}"
    if len(message.command) < 3:
        return await message.reply_text(usage)
    genre = message.text.split(None, 2)[1].strip()
    count = message.text.split(None, 2)[2].strip()
    if not count:
        return await message.reply_text(usage)
    if count not in options:
        return await message.reply_text(usage)
    if genre not in options_Genre:
        return await message.reply_text(usage)
    if str(count) == "all":
        buttons = delete_playlist_markuup("Group", genre)
        return await message.reply_text(
            f"Konfirmasi!!\nAnda yakin ingin menghapus seluruh Grup {genre} daftar putar?",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        _playlist = await get_playlist_names(message.chat.id, genre)
    if not _playlist:
        await message.reply_text(
            f"Anda tidak memiliki Daftar Putar di {MUSIC_BOT_NAME}'s Server"
        )
    else:
        titlex = []
        j = 0
        count = int(count)
        for note in _playlist:
            j += 1
            _note = await get_playlist(message.chat.id, note, genre)
            if j == count:
                deleted = await delete_playlist(message.chat.id, note, genre)
                if deleted:
                    return await message.reply_text(
                        f"**dihapus {count} musik dalam daftar putar grup**"
                    )
                else:
                    return await message.reply_text(
                        f"**Tidak ada musik yang disimpan dalam daftar putar Grup.**"
                    )
        await message.reply_text("Anda tidak memiliki musik seperti itu di Daftar Putar.")


@app.on_callback_query(filters.regex(pattern=r"show_genre"))
async def show_genre(_, CallbackQuery):
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    userid = CallbackQuery.from_user.id
    a, b, c = callback_request.split("|")
    buttons = play_genre_playlist(a, b, "abcd")
    await CallbackQuery.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@app.on_callback_query(filters.regex(pattern=r"playlist_check"))
async def playlist_check(_, CallbackQuery):
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    userid = CallbackQuery.from_user.id
    a, b, c = callback_request.split("|")
    print(b)
    buttons = check_genre_markup(b, "abcd", userid)
    await CallbackQuery.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@app.on_callback_query(filters.regex(pattern=r"main_playlist"))
async def main_playlist(_, CallbackQuery):
    await CallbackQuery.answer()
    user_id = CallbackQuery.from_user.id
    user_name = CallbackQuery.from_user.first_name
    buttons = playlist_markup(user_name, user_id, "abcd")
    await CallbackQuery.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@app.on_callback_query(filters.regex(pattern=r"your_playlist"))
async def your_playlist(_, CallbackQuery):
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    userid = CallbackQuery.from_user.id
    videoid, user_id = callback_request.split("|")
    buttons = add_genre_markup(user_id, "Personal", videoid)
    await CallbackQuery.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@app.on_callback_query(filters.regex(pattern=r"group_playlist"))
async def group_playlist(_, CallbackQuery):
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    userid = CallbackQuery.from_user.id
    videoid, user_id = callback_request.split("|")
    buttons = add_genre_markup(user_id, "Group", videoid)
    await CallbackQuery.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@app.on_callback_query(filters.regex(pattern=r"other"))
async def otherhuvai(_, CallbackQuery):
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    userid = CallbackQuery.from_user.id
    videoid, user_id = callback_request.split("|")
    buttons = others_markup(videoid, user_id)
    db_mem[videoid]["check"] = 1
    await CallbackQuery.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@app.on_callback_query(filters.regex(pattern=r"goback"))
async def goback(_, CallbackQuery):
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    userid = CallbackQuery.from_user.id
    videoid, user_id = callback_request.split("|")
    buttons = others_markup(videoid, user_id)
    try:
        await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except:
        pass
