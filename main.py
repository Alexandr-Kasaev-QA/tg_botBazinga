# подключение библиотек
# В google colab добавить: !pip install pyTelegramBotAPI
# для установки необходимо в файл requirements.text добавить строку
# 'PyTelegramBotApi'

from telebot import TeleBot, types
import random


bot = TeleBot(token='7212886473:AAFWcthurver88BaCf7jcpagZdQyFQvoqco', parse_mode='html') # создание бота



brain_list = ["Жарим котлеты. -\nМы располагаем сковородой, на которую помещается две колеты. Нам необходимо пожарить три котлеты за 3 минуты, при том, что одна сторона котлеты жарится ровно 1 минуту (котлеты необходимо прожарить с обеих сторон).\nВопрос:Как прожарить котлеты? Ответ по ссылке\nhttps://chesscomp.ru/golovolomki/20-6", "Тортик -\nПредположим, у нас имеется круглый торт. Нам нужно разрезать его на восемь кусков, при этом сделав только три надреза.Вопрос: как это сделать? Ответ по ссылке\nhttps://www.thevoicemag.ru/lifestyle/stil-zhizni/reshi-etu-zadachu-i-uznay-naskolko-ty-soobrazitelna/","Мудрецы и колпаки -\nЦарь решил проверить своих троих мудрецов на мудрость, пригласил их и сказал: «Мудрецы, у меня есть 5 колпаков – 3 из них черные, а 2 белые. Сейчас вы закроете глаза, и я надену на ваши головы эти колпаки, при этом вы не будете знать, колпак какого цвета у вас на голове, но будете видеть колпаки других мудрецов». После осуществленных действий мудрецы открыли глаза и долго-долго молчали. Затем один из мудрецов произнес: «На моей голове черный колпак!» И он был прав. Вопрос: Как мудрец догадался? Ответ по ссылке.\nhttps://masterok.livejournal.com/3624069.html", "Рыбки -\nИзначально в аквариуме плавает 10 рыбок. Однако спустя неделю 2 из них утонули, 4 – уплыли, а еще 3 – погибли. Сколько рыбок осталось в аквариуме? Ответ по ссылке\nhttps://dumaika.ru/news/ru/123/v-akvariume-10-rybok-zadacha-na-logiku", "Возраст -\nВозраст матери и дочери вместе составляет 77 лет. При этом возраст одной можно получить, если поменять цифры возраста другой.\nСколько лет матери и сколько лет дочери?", "День -\nПеречислите 5 дней подряд, не пользуясь числами или названиями дней недели. Ответ в ссылке\nhttps://reshimvse.com/zadacha.php?id=25955", "Сестры -\nВсе пять сестер чем-то заняты: Катя играет на пианино; Маша стирает; Ольга играет в шахматы; Алиса готовит пирог. Вопрос: Чем занята Наташа? Ответ в ссылке\nhttps://mysweetworld.ru/pereplanirovka-i-remont/v-komnate-5-sester-anya.html", "Напитки -\nНа склад привезли три машины для напитков. Одна из них выдаёт чай, вторая выдаёт кофе, а третья — чай или кофе (определяется случайно). Любой автомат продаст стакан напитка за одну монету. На каждом автомате приклеена этикетка с выдаваемым напитком. Но на заводе произошла ошибка, из-за чего на всех автоматах наклеены не те этикетки, которые должны быть.\nВопрос: сколько потребуется денег, чтобы определить, где какие автоматы?\nhttps://itproger.com/tasks/3-logicheskie-zadachi-dlya-nastoyashtego-programmista", "Мотоциклы -\nУ вас есть 50 мотоциклов с полным баком, которого хватает на 100 км езды.\nВопрос: используя все мотоциклы, какое максимальное расстояние вы сможете проехать? Все мотоциклы в начале пути находятся условно в одной точке.\nhttps://chesscomp.ru/golovolomki/zadacha-pro-50-mototsiklov-prostoe-reshenie-naydet-ne-kazhdyy", "Комнаты -\nЕсть 2 комнаты. Первая комната закрыта дверью, в ней низкие потолки и висят 3 лампы накаливания. Во второй комнате есть 3 выключателя, подсоединённых к каждой из ламп. Можно как угодно переключать выключатели, но перейти из второй комнаты в первую можно лишь один раз.\nВопрос: как узнать, за какую лампу отвечает каждый из выключателей?\nhttps://dzen.ru/a/Yn7BklAD1i-WQ-3f"]
rainbow_list = ["Чашки -\nПредставьте ряд из шести чашек на столе. Три первые из них ничем не наполнены, а три следующие – с водой. Как добиться чередования пустых чашек и чашек с водой? Касаться разрешается только одной чашки. При этом толкать чашку чашкой запрещается. \nЧто вы предпримите? Ответ по ссылке\nhttps://dzen.ru/a/ZTa5O-xw-1ZbUK2w", "Теннис -\nВ санатории на лужайке двое мужчин играют в настольный теннис. Один ударяет ракеткой так сильно, что теннисный шарик улетает далеко и попадает в трубу из стали. Труба зарыта в землю вертикально на три метра. Шарик лежит на дне трубы, то есть на расстоянии трёх метров от плоскости земли. У игроков нет другого шарика.\nКак спортсменам достать игральный шар без извлечения трёхметровой трубы из-под земли? Ответ по ссылке\nhttps://shkolenet.ru/QA/8998990/", "Мост -\nЧерез пролив идет десятикилометровый мост. Максимальная нагрузка для него – 25 тонн. С начала этого моста стартовал грузовик, масса которого – ровно 25 тонн. Автомобиль продолжает движение к противоположному краю. Баланс моста пока не нарушен. Неожиданно, когда грузовик достиг середины пути, на него сел воробей со своим весом. \nПриведёт ли вес птицы к нарушению балансировки и разрушению моста?", "Блэндер -\nВас уменьшили и бросили в блендер, который включится через 30 секунд. Что вы будете делать?\nhttps://dzen.ru/a/XjrwC8D3hU_lwCb3", "Тонель -\nПри строительстве тоннеля метро под вокзалом «Виктория» в Лондоне возникла серьезная проблема: в тоннель стала просачиваться вода. Как удалось устранить эту проблему и продолжить работы?", "Ботинки -\nПроизводитель обуви принял стратегическое решение: все правые ботинки производить в одном городе, а все левые — в другом. Зачем это было нужно?", "Продажи -\nКомпания по производству средств для ухода за волосами нанимает маркетолога, чтобы увеличить продажи. Он добавляет всего одну фразу на этикетку —продажи растут в 2 раза. Что это была за фраза?\nhttps://dzen.ru/a/ZJvSAnwYaHOETlOd", "Лифт -\nЖители дома жаловались, что лифт слишком медленно поднимается и спускается. Замена лифта стоила бы очень дорого, поэтому хитрый управдом придумал, как сэкономить и при этом все жители были довольны. Что он сделал?", "Случается ли? -\nWhat occurs twice in a week once in a year but never in a day? Что случается дважды в неделю один раз в год, но никогда днем? (важно смотреть именно в английское предложение, перевод только для понимания смысла) Ответ по ссылке (14 задача).\nhttps://almanax.co.uk/tpost/k2apauy161-20-zadachek-dlya-razvitiya-kreativnogo-i", "Свеча и коробки -\nУ вас свеча, коробка спичек и коробка кнопок. Как наиболее рационально прикрепить свечу к деревянной двери так, чтобы обеспечить с ее помощью максимальное освещение?\nhttps://dzen.ru/a/X-Mkxd0lSmuGqFV4"]



# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Задачка на логику🧠")
    btn2 = types.KeyboardButton("Задачка на воображение🌈")
    
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Приветствую тебя землянин, {0.first_name}! выбери для начала задачу😉 ВАЖНО:не на все задачи есть ответы)".format(message.from_user), reply_markup=markup)
    bot.send_photo(message.chat.id, 'https://s00.yaplakal.com/pics/pics_original/0/4/3/12908340.jpg', None, 'Text')


# обработчик всех остальных сообщений    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Задачка на логику🧠"):
     bot.send_message(message.chat.id,"Вот что выдал мой гениальный разум:\n\n{0}".format(random.choice(brain_list)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("Да, спасибо, пойду думать!👍")
     btn2 = types.KeyboardButton("Давай другую🧐")
     btn3 = types.KeyboardButton("Лучше на воображение🌈")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Ну что, сможешь ее осилисть?", reply_markup=markup)
     bot.send_video(message.chat.id, 'https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2dzNnFpZ3k1Y3YxZG92OXB6MTc2ajNlM2dybnVxb2F1NWZrdWVkZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MdGUUTVHk7s1BA5Pyk/giphy.gif', None, 'Text')

    elif(message.text == "Давай другую🧐"):
      bot.send_message(message.chat.id,"Вот что выдал мой гениальный разум:\n\n{0}".format(random.choice(brain_list)))
      bot.send_message(message.chat.id,text="А эта?🙄")
      bot.send_video(message.chat.id, 'https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExeHYxemNhNjYyenlqMThldm1zZXl3M3IxaGtoZ296b3djb3BrcjNrMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/i79na9XMwDues/200w.gif', None, 'Text')



    elif(message.text == "Лучше на воображение🌈"):
      bot.send_message(message.chat.id,"Вот что выдал мой гениальный разум:\n\n{0}".format(random.choice(rainbow_list)))
      bot.send_message(message.chat.id,text="Ну как?🙄")
      bot.send_video(message.chat.id, 'https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMHVlczB4NGV0MjU0bTdvc29iMjl6am11eHVwOG96eDB6MHF6bWhobCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/13Syr1nwDffUcw/giphy.gif', None, 'Text')


    elif(message.text == "Задачка на воображение🌈"):
     bot.send_message(message.chat.id,"Вот что выдал мой гениальный разум:\n\n{0}".format(random.choice(rainbow_list)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("Да, спасибо, пойду думать!👍")
     btn2 = types.KeyboardButton("Давай другую🌈")
     btn3 = types.KeyboardButton("Лучше на логику🧠")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Ну что, сможешь ее осилисть?", reply_markup=markup)
     bot.send_video(message.chat.id, 'https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2dzNnFpZ3k1Y3YxZG92OXB6MTc2ajNlM2dybnVxb2F1NWZrdWVkZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MdGUUTVHk7s1BA5Pyk/giphy.gif', None, 'Text')


    elif message.text == "Давай другую🌈":
      bot.send_message(message.chat.id,"Вот что выдал мой гениальный разум:\n\n{0}".format(random.choice(rainbow_list)))
      bot.send_message(message.chat.id,text="А эта?🙄")
      bot.send_video(message.chat.id, 'https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExeHYxemNhNjYyenlqMThldm1zZXl3M3IxaGtoZ296b3djb3BrcjNrMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/i79na9XMwDues/200w.gif', None, 'Text')


    elif(message.text == "Лучше на логику🧠"):
      bot.send_message(message.chat.id,"Вот что выдал мой гениальный разум:\n\n{0}".format(random.choice(brain_list)))
      bot.send_message(message.chat.id,text="Ну как?🙄")
      bot.send_video(message.chat.id, 'https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMHVlczB4NGV0MjU0bTdvc29iMjl6am11eHVwOG96eDB6MHF6bWhobCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/13Syr1nwDffUcw/giphy.gif', None, 'Text')

  
    
    elif(message.text == "Да, спасибо, пойду думать!👍"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("/start")
        markup.add(btn1)
        bot.send_message(message.chat.id,text="Возвращайся если что, Шелдон поможет", reply_markup=markup)
        bot.send_video(message.chat.id, 'https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3B4bXRzdmNxOTZrY2V1N2Q2dDA3aGx1bjdyNDluanAzMnA4ZjgwcyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/f79OYWh5uwIfK/giphy.gif', None, 'Text')
    
    
    else:
        bot.send_message(message.chat.id, text="Эта теория непонятна мне😟")
        bot.send_video(message.chat.id, 'https://gifdb.com/images/high/throw-in-the-towel-sheldon-cooper-gives-up-0tb4r9qwfdisch3i.gif', None, 'Text')



# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()

