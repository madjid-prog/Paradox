import asyncio
from os import path
from pyrogram import filters
from pyrogram.types import (InlineKeyboardMarkup, InputMediaPhoto, Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove,
                            Voice)
from youtube_search import YoutubeSearch
from venz.Database import is_on_off, get_active_video_chats, get_video_limit, is_active_video_chat
from venz import (BOT_USERNAME, DURATION_LIMIT, DURATION_LIMIT_MIN,
                   MUSIC_BOT_NAME, app, db_mem)
from venz.Core.PyTgCalls.Converter import convert
from venz.Core.PyTgCalls.Downloader import download
from venz.Decorators.assistant import AssistantAdd
from venz.Decorators.checker import checker
from venz.Decorators.permission import PermissionCheck
from venz.Inline import (playlist_markup, search_markup, search_markup2, stream_quality_markup, choose_markup, livestream_markup,
                          url_markup, url_markup2)
from venz.Utilities.changers import seconds_to_min, time_to_seconds
from venz.Utilities.chat import specialfont_to_normal
from venz.Utilities.videostream import start_video_stream, start_live_stream
from venz.Utilities.theme import check_theme
from venz.Utilities.thumbnails import gen_thumb
from venz.Utilities.url import get_url
from venz.Utilities.youtube import (get_yt_info_id, get_yt_info_query, get_m3u8, 
                                     get_yt_info_query_slider)

from youtubesearchpython import VideosSearch

loop = asyncio.get_event_loop()

__MODULE__ = "VideoCalls"
__HELP__ = f"""

/play [Balas ke Video apa pun] atau [YT link] atau [Music Name]
- Streaming Video di Obrolan Suara

**Untuk Pengguna Sudo:-**

/set_video_limit [Number of Chats]
- Tetapkan Jumlah Obrolan maksimum yang diizinkan untuk Panggilan Video dalam satu waktu.


"""



@app.on_callback_query(filters.regex(pattern=r"Venz"))
async def choose_playmode(_, CallbackQuery):
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    videoid, duration, user_id = callback_request.split("|")
    if CallbackQuery.from_user.id != int(user_id):
        return await CallbackQuery.answer(
            "Ini bukan untukmu! Cari Lagu Anda Sendiri.", show_alert=True
        )
    buttons = choose_markup(videoid, duration, user_id)
    await CallbackQuery.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@app.on_callback_query(filters.regex(pattern=r"Choose"))
async def quality_markup(_, CallbackQuery):
    limit = await get_video_limit(141414)
    print(limit)
    if not limit:
        await CallbackQuery.message.delete()
        return await CallbackQuery.message.reply_text("**Tidak Ada Batas yang Ditetapkan untuk Panggilan Video**\n\nTetapkan Batas Jumlah Panggilan Video Maksimum yang diizinkan di Bot dengan /set_video_limit [Khusus Pengguna Sudo]")
    count = len(await get_active_video_chats())
    print(count)
    if int(count) == int(limit):
        if await is_active_video_chat(CallbackQuery.message.chat.id):
            pass
        else:
            return await CallbackQuery.answer("Maaf! Bot hanya mengizinkan panggilan video dalam jumlah terbatas karena masalah kelebihan CPU. Obrolan lain menggunakan panggilan video sekarang. Coba beralih ke audio atau coba lagi nanti", show_alert=True)
    if CallbackQuery.message.chat.id not in db_mem:
        db_mem[CallbackQuery.message.chat.id] = {}
    try:
        read1 = db_mem[CallbackQuery.message.chat.id]["live_check"]
        if read1:
            return await CallbackQuery.answer("Pemutaran Live Streaming... Hentikan untuk memutar musik", show_alert=True)
        else:
            pass
    except:
        pass
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    videoid, duration, user_id = callback_request.split("|")
    if CallbackQuery.from_user.id != int(user_id):
        return await CallbackQuery.answer(
            "Ini bukan untukmu! Cari Lagu Anda Sendiri.", show_alert=True
        )
    buttons = stream_quality_markup(videoid, duration, user_id)
    await CallbackQuery.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup(buttons)
    )


    

@app.on_callback_query(filters.regex(pattern=r"LiveStream"))
async def Live_Videos_Stream(_, CallbackQuery):
    limit = await get_video_limit(141414)
    if not limit:
        await CallbackQuery.message.delete()
        return await CallbackQuery.message.reply_text("**No Limit Defined for Video Calls**\n\nSet a Limit for Number of Maximum Video Calls allowed on Bot by /set_video_limit [Sudo Users Only]")
    count = len(await get_active_video_chats())
    if int(count) == int(limit):
        if await is_active_video_chat(CallbackQuery.message.chat.id):
            pass
        else:
            return await CallbackQuery.answer("Sorry! Bot only allows limited number of video calls due to CPU overload issues. Other chats are using video call right now. Try switching to audio or try again later", show_alert=True)
    if CallbackQuery.message.chat.id not in db_mem:
        db_mem[CallbackQuery.message.chat.id] = {}
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    chat_id = CallbackQuery.message.chat.id
    chat_title = CallbackQuery.message.chat.title
    quality, videoid, duration, user_id = callback_request.split("|")
    if CallbackQuery.from_user.id != int(user_id):
        return await CallbackQuery.answer(
            "Ini bukan untukmu! Cari Lagu Anda Sendiri.", show_alert=True
        )
    await CallbackQuery.message.delete()
    title, duration_min, duration_sec, thumbnail = get_yt_info_id(videoid)
    await CallbackQuery.answer(f"Processing:- {title[:20]}", show_alert=True)
    theme = await check_theme(chat_id)
    chat_title = await specialfont_to_normal(chat_title)
    thumb = await gen_thumb(thumbnail, title, user_id, theme, chat_title)
    nrs, ytlink = await get_m3u8(videoid)
    if nrs == 0:
        return await CallbackQuery.message.reply_text("Format Video tidak Ditemukan..")
    await start_live_stream(CallbackQuery, quality, ytlink, thumb, title, duration_min, duration_sec, videoid)



@app.on_callback_query(filters.regex(pattern=r"VideoStream"))
async def Videos_Stream(_, CallbackQuery):
    if CallbackQuery.message.chat.id not in db_mem:
        db_mem[CallbackQuery.message.chat.id] = {}
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    chat_id = CallbackQuery.message.chat.id
    chat_title = CallbackQuery.message.chat.title
    quality, videoid, duration, user_id = callback_request.split("|")
    if CallbackQuery.from_user.id != int(user_id):
        return await CallbackQuery.answer(
            "Ini bukan untukmu! Cari Lagu Anda Sendiri.", show_alert=True
        )
    if str(duration) == "None":
        buttons = livestream_markup(quality, videoid, duration, user_id)
        return await CallbackQuery.edit_message_text("**Live Stream Detected**\n\nWant to play live stream? This will stop the current playing musics(if any) and will start streaming live video.", reply_markup=InlineKeyboardMarkup(buttons))
    await CallbackQuery.message.delete()
    title, duration_min, duration_sec, thumbnail = get_yt_info_id(videoid)
    if duration_sec > DURATION_LIMIT:
        return await CallbackQuery.message.reply_text(
            f"**Batas Durasi Terlampaui**\n\n**Durasi yang Diizinkan: **{DURATION_LIMIT_MIN} minute(s)\n**Durasi yang Diterima:** {duration_min} minute(s)"
        )
    await CallbackQuery.answer(f"Processing:- {title[:20]}", show_alert=True)
    theme = await check_theme(chat_id)
    chat_title = await specialfont_to_normal(chat_title)
    thumb = await gen_thumb(thumbnail, title, user_id, theme, chat_title)
    nrs, ytlink = await get_m3u8(videoid)
    if nrs == 0:
        return await CallbackQuery.message.reply_text("Format Video tidak Ditemukan..")
    await start_video_stream(CallbackQuery, quality, ytlink, thumb, title, duration_min, duration_sec, videoid)
