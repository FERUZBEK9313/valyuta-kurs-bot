from aiogram import Bot, Dispatcher, types
from aiogram.types import *
from aiogram.utils import executor
import requests
from bs4 import BeautifulSoup as BS

TOKEN = "5609888107:AAFBcryqeCFkokTtM1HsLLIMiAWZwsJxq0o"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

usd=[]
rub= []
eur= []
gbr= []
kzt= []
usd_kurs= []
rub_kurs= []
eur_kurs= []
gbr_kurs= []
kzt_kurs= []
def req():
    global usd,usd_kurs, rub,rub_kurs, eur,eur_kurs, gbr,gbr_kurs, kzt,kzt_kurs
    usd=[]
    rub= []
    eur= []
    gbr= []
    kzt= []
    usd_kurs= []
    rub_kurs= []
    eur_kurs= []
    gbr_kurs= []
    kzt_kurs= []
    r = requests.get('https://bank.uz/currency')
    soup = BS(r.text, 'html.parser')
    src = soup.find_all('div', {'class': 'bc-inner-block-left-text'})
    t=0
    for i in src:
        src1=i.find_all('span', {'class': 'medium-text'})
        s = str(src1)
        t+=1
        if t<=60:
            ss = s[27:len(s)-9]
            usd.append(ss)
        elif 60<t<=116:
            ss = s[27:len(s)-9]
            rub.append(ss)
        elif 116<t<=174:
            ss = s[27:len(s)-9]
            eur.append(ss)
        elif 174<t<=226:
            ss = s[27:len(s)-9]
            gbr.append(ss)
        elif 226<t<=238:
            ss = s[27:len(s)-9]
            kzt.append(ss)

    src = soup.find_all('div', {'class': 'bc-inner-block-left-texts'})
    t=0
    for i in src:
        src1=i.find_all('span', {'class': 'medium-text green-date'})
        s = str(src1)
        t+=1
        if t<=60:
            ss = s[39:len(s)-9]
            usd_kurs.append(ss)
        elif 60<t<=116:
            ss = s[39:len(s)-9]
            rub_kurs.append(ss)
        elif 116<t<=174:
            ss = s[39:len(s)-9]
            eur_kurs.append(ss)
        elif 174<t<=226:
            ss = s[39:len(s)-9]
            gbr_kurs.append(ss)
        elif 226<t<=238:
            ss = s[39:len(s)-9]
            kzt_kurs.append(ss)

menu1 = ReplyKeyboardMarkup(resize_keyboard=True).row('🇺🇸USD','🇷🇺RUB').row('🇪🇺EUR','🇬🇧GBR').row('🇰🇿KZT')
menu2 = ReplyKeyboardMarkup(resize_keyboard=True).row('⬇️Покупка', '⬆️Продажа').row('⬅️Назад')

valyuta = ''

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    fr_name= message.from_user.first_name
    xabar = '👋Здравствуй дорогой ' + str(fr_name) + '. Через этого бота вы сможете узнать курс всех банков нашей республики!\n👇Выберите один из следующих вариантов:'
    await bot.send_message(chat_id=message.chat.id, text=xabar, reply_markup=menu1)

@dp.message_handler()
async def events(message: types.Message):
    global valyuta
    if message.text=='🇺🇸USD':
        valyuta = 'USD'
        await message.reply('👇Выберите один из следующих вариантов:', reply_markup=menu2)
    elif message.text=='🇷🇺RUB':
        valyuta = 'RUB'
        await message.reply('👇Выберите один из следующих вариантов:', reply_markup=menu2)
    elif message.text=='🇪🇺EUR':
        valyuta = 'EUR'
        await message.reply('👇Выберите один из следующих вариантов:', reply_markup=menu2)
    elif message.text=='🇬🇧GBR':
        valyuta = 'GBR'
        await message.reply('👇Выберите один из следующих вариантов:', reply_markup=menu2)
    elif message.text=='🇰🇿KZT':
        valyuta = 'KZT'
        await message.reply('👇Выберите один из следующих вариантов:', reply_markup=menu2)
    elif message.text=='⬇️Покупка':
        req()
        s=''
        if valyuta=='USD':
            for i in range(len(usd)//2):
                s+=f'<b>{str(usd[i])}</b>  -  <i>{str(usd_kurs[i])}</i> ✅\n'
        elif valyuta=='RUB':
            for i in range(len(rub)//2):
                s+=f'<b>{str(rub[i])}</b>  -  <i>{str(rub_kurs[i])}</i> ✅\n'
        elif valyuta=='EUR':
            for i in range(len(eur)//2):
                s+=f'<b>{str(eur[i])}</b>  -  <i>{str(eur_kurs[i])}</i> ✅\n'
        elif valyuta=='GBR':
            for i in range(len(gbr)//2):
                s+=f'<b>{str(gbr[i])}</b>  -  <i>{str(gbr_kurs[i])}</i> ✅\n'
        elif valyuta=='KZT':
            for i in range(len(kzt)//2):
                s+=f'<b>{str(kzt[i])}</b>  -  <i>{str(kzt_kurs[i])}</i> ✅\n'
        await message.answer(s, parse_mode='html')
    elif message.text=='⬆️Продажа':
        req()
        s=''
        if valyuta=='USD':
            for i in range(len(usd)//2, len(usd)):
                s+=f'<b>{str(usd[i])}</b>  -  <i>{str(usd_kurs[i])}</i> ✅\n'
        elif valyuta=='RUB':
            for i in range(len(rub)//2, len(rub)):
                s+=f'<b>{str(rub[i])}</b>  -  <i>{str(rub_kurs[i])}</i> ✅\n'
        elif valyuta=='EUR':
            for i in range(len(eur)//2, len(eur)):
                s+=f'<b>{str(eur[i])}</b>  -  <i>{str(eur_kurs[i])}</i> ✅\n'
        elif valyuta=='GBR':
            for i in range(len(gbr)//2, len(gbr)):
                s+=f'<b>{str(gbr[i])}</b>  -  <i>{str(gbr_kurs[i])}</i> ✅\n'
        elif valyuta=='KZT':
            for i in range(len(kzt)//2, len(kzt)):
                s+=f'<b>{str(kzt[i])}</b>  -  <i>{str(kzt_kurs[i])}</i> ✅\n'
        await message.answer(s, parse_mode='html')
    elif message.text=='⬅️Назад':
        await message.reply('👇Выберите один из следующих вариантов:', reply_markup=menu1)
    
    else:
        await message.delete()
if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)