from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
from app.middlewares import TestMiddleware

router_h = Router()

router_h.message.outer_middleware(TestMiddleware())

# /start
@router_h.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет, это бот Difely') #reply_markup=await kb.inline_art())  # answer просто отправка сообщ


# /help
@router_h.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Всё работает')


# text
@router_h.message(F.text == '!')
async def how_are_you(message: Message):
    await message.reply(        # reply ответ на сообщ
        f'Your ID: {message.from_user.id}\nYour name: {message.from_user.first_name}',
    reply_markup=kb.main)


# id photo
@router_h.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID photo: {message.photo[-1].file_id}')  # Photo id


# send photo with id
@router_h.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(
        photo='AgACAgIAAxkBAAMWaPkp5CRCpuwt-m17_pjROo2U948AAvD_MRtfkMhLzXpzk81VRksBAAMCAAN4AAM2BA',
        caption='dsadsad')


@router_h.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.answer('') #show_alert=True - notif wind
    await callback.message.edit_text('Список исполнителей', reply_markup=await kb.inline_art())


