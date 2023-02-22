import telebot  # 4.9.0 version library
from telebot import types
import os

bot = telebot.TeleBot('', parse_mode='html')


def up_data(a_level, cid):
    with open(f'data_user/{cid}.txt', 'wb'):  # clean file
        pass

    f = open(f'data_user/{cid}.txt', 'w')
    f.write(str(a_level))
    f.close()


def up_data_2(cid):  # clean file and write 0
    with open(f'data_user/{cid}.txt', 'wb'):  # clean file
        pass

    f = open(f'data_user/{cid}.txt', 'w')
    f.write(str('0'))
    f.close()


@bot.message_handler(commands=['start'])
def welcome(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Up level")

    markup.add(item1)

    bot.send_message(m.chat.id,
                     "Hello, <b>{0.first_name}</b>!\nI understand what use me only you... \nHonor and good luck".format(
                         m.from_user, bot.get_me()), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def main(m):
    cid = m.chat.id  # get user info
    filename = f"{cid}.txt"  # name file
    directory = "data_user"  # directory file
    if m.chat.type == 'private':
        if m.text == 'Up level':

            if os.path.isfile(os.path.join(directory, filename)):  # if user register
                pass

            else:
                new_file = open(f'data_user/{cid}.txt', 'w')
                new_file.write('0')
                new_file.close()

            the_level = []
            with open(f'data_user/{cid}.txt') as f:  # write data to variable
                for line in f:
                    the_level.extend([int(x) for x in line.split()])
            the_level = the_level[0] + 1

            if the_level < 100:
                up_data(the_level, cid)
                photo = open(f'level_img/{the_level}.png', 'rb')
                bot.send_photo(m.chat.id, photo)
                bot.send_message(m.chat.id, f'Your next level {the_level}!')

            else:
                up_data(the_level, cid)
                photo = open(f'level_img/{the_level}.png', 'rb')
                bot.send_photo(m.chat.id, photo)
                bot.send_message(m.chat.id,
                                 f'Your next level {the_level}!\nYou’ve reached the maximum level!\nCongratulations again, everyone! ')
                up_data_2(cid)
                bot.send_message(m.chat.id, 'Level of anylation')

        else:
            bot.send_message(m.chat.id, 'I can only level up')


bot.polling(none_stop=True)
