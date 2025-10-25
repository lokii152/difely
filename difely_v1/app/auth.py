from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

router_auth = Router()

class Auth(StatesGroup):
    login = State()
    email = State()
    number = State()
    password = State()

@router_auth.message(Command('auth'))
async def auth_one(message: Message, state: FSMContext):
    await state.set_state(Auth.email)
    await message.answer('Введите почту')

@router_auth.message(Auth.email)
async def two_three(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await state.set_state(Auth.password)
    await message.answer('Введите пароль')

@router_auth.message(Auth.password)
async def three_four(message: Message, state: FSMContext):
    await state.update_data(password=message.text)
    data = await state.get_data()
    await message.answer(f'Авторизация завершена.\nПочта: {data['email']}\nПароль:{data['password']}')
    await state.clear()