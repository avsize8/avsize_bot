import asyncio
import datetime
import logging
import os
import random
import secrets
import sys
from datetime import datetime

from dotenv import find_dotenv, load_dotenv
from aiogram import *
from aiogram.filters import CommandStart, Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.markdown import hbold
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher, F, Router, html, types
from aiogram.enums import ParseMode
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import KeyboardButton,Message,ReplyKeyboardMarkup, ReplyKeyboardRemove


load_dotenv(find_dotenv())
logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.getenv('TOKEN'), parse_mode=ParseMode.HTML)
router = Router()
ALLOWED_UPDATES = ['message, edited_message']
dp = Dispatcher()


class Reg(StatesGroup):
    days = State()
    mounts = State()


@router.message(CommandStart())
async def start_cmd(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="NICK",
        callback_data="random_nick")
    )
    builder.add(types.InlineKeyboardButton(
        text="PASSWORD",
        callback_data="random_password"
    ))
    await message.answer(
        f"Команда start специально для тебя, {message.from_user.full_name}",
        reply_markup=builder.as_markup()
    )
    await message.delete()


@router.message(Command('help'))
async def start_cmd(message: types.Message):
    await message.reply(f"Так если тебе нужна помощь,ты  {hbold(message.from_user.full_name)},"
                        f"можешь обратиться к админестрации:\n" 
                        f"https://t.me/avsize ")


@router.message(Command('support'))
async def support_handler(message: types.Message):
    await message.reply(f"Если есть желание поддержать проект?💸 \n"
                        f"\n"
                        f"    💳:tinkoff 💲 2200701068800454  ")


nicks = ['zitrezy', 'gentlecarnivore', 'yoshihiro', 'kurosaki', 'idzend', 'hatemysalfe',
         'all-mute', 'Sadness', 'Dan4ous', 'knyko', 'rain', 'ALL MUTE', 'codevi', 'fearless', 'broken', 'of. moon',
         'мракобес', 'ˢʰᵃᵈᵒʷ', 'Rakuzan', 'aomine', 'knyko', 'Lifeless Soul', 'Lifeless Soul', 'Soulless Being',
         'Hollow Spirit', 'Emotionless Existence', 'Voided Essence', 'Numb Soul', 'Deadened Heart', 'Lifeless Vessel',
         'Soul in Darkness', 'Empty Shell', 'Desolate Being', 'Spiritual Void', 'Nihilistic Soul', 'Soul without Pulse',
         'Lifeless Entity', 'Heart of Stone', 'Emotionally Dead', 'Soul Drained', 'Void within', 'Dead Heartbeat',
         'Soul in Despair', 'Empty Existence', 'Lifeless Core', 'Numb Being', 'raddan', 'Spiritual Emptiness',
         'Soul of Darkness', 'Voided Heart', 'Deadened Spirit', 'Lifeless Vortex', 'Soul without Hope', 'Empty Husk',
         'Desolate Soul', 'Spiritual Abyss', 'Nihilistic Existence', 'Soul in Silence', 'Heart of Darkness',
         'Emotionally Numb', 'Soul Drained of Life', 'Deadened Being', 'Lifeless Echo', 'Soul in Desolation',
         'Empty Vessel', 'Desolate Heart', 'Soul without Purpose', 'Hollowed Core', 'Emotionless Vortex ']

awg = ['殺', '別', '田', '最', '高', '123', '†', '斯', '坦', '尼', '斯', '会', '文', '社', '777',
       '111', 'xd', 'dx', '666']


@router.message(Command('nick'))
async def nick_cmd(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="PRESS ON ME",
        callback_data="random_nick")
    )
    builder.add(types.InlineKeyboardButton(
        text="MENU",
        callback_data="menu")
    )
    await message.answer(
        "Нажмите на кнопку, чтобы бот отправил ник",
        reply_markup=builder.as_markup()
    )


@router.callback_query(F.data == "random_nick")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.reply(str(random.choice(nicks) + (random.choice(awg))))


p = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$", "&", "*", "a", 'b', 'c', 'd', 'e', 'f', 'g',
     'h',
     'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E',
     'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


@router.message(Command('password'))
async def password_cmd(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="PRESS ON ME",
        callback_data="random_password")
    )
    builder.add(types.InlineKeyboardButton(
        text="MENU",
        callback_data="menu")
    )
    await message.answer(
        "Нажмите на кнопку, чтобы бот отправил пароль",
        reply_markup=builder.as_markup()
    )
    

@router.callback_query(F.data == "random_password")
async def send_random_password(callback: types.CallbackQuery):
    await callback.message.reply(str(secrets.choice(p) + secrets.choice(p) + secrets.choice(p) + secrets.choice(p) +
                                     secrets.choice(p) + secrets.choice(p) + secrets.choice(p) + secrets.choice(p)))
    

@router.message(Command("birthday"))
async def data(message: types.Message, state:FSMContext):
    await state.set_state(Reg.days)
    await message.answer("Введите день в формате '00':")


@router.message(Reg.days)
async def give(message: types.Message, state:FSMContext):
    await state.update_data(days=message.text)
    await state.set_state(Reg.mounts)
    await message.answer("Введите месяц в формате '00':")

    
date1 = datetime.now()


@router.message(Reg.mounts)
async def give_1(message: types.Message, state:FSMContext):
    await state.update_data(mounts=message.text)
    data  = await state.get_data()
    day = int(data['days'])
    month = int(data['mounts'])
    year = date1.year
    date2  = (datetime(day = day,month = month,year = year))
    timedelta = (date2 - date1)
    date3 = (datetime(day = day,month = month,year = 2025))
    timedelta2 = (date3 - date1)
    if int(timedelta.days)<0:
        await message.answer(f"Кол-во дней до ДР:{int(timedelta2.days)}")
    if int(timedelta.days)>=0:   
        await message.answer(f"Кол-во дней до ДР: {int(timedelta.days)}")
    await state.clear()


@router.callback_query(F.data == "back")
async def back_callback(callback: types.CallbackQuery):
    await callback.answer(Command=CommandStart())

@router.message()
async def idk(massage: types.Message):
    await massage.answer(f"Простите, я вас не понимаю")



async def main() -> None:
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
