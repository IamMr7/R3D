# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from FallenMusic import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="• مسح •", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="𝐸𝑛𝑑", callback_data="end_cb"),
            InlineKeyboardButton(text="𝑅𝑒𝑠𝑢𝑚𝑒", callback_data="resume_cb"),
            InlineKeyboardButton(text="𝑃𝑎𝑢𝑠𝑒", callback_data="pause_cb"),
            ],[
            InlineKeyboardButton("𝐶ℎ𝑎𝑛𝑛𝑒𝑙", url=f"https://t.me/rr_yn7"),
            InlineKeyboardButton("𝐺𝑟𝑜𝑢𝑝", url=f"https://t.me/tr_56n"),
            ],[
            InlineKeyboardButton(
            text="• ᗩძძ TᏂᥱ ᙖ᥆T T᥆ Y᥆ᥙɾ ᘜɾ᥆ᥙρ •",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
            ],[
            InlineKeyboardButton("𝑆𝑜𝑢𝑟𝑐𝑒 𝑅Ꮛ𝐷", url=f"https://t.me/rr_yn7"),
            ],[
            InlineKeyboardButton(text="• ᗪᥱ᥎ •", user_id=config.OWNER_ID),
        ]
    ]
)


pm_buttons = [
    [
        InlineKeyboardButton(
            text="‹ اضف البوت في مجموعتك ›",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="• اوامࢪ التشغيل •", callback_data="fallen_help")],
    [
        InlineKeyboardButton(text=" سوࢪس رعـد •", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="• جࢪوب الدعم •", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="• 𝐋𝐨𝐫𝐝 •", url="https://t.me/M_R_C2"
        ),
        InlineKeyboardButton(
            text="• 𝐀𝐥𝐞𝐱 •", url="https://t.me/F_b_i_c"),
    ],
    [
        InlineKeyboardButton(
            text="• 𝐑𝐲𝐚𝐧 •", url="https://t.me/rr_y_n"),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="‹ اضف البوت في مجموعتك ›",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="• سوࢪس رعـد •", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="• جࢪوب الدعم •", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="• 𝐋𝐨𝐫𝐝 •", url="https://t.me/M_R_C2"
        ),
        InlineKeyboardButton(
            text="• 𝐀𝐥𝐞𝐱 •", url="https://t.me/F_b_i_c"),
    ],
    [
        InlineKeyboardButton(
            text="• 𝐑𝐲𝐚𝐧 •", url="https://t.me/rr_y_n"),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="• اوامࢪ التشغيل •",
            callback_data="fallen_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="• اوامࢪ المطور •", callback_data="fallen_cb sudo"),
        InlineKeyboardButton(text="• اوامࢪ المالك •", callback_data="fallen_cb owner"),
    ],
    [
        InlineKeyboardButton(text="• ࢪجوع •", callback_data="fallen_home"),
        InlineKeyboardButton(text="• مسح •", callback_data="close"),
    ],
]


help_back = [
    [InlineKeyboardButton(text="• جࢪوب الدعم •", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="• ࢪجوع •", callback_data="fallen_help"),
        InlineKeyboardButton(text="• مسح •", callback_data="close"),
    ],
]
