import telebot


TOKEN = "6408076334:AAEuhXXupGsbop4F8Lprndqn22uswjJFWGE"
bot = telebot.TeleBot(TOKEN)
STATE = {}

massage1 = "/start - <b>Запуск бота</b> \n/quest - Начать квест\n/help - <b>Список команд</b>\n/mem - <b>Показ мема</b> \n/id - <b>Показывет ваш id</b>"
massage2 = "Привет, сейча мы с тобой начнем квест, если ты испугался, то все равно продолжай проходить, квест очень простой и вообще не страшный)"
massage3 = "В этой комнате тоже довольно пуставато, она тоже заполнена разным строительным мусором. По середине комнаты стоит очень странная кровать, которая одновременнна служит для того, чтобы там можно было спать, или хранить вещи, така как эта кровать была ещё и тумбочкой. Но вроде кроме этого здесь больше ничего нет, даже тумбочка-кровать путса."
massage4 = "Это комната, на удивление, была просто пуста, но опять же заполнена мусором. Единственное что странно, так это окно которое ведет в стену другого дома, можно сказать что оно было просто перекрыто. В этой комнате тоже ничего не оказалось полезного "
massage5 = "Кроме огромного количества мусора, здесь ничего нет("
massage6 = "К сожалению, твоя идея была дурацкая. Он тебе моментально сожрал. Советую в следующий раз выбрать что-то нормальное"


qustions = {
    1: {
        "question": "Ты просыпаешься в странном помещении, которое напоминает тебе каморку строителя. У тебя очень сильно болит голова, осмотревшись вокруг, ты видишь на полу разбросанные кучки строительного мусора, на стене перед тобой весит большая белая доска, на которой что-то не понятное написано, слева от доски ты видишь старый деревянный шкаф, который полностью забит старыми и пыльными книгами. Сбоку от тебя стоит вроде путсая, разбитая в хлам тумбочка. Сзади тебя есть дверь, но судя по замку , которые весит на двери, тебе нужно найти ключ или инструмент для взлома этого замка. Чтобы посмотреть с самого начала? ",
        "answers": {
            1: "Маленький столик, который стоит перед тобой",
            2: "Осмотреть доску на которой что-то написанно",
            3: "Попробовать осмотерть мусор на полу",
            4: "Посмотреть тумбочку"
        },
        "photo": "каморка.jpg"
    },
    2:  {
        "question": "Когда ты присмотрелся к доске, то увидел там написанный текст: “ Проверь книгу где кот сжег примус”",
        "answers": {
            2: "Интересно, значит надо пойти к шкафу и просмотреть книги от туда"
        },
        "photo": "доска.png"
    },
    3:  {
        "question": "Было видно, что книги в шкафу были очень старые, на них были стерты даже названия, но к счастью видно названий несколько книг:\n \n1) Таня Гро..р(видимо несколько букв  стрелось) \n2) Эркюль Пуаро( видимо какой-то старый детектив)  \n3) Кто знает физику. Сказания о инженерах( по моему тут врядли будет кот) \n4)Мастер и Маргарита( В книге с таким названием, кот не может сжечь примус(наверное))",
        "answers": {
            3: "Таня Гро..р",
            4: "Эркюль Пуаро",
            1: "Кто знает физику. Сказания о инженерах",
            2: "Мастер и Маргарита"
        },
        "photo": "шкаф.png"
    },
    4:  {
        "question": "Удивительно, но ты прав, в этой книге были вырезаны страницы и там был спрятан ключ",
        "answers": {
            2: "Если есть ключ, то можно и убиратся от сюда и бежать быстрее к двери",
        },
        "photo": "дверь.png"
    },
    5:  {
        "question": "Отперев дверь, ты попадаешь в довольно большую комнату. В конце её можно увидеть лифт, который явно не запущен, также есть несколько проходов в другие комнаты. В комнате с лифтом довольно слабое освещение, тут опять же разбросан мусор. Надо пойти и поискать какую-нибудь вещь, которая сможет запустить лифт.",
        "answers": {
            2: "Комната 1",
            10: "Комната 2",
            11: "Комната 3",
            12: "Поискать что-то в этой комнате"
        },
        "photo": "лифт.jpg"
    },
    6:  {
        "question": "Ты зашел в эту комнату, которая как и все остальные, была завалена хламом, но ты  увидел странный деревянный закрытый шкаф в комнате. Похоже это единственное место, где можно найти что-нибудь дельное.",
        "answers": {
            2: "Открыть шкаф",
        },
        "photo": "шкаф.jpg"
    },
    7:  {
        "question": "Открыв шкаф, ты видишь что в нем куча не нужного барахла, но спустя время покопавшись в нем, ты заметил , что на одной из полок видны какие-то провода. Ты спихнул весь мусор, который лежал на полке и увидел: у шкафа не было задней стенки, вместо неё можно было увидеть электрический  щиток, который, к сожалению, был отключен. Теперь понятно почему не работает лифт, так как не было электричество. Но есть одна загвоздка, тебе надо правильно соединить и подкрутить провода, так как он был отключен из-за того, что слетели провода.",
        "answers": {
            3: "🟩🟦Соединить зеленый и синий",
            4: "🟦🟥Соеденить синий и красный",
            2: "🟥🟩Соединить красный и зеленый",
        },
        "photo": "открытый шкаф.jpg"
    },
    8:  {
        "question": "Ты слышишь, что электричество пошло по проводам, так как начал шуметь лифт. Ты быстрее бежишь к лифту, но замечаешь что-то не понятное. Это существо смотрит на тебя маниакальным взглядом с огромной улыбкой. Существо выглядит стремно, большое похожее на человека, но длиннее, также оно черного цвета. Ты чувствуешь беспокойство и понимаешь, что тебе лучше всего немедленно спрятаться. ",
        "answers": {
            4: "Убежать в пустую комнату и закопатся в мусор",
            3: "Попробовать притворится мертвым(я лучше бы не советовал)",
            2: "Быстрее забежать в комнату с непонятной тумбочкой-кроватью и спрятатся под неё",
            1: "Попытатся спрятатся за шкаф"
        },
        "photo": "Страшная Уга Буга.jpg"
    },
    9:  {
        "question": "УРА! Оно ушло, ты вылез и со скоростью пули побежал к лифту, теперь точно можно от сюда смыться ",
        "answers": {
            2: "Вызвать лифт",
        },
        "photo": "лифт.jpg"
    },
    10:  {
        "question": "При выходе из лифта, ты видишь перед собой большую строительную площадку. На ней находится 2 блочных домика для строителей, пару мусорок, трактор и всё тот же строительный мусор.  По небо ты определили, что уже давно ночь и пора быстрее валить от сюда. Та залез в трактор и понял, что без ключей его не завести, но есть проблема – ключ лежал сломанный под рулем. Тут ты понимаешь, что можно попробовать завести трактор как в фильмах. Для этого тебе понадобится скрепление для проводов и плоскогубцы. Тогда придется сначала идти в ближайший дом.",
        "answers": {
            2: "Пойти в первый строительный домик",
        },
        "photo": "Строительная площадка.jpg"
    },
    11:  {
        "question": "Когда ты вошел в домик строителя, то сразу испугался, но быстро успокоился, так как сбоку стола стоял манекен, который сначала напоминал что-то не понятное. Это был обычный строительный домик, там был строительный стол, доска для чертежей, пару полочек с хламом, ящик с инструментами и раскиданные по полу сумки.",
        "answers": {
            1: "Осмотреть все полки",
            4: "Открыть и посмотреть лежащие сумки на полу",
            3: "Осмотреть рабочий стол",
            2: "Попробовать посмотреть в ящике с инструментами"
        },
        "photo": "домик1.jpg"
    },
    12:  {
        "question": "Бинго! Конечно инструмент будет лежать в ящике с инструментами. Теперь пора идти в другой домик",
        "answers": {
            2: "Идти во второй домик",
        },
        "photo": "Строительная площадка.jpg"
    },
    13:  {
        "question": "Второй домик был намного хуже, сразу было видно, что тут давно не убирались. В нем находилось полно хлама, почти сломанный столик для работ, деревянный шкаф и что-то, похожие на вешалку, висело на стене",
        "answers": {
            4: "Осмотреть шкаф",
            2: "Посмотерть, что там висит на вешалке",
            3: "Посмотреть стол",
            1: "Попробовать порытся в мусоре"
        },
        "photo": "домик2.jpg"
    },
    14:  {
        "question": "Очень странно, но прикольно, что провода в итоге висели на вешалке. Когда ты уже имеешь все нужные инструменты ты побежал запускать трактор. Но как только ты вышел из домик, ты опять увидел это существо. Нету времени думать и надо опять прятаться и желательно побыстрее, так как мы пока не знаем, что она может с нами сделать",
        "answers": {
            2: "Ты видишь рядом с собой мусорку полную хлама, и прыгаешьв ней",
            2: "Спрятатся в кустах",
            3: "Попробовать притворится мертвым(я лучше бы не советовал)",
            1: "Попробовать спрятатся в дальней мусорке"
        },
        "photo": "Огромная уга буга2.jpg"
    },
    15:  {
        "question": "Спустя несколько часов ты перестал слышать страшные звуки, которое издает это существо. Ты быстро вылез из мусорки и побежал трактор.  Трактор долго не запускался и ты совсем отчаялся, но в последний раз когда ты решил соединить провода и подать ток…… Всё сработало! Ты уселся поудобнее в сидень, развернул трактор и поехал со всей скорости в сторону ворот, которые закрывали тебе путь",
        "answers": {
            2: "Улипётываем быстрее!!!!",
        },
        "photo": 0
    },
    16:  {
        "question": " ",
        "photo": 0
    },

}
