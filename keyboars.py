from aiogram import types
from aiogram.utils.callback_data import CallbackData

cat_kb = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton("🍳 Завтраки", callback_data="breakfast")
        ],
        [
            types.InlineKeyboardButton("🥗 Салаты", callback_data="salat")
        ],
        [
            types.InlineKeyboardButton("🍰 Десерты", callback_data="dessert")
        ]
        
    ]
)

recipes = CallbackData("recipe", "name", "cat")

breakfast_kb = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(
                "Блиц-хачапури", callback_data=recipes.new(name="hachap", cat="breakfast"))
        ],
        [
            types.InlineKeyboardButton(
                "Необычные оладьи", callback_data=recipes.new(name="olad", cat="breakfast"))
        ],
        [
            types.InlineKeyboardButton(
                "Сырники", callback_data=recipes.new(name="seern", cat="breakfast"))
        ],
        [
            types.InlineKeyboardButton("↩️ Назад", callback_data="menu")
        ],
    ]
)

salat_kb = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(
                "Салат «Отпад»", callback_data=recipes.new(name="otpad", cat="salat"))
        ],
        [
            types.InlineKeyboardButton(
                "Салат «Идиллия»", callback_data=recipes.new(name="idilia", cat="salat"))
        ],
        [
            types.InlineKeyboardButton(
                "Салат «Глехурад»", callback_data=recipes.new(name="glehurad", cat="salat"))
        ],
        [
            types.InlineKeyboardButton("↩️ Назад", callback_data="menu")
        ],
    ]
)

dessert_kb = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(
                "Торт «Штучная работа»", callback_data=recipes.new(name="shtuch", cat="dessert"))
        ],
        [
            types.InlineKeyboardButton(
                "Конфеты а-ля «Сникерс»", callback_data=recipes.new(name="snikers", cat="dessert"))
        ],
        [
            types.InlineKeyboardButton(
                "Творожная запеканка со сметанным кремом", callback_data=recipes.new(name="zapek", cat="dessert"))
        ],
        [
            types.InlineKeyboardButton("↩️ Назад", callback_data="menu")
        ],
    ]
)


def back_to_cat(category):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    "↩️ Назад", callback_data=category)
            ],
        ]
    )
    return keyboard
