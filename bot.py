# - *- coding: utf- 8 - *-
import datetime
import telebot
import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text.lower() == "link":
        date = datetime.datetime.today()
        time = datetime.datetime.now()
        times = [time.hour, time.minute]
        local = times[0] + 6
        if local > 23:
            local = local - 24
        if date.strftime('%A') == 'Monday':
            if local >= 9 and local < 11:
                bot.send_message(message.chat.id,
                                 "Ближайшая пара с 10:30 до 12:35 - YAZILIM MÜHENDİSLİĞİ GÜLŞAT MUHAMEDCANOVA")
                bot.send_message(message.chat.id, "https://meet.google.com/ngd-jqdc-zpd")

            elif local >= 11 and local < 13:
                bot.send_message(message.chat.id,
                                 "Ближайшая пара с 10:30 до 12:35 - YAZILIM MÜHENDİSLİĞİ GÜLŞAT MUHAMEDCANOVA")
                bot.send_message(message.chat.id, "https://meet.google.com/ngd-jqdc-zpd")

            elif local >= 13 and local < 14:
                bot.send_message(message.chat.id,
                                 "Ближайшая пара с 13:30 до 14:40 - PROGRAMLAMA DİLLERİ VE TEKNİKLERİ II GÜLŞAT MUHAMEDCANOVA")
                bot.send_message(message.chat.id, "https://meet.google.com/hqd-qdhk-kxa")

            elif local >= 14 and local < 16:
                bot.send_message(message.chat.id,
                                 "Ближайшая пара с 15:00 до 16:20 - BİLGİ SİSTEMLERİNİN YÖNETİMİ GÜLŞAT MUHAMEDCANOVA")
                bot.send_message(message.chat.id, "https://meet.google.com/oru-vqah-zth")

            else:
                bot.send_message(message.chat.id, "Можешь поспать, пар пока нету")


        ######################################################################

        elif date.strftime('%A') == 'Tuesday':

            if local >= 9 and local < 11:
                bot.send_message(message.chat.id,
                                 "Ближайшая пара с 9:45 до 11:05 - BİLGİ SİSTEMLERİNİN YÖNETİMİ GÜLŞAT MUHAMEDCANOVA")
                bot.send_message(message.chat.id, "https://meet.google.com/oww-awkc-fzu")

            elif local >= 11 and local < 13:
                bot.send_message(message.chat.id,
                                 "Ближайшая пара с 11:15 до 12:35 - İŞ GÜVENLİĞİ VE SAĞLIĞI NAZGÜL CUMABAYEVA")
                bot.send_message(message.chat.id, "https://meet.google.com/jyi-zsyg-tch")

            elif local >= 13 and local < 14:
                bot.send_message(message.chat.id,
                                 "Ближайшая пара с 13:30 до 14:40 - VERİ TABANI VE YÖNETİMİ MAYRAMBEK TEMİROV")
                bot.send_message(message.chat.id, "https://meet.google.com/zpt-wtwz-qrr")

            elif local >= 14 and local < 16:
                bot.send_message(message.chat.id,
                                 "Ближайшая пара с 15:00 до 16:20 - KISMI TÜREVLİ DİFERANSİYEL DENKLEMLER II TAALAYBEK KARAKEEV")
                bot.send_message(message.chat.id, "https://meet.google.com/oru-vqah-zth")

            else:
                bot.send_message(message.chat.id, "Можешь поспать, пар пока нету")

        ######################################################################

        elif date.strftime('%A') == 'Wednesday':

            if local >= 9 and local < 11:
                bot.send_message(message.chat.id,
                                 "Ближайшая пара с 9:45 до 11:05 - VERİ TABANI VE YÖNETİMİ MAYRAMBEK TEMİROV")
                bot.send_message(message.chat.id, "https://meet.google.com/zpt-wtwz-qrr")


            elif local >= 11 and local < 13:
                bot.send_message(message.chat.id,
                                 "Ближайшая пара с 11:15 до 12:35 - SAYISAL ANALİZ II TAALAYBEK KARAKEEV")
                bot.send_message(message.chat.id, "https://meet.google.com/oru-vqah-zth")


            elif local >= 13 and local < 14:
                bot.send_message(message.chat.id,
                                 "Ближайшая пара с 13:30 до 14:50 - İŞ GÜVENLİĞİ VE SAĞLIĞI NAZGÜL CUMABAYEVA")
                bot.send_message(message.chat.id, "https://meet.google.com/jyi-zsyg-tch")

            elif local >= 14 and local < 16:
                bot.send_message(message.chat.id,
                                 "Ближайшая пара с 15:00 до 16:20 - KISMI TÜREVLİ DİFERANSİYEL DENKLEMLER II TAALAYBEK KARAKEEV")
                bot.send_message(message.chat.id, "https://meet.google.com/oru-vqah-zth")
            elif local >= 16 and local <= 17:
                bot.send_message(message.chat.id,
                                 "Ближайшая пара с 16:30 до 17:50 - SAYISAL ANALİZ II TAALAYBEK KARAKEEV")
                bot.send_message(message.chat.id, "https://meet.google.com/oru-vqah-zth")

            else:
                bot.send_message(message.chat.id, "Можешь поспать, пар пока нету")

            ######################################################################

        elif date.strftime('%A') == 'Thursday':
            if local >= 8 and local < 11:
                bot.send_message(message.chat.id,
                                 "Ближайшая пара с 9:00 до 10:20 - SİSTEM VE UYGULAMA YAZILIMI MAYRAMBEK TEMİROV")
                bot.send_message(message.chat.id, "https://meet.google.com/rxw-wtgv-zzd")

            elif local >= 11 and local < 13:
                bot.send_message(message.chat.id,
                                 "Ближайшая пара с 11:15 до 12:35 - BİLGİSAYAR ANİMASYONUNA GİRİŞ MAHABAT AMANALİEVA")
                bot.send_message(message.chat.id, "https://meet.google.com/ace-ynpx-har")

            elif local >= 13 and local < 14:
                bot.send_message(message.chat.id,
                                 "Ближайшая пара с 13:30 до 14:50 - SİSTEM VE UYGULAMA YAZILIMI MAYRAMBEK TEMİROV")
                bot.send_message(message.chat.id, "https://meet.google.com/rxw-wtgv-zzd")

            elif local >= 14 and local < 16:
                bot.send_message(message.chat.id,
                                 "Ближайшая пара с 15:00 до 16:20 - PROGRAMLAMA DİLLERİ VE TEKNİKLERİ II GÜLŞAT MUHAMEDCANOVA")
                bot.send_message(message.chat.id, "https://meet.google.com/hqd-qdhk-kxa")
            elif local >= 16 and local <= 17:
                bot.send_message(message.chat.id,
                                 "Ближайшая пара с 16:30 до 17:50 - BİLGİSAYAR ANİMASYONUNA GİRİŞ MAHABAT AMANALİEVA")
                bot.send_message(message.chat.id, "https://meet.google.com/ace-ynpx-har")
            else:
                bot.send_message(message.chat.id, "Можешь поспать, пар пока нету")

        elif date.strftime('%A') == 'Friday' or date.strftime('%A') == 'Saturday' or date.strftime('%A') == 'Sunday':
            bot.send_message(message.chat.id, "Сегодня пар нету")

    elif message.text.lower() == "стая":
        bot.send_message(message.chat.id, "Ауф")


bot.polling(none_stop=True)

