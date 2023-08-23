import os
import aiogram
import logging

from aiogram import Bot, types, Dispatcher, F
from aiogram.filters.command import Command
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message, ReplyKeyboardRemove)
from aiogram.filters.state import State, StatesGroup

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.memory import MemoryStorage
from spreadsheet import get_data_from_spreadsheet, existing_sheets
from Json_funk import writing_to_json, write_users_dict, readind_users_dict, load_data_from_json # creating or recreating data.json
from keyboards import LEXICON, PROFESSION, create_inline_kb_country, create_inline_kb_prof, generate_next_step_kb, data


API_TOKEN = os.getenv('TOKEN')
bot: Bot = Bot(token=API_TOKEN, parse_mode='HTML')
storage: MemoryStorage = MemoryStorage()
dp: Dispatcher = Dispatcher(storage=storage)

# class FSMFillForm(StatesGroup):
#     fill_country = State()
#     fill_prof = State()


user_data_dict = readind_users_dict()




# get_data_from_spreadsheet()
#
# existing_sheets()
# writing_to_json()


@dp.message(CommandStart())
async def process_start_command(message: Message):
    keyboard = create_inline_kb_country(4, last_btn='last_c', **LEXICON)
    await message.answer(text='Вибір країни',
                         reply_markup=keyboard)
    user_id = message.from_user.id
    user_data_dict[user_id] = {"country": '', "profession": ''}



@dp.message(Command('prof'))
async def cmd_prof(message: types.Message):
    keyboard = create_inline_kb_prof(4, last_btn='last_p', **PROFESSION)
    await message.answer(text='Вибір професій',
                         reply_markup=keyboard)


# @dp.message(Command('res'))
# async def res(message: Message, state: FSMContext):
#     user_data = state.get_data()
#     await message.answer(text=f'{user_data}')

@dp.message(Command('res'))
async def res(message: Message):
    print(user_data_dict)
    await message.answer(text=f'{user_data_dict}')
    write_users_dict(user_data_dict)
    # res = readind_users_dict()
    # await message.answer(text=f'{res}')
    # print(res)


@dp.callback_query(F.data.in_(LEXICON))
async def lex_call(callback: CallbackQuery, state: FSMContext):
    print(LEXICON[callback.data])
    # await state.update_data(country=LEXICON[callback.data])
    # await state.set_state(FSMFillForm.fill_country)
    # print(state)
    await callback.answer(LEXICON[callback.data])
    await callback.message.answer(text=f'Ви обрали {LEXICON[callback.data]}')
    # await bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
    #                                     reply_markup=None)
    user_id = callback.from_user.id
    if user_id in user_data_dict:
        user_data_dict[user_id]["country"] = str(LEXICON[callback.data])



@dp.callback_query(F.data.in_(PROFESSION))
async def lex_call(callback: CallbackQuery):
    print(PROFESSION[callback.data])
    await callback.answer(PROFESSION[callback.data])
    await callback.message.answer(text=f'Ви обрали {PROFESSION[callback.data]}')
    # await bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
    #                                     reply_markup=None)
    user_id = callback.from_user.id
    if user_id in user_data_dict:
        user_data_dict[user_id]["profession"] = str(PROFESSION[callback.data])


@dp.callback_query()
async def last(callback: CallbackQuery):
    print(callback.data)
    await callback.answer(text=f'{callback.data}')
    if callback.data == 'last_btn_country':
        await bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                            reply_markup=None)
        keyboard = create_inline_kb_prof(4, last_btn='last_p', **PROFESSION)
        await callback.message.answer(text='Вибір професій',
                             reply_markup=keyboard)
    else:
        await bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                            reply_markup=None)
        await callback.answer(text=f'{callback.data}')
        data_vac = load_data_from_json()
        await callback.message.answer(text='Ось вакансії ')
        if callback.from_user.id in user_data_dict:
            print(user_data_dict[callback.from_user.id])
            for item in data_vac:
                if item['Країна'] == user_data_dict[callback.from_user.id]['country'] and item['Вакансія'] == user_data_dict[callback.from_user.id]['profession']:
                    print(item)
                    formatted_text = f"<b>Номер вакансії:</b> {item['Номер вакансії']}\n" \
                                     f"<b>Країна:</b> {item['Країна']}\n" \
                                     f"<b>Вакансія:</b> {item['Вакансія']}\n" \
                                     f"<b>Плата:</b> {item['Плата']}"
                    await callback.message.answer(text=formatted_text, parse_mode="HTML")
                else:
                    await callback.message.answer(text="Вибачайте, наразі немає варансій по вашому запиту, можливо виберіть іншу країну або професію")
                    break




if __name__ == '__main__':
    print('Зчитування з таблиці')
    writing_to_json()
    print("Успішно записано ")
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

    dp.run_polling(bot)
