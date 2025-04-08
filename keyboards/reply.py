from operator import truediv

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from telebot.types import ReplyKeyboardRemove

start_bro = ReplyKeyboardBuilder()
start_bro.add(
    KeyboardButton(text="Забронировать")
)


start_kb = ReplyKeyboardBuilder()
start_kb.attach(start_bro)
start_kb.row(KeyboardButton(text="О нас"))


bron_kb = ReplyKeyboardBuilder()
bron_kb.add(
        KeyboardButton(text='Приватный зал'),
        KeyboardButton(text='Столик(общий зал)'),
        KeyboardButton(text='Консоль'),
        KeyboardButton(text='ПК'),
)

console_kb = ReplyKeyboardBuilder()
console_kb.add(
    KeyboardButton(text='PlayStation 4'),
    KeyboardButton(text='PlayStation 5'),
    KeyboardButton(text='PlayStation 4 с VR-шлемом')
)

privat_kb = ReplyKeyboardBuilder()
privat_kb.add(
    KeyboardButton(text='До 10'),
    KeyboardButton(text='10-13'),
    KeyboardButton(text='13-16'),
    KeyboardButton(text='16-20'),
)

oukey_kb = ReplyKeyboardBuilder()
oukey_kb.add(
    KeyboardButton(text='Мне подходит'),
    KeyboardButton(text='Назад')
)