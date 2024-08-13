import telebot
import time
photo1 = open("5321530163135112208.jpg",'rb')
photo2 = open("5321530163135112209.jpg",'rb')
photo3 = open("5321530163135112210.jpg",'rb')
photo4 = open("5321530163135112215.jpg",'rb')
photo5 = open("5321530163135112211.jpg",'rb')
photo6 = open("5321530163135112212.jpg",'rb')
photo7 = open("5321530163135112213.jpg ",'rb')
photo8 = open("5321530163135112214.jpg",'rb')
photo9 = open("5321530163135112216.jpg",'rb')
photo10 = open("5321530163135112219.jpg",'rb')
photo11 = open("5321530163135112220.jpg",'rb')
photo12 = open("5321530163135112221.jpg",'rb')

bot =telebot.TeleBot("6640234265:AAFC5Owkusa1_B1F7YCiKJ8EnytmKSojOLg")
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет, этот бот поможет с подготовкой к ОГЭ введите /zadachi')
@bot.message_handler(commands=['zadachi'])
def zadachi(message):
    bot.send_message(message.chat.id,"Выберите номер задачи: /1,/2,/3,/4,/5,/6,/7,/8,/9,/10,/11,/12")
@bot.message_handler(commands=['1'])
def asd(message):
    bot.send_photo(message.chat.id,photo1)
    bot.register_next_step_handler(message,fisting)
def fisting(message):
    if message.text == '34125':
        bot.send_message(message.chat.id,'Вы ответили правильно, молодцы!')
    elif message.text != '34125':
        bot.send_message(message.chat.id, 'К сожалению это неправильный ответ')
@bot.message_handler(commands=['2'])
def sa2(message):
    bot.send_photo(message.chat.id,photo2)
    bot.register_next_step_handler(message, fistingas)
def fistingas(message):
    if message.text == '78':
        bot.send_message(message.chat.id,'Вы ответили правильно, молодцы!')
    elif message.text != '78':
        bot.send_message(message.chat.id, 'К сожалению это неправильный ответ')
@bot.message_handler(commands=['3'])
def sa3(message):
        bot.send_photo(message.chat.id,photo3)
        bot.register_next_step_handler(message, fistings)
def fistings(message):
    if message.text == '132':
        bot.send_message(message.chat.id,'Вы ответили правильно, молодцы!')
    elif message.text != '132':
        bot.send_message(message.chat.id, 'К сожалению это неправильный ответ')
@bot.message_handler(commands=['4'])
def sa4(message):
        bot.send_photo(message.chat.id,photo4)
        bot.register_next_step_handler(message, fistingds)
def fistingds(message):
    if message.text == '-24':
        bot.send_message(message.chat.id,'Вы ответили правильно, молодцы!')
    elif message.text != '-24':
        bot.send_message(message.chat.id, 'К сожалению это неправильный ответ')
@bot.message_handler(commands=['5'])
def sa5(message):
        bot.send_photo(message.chat.id,photo5)
        bot.register_next_step_handler(message, fistinggs)
def fistinggs(message):
    if message.text == '9,1':
        bot.send_message(message.chat.id,'Вы ответили правильно, молодцы!')
    elif message.text != '9,1':
        bot.send_message(message.chat.id, 'К сожалению это неправильный ответ')
@bot.message_handler(commands=['6'])
def sa6(message):
        bot.send_photo(message.chat.id,photo6)
        bot.register_next_step_handler(message, fistinghg)
def fistinghg(message):
    if message.text == '5':
        bot.send_message(message.chat.id,'Вы ответили правильно, молодцы!')
    elif message.text != '5':
        bot.send_message(message.chat.id, 'К сожалению это неправильный ответ')

@bot.message_handler(commands=['7'])
def sa7(message):
        bot.send_photo(message.chat.id,photo7)
        bot.register_next_step_handler(message, fistang)
def fistang(message):
    if message.text == '3':
        bot.send_message(message.chat.id,'Вы ответили правильно, молодцы!')
    elif message.text != '3':
        bot.send_message(message.chat.id, 'К сожалению это неправильный ответ')
@bot.message_handler(commands=['8'])
def sa8(message):
        bot.send_photo(message.chat.id,photo8)
        bot.register_next_step_handler(message, fistingc)
def fistingc(message):
    if message.text == '1':
        bot.send_message(message.chat.id,'Вы ответили правильно, молодцы!')
    elif message.text != '1':
        bot.send_message(message.chat.id, 'К сожалению это неправильный ответ')

@bot.message_handler(commands=['9'])
def sa8s(message):
        bot.send_photo(message.chat.id,photo9)
        bot.register_next_step_handler(message, fistinddgc)
def fistinddgc(message):
    if message.text == '0,625':
        bot.send_message(message.chat.id,'Вы ответили правильно, молодцы!')
    elif message.text != '0,625':
        bot.send_message(message.chat.id, 'К сожалению это неправильный ответ')
@bot.message_handler(commands=['10'])
def sa8s(message):
        bot.send_photo(message.chat.id,photo10)
        bot.register_next_step_handler(message, afistinddgc)
def afistinddgc(message):
    if message.text == '50':
        bot.send_message(message.chat.id,'Вы ответили правильно, молодцы!')
    elif message.text != '50':
        bot.send_message(message.chat.id, 'К сожалению это неправильный ответ')
@bot.message_handler(commands=['11'])
def sa8s(message):
        bot.send_photo(message.chat.id,photo11)
        bot.register_next_step_handler(message, faistinddgc)
def faistinddgc(message):
    if message.text == '40':
        bot.send_message(message.chat.id,'Вы ответили правильно, молодцы!')
    elif message.text != '40':
        bot.send_message(message.chat.id, 'К сожалению это неправильный ответ')
@bot.message_handler(commands=['12'])
def sa8s(message):
        bot.send_photo(message.chat.id,photo12)
        bot.register_next_step_handler(message, fidstinddgc)
def fidstinddgc(message):
    if message.text == '234':
        bot.send_message(message.chat.id,'Вы ответили правильно, молодцы!')
    elif message.text != '234':
        bot.send_message(message.chat.id, 'К сожалению это неправильный ответ')



bot.polling(non_stop=True)