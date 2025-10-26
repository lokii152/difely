from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from app.database.requests import get_performers, get_perf_song

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Исполнители')],
    [KeyboardButton(text='Профиль'), KeyboardButton(text='Информация')]
],
                        # resize_keyboard=True, уменьшить кнопки
                        input_field_placeholder='Use menu.')

# main = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Исполнители', callback_data='catalog')],
#     [InlineKeyboardButton(text='Профиль', callback_data='profile'), InlineKeyboardButton(text='Информация', callback_data='info')]
# ])

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='YouTube', url='https://youtube.com/')]
    ])


#inlinekb of performers
async def performers():
    all_performers = await get_performers()
    keyboard = InlineKeyboardBuilder()
    for performer in all_performers:
        keyboard.add(InlineKeyboardButton(text=performer.name, callback_data=f"performer_{performer.id}"))
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()

#inlinekb of songs
async def songs(performer_id):
    all_songs = await get_perf_song(performer_id)
    keyboard = InlineKeyboardBuilder()
    for song in all_songs:
        keyboard.add(InlineKeyboardButton(text=song.name, callback_data=f"song_{song.id}"))
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()

