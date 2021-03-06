from config import MUSIC_BOT_NAME, SUPPORT_CHANNEL, SUPPORT_GROUP
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from venz import BOT_USERNAME

def setting_markup2():
    buttons = [
        [
            InlineKeyboardButton(text="ð Kualitas Audio", callback_data="AQ"),
            InlineKeyboardButton(text="ð Volume Audio", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="ð¥ Pengguna Resmi", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="ð» Dashboard", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="âï¸ Tutup", callback_data="close"),
        ],
    ]
    return f"ð§  **{MUSIC_BOT_NAME} Pengaturan**", buttons



def start_pannel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="ð Menu Perintah Pembantu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ð§ Pengaturan", callback_data="settingm"
                )
            ],
        ]
        return f"ð  **Ini {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="ð Menu Perintah Pembantu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ð§ Pengaturan", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="ð¨Grup pendukung", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"ð  **Ini {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="ð Menu Perintah Pembantu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ð§ Pengaturan", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="ð¨Channel Resmi", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"ð  **Ini {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="ð Menu Perintah Pembantu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ð§ Pengaturan", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="ð¨ Channel Resmi", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="ð¨Grup pendukung", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"ð  **Ini {MUSIC_BOT_NAME}**", buttons


def private_panel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="ð Menu Perintah Pembantu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "â Tambahkan saya ke Grup Anda",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
        ]
        return f"ð  **Ini {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="ð Menu Perintah Pembantu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "â Tambahkan saya ke Grup Anda",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="ð¨Grup pendukung", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"ð  **This is {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="ð Menu Perintah Pembantu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "â Tambahkan saya ke Grup Anda",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="ð¨ Channel Resmi", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"ð  **Ini {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="ð Menu Perintah Pembantu", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "â Tambahkan saya ke Grup Anda",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="ð¨ Channel Resmi", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="ð¨Grup pendukung", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"ð  **Ini {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="ð Kualitas Audio", callback_data="AQ"),
            InlineKeyboardButton(text="ð Volume Audio", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="ð¥ Pengguna Resmi", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="ð» Dashboard", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="âï¸ Tutup", callback_data="close"),
            InlineKeyboardButton(text="ð Kembali", callback_data="okaybhai"),
        ],
    ]
    return f"ð§  **{MUSIC_BOT_NAME} Pengaturan**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="ð Setel Ulang Volume Audio ð", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="ð Vol rendah", callback_data="LV"),
            InlineKeyboardButton(text="ð Vol sedang", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="ð Vol tinggi", callback_data="HV"),
            InlineKeyboardButton(text="ð Volume yang Diperkuat", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="ð½ Volume Kustom ð½", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="ð Kembali", callback_data="settingm")],
    ]
    return f"ð§  **{MUSIC_BOT_NAME} Pengaturan**", buttons


def custommarkup():
    buttons = [
        [
            InlineKeyboardButton(text="+10", callback_data="PTEN"),
            InlineKeyboardButton(text="-10", callback_data="MTEN"),
        ],
        [
            InlineKeyboardButton(text="+25", callback_data="PTF"),
            InlineKeyboardButton(text="-25", callback_data="MTF"),
        ],
        [
            InlineKeyboardButton(text="+50", callback_data="PFZ"),
            InlineKeyboardButton(text="-50", callback_data="MFZ"),
        ],
        [InlineKeyboardButton(text="ð¼ Volume Kostum ð¼", callback_data="AV")],
    ]
    return f"ð§  **{MUSIC_BOT_NAME} Pengaturan**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="ð¥ Setiap orang", callback_data="EVE"),
            InlineKeyboardButton(text="ð Admin", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="ð Daftar Pengguna Resmi", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="ð Go back", callback_data="settingm")],
    ]
    return f"ð§  **{MUSIC_BOT_NAME} Pengaturan**", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="âï¸ Waktu aktif", callback_data="UPT"),
            InlineKeyboardButton(text="ð¾ Ram", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="ð» Cpu", callback_data="CPT"),
            InlineKeyboardButton(text="ð½ Disk", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="ð Kembali", callback_data="settingm")],
    ]
    return f"ð§  **{MUSIC_BOT_NAME} Pengaturan**", buttons
