from aiogram import types

from loader import dp
from filters import IsPriver

# Echo bot
@dp.message_handler(IsPriver(),state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)
