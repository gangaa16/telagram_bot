from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton

bot = Bot(token='6120743109:AAEWur0rl4QcLQG-apBePEh0XpXrFWAoNQo')
dp = Dispatcher(bot)

button1 = KeyboardButton('Stupid')
button2 = KeyboardButton('Fat')
button3 = KeyboardButton('Dumb')
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(button1).add(button2).add(button3)

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hello! welcome to newBot🤗🤗",reply_markup=keyboard1)

@dp.message_handler()
async def kb_answer(message:types.Message):
    if message.text =='Stupid':
        await message.answer("Yo momma is so stupid when an intruder broke into her house, she ran downstairs, dialed 9-1-1 on the microwave, and couldn't find the CALL button.")
    elif message.text =='Fat':
        await message.answer("Yo Momma is so fat when I told her to touch her toes she said, What are those?")
    elif message.text == 'Dumb':
        await message.answer("Yo momma's so dumb, when y'all were driving to Disneyland, she saw a sign that said Disneyland left, so she went home.")
    else:
        await message.answer(f'Your message is:{message.text}')




if __name__ == '__main__':
    executor.start_polling(dp)