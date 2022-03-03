from aiogram import types, Dispatcher
from create_bot import dp



# @dp.message_handler()
async def echo_send(message: types.Message):
    if message.text == "Привет":
        await message.answer("И тебе привет!")
    # await message.reply(message.text)
    await message.answer(message.text)

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)