from aiogram import Bot, Dispatcher, types
import random

API_TOKEN = '6257158066:AAH7bXfG_HRrA75jUmNkkNR6nqUZF79Y7Kk'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

EXCUSES_FILE = 'excuses.txt'
excuses = []

# Load the excuses from the file when the bot starts up
with open(EXCUSES_FILE, 'r') as f:
    for line in f:
        excuses.append(line.strip())

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
    await message.answer(f"{item} has been added to the list.")

dp.register_message_handler(search, commands=['search'])
dp.register_message_handler(add, commands=['add'])

if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.create_task(dp.start_polling())
        loop.run_forever()
    finally:
        loop.stop()


