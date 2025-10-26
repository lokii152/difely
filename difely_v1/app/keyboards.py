from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# main = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='Catalog')],
#     [KeyboardButton(text='Profile'), KeyboardButton(text='Info')]
# ],
#                         # resize_keyboard=True, уменьшить кнопки
#                         input_field_placeholder='Use menu.')

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Исполнители', callback_data='catalog')],
    [InlineKeyboardButton(text='Профиль', callback_data='profile'), InlineKeyboardButton(text='Информация', callback_data='info')]
])

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='YouTube', url='https://youtube.com/')]
    ])


#список исполнителей
artists = ['basta', 'morgenshtern', 'ladygaga', 'fdsfsdfsd', 'dastrv', 'dawojkcoi', 'dasdsa', 'fvovo', 'lvooo', 'amwnn', 'fewqq',
           'fsdfsaaa', 'fsdivui', 'aswiiuiv', 'pppp', 'fpzpo', 'qwnvjx', 'dkoiiii', 'zopc[[[[', 'fpvknnwn']

async def inline_art():
    keyboard = InlineKeyboardBuilder()
    for art in artists:
        keyboard.add(InlineKeyboardButton(text=art, url='https://youtube.com/'))
    return keyboard.adjust(2).as_markup()