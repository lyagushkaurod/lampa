import asyncio
import os
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import CommandStart, or_f, Command
from aiogram import F
from aiogram.methods import send_photo

from keyboards import reply

user_router = Router()


@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Привет! Это бот для онлайн-бронирования в тайм-кафе Lampa. Что ты хочешь?',
                         reply_markup=reply.start_kb.as_markup(
                             resize_keyboard=True,
                             input_field_placeholder='Что вас интересует?'
                         ))

@user_router.message(F.text.lower() == 'о нас')
async def abt(message: types.Message):
    with open('about_us.txt', 'r', encoding='utf-8') as file:
        abt_txt = file.read()
    await message.answer(abt_txt,
                         reply_markup=reply.start_bro.as_markup(
                             resize_keyboard=True,
                             input_field_placeholder='Что вас интересует?'
                         ))

@user_router.message(F.text.lower() == 'забронировать')
async def bron(message: types.Message):
    await message.answer('Конечно! За чем вы бы хотели провести время?',
                         reply_markup=reply.bron_kb.as_markup(
                             resize_keyboard=True,
                             input_field_placeholder='Выберите где хотите посидеть'
                         ))

@user_router.message(F.text.lower() == 'консоль')
async def cons(message: types.Message):
    await message.answer('За какой консолью тебе хотелось бы посидеть?',
                         reply_markup=reply.console_kb.as_markup(
                             resize_keyboard=True,
                             input_field_placeholder='Выберите консоль'
                         ))

@user_router.message(F.text.lower() == 'приватный зал' or 'назад')
async def privat(message: types.Message):
    await message.answer('Сколько человек планируется?',
                         reply_markup=reply.privat_kb.as_markup(
                             resize_keyboard=True,
                             input_field_placeholder='Выберите кол-во человек'
                         ))

@user_router.message(F.text.lower() == 'до 10')
async def fiol(message: types.Message):
    with open('fiol.txt', 'r', encoding='utf-8') as file:
        violet = file.read()
    await message.answer_photo('fiol.png',caption=violet,
                              reply_markup=reply.oukey_kb.as_markup(
                                  resize_keyboard=True,
                                  input_field_placeholder='Вам подходит?'
                              ))