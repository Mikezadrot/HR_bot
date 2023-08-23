from typing import Dict
from Json_funk import load_data_from_json as load_json
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder


def generate_lexicon(button_count: int, button_prefix: str = 'country_') -> Dict[str, str]:

    lexicon = {}
    for i in range(1, button_count + 1):
        button_key = f'{button_prefix}{i}'
        button_value = f'{country_dict[i]}'
        lexicon[button_key] = button_value
    return lexicon


def generate_professions(button_count: int, button_prefix: str = 'prof_') -> Dict[str, str]:

    prof = {}
    for i in range(1, button_count + 1):
        button_key = f'{button_prefix}{i}'
        button_value = f'{profession_dict[i]}'
        prof[button_key] = button_value
    return prof


def generate_next_step_kb(button_count: int, next_dict, button_prefix: str = 'next_') -> Dict[str, str]:
    next = {}
    for i in range(0, button_count+1):
        button_key = f'{button_prefix}{i+1}'
        button_value = f'{next_dict[i]}'
        next[button_key] = button_value
    return next


def create_inline_kb(width: int,
                     *args: str,
                     last_btn: str | None = None,
                     **kwargs: str) -> InlineKeyboardMarkup:

    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    buttons: list[InlineKeyboardButton] = []


    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))


    kb_builder.row(*buttons, width=width)

    if last_btn:
        kb_builder.row(InlineKeyboardButton(
                            text='Продовжити',
                            callback_data='last_btn'))


    return kb_builder.as_markup()


def create_inline_kb_country(width: int,
                     *args: str,
                     last_btn: str | None = None,
                     **kwargs: str) -> InlineKeyboardMarkup:

    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    buttons: list[InlineKeyboardButton] = []


    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))


    kb_builder.row(*buttons, width=width)

    if last_btn:
        kb_builder.row(InlineKeyboardButton(
                            text='Продовжити',
                            callback_data='last_btn_country'))


    return kb_builder.as_markup()


def create_inline_kb_prof(width: int,
                     *args: str,
                     last_btn: str | None = None,
                     **kwargs: str) -> InlineKeyboardMarkup:

    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    buttons: list[InlineKeyboardButton] = []


    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))


    kb_builder.row(*buttons, width=width)

    if last_btn:
        kb_builder.row(InlineKeyboardButton(
                            text='Продовжити',
                            callback_data='last_btn_prof'))


    return kb_builder.as_markup()




data = load_json()
country_dict = []
profession_dict = []

for item in data:
    if item['Країна'] not in country_dict:
        country_dict.append(item['Країна'])
    if item['Вакансія'] not in profession_dict:
        profession_dict.append(item['Вакансія'])

# використання:
button_count_country = len(country_dict) - 1
button_count_profession = len(profession_dict) - 1
LEXICON = generate_lexicon(button_count_country)

PROFESSION = generate_professions(button_count_profession)
# print(LEXICON)
# print(PROFESSION)
