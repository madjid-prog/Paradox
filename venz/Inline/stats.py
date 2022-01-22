from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

stats1 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Statistik Sistem", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="Statistik Penyimpanan", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Statistik Bot", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="Statistik MongoDB", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Statistik Asisten", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats2 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Statistik Umum", callback_data=f"gen_stats"
            ),
            InlineKeyboardButton(
                text="Statistik Penyimpanan", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Statistik Bot", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="Statistik MongoDB", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Statistik Asisten", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats3 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Statistik Sistem", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="Statistik Umum", callback_data=f"gen_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Statistik Bot", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="Statistik MongoDB", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Statistik Asisten", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats4 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Statistik Sistem", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="Statistik Penyimpanan", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Statistik Umum", callback_data=f"gen_stats"
            ),
            InlineKeyboardButton(
                text="Statistik MongoDB", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Statistik Asisten", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats5 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Statistik Sistem", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="Statistik Penyimpanan", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Statistik Bot", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="Statistik Umum", callback_data=f"gen_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Statistik Asisten", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats6 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Statistik Sistem", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="Statistik Penyimpanan", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Statistik Bot", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="Statistik MongoDB", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Statistik Umum", callback_data=f"gen_stats"
            )
        ],
    ]
)


stats7 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Mendapatkan Statistik Asisten....",
                callback_data=f"wait_stats",
            )
        ]
    ]
)
