# import os
# import aiogram
# from aiogram import Bot, types, Dispatcher, F
# from aiogram.filters.command import Command
# from aiogram.filters import CommandStart
# from aiogram.types import (CallbackQuery, InlineKeyboardButton,
#                            InlineKeyboardMarkup, Message)
# from spreadsheet import get_data_from_spreadsheet, existing_sheets
# from Json_funk import writing_to_json # creating or recreating data.json
# from keyboards import LEXICON, PROFESSION, create_inline_kb_country, create_inline_kb_prof, generate_next_step_kb, data
#
#
# API_TOKEN = os.getenv('TOKEN')
# bot: Bot = Bot(token=API_TOKEN, parse_mode='HTML')
# dp: Dispatcher = Dispatcher()
#
#
# # get_data_from_spreadsheet()
# #
# # existing_sheets()
# # writing_to_json()
#
#
# @dp.message(CommandStart())
# async def process_start_command(message: Message):
#     keyboard = create_inline_kb_country(4, last_btn='last', **LEXICON)
#     await message.answer(text='Вибір країни',
#                          reply_markup=keyboard)
#
#
# @dp.message(Command('prof'))
# async def cmd_prof(message: types.Message):
#     keyboard = create_inline_kb_prof(4, last_btn='last', **PROFESSION)
#     await message.answer(text='Вибір професій',
#                          reply_markup=keyboard)
#
# selected_counry = []
# selected_prof = []
# selected_data = []
#
#
#
#
# @dp.callback_query()
# async def callback(callback: CallbackQuery):
#     print(callback.data)
#     if 'country' in str(callback.data):
#         if 'last' not in str(callback.data):
#             if LEXICON[callback.data] not in selected_counry:
#                 selected_counry.append(LEXICON[callback.data])
#             else:
#                 selected_counry.remove(LEXICON[callback.data])
#             await callback.answer(f'Ви обрали {LEXICON[callback.data]}')
#             # await callback.answer(show_keyboard=False)
#             # await callback.message.answer("Next", reply_markup=keyboard)
#         else:
#             selecteds = []
#             for item in data:
#                 if item['Країна'] in selected_counry:
#                     selecteds.append(item['Вакансія'])
#             selecteds = list(set(selecteds))
#             print(selecteds)
#             NEXT = generate_next_step_kb((len(selecteds)-1), selecteds)
#             print(NEXT)
#             keyboard = create_inline_kb_prof(4, last_btn='last_btn_country', **NEXT)
#             await callback.message.answer(text="Ось доступні професії")
#             await callback.message.answer(text='Вакансії',reply_markup=keyboard)
#
#     elif 'next' in str(callback.data):
#         selecteds = []
#         for item in data:
#             if item['Країна'] in selected_counry:
#                 selecteds.append(item['Вакансія'])
#         selecteds = list(set(selecteds))
#         NEXT = generate_next_step_kb((len(selecteds) - 1), selecteds)
#         if NEXT[callback.data] not in selected_prof:
#             selected_prof.append(NEXT[callback.data])
#         else:
#             selected_prof.remove(NEXT[callback.data])
#         await callback.answer(f'{NEXT[callback.data]}')
#
#
#     # elif 'last_btn' == str(callback.data):
#
#
#
#     elif 'last' not in str(callback.data):
#         if PROFESSION[callback.data] not in selected_prof:
#             selected_prof.append(PROFESSION[callback.data])
#         else:
#             selected_prof.remove(PROFESSION[callback.data])
#         await callback.answer(f'{PROFESSION[callback.data]}')
#     elif 'last_btn_country' in str(callback.data):
#         await callback.answer("Next step")
#
#     print(selected_counry)
#     print(selected_prof)
#
#     for item in data:
#         if item['Країна'] in selected_counry:
#             if item['Вакансія'] in selected_prof:
#                 if item not in selected_data:
#                     selected_data.append(item)
#                 print(item)
#
#     print(selected_data)
#
#     if 'last_btn' in str(callback.data):
#
#         for vacancy in selected_data:
#             await callback.message.answer(
#                 f"Номер вакансії: {vacancy['Номер вакансії']}\nКраїна: {vacancy['Країна']}\nВакансія: {vacancy['Вакансія']}\nПлата: {vacancy['Плата']}")
#
#
# @dp.message(Command('res'))
# async def res(message: types.Message):
#     print(selected_data)
#     vacancies = selected_data
#     for vacancy in vacancies:
#         await message.answer(
#             f"Номер вакансії: {vacancy['Номер вакансії']}\nКраїна: {vacancy['Країна']}\nВакансія: {vacancy['Вакансія']}\nПлата: {vacancy['Плата']}")
#
#
# if __name__ == '__main__':
#     dp.run_polling(bot)
