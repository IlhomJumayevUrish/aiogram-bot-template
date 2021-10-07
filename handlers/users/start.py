from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from filters import IsPriver

@dp.message_handler(IsPriver(),CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name} Shaxsiy! ")
