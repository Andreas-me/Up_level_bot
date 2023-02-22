import telebot  # 4.9.0 version library
from telebot import types

bot = telebot.TeleBot('6217176905:AAHXOO-00y4qzE7qLo8smdZMOEYhWrtR-VQ', parse_mode='html')


def up_data(a_level):
    with open('level.txt', 'wb'):  # clean file
        pass

    f = open('level.txt', 'w')
    f.write(str(a_level))
    f.close()


@bot.message_handler(commands=['start'])
def welcome(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Up level")

    markup.add(item1)

    bot.send_message(m.chat.id,
                     "Hello, <b>{0.first_name}</b>!\nI understand what use me only you... \nHonor and good luck".format(
                         m.from_user, bot.get_me()), reply_markup=markup)


# photo1 = open(r"C:\Users\Andreas\Documents\Adobe\Photoshop\level up\new.png", 'rb')
#
#
# @bot.message_handler(commands=['photo'])
# def msg4(message):
#     bot.send_photo(message.chat.id, photo1)

@bot.message_handler(content_types=['text'])
def main(m):
    if m.chat.type == 'private':
        if m.text == 'Up level':

            the_level = []
            with open('level.txt') as f:
                for line in f:
                    the_level.extend([int(x) for x in line.split()])

            the_level = the_level[0] + 1

            up_data(the_level)
            bot.send_message(m.chat.id, f'Your new level {the_level}!')

        else:
            bot.send_message(m.chat.id, 'I can only level up')


bot.polling(none_stop=True)
