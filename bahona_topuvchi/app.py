from aiogram import Bot, Dispatcher, types
import random

API_TOKEN = '6257158066:AAH7bXfG_HRrA75jUmNkkNR6nqUZF79Y7Kk'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

EXCUSES_FILE = 'excuses.txt'
excuses = []

# Bot ishga tushgani bilan excuses.txt ni ko'rsata boshlaydi
with open(EXCUSES_FILE, 'r') as f:
    for line in f:
        excuses.append(line.strip())


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        "Salom, Men bilan turli vaziyatlarga mos bahonlar toping.\nBahona topish uchun /search ni bosing")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("/start - botni qayta ishga tushirish\n/search - bahonalarni topish\n/add - bahona qo'shish")


async def show(message: types.Message):
    # Get the total number of items in the list
    total_items = len(excuses)
    # Send a message with the total number of items to the user
    await message.answer(f"Hozirgacha ro'yhatda {total_items} ta bahona mavjud  ")


async def search(message: types.Message):
    # Get a random element from the list
    random_element = random.choice(excuses)
    # Send a message with the random element to the user
    await message.answer(random_element)


async def add(message: types.Message):
    # Get the item to add from the message
    item = message.text.replace('/add ', '')
    # Add the item to the list

    excuses.append(item)
    # Write the updated list to the file
    with open(EXCUSES_FILE, 'a') as f:
        f.write(item + '\n')
    # Send a confirmation message to the user
    await message.answer(f"Bu bahona ro'yhatga qo'shildi\n'{item}'  ")






dp.register_message_handler(search, commands=['search'])
dp.register_message_handler(add, commands=['add'])
dp.register_message_handler(show, commands=['show'])


if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.create_task(dp.start_polling())
        loop.run_forever()
    finally:
        loop.stop()


