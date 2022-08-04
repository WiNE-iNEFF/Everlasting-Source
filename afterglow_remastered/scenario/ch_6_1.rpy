label agr_day_6:

    $ backdrop = "days"
    $ agr_new_chapter(10, "Аномалия")
    $ persistent.sprite_time = "day"
    $ day_time()
    pause(1)
    window auto
    scene bg ext_bathhouse_day with dissolve
    play music seven_summer_day fadein 3
    $ karta_otkrytie = True

    "Подходил к середине август месяц. Как и предрекал Шурик, практически сразу после катастрофы, климат начал меняться."
    "Раз в неделю стабильно приходили штормы, продолжающиеся часами, а то и днями. Эфир на коротких волнах иногда заполняли чьи-то переговоры, монологи и инструкции."
    "Радиация оставалась на том же уровне, и тем не менее, к реке мы ходили лишь единожды, замеряя фон."

    scene white with dissolve
    $ prolog_time()
    scene bg ext_boathouse_after_rain
    show gas_mask
    show prologue_dream
    with dissolve
    $ karta_otkrytie = False
    play sound tresk_gaygera_piz loop

    me "Что там?"
    el "Ну же, дрянь, работай…{w=2} так-так…{w=1} это если перевести…{w=2} Всё, валим."
    me "Сколько там?"
    "Сквозь маску противогаза было плохо слышно."
    el "Четверть зиверта в час."
    me "Это критично?"
    el "Это неприятно, но не смертельно. Тут большую опасность представляют продукты распада и прочая дрянь, что с ГЭС утекла."
    "Главными проблемами оставались электричество и топливо для котельной. Дровами можно было запастись на месяца три-четыре — а надо было больше, значительно больше."
    "Мы съехались с Алисой окончательно, а Ульяна переехала к Славе.{w} Жизнь потихоньку налаживалась."
    "Шурик раз в два дня лазил в бункер. Таскал всё: от сухпайков до одежды и спального белья."
    "Сам лагерь потихоньку начинал напоминать крепость."

    stop music fadeout 3

    extend " Ворота не открывали."

    stop sound fadeout 1
    play ambience ambience_forest_day fadein 3
    scene bg ext_bathhouse_day with dissolve
    $ day_time()
    $ karta_otkrytie = True

    "Я закончил рубить дрова, сложил в поленницу у бани. Сегодня парились девушки."

    window hide
    show mt smile pioneer with dissolve
    window auto

    mt "Спасибо, Семён. Ты молодец."
    mt "Что бы мы без вас делали, без мальчиков..."
    me "Привет, Оль. Слушай, там Шурик мыло неплохое надыбал, спроси у него."
    mt "Непременно. Холодает не по дням, а по часам. Думаешь, уложимся за пару недель?"
    me "Понятия не имею."
    me "Алиса и Мику сейчас со Славей, вроде, возятся с саженцами.{w} Лену с Виолой из леса хрен вытащишь.{w} Кибернетики уже заняты...{w} Разве что Ульянку подключать."

    play music music_list["get_to_know_me_better"] fadein 3
    stop ambience fadeout 3

    "Работы было навалом. Девочки, после того как мы с Шуриком вытащили из недр бомбоубежища коробку с семенами, занялись садоводством."
    "Выкинув ненужные, декоративные цветы из всех ваз, что нашли в лагере, они переоборудовали их под контейнеры."
    "На складе нашлась ещё парочка банок и деревянных коробок, а значит, что к зиме, если только не подохнет в комнатной температуре, должен быть первый урожай."
    "Котельная работала исправно — проверяли."
    me "Я пойду, помогу Серёге, он что-то хотел."
    mt "Давай."

    scene bg ext_backroad_day with dissolve

    "Пока шёл в лагерь, встретил медсестру и Лену. Обе шли с наполненными, по крайней мере наполовину, корзинками. В нос ударил едва уловимый, грибной запах."

    window hide
    show cs normal ag_civil at left
    show un shy pioneer at right
    with dissolve
    window auto

    me "Как улов, дамы?"

    show un smile pioneer with dspr

    un "Ой, Сёма, привет. Больше обычного! Мы такую полянку нашли, много грибов было!"

    show cs smile ag_civil with dspr

    cs "Да, всё весьма удачно."
    "Виола сменила медицинский халат на ту одежду, в которой приехала в лагерь. Поначалу было непривычно, но сейчас, на такие банальности никто не обращал внимания."

    scene bg black with dissolve2
    stop music fadeout 3
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_square_day
    show cs smile ag_civil at left
    show un smile pioneer at right
    with dissolve2

    "Изредка перекидываясь фразами, мы дошли до площади, где и разминулись."

    scene bg ext_square_day with dissolve

    "Девушки ушли в столовую, а я направился в сторону клубов, где наверняка, сейчас, были кибернетики."

    scene bg ext_clubs_day with dissolve

    "На двери клубов висела записка, написанная карандашом."
    "\"{i}Мы утепляем домики, ждите только к обеду. Шурик.{/i}\""
    th "Недурно. Чем, интересно, утепляют? Мне Саня ничего не рассказывал."
    "Твёрдо решив не тратить времени зря, я направился в сторону домиков."

    scene bg ext_houses_day with dissolve

    "Календарь будто врал, опаздывая на месяц-полтора. По ощущениям, на улице была осень, но деревья только начали желтеть, трава ещё была зелена."
    "Только прохлада, даже в самые жаркие часы, где-то плюс десять градусов, говорила об обратном."
    "По пути встретил Мику. Девушка шла, держась за живот, чуть покачиваясь."
    "Завидев неладное, я споро перешёл на бег, за пару секунд оказавшись рядом с японкой."

    window hide
    show mi normal pioneer with dissolve
    window auto

    mi "Привет, Сём."
    me "Присядь."

    show bg ext_houses_day:
        zoom 1.0
        ease 0.8 zoom 1.12 truecenter
    show mi normal pioneer at sit_close

    "Рядом удачно оказалась лавочка."
    me "Рассказывай, что болит? Хотя, это, скорее, к Виоле тебе надо..."

    show mi upset with dspr

    mi "Живот тянет вторые сутки."
    me "Отравилась, может?"
    "Я быстро прикинул, что наша компания ела последние пару дней."

    show mi normal pioneer with dspr

    mi "Не, это по женской…{w=2}{nw}"

    show mi scared pioneer with dspr

    extend " ой…{w=1}{nw}"

    hide mi with dspr

    "Девушка не успела договорить, отвернулась, свесив голову через лавочку. Я только и успел придержать роскошные, аквамариновые хвостики, сохранившие, несмотря ни на что, свою шелковистость."
    "Рвало её недолго, но я полностью отдавал себе отчёт, что ничего хорошего происходящее не сулило."
    "Как только её отпустило, я помог ей встать, и мы медленно пошли в сторону медпункта."

    window hide
    scene bg ext_square_day with dissolve
    show mi cry_smile pioneer at left with dissolve
    window auto

    mi "Сень, ты прости…"
    me "Да ты чего, всё хорошо. Сейчас дойдём до медсестры, она тебя мигом подлатает."

    show mi sad pioneer at left with dspr

    mi "Хорошо."

    window hide
    show sh normal pioneer far at fright with dissolve
    window auto

    "Вдалеке замаячила знакомая фигура с узнаваемым ящиком для инструментов."

    show sh normal pioneer at right with dspr

    "Шурик буквально подлетел к нам и недолго думая подменил меня."
    sh "Чего произошло? Привет, Сём."
    me "Виделись. У неё, вон, спроси. Виола в медпункте."
    sh "Погоди, там Славя в лесу какую-то хрень нашла."
    me "Успеется. Как разберётесь, дуйте в столовую."
    sh "Ладно."

    scene bg ext_square_day with dissolve

    th "Какую хрень Славя могла найти в лесу? Мы ж его уже вдоль и поперёк исходили...{w} Разве что в стороне озёр?"

    scene bg ext_dining_hall_away_day with dissolve

    "К озёрам мы не ходили. Не потому что это было опасно, нет, отнюдь. Просто далеко, а воду брали в лесном ручье, неподалёку от лагеря."

    window hide
    show dv normal pioneer far
    show sl normal pioneer far at right
    with dissolve
    window auto

    "Около столовой стояла Славяна, что-то активно рассказывая Алисе. Моя рыженькая с того времени, как мы съехались, для остальных никак не изменилась.{w} Но не для меня."
    "Оказалось, что она весьма недурно готовит, а образ хулиганки оказался лишь маской, за которой пряталась начитанная, опрятная и умная девушка."

    scene bg ext_dining_hall_near_day
    show dv surprise pioneer
    show sl scared pioneer at fright
    with dissolve

    me "Что случилось?"

    stop ambience fadeout 5

    "С улыбкой спросил я, подойдя поближе."

    play music music_list["no_tresspassing"] fadein 3

    "В глазах у Слави стояли ледяной стеной искреннее непонимание и страх. Такой же страх, какой испытывали все мы в день катастрофы."
    sl "Я искала грибные места, всё как обычно."
    sl "Зашла чуть дальше, чем обычно. Там озерцо небольшое, а над ним {w=1}{b}оно{/b}."
    "На последнем слове девушка сделала яркий акцент."
    me "Что — {b}оно{/b}?"
    sl "Не знаю. Это… необъяснимая штука какая-то."
    me "Дорогу запомнила?"
    sl "Да."

    show dv normal pioneer with dspr
    stop music fadeout 5

    dv "Ну вот, как поедим, так и сводишь. Сём, кушать хочу, пойдём."

    scene bg int_dining_hall_day with dissolve
    play music re_mebuki fadein 3

    "В столовой были Электроник, Женя и Лена. Вся компания вовсю готовила что-то обворожительное, пахнущее грибами."
    "Сухпайки из бункера мы расходовали максимально экономно, запасаясь на зиму. Помнится, Ольга как-то даже хлеб испекла."
    "Ну как, хлеб… Булка какая-то пресная, но вкуснее хлеба я не ел никогда."
    "Благо с самой готовкой проблем не возникало и не планировалось их иметь как минимум до весны. Все конфорки работали на газу, а его ещё в начале смены завезли с запасом. И конечно, экономили, как могли."
    "Решив, что на кухне буду лишним, я уселся за столик, облокотившись на спинку стула. Алиса, последнее время, выглядела особенно уставшей, хоть виду и не подавала."
    "Ночью приходила и падала на кровать без задних ног, с утра уходила возиться с растениями или готовить оборудование для рыбалки."
    "Помню, как-то проснулась ночью, вся в слезах, вцепилась в меня, как бездомный котёнок. И ничего не поделать, как бы не хотелось."
    "Пока что, я вывозил объёмы работ и даже находил время помогать моей рыжей, но постепенно сдавали и нервы, и мускулы. Каждый работал на износ, чтобы завтра наступило."

    window hide
    show dv normal pioneer with dissolve
    window auto

    "Алиса уселась напротив меня за столик."
    dv "Знал бы ты, Сёмка, как фартук этот достал, и растения эти…"

    show dv smile pioneer with dspr

    dv "Помню, в прошлом году в это время сидела с ребятами из Киева, орали Башлачёва. Мы тогда уже у бабушки жили, с кем-то даже подружилась."
    me "Потерпи ещё немного, родная. Вот смотри, к сентябрю должны основные работы закончить, останется всего-ничего."
    me "А там что? Гоняй балду, лови рыбку, да и растения твои к тому моменту в такой заботе нуждаться не будут."

    show dv sad pioneer with dspr

    dv "Не надо больше про них, слышать не хочу."
    "С кухни послышался голос Лены."
    un "Через минут пять всё будет готово, зови остальных."
    "Я сжал в руках холодную, Алисину ладошку, погладил огрубевшую от работы кожу."

    show dv smile pioneer with dspr

    dv "Иди, Сёмка."

    stop music fadeout 5

    "На лице девушки показалась грустная улыбка."

    window hide
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_dining_hall_near_day with dissolve
    show cs normal ag_civil at cleft
    show mi surprise pioneer at cright
    with dissolve
    window auto

    "Впрочем, далеко идти не пришлось. На крыльце пересёкся с медсестрой и Мику."
    "Японка была краснее помидора, Виола же была скорее встревожена." #Сталкерюга одобрил джинсы Виолы
    me "Чего там?"
    "Виола на секунду закусила губу."

    show cs smile ag_civil with dspr

    cs "Шурика найди."
    me "Сейчас подойти должен."
    cs "Хорошо."

    scene bg ext_square_day with dissolve

    "Техника встретил на площади с озадаченным видом."

    window hide
    show sh serious pioneer with dissolve
    window auto

    me "Шур, там Виола что-то хотела. Ты Ольгу нигде не видел?"
    sh "Ща, через пару минут должна прийти."

    show sh normal pioneer with dspr

    sh "А в чём там дело-то у моей? Грибы небось эти, тьфу."
    "Я развёл руками."
    me "Врач рекомендаций не давал."

    show sh serious pioneer with dspr

    sh "Пошли разбираться."

    scene bg black with dissolve
    pause(1)
    scene bg ext_dining_hall_away_day
    show sh serious pioneer
    with dissolve

    "Какое-то время мы шли молча."
    me "Я так понял, до медпункта ты её всё-таки довёл?"

    show sh normal pioneer with dspr

    sh "Нам Виола на полпути встретилась."
    me "Лады. Не переживай ты, всё с твоей японкой хорошо будет."

    show sh serious pioneer with dspr
    stop ambience fadeout 3

    sh "Надеюсь."

    scene bg black with dissolve
    play ambience ambience_dining_hall_empty fadein 3
    scene bg int_dining_hall_day with dissolve

    if persistent.easter_egg == True:
        "Сегодняшний обед, по совместительству ужин, был роскошным. Жареный Ритан и парочка подосиновиков." # Ритан одобрил
    else:
        "Сегодняшний обед, по совместительству ужин, был роскошным. Жареный ротан и парочка подосиновиков."
    "Улька выбила себе белый гриб, на что, в принципе, могла спокойно претендовать."
    "Девочка хорошо знала окрестные леса и весьма увлечённо рыбачила, обеспечивая нас рыбой, информацией по грибницам и местам, где растут ягоды, иногда таская мелкую дичь."
    "Обычно все во время приёма пищи молчали, но в этот раз медсестра, как только доела, пристально посмотрела на Шурика."

    window hide
    show cs ag_civil normal at cleft with dissolve
    window auto 

    cs "Ну, что ж, Александр."

    window hide
    show sh normal pioneer at cright with dissolve
    window auto
    if persistent.easter_egg == True:
        $ ag_meet('sh', u'Сахаров')
        sh "Да-да?"
    else:
        sh "Да-да?"
    $ agr_meet('sh', u'Шурик')

    show cs smile ag_civil with dspr

    cs "Поздравляю, будешь папашей. Месяцев через восемь."

    stop ambience fadeout 3

    "Над столом повисла гробовая тишина, лицо японки горело. Первой отмерла Славя."

    window hide
    play music philosophy fadein 3
    show sl surprise pioneer at fleft with dissolve
    window auto

    sl "Ой, так вы…"
    "Шурик обалдело пялился в тарелку, пытаясь дрожащими руками поправить очки."

    show sh upset pioneer with dspr

    sh "Я… отцом?"
    cs "Да, Саш. От «этого» дети бывают."

    window hide
    show us surp2 sport with dissolve
    window auto 

    us "От чего «этого»?"
    if persistent.easter_egg == True:
        "Любопытно вставила свои пятьдесят грамм мелкая."
    else:
        "Любопытно вставила свои две копейки мелкая."

    window hide
    show mi cry pioneer at fright with dissolve
    window auto 

    "Японка, видимо, не смогла сдержать поток эмоций, поднялась с места. По аккуратной нежной щеке катилась слезинка."

    window hide
    hide cs
    hide sl
    hide us
    with dissolve
    show sh upset pioneer far:
        xalign 0.7 xanchor 0.5 yanchor 0.0
    show mi sad pioneer far:
        xalign 0.8 xanchor 0.5 yanchor 0.0
    with dissolve
    window auto

    "Шурик резко встал с места, подошёл к ней и крепко обнял. За ним встала Ольга, Лена, Электроник, Женя, Алиса."
    "Все стояли и молча смотрели на техника и музыкантку, замерших в объятиях, будто в последний раз."

    window hide
    # Сюда бы ЦГ соответсвующий. Момент всё-таки такой...
    stop music fadeout 3
    pause(3)
    play music music_list["memories"] fadein 3
    show sh smile pioneer far
    show mi cry_smile pioneer far
    with dspr
    window auto

    "Минута, две, три… время медленно текло. То ли от радости, то ли от чего-то ещё, улыбались и плакали уже все, только Улька непонимающе водила глазами."
    "Я приобнял Алису за талию, Лена тихо нашёптывала что-то Славе. Когда Шурик наконец-то отпустил Мику, он улыбался."

    show sh normal_smile pioneer far
    show mi happy pioneer far
    with dspr

    "Улыбался, как никогда раньше — по-глупому, по-настоящему, от безмерного счастья."
    "Алиса потянулась к моему уху."

    window hide
    show dv smile pioneer close at left with dissolve
    window auto

    dv "Может, мне тоже сходить провериться? А то вдруг…"
    me "Издеваешься? У нас когда последний раз-то был, недели три назад?"

    show dv laugh pioneer close with dissolve

    dv "Не издеваюсь, а шучу."
    "На миг к рыжей вернулся знакомый ехидный тон.{w} Давно, чёрт побери, давно я его не слышал. И горы был готов свернуть, только чтобы он вернулся."

    stop music fadeout 3
    scene bg int_dining_hall_day with dissolve
    play ambience ambience_dining_hall_empty fadein 3

    "Когда девчонки вернулись к еде, нас с Электроником подозвал Шурик."

    window hide
    show sh normal pioneer at right with dissolve
    window auto

    sh "Мужики, можно вас?"

    window hide
    show el normal pioneer at left with dissolve
    window auto

    me "Отмечаем?"

    show sh normal_smile pioneer with dspr

    sh "Спрашиваешь ещё? У меня сын будет! Или дочка!"

    show el serious pioneer with dspr

    el "Только вот чем?"

    show sh smile pioneer with dspr

    sh "Есть у меня одна идея."

    show el laugh pioneer with dspr

    el "Запас на чёрный день?"
    me "А о чём речь-то?"

    show sh normal pioneer with dspr

    sh "Водка. Там полбутылки осталось, мы ей провода протирали раньше."

    show el smile pioneer with dspr

    el "Тогда вечером?"
    me "Возражений не имею."

    scene bg int_dining_hall_day with dissolve

    "За столом уже шутили и вовсю обсуждали эту неожиданность. В беспросветной и смертельно скучной реальности появилось что-то новое, подумать только!"
    "А вообще, я в определённой степени завидовал Сане. Огромная ответственность, трудности — это понятно, но зато наследник уже есть."
    th "Надо будет с Алисой этот момент обсудить. Хотя, конечно, лагерю с двумя беременными будет сложновато."

    stop ambience fadeout 3
    scene bg black with dissolve2
    pause(1)
    play ambience ambience_dining_hall_empty fadein 3
    scene bg int_dining_hall_day with dissolve2

    "После обеда все остались за столом. Вообще, сегодня очередь мыть посуду была на Ольге, но этот вопрос мало кого интересовал."

    window hide
    show sl sad pioneer at cleft with dissolve
    window auto

    sl "Я шла по лесу, нашла небольшую грибницу, чувствую — ветерок свежий, как у водоёма. Ну я и пошла в сторону, дальше от лагеря, деревья пометила."

    show sl scared pioneer with dspr

    sl "Вышла к озерцу небольшому, а там {b}оно{/b}."

    window hide
    show sh serious pioneer at cright with dissolve
    window auto

    sh "Что — {b}оно{/b}?"

    show sl normal pioneer with dspr

    sl "Не знаю, как объяснить.{w} Шаровую молнию видел когда-нибудь?"
    sh "Нет, но представление имею…"
    sl "Вот там похожая штука висит, только, наверное, побольше."

    window hide
    show el serious pioneer at fleft behind sl with dissolve
    window auto

    el "Этого не может быть!"

    window hide
    show mt surprise pioneer behind sh:
        xpos 0.65
    with dissolve
    window auto

    mt "Почему?"

    window hide
    show mz bukal glasses pioneer:
        xpos -0.5 ypos -0.12 rotate 0.0
        ease 0.7 xpos -0.28 rotate 15.0
    pause(0.7)
    window auto
    
    mz "Я читала, это правда. Они, эти молнии, долго не живут."

    show mz bukal glasses pioneer:
        ease 0.7 xpos -0.5 rotate 0.0

    "Неожиданно подала голос Женя."

    hide mz

    sh "Вообще феномен плохо изучен…"
    me "Чёрт с ним. Сань, щас в клубы, химзу на троих возьми, аппаратуру свою тоже тащи."

    window hide
    hide mt with dissolve
    show us normal sport at fright with dissolve
    window auto

    us "А мы?"
    me "А вы пока что тут, вдруг эта хрень опасная?"

    window hide
    hide el with dissolve
    show dv normal pioneer at fleft behind sl with dissolve
    window auto

    dv "Вот именно. Кто вас до медпункта потащит, если с вами что-нибудь случится?"

    window hide
    hide us with dissolve
    window auto

    me "Это не обсуждается. Ждите в лагере. Славь, сколько дотуда?"
    if persistent.easter_egg == True:
        sl "Минут пять десять пятнадцать минут пять десять пятого четыре пять десять пятого утра."
        me "Ладно."
    else:
        sl "Минут пятнадцать."
    dv "Ну нет, дорогой, я с вами, хоть ты тресни."

    show mt normal pioneer:
        xpos 1.0
        ease 0.7 xpos 0.65

    mt "И я!"
    me "Чёрт с вами, пошли все вместе, только держите дистанцию."

    scene black with dissolve2
    stop ambience fadeout 3
    pause(1)
    play ambience ambience_forest_day fadein 3
    scene bg ext_path_day
    show gas_mask
    with dissolve2
    play sound dychanie_w_protivogaze loop fadein 2
    play sound2 tresk_gaygera_norm_protg loop fadein 2

    "Лицо холодной резиной облегал противогаз. Такая же резина на всём теле."
    "Костюмы шили девочки, Лена и Женя, из неудобных плащей ОЗК, которые уже на втором заходе вытащил Шурик из бункера. Получалось удобно и, пожалуй, даже более безопасно, чем в исходниках."
    "Ниток было полно на складе, но иголки нужного калибра, такие, чтобы можно было шить тяжёлую, прорезиненную ткань, нашлись не сразу. Мы пользовались всеми ресурсами бункера, кроме запасов продовольствия, на полную катушку."
    "Шурик надеялся на ядерный реактор, от которого бы питался весь центр и коммуникации, однако на деле всё работало на обычном генераторе, уже частично развалившемся."
    "Из двух нерабочих генераторов технари собрали один, в более-менее трудоспособном состоянии."
    "На спине Шурик нёс не только рюкзак, но и сумку с дозиметром, то и дело бросая косой взгляд на показания прибора."
    "Ощущение, какое-то, поганенькое, будто сзади воронёные стволы пулемётов. Казалось, оно сейчас появилось, да только не так. Осада нашего рая-«Совёнка» идёт ровно с того дня, когда небо прорезал вой ракеты."
    sl "Почти пришли."
    me "Противогазы наде..."
    sh "Не надо пока, дозиметр норму показывает, даже чище, чем в лагере."
    "Перебил меня Саня, с подозрением принюхиваясь."

    window hide
    stop sound fadeout 2
    stop sound2 fadeout 2
    play sound2 gasmask_take_off 
    scene bg ext_path_day with dissolve
    show sh normal hazmat_suit at right with dissolve
    window auto

    me "Сигарету подай."

    show sl angry pioneer with dissolve

    sl "Тьфу, мальчики, опять свою дрянь курите."
    "Шурик передал чуть помятую пачку «Космоса», из запасов бомбоубежища."
    me "Нервишки шалят."

    stop ambience fadeout 4

    sl "Ладно уж… А мы пришли."

    play music "<loop 47>afterglow_remastered/sound/music/day_one.mp3" fadein 3

    window hide
    scene bg black with dissolve
    scene anim_bg ext_polyana_anomaly_day
    show black
    pause(1)
    hide black with dissolve
    window auto
    play sound zvuk_anomalii loop fadein 2

    "Перед глазами была любопытная полянка, посреди которой было небольшое озерцо. В общем-то ничего примечательного, да только над водной гладью повисла…"
    me "Шур, а Шур, это чё такое?"
    "Шурик аж очки протёр, обалдело рассматривая… Шаровую молнию?{w} Над водой повисла какая-то аморфная сфера, испуская ненавязчивое, манящее свечение."
    sh "Антинаучно…"
    me "Так что это?"
    "Электроник рядом чесал затылок, рассматривая образование."
    sl "Мальчики?"
    me "Вообще без понятия."
    "Подошли остальные. Через пару секунд ничего не понимали уже все."
    "А Шурик возьми, да кинь в эту штуку камушек какой-то. "

    play sound2 kamen_anomalia
    pause(1)
    with vpunch

    extend "Образование проглотило камушек, потрещало, как падающее дерево, и тут жахнуло так, что листья с деревьев посыпались. И тишина…"
    "Непонятно что, непонятно как."

    stop sound fadeout 2
    pause(1)
    play sound zvuk_anomalii_ciho loop fadein 2
    window hide
    scene bg ext_polyana_day with dissolve
    show sh surprise hazmat_suit:
        xalign 0.43 xanchor 0.5 yanchor 0.0
    with dissolve
    window auto

    sh "Твою-то! Тьфу."
    "Славя чуть не упала, я выронил сигарету."
    me "Больше не кидай!"

    show sh serious hazmat_suit with dspr

    sh "Это… аномальное образование какое-то."

    window hide
    show dv surprise pioneer at fleft with dissolve
    window auto

    dv "Надо бы на карту нанести, а?"
    "Подала голос моя благоверная."
    me "На карту — это да, это всегда хорошо."

    window hide
    show us surp1 sport at cright with dissolve
    window auto

    us "А выглядит классно-о-о..."
    "Протянула девочка рядом. В рюкзаке Электроника что-то светилось."
    me "Электроник, экий ты балбес, фонарик, что ли, не выключил?"

    window hide
    show el surprise pioneer at fright behind us with dissolve
    window auto

    el "Как… не выключил?"
    "Электроник снял рюкзак, не отрываясь от разглядывания сферы, достал фонарик, потыкал кнопку и так, и так, всё нет, светится."

    show el angry pioneer with dspr

    "Серый психанул, развинтил фонарик, выкрутил лампу. Лампа не гасла."

    show el surprise pioneer with dspr

    dv "Это… как?"
    sh "А вот это я, пожалуй, объяснить могу."
    "Шурик жадно разглядывал аномалию."
    me "Ась?"

    show sh normal hazmat_suit with dspr

    sh "Электромагнитное поле. Видать, сильное. У этой вот штуки."
    "Кибернетик говорил медленно, даже немного растерянно. Он пальцем показал на сферу."

    show dv normal pioneer with dspr

    dv "Во дела... Это что ж творится: сначала ракета, помидоры, прости Господи, эта хрень."

    show el smile pioneer with dspr

    "Электроник вдруг будто подорвался, заулыбался."
    sh "Ты чего?"
    el "Поле, говоришь, так? А аккумулятор так заряжать можно?"
    sh "Ну, пожалуй…"

    show sh normal_smile hazmat_suit with dspr

    extend " Серый, ты гений!"
    "Я ещё не совсем понимал, что учудили наши технари."
    me "А в чём собственно…"
    sh "У нас электричество может быть! Сёмыч, электричество!"

    show el laugh pioneer with dspr

    el "Ну, на то, чтобы лагерь запитать, это вряд ли… Но аккумуляторы, батарейки — это да, это можно."

    show sh normal hazmat_suit with dspr

    sh "Только тут дежурить нужно будет, когда заряжать будем. Да и, в сущности…"
    us "Мы ни черта не знаем о том, что это за штука! Слушай, а переливается как…"
    dv "Только больше мы туда ничего не кидаем."
    me "Ага, вот именно."

    stop sound fadeout 2
    stop music fadeout 4
    scene bg black with dissolve2
    pause(1)
    $ agr_meanwhile("Спустя несколько часов")
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    scene bg ext_no_bus_sunset with dissolve2
    play music hate_life fadein 4
    pause(2)

    "Была у меня одна практически традиция. Каждый день я шёл к клубам, перелезал через забор и выходил на дорогу."
    "Пошарил по карманам, вытащил помятую сигарету."
    "Впереди бесконечная даль. Наша даль. С чего это мы перестали выходить на связь?"
    "Ах, да… Союз, как оказалось, выжил. Сначала все радовались, конечно. Пока через несколько дней не услышали переговоры чьи-то."
    "Всех облучённых расстреливали, больных расстреливали."
    "Будто нацисты, суки в погонах стреляли во всех, кто не мог дать потомство без дефектов."
    "Половина сигареты пеплом разлетелась по ветру. Радиостанция в бункере работала лучше, чем наша, да и рассчитана была на другие дистанции."
    "На западе, вдалеке, показались тучи."

    show dv normal pioneer:
        xalign -0.7
        ease 0.7 xalign 0.28 xanchor 0.5 yanchor 0.0

    dv "Завтра гроза будет."
    me "Шпионила?"

    show dv grin pioneer with dspr

    dv "Талант не пропьёшь."
    me "Было бы чем."

    show dv normal pioneer with dspr

    dv "Чего?"
    me "Было бы чем пропивать."

    show dv smile pioneer with dspr

    dv "Так вон, у вас мальчишник намечается."
    me "А ты откуда?..."
    dv "Мику сказала, а ей Шурик. Очкарик совершенно врать не умеет."
    me "Эх, женщины…"

    show dv angry pioneer with dspr

    dv "Что — женщины?"
    "Начала заводиться Двачевская."

    show blink
    $ karta_otkrytie = False

    "Я потянулся к ней, прикрыл глаза, горячо поцеловал сочные губы, приобнял пониже талии. И эта рыжая хулиганка обомлела, ослабла в моих руках, ноги у неё чуть подкосились, оставив передо мной милую, добрую девушку, без ехидства и злости."
    
    window hide
    pause(4)
    window auto
    
    "Оторвались мы друг от друга нескоро."

    show dv shy pioneer at center
    hide blink
    show unblink

    dv "Что ж ты со мной делаешь, Сёмчик…"
    me "А не видно? Целую."

    show dv guilty pioneer with dspr
    $ karta_otkrytie = True

    dv "Дурак."
    me "Сама ты."
    "Какое-то время мы молча обнимались."
    dv "Люблю тебя безумно."
    me "И я тебя."

    show dv shy pioneer with dspr

    dv "Хочу."
    me "Что?"

    show dv sad pioneer with dspr

    dv "Тебя. Чувствовать, обнимать. Вечность бы так стояла."
    me "Мы свою вечность уже заслужили, солнце."

    stop music fadeout 3

    extend " Пойдём?"

    scene bg black with dissolve
    pause(1)
    play music music_list["heather"] fadein 3
    scene bg int_clubs_male_sunset with dissolve

    "Мы сидели в клубах — я, Серый и Шурик с японкой, сидевшей у него на коленях. Остальные по случаю праздника решили просто дать себе выходной и отдохнуть от работы."
    "Алису я уложил в нашем домике, полежал, подождал пока уснёт, и ушёл к ребятам."

    window hide
    show el laugh pioneer at fleft with dissolve
    window auto

    el "Не, ну это прям неожиданно. Как думаете, мальчик или девочка?"
    "Чуть пьяный кибернетик развалился на табуретке, улыбаясь. Этот, кажется, был рад за всех, чуть ли не больше самого, будущего отца."

    window hide
    show sh serious pioneer at right
    show mi smile pioneer at fright
    with dissolve
    window auto

    sh "Не знаю, но хотелось бы сына."

    show mi happy pioneer with dspr

    "Мику что-то нежно промурлыкала ему на ушко."
    me "А как назовёте?"

    show mi grin pioneer with dspr

    mi "Если мальчик, думаю, Артём. Если девочка — Аней."
    me "Красиво. А не хотели как-нибудь на твоём родном?"

    show mi happy pioneer with dspr

    mi "Не, у вас язык красивый и эти имена мне нравятся."

    show sh normal pioneer with dspr

    "Шурик лишь утвердительно кивнул."

    show el normal pioneer with dspr

    el "Шур, слушай, я понимаю, что праздник, но можно ведь как-то аномалию нашу задействовать, электричество нам вовсе не помешает."
    el "Батарейки в фонариках садятся довольно быстро, а в бункере их не очень много осталось."
    el "Разбить там палатку да подносить к берегу, пока всё не зарядится.{w} И так раз в неделю, да можно про свечи забыть!{w} И жить себе со светом электрическим, как раньше."

    show sh serious pioneer with dspr
    
    sh "Это ты дело говоришь, дружище. Только сегодня, наверное, не…"
    me "Я пойду. Неизвестно, как долго эта штука там будет, а заряженные аккумуляторы нам всегда нужны."

    show sh surprise pioneer
    show mi shocked pioneer
    show el surprise pioneer
    with dspr

    sh "На ночь глядя? Может, хоть до утра подождёшь?"
    me "Послушай, Шур, нельзя упускать такой момент. Собери все батарейки, аккумуляторы и накопители."

    stop music fadeout 3

    extend " Я за палаткой."

    scene bg black with dissolve
    pause(1)
    play music AR_violent fadein 3
    scene bg ext_square_sunset with dissolve

    "Не знаю, с чего во мне проснулся такой героизм, но вот смотрю я на них, на Мику с Шуриком, и понимаю, что есть у нас будущее.{w} А за будущее надо бороться."
    "Палатки лежали на складе."

    scene bg black with dissolve
    pause(1)
    scene bg int_clubs_male2_night_nolight with dissolve
    $ night_time()

    "Пока шёл, пока искал ту, что без дыр, и спальный мешок, за окном смеркалось. На выходе захватил арбалет, сконструированный, кажется, Электроником для Ульяны."
    "Дельная штука, а главное - дешёвая, по сравнению с тем же автоматом: патроны не нужны, болты для этой штуки можно и из мусора собрать."
    
    scene bg ext_square_sunset with dissolve
    $ sunset_time()

    "На душе скреблись кошки, почему-то думалось, что Алиса обязательно будет переживать, когда проснётся. Да и потащиться в дикий лес, в плохо знакомую часть, ночью — затея хреновая."
    "Но отступать уже некуда, эта электрическая хрень вполне может пропасть в любую секунду, как и появилась."
    
    scene bg int_clubs_night with dissolve
    $ persistent.sprite_time = "night"
    $ night_time()

    "Шурик собрал увесистую сумку и строго наказал дольше шести часов не держать аккумуляторы в зоне, где электромагнитное поле. Даже будильник выдал."
    "Напоследок распрощавшись с ребятами и захватив фонарик, я вышел за ворота лагеря."
    
    scene bg ext_camp_entrance_night with dissolve

    th "Так, куда там Славя показывала…"

    $ agr_meet('dv', u"Голос")

    dv "Стой, дурак!"

    $ agr_meet('dv', u"Алиса")

    "Со стороны лагеря ко мне стремительно приближался знакомый силуэт."

    window hide
    show dv angry pioneer2 with dissolve
    window auto

    me "Алис, ты чего?"

    show dv rage pioneer2 with dspr

    dv "С ума сошёл? На ночь глядя! Не пущу!"
    me "А если эта хрень исчезнет?!"

    show dv angry pioneer2 close with dspr

    "Алиса подошла вплотную."
    th "Как только узнала…"
    dv "Ну и пусть! Пусть исчезнет! Не пущу, стой, придурок!"
    me "Алис, ну сама же понимаешь, что надо."
    "Я постарался придать утвердительно-примирительную интонацию голосу."

    show dv normal pioneer2 close with dspr

    dv "Тогда я с тобой!"
    "Прикинув все за и против, я довольно быстро согласился. Какой-то серьёзной опасности сегодняшняя находка не представляла, а вдвоём только веселее."

    stop music fadeout 3
    play ambience ambience_forest_night fadein 3
    scene bg ext_path_night with dissolve2

    "Двигалась Алиса по едва заметной тропинке как-то органично, будто родилась в этом лесу."
    me "Лис, а ты как меня нашла-то вообще?"
    "Девушка какое-то время молчала, потом замедлила шаг."

    window hide
    show dv normal pioneer2 with dissolve
    window auto

    dv "Кот меня разбудил, сволочь мохнатая. Тебя нет, ну решила в клубы сходить, так и нашла."
    me "Эх, Барсик… Ладно."
    "Лес, как и лагерь, жил после конца мира, хотя и местами встречались рыжие проплешины. Шурик что-то рассказывал про то, что они вызваны радиацией, но, благо, близ Совёнка таких не было."
    
    stop ambience fadeout 3
    scene bg black with dissolve
    play music music_list["forest_maiden"] fadein 3
    scene anim_bg ext_polyana_anomaly_night
    show black
    pause(1)
    hide black with dissolve
    play sound zvuk_anomalii_ciho loop fadein 2

    "Мы вышли к озерцу. Свет от аномалии в полумраке сумерек красиво покрывал ближайшие к озеру кусты и траву."
    "Я осторожно выложил груз из сумки, оставив рядом фонарик, пусть заряжается."

    scene bg black with dissolve
    scene bg ext_polyana_night with dissolve

    "Через десять минут мы с Алисой уже разбили палатку, положив на землю какой-то брезент, чтоб не мёрзнуть."
    "Я вытащил из кармана последнюю сигаретку, совсем смятую, прикурил, затянулся, передал Алисе. Та что-то неприязненно пробурчала и мотнула головой."
    me "Чего?"

    window hide
    show dv angry pioneer2 with dissolve
    window auto

    dv "Совсем о будущих детях не думаешь!"
    "Я опешил. Откуда у Двачевской такие мысли могли появиться, было понятно, вон, Мику с Шуриком, но чтобы так резко?"
    me "Алис, милая, послушай…"

    show dv normal pioneer2 with dspr

    dv "Слышать ничего не хочу."
    "Она насупилась, немного комично задрав носик. Но почти сразу сменила тон."

    show dv grin pioneer2 with dspr

    dv "А знаешь что?"

    stop music fadeout 5

    $ karta_otkrytie = False    

    "В голосе девушки появились масляные нотки."
    me "А?"

    stop sound fadeout 2.0
    window hide
    play music music_list["i_dont_blame_you"] fadein 3
    show dv shy_smile booba with dissolve
    window auto

    "Она быстро расстегнула рубашку, под которой, как оказалось, ничего не было.{w} И тут я поплыл."
    "Она отчего-то смущалась, хотя уже сколько вместе живём…"
    "Она покусывала губы и в конце концов одним неловким движением уложила меня на раскрытый, спальный мешок."

    show bg ext_polyana_night:
        ease 0.8 zoom 1.2 ypos 1.15
    show dv shy_smile booba at sit_close

    dv "Ну, чего же ты… снимай."
    me "Да снимаю я, не ори."

    show dv grin booba with dspr

    dv "А я… буду!"

    window hide
    show blink
    $ renpy.pause(1.5, hard=True)
    scene bg semen_i_alisa_palatka
    show prologue_dream
    with dissolve
    window auto

    "Она и орала. Тихо, на ушко. От удовольствия.{w} Этой ночью мы не будем спать, на это нет времени."
    "Все негативные эмоции, что скапливались за день, попросту уходили в такие моменты."
    "Само место, конечно, было не лучшее."
    "В палатке было тесно и холодно, но нас это волновало в последнюю очередь. Мы впервые за долгое время были по-настоящему вместе, были единым целым."

    stop music fadeout 4
    pause(3)
    scene bg ext_polyana_night with dissolve2
    play ambience ambience_forest_night fadein 3
    pause(1)
    $ karta_otkrytie = True

    "Время давно ушло за полночь. Алиска с довольным лицом сидела рядом со мной, закутавшись в спальный мешок."
    "Рядом с палаткой мы нашли пару грибов, подберёзовиков, кажется. Быстро развели костёр, наломали какие-то палочки и стали жарить импровизированный ужин."
    me "Ну что, как тебе грибы?"

    show dv grin pioneer2 with dissolve

    dv "Даже лучше чем в ресторанах."
    "С улыбкой ответила Алиса."

    hide dv with dissolve

    "Вот так сидеть, не переживая ни о чём. Хочется провести вечность с Алиской моей, веселясь и радуясь. Ради этого мы и стараемся."

    show dv shy pioneer with dissolve

    dv "Слушай...{w} А ты не думал о том, чтобы завести детей?"
    "С видом, будто бы облившись красной краской, спросила Алиса."
    th "Что ж сегодня с ней такое, вот точно ситуация с Шуриком повлияла."
    me "Думал. Но сейчас, мы не можем позволить себе этого, иначе будет слишком тяжко."
    dv "А в будущем?..."

    show dv sad pioneer with dspr

    "Тихо, с волнением, спросила она. Было слышно, что девочка моя боится.{w} Боится того, что завтра не наступит."
    me "В будущем - конечно. А пока что ложись и отдыхай."

    show dv smile pioneer with dspr
    pause(1)
    hide dv with dissolve

    "Посмотрев на меня с улыбкой, она свернулась в комочек и легла, головой, ко мне на колени."
    "Она не говорила, только тихо мурчала. Были только мы."

    show blink
    pause(2)
    scene bg alisa_drychnet_v_palatke
    show unblink
    with dissolve

    "Через минут пять, Алиса заснула и я перенёс её в палатку, накрыв одеялом."
    
    scene bg ext_polyana_night with dissolve
    
    extend " А самому спать ещё не хотелось, меня накрыла своего рода меланхолия."
    th "Сколько же всего произошло, сначала бомба, потом Алеся, дальше шахта. Так много пережили, сейчас, вот, Мику беременна.{w} Эх... Завидую я тебе Шурик, в некотором плане."
    th "Ещё и эти сны про какого-то Кира Белого. Кто это? Откуда он в моих снах? Ничего не понимаю. Ещё и похож так на меня..."
    th "Чушь какая-то.{w} Попробую ещё у Виолы спросить, может она чего знает?"
    "Мыслей было много, хотелось всё разложить по полочкам у себя в голове, как-нибудь привыкнуть, да не получается."
    th "Так, точно, будильник. Сколько там осталось... Ага, ещё недолго и будильник бы прозвенел."
    "Отложив вещи на нужное расстояние, я отправился в палатку к Алисе."

    scene bg alisa_drychnet_v_palatke with dissolve

    th "Крепко же ты спишь, рыжая моя. А теперь подвинься, мне тоже спать хочется..."
    
    show blink

    "Впереди нас ждала осень."


    window hide
    scene bg black with dissolve2
    stop ambience fadeout 3
    pause(1)

    jump agr_day_7