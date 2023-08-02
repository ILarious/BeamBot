from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_kb_start() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    b_calculation = KeyboardButton('Начать расчет')
    b_help = KeyboardButton('Help')
    kb.add(b_calculation, b_help)

    return kb


def get_kb_cancel() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Отменить'))

    return kb


def get_kb_next() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Продолжить'))

    return kb


def get_kb_metal() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb_1 = KeyboardButton('C38/23')
    kb_2 = KeyboardButton('C44/29')
    kb_3 = KeyboardButton('C46/33')
    kb_4 = KeyboardButton('C52/40')
    kb_5 = KeyboardButton('C60/45')
    kb_6 = KeyboardButton('C70/60')
    kb_7 = KeyboardButton('C85/75')
    kb.add(kb_1, kb_2, kb_3, kb_4, kb_5, kb_6, kb_7)

    return kb