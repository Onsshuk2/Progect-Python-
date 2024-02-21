from aiogram import types,Router,F
from aiogram.filters import CommandStart,Command
import random
# from aiogram.untils import executor
import io


FILE_PATH='/Users/admin/Library/Application Support/Code/User/History/79c11cf8/qgWW.py'
user_private_router=Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Hello, I'm your personal bot")

@user_private_router.message(Command('menu'))
async def menu_cmd(message: types.Message):
    await message.answer('MENU: \n1. /start\n2. /menu\n3. /watch\n4. /help\n')  

@user_private_router.message(Command('help'))
async def help_cmd(message: types.Message):
    await message.answer('HELP:I wont help you. Ask your questions and I wil process them') 

@user_private_router.message(Command('watch'))
async def watch_cmd(message: types.Message):
   await message.answer('WATCH: \n1. /EMPORIO_ARMANI_AR607\n2. /Michael_Kors\n3. /Garmin_Tactix_Delta_Sapphire\n4. /JS9_PRO_MAX\n5. /Samsung_Galaxy_Watch\n')  

@user_private_router.message(Command('EMPORIO_ARMANI_AR607'))
async def watch1_cmd(message: types.Message):
    await message.answer('INFO:\n1. /link1\n2. /foto1\n3. /price1\n4. /details') 

@user_private_router.message(Command('link1'))
async def link1_cmd(message: types.Message):
    await message.answer('https://www.olx.ua//d/uk/obyavlenie/godinnik-emporio-armani-ar6073-orignal-komplekt-sertifkat-IDUhOx9.html')

@user_private_router.message(Command('foto1'))
async def foto1_cmd(message: types.Message):
    await message.answer_photo('https://www.olx.ua//d/uk/obyavlenie/godinnik-emporio-armani-ar6073-orignal-komplekt-sertifkat-IDUhOx9.html')

# @user_private_router.message(Command('foto1'))
# async def send_photo_bytes(message: types.Message):
#     with open('handlers/IMG_3795.jpg', 'rb') as image_file:
#         image_bytes = image_file.read()
#     image_stream = io.BytesIO(image_bytes)
#     image_stream.name = 'IMG_3795.jpg'
#     await message.answer_photo(photo=image_stream, caption="EMPORIO_ARMANI_AR607")


@user_private_router.message(Command('price1'))
async def price1_cmd(message: types.Message):
    await message.answer('7999 грн')  

@user_private_router.message(Command('Michael_Kors'))
async def watch2_cmd(message: types.Message):
    await message.answer('INFO:\n1. /link2\n2. /foto2\n3. /prise2\n4. /details')

@user_private_router.message(Command('link2'))
async def link2_cmd(message: types.Message):
    await message.answer('https://www.olx.ua//d/uk/obyavlenie/zhnochiy-godinnik-michael-kors-IDUtfmt.html')

@user_private_router.message(Command('foto2'))
async def foto2_cmd(message: types.Message):
    await message.answer_photo('https://www.olx.ua//d/uk/obyavlenie/zhnochiy-godinnik-michael-kors-IDUtfmt.html')

@user_private_router.message(Command('price2'))
async def price2_cmd(message: types.Message):
    await message.answer('7 400 грн') 

@user_private_router.message(Command('Garmin_Tactix_Delta_Sapphire'))
async def watch3_cmd(message: types.Message):
    await message.answer('INFO:\n1. /link3\n2. /foto3\n3. /prise3\n4. /details')

@user_private_router.message(Command('link3'))
async def link3_cmd(message: types.Message):
    await message.answer('https://www.olx.ua//d/uk/obyavlenie/godinnik-garmin-tactix-delta-sapphire-IDUteZs.html')

@user_private_router.message(Command('foto3'))
async def foto3_cmd(message: types.Message):
    await message.answer_photo('https://www.olx.ua//d/uk/obyavlenie/godinnik-garmin-tactix-delta-sapphire-IDUteZs.html')

@user_private_router.message(Command('price3'))
async def price3_cmd(message: types.Message):
    await message.answer('18 900 грн') 

@user_private_router.message(Command('JS9_PRO_MAX'))
async def watch4_cmd(message: types.Message):
    await message.answer('INFO:\n1. /link4\n2. /foto4\n3. /price4\n4. /details')

@user_private_router.message(Command('link4'))
async def link4_cmd(message: types.Message):
    await message.answer('https://www.olx.ua//d/uk/obyavlenie/smart-godinnik-js9-pro-max-IDUtht4.html')

@user_private_router.message(Command('foto4'))
async def foto4_cmd(message: types.Message):
    await message.answer_photo('https://www.olx.ua//d/uk/obyavlenie/smart-godinnik-js9-pro-max-IDUtht4.html')

@user_private_router.message(Command('price4'))
async def price4_cmd(message: types.Message):
    await message.answer('2 999 грн') 

@user_private_router.message(Command('Samsung_Galaxy_Watch'))
async def watch5_cmd(message: types.Message):
    await message.answer('INFO:\n1. /link5\n2. /foto5\n3. /price5\n4. /details')

@user_private_router.message(Command('link5'))
async def link5_cmd(message: types.Message):
    await message.answer('https://www.olx.ua//d/uk/obyavlenie/smart-godinnik-samsung-galaxy-watch-4-IDUtg91.html')

@user_private_router.message(Command('foto5'))
async def foto5_cmd(message: types.Message):
    await message.answer_photo('https://www.olx.ua//d/uk/obyavlenie/smart-godinnik-samsung-galaxy-watch-4-IDUtg91.html')

@user_private_router.message(Command('price5'))
async def price5_cmd(message: types.Message):
    await message.answer('3 400 грн')

@user_private_router.message(Command('details'))
async def details_cmd(message: types.Message):
    await message.answer('Onishchuk Iruna\n 4441114419281223\n\nAfter payment, write the data for sendingbefore them, indicating /data')

@user_private_router.message(Command('data'))
async def data_cmd(message: types.Message):
    await message.answer('Your data has been successfully received, please wait for a message about sending')


          
@user_private_router.message((F.text.contains("say"))|(F.photo)|(F.audio)|(F.sticker))
async def photo(message: types.Message):
    await message.answer("I see this Message,but tell me why?")

@user_private_router.message()
async def echo(message: types.Message):
    listOf=['hi', 'hello', 'привіт','добрий день']
    text=message.text.lower()
    randomCoice=random.choice(listOf)
    if text in ['hi', 'hello', 'привіт','добрий день']:
        await message.answer(randomCoice)
    elif text in ['by', 'goodbye']:
        await message.answer('By,my friend')
    else:
        await message.answer('i don*t understand, repeat please')
    # await message.answer(message.text)
    # await message.reply(message.text)
    # await message.reply(message.text+str(message.from_user.id))
    