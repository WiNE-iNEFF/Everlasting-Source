init:

    image bg cum_room_day = "Azure_summer/bg/cum_room_day.jpg"
    
    image bg ext_music_club_verandah_day = "Azure_summer/bg/ext_music_club_verandah_day.jpg"
    
    image bg lake = "Azure_summer/bg/lake.jpg"
    
    image bg road_out_camp = "Azure_summer/bg/road_out_camp.jpg"
    
    image bg road_out_camp_day = "Azure_summer/bg/road_out_camp_day.jpg"
    
    image bg inside_music_club_sunset = "Azure_summer/bg/inside_music_club_sunset.jpg"
    
    image bg ext_mimusicclub_night = "Azure_summer/bg/ext_mimusicclub_night.jpg"
    
    image bg houses_night = "Azure_summer/bg/houses_night.jpg"
    
    image bg cum_hata_night = "Azure_summer/bg/cum_hata_night.jpg"
    
    image bg ext_house_of_mi_night = "Azure_summer/bg/ext_house_of_mi_night.jpg"
    
    image bg cum_room_light_night = "Azure_summer/bg/cum_room_light_night.jpg"
    
    image bg cum_room_night = "Azure_summer/bg/cum_room_night.jpg"
    
label EvSuDAY_1: 
    $ backdrop = "days"
    $ new_chapter(1, u"День первый.")
    
    $ day_time()
    $ persistent.sprite_time = 'day'
    play ambience ambience_ext_road_day fadein 2
    scene bg int_bus with dissolve 
    
    show unblink
    
    "Я открыл глаза"
    
    show blinking
    
    th "Что...?" 
    th "Я проспал до конечной?"
    th "А почему автобус другой?"
    th "Меня что усыпили газом и привезли в какую-то игру на выживание?"
    
    "В салоне никого не было. Я выглянул в окно и вопросов у меня в несколько раз, прибавилось."
    "Я осмотрел салон.{w} С виду данное транспортное средство явно было построено в конце, или даже середине прошлого века."
    "Я положил руку на спинку сидения спереди дабы подняться, но ноги не слушались."
    "Чья это рука?{w} Нет, она определенно моя, но что-то со ней явно не так."
    "Я сразу потянулся в карман за телефоном.{w} Странно что его не вытащили пока меня перетаскивали в другой автобус, а впрочем, может и нет." 
    
    play sound sfx_cellular_phone_error
    
    "Связи на двух симках нет." 
    "Я открыл фронталку и на пару минут меня заклинило.{w} Сейчас мне не 23 года, а где-то 16-17."
    "Может я умер?{w} Мне известна весьма правдоподобная теория, что когда мозг умирает, из-за инстинкта самосохранения он может воспроизводить то, во что верил человек при жизни." 
    "Рай, ад, коммунизм, и т.д.{w} Всё лишь бы жить.{w} Этим и объясняются рассказы тех, кому врачи заново запускали сердце.{w} Якобы я стоял перед страшным судом, но вдруг проснулся в палате. Такие сны длятся до минуты, пока все клетки мозга не отомрут."
    "Вот только сижу я в этом бусе явно дольше и чувствую себя вполне реально.{w} И либо здесь время идёт медленней, либо остаётся последний вариант: меня и вправду перебросило в другой мир." 
    "После всех просмотренных фильмов, сериалов и аниме - мне это кажется возможным."
    
    $ day_time()
    $ persistent.sprite_time = 'day'
    scene bg ext_road_day with dissolve 
    
    "Всё-таки выбравшись с автобуса я осмотрелся по сторонам."
    "Я бегал взглядом по бескрайнему полю и пытался за что-то ухватиться,{w} но ловил лишь одинокие деревья, что росли вдоль дороги, плывущей за горизонт."
    
    $ day_time()
    $ persistent.sprite_time = 'day'
    scene bg ext_camp_entrance_day with dissolve 
    
    "Как только я обошел автобус, меня встретили два мраморных пионера стоявшие у громоздких ворот."
    "Ну, думаю идти вдоль дороги или через поле, которым конца края не видно, - идея так себя." 
    "Нужно глянуть что за воротами.{w} Бояться мне уже нечего, хотя, может быть, стоит, ведь я убедился, что ещё жив.{w} Ладно, надеюсь там не живет какая-нибудь группа бомжей или сатанистов.{w} За воротами послышались шаги." 
    "Значит живут." 
    "Я сразу увидел женскую фигуру через прорезь в воротах и успокоился." 
    
    play sound sfx_carousel_squeak
    
    "Скрип петель."
    
    $ day_time()
    $ persistent.sprite_time = 'day'
    
    show mt smile pioneer far with dissolve
    hide mt smile pioneer far with dissolve
    
    show mt smile pioneer with dissolve
    hide mt smile pioneer with dissolve
    
    show mt smile pioneer close with dissolve
    
    "Предо мной стояла приятная на вид зеленоглазая девушка в пионерской форме."
    
    mtp "А вот и последний пионер явился! Чего стоим? Проходи не стесняйся, сейчас устроим тебя."
    
    me "Девушка, вы вообще кто?"
    
    hide mt smile pioneer close with dissolve
    
    show mt rage pioneer close with dissolve
    
    mtp "ЧТО!? Это что за хамство? Ты как со своей вожатой разговариваешь?"
    
    me "Простите, кем?"
    
    hide mt rage pioneer close with dissolve
    
    show mt angry pioneer close with dissolve
    
    mtp "Тебе голову напекло? Куда ты, по-твоему, приехал?" 
    
    me "Не знаю. Куда?" 
    
    mtp "Хватит отвечать вопросами на вопросы.{w} Ты, видимо, крепко задремал пока сюда ехал и ещё не проснулся."
    mtp "Семён Персунов, вы прибыли в лагерь “Совёнок”,{w} что расположен в Туапсинском районе Краснодарского края.{w} Пришёл в себя?{w} Ещё вопросы будут?"
    
    th "Вопросов ещё масса, но не похоже, что она сейчас на всё ответит."
    th "Буду подыгрывать этому цирку, может по ходу дела что-нибудь узнаю."
    
    me "Пока вроде нет…"
    
    hide mt angry pioneer close with dissolve
    
    show mt grin pioneer close with dissolve
    
    mtp "Отлично. Идём заселятся. За мной!"
    
    hide mt grin pioneer close with dissolve
    
    $ day_time()
    $ persistent.sprite_time = 'day'
    scene bg ext_houses_day with dissolve
    
    "За воротами действительно был лагерь в советском стиле." 
    "Мы прошли по широкой дороге, вымощенной бетонными плитами.{w} Затем, миновав несколько маленьких деревянных домиков и два здания покрупнее, вышли на площадь."
    
    $ day_time()
    $ persistent.sprite_time = 'day'
    scene bg ext_square_day with dissolve
    
    show mt smile pioneer with dissolve
    
    mt "Ой, совсем забыла представиться.{w} Я Ольга Дмитриевна, вожатая твоего отряда." 
    mt "У нас пионеры живут по двое, но с тобой получается нечётное количество людей,{w} так что жить ты будешь один." 
    
    hide mt smile pioneer with dissolve

    show mt grin pioneer with dissolve  
   
    mt "Зато по соседству со мной!" 
    
    hide mt grin pioneer with dissolve 
    
    show mt smile pioneer with dissolve 
    
    mt "По поводу вещей не волнуйся, меня предупредили что ты приедешь без них.{w} Одежду найдешь в шкафу своего домика, он у тебя номер 16.{w} Мой 17-й.{w} Ну, идём, проведу тебя." 
    
    me "Подождите, а кто вас предупредил что я приеду?"
    
    hide mt grin pioneer with dissolve 
    
    show mt surprise pioneer with dissolve
    
    mt "Твои родители. Кто ж ещё-то?"
    
    th "Вот как, у меня здесь есть родители. Уверен абсолютно мне незнакомые люди."
    
    me "Точно."
    "Подыграл я её ответу."
    
    hide mt surprise pioneer with dissolve
    
    stop ambience
    
    $ day_time()
    $ persistent.sprite_time = 'day'
    play ambience ambience_int_cabin_day fadein 1
    play sound sfx_open_door_2
    scene bg cum_room_day with dissolve 

    "Мы прошли площадь, она завела меня в мою “виллу”.{w} По размерам она была раза в полтора больше моей комнаты."
    
    show mt smile pioneer with dissolve2
    
    mt "Ну, располагайся!{w} Снимай уже своё пальто, а то стоит на тебя посмотреть, аж в пот бросает."
    
    "Стоило ей напомнить о моей одежде, как мне тут же стало жарко.{w} До этого впечатления от увиденного ранее отодвигали жару на второй план." 
    
    
    
    "Я сбросил пальто, кофту, остался в футболке и джинсах."
    
    me "Всё. Что дальше?" 
    
    hide mt smile pioneer with dissolve
    show mt grin pioneer with dissolve
    
    mt "Какое же всё?"
    
    hide mt grin pioneer with dissolve
    show mt smile pioneer with dissolve
    
    mt "Ты чем меня слушаешь?{w} Повторяю ещё раз, форма в шкафу."
    mt "Как закончишь - подходи к моему домику."
    
    hide mt smile pioneer with dissolve
    
    play sound sfx_close_door_1
    
    "Cказала вожатая, закрывая за собой дверь."
    
    "Я окинул взглядом комнату."
    
    th "Дааа. И куда я попал?{w} Связи по-прежнему нет. Выключу пока телефон, буду экономить батарею." 
    th "Так что мне там надеть надо?"
    
    play sound sfx_open_cupboard
    
    "Открыв шкаф, я принялся изучать содержимое.{w} На плечиках висело две пионерские формы, один спортивный костюм.{w} Внизу стояли две пары белых кроссовок." 
    
    th "Думаю, под «переодеться» она не имела ввиду спортивный костюм."
    
    "Надев рубашку из очень приятной на ощупь ткани, придурошные шорты и длинные носки, завязав красный галстук, я посмотрел на себя в зеркало."
    
    th "Выгляжу хуже, чем клоун. Надеюсь, что тут все в таком ходят."
    
    play sound sfx_close_door_1
    
    stop ambience
    
    $ day_time()
    $ persistent.sprite_time = 'day'
    play ambience ambience_camp_center_day fadein 1
    scene bg ext_house_of_mt_day with dissolve
    
    show mt smile pioneer far at cleft with dissolve
    
    show sl smile pioneer far at cright with dissolve
    
    "Выйдя из домика, я направился к соседнему, у которого стояли и беседовали Ольга Дмитриевна и какая-то блондинка, одетая в тоже, что и вожатая."
    
    mt "Ну вот, сразу на человека стал похож."
    
    "Одобрительно кивнула Ольга Дмитриевна."
    
    mt "Это - Славяна, - указала она взглядом на свою собеседницу. – А это Семён, - переводя взгляд на меня, продолжила вожатая."
    
    sl "Привет! Приятно познакомиться. Можно просто Славя."
    
    me "Здравствуйте, мне тоже приятно познакомится." 
    "Протараторил я."
    
    hide sl smile pioneer far at cright with dissolve
    
    show sl laugh pioneer far at cright with dissolve
    
    sl "Ха-ха-ха! Зачем так официально, мы же одного возраста."
    
    hide sl laugh pioneer far at cright with dissolve
    
    show sl smile pioneer far at cright with dissolve
    
    me "А… да, точно…"

    mt "Семён, хватит мямлить. Бери обходной лист."
    "Она протянула мне бумажку. "
    
    play sound sfx_paper_bag
    
    mt "Тебе нужно обойти все места, указанные в нём, собрать подписи и записаться в один из кружков.{w} Славя покажет ко всему дорогу."
    
    "Я взглянул на листик."
    th "Кружки, столовая, медпункт, библиотека."
    me "Понятно."
    
    mt "Раз понятно, то не смею задерживать."
    
    hide mt smile pioneer far at cleft with dissolve
    
    "Сказала она и ушла в неизвестном мне направлении."
    
    hide sl smile pioneer far at cright with dissolve
    
    show sl smile pioneer far at center with dissolve
    
    sl "Иди за мной."
    
    hide sl smile pioneer far at center with dissolve
    
    $ day_time()
    $ persistent.sprite_time = 'day'
    scene bg ext_houses_day with dissolve
    
    "Мы пошли в сторону площади, туда откуда Ольга привела меня."
    
    me "Слушай, а можешь ответить на один вопрос?{w} Только в ответ ничего не спрашивай и не смейся, пожалуйста."
    
    show sl smile pioneer close with dissolve
    
    sl "Постараюсь ответить. Но насчёт остального не уверена." 
    
    me "Ладно. Какой сейчас год?"
    
    sl "1979й"
    
    
    "Ответила она и тут же рассмеялась."
    
    hide sl smile pioneer close with dissolve
    
    show sl laugh pioneer close with dissolve
    hide sl laugh pioneer close with dissolve
    
    show sl smile pioneer close with dissolve

    sl "Ой прости, я правда не хотела."
    
    th "Теперь понятно, а то я думал это косплей-лагерь какой-то.{w} И почему связи нет - тоже стало ясно." 
    th "Неизвестно только как я сюда попал и почему помолодел.{w} Буду придерживаться плана: делать что скажут."
    
    me "Шутка. А ты откуда и как давно здесь, если не секрет?"
    
    "Нелепо сменил я тему."
    
    sl "Я из Мурманска. Приехала позавчера, как и большинство пионеров. Вчера ещё несколько человек прибыло. А сам ты откуда?"
    
    me "Из Харькова"
    "Назвал я своё место жительства."
    
    th "Со слов вожатой, у меня здесь есть семья.{w} Скорее всего вместе с ней мне и документы сгенерировало.{w} Не могли ж меня без них оформить.{w}Они мне еще пригодятся, если я в этом мире надолго или навсегда."
    
    hide sl smile pioneer close with dissolve
    
    "Тем временем, мы подошли к небольшому зданию неподалёку от входных ворот." 
    
    $ day_time()
    $ persistent.sprite_time = 'day'
    scene bg ext_clubs_day with dissolve
    
    show sl smile pioneer with dissolve
    
    sl "Сейчас зайдём к кибернетикам. Возьмёшь у них подпись, а если понравится их компания, то можешь сразу и…"
    
    hide sl smile pioneer with dissolve
    
    show us laugh2 sport at cleft with dissolve
    
    show sl smile pioneer at cright with dissolve
    
    play music music_list['i_want_to_play'] fadein 1  
    
    usp "Ого, Славя! Ты, я смотрю, времени зря не теряешь. Так держать!"
    
    hide sl smile pioneer at cright with dissolve
    
    show sl serious pioneer at cright with dissolve
    
    sl "Ульяна, прекращай!"
    "Нахмурилась Славя."
    
    hide sl serious pioneer at cright with dissolve
    
    show sl smile pioneer at cright with dissolve
    
    sl "Семён, это Ульяна, а также главный источник проблем в лагере. Она из нашего отряда."
    
    hide us laugh2 sport at cleft with dissolve
    
    show us dontlike sport at cleft with dissolve
    
    us "И ничего не главный!"
    
    hide us dontlike sport at cleft with dissolve
    
    show us grin sport at cleft with dissolve
    
    "Запротестовала она и протянула мне руку." 
    
    us "Рада знакомству!"
    
    hide us grin sport at cleft
    
    show us grin sport at cleft with flash
    hide us grin sport at cleft with dissolve
    
    "Стоило нашим ладоням на секунду соприкоснутся, как я тут же отдёрнул свою.{w} На землю упало какое-то насекомое, а Ульяна уже убегала, заливаясь смехом."
    
    stop music fadeout 1
    
    play ambience ambience_camp_center_day
    
    hide sl smile pioneer at cright with dissolve
    
    show sl smile pioneer with dissolve
    
    sl "Как-то так, с ней нужно всегда быть внимательным.{w} Давай уже зайдем."
    
    stop ambience
    
    hide sl smile pioneer with dissolve
    
    $ day_time()
    $ persistent.sprite_time = 'day'
    play ambience ambience_clubs_inside_day fadein 1
    play sound sfx_open_door_clubs
    scene bg int_clubs_male_day with dissolve
    
    "За дверью, стоял специфический запах канифоли.{w} Два пионера совершенно не обращали на нас внимания, увлеченно пытаясь что-то припаять."
    
    show sl smile pioneer with dissolve:
        xcenter 0.77 ycenter 0.50
    
    sl "Всем привет! Не отвлекаю?"
    
    show el smile pioneer with dissolve
    
    show sh normal pioneer with dissolve:
        xcenter 0.17 ycenter 0.50
    
    elp "О, привет.{w} Мы вас не заметили.{w} Это, я так понимаю, новоприбывший?{w} По какому поводу пожаловали?"
    
    "Не дожидаясь ответа, он протянул мне руку."
    
    el "Серёжа.{w} Все зовут меня Электроник, и ты можешь.{w} Почему так, оставлю твоему воображению."
    
    me "Семён. Просто Семён."
    
    sh "А я - Шурик."
    
    "Вмешался его товарищ и пожал мне руку."
    
    sh "По какому вопросу?"
    
    th "Жал им руки я с опаской. Мало ли сколько еще здесь таких шутников как Ульяна."
    
    me "Да вот, нужно чтобы вы подписали."
    
    play sound sfx_paper_bag
    
    "Показал я бегунок."
    
    el "Эт можно. Будет здорово, если ты к нам вступишь. У нас тут много чем интересным можно заняться."
    
    th "Не сомневаюсь."
    
    me "Вы первые, к кому мы зашли. Сначала все осмотрю, а там видно будет."
    
    sh "Ну так давай быстрее. Возвращайся и вступай, не пожалеешь."
    
    "Продолжил он агитировать."
    
    "Тем временем Электроник вернул мне листок с подписью."
    
    el "Держи и давай не задерживайся. Будем ждать."
    
    me "Да-да, ещё непременно свидимся."
    
    "Ответил я и заторопился к выходу."
    
    sl "Ну, бывайте. Мы пошли."
    
    hide sl smile pioneer with dissolve
    hide el smile pioneer with dissolve
    hide sh smile pioneer with dissolve
    
    stop ambience
    
    $ day_time()
    $ persistent.sprite_time = 'day'
    play ambience ambience_camp_center_day fadein 1
    play sound sfx_close_door_campus_1
    scene bg ext_clubs_day with dissolve
    
    sh "До встречи. Надолго не прощаемся, Семён!"
    
    "Прокричал он в закрывающуюся дверь."
    
    th "Вот неугомонные. Им бы в секте работать."
    
    show sl smile pioneer with dissolve
    
    sl "Надеюсь парни не сильно тебя отпугнули, так-то они хорошие ребята.{w} Я бы тебе рекомендовала выбирать между ними и музкружком, туда мы сейчас и направляемся.{w} В остальных - дети с младших отрядов, но при желании можно и к ним вступить."
    
    scene bg ext_houses_day with dissolve
    show sl smile pioneer with dissolve
    
    me "Сколько всего людей в нашем отряде?"
    
    sl "С тобой девять.{w} Двоих ты только что видел, а ещё трое, включая Ульяну, состоят в музкружке.{w} Также есть библиотекарша, но у неё уже есть помощница.{w} Я нигде не состою, так как помогаю вожатой во всём понемногу."
    
    me "Ты что-то вроде её правой руки?"
    
    scene bg ext_musclub_day with dissolve
    show sl smile pioneer with dissolve
    
    sl "Что-то вроде.{w} Если будут вопросы или проблемы, то можешь и ко мне обращаться.{w} Вот, пришли. Это музыкальный кружок."
    
    me "Слушай, я дальше сам справлюсь, не нужно везде со мной ходить.{w} Не маленький уже всё-таки."
    
    th "Уж постарше всех своих коллег, а может и Ольги Дмитриевны.{w} Хоть она и выглядит максимум на 20 с небольшим, но кто её знает…"
    
    hide sl smile pioneer with dissolve
    
    show sl happy pioneer with dissolve
    
    sl "Раз я так тебя смущаю…"
    
    "Она улыбнулась белоснежной улыбкой, от которой я теперь точно засмущался."
    
    sl "…то так и быть, давай дальше сам."
    
    me "Просто ты меня как мама везде за руку водишь."
    
    hide sl happy pioneer with dissolve
    
    show sl tender pioneer with dissolve
    
    "Сейчас уже она смутилась."
    
    sl "Тебе правда так кажется?"
    
    me "Нет. Я в общем как-бы, это не то…"

    sl "Ничего, все нормально. Я действительно из всего отряда только тебя так вожу по лагерю… Давай дальше сам. Удачи!"
    
    hide sl tender pioneer with dissolve
    
    "После этих слов она удалилась."
    
    scene bg ext_music_club_verandah_day with dissolve
    
    th "Мои навыки общения, особенно с девушками, не соответствуют не то, что старому, а и новому возрасту.{w} Нужно с этим что-то делать."
    
    play sound sfx_knock_door2
    
    "С этими мыслями я поднялся на веранду и постучал в дверь."
    
    mip "Открыто!"
    
    stop ambience
    
    play sound sfx_open_door_1

    scene bg int_musclub_day with dissolve
    
    play ambience ambience_music_club_day fadein 1
    
    "Войдя внутрь здания, я сразу заприметил чей-то силуэт под роялем и подошёл ближе."
    
    stop ambience
    
    play music music_list['gentle_predator'] fadein 1
    
    scene cg d2_miku_piano2 with dissolve
    
    me "Ой прости, я сразу не увидел, что ты в общем это, тут вот так…"
    
    th "Я, конечно, решил внятней формулировать мысли, но не при таких же обстоятельствах."
    
    stop music
    
    scene cg d2_miku_piano with dissolve
    play sound sfx_piano_head_bump
    
    "Девушка, выбралась из-под рояля, попутно ударившись об него затылком."
    
    play ambience ambience_music_club_day fadein 1
    scene bg int_musclub_day with dissolve

    show mi normal pioneer far with dissolve 
    
    hide mi normal pioneer far with dissolve2
    
    show mi shocked pioneer with dissolve

    mip "Ты о чём? Я же сказала открыто."
    
    "Не понимающе посмотрела на меня девушка."
    
    th "Она правда не поняла, что демонстрировала мне?"
    
    me "А… Неважно.{w} Не отвлекаю?{w} Я Семён, сегодня приехал только."
    
    hide mi shocked pioneer with dissolve
    
    show mi normal pioneer with dissolve
    
    th "Стоп.{w} Почему у неё крашеные волосы?{w} Я ж вроде в Советском Союзе.{w} Ну, не буду сразу в лоб спрашивать."
    
    mi "Меня зовут Мику.{w} Просто я на половину японка, поэтому имя такое странное."
    
    me "Да нет, не странное.{w} Я пришёл за подписью.{w} Вожатая сказала осмотреть лагерь."
    
    mi "А зачем подпись?{w} Ольга Дмитриевна никого до тебя не присылала с подобным..."
    
    th "Вот оно как.{w} А Славя и братья кибернетики об этом даже не заикнулись."
    
    me "И тем не менее…"
    
    mi "Ну раз надо, так надо.{w} Сейчас за ручкой схожу."
    
    hide mi normal pioneer with dissolve
    
    "Тем временем я рассматривал клубную комнату."
    
    th "Да тут определённо уютней чем в том цеху.{w} И Мику привлекательнее юных инженеров.{w} Если выбирать из двух вариантов, я остановлюсь на этом."
    
    show mi smile pioneer with dissolve
    
    mi "Вот, держи.{w} Подписала.{w} Извини что сразу навязываюсь…"
    
    "Она, слегка улыбаясь, подняла на меня взгляд."

    th "У неё слишком красивые глаза лазурного оттенка.{w} От этого взгляда меня, кажись, бросило в жар.{w} Да и в целом у неё очень приятная внешность." 
    th "К тому же короткая юбка и чулки отлично подчеркивают стройные ножки.{w} Интересно, а лифчик у неё тоже в полосочку?{w} Или может она его не носит…"
    
    mi "Что скажешь?"
    
    "Спросила она, не отводя взгляда."
    
    th "Похоже я на нее пялюсь.{w} Что-то увлекся."
    
    me "Прости, что ты спросила перед этим?"

    mi "Вступишь ко мне?{w} То есть, к нам.{w} Есть еще Алиса и Ульянка, но они ещё не пришли.{w} Они очень хорошие. Я вас познакомлю и вы точно подружитесь." 
    mi "А ты умеешь петь или на чём-то играть?{w} Если не умеешь - не страшно.{w} Ульянка не умела, но мы с Алисой её быстро научили.{w} Правда это было в прошлом году, может она уже разучилась.{w} Не знаю.{w} Ой я сразу столько всего наговорила, у меня так всегда."
    
    th "Выдала она и вправду многовато, но на голову это почему-то не давит."
    
    me "Нет, все нормально.{w} Тебя приятно слушать."
    
    "Неожиданно для самого себя, произнес я."
    
    hide mi smile pioneer with dissolve
    
    show mi surprise pioneer with dissolve
    
    mi "Что правда?{w} А мне все говорят, что я чересчур много болтаю."
    
    me "Правда. Теперь давай по порядку. Я вступлю к тебе… то есть к вам в клуб. В смысле в кружок."
    
    "Я снова начал запинаться и нервно смотреть по сторонам."
    
    hide mi surprise pioneer with dissolve
    
    show mi normal pioneer with dissolve
    
    mi "Клуб?{w} Я тоже часто так оговариваюсь.{w} Ты первый кто при мне кружок клубом назвал, а я тут не первую смену!{w} Может ты из другой страны?"
    
    me "Ну почти, я из Харькова,{w} но дело не в этом, просто читал и смотрел много зарубежного вот и нахватался слов."
    
    hide mi normal pioneer with dissolve
    
    show mi smile pioneer with dissolve
    
    mi "Ух ты!{w} Я тоже интересуюсь зарубежным творчеством…{w} Ой опять меня унесло.{w} Спасибо что вступил, я правда очень рада!{w} И девочки тоже обрадуются.{w} Так что, ты на чём-то играешь?"
    
    me "Нет, но я быстро учусь."
    
    th "А бросаю новые занятия еще быстрее."
    
    play sound sfx_open_door_1
    
    hide mi smile pioneer with dissolve
    
    show mi smile pioneer at cright with dissolve
    
    show dv normal pioneer2 at cleft with dissolve
    
    "Мику набрала воздуха, явно собираясь выпалить мотивирующую речь, но тут к нам зашла ещё одна рыжая пионерка." 
    "В отличие от Ульяны, эта была наверняка старше и с куда более выдающимися формами. Это особенно заметно при таком методе ношения рубашки."
    
    mi "О! А вот и Алиса!{w} Алиска, представляешь у нас новый участник!{w} Сегодня приехал и уже вступил к нам.{w} Правда здорово!?"
    
    dv "Я тоже рада тебя видеть Мику." 
    
    hide dv normal pioneer2 with dissolve
    
    show dv angry pioneer2 at cleft with dissolve
    
    dv "А тебя не очень.{w} Ты кто и что тут делаешь с Мику, а?"
    
    "Кинула она грозный взгляд в мою сторону."
    
    me "Да… Я это… Пришёл вступить в…"
    
    hide dv angry pioneer2 with dissolve

    show dv laugh pioneer2 at cleft with dissolve

    dv "Ха-ха-ха!{w} Да расслабься ты, шучу.{w} Я Алиса."
    
    "На её лице появилась улыбка."
    
    me "Семён.{w} Я сегодня приехал."

    hide dv laugh pioneer2 with dissolve
    
    show dv normal pioneer2 at cleft with dissolve
    
    play sound sfx_paper_bag
    
    "Алиса резво выхватила у меня из рук листик."
    
    me "Ольга Дмитриевна, дала этот идиотский лист для подписей.{w} И как оказалось, одному мне."
    
    dv "Интересно она придумала."
    
    "Алиса пробежалась глазами по списку."
    
    dv "Смотрю ты только в кружках побывал?"
    
    me "Да."
    
    mi "А хочешь, мы с Алисой тебе остальное покажем, чтоб ты сам не заблудился тут.{w} Я, когда впервые сюда приехала, поначалу терялась.{w} Алисочка, ты ведь не против прогуляться?"
    
    play sound sfx_dinner_horn_processed
    
    dv "Не против.{w} Начнём с прогулки в столовую.{w} Я как раз за тобой заходила, чтоб ты не заблудилась по пути."
 
    hide mi smile pioneer with dissolve
    
    show mi dontlike pioneer at cright with dissolve
    
    mi "Не смешно!"
    
    "Мику на мгновение сделала обиженный вид."
    
    hide mi dontlike with dissolve
    
    show mi normal pioneer at cright with dissolve
    
    mi "Ладно, идём Сень. Прости, можно тебя так называть?"
    
    me "На здоровье."
    
    dv "Подождите меня на улице, я быстро кое-что сделаю."
    
    hide dv normal pioneer2 with dissolve
    
    hide mi normal pioneer with dissolve

    stop ambience
    
    play ambience ambience_camp_center_day fadein 1
    scene bg ext_music_club_verandah_day with dissolve
    
    show mi normal pioneer with dissolve

    "Ничего не спрашивая мы вышли на веранду."
    
    me "Что она…"
    
    mi "Сейчас сам все увидишь."
    
    "Не дав мне закончить вопрос, перебила Мику."
    
    hide mi normal pioneer with dissolve
    
    show mi normal pioneer at cright with dissolve
    
    show dv normal pioneer at cleft with dissolve
    
    "Не прошло и минуты, как Алиса снова появилась.{w} Изменение трудно было не заметить." 
    "Теперь её рубашка была застегнута на пуговицы и заправлена в юбку."
    
    dv "Теперь можно идти, не боясь лекции о нравственности и морали от вожатой."
    
    hide mi normal pioneer with dissolve
    
    hide dv normal pioneer with dissolve
    
    scene bg ext_dining_hall_near_day with dissolve
        
    show dv normal pioneer at left with dissolve
    show mt smile pioneer with dissolve
    show mi normal pioneer with dissolve:
        xcenter 0.78 ycenter 0.50
    
    "В таком составе мы отправились на обед. Перед входом в столовую меня ожидала Ольга Дмитриевна."
    
    mt "Ну что, везде побывал?"
    
    me "Нет, только кружки успел обойти, вступил в музыкальный.{w} А почему, вы мне одному дали такое задание?"
    
    hide mt smile pioneer with dissolve
    
    show mt grin pioneer with dissolve

    mt "Чтоб быстрее наверстал упущенное за два дня.{w} И п-о-ч-е-м-у ж-е ты решил сразу в музыкальный вступить?"
    
    "Она посмотрела на девочек, которые всё это время стояли рядом."
    
    mt "Буду считать, что тебя очень тянет к искусству!"
    
    hide mt grin pioneer with dissolve
    
    show mt smile pioneer with dissolve
    
    mt "А теперь марш на обед. Вы ведь руки помыли?"
    
    dv "Само собой."
    
    hide dv normal pioneer with dissolve
    
    mt "Верю на слово."
    
    stop ambience
    
    $ day_time()
    $ persistent.sprite_time = 'day'
    play ambience ambience_dining_hall_full fadein 1
    scene bg int_dining_hall_people_day with dissolve
    
    "Войдя внутрь и взяв по подносу, мы сели за свободный столик."
    
    scene cg d1_food_normal with dissolve
    
    "Пюре, котлета, горошек и стакан компота с виду вопросов не вызывали." 
    
    th "Вряд ли меня сейчас будут травить."
    
    scene bg int_dining_hall_people_day with dissolve
    
    show mi normal pioneer at cright with dissolve
    
    show dv normal pioneer at cleft with dissolve
    
    mi "Всем приятного аппетита!"
    
    dv "Приятного."
    
    me "Приятного."
    
    "Не успел я попробовать содержимое тарелки, как к нам подсела Ульяна." 
    
    hide mi normal pioneer at cright with dissolve
    
    hide dv normal pioneer at cleft with dissolve
    
    show mi normal pioneer at right with dissolve
    
    show dv normal pioneer with dissolve
    
    show us dontlike sport at left with dissolve
    
    us "А почему меня никто не подождал?!"
    
    dv "Кто знает, где тебя носит и когда ты придёшь."
    
    us "Ладно этот."
    
    "Мотнула она головой в мою сторону."
    
    us "Но вы, как хорошие подруги, могли бы хоть немного подождать!"
    
    mi "Не обижайся, Ульянка.{w} К нам, между прочим, Семён в кружок вступил, представляешь?"
    
    hide us dontlike sport with dissolve
    
    show us surp1 sport at left with dissolve

    us "Серьёзно?"
    
    me "Серьёзней некуда. А жука мне в руку ты зачем всунула?"
    
    hide us surp1 sport with dissolve
    
    show us normal sport at left with dissolve
    
    hide dv normal pioneer with dissolve
    
    show dv smile pioneer with dissolve
    
    dv "Тебе повезло что в руку, могла и за шиворот."
    
    us "И правда…{w} Что-то я не подумала."
    
    me "Не нужно ей идеи подкидывать."
    
    dv "Ладно, приберегу их для себя.{w} Давайте поедим уже."

    hide us normal sport with dissolve
    
    show us laugh2 sport at left with dissolve
    
    us "А тебе лишь бы жрать."
    
    hide dv smile pioneer with dissolve
    
    show dv angry pioneer with dissolve
    
    dv "Ах ты мелкая…"
    
    hide mi normal pioneer with dissolve
    
    show mi smile pioneer at right with dissolve
    
    mi "Ну всё хватит вам. Приятного аппетита, Ульяна."
    
    us "Спасибо!"
    
    hide us laugh2 sport with dissolve

    hide dv angry pioneer with dissolve
    
    hide mi smile pioneer with dissolve
    
    scene cg d1_food_normal with dissolve
    
    "Наконец я принялся за еду.{w} По вкусу вполне себе достойно.{w} На порядок лучше того, чем меня кормили в школе.{w} Для меня по сей день загадка, как можно было херово приготовить пюре, ладно еще котлету. "
    
    scene bg int_dining_hall_people_day with dissolve
    
    show mi normal pioneer at right with dissolve
    
    show dv normal pioneer with dissolve
    
    show us normal sport at left with dissolve
    
    "Закончив трапезу и отнеся поднос с посудой, я вернулся к своей компании."
    
    me "Не хочу вас напрягать, наверное, сам обойду остальное."
    
    hide mi normal pioneer with dissolve

    show mi smile pioneer at right with dissolve
    
    mi "Ты о чём?{w} Я ведь сказала, мы с Алисой тебе все покажем."
    
    me "Просто у вас, наверное, свои планы."
    
    hide dv normal pioneer with dissolve
    
    show dv smile pioneer with dissolve
    
    dv "Да ладно, тебе!{w} Сейчас у нашего отряда, кажется, по расписанию пляж.{w} Но сегодня только второй день смены, ещё успеем."
    
    me "А сколько смена продлиться? Что-то из головы вылетело."
    
    dv "Значит, нам точно нужно с тобой идти,{w} а то дорогу тебе расскажем - у тебя и это из головы вылетит.{w} Потеряешься ещё, оно тебе надо?"
   
    mi "Точно-точно.{w} Зайдем еще к медсестре, она тебе таблетки для памяти выпишет."
    
    me "Очень смешно."
    
    dv "Ничего смешного. Это очень серьёзно, особенно в столь юном возрасте."
    
    "Не унималась Алиса."
    
    me "Хорошо я понял.{w} Идём вместе."
    
    mi "Вот и славно. Сейчас посуду только отнесем и надо будет вожатую предупредить, что мы с тобой идём."
    
    "Голос подала Ульяна, которая, на удивление, всё это время сидела молча."
    
    hide us normal sport with dissolve
    
    show us dontlike sport at left with dissolve
    
    us "Я никому ничего не обещала и пойду на пляж.{w} Вы как хотите."
    
    hide us dontlike sport with dissolve
    
    "Она встала из-за стола и удалилась."
    
    dv "Ну и иди!"
    
    "Крикнула ей в след Алиса."
    
    mi "Сень, жди нас у выхода, мы пока тарелки отнесём."
    
    me "Хорошо, если встречу Ольгу Дмитриевну, скажу, что вы со мной."
    
    hide mi smile pioneer with dissolve
    
    hide dv smile pioneer with dissolve
    
    stop ambience
    
    play ambience ambience_camp_center_day fadein 1
    
    scene bg ext_dining_hall_near_day with dissolve

    "На выходе, перед лестницей стояла Ольга."
    
    show mt grin pioneer with dissolve
    
    mt "Как раз тебя жду.{w} Вижу подружек себе нашёл? Значит дела, твои, идут не плохо."
    
    me "Никого я не…"
    
    th "Спорить бесполезно, она все равно такой реакции и ждёт."
    
    me "Так что вы хотели?"
    
    hide mt grin pioneer with dissolve
    
    show mt smile pioneer with dissolve
    
    mt "Хотела сказать, что можешь не торопится с остальными автографами."
    
    mt "Хотя вообще не надо их собирать, бумажку можешь оставить себе."
    
    me "А без этого цирка с подписями не могли попросить всё осмотреть и вступить куда-нибудь?"
    
    mt "Ты бы так и сделал?"
    
    me "Вряд ли."
    
    mt "То-то же.{w} Тебе наверняка уже сообщили куда мы сейчас идём.{w} Я положила плавки и полотенце тебе на кровать в домике, иди собирайся."
    
    th "Она по всех жилищах так может шастать?{w} Эх, в СССР и вправду всё «наше»."
    
    me "Можно без меня?{w} Хочу уже закончить обход по лагерю.{w} Мику с Алисой хотят со мной пойти.{w} Я их отговаривал, но…"
    
    show dv smile pioneer at right with dissolve

    show mi normal pioneer at left with dissolve
    
    "Как раз вышли вышеупомянутые барышни."
    
    mi "Ольга Дмитриевна!{w} Мы как раз вас искали.{w} В общем я и Алиса пойдем Семёну лагерь покажем, а то территория большая, ещё заблудится.{w} Мы ведь не можем бросить товарища в беде."
    
    mt "Я только что отменила ему задание по изучению лагеря, но, если вы уже настроились прогулять водные процедуры, можете показать окрестности.{w} Только за территорию не выходить!"

    dv "Спасибо, мы тогда прогуляемся."
    
    mt "Хорошо, а я пошла смотреть, чтоб никто не утонул."
    
    hide mt smile pioneer with dissolve
    
    mi "Куда пойдём сначала?"
    
    dv "Можно пройтись по лесу и выйти к озеру, там везде тень и не придётся парится на солнце."
    
    mi "Отличная идея, я за!{w} Ты как, Сень?"
    
    me "Идём."
    
    hide dv smile pioneer with dissolve
    
    hide mi normal pioneer with dissolve
    
    stop ambience
    
    play ambience ambience_forest_day fadein 1
    
    scene bg road_out_camp
    
    "Мы двинули в путь."
    
    show dv smile pioneer at cright with dissolve
    
    show mi normal pioneer at cleft with dissolve
    
    dv "Рассказывай!{w} Что ты, кто ты?{w} Чем увлекаешься, где учишься, куда поступать будешь?{w} Или сразу на завод?"
    
    th "Ничего себе она налетела с расспросами."
    
    scene bg road_out_camp_day with dissolve
    
    show mi normal pioneer at cleft with dissolve
    
    show dv smile pioneer at cright with dissolve
    
    me "Даа…{w} Обычную городскую школу заканчиваю.{w} Куда дальше пойду ещё не знаю."
    
    dv "Мутный ты какой-то, обычная школа, куда пойдешь не знаешь.{w} Нет, ты точно или странный, или скрываешь что-то."
    
    th "Интересно что бы ты сказала, услышав правду.{w} Был бы я не странный, а сумасшедший."
    
    mi "Алиса, ну что ты налетела на него с глупыми вопросами, как родитель.{w} Думаю, всем этого и дома хватает."
    
    dv "Хорошо, Мику, давай ты."

    hide mi normal pioneer with dissolve
    
    show mi smile pioneer at cleft with dissolve
    
    mi "Сень, чем тебе нравится заниматься?" 
    mi "Я вот увлекаюсь музыкой, хожу в музыкальную школу.{w} Играю на гитаре и пианино, вроде неплохо выходит.{w} Дома иногда пою, но выходит весьма посредственно."

    hide dv smile pioneer with dissolve
    
    show dv grin pioneer at cright with dissolve
    
    dv "Ага.{w} Очень посредственно.{w} Не слушай её, Семён.{w} Она поёт не хуже известных певцов."
    
    hide dv grin pioneer with dissolve
    
    show dv smile pioneer at cright with dissolve
    
    hide mi smile pioneer with dissolve
    
    show mi shy pioneer at cleft with dissolve
    
    mi "Ой, да ладно тебе."

    "Она засмущалась и покраснела."
    
    hide mi shy pioneer with dissolve
    
    hide dv smile pioneer with dissolve
    
    scene bg ext_path_day with dissolve
    
    show dv smile pioneer at cright with dissolve
    
    show mi normal pioneer at cleft with dissolve
    
    me "Мне тоже музыка нравится, только я слушаю, а не играю.{w} Ещё почитываю книги иногда"
    
    th "А ещё мне нравится смотреть аниме, фильмы, играть на компе, но оставлю это при себе."
    
    dv "В общем наслаждаешься творчеством других." 
    
    "Подытожила она."  
    
    dv "Что слушаешь?"
    
    me "Ну…{w} Так сразу на ум приходит только Высоцкий и Лещенко, может еще кого вспомню…"
    
    th "Да нет, я всех вспомнил.{w} Только половина из них ещё не родилась, а другая половина ещё в школу ходит."
    
    dv "Мне тоже они нравятся, здорово было бы хоть на один концерт попасть."
    
    mi "Я тоже хочу, еще ни разу не была на живом выступлении."
    
    me "Обязательно сходите, ещё всё впереди."
    
    dv "А у тебя, позади уже?"
    
    me "Нет конечно, с чего ты так решила?"
    
    dv "Формулировка у тебя странная."
    
    mi "Давайте, хоть и через пару лет все вместе сходим?{w} И ещё кого-нибудь позовём!"
    
    me "Звучит неплохо, конечно, но мы, наверное, далековато живем друг от друга.{w} Вы откуда?"
    
    dv "Мы с Мику живём в Ленинграде, и не только мы, ещё Лена, с которой мы тебя познакомим, и Ульянка.{w} Все четверо ходим в одну школу даже."
    
    mi "Как будешь в наших краях, ждём в гости."
    
    stop ambience 
    
    play ambience ambience_lake_shore_day fadein 1
    
    scene bg lake with dissolve
    
    hide mi normal pioneer with dissolve
    
    hide dv smile pioneer with dissolve
    
    show dv smile pioneer far at cright with dissolve
    
    show mi smile pioneer far at cleft with dissolve
    
    mi "Мы пришли!{w} Сейчас бы нырнуть в прохладную водичку!{w} Нужно было сходить надеть купальник."
    
    dv "Это точно! Ну может хоть ноги помочим?"
    
    mi "Давай с нами, Семён."
    
    "Сказала Мику снимая обувь и стягивая чулки."
    
    me "Да нет, я на берегу посижу."
    
    hide dv smile pioneer with dissolve
    
    show dv grin pioneer far at cright with dissolve
    
    dv "Ага, тихонько посидишь и попялишься."
    
    me "И в мыслях не было."
    
    mi "Не нужно быть таким зажатым, водичка класс!"
    
    play sound sfx_draw_water
    
    "Алиса с Мику уже хлюпали ногами по воде."
    
    me "Нет, я правда не хочу, развлекайтесь."
    
    hide mi smile pioneer with dissolve
    
    hide dv grin pioneer with dissolve
    
    show dv normal pioneer at cright with dissolve

    show mi normal pioneer at cleft with dissolve
    
    dv "Развлечешься с тобой. Весь настрой убил своим бурчанием."
    
    "Они вылезли с воды и присели рядом."
    
    mi "Может ты первый раз в лагерь приехал и поэтому не можешь сразу вклиниться в компанию?"
    
    me "Да, это моя первая поездка."
    
    th "В этом мире."
    
    me "Как-то не привычно, вот так сразу познакомились и стали друзьями."
    
    mi "Ну ничего, это мы исправим. Ещё столько всего интересного впереди!"
    
    me "А сколько мы в лагере пробудем?"
    
    mi "Ну ты странный. Как этого можно не знать?"

    me "Забыл спросить перед отъездом."
    
    dv "Тогда пусть для тебя это будет сюрприз!{w} Будешь проживать каждый день как последний."
    
    me "Звучит страшновато."
    
    dv "Да ну тебя, какой нудный!{w} По-моему, очень весело и интригующе.{w} Я б не отказалась быть на твоем месте."
    
    me "Серьёзно, сколько смена длится?"
    
    hide mi with dissolve
    
    show mi smile pioneer at cleft with dissolve
    
    mi "Мы серьёзно не скажем!{w} Наслаждайся каждым моментом!"
    
    me "Непременно.{w} Чем в этом лагере ещё занимаются, помимо купания?"
    
    mi "Ну, например, клубной деятельностью.{w} Также выполняем поручения вожатой или просто развлекаемся кто как может."
    
    dv "Здесь есть большой стадион, где можно сыграть в бадминтон, футбол или просто подурачиться."
    
    mi "Послезавтра ещё танцы будут!"
    
    dv "Да-да!{w} Наш кружок предоставляет аппаратуру и ставит музыку.{w} Мы с Мику работаем посменно. Одна переключает, другая танцует.{w} Если обе хотим потанцевать или пообщаться с кем-то, то можем и Ульянку запрячь."
    
    mi "Все пионеры участвуют, так что и тебе стоит."
    
    me "Это вряд ли.{w} Я предпочту пропустить это мероприятие."
    
    dv "Не получится.{w} Во-первых, ты в нашем кружке, а значит мы одна команда, во-вторых, не придёшь сам - мы тебя принесём."
    
    mi "Всё правильно, Алисик, говоришь.{w} Нельзя же быть таким занудой, вся юность пролетит, потом будешь старый жалеть сидеть."
    
    th "И тут та же песня. Можно только то, что делают все."
    
    me "Я просто не люблю такие шумные мероприятия."
    
    dv "Да расслабься ты, там и танцевать не обязательно.{w} Большинство просто приходят пообщаться с друзьями и музыку послушать.{w} Танцуют в основном парочки и те, кому не сидится, например такие как Ульянка."
    
    mi "Как видишь ничего там страшного нет. Если придёшь не пожалеешь, тем более ты музыкой увлекаешься."
    
    me "Ладно-ладно, если всё так круто как вы говорите, то приду обязательно."
   
    hide dv with dissolve
    
    hide mi with dissolve
 
    show mi smile pioneer at cleft with dissolve

    show dv smile pioneer at cright with dissolve
    
    dv "Ну вот же. На глазах в человека превращаешься."
    
    mi "Может будем потихоньку возвращаться?{w} Остальные уже должны были вернуться.{w} Заодно можем зайти за Леной и Женей и вместе пойдем на ужин.{w} Ты с ними ведь не знаком ещё?"
    
    me "Нет."
    
    mi "А тебя с кем поселили?"
    
    me "Я сам живу.{w} Мне не нашли сожителя."
   
    dv "Свезло. Меня Ульяна постоянно из себя выводит…"
    
    mi "Да что ты говоришь! Вы обе стоите друг друга."
    
    dv "Ты о чем это?"
    
    mi "О том, что все выходки зачастую вы вдвоём проделываете.{w} Например, кто в прошлом году Генду разрисовал?"
    
    dv "В том же году кто с нами с похода сбегал?"
    
    hide mi with dissolve
    
    show mi dontlike pioneer at cleft with dissolve
    
    mi "Так, всё. Это было один раз! Идём уже обратно."
    
    dv "Идём-идём."
    
    stop ambience
    
    play ambience ambience_forest_day fadein 1
    
    hide dv with dissolve
    
    hide mi with dissolve
    
    scene bg ext_path_day with dissolve
    
    "Всю дорогу обратно в лагерь я молчал, общались только девочки.{w}Что мне удалось узнать об этом месте?"
    
    "Первое, это действительно пионерлагерь и второе,{w} я на самом деле в прошлом, а точнее во времена СССР.{w} Причём далеко от родного города."
    
    "Вот только местные обитатели здесь никак не вяжутся с началом 80-х.{w} У всех слишком броская внешность.{w} Даже в 21ом веке люди так не выделяются, не говоря уже про жителей СССР."
    
    scene bg road_out_camp_day with dissolve
    
    "Может это какой-то параллельный мир?{w} Очень на то похоже.{w} Нужно выяснить что ещё тут общее с моей вселенной."
    
    "Чутьё подсказывает, если я доберусь до ближайшего города,{w} то ничего меня там не ждёт."
    
    scene bg road_out_camp with dissolve
    
    "Ведь у меня нет денег и звонить некуда."
    
    scene bg ext_houses_day with dissolve
    
    play ambience ambience_camp_center_day fadein 1

    "Из раздумий меня вывела Алиса."
    
    show dv normal pioneer at cright with dissolve
    
    show mi normal pioneer at cleft with dissolve
    
    dv "Эй! Ты чё в облаках летаешь?"
    
    me "А что нельзя?"
    
    dv "Не зли меня."
    
    me "Чем?"
    
    scene bg ext_library_day with dissolve
    
    show dv normal pioneer at cright with dissolve
    
    show mi normal pioneer at cleft with dissolve
    
    mi "Успокойтесь. Вот уже и библиотека."
    
    play sound sfx_door_squeak_light
    
    stop ambience
    
    play ambience ambience_library_day fadein 1
    
    scene bg int_library_day with dissolve

    "Внутри была пионерка. Она выделялась забавными косичками и, помимо этого, имела неестественный цвет волос для этого времени. "
    
    show un normal pioneer far with dissolve:
        xcenter 0.44 ycenter 0.50

    show mi normal pioneer far with dissolve:
        xcenter 0.23 ycenter 0.50
    
    show dv normal pioneer far with dissolve:
        xcenter 0.64 ycenter 0.50
    
    mi "Привет, Леночка! А где Женя?"
    
    un "Привет, Женя со мной."
    
    mz "Я здесь."
    
    "Вышла из-за стеллажа с книгами ещё одна пионерка."
    
    show mz normal glasses pioneer far at fright with dissolve

    "Здравствуйте, кто это с вами?{w} Новенький?"
    
    me "Да, сегодня приехал, я Семён."
    
    mz "Я здесь выполняю роль библиотекаря.{w} Это Лена - моя помощница."
    
    hide un with dissolve
    
    show un smile pioneer far with dissolve:
        xcenter 0.44 ycenter 0.50
    
    un "Рада знакомству. Как первые впечатления от лагеря?"
    
    me "Вроде не плохо, в целом мне нравится."
    
    mi "Вы как покупались?"
    
    mz "Великолепно."
    
    "С каменным лицом произнесла Женя."
    
    mz "А вы где были?"
    
    dv "Показывали местные красоты новоприбывшему.{w} Прогулялись по лесу, посидели у озера."
    
    mz "Надо было меня с собой звать,{w} не очень я люблю плескаться в воде и жариться на солнце."
    
    mi "В следующий раз обязательно позовем!{w} А может и завтра сходим?"
    
    dv "Нет, второй раз подряд Ольга Дмитриевна точно не разрешит отклоняться от графика."
    
    un "Ульяна сегодня предлагала на днях сходить ближе к ночи в старый лагерь.{w} Сказала испытание на смелость какое-то."
    
    hide mi with dissolve
    
    show mi sad pioneer far with dissolve:
        xcenter 0.23 ycenter 0.50
        
    mi "Ой не люблю я такое…"
    
    hide mi with dissolve
    
    show mi normal pioneer far with dissolve:
        xcenter 0.23 ycenter 0.50
        
    dv "Просто ты трусиха Мику.{w} Я с удовольствием пойду.{w} Остальные как?"
    
    mz "Детский сад какой-то, я пас.{w} Найду более интересное для себя занятие."
    
    dv "Даже знаю какое, опять в книжку уткнешься."
    
    mz "И что такого?"
    
    dv "Да ничего, дело твоё.{w} Семён, Лена, вы что скажете?"
    
    me "Почему нет?{w} Я пойду."
    
    un "Ну… Если Мику пойдёт, то я тоже.{w} Но я так понимаю это не официальное мероприятие?"
    
    dv "Конечно нет.{w} Кто бы нас пустил ночью."
    
    mi "А ты прям ночью хочешь идти?{w} Даже не знаю… Что если вожатая узнает?"
    
    dv "Да как она узнает?{w} Ты думаешь она по ночам в каждый домик заглядывает?"
    
    mi "Ладно, если все идут, то я тоже."
    
    mz "Я значит в число всех не вхожу?"
    
    dv "Ой да ладно тебе, что к словам придираешься?"
    
    mi "Я хочу, просто и вправду побаиваюсь.{w} Мне и страшно, и в тоже время интересно, поэтому всё-таки пойду."
    
    play sound sfx_dinner_horn_processed
    
    mi "О, уже ужин. Идём?"
    
    un "Вы идите, мы с Женей попозже,{w} нам нужно ещё кое-что доделать."
    
    mi "Смотрите, не пропустите.{w} Мы пошли!"
    
    hide mi with dissolve
    
    hide un with dissolve
    
    hide dv with dissolve
    
    hide mz with dissolve
    
    stop ambience
    
    play ambience ambience_dining_hall_full fadein 1
    
    scene bg int_dining_hall_people_day with dissolve

    "На ужин давали гречневую кашу с жареной рыбой и стаканом узвара.{w} Только мы принялись за еду, к нам подсела Ульянка."
    
    show mi normal pioneer with dissolve
    
    show dv normal pioneer at fleft with dissolve
    
    show us smile pioneer at fright with dissolve
    
    us "И где вас носило?"
    
    hide dv with dissolve
    
    show dv smile pioneer at fleft with dissolve
    
    dv "Тебе то какое дело?"
    
    hide us with dissolve
    
    show us dontlike pioneer at fright with dissolve
    
    us "Что ты вредничаешь опять.{w} Спросить уже нельзя?"
    
    mi "Просто прогулялись немного,{w} а на обратном пути зашли в библиотеку к Лене с Женей."
    
    hide us with dissolve
    
    show us normal pioneer at fright with dissolve
    
    us "Они вам передали мой план?"
    
    dv "А как же,{w} все идут кроме Жени."
    
    us "И даже Лена?"
    
    mi "Ага."
    
    us "Ну Женя предсказуемо не захотела,{w} но я не думала, что Лена согласиться."
    
    me "Может послезавтра тогда пойдём?"
    
    us "Почему не завтра?"
    
    me "Сегодня, как я понимаю, второй день смены.{w} Поэтому не стоит так рано правила нарушать и шастать по ночам.{w} Плюс, я сегодня только приехал и у Ольги Дмитриевны, как мне кажется, повышенное внимание ко мне.{w} Давайте через день лучше." 
    
    dv "А ты умён.{w} Тогда так и поступим.{w} Чем сейчас займёмся?{w} До отбоя ещё далеко."
    
    mi "Идём в наш клуб посидим, поиграем.{w} Послушаем игру Семёна."
    
    stop ambience
     
    hide us with dissolve
    
    hide mi with dissolve
    
    hide dv with dissolve
    
    stop ambience
    
    $ sunset_time()
    $ persistent.sprite_time = 'sunset'
    
    scene bg ext_music_club_verandah_day with dissolve    
    
    play ambience ambience_camp_center_day fadein 1
    
    "Через пару минут мы с Ульяной, Алисой и Мику стояли на пороге музкружка,{w} последняя достала из нагрудного карманчика ключ, открыла дверь и жестом пригласила нас во внутрь."
    
    play sound sfx_key_drawer
    
    stop ambience
    
    play ambience ambience_music_club_day fadein 1
    
    scene bg inside_music_club_sunset with dissolve
    
    show mi normal pioneer with dissolve
    
    show dv smile pioneer at fright with dissolve
    
    show us smile pioneer at fleft with dissolve

    us "Так, Семёныч!{w} Рассказывай на чем играть хочешь, хотя выбор у тебя невелик, можем выделить тебе акустическую гитару.{w} Я на барабанах, Алиса на электрогитаре, Мику на вокале."
    
    me "Стоп, подожди.{w} Я не сильно-то умею на гитаре, когда-то занимался ею, но это было когда-то."
    
    us "Зачем тогда к нам вступил?{w} Как нам с тобой выступать в конце смены?{w} Все члены каждого кружка на концерте в честь закрытия смены показывают, так сказать, чем они занимались."
    
    me "Я про концерт ничего не знал.{w} А когда закрытие смены собственно?"
    
    hide us with dissolve
    
    show us normal pioneer at fleft with dissolve
    
    us "Ну как когда?{w} Сегодня 14ое июля, смена заканчивается 28го."
    
    me "И нужно было эти даты от меня скрывать?"
    
    "Посмотрел я на Алису и Мику."
    
    dv "Ой да ладно тебе.{w} Не сегодня - так завтра б сказали.{w} А то, что ты играешь так себе, как я поняла – не хорошо.{w} Я думала готовиться за 3-4 дня до выступления,{w} мы то умеем кое-что, но походу тебя придется раньше начинать натаскивать.{w} Может, пока не поздно, к кибернетикам перейдёшь?"
    
    hide mi with dissolve
    
    show mi angry pioneer with dissolve
    
    mi "Никто никуда не переходит!{w} Я тебя пригласила, я тебя и научу - гитара мой конёк как-никак.{w} И ты, Алиса, не выделывайся тут, сама в прошлом году ничего не умела.{w} Забыла?"

    hide dv with dissolve
    
    show dv guilty pioneer at fright with dissolve
    
    "Алиса стыдливо отвела взгляд."
    
    me "Спасибо, Мику. Я буду стараться."
    
    hide mi with dissolve
    
    show mi grin pioneer with dissolve
    
    mi "Вот это правильный настрой!"
    
    hide mi with dissolve
    
    show mi normal pioneer with dissolve

    mi "Получается мне не придется петь и играть одновременно на гитаре, это, знаешь ли, не очень просто."
    
    hide dv with dissolve
    
    show dv grin pioneer at fright with dissolve
    
    dv "Не упало бы качество музыки от разделения обязанностей с Семёном… "
    
    hide mi with dissolve
    
    show mi angry pioneer with dissolve
    
    mi "Алиса!{w} Угомонись уже!{w} Никто ещё даже ничего не пробовал сыграть, а ты нагнетаешь."
    
    hide dv with dissolve
    
    show dv smile pioneer at fright with dissolve
    
    dv "Да чего ты так завелась?{w} Шучу просто.{w} Подбодрить таким образом пытаюсь, замотивировать." 
    
    hide mi with dissolve
    
    show mi serious pioneer with dissolve
    
    mi "Ну можно же как-то иначе это сделать.{w} Давайте может лучше что-нибудь сыграть попробуем?"
    
    hide us with dissolve
    
    show us smile pioneer at fleft with dissolve

    us "Да куда спешить?{w} Второй день только, впереди практически две недели ещё.{w} Может поиграем во что-нибудь?"
    
    mi "Думаю можно."
    
    hide mi with dissolve
    
    show mi smile pioneer with dissolve
    
    "Она резко сменила серьёзность улыбкой."
    
    mi "Во что предлагаешь?"
    
    us "У меня карты здесь припрятаны. Все согласны?"
    
    dv "Только за!"
    
    me "Я не против."
    
    hide mi with dissolve
    
    hide dv with dissolve
    
    hide us with dissolve
    
    "Играли несколько часов напролёт, разговаривали о всякой бессмыслице.{w} После игры снова болтали, девочки немного рассказывали о себе.{w} Я же пытался сочинять правдоподобную легенду:{w} кто я и откуда."
    
    show mi normal pioneer with dissolve
    
    show dv normal pioneer at fright with dissolve
    
    show us normal pioneer at fleft with dissolve
    
    "Мику посмотрела на часы на стене и сказала."
    
    mi "Уже почти 10, меня уже в сон клонить начинает, сегодня ещё и подъём ранний с непривычки.{w} Может всё на сегодня?"
    
    dv "Ну тогда пошли по домам."
    
    stop ambience
    
    play ambience ambience_camp_center_night fadein 1
    
    scene bg ext_mimusicclub_night with dissolve
    
    "Вышли из клуба. Мику заперла дверь, забрала ключ с собой."
    
    $ night_time()
    $ persistent.sprite_time = 'night'
    
    scene bg houses_night with dissolve
    
    "Дошли до первого поворота."
    
    show mi smile pioneer with dissolve
    
    show dv smile pioneer at fright with dissolve
    
    show us smile pioneer at fleft with dissolve

    us "Ну бывайте!{w} Мы в этой части лагеря проживаем."
    
    mi "Пока-пока! Спокойной ночи."
    
    dv "Спокойной ночи, Мику! А ты чтоб довёл её в целости и сохранности."
    
    me "Непременно, бывайте."
    
    hide us with dissolve
    
    hide mi with dissolve
    
    hide dv with dissolve
    
    "Дальше мы шли с Мику вдвоём."
    
    show mi normal pioneer with dissolve
    
    me "Полагаю ты живёшь в той же части лагеря, где и я?"
    
    mi "Да.{w} У тебя какой номер домика?"
    
    me "16й, возле вожатой."
    
    mi "У меня 13й на той же…{w} Линии? Или правильней сказать улице? Даже не знаю."
    
    scene bg cum_hata_night with dissolve
    
    show mi normal pioneer with dissolve
    
    me "Ну, до завтра."
    
    mi "До завтра…" 
    
    hide mi with dissolve
    
    show mi shy pioneer with dissolve
    
    mi "Стой.{w} Можешь…{w} провести меня…{w} я в последнем живу…{w} там темно просто…{w} если ты не спешишь…{w} то есть не против…"  
    
    "Непривычно для самой себя начала мямлить Мику, смущённо смотря в землю."
    
    me "А… да…{w} Конечно, пошли проведу."
    
    scene bg houses_night with dissolve

    "Дальше мы шли молча."
    
    th "Понятия не имею что сейчас говорить, да и нужно ли вообще.{w} Она, судя по всему, тоже."
    
    scene bg ext_house_of_mi_night with dissolve
    
    show mi normal pioneer with dissolve
    
    mi "Пришли.{w} Спасибо и спокойной ночи."
    
    "Она на секунду подняла глаза, слегка улыбаясь."
    
    me "Да… и тебе."
    
    scene bg cum_hata_night with dissolve
    
    "Я пошёл обратно к себе. Возле своего домика встретился с вожатой."
    
    show mt normal pioneer with dissolve
    
    mt "О! Я думаю, где тебя носит?{w} Неужели первый день не понравился и сбежать решил?{w} Уже вообще-то время отбоя, но для старшего отряда я на это глаза закрываю."
    
    hide mt with dissolve
    
    show mt smile pioneer with dissolve
    
    mt "Понимаю, что вы не дети малые загонять вас в 10 в койку.{w} Хочется погулять, пообщаться, юность, гормоны все дела… "
    
    mt "Поэтому после отбоя главное тихо вести себя и не привлекать лишнего внимания.{w} Понял?"
    
    me "Понял."
    
    mt "Так где был?"
    
    me "Мику провёл…"
    
    "Хотел добавить, что та сама попросила, но почему-то ком в горле застрял."
    
    mt "Это ты молодец.{w} Линейка в 8 начинается, завтрак в 8-30.{w} Поставить будильник на 7-30 чтобы ещё себя в порядок привести.{w} Щётка, зубной порошок, полотенца я отнесла к тебе."
    
    mt "Вроде ничего не забыла.{w} Увидимся завтра."
    
    me "Увидимся."
    
    stop ambience
    
    play ambience ambience_int_cabin_night fadein 1
    
    scene bg cum_room_light_night with dissolve
    
    play sound sfx_open_door_2

    "Вошёл к себе.{w} На столе пакет со средствами гигиены и часы на маленьких ножках.{w} Покрутил часы в руках."
    
    th "И как тут будильник наводиться?{w} Ладно, хер с ним, так встану."
    
    scene bg cum_room_night with dissolve
    
    "Лёг в постель.{w} Тишина.{w} Наконец-то остался наедине с мыслями.{w} Прокручивал в голове вчерашнюю поездку в автобусе и сегодняшний день в лагере.{w} Не мог понять, как такое произошло." 
    "Как здесь очутился?{w} Пионерлагерь, прошлое, СССР.{w} Вроде не раз удостоверился что мир реален,{w} но какая-то часть меня всё равно отказывалась принимать произошедшее за правду." 
    "Есть ли вероятность что сейчас усну и проснусь у себя дома или хотя бы в своём времени?{w} Может принять всё случившееся и просто смотреть, что будет дальше?{w} За весь день почему-то ни разу не задумался, что там родные и так называемые друзья думают." 
    "Заметили ли они мою пропажу, а может им ещё предстоит заметить." 
    "Меня это совсем не волновало.{w} Куча вопросов еще крутилась в голове, хоть бы на один найти ответ."
    
    stop ambience
    
    show unblink
    
    scene bg black with dissolve
    
    show blinking
    
    $ day_time()
    $ persistent.sprite_time = 'day'
    
    play music music_list['door_to_nightmare'] fadein 1
    
    show prologue_dream
    
    show uv normal far with dissolve

    uvp "Здраствуй."
    
    me "Ты кто?"
    
    uv "Юля."
    
    me "Почему у тебя уши...?"
    
    uv "Это не важно."
    
    me "А что тогда важно?"
    
    uv "Как тебе здесь, нравится?"
    
    me "В лагере?"
    
    uv "Да.{w} Нравится?"
    
    me "Не знаю.{w} Как я сюда попал?"
    
    uv "Ты ведь всегда хотел здесь оказаться."
    
    me "Я никогда не хотел в пионерлагерь."
    
    uv "Важен не сам лагерь, а то, что в нём."
    
    me "Что в нём?"
    
    uv "Сам мне скажи.{w} Хотя пробыл ты тут пока не долго, но постарайся ответить на свой вопрос побыстрее."
    
    me "Зачем?{w} Я могу вернуться назад?"
    
    uv "Ты хочешь обратно?"
    
    me "Не знаю…{w} Наверное…"
    
    uv "Остаться здесь хочешь?"
    
    me "Не знаю…{w} Как я сюда попал?{w} Ответь, пожалуйста."
    
    uv "Ты этого хотел.{w} Это желание копилось в тебе очень долго, вот мировая линия и выбросила тебя."
    
    me "Что значит выбросила?{w} Куда линия меня выбросила?"
    
    uv "На другую линию.{w} На ту, где ты хотел быть."
    
    me "Я теперь тут всегда буду… жить?"
    
    uv "От тебя зависит.{w} Ты ни на одной линии пока не закрепился.{w} Не смог."
    
    me "Как мне закрепиться на одной из них?"
    
    uv "Так же, как и попал сюда.{w} Захотеть."
    
    me "Я тебя вообще не понимаю…"
    
    uv "Главное решить, где ты хочешь жить."
    
    hide prologue_dream
    
    stop music fadeout 1
    
    jump EvSuDAY_2
    
    
    
    
    
    
    
    

    
    
    
    

    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    

    
    
    
    
    

    
    


    
    
    
    

    
    
    
    
    
    
    
    
  

