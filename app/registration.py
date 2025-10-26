from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

router_reg = Router()

class Reg(StatesGroup):
    login = State()
    email = State()
    number = State()
    password = State()

@router_reg.message(Command('reg'))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.login)
    await message.answer('Введите логин')

@router_reg.message(Reg.login)
async def two_three(message: Message, state: FSMContext):
    await state.update_data(login=message.text)
    await state.set_state(Reg.email)
    await message.answer('Введите эл.почту')

@router_reg.message(Reg.email)
async def two_three(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await state.set_state(Reg.number)
    await message.answer('Введите номер телефона')

@router_reg.message(Reg.number)
async def one_two(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    await state.set_state(Reg.password)
    await message.answer('Введите пароль')

@router_reg.message(Reg.password)
async def three_four(message: Message, state: FSMContext):
    await state.update_data(password=message.text)
    data = await state.get_data()
    await message.answer(f'Регистрация завершена.\nПочта: {data['email']}\nНомер: {data['number']}\n'
                         f'Логин:{data['login']}\nПароль:{data['password']}')
    await state.clear()