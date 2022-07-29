init 1001:
    $ reload_names()
init 2:
    $ music_list["reflection"] = "zhenya/sounds/reflection.mp3"
    $ music_list["just_another_summer_day"] = "zhenya/sounds/just_another_summer_day.mp3"
    $ music_list["free_love"] = "zhenya/sounds/free_love.mp3"
    image red = "#ff0000"
    image blood = "zhenya/images/blood.png"
    image cg zhenya1 = "zhenya/images/zhenya1.jpg"
    image cg zhenya1_smile = "zhenya/images/zhenya1.jpg"
    image cg zhenya1_dontlike = "zhenya/images/zhenya1.jpg"
    image cg zhenya2 = "zhenya/images/zhenya2.jpg"
    image cg zhenya2_hug = "zhenya/images/zhenya2.jpg"
    image cg zhenya3 = "zhenya/images/zhenya3.jpg"
    image pi2 normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "images/sprites/normal/pi/pi_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "images/sprites/normal/pi/pi_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "images/sprites/normal/pi/pi_1_pioneer.png") )
    image pi normal far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), "images/sprites/far/pi/pi_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), "images/sprites/far/pi/pi_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), "images/sprites/far/pi/pi_1_pioneer.png") )
    image pi normal close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "images/sprites/close/pi/pi_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "images/sprites/close/pi/pi_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "images/sprites/close/pi/pi_1_pioneer.png") )
    image pi smile close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), "images/sprites/close/pi/pi_1_pioneer_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), "images/sprites/close/pi/pi_1_pioneer_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), "images/sprites/close/pi/pi_1_pioneer_smile.png") )
    image mz cry_smile pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/mz/mz_3_body.png",(0,0), "zhenya/images/mz_3_crysmile.png",(0,0), "images/sprites/normal/mz/mz_3_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/mz/mz_3_body.png",(0,0), "zhenya/images/mz_3_crysmile.png",(0,0), "images/sprites/normal/mz/mz_3_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "images/sprites/normal/mz/mz_3_body.png",(0,0), "zhenya/images/mz_3_crysmile.png",(0,0), "images/sprites/normal/mz/mz_3_pioneer.png") )
    image mz cry_smile glasses pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/mz/mz_3_body.png",(0,0), "images/sprites/normal/mz/mz_3_glasses.png",(0,0), "zhenya/images/mz_3_crysmile.png",(0,0), "images/sprites/normal/mz/mz_3_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/mz/mz_3_body.png",(0,0), "images/sprites/normal/mz/mz_3_glasses.png",(0,0), "zhenya/images/mz_3_crysmile.png",(0,0), "images/sprites/normal/mz/mz_3_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "images/sprites/normal/mz/mz_3_body.png",(0,0), "images/sprites/normal/mz/mz_3_glasses.png",(0,0), "zhenya/images/mz_3_crysmile.png",(0,0), "images/sprites/normal/mz/mz_3_pioneer.png") )
    image mz irl = "zhenya/images/mz_irl.png"
    image mt shocked panama pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0),  "images/sprites/normal/mt/mt_2_panama.png", (0,0),"images/sprites/normal/mt/mt_2_pioneer.png",(0,0), "images/sprites/normal/mt/mt_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_panama.png",(0,0),"images/sprites/normal/mt/mt_2_pioneer.png",(0,0), "images/sprites/normal/mt/mt_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_panama.png",(0,0),"images/sprites/normal/mt/mt_2_pioneer.png",(0,0), "images/sprites/normal/mt/mt_2_shocked.png") )

    $ colors['pi2'] = {'night': (150, 150, 150, 255), 'sunset': (183, 183, 183, 255), 'day': (183, 183, 183, 255), 'prolog': (183, 183, 183, 255)}
    $ names['pi2'] = translation_new["pi"]
    $ store.names_list.append('pi2')

    $ colors['pi3'] = {'night': (48, 43, 149, 255), 'sunset': (67, 59, 219, 255), 'day': (67, 59, 219, 255), 'prolog': (67, 59, 219, 255)}
    $ names['pi3'] = translation_new["pi"]
    $ store.names_list.append('pi3')

    $ colors['pi4'] = {'night': (225, 221, 125, 255), 'sunset': (225, 221, 125, 255), 'day': (225, 221, 125, 255), 'prolog': (225, 221, 125, 255)}
    $ names['pi4'] = translation_new["pi"]
    $ store.names_list.append('pi4')

    $ colors['uv2'] = {'night': (64, 208, 0, 255), 'sunset': (78, 255, 0, 255), 'day': (78, 255, 0, 255), 'prolog': (78, 255, 0, 255)}
    $ names['uv2'] = translation_new["uv2"]
    $ store.names_list.append('uv2')
init:
    $ mods["zhenya_route"] = translation_new["pioneers_story"]
    $ style.fuckyou = Style(style.default)
    if _preferences.language == "chinese":
        $ style.fuckyou.font  = "fonts/STZHONGS.ttf"
    elif True:
        $ style.fuckyou.font  = "fonts/corbelb.ttf"
    $ style.fuckyou.color = "#ff0000"
    $ style.fuckyou.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.fuckyou.drop_shadow_color = "#000"
    $ style.fuckyou.italic = False
    $ style.fuckyou.bold = True
    image fuckyou = ParameterizedText(style = "fuckyou", size = 150)
    define showFade = ImageDissolve("zhenya/images/memoryfade.png",5,32)
    define dissolveC = MultipleTransition([
        False, Dissolve(2),
        "zhenya/images/memoryfade.png", Fade(1, 0, 3, color="#fff"),
        True])
    define complexdissolve = ComposeTransition(dissolveC, before=showFade)
    image zhenya_anim0:
        contains:
            "bg ext_aidpost_night"
        contains:
            "bg ext_aidpost_night"
            ease 0.2 pos (0, 0)
            ease 0.2 pos (50,50)
            ease 0.2 pos (0, 0)
            ease 0.2 pos (-50,50)
            repeat
        contains:
            "zhenya/images/blink.png"
    image zhenya_anim1:
        contains:
            "bg ext_square_night"
        contains:
            "bg ext_square_night"
            ease 0.2 pos (0, 0)
            ease 0.2 pos (50,50)
            ease 0.2 pos (0, 0)
            ease 0.2 pos (-50,50)
            repeat
        contains:
            "zhenya/images/blink.png"
    image zhenya_anim2:
        contains:
            "bg ext_clubs_night"
        contains:
            "bg ext_clubs_night"
            ease 0.2 pos (0, 0)
            ease 0.2 pos (50,50)
            ease 0.2 pos (0, 0)
            ease 0.2 pos (-50,50)
            repeat
        contains:
            "zhenya/images/blink.png"
    image zhenya_anim3:
        contains:
            "bg ext_camp_entrance_night"
        contains:
            "bg ext_camp_entrance_night"
            ease 0.2 pos (0, 0)
            ease 0.2 pos (50,50)
            ease 0.2 pos (0, 0)
            ease 0.2 pos (-50,50)
            repeat
        contains:
            "zhenya/images/blink.png"
    image zhenya_anim4:
        contains:
            "bg ext_path_night"
        contains:
            "bg ext_path_night"
            ease 0.2 pos (0, 0)
            ease 0.2 pos (50,50)
            ease 0.2 pos (0, 0)
            ease 0.2 pos (-50,50)
            repeat
        contains:
            "zhenya/images/blink.png"
    image zhenya_anim5:
        contains:
            "bg ext_path2_night"
        contains:
            "bg ext_path2_night"
            ease 0.2 pos (0, 0)
            ease 0.2 pos (50,50)
            ease 0.2 pos (0, 0)
            ease 0.2 pos (-50,50)
            repeat
        contains:
            "zhenya/images/blink.png"
    image zhenya_anim6:
        contains:
            "bg ext_polyana_night"
        contains:
            "bg ext_polyana_night"
            ease 0.2 pos (0, 0)
            ease 0.2 pos (50,50)
            ease 0.2 pos (0, 0)
            ease 0.2 pos (-50,50)
            repeat
        contains:
            "zhenya/images/blink.png"
label zhenya_route:

    $ new_chapter(-1, translation_new["DayX"])
    $ prolog_time()
    scene black
    if not ( persistent.endings["main_good"] and persistent.endings["sl_good"] and persistent.endings["dv_good"] and persistent.endings["un_good"] and persistent.endings["us_good"] and persistent.endings["mi"] and persistent.endings["uv_unknown_fucken_shit"] and persistent.endings["uv_city"] ):
        "Возвращайтесь позже..."
        return
    $ renpy.pause(2, hard=True)
    play sound_loop "zhenya/sounds/heavy_breathing.ogg" fadein 2
    $ renpy.pause(3, hard=True)
    scene zhenya_anim0
    with fade
    $ renpy.pause(5, hard=True)
    scene zhenya_anim1
    with fade
    $ renpy.pause(5, hard=True)
    scene zhenya_anim2
    with fade
    $ renpy.pause(5, hard=True)
    scene zhenya_anim3
    with fade
    $ renpy.pause(5, hard=True)
    scene zhenya_anim4
    with fade
    $ renpy.pause(5, hard=True)
    scene zhenya_anim5
    with fade
    $ renpy.pause(5, hard=True)
    scene zhenya_anim6
    with fade
    $ renpy.pause(5, hard=True)
    scene black
    with fade3
    stop sound_loop fadeout 3
    $ renpy.pause(2, hard=True)
    play music music_list["torture"] fadein 3
    $ renpy.pause(2, hard=True)
    scene anim prolog_1
    with fade3
    window show
    "Мой мир пуст, так же как пуст я сам."
    "Я уничтожил себя, чтобы стать целым миром – миром пустоты, который уничтожил меня…"
    "Мне казалось, что в моих руках находятся чьи-то судьбы, в моей власти – оборвать чужие жизни."
    "Но я лишь блуждал в темноте, тщетно прячась от каждого нового тусклого лучика света, каждый из которых лишь рождал пустые тени."
    "Каждая тень – это моё безликое отражение, сгусток кромешной тьмы, единственная цель которого – поглотить меня."
    "Я прятался от них, сливался с ними, они становились мною, а я – ими, и, наконец, уже перестало быть важным, кто из нас по {i}ту{/i} сторону зеркала."
    "…"
    window hide
    with fade
    window show
    "Однако в данном случае это не просто клишированная фраза или какая-нибудь рефлексия доморощенного неудачника."
    "Это – факт."
    "Пусть раньше было не так, пусть раньше миров было много, а мою жизнь можно было назвать жизнью."
    "Ведь всё закончилось в одно мгновение."
    "Сначала этот чёртов автобус – опять он, всюду он! – и толпа таких же, как я, весело улюлюкающих {i}пионеров{/i} вокруг…"
    "А потом ещё и ещё – как яркий калейдоскоп лиц, событий, эмоций и чувств."
    "Но какая уже, к чёрту, разница?!"
    "Ведь если человек умер, то сожалеть он будет о том, что не успел, что не сделал, что не сказал, а не о том, как именно окончился его земной путь."
    "Но разве сейчас я в одном из тех мест, куда попадают души после смерти?.."
    "А ведь всё могло быть иначе!"
    "Неважно, что конец всегда один и тот же, если дорога к нему может быть разной – она зависит от моего выбора."
    "Зависела раньше…"
    "Когда же всё изменилось?"
    "Варианты событий, линии жизни, судьбы людей словно перекрутили вместе несколько раз, а получилось что-то вроде роковой верёвки, на которой только и остаётся что удавиться!"
    "Когда же всё изменилось?.."
    "Уж точно не в один день, не в один час, но точно – так быстро, что я и не успел заметить."
    "…"
    window hide
    $ day_time()
    stop music fadeout 3
    scene black
    with fade3
    pause(3)
    play music music_list["you_lost_me"] fadein 2
    pause(2)
    $ persistent.sprite_time = "day"
    scene bg int_bus
    with flash
    window show
    "В глаза ударили яркие лучи летнего солнца."
    "Летнего – нет, ну кто бы мог подумать, какая неожиданность!"
    "Ведь вчера была зима…{w} Или не вчера?"
    "В бардачке у водителя припрятана пачка сигарет и коробок спичек – я знаю."
    window hide
    scene bg ext_bus
    with flash
    window show
    "От глубокой затяжки закружилась голова, а противный привкус ментола сковал холодком мозг."
    "«Космос», экспортный."
    "Вот ведь умели тогда делать вещи на экспорт – не то что сейчас!"
    "Атомные реакторы, автоматы, сигареты и коммунизм."
    "Много коммунизма – в коробках, ящиках, бандеролях, контейнерах, в трюмах сухогрузов, в грузовых отсеках самолетов, в вагонах поездов, даже в космических кораблях!"
    "Ещё больше коммунизма – пигмеям Африки, индейцам Южной Америки, папуасам Новой Гвинеи…"
    "Ну и пингвинам в Антарктиду можно тоже закинуть посылочку."
    "Тьфу, бред!"
    window hide
    scene bg ext_camp_entrance_day
    with dissolve
    window show
    "Докурив третью сигарету, я уставился на ворота и принялся ждать."
    "Да мне даже часы не нужны – в голове работает безотказный внутренний хронометр."
    "Вот сейчас, ещё немного…"
    stop music fadeout 3
    play ambience ambience_day_countryside_ambience fadein 2
    show sl normal pioneer far at center with dissolve
    "Одна створка противно скрипнула и слегка приоткрылась, оттуда выглянула девочка в пионерской форме, осмотрелась по сторонам и заметила меня."
    show sl surprise pioneer at center with dissolve
    "Подойдя, она потянула носом тяжёлый раскалённый воздух и как будто слегка удивилась, но тут же улыбнулась и заговорила:"
    slp "Привет, ты, должно быть, нове…"
    window hide
    if _preferences.language == None:
        $ fuckyoutext = "Да пошла ты на ...!"
    elif _preferences.language == "spanish":
        $ fuckyoutext = "¡Vete a la mierda!"
    elif _preferences.language == "italian":
        $ fuckyoutext = "Va' a farti fottere!"
    elif _preferences.language == "chinese":
        $ fuckyoutext = "滚！"
    elif True:
        $ fuckyoutext = "Go ... yourself!"
    show fuckyou fuckyoutext:
        align (0.5, 0.5)
        zoom 0.8
        linear 1.0 zoom 1.0
    play sound sfx_scary_sting
    with vpunch
    with hpunch
    pause(1)
    hide fuckyou with dissolve
    show sl scared pioneer at center with dspr
    window show
    "Заорал я, встал и, игнорируя её, направился в лагерь."
    window hide
    stop ambience fadeout 5
    scene bg ext_clubs_day
    with dissolve
    play ambience ambience_camp_center_day fadein 5
    window show
    "Когда-то это было смешно, потом – забавно, теперь же это просто привычка."
    "Глупая такая, но навязчивая – как класть разные вещи в разные карманы."
    "Вот я, например, не могу носить телефон в правом кармане, потому что…"
    "А чёрт его знает почему!"
    "Вот и тут так же: с утра обидел девочку – день начинается неплохо!"
    window hide
    scene bg ext_houses_day
    show dv normal pioneer2 at center
    with dissolve
    window show
    "По дороге мне повстречалась ещё одна пионерка."
    show dv scared pioneer2 at center with dspr
    "Точнее, она попыталась ударить меня по спине, но я вовремя отскочил и посмотрел на неё так, что у бедной девочки внезапно, похоже, появились более срочные дела."
    window hide
    stop ambience fadeout 2
    scene bg ext_house_of_mt_day
    with dissolve
    window show
    "Домик вожатой утопал в кусте сирени…{w} Когда же он уже утонет наконец, мать его!"
    window hide
    scene bg int_house_of_mt_day
    show mt normal pioneer far at center
    with dissolve
    play sound sfx_open_door_kick
    play music music_list["afterword"] fadein 3
    window show
    "Громкий хлопок двери отвлек хозяйку от чтения какой-то книжки."
    "Нет, мне правда никогда не было интересно, что читает вожатая."
    show mt surprise pioneer at center with dissolve
    "Не раздеваясь, я плюхнулся на кровать, а ноги в зимних ботинках закинул на спинку."
    show mt angry pioneer at center with dspr
    mtp "Ты что себе позволяешь?! И кто ты вообще такой?!"
    "Искренне возмутилась вожатая."
    pi "Закрой рот, женщина."
    "Лениво бросил я."
    show mt shocked pioneer at center with dspr
    "Она остолбенела, не в силах вымолвить и слова."
    "Так всегда бывает – каждый чёртов раз."
    pi "Вот скажи мне лучше – почему ты до сих пор себе мужика не нашла? Тебе сколько – двадцать пять? Двадцать пять с чем-то? В таком возрасте уже пора понимать, что к чему!"
    "На секунду наступило молчание."
    pi "Не знаешь? А я тебе скажу – да кому ты такая вообще сдалась?!"
    "Домик вожатой огласился громким смехом, скорее даже лошадиным ржанием, а за окном весело бубнила знакомая мелодия."
    "Я пару раз пытался найти, откуда играет обеденная музыка, чтобы вместо неё из динамиков по всему лагерю запустить что-нибудь более или менее ободряющее."
    "Но не нашёл – похоже, это ангельское пение не нуждается в проигрывателе, проводах или электроэнергии."
    "Ну и чёрт с ним…"
    "Сейчас я бы, например, не отказался, чтобы весь этот «Совёнок» услышал мой смех, услышал, как я смеюсь… смеюсь…"
    "Но только вот над кем?"
    "Но ведь не над собой, нет!"
    "Я просто смеюсь, потому что смех – это отличная защитная реакция, а также способ развеять скуку."
    "Минута смеха прибавляет сколько? Пять минут жизни?"
    "Ну мне-то ни к чему – я де-факто бессмертен, осталось только нотариально заверить."
    show mt angry pioneer at center with dspr
    mtp "Как ты разговариваешь со старшими?!"
    pi "Оленька, дорогая, ну смени пластинку уже, а? Ей-богу, надоело одно и то же из раза в раз слушать! Давай попробуем вот так: «Привет, как у тебя дела?» Видишь, не так сложно? Давай, теперь ты!"
    show mt surprise pioneer at center with dspr
    mtp "Что?.."
    pi "Не {i}что{/i}, а «Привет, как у тебя дела?»"
    pi "А я тебе отвечу: «Спасибо, плохо, как всегда». А может, даже добавляю: «Вашими молитвами!»"
    show mt rage pioneer at center with dspr
    mtp "Убирайся отсюда! Я сейчас милицию вызову!"
    pi "Как? По голубиной почте? Телефон же не работает."
    show mt surprise pioneer at center with dspr
    mtp "Да, но… я…"
    "Замялась вожатая."
    pi "Хотя…"
    "Я полез в карман – в левый, – достал мобильник и кинул ей."
    pi "Попробуй вот."
    "Вожатая поймала телефон, он несколько раз подпрыгнул у неё в руках и чуть не полетел на пол."
    mtp "Что… это?"
    pi "Телефон."
    "Коротко ответил я и закрыл глаза."
    pi "Знаешь, такой: «Зазвонил телефон, кто говорит? Слон»."
    show mt angry pioneer at center with dspr
    mtp "Ты что, больной?"
    "Вожатая наконец, похоже, начала приходить в себя."
    pi "А ты?"
    mtp "Я не знаю, что здесь проис…"
    pi "Ты смотрела когда-нибудь фильм «День сурка»? Не смотрела. Ну и ладно. Если бы у вас в библиотеке были книги по психиатрии, на твой вопрос о моём психическом состоянии я бы смог ответить с большей уверенностью. Поэтому сейчас готов сказать лишь как дилетант – да, Оленька, я больной!"
    "И опять громкий, дьявольский смех."
    show mt surprise pioneer at center with dspr
    "Вожатая от неожиданности выпустила телефон из рук, он упал на ребро и отскочил ко мне."
    "Я быстро подобрал мобильник и сунул в карман."
    pi "Но не тобою."
    "Добавил я, открыв один глаз."
    window hide
    play sound sfx_knock_door7_polite
    pause(1)
    play sound sfx_open_door_1
    show un normal pioneer far behind mt at right with dissolve
    window show
    "В дверь робко постучали, затем она открылась, и на пороге появилась пионерка…"
    pi "Ух ты ж, твою мать!"
    "Наигранно вскочил я с кровати."
    pi "А тесак где, дома забыла?"
    show un surprise pioneer far behind mt at right with dspr
    "Пионерка непонимающе посмотрела на вожатую."
    show mt normal pioneer at center with dspr
    mtp "Это…"
    "Начала она, вздохнула и тяжело опустилась на кровать напротив."
    "На самом деле я знал, что вожатая меня не боится – страх у неё просто в программу не заложен."
    "Она может возмущаться – это да, сколько угодно; имитировать испуг – всенепременно!"
    "Но пройдёт пара минут, и она самоустранится, оставив меня в покое."
    "Тоже мне…{w} Вот я бы на её месте!.."
    unp "Я, наверное, не вовремя…"
    "Робко пролепетала пионерка, потупив взгляд и собираясь уходить."
    pi "Да ты не стесняйся!"
    "Радушно воскликнул я, жестом показывая на место рядом с собой."
    pi "Ты присаживайся, чувствуй себя как дома!"
    unp "Нет, я…"
    pi "Присаживайся, кому сказано!"
    show un scared pioneer far behind mt at right with dspr
    "Рявкнул я."
    "Вот эта девочка точно умеет сыграть и настоящий испуг, и страх, и даже ужас."
    show un scared pioneer at right with dissolve
    "Она медленно подошла и села на мою кровать, вжавшись в спинку."
    pi "Ну, что хорошего расскажешь?.."
    stop music fadeout 3
    "…"
    window hide
    scene anim prolog_1
    with complexdissolve
    pause(1)
    play music music_list["just_another_summer_day"] fadein 3
    window show
    "Меня, как и всякого порядочного ребёнка, родители с детства учили, что нельзя открывать дверь незнакомым людям."
    "Также не стоит идти непонятно куда, когда тебя зовёт непонятно кто."
    "Но то – в детстве…"
    "А сейчас от того, доверюсь я незнакомцу или нет, зависит буквально всё!"
    "Казалось, что прошла уже целая жизнь, и я успел состариться, если не физически, то духовно."
    "И забыл, что такое зима, снег, холод, вечерняя темнота, пронизывающий до костей ветер и вечная слякоть."
    "Так и город, не останавливающийся ни на минуту, вечно куда-то бегущий и коптящий грязное небо и людей рядами прогнивших дымоходов и автомобильных труб, остался далеко в прошлом, словно на выцветших страницах старого фотоальбома, за ненадобностью заброшенного в пыльный чулан."
    window hide
    show cg zhenya1
    with flash2
    window show
    mz "Эй!"
    "Голос сидящей рядом девочки несколько отвлёк меня от этих мыслей."
    mz "Опять завис? Всё думаешь об {i}этом{/i}?"
    me "О чём?"
    "Она говорила беззлобно, и я переспросил скорее просто для порядка – ответ был и так известен."
    mz "Ты знаешь."
    "Мы сидели на крыше библиотеки, свесив ноги вниз."
    "Женя немного откинулась назад, её волосы красиво развевались на ветру."
    "В глаза нам било яркое солнце, заставляя жмуриться, но оно не было ослепляющим – скорее бархатно-тёплым – и словно обволакивало всего тебя приятным жаром летнего дня."
    me "Нет…{w} То есть я не знаю. Наверное.{w} Последнее время не всегда получается понять, о чём думаешь. В голове – каша из мыслей."
    "Я замолчал на мгновение и посмотрел на Женю."
    "Она выглядела так, как будто её не интересует не только наш разговор, но и вообще всё происходящее вокруг."
    "Словно бы эту девочку всё устраивает – лето, солнце, приятный ветерок, молодость…"
    "Словно этого ей достаточно для счастья, а остальное – лишь глупые условности."
    me "Короче, ты меня понимаешь! Зачем вообще спрашивать?"
    show cg zhenya1_smile with dspr
    mz "Потому что человек – существо социальное, ему положено общаться с себе подобными."
    "Она еле заметно усмехнулась."
    me "Ну да, кто бы говорил! Сейчас, подожди, схожу за наградой самой общительной пионерке 1980-какого-то там года."
    mz "А я что? У меня, в отличие от некоторых, есть в этом лагере вполне конкретные обязанности! Я уважаемый член нашего коллектива, незаменимый даже в каком-то роде! Не то что ты!"
    "Женя сверкнула глазами и ехидно ухмыльнулась."
    me "Ну да, обязанности…"
    "Я прикрыл глаза ладонью и откинулся на спину."
    me "Нет, ты сама себе слышишь? Обязанности у неё! Коллектива…"
    show cg zhenya1_dontlike with dspr
    mz "Эй!"
    "Грозно сказала Женя и больно ткнула меня в живот."
    me "Ох."
    "Скорее наигранно застонал я и бросил в её сторону гневный взгляд."
    me "А если бы я упал? Разбился? А?"
    show cg zhenya1 with dspr
    mz "Это было бы крайне прискорбно!"
    me "Тут даже жизнь застраховать негде!"
    mz "Ну да, и страховку выплачивать потом тоже будет некому."
    me "Ну как некому…"
    "Я почесал затылок, глупо ухмыльнулся и сказал:"
    me "А тебе?"
    mz "Мне…"
    "Женя задумалась."
    mz "Ну, допустим, но не думаю, что в столовой принимают доллары, евро, кредитные карты или на худой конец российские рубли. Да и обменника здесь наверняка нет. А если бы и был, то еще неизвестно, как там дела с курсом. Я, знаешь ли, не хочу страдать от его скачков!"
    me "Проси выплат в золоте!"
    show cg zhenya1_smile with dspr
    mz "В золоте ему!"
    "Она навалилась на меня, и попыталась то ли защекотать, то ли задавить, то ли побить, то ли всё вместе."
    stop music fadeout 3
    "…"
    window hide
    scene bg ext_house_of_mt_day
    with complexdissolve
    play ambience ambience_camp_center_day fadein 5
    window show
    "Я вышел из домика вожатой посмеиваясь."
    "Вряд ли стоило чего-то ждать от разговора с этой пионеркой."
    "Я и не ждал, зачем?"
    "Ведь всё уже давно известно – эту пьесу мне по силам сыграть самостоятельно, как в убогом театре одного актера."
    "Какая ирония – пьеса одного актера в театре одного зрителя в городе одного жителя в мире одного человека во вселенной одного живого существа?"
    "Или «живого» – в кавычках? Или, может, {i}живого{/i} – курсивом? Какой некролог вам больше нравится? С виньетками или без? С буквицей или без? Какой шрифт желаете? Бумага матовая или глянцевая?"
    "Тьфу, опять!.."
    window hide
    scene bg ext_houses_day
    show us laugh sport far at center
    with dissolve
    window show
    "По дороге вприпрыжку скакала весёлая девочка."
    "Может быть, в этот раз начать с неё?"
    "Помню, в столовой есть отличные крюки для мяса…"
    "Или нет?.."
    show us surp1 sport at center with dissolve
    usp "А ты кто?"
    "Выпалила она, поравнявшись со мной."
    pi "Я – ужас, летящий на крыльях ночи! Бу!"
    "Я демонстративно развёл руки в стороны и навис над ней."
    show us laugh2 sport at center with dspr
    usp "И совсем не страшно."
    pi "Не страшно? Ну это пока…"
    "Ухмыльнулся я и направился дальше."
    show us surp2 sport far at center with dissolve
    usp "Эй!"
    "Кричала она мне вслед."
    show us surp1 sport at center with dissolve
    usp "Подожди."
    "Девочка догнала меня и схватила за руку."
    stop ambience fadeout 3
    pi "Не трогай!"
    window hide
    show us cry sport with dspr:
        xalign 0.5
        ease 1.0 xalign 2.0
    pause(0.2)
    play sound sfx_bush_body_fall
    window show
    "Брезгливо заорал я и с силой одёрнул руку так, что юная пионерка слетела с дорожки и упала в кусты."
    show us cry2 sport with dspr:
        xalign 2.0
        ease 1.0 xalign 0.5
    pause(0.2)
    play music music_list["dance_of_fireflies"] fadein 3
    usp "Ай, больно же!"
    "Заплакала она."
    "Странно.{w} Вот сейчас – правда странно."
    "Кажется, такого раньше не было."
    "Конечно, этот день повторялся уже столько раз, что и не сосчитать..."
    "И ведь дело совсем не в том, что девочка улетела в кусты, а в том, что здесь не должно быть {b}ничего{/b} нового!"
    "Даже такое малозначительное, казалось бы, событие может в итоге оказаться важнее, чем все предыдущие {i}разы{/i}!{w} Чем первый {i}раз{/i}!"
    "Не знаю даже почему – просто чувствую, просто уж слишком давно не случалось {b}ничего{/b} нового!"
    "Конечно, этот мир нельзя сравнить с монотонным механизмом, бездушно выполняющим свою работу, но все вариации сценария мне знакомы!"
    "И когда я говорю {i}все{/i}, я имею в ввиду {b}все{/b}!"
    "Пару минут назад в домик к вожатой могла прийти не та застенчивая пионерка, а девочка, встретившая меня у ворот лагеря, – и я бы был готов."
    "Или наглая пионерка, приветствующая незнакомцев ударом по спине, – и я бы был готов."
    "Или даже вот эта мелка плакса – и я бы всё равно был готов…"
    "Но сейчас, в этот самый момент, происходит то, к чему я не готов!"
    "А не готов я в первую очередь к неожиданностям!"
    "Девочка продолжала плакать и смотрела на меня глазами, полными гнева и обиды."
    usp "Это ты! Это всё ты!"
    pi "Да ладно, чего ревёшь…"
    "Я неуверенно подошёл к ней и подал руку."
    show us sad sport at center with dspr
    "Девочка на секунду сделала недоумённое лицо, но затем схватилась за меня и рывком поднялась на ноги."
    show us dontlike sport at center with dspr
    usp "Стыдно небось стало? А вот то-то и оно – маленьких обижать нельзя!"
    pi "Стыдно?"
    "Переспросил я, мыслями находясь далеко отсюда."
    pi "Перед кем? Перед тобой? С какой стати?"
    show us angry sport at center with dspr
    usp "А должно быть!"
    hide us with dissolve
    "Насупилась она и побежала в сторону домика вожатой."
    "Может быть, жаловаться – я не знал."
    "Действительно не знал!"
    "Впервые за долгое, очень долгое время произошло что-то подобное!"
    "Ещё пару минут назад я мог с уверенностью сказать, чем занят каждый пионер в данный конкретный момент.{w} А что теперь?"
    "Тьфу!.."
    stop music fadeout 3
    "…"
    window hide
    scene bg int_dining_hall_people_day
    with dissolve
    play ambience ambience_dining_hall_full fadein 3
    window show
    "За обедом ко мне подошла вожатая."
    show mt normal pioneer at center with dissolve
    mtp "Неудобно получилось…"
    "Начала она, собравшись с мыслями."
    mtp "Мне твои родители позвонили и…"
    show mt angry pioneer at center with dspr
    mtp "Но ты бы мог вести себя поприличнее! Представиться для начала хотя бы!"
    "Переменившись в лице, продолжила она."
    show mt smile pioneer at center with dspr
    mtp "Но ничего, мы сделаем из тебя образцового пионера."
    "Раньше я бы ей в подробностях рассказал и о пионерах, и об образцовости, но сейчас просто не было никакого желания разговаривать – ни с ней, ни с кем бы то ни было еще."
    show mt normal pioneer at center with dspr
    mtp "Ну да ладно. Для начала тебе надо познакомиться с товарищами."
    show mi normal pioneer at left
    show mz normal glasses pioneer at right
    with dissolve
    "Вожатая махнула рукой, приглашая кого-то к столу, и к нам подошли две девочки."
    mtp "Ну, приятного вам аппетита, а у меня ещё дела."
    hide mt with dissolve
    "Неуверенно сказала она и оставила пионерок наедине со мной."
    show mi smile pioneer at left
    mip "Привет, а ты новенький, да? Любишь музыку? Вступай к нам в музыкальный кружок! Я там, правда, пока одна, но с тобой нас будет двое, весело, как думаешь?"
    "Я не смотрел на неё и продолжал сосредоточенно есть."
    mzp "Да отстань от него – не видишь, он какой-то дурной."
    "Если первая девочка была просто туповата, то вторую я бы сравнил с той угрюмой кошкой из интернета."
    "А что если?.."
    "Ведь я раньше никогда такого не делал – просто в голову не приходило."
    "Ну, а раз будущие события теперь мне неизвестны, то почему бы не попробовать?"
    window hide
    stop ambience fadeout 0
    play sound sfx_throw_compote
    pause(0.7)
    show mz rage glasses pioneer at right
    show mi shocked pioneer at left
    play music music_list["pile"] fadein 3
    window show
    "Я молча встал, схватил стакан с компотом и вылил его второй пионерке на голову."
    pi "Приятного аппетита."
    hide mi
    hide mz
    with dissolve
    "Каменным голосом подытожил я этот акт вандализма и направился к выходу из столовой."
    "Девочка кричала, визжала, хрипела и даже как-то надрывно стонала, но не пыталась меня остановить."
    "Сейчас больше всего хотелось оказаться в другом месте – посмотреть на мир со стороны, понаблюдать за страданиями других с высоты своего опыта."
    "Но тех мест с сегодняшнего дня больше нет."
    show sl angry pioneer at center with dissolve
    "В дверях я столкнулся с той первой девочкой, встретившей меня у ворот, попытался обойти её, но…"
    window hide
    play sound sfx_face_slap
    with hpunch
    pause(1)
    window show
    "Получил хлёсткую пощёчину."
    "Звук мгновенно разлетелся по столовой, эхом застыв под потолком."
    "Вмиг наступила полная тишина."
    "Рука в долю секунды сжалась в кулак, ногти до крови впились в ладонь, кожа на костяшках натянулась буквально до разрыва…"
    "Я уже намеревался отправить эту тварь в нокаут…"
    show us angry sport at center with dissolve
    "Может быть, мне не хватило доли секунды – между нами словно из-под земли выросла та маленькая пионерка, которую я кинул в кусты, и развела руки в стороны, своим маленьким тельцем защищая подругу."
    "И на этом всё кончилось…"
    hide us
    hide sl
    with dissolve
    stop music fadeout 2
    "Я безвольно разжал руку, опустил голову, протиснулся между ними и вышел из столовой."
    window hide
    scene bg ext_dining_hall_near_day
    with dissolve
    play ambience ambience_camp_center_day fadein 3
    window show
    "Неужели они оказались сильнее меня?"
    "Почему вообще такое произошло?{w} Ведь раньше я бы…"
    "Да почему «бы» – ведь столько раз меня ничего не останавливало."
    "Что там – ударить девочку!{w} Я делал вещи и пострашнее."
    "Похоже, этот мир изменился, не поставив меня в известность!"
    "…"
    window hide
    scene bg ext_square_day
    with dissolve
    play sound "zhenya/sounds/smoking.ogg"
    window show
    "Колечки сигаретного дыма медленно летели в сторону Генды."
    "Пачка уже почти опустела, а больше курево здесь достать негде – придётся ждать ещё неделю…"
    "Само собой можно сходить к братьям-аутистам, взять бутылку водки и напиться – только что это изменит?"
    "Такие простые раньше и такие сложные сейчас решения…"
    "Тьфу, неужели я уже начал рассуждать как тот чёртов неудачник?!{w} Да никогда! "
    show dv normal pioneer2 at center with dissolve
    dvp "А ещё не найдется?"
    "Ко мне подсела очередная пионерка."
    pi "Чего?"
    "Непонимающе спросил я."
    "Она показала на сигарету."
    pi "Курить – здоровью вредить!"
    show dv grin pioneer2 at center with dspr
    dvp "Кто бы говорил."
    "Усмехнулась она."
    pi "А у меня оно резиновое. Хочешь проверить?"
    show dv smile pioneer2 at center with dspr
    dvp "Не надо, верю на слово."
    "Я протянул ей сигарету и дал прикурить."
    show dv shocked pioneer2 at center with dspr
    dvp "А круто ты сегодня… ну…"
    "Закашлявшись, сказала она."
    show dv smile pioneer2 at center with dspr
    dvp "И вожатую в её домике – я слышала. И на обеде. Теперь я хоть не главный позор лагеря!"
    "Я пристально посмотрел на неё."
    "Пионерка неумело курила сигарету и улыбалась так самодовольно, как будто весь мир уже признал её правоту."
    pi "А ты, я смотрю, только о себе и думаешь."
    show dv surprise pioneer2 at center with dspr
    dvp "Что? О чём ты? Я… нет…"
    "Переменилась она в лице, даже немного запаниковала и подавилась дымом."
    pi "Но ты права. Самой плохой тут ты точно никогда не была. Вот насчёт себя я не уверен."
    show dv normal pioneer2 at center with dspr
    dvp "Ты так говоришь… Так… Ну… Круто!"
    "Вот ещё мне не хватало похвалы от неё."
    stop ambience fadeout 3
    "Или, может быть?.."
    play music music_list["heather"] fadein 3
    pi "Слушай…"
    "Улыбнувшись одной из своих заученных улыбок, начал я."
    pi "А не хочешь заодно и обмыть знакомство, так сказать?"
    show dv smile pioneer2 at center with dspr
    dvp "А у тебя есть?"
    "Сверкнула глазами пионерка."
    pi "Для хорошего человека – всегда найдётся!"
    stop music fadeout 3
    "…"
    window hide
    scene anim prolog_1
    with complexdissolve
    pause(1)
    play music music_list["just_another_summer_day"] fadein 3
    window show
    "Впрочем, начиналось всё – как в плохом романе, печатающемся по главам в бульварной газетёнке – совсем не так."
    "Воспоминания слились в сплошное марево красно-оранжевого оттенка, как дорога из жёлтого кирпича, ведущая в Изумрудный город."
    "Только вот Элли подросла и зарабатывает на жизнь проституцией, потому что вместо того, чтобы усердно учиться, витала в фантазиях о волшебной стране."
    "Трусливый лев подсел на мет и был застрелен в перестрелке с полицией."
    "Вот Железному Дровосеку жилось неплохо – он стал наёмным убийцей."
    "А Страшила и вовсе не изменился, устроившись на стабильную, низкооплачиваемую работу в офис с удобным графиком с 9 до 6 и отсутствием перспектив карьерного роста."
    "Наверное, и не было никогда впереди никакого города."
    "Бесконечная дорога, без цели и смысла."
    "Ведь тогда {i}он{/i} действительно говорил о чём-то подобном, по крайней мере пытался предупредить – я не слушал и в итоге единственный из всех застрял в этой чёртовой ленте Мёбиуса."
    window hide
    show cg zhenya1_dontlike
    with flash2
    window show
    "Она сидела рядом и недовольно хмурилась."
    mz "Эй! Приём, приём, вызывает Земля!"
    me "Ладно, что такого-то? Уже и подумать как будто нельзя!"
    mz "Мысли должны приводить к какому-то результату, а у тебя что?"
    me "А у меня что?"
    mz "Отсутствие результата!"
    me "Отсутствие результата тоже результат!"
    "Женя больно ущипнула меня за плечо и отодвинулась на метр."
    stop music fadeout 3
    "…"
    window hide
    scene anim prolog_1
    with complexdissolve
    pause(1)
    window show
    "А потом появилась {i}она{/i}."
    "Нет, Женя… Жени всегда были в «Совёнке», но мою Женю я увидел тогда впервые."
    "Может быть, я плохо помню то, что было до и что было после, но те несколько дней останутся у меня в памяти навсегда!"
    "…"
    window hide
    scene bg ext_dining_hall_away_day
    with dissolve
    play ambience ambience_camp_center_day fadein 5
    window show
    "Я уже чётко осознал, что это не мой застывший мир, понимал, что спустя бесконечность времени мне вновь, как когда-то, удалось провалиться в другой."
    "Удалось случайно – словно пересеклись на миг орбиты двух далёких планет, а у меня было всего мгновение."
    "Опоздай я на секунду – и они разлетелись бы навсегда, с бешеной скоростью удаляясь друг от друга."
    "Этот мир так же одинок и пуст, как и предыдущий."
    "Но главное в нём – что он не такой, он новый!"
    "И здесь есть вещи, мне не знакомые."
    "О, это действительно важно, для меня это так важно!"
    "Например, Женя, сидящая не в библиотеке, а на крыльце столовой."
    "После всего случившегося я просто был не способен на сарказм."
    window hide
    scene bg ext_dining_hall_near_day
    show mz normal glasses pioneer at center
    with dissolve
    window show
    pi "Привет."
    "Сказал я, подойдя поближе, но всё же остановившись на безопасном расстоянии."
    show mz bukal glasses pioneer at center with dspr
    "Женя подняла на меня глаза, по её лицу было видно, что она не ожидала здесь кого-то встретить."
    mzp "Привет…"
    "Да и голос её звучал не как обычно – уж интонации нашей библиотекарши я бы ни с чем не спутал!"
    me "Решила на обед пораньше?"
    mzp "Нет… Не знаю… А во сколько обед?"
    "Скороговоркой ответила она."
    me "Как это «во сколько обед»?"
    "Её ответ поверг меня в ступор, и я расплылся в глупой улыбке, но по всему телу пробежал холодок."
    mzp "А, нет, извини, я знаю, конечно, во сколько обед, просто… ну…"
    "Женя окончательно запуталась и уставилась себе под ноги."
    "Казалось, что ей сейчас меньше всего хотелось находиться здесь, но уйти не хватало решимости."
    "Это было странно, но совсем не пугало – наоборот, я был рад, ведь наконец-то случилось что-то новое, выходящее за рамки шаблона!"
    pi "С тобой всё в порядке?"
    "Задал я самый глупый вопрос, который только можно было задать в такой ситуации."
    "И что только ожидал услышать в ответ?"
    show mz shy glasses pioneer at center with dspr
    mz "Да, спасибо."
    me "За что?"
    mz "Не знаю. Ну, за то, что беспокоишься."
    me "Да я прост…"
    show mz bukal glasses pioneer at center with dspr
    "На её лице промелькнули нотки недовольства, но тут же исчезли, и Женя медленно встала."
    show mz normal glasses pioneer at center with dspr
    mz "Мне пора."
    me "Подожди, но ты же на обед собиралась…"
    mz "Попозже приду, у меня ещё дела."
    me "Ладно…"
    hide mz with dissolve
    "Я не стал её останавливать, но решил проследить."
    "Бог знает, как давно со мной не случалось ничего подобного!"
    "Может быть, только в первые разы здесь…"
    window hide
    scene bg ext_square_day
    with dissolve
    window show
    "Женя вышла на площадь и быстро направилась в сторону библиотеки."
    "Всю дорогу она не оборачивалась, поэтому мне даже не приходилось особо скрываться."
    window hide
    scene bg ext_library_day
    with dissolve
    window show
    "Когда за ней захлопнулась дверь, я застыл в нерешительности."
    "А что дальше? Постучаться и зайти? Но что ей сказать?"
    "Тут не надо быть детективом, чтобы понять, что я за ней следил."
    show el normal pioneer at center with dissolve
    "Из раздумий меня вывел Электроник, возникший передо мной словно из-под земли."
    elp "Что, с обходным пришёл?"
    pi "А? Да, вот решил зайти в библиотеку."
    show el smile pioneer at center with dspr
    elp "Понятно, не буду тебя отвлекать."
    "Сказал он и уже собирался уходить."
    pi "Подожди.{w} А тебе не показалось, что Женя последнее время ну… несколько странно себя ведёт, что ли?"
    show el serious pioneer at center with dspr
    "Электроник внимательно, даже оценивающе, посмотрел на меня и нахмурил брови."
    elp "Что-то случилось?"
    me "Нет, ничего…"
    "Выглядело так, как будто я оправдываюсь, и тут же меня охватило мерзкое чувство собственной ничтожности – с какой стати мне перед ним оправдываться!"
    pi "Просто спрашиваю! Что, спросить уже нельзя?!"
    show el surprise pioneer at center with dspr
    elp "Да нет, можно, конечно…"
    "Испуганно ответил он."
    show el normal pioneer at center with dspr
    elp "Может быть, действительно немного странно.{w} Пожалуй, что-то такое я замечал последние пару дней."
    pi "Вот как? И в чём эти странности выражались?"
    elp "Не знаю, просто она обычно более уверена в себе, что ли. Думаешь, нам стоит с ней поговорить?"
    "Я уже было хотел ответить «тебе-то точно не стоит», но сдержался."
    pi "Ладно, забудь. Может, настроение такое."
    elp "Какое?"
    pi "Никакое! Такое – догадайся, ты же у нас будущий учёный!"
    "Резко ответил я."
    show el serious pioneer at center with dspr
    "Электроник на секунду задумался – словно о судьбах мира, – а затем понимающе кивнул."
    show el normal pioneer at center with dspr
    elp "Ладно."
    "Я слегка развел руками в стороны и наклонил голову, показывая, что, если у него ко мне больше нет дел, то стоит вернуться к постройке роботов и стоит это сделать как можно скорее."
    "Конечно, он был несколько медленноват, но сейчас понял меня с первого раза."
    hide el with dissolve
    stop ambience fadeout 3
    play music music_list["just_think"] fadein 3
    "Когда Электроник ушёл, я сел, прислонившись спиной к дереву рядом с библиотекой, так, чтобы меня не было видно из окон, и задумался."
    "Точнее, я попытался задуматься, потому что для всеобъемлющего логического анализа ситуации катастрофически не хватало фактов."
    "Когда обои в вашей комнате из белых превращаются в чёрные, можно удивиться, испугаться, предположить, что их перекрасили без вашего ведома, разозлиться на тех, кто это сделал…"
    "Но всё это – эмоции."
    "Фактом в данной ситуации послужила бы записка, лежащая на столе и сообщающая что-то вроде «дорогой, я подумала, что к вечности лучше подготовиться заранее, поэтому сменила тон интерьера на более подходящий»."
    "А что я имел на руках в тот момент: огромное количество однообразных витков – позади, странное поведение библиотекарши – сейчас и неизвестность – впереди."
    "Не больно-то основательная база для построения каких-либо теорий."
    "О, а уж в теориях я был мастер! Впрочем, всё это осталось в прошлом, потому что с какого-то момента стало уже абсолютно наплевать, почему мне суждено провести вечность именно в этом лагере."
    "Тьфу, опять!"
    "И что бы я там ни решил, всё это – не я!"
    "Я так не думаю и, наверное, никогда не думал."
    "Словно кто-то вложил мне в голову чужие мысли. Попав в чужой мир, я перестал быть собой?"
    "Трава предательски шуршала под ногами, выдавая моё присутствие – я пробирался к окнам библиотеки, намереваясь узнать, что творится внутри."
    "Женя сидела за столом, уставившись куда-то перед собой."
    "Даже без книги – пронеслось в голове."
    "Она выглядела растерянно, возможно обреченно, как человек, которому сообщили, что жить ему осталось несколько часов."
    "Вот бы ей сказать, что всё в порядке и через пять дней всё повторится опять, а потом опять…"
    "Да и как такое вообще может быть {i}в порядке{/i}?"
    "Словно сообщить больному, что он умрёт через пять дней, но не должен волноваться, ведь ещё через семь дней он умрёт снова!"
    window hide
    with fade
    window show
    "Прошло, наверное, минут десять, а Женя не сдвинулась с места, иногда мне даже казалось, что она не дышит."
    "Вот теперь я уже точно начал понимать, что это не просто странно, это – {i}оно{/i}! То, что закинуло меня в этот новый мир!"
    "Предстояло только решить, с чего начать."
    "Можно попробовать спросить в лоб, рассказать свою историю…"
    stop music fadeout 0
    play ambience ambience_camp_center_day fadein 2
    show mt angry panama pioneer at center with dissolve
    mtp "А, вот ты где!"
    "Позади меня стояла вожатая."
    "Я резко обернулся и раздражённо сказал:"
    pi "Тебе чего?"
    "Как обычно, как привык."
    mtp "Что ты тут крутишься? Забыл, что в библиотеке тебе тоже надо подпись поставить?"
    "Вожатая, казалось, не обратила внимания на мои слова и тон."
    "Не как обычно, а как когда-то давно."
    "С воспоминаниями о моём попадании в этот лагерь вернулись и забытые образы местных обитателей – которых я тогда ещё считал людьми, а не просто декорациями."
    pi "Да вот, понимаете…"
    mtp "Ничего и знать не хочу – чтобы до ужина всё подписал!"
    pi "Конечно, я как раз собирался зайти…"
    mtp "Ну так и иди!"
    stop ambience fadeout 3
    "Ольга Дмитриевна проводила меня взглядом до двери, так что выбирать, что делать дальше, и не пришлось – {i}помогла{/i} вожатая."
    window hide
    scene bg int_library_day
    with dissolve
    play ambience ambience_library_day fadein 3
    window show
    "В библиотеке пахло книжной пылью, старой советской мебелью и немного – сыростью."
    "Женя сидела, не обращая на меня никакого внимания, и только когда я закрыл за собой дверь, словно бы пришла в себя."
    show mz bukal glasses pioneer at center with dissolve
    pi "Привет ещё раз."
    "Неуверенно начал я."
    "В конце концов, привыкнув к определённой модели поведения и взаимодействия с обитателями лагеря, перестраиваться мне было достаточно тяжело."
    "А тут ещё эта вожатая не дала подготовиться!{w} Задушить бы её панамкой, как обычно!"
    "Женя не отвечала, но смотрела на меня с опаской."
    pi "А я тут обходной пришёл подписать…"
    show mz normal glasses pioneer at center with dspr
    mzp "Хорошо, давай."
    "Безэмоционально ответила она."
    "Я начал рыться в карманах и тут понял…"
    "Нет, точно со мной творится что-то не то!"
    "За столько времени я бы уже должен был привыкнуть ко всему, а веду себя как первоклассник!{w} Точнее, как {i}первосменник{/i} – в терминах этого мира."
    pi "Кажется, потерял…"
    "Сказал я, для вида сделав расстроенное лицо."
    mzp "Плохо."
    "Всё так же сухо и без интереса ответила она."
    "Я застыл в некоей суперпозиции – если сейчас развернусь и уйду, то… то что?"
    "Но в тот момент непонятно откуда взялась решимость."
    pi "Можно тебе вопрос задать?"
    show mz bukal glasses pioneer at center with dspr
    mzp "Какой?"
    "И ведь действительно – какой?"
    "«Тебе не кажется, что в столовой последнее время недосаливают еду?», «Ночи нынче какие-то холодные, не находишь?», «А кстати, ты в курсе, что я пришелец из будущего?»…"
    pi "С тобой всё в порядке? В последнее время мне кажется, ты чем-то расстроена."
    show mz normal glasses pioneer at center with dspr
    "На лице Жени промелькнула заинтересованность."
    mzp "Но мы с тобой не знакомы."
    pi "Да, конечно, просто… Я тебя вчера видел и подумал…"
    "Я завирался всё больше."
    "Неспособность сказать правду всё дальше вгоняла меня в аутизм и всё сильнее сокращала словарный запас."
    mzp "Я тоже видела, как ты вчера бегал по лагерю, но мы ведь не знакомы."
    pi "Нет, не знакомы, но мне… Славя про тебя рассказывала, да! Вы же с ней соседки?"
    show mz bukal glasses pioneer at center with dspr
    mzp "И что она рассказывала?"
    "Понемногу Женя начала выходить из своего созерцательного состояния."
    pi "Ничего."
    "Я обреченно вздохнул и тяжело опустился на стул рядом с дверью."
    "За окном мерно распевали свои песни разноголосые птицы, стрекотали сверчки, где-то лилась вода, а издалека доносился задорный детский смех."
    "Но это всё было там – за стенами библиотеки, внутри которой нас только двое, я и Женя – точнее, та девочка, которая выглядит как Женя."
    "Страха нет, скорее – удивление."
    pi "Давай предположим, что я – это не я."
    mzp "А кто же тогда ты?"
    "Мне на секунду даже стало обидно, что она не знает, кто такой я."
    "Ну как же, я! А, это тот я, тот самый? Да-да, вот этот парень!"
    "О моих подвигах слагали легенды пионеры многих миров!"
    "Но именно этой конкретной Жене в этом конкретном мире было, похоже, совершенно наплевать, кто я и что я здесь делаю, а наш разговор, который уже, кажется, начинал ее интересовать, вновь превратился в бесполезную болтовню."
    pi "А на кого похож?"
    "Женя окинула меня беглым взглядом."
    show mz normal glasses pioneer at center with dspr
    mzp "На пионера?"
    pi "Ну да, на пионера, логично, отличная шутка!"
    "Натужно ухмыльнулся я."
    mzp "Я не шутила."
    pi "Просто я похож на себя, а вот ты – нет."
    mzp "Не похожа на тебя?"
    pi "На себя ты не похожа, господи!"
    "Началось финальное наступление."
    show mz bukal glasses pioneer at center with dspr
    mzp "В каком смысле?"
    "Удивилась она."
    pi "В том смысле, что ты не Женя! Нет, то есть ты не местная библиотекарша!"
    mzp "А кто я тогда?"
    "Она отвела взгляд, словно ища что-то на книжных полках."
    pi "Не знаю, поэтому и спрашиваю."
    mzp "Если это опять какая-то шутка…"
    pi "Шутка?"
    show mz shy glasses pioneer at center with dspr
    mzp "Ну ты же знаешь, все уже знают…"
    "Она смутилась и покраснела."
    pi "Нет, не знаю."
    mzp "С кнопкой на стуле… Я отошла за книгой, а пока искала, Алиса…"
    "Женя уставилось в пол, а я заметил, что у неё на глаза навернулись слёзы."
    pi "Нет, я про такое не слышал."
    "Хотя, если подумать, то что-то подобное было в прошлые разы – Алиса решила прикольнуться."
    "Просто тогда я не обратил на это совершенно никакого внимания."
    "Да и Женя отреагировала, кажется, по-другому."
    "Алиса…"
    stop ambience fadeout 2
    "…"
    window hide
    $ persistent.sprite_time = "night"
    $ night_time()
    scene bg int_clubs_male2_night
    show dv scared pioneer2 at center
    with complexdissolve
    pause(1)
    play music music_list["door_to_nightmare"] fadein 3
    window show
    dvp "Отстань от меня!"
    "Еле ворочая языком, мямлила пионерка, застёгивая рубашку."
    "Кружок кибернетики купался в ярком лунном свете, на столе валялась пустая бутылка, вокруг которой аккуратным круглым пятном разлилось небольшое водочное озеро."
    "Щека слегка горела, а голова кружилась так сильно, что уже и не понять, от чего именно – но вряд ли только от алкоголя."
    dvp "Если ты подумал, что я такая, то хрен тебе!"
    "Пальцы не слушались девочку, пуговица скакала туда-сюда, но никак не хотела вставать на положенное место."
    pi "Дааа?"
    show dv shocked pioneer2 at center with dspr
    "Я вышел из себя, схватил пионерку за руки, прижал спиной к столу и зубами разорвал её рубашку."
    pi "А какая? А, какая, я тебя спрашиваю? Это не риторический вопрос – отвечай!"
    "Я не хотел ничего менять, меня всё устраивало!"
    "Я жил привычной жизнью в привычном мире, делал, что хотел!"
    "На черта мне сдалась эта новизна?!"
    pi "Ты же хочешь, я знаю! Пойти хлестать водку с незнакомым человеком после пяти минут знакомства! Не такая она! В гробу я вас всех видал! Верните всё как было!"
    "Я терял контроль над собой, над ситуацией, над миром, наконец…"
    dvp "Отпусти, мне больно!"
    "Кричала девочка."
    show dv cry pioneer2 at center with dspr
    "Но я крепко держал её и через минуту она обмякла и закрыла глаза, из которых изредка капали горячие солёные слёзы."
    pi "Вот видишь, так гораздо лучше."
    "Я грубо лапал её везде, при этом часто и громко дыша."
    pi "Потому что ты – моя! Вы все тут – мои! Весь этот мир – мой!"
    "Но девочка не сопротивлялась, и мне вдруг стало не интересно, даже противно."
    pi "Да и не нужна ты мне – тут есть и получше!"
    scene bg int_clubs_male2_night:
        ease 1.5 zoom 1.1
        linear 1.5 zoom 1.0
    show dv cry pioneer2 at center
    "Я отпустил её и обессиленно сполз на пол."
    "Пионерка же не сдвинулась с места, лишь продолжала тихо всхлипывать."
    pi "Да я могу тут любую! Слышишь, любую! А потом возьму топор для разделки мяса и… Думаешь, такого раньше не было?"
    "Кричал я."
    pi "Думаете, думаете, вы можете мне указывать?! Это мой мир, слышите, мой! Да вас вообще не существует! Я разговариваю сам с собой!"
    pi "Хватит ныть!"
    "Я окончательно вышел из себя, вскочил и навалился на пионерку всем телом."
    "Кажется, она уже была близка к обмороку."
    "Я наклонился и прошептал ей на ухо:"
    pi "А знаешь, что я с тобой делал? Столько раз… Хочешь послушать? Нет, ты уж послушай, я расскажу!"
    "Внезапно у меня начался приступ паники."
    "С самого {i}начала{/i} прошло бесконечно много времени, но каждую секунду я «жил», осознавал себя как личность, управлял ситуацией, этим – а раньше еще и многими другими – миром."
    "И впервые появилось чувство, что я исчезаю, пройдёт мгновение – и меня не станет!"
    "Как это так – ведь это Я, разве вы не видите? Разве вы не помните?.."
    show dv normal pioneer2 at center with dspr
    dvp "Ты тряпка…"
    "Словно из другого мира донёсся шёпот девочки."
    dvp "Жалкая тряпка, ничтожество. Мне бы было тебя жаль, но нельзя жалеть пустое место."
    "Я в ужасе отскочил от неё."
    show dv angry pioneer2 at center with dspr
    "На лице пионерки застыла гримаса презрения, слёзы исчезли, словно их и не было."
    show dv angry pioneer2 close at center with dissolve
    "Она встала со стола, сделала пару шагов в мою сторону и остановилась."
    stop music fadeout 3
    "…"
    window hide
    $ day_time()
    scene cg zhenya2
    with complexdissolve
    pause(1)
    play music music_list["just_another_summer_day"] fadein 3
    window show
    mz "И зачем ты мне всё это рассказываешь?"
    "Лениво спросила Женя, перелистнув страницу."
    "По воде бежала мелкая рябь, над нами тихо колыхались листья берёзы, сквозь которые били яркие лучи томящего полуденного солнца."
    "В роще громко пели птицы, а у меня по ногам деловито прыгали букашки, скрываясь в высокой траве."
    pi "А зачем ты читаешь эту книгу? Только не говори мне, что в первый раз!"
    mz "Нравится. Тебе вот нравится рассказывать, а мне нравится читать."
    "На другом берегу, на пляже, резвились пионеры, Ольга Дмитриевна бегала за Ульянкой, а на середине реки я разглядел золотистую голову Слави.{w} Неужели она плывёт сюда?"
    mz "Ну и?"
    pi "Что?"
    mz "Что было дальше?"
    pi "Так тебе же не интересно."
    mz "Зато тебе интересно."
    "Женя улыбнулась."
    stop music fadeout 3
    "…"
    window hide
    $ night_time()
    scene bg int_clubs_male2_night
    with complexdissolve
    pause(1)
    play music music_list["sunny_day"] fadein 3
    play sound sfx_close_door_campus_1
    window show
    "Она плюнула мне в лицо и вышла на улицу, громко хлопнув дверью."
    "А я остался стоять."
    "Что, вот он – конец?"
    "Когда-то я ждал его, может быть даже с нетерпением."
    "Но это было давно, так давно, что уже и не помню…"
    "А что теперь?"
    "Эти куклы, бездушные куклы разрушили мой мир, который я строил всю жизнь?..{w} Вот так просто – всего за один день?.."
    "Я провёл рукой по щеке – на пальцах осталось что-то мокрое."
    "…"
    window hide
    with fade
    window show
    "На лагерь уже давно опустилась ночь, спрятав под своим покровом местных пионеров, спрятав их злобу и коварство."
    "А я просто сидел на полу в кружке кибернетики, обхватив колени руками, и медленно покачивался из стороны в сторону."
    "Может быть, та пионерка сейчас вернётся, ведь она могла унизить меня куда сильнее.{w} Или даже сделать что похуже…"
    "Однако время шло, и лишь тише становилось пение ночных птиц да трескотня сверчков."
    "А ведь скоро рассвет, тогда лагерь проснётся, и заживёт своей жизнью, внезапно ставшей для меня неизвестной."
    "Ну и ладно, ну и пусть…"
    "Я с трудом поднялся на ноги и посмотрел на пустую бутылку водки, лежащую на столе."
    "Вот бы сейчас отключиться, а завтра проснуться как ни в чем не бывало, забыв сегодняшний день, оказаться в одном из привычных миров, где поведение пионеров знакомо и предсказуемо!"
    "А ведь всё началось с той маленькой девочки…"
    "Раньше она никогда не плакала."
    "А может, и плакала, а я просто не обращал внимания?"
    "Даже если так, то что – становиться тряпкой, жалеть эту малявку, опускаться до {i}их{/i} уровня, наконец?!"
    stop music fadeout 3
    "Нет, надо взять себя в руки!"
    window hide
    scene bg ext_clubs_night
    with dissolve
    play ambience ambience_camp_center_night fadein 3
    window show
    "Я вышел из клуба кибернетики, громко хлопнув дверью, и полной грудью вдохнул свежий ночной воздух."
    "Странно, сейчас он не казался таким искусственным, как обычно."
    "Куда же пойти?"
    "Пожалуй, стоит догнать ту пионерку и отомстить за плевок в лицо!"
    "Я никогда раньше не простил бы такое оскорбление – не прощу и сейчас!"
    window hide
    scene bg ext_square_night
    with dissolve
    window show
    "На площади не было ни одной живой души, кроме пионера, сидевшего на лавочке."
    "Сначала я не обратил на него внимания – мало ли тут всяких придурков? – но он окликнул меня:"
    stop ambience fadeout 3
    play music music_list["orchid"] fadein 3
    show pi normal far at center with dissolve
    pi2 "Эй, Семён!"
    "Какой я тебе Семён, мать твою!{w} Зашипел я себе под нос."
    "Но пионер не унимался:"
    pi2 "Ты, наверное, ищешь кого-то? Так она не туда пошла."
    show pi normal at center with dissolve
    "Я замер, но тут же развернулся и быстро подошёл к нему."
    pi "Так ты её видел?"
    show pi smile at center with dspr
    pi2 "Конечно видел!"
    "На его лице появилась мерзкая улыбка, даже скорее оскал, звериный, выражающий лишь превосходство над противником."
    pi "Ну так говори, мы же тут с тобой не в угадайку играем!"
    pi2 "Да подожди ты, куда разогнался? Ты присядь, поговорим сначала спокойно."
    pi "Не о чем мне с тобой говорить."
    show pi normal at center with dspr
    "Пионер на секунду задумался, затем порылся в карманах шорт, достал оттуда пачку «Космоса» и протянул мне."
    pi2 "Будешь?"
    pi "Это… откуда у тебя?"
    "Не помню, чтобы раньше у простых пионеров водились сигареты!"
    "Впрочем, за последние сутки случилось много такого, чего не происходило раньше…"
    "Я медленно вытянул одну сигарету и отдал пачку странному пионеру."
    "Он повертел её в руках некоторое время и бросил мне обратно."
    show pi smile at center with dspr
    pi2 "Да не, бери, я бросил."
    "И опять эта мерзкая ухмылка!"
    "Хотя плевать на неё – надо поймать наглую девку!"
    pi "Ну так? Говори, куда она пошла!"
    pi2 "А зачем тебе эта несчастная девочка? В масштабах Вселенной она ничтожно мала, а в этой Вселенной, возможно, и вовсе не существует."
    show pi normal at center with dspr
    "Он задумался, а потом продолжил."
    pi2 "Как и тебя. Ты уверен, что ты – существуешь? А даже если так, то ты уверен, что твоё существование здесь и сейчас – настоящее? Может быть, раньше ты действительно существовал, а сейчас нет?"
    pi2 "Или будешь существовать потом, а передо мной лишь кукла?"
    "Слово «кукла» больно стрельнуло у меня в голове, как будто кольт сорок пятого калибра вышиб мозги, разбрызгав всё содержимое черепной коробки по площади."
    "Ну да, а Славе завтра убирать…{w} Невольно усмехнулся я про себя."
    pi "Ты кто?"
    "Наглая девчонка, плюнувшая мне в лицо, давно вылетела из головы вместе с мозгами."
    pi "Ты кто, тебя спрашиваю!"
    show pi normal close at center with dissolve
    "Я схватил его за галстук и дёрнул на себя с такой силой, что чёртова красная тряпка затрещала и чуть не порвалась."
    show pi smile close at center with dspr
    "Однако пионер лишь ухмыльнулся."
    pi2 "Спокойно, не надо так волноваться. Ведь здесь нельзя умереть – ты знаешь, ты делал это сотни раз."
    show pi smile at center with dissolve
    "Я в ужасе отшатнулся от него."
    "Эта фраза…{w} Я точно слышал её раньше!"
    "Нет, даже не так – я сам её говорил!"
    "Когда-то давно, в прошлой… в одной из прошлых жизней."
    pi2 "Потому что ты Семён.{w} И я Семён. Потому что ты – это я."
    scene anim prolog_1
    show bg ext_square_night:
        parallel:
            linear 1.0 zoom 0.5
        parallel:
            linear 1.0 align (0.5, 0.5)
    show pi smile at center:
        parallel:
            linear 1.0 zoom 0.5
        parallel:
            linear 1.0 align (0.5, 0.5)
    "Лавочка и пионер резко отдалились от меня на сотню метров, как будто я падал вниз с американских горок, лишь его мерзкий оскал стоял перед глазами."
    window hide
    scene black
    with fade2
    window show
    "А затем мир вокруг накрыла тьма…"
    stop music fadeout 3
    "…"
    window hide
    $ day_time()
    scene cg zhenya2
    with complexdissolve
    pause(1)
    play music music_list["just_another_summer_day"] fadein 3
    window show
    me "Ну и потом я исчез."
    mz "Так просто?"
    "Женя не отрывала глаз от книги, но история, казалось, начала её интересовать."
    me "А что сложного? Вовремя уйти – большое искусство, знаешь ли, а я в нём уж точно мастер!"
    mz "Ага, ты во всём мастер…"
    show cg zhenya2_hug with dspr
    "Она отложила книгу и обняла меня."
    "Славя, явно плывущая в нашу сторону, похоже, заметила это и развернулась в сторону пляжа."
    me "Подожди! Я ведь ещё до самого главного не дошёл!"
    me "Да и не здесь, в конце-то концов…"
    "Я смущённо отвернулся от неё."
    show cg zhenya2 with dspr
    "Это явно не понравилось Жене, и она отстранилась от меня."
    mz "Надоели твои истории – постоянно одно и то же! Дай-ка я лучше свою расскажу."
    me "Ну и про что же, интересно?"
    mz "Да вот хоть про то, как я сюда попала!"
    me "Слыхал уже сто раз."
    mz "Ну да, а я твои – двести!"
    "..."
    window hide
    with fade
    window show
    "Для Жени «Совёнок» не начался с нашего знакомства и обходного листа."
    "Ведь у меня всегда был, есть и будет {i}мой{/i} первый день смены, а для неё прошло уже несколько недель, проведённых в лагере."
    mz "Ты знаешь это чувство, когда время остановилось? Когда нельзя умереть, хоть и хочется?"
    me "Ну да. Как здесь, в этом лагере?"
    mz "Нет, здесь мне всегда было даже проще. Люди ведут себя честно, правильно, никто ни над кем не издевается по-настоящему, нет, в конце концов, той злобы, которая была везде тогда, {i}раньше{/i}, ты помнишь?"
    "Я промолчал."
    mz "Я могу просто читать книги, просто общаться с людьми, я кому-то нужна, кто-то меня считает другом, у меня есть обязанности…"
    "Мне казалось, что Женя готова расплакаться."
    mz "Ну ладно, что это я… Короче, однажды я просто проснулась от тряски в автобусе 410-го маршрута, ты на нём когда-нибудь ездил?"
    "Я кивнул."
    mz "А я вот никогда, у нас в городе вообще трёхзначных номеров маршрутов нет."
    mz "Ещё толком не поняла, что произошло, а девочка, сидящая рядом, мне и говорит: «Привет, меня Славя зовут»."
    mz "Славя? Какая Славя? Кого славим?.."
    mz "Я, конечно, растерялась, но виду старалась не подавать. Потом приехали в лагерь, и всё закружилось-завертелось…"
    me "А потом опять…"
    mz "А потом опять…"
    "Вздохнула Женя."
    mz "И тебя я видела много раз. Как ты со Славей, с Алисой, с Леной…"
    "Она еле слышно скрипнула зубами."
    me "Ну так ведь это был не я! Сто раз уже говорили, а ты опять по новой!"
    mz "Ты, не ты… Да все вы на одно лицо! «Я» же тоже была в {i}твоих{/i} лагерях? Но ведь совсем не такая, как я настоящая!"
    me "Вот именно! Отличить подделку от оригинала не так сложно, как ты думаешь!"
    mz "Да, потому что подделки каждый раз обновляются, а оригиналы остаются."
    me "Всё не совсем так…"
    mz "Как будто ты всё знаешь!"
    me "Да какая разница!"
    show cg zhenya2 with dspr
    "Я крепко обнял Женю и закрыл глаза."
    stop music fadeout 3
    "..."
    window hide
    $ persistent.sprite_time = "day"
    $ day_time()
    scene bg ext_square_day
    with complexdissolve
    pause(1)
    play ambience ambience_camp_center_day fadein 3
    window show
    "Я очнулся весь в поту, сердце бешено стучало."
    "Восходящее солнце пекло невыносимо, хотя, судя по всему, было не больше шести-семи утра."
    "Что за чертовщина со мной произошла?{w} Зловещий пионер – что это было?"
    "Может быть, просто сон, галлюцинация?"
    "Сейчас я готов поверить и в это…{w} Да вообще во что угодно!"
    "Кто-то медленно шёл по площади в мою сторону."
    show mt normal panama pioneer far at center with dissolve
    "Я пригляделся и узнал вожатую."
    show mt angry panama pioneer close at center with dissolve
    mtp "Значит, ты опять за своё?"
    "Грозно сказала она, нависнув надо мной."
    show mt angry panama pioneer at center with dissolve
    "Пришлось встать с лавочки и отойти на шаг."
    mtp "Я уже думала, что вчерашний случай – просто случайность, а ты… У меня просто нет слов! Чтобы с девочкой вот так поступить!"
    "О чём она вообще?"
    "Какая девочка, что ей от меня нужно, чёрт возьми?!"
    "По крайней мере вожатая выглядела как обычно, и это меня немного успокоило."
    show mt rage panama pioneer at center with dspr
    mtp "Отвечай, чего молчишь! Думаешь, в этот раз удастся так просто отделаться? Да я в милицию позвоню, да я до секретаря всесоюзной комсомольской организации дойду!"
    "Она так пыхтела, что даже покраснела и начала задыхаться."
    mtp "Чтобы в моём лагере! Да я! Да я тебя!"
    "В принципе, такое поведение вожатой меня ничуть не удивило."
    "Однако мне было не по себе, потому что в памяти всё ещё всплывали события прошлой ночи, оставляя после себя гнетущее, болезненное ощущение сродни стыду за совершенное в хмельном угаре."
    "Самое странное, что мне было наплевать на вожатую, надрывающуюся всего лишь в метре от меня."
    pi "Помолчи уже, а! Орёшь как на пожаре! Что ты вообще знаешь о проблемах?! Думаешь, у тебя тут проблема? Ай-яй-яй, пионерку чуть не изнасиловали, беда-беда."
    show mt shocked panama pioneer at center with dspr
    "Я скрипнул зубами и грозно посмотрел на вожатую, отчего у неё на лице промелькнул испуг."
    pi "Хочешь, я тебе расскажу что такое настоящие {i}проблемы{/i}?! Не в твоём выдуманном мирке!"
    pi "Хотя ну тебя! Только время терять!"
    "Впрочем, этого самого времени у меня всегда предостаточно…"
    "В голове вдруг стрельнула страшная мысль: а что если теперь всё всегда будет {i}так{/i}?.."
    "Что если я навсегда потеряю контроль над этим миром?"
    "Любая пионерка сможет безнаказанно плевать мне в лицо, а вожатая – отчитывать, словно я какой-то Электроник?.."
    "Ведь это хуже смерти!"
    pi "Ладно, мне пора…"
    stop ambience fadeout 3
    "Бросил я ещё не отошедшей от шока вожатой и направился куда глаза глядят."
    window hide
    scene bg ext_path_day
    with dissolve
    play ambience ambience_forest_day fadein 3
    window show
    "А ведь действительно – что такое смерть лично для меня?"
    "Кажется, я давно перестал понимать саму концепцию этого понятия."
    "Ведь если я не могу исчезнуть, если мне предстоит вновь и вновь проживать одну и ту же неделю в этом чёртовом лагере, может быть, смерть – это потеря себя?"
    "Потеря власти над миром, неизвестность впереди?"
    "Так ведь это ещё хуже судьбы любого {i}обычного{/i} человека!"
    "Их жизнь – это игра с невесёлой концовкой, без возможности сохранений."
    "Моя жизнь – это игра без концовки, с возможностью сохранений…"
    "Как бы {i}они{/i} назвали такую жизнь?.."
    "Если бы просто вспомнить – каково это быть обычным человеком…"
    "Наверное, они бы назвали это адом!"
    "А данный конкретный цикл, где меня унижают даже бездушные куклы, – это его последний круг."
    "Я готов был сойти с ума, если бы мог."
    "Все те мысли, что я так тщательно отгонял от себя, вдруг нахлынули с новой силой, появились давно забытые чувства."
    "И кто в итоге оказался прав?"
    "Я всегда убеждал себя, что прав я, а не {i}они{/i}, потому что я – жив, а все {i}они{/i} исчезли, погнавшись за пустыми иллюзиями."
    "Но так ведь {i}они{/i} – исчезли, а я – остался."
    "И кому в итоге лучше?.."
    stop ambience fadeout 3
    play music music_list["faceless"] fadein 3
    pi2 "Хе-хе."
    "Рядом раздался уже знакомый смешок."
    show pi smile at center with dissolve
    pi2 "Похоже, сегодня ты кое-что понял!"
    pi "Я знаю, кто ты."
    "Мой голос звучал спокойно, но сердце бешено стучало, так, как никогда прежде."
    pi2 "О, правда? Интересно послушать."
    pi "Ты такой же, как я, пионер из другого цикла!"
    pi2 "Но ты же всегда думал, что {i}других{/i} не осталось, после того как Семён уехал на автобусе в {i}тот{/i} раз? Ты думал, что теперь ты один во всех этих бесконечных лагерях!"
    pi "Я мог ошибаться…"
    "Как бы сложно ни было мне это признавать, такая возможность существовала."
    pi2 "Ты? Ошибаться! Да ну, не может такого быть!"
    pi "Короче, что тебе надо, просто пришёл поиздеваться, как я делал раньше?"
    pi2 "Ты это так говоришь…{w} Как будто чувствуешь себя виноватым."
    pi "Я не чувствую себя виноватым, и в любом случае это не твоё дело! Просто ответь на вопрос."
    pi2 "Ну, может, ты и прав…"
    show pi normal at center with dspr
    "Пионер на секунду задумался."
    pi2 "Хотя грешно над убогими смеяться!"
    "Мне вдруг отчётливо захотелось сбить эту мерзкую ухмылку с его лица!"
    "В конце концов, тварь я дрожащая или право имею?!"
    "Кто {i}ему{/i} позволил наводить свои порядки в моём мире?!"
    pi "Убирайся!"
    window hide
    hide pi with dissolve
    with hpunch
    play sound sfx_bodyfall_1
    scene bg ext_path_day:
        parallel:
            ease 0.5 zoom 1.1
            ease 0.5 zoom 1.0
        parallel:
            ease 0.5 align (0.1,0.1)
            ease 0.5 align (0,0)
    pause(0.5)
    window show
    "Заорал я, вскочил и что есть силы махнул кулаком в его сторону…"
    "Однако рука пролетела сквозь дымку, растворившуюся в воздухе, а я, потеряв равновесие, больно упал на землю."
    stop music fadeout 3
    "…"
    window hide
    play ambience ambience_forest_day fadein 3
    with fade
    window show
    "Когда боль слегка отступила, почудилось, что кто-то стоит рядом."
    show us laugh sport far at center with dissolve
    "И действительно, из кустов выглядывала маленькая нахальная пионерка."
    usp "Так тебе и надо!"
    "Она показала мне язык."
    usp "Со своими сверстниками небось не такой смелый!"
    pi "Да ты…"
    "От неожиданности я даже забыл, что хотел сказать."
    pi "А тебя вообще не удивляет, что на твоих глазах человек просто растворился в воздухе?"
    usp "Ну…{w} Всякое бывает. Может, это фокус какой-то! Да и какая разница? Главное, что ты своё получил!"
    show us laugh2 sport far at center with dissolve
    "Больше эти оскорбления я был сносить не намерен, резко вскочил и бросился к ней."
    window hide
    scene bg ext_path2_day
    with dissolve
    window show
    "Однако девочка ловко бежала между деревьями, в то время как мне приходилось тратить драгоценные секунды на то чтобы уклоняться от хлещущих по лицу веток, торчащих кочек и невидимых овражков."
    window hide
    stop ambience fadeout 3
    scene bg ext_square_day
    show us cry sport at center
    with dissolve
    play music music_list["scarytale"] fadein 3
    window show
    "Набив пару шишек и расцарапав в кровь руки, я всё-таки догнал её на площади."
    pi "Ну что, всё-таки не такая ты быстрая? Это тебе не от всяких полудурков бегать!"
    usp "Отпусти! Отстань!"
    "Плакала пионерка."
    window hide
    play sound "zhenya/sounds/punch.ogg"
    scene bg ext_square_day
    show blood
    with flash_red
    pause(1)
    play sound sfx_bodyfall_1
    window show
    "Вдруг я почувствовал сильный удар в спину, перед глазами всё поплыло, а земля начала приближаться с огромной скоростью."
    window hide
    play sound "zhenya/sounds/punch.ogg"
    scene bg ext_square_day
    show blood
    with flash_red
    pause(1)
    window show
    dvp "Так ты и малолетками не брезгуешь?"
    window hide
    play sound "zhenya/sounds/punch.ogg"
    scene bg ext_square_day
    show blood
    with flash_red
    pause(1)
    window show
    slp "Так его, так!"
    window hide
    play sound "zhenya/sounds/punch.ogg"
    scene bg ext_square_day
    show blood
    with flash_red
    pause(1)
    window show
    "Удар в живот…"
    "Я инстинктивно закрыл голову руками."
    window hide
    play sound "zhenya/sounds/punch.ogg"
    scene bg ext_square_day
    show blood
    with flash_red
    pause(1)
    window show
    mip "Теперь не такой крутой?!"
    window hide
    play sound "zhenya/sounds/punch.ogg"
    scene red
    with flash_red
    pause(1)
    window show
    "Ещё удар…"
    "Я уже был готов потерять сознание, но собрал последние силы в кулак, приподнялся на локтях и откатился на несколько метров в сторону."
    "Кровь заливала глаза, поэтому толпа пионеров, избивающих меня, слилась в сплошное красное марево."
    mtp "Это, конечно, не самый лучший способ воспитания, но, думаю, вполне действенный."
    "Непонятно откуда донёсся ехидный голос вожатой."
    pi "Что вы делаете?! Хватит…"
    stop music fadeout 3
    "..."
    window hide
    scene cg zhenya1
    with complexdissolve
    pause(1)
    play music music_list["just_another_summer_day"] fadein 3
    window show
    mz "Ты читал Дон Кихота?"
    "Женя сидела рядом и весело болтала ногами."
    me "Да, но уже плохо помню, о чём там."
    mz "Ветряные мельницы же! Все твои истории – как борьба с ветряными мельницами."
    me "Да какие мельницы, я тебя умоляю…"
    mz "А даже если мельницы и нет, ты обязательно её построишь, ведь надо же тебе с чем-то бороться."
    me "Ты так говоришь, как будто я мазохист какой-то!"
    mz "А разве нет?"
    show cg zhenya1_smile with dspr
    "Хитро улыбнулась она."
    "Женя…{w} Что бы я делал без неё?"
    "Иногда мне даже казалось, что всё, произошедшее со мной в этом лагере, было не таким уж плохим, раз в конце меня ждала награда."
    "Я притянул её к себе и поцеловал."
    mz "Стой, что ты… А если кто-нибудь увидит?"
    "Женя покраснела и возмутилась, но скорее просто для вида."
    me "Не часто тебя это волнует."
    mz "Нет, но…{w} Ладно, о чём это я?"
    me "О ветряных мельницах?"
    show cg zhenya1 with dspr
    mz "Да…{w} То есть нет! То есть я имела в виду, что ты никак не можешь угомониться! Вот поехал бы, как все нормальные {i}люди{/i}, тогда на этом автобусе…"
    me "И не встретил бы тебя."
    show cg zhenya1_dontlike with dspr
    mz "А то ты раньше меня встречал! Всё Славя, Лена, Алиса…"
    "Обиделась она."
    me "Ну вот, получается, я всё сделал правильно!"
    mz "Да ну тебя! Тоже мне, альфа-самец с гаремом!"
    me "Хватит уже о прошлом – у нас вся жизнь впереди!"
    stop music fadeout 3
    "..."
    window hide
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    scene bg ext_polyana_sunset
    show blood
    with complexdissolve
    pause(1)
    play music music_list["sunny_day"] fadein 3
    window show
    pi3 "Эй! Ты живой?"
    window hide
    hide blood with dissolve
    play sound sfx_water_splash
    pause(0.5)
    window show
    "В лицо хлынула холодная вода, и я с трудом открыл заплывший гематомой глаз."
    show pi normal at center with dissolve
    "Надо мной склонился…{w} пионер."
    pi "Это опять ты… Что, {i}они{/i} меня не добили – решил помочь? Ну давай, не томи!"
    "Где-то в глубине души я был даже рад такому развитию событий – наконец-то этот сломанный замкнутый круг разорвётся!"
    pi3 "Да нет, ты не так всё понял! Я не…{w} Я не он!"
    pi "А кто тогда?"
    "Мне было уже наплевать – вот бы сейчас умереть, завершить этот виток и отправиться на новый!"
    "Наверное, я никогда так сильно не хотел, чтобы бесконечные циклы моей {i}жизни{/i} продолжались!"
    "Главное, чтобы всё подчинялось знакомым издавна правилам."
    pi3 "Как будто ты не понимаешь?.."
    "С надрывом произнёс пионер."
    pi "Не-не, в эти игры я больше не играю!"
    "Действительно, они что, решили поставить меня на место {i}того{/i} идиота?"
    "Это что, какая-то игра, а я для них – зелёный нуб!{w} Ну только не на моём сервере!"
    pi "И вообще, мне плевать!"
    scene bg ext_polyana_sunset:
        parallel:
            ease 0.5 zoom 1.1
            ease 0.5 zoom 1.0
        parallel:
            ease 0.5 align (0.1,0.1)
            ease 0.5 align (0,0)
    show pi normal at center
    "Я попытался встать, но от боли лишь застонал и привалился к стоявшему рядом пеньку."
    "Хотя, если предстоит провести в этом чёртовом цикле ещё пять с половиной дней, очевидно придётся идти на некоторые компромиссы."
    pi "Ладно, мне всё равно, кто ты и зачем ты здесь, но, если действительно хочешь помочь, я не откажусь."
    "Если он на самом деле тот, кем хочет казаться, то помощи от него ждать можно."
    pi3 "Да, конечно…"
    pi "Тогда принеси мне попить."
    hide pi with dissolve
    "Пионер быстро вскочил и скрылся за деревьями."
    pi "Неужели в столовую побежал? Дурной какой-то."
    "…"
    window hide
    $ persistent.sprite_time = "night"
    $ night_time()
    scene bg ext_polyana_night
    with dissolve
    window show
    "Время тянулось предательски медленно."
    "Телефон я потерял – то ли во время драки, то ли ещё раньше, так что, сколько прошло с того момента, как пионер побежал за водой, я сказать не мог."
    "Но в любом случае он должен был уже вернуться."
    "Раны болели нестерпимо, и, похоже, у меня начала подниматься температура.{w} Неужели заражение?"
    "Можно же просто умереть!"
    "Да хоть бы они меня там забили насмерть!"
    "Так ведь нет – надо лежать и ждать конца в мучениях."
    "Ну погодите!"
    "В следующий раз я вам покажу, я вам всем покажу!"
    "Страх смерти для меня перестал существовать просто потому, что бояться можно чего-то, что пугает."
    "В моей ситуации смерть явилась бы избавлением."
    "Но в это верилось с трудом – скорее в следующий раз всё повторится, а это значит, что придётся драться, придётся бороться за себя, за свою жизнь!"
    "Точно так же, как в те первые разы."
    "Сделать всё, чтобы не стать нытиком и сопляком, как {i}тот{/i}."
    "Я с трудом поднялся на ноги и поковылял в сторону лагеря."
    window hide
    scene bg ext_path2_night
    with dissolve
    window show
    "Смеркалось."
    "Стоило, наверное, спросить пионера, что случилось после того, как я потерял сознание во время избиения на площади."
    "Может быть, они меня ищут?"
    "Или думают, что я уже мёртв?"
    "В любом случае надо быть осторожным."
    "Сейчас мне, конечно, пригодились бы разнообразные навыки, которыми я овладел за всё время, проведённое в этих витках."
    "Только вот боец из одноногого-однорукого калеки никудышный…"
    stop music fadeout 3
    "..."
    window hide
    scene bg ext_square_night
    with dissolve
    play ambience ambience_camp_center_night fadein 3
    window show
    "На первый взгляд площадь выглядела пустынной – ни пионеров, ни птиц, ни белок, обильно населявших лес вокруг лагеря."
    "Да и в воздухе звенела опасная тишина – как затишье перед боем или как минное поле, которое обходят и люди и звери."
    "Сделай шаг – и разлетишься на куски."
    "Если бы всё было так просто…"
    "Однако я не мог просто стоять и ждать – нужно добраться до медпункта, промыть и перевязать раны, выпить обезболивающее и антибиотики."
    "Первые шаги по площади давались с трудом скорее от сильного морального напряжения, а не от боевых увечий."
    window hide
    scene bg ext_aidpost_night
    with dissolve
    play sound sfx_hiding_in_bush
    window show
    "Я кое-как доковылял до конца, прошёл по узкой дорожке, добрался до медпункта и уже начал возиться с замком, как вдруг рядом в кустах послышался знакомый шорох."
    "Точно: это не животное или птица – это человек!"
    "Однако я хорошо понимал, что озверевшие пионеры прятаться не будут – они теперь действуют в открытую."
    pi "Не знаю, кто там засел, но лучше тебе выйти, а не то…"
    "А не то что?"
    "В таком состоянии я вряд ли представлял большую угрозу, чем хоть та нахальная маленькая девчонка!"
    unp "Это всего лишь я…"
    show un surprise pioneer at center with dissolve
    "Почти что прошептала застенчивая пионерка, выбираясь из своего укрытия."
    pi "А, ты?"
    "Спросил я саркастично."
    pi "Одна? А где же остальные? Хотя да, тебя и одной хватит…"
    show un sad pioneer at center with dspr
    unp "Нет, я…{w} могу уйти, если мешаю."
    pi "Оставайся уж – хуже не будет."
    "Я тщетно возился с замком."
    "Конечно, мне не сложно было вскрыть его хоть зубочисткой, хоть спичкой, но то – со здоровыми пальцами, а мои были все в гематомах и ссадинах, суставы через один – выбиты."
    "Самое сложное действие, что под силу мне сейчас, – это держать пионерское знамя и лениво размахивать им над головой."
    "Само по себе дурное занятие, но местные пионеры могут меня заставить делать и такое."
    show un surprise pioneer at center with dspr
    unp "Может, я помогу?"
    pi "Чем? Моральной поддержкой?"
    show un normal pioneer at center with dspr
    unp "А у меня вот…"
    "Замолчала она на полуслове и протянула мне связку ключей."
    pi "Откуда?"
    "Да, я не ожидал подобного, но особо не удивился – было не до того."
    unp "Взяла у Слави."
    pi "Вот так просто? Хочешь сказать, она их отдала даже не спрашивая, зачем они тебе?"
    unp "Ну, я сказала, что плохо себя чувствую, но не хочу её отвлекать, поэтому могу сама сходить в медпункт."
    pi "Да уж, отличная отмазка. Хитрость, лукавство и притворство. Говорят, что за каждым сильным мужчиной стоит сильная женщина."
    "Я вспомнил про вторую пачку «Космоса», подаренную пионером."
    "Сигареты оказались изрядно помяты, но мне всё же удалось найти парочку целых."
    pi "Ладно, ключи мне действительно не помешают, это ты хорошо придумала."
    show un smile pioneer at center with dspr
    unp "Спасибо."
    "Еле заметно улыбнулась девочка."
    "Вдруг она и правда не прячет нож за спиной?..{w} Хотя откуда вообще такие мысли?!"
    "Презумпция невиновности никогда не работала в этом мире, а уж теперь самым правильным будет считать всех окружающих враждебными априори!"
    "Я внимательно оглядел девочку с ног до головы."
    show un surprise pioneer at center with dspr
    unp "Что?.. Со мной что-то не так?"
    pi "Да вот даже не знаю. Это ты мне лучше скажи – так всё с тобой или не так?"
    show un sad pioneer at center with dspr
    unp "Я тебя не понимаю…"
    "Пионерка явно смутилась и расстроилась."
    "Ну и ладно, пока она хотя бы притворяется {i}хорошей{/i}, стоит это использовать – самому, негнущимися руками будет проблематично перевязать все раны."
    pi "Не бери в голову. Если правда хочешь помочь…"
    stop ambience fadeout 3
    "…"
    window hide
    $ persistent.sprite_time = "day"
    scene bg int_aidpost_night
    with dissolve
    play music music_list["free_love"] fadein 3
    window show
    "Медпункт ярко осветили лампы дневного света, висящие под потолком."
    "Я с трудом взгромоздился на кушетку и попытался снять рубашку."
    show un normal pioneer at center with dissolve
    unp "Давай я помогу."
    pi "Ну помоги."
    "Слева и справа в районе живота ужасающими сине-красными подтёками рдели синяки."
    "Наверное, я сломал несколько рёбер, а может, наоборот, лишь несколько остались целыми."
    "Каждое движение отдавалось внутри резкой болью:"
    pi "Ыыыыы! Поаккуратнее нельзя?"
    show un sad pioneer at center with dspr
    unp "Извини."
    "Пионерка уж слишком ретиво начала меня раздевать."
    "Наконец я остался в одних шортах."
    show un surprise pioneer at center with dspr
    unp "Сейчас-сейчас, надо йодом смазать, продезинфицировать!"
    pi "Ага, ну да, чтобы я стал похож на бурого медведя? Нет уж, давай перекисью – в ящике стола лежит."
    show un normal pioneer at center with dspr
    "Пионерка не стала спорить."
    "Впрочем, что перекись, что йод – жжёт одинаково!"
    "Мне пришлось приложить нечеловеческие усилия, чтобы не заорать."
    show un sad pioneer at center with dspr
    unp "Больно?"
    pi "А ты как думаешь?!"
    "Сквозь зубы прошипел я."
    "Затем пионерка начала забинтовывать меня."
    "Каждый раз, когда ей приходилось перехватывать бинт с другой стороны, она практически вплотную прижималась ко мне."
    show un smile2 pioneer at center with dspr
    unp "Ну вот!"
    "С чувством выполненного долга сказала она."
    "Переигрывает – пронеслось у меня в голове."
    pi "Да, так получше."
    "Не то чтобы я действительно чувствовал себя лучше – скорее увереннее, что уже завтра я буду почти здоров."
    "Однако то – завтра."
    "Я попытался встать, чтобы дойти до шкафчика с лекарствами, но у меня неожиданно закружилась голова, и пришлось вновь сесть на кушетку."
    pi "Принеси мне анальгин и…{w} и…{w} ну, это…"
    show un normal pioneer at center with dspr
    "Неужели я действительно забыл содержимое местной аптечки?"
    "Поднёс руку ко лбу – он горел."
    pi "Что-нибудь от столбняка, я не знаю. Там написано, инструкция есть."
    window hide
    with fade
    window show
    "Девочка засуетилась и вскоре принесла мне горсть разноцветных таблеток."
    pi "Это что?"
    unp "Как ты и просил…"
    "Конечно, я рисковал, но хуже уже явно быть не могло."
    pi "Ну и воды – запить."
    "Я проглотил таблетки и с трудом растянулся на кушетке."
    show un serious pioneer at center with dspr
    "Пионерка села на стул рядом и выжидающе смотрела на меня."
    "Что же ей надо, в конце-то концов?"
    "Неизвестность утомляла."
    "Я просто хотел спать, отключиться и хоть на какое-то время забыть об этом безумном мире.{w} А ещё лучше – проснуться в другом!"
    "Пусть они закончат начатое и добьют меня!"
    "Или вот эта застенчивая девочка…"
    pi "И долго планируешь вот так сидеть?"
    show un surprise pioneer at center with dspr
    unp "Если я мешаю, то могу уйти."
    pi "Нет, ты не мешаешь."
    "Вдруг в голове родилась шальная, но при этом не лишённая смысла идея!"
    pi "Даже можешь помочь…"
    "Пионерка вопросительно посмотрела на меня."
    pi "Возьми вот ту баночку, видишь?"
    "Я с трудом поднял руку и показал пальцем на нужное лекарство."
    pi "А теперь набери оттуда полный шприц."
    stop music fadeout 3
    "..."
    window hide
    $ day_time()
    scene cg zhenya2_hug
    with complexdissolve
    pause(1)
    play music music_list["just_another_summer_day"] fadein 3
    window show
    mz "То есть ты это серьёзно?"
    "Лицо Жени горело, а голос звучал даже не удивлённо – испуганно!"
    me "Вполне!"
    mz "Нет, ты точно не в своём уме!"
    me "А что такого-то? Уж в крайнем случае через пару дней – новый виток, и никто уже и не вспомнит об этом."
    mz "Я вспомню – этого уже достаточно!"
    me "То есть твой ответ – нет?"
    mz "Мой ответ – хватит надо мной издеваться!"
    "Она попыталась встать, но я крепко схватил её за руки."
    mz "Эй!"
    "Вместо того чтобы попытаться вырваться, Женя засмеялась и крепко прижалась ко мне."
    mz "Ты точно не шутишь? А что если мы всё-таки выберемся отсюда?"
    me "Ты давно об этом не говорила."
    mz "Не говорила, а теперь говорю! Если в реальном мире ты рассчитываешь забыть и притвориться, что ничего сейчас не говорил, то…"
    me "Нет, и здесь, и в реальном мире мои слова искренни!"
    mz "Всё равно…{w} В это просто сложно проверить! Так внезапно…"
    me "Да что же тут внезапного? Как давно мы знакомы? Я уже потерял счёт виткам."
    mz "А я считаю…"
    "Тихо сказала Женя и ещё крепче обняла меня."
    stop music fadeout 3
    "…"
    window hide
    $ night_time()
    scene bg int_aidpost_night
    show un normal pioneer at center
    with complexdissolve
    pause(1)
    play ambience ambience_medstation_inside_night fadein 3
    window show
    "Пионерка послушно наполнила шприц бесцветной прозрачной жидкостью и протянула его мне."
    pi "Нет, ну где это видано, чтобы пациент сам себе уколы делал!"
    show un sad pioneer at center with dspr
    unp "Но я ведь не умею."
    pi "Да тут нет ничего сложного."
    "Просто для меня в этом мире всё-таки существовало одно-единственное табу – это самоубийство."
    "Я был готов (и даже хотел) умереть от рук обезумевших пионеров или от смертельной инъекции, но наложить на себя руки…"
    "Почему-то мне казалось, что нельзя, я даже сам толком не мог объяснить почему и никогда не пытался проверить."
    "Возможно, всему виной страх неизвестности, который с новой силой захватил меня в последние сутки, а может, всё куда проще и причина в банальном инстинкте самосохранения."
    "Как бы там ни было, я был уверен, что, если меня убьёт кто-то другой, то я тут же очнусь в новом витке, но уже готовый ко всему!"
    "Проблема только в том, что эта девочка явно не собиралась мне помогать в добровольном уходе из жизни."
    show un shocked pioneer at center with dspr
    unp "Нет, я…{w} А вдруг что-то не так сделаю? Лучше медсестру позвать! Я сейчас, я быстро."
    "Вот медсестры тут только не хватало!"
    pi "Подожди!"
    "Я с трудом приподнялся на локте и схватил её за руку."
    pi "Ты не бойся – я делал это сотни раз и тебя научу! Тут нет ничего сложного."
    show un surprise pioneer at center with dspr
    "Девочка заколебалась."
    pi "Сначала возьми жгут…"
    "Хотя нет, зачем ей жгут – он же нужен, когда кровь берут."
    pi "Ладно, жгут не бери."
    show un normal pioneer at center with dspr
    "Пионерка положила жгут на стол рядом со мной."
    "Я отвёл в сторону левую руку, чтобы ей было удобнее."
    show un sad pioneer at center with dspr
    unp "Может быть, всё-таки не стоит?.."
    pi "Да я даже ничего не почувствую."
    "Её руки дрожали, и игла скакала из стороны в сторону."
    "Если промахнётся мимо вены – будет не здорово."
    "И так-то эвтаназия лекарствами из советской аптечки – сомнительное удовольствие…"
    show un serious pioneer at center with dspr
    unp "Не смотри на меня так."
    "Вдруг сказала девочка."
    pi "Как я на тебя смотрю? Не отвлекайся!"
    show un sad pioneer at center with dspr
    unp "Я так не могу…"
    pi "Ну начинается…"
    "Обречённо вздохнул я и одёрнул руку."
    pi "Ладно, забей. Я просто посплю и завтра буду в норме. Когда будешь уходить, не забудь выключить свет и закрыть дверь!"
    show un normal pioneer at center with dspr
    "Девочка покорно направилась к выходу, но замерла на полпути."
    show un sad pioneer at center with dspr
    unp "Тебе правда очень больно?"
    pi "Правда-правда! Какая теперь разница? Буду терпеть."
    unp "Я могла бы…{w} только… если ты закроешь глаза."
    pi "Ну закрою, и что изменится?"
    show un smile pioneer at center with dspr
    unp "Мне будет так проще. Как будто ты спишь."
    "Улыбнулась она одними глазами."
    pi "Хорошо, давай закрою."
    "Как будто бы ничего страшного."
    "Пионерка подошла ко мне и взяла шприц."
    show un serious pioneer at center with dspr
    unp "Ну?"
    pi "Да-да."
    window hide
    stop ambience fadeout 3
    show blink
    window show
    "Я закрыл глаза, и в ту же секунду в мозгу стрельнула мысль: а почему вообще я так слепо ей доверяю?"
    "Ещё полчаса назад, стоя на крыльце, я думал совсем другое!"
    play music music_list["scarytale"] fadein 3
    "Что-то придавило меня к койке так сильно, что я не мог пошевелить ни руками, ни ногами.{w} Вот тварь!"
    window hide
    scene bg int_aidpost_night
    show un evil_smile pioneer close at center
    show unblink
    with dissolve
    window show
    "Надо мной нависла пионерка, держащая в руках жгут."
    "Ещё мгновение – и он крепко затянулся вокруг моей шеи."
    pi "Ты что…"
    "Захрипел я."
    "Если даже это и есть смерть, к которой я и стремился, то ведь не так, не удавить же меня жгутом! Нет! Подождите, я не готов!"
    "Пионерка давила всё сильнее, у неё на лице застыла гримаса безумия: рот оскалился в дьявольской улыбке, а запавшие глаза были широко открыты и как будто даже светились каким-то неестественным светом."
    "Я тщетно пытался вырваться – мешали раны и слабость."
    window hide
    show blink
    window show
    "И вот уже начинается кислородное голодание – перед глазами всё плывёт, я закрываю их, но на веках с внутренней стороны остается отпечаток её безумной гримасы!"
    window hide
    scene bg int_aidpost_night
    show sl serious pioneer close at center
    show unblink
    with dissolve
    window show
    "На краю сознание слышится стук распахнутой двери, дьявольская пионерка ослабляет хватку, и вот уже надо мной нависло лицо другой девочки."
    slp "Пойдём! Скорее!"
    "Шепчет знакомый голос."
    hide sl with dissolve
    "Кто-то помог мне подняться, я опёрся на кого-то и поковылял прочь из медпункта."
    "…"
    window hide
    stop music fadeout 2
    $ persistent.sprite_time = "night"
    scene black
    with fade2
    $ renpy.pause(2, hard=True)
    play sound_loop "zhenya/sounds/heavy_breathing.ogg" fadein 2
    $ renpy.pause(3, hard=True)
    scene zhenya_anim0
    with fade
    $ renpy.pause(5, hard=True)
    scene zhenya_anim1
    with fade
    $ renpy.pause(5, hard=True)
    scene zhenya_anim2
    with fade
    $ renpy.pause(5, hard=True)
    scene zhenya_anim3
    with fade
    $ renpy.pause(5, hard=True)
    scene zhenya_anim4
    with fade
    $ renpy.pause(5, hard=True)
    scene zhenya_anim5
    with fade
    $ renpy.pause(5, hard=True)
    scene zhenya_anim6
    with fade
    $ renpy.pause(5, hard=True)
    scene bg ext_polyana_night
    with fade3
    stop sound_loop fadeout 3
    $ renpy.pause(2, hard=True)
    window show
    "Мы шли медленно, постоянно спотыкаясь и натыкаясь на всё подряд."
    "Я то терял сознание, то вновь приходил в себя, но никак не мог поднять голову и смотрел лишь себе под ноги: брусчатка перед медпунктом сменилась асфальтом на площади, а та – землёй, покрытой опавшими листьями и хвоей."
    "Наконец мы остановились, я с трудом опустился на землю и осмотрелся."
    "Как будто та же поляна, куда меня принёс пионер…"
    pi "Какие-то адские круги сегодня нарезаю…"
    "Попытался я усмехнуться, но тут же закашлялся; тыльная сторона ладони была в крови."
    play ambience ambience_forest_night fadein 3
    show sl serious pioneer at center with dissolve
    slp "На вот, попей."
    "Девочка протянула мне походную флягу."
    "Я с трудом сделал несколько глотков и посмотрел на свою спасительницу."
    "Вроде та же знакомая девочка, только что-то словно выбивалось из её привычного облика."
    "Всё-таки улыбка этой пионерке шла больше, чем выражение холодной решимости, застывшее у неё на лице."
    "Я даже толком не знал, что сказать…"
    "Если уже один раз ошибся насчёт той маньячки в медпункте, позволил себе секундную расслабленность, то теперь надо быть собранным до конца!"
    "Однако невыносимая боль во всём теле и головокружение не давали сконцентрироваться даже на миг."
    pi "Да что тут…"
    show sl sad pioneer at center with dspr
    slp "Тихо, не надо говорить – тебе станет хуже! Я всё знаю."
    "Сказала девочка и пристально посмотрела на меня, словно, вопреки своим же словам, ожидала ответа."
    slp "Я всё знаю про тебя. На самом деле я тоже… настоящая."
    pi "Да какая ты, к чёрту, настоящая?! Мы уже встречались вчера – и ничего {i}настоящего{/i} я в тебе не заметил!"
    "Я вновь откашлялся кровью."
    pi "Это опять какая-то ваша шутка?"
    "Продолжил я тише."
    pi "Нельзя просто так убить меня, нельзя, да? Надо помучить, поиздеваться?! Хотите, чтобы я сошёл с ума?!"
    "И тут я понял, что всё это уже было когда-то…{w} только сейчас наши роли поменялись."
    show sl serious pioneer at center with dspr
    slp "Нет, нет, всё не так! Ты неправильно понял! Вчера ты разговаривал не со мной. Да что я объясняю – как будто сам не понимаешь!"
    "Нахмурилась пионерка."
    slp "Будто ты своих копий никогда не встречал?"
    "В её словах совершенно определённо была логика, изъян в которой у меня сходу найти не получилось."
    pi "Ну, допустим…{w} И зачем тебе всё это? Помогать мне, я имею в виду?"
    show sl normal pioneer at center with dspr
    slp "Потому что ты такой же, как я, {i}настоящий{/i}! Разве это не естественно? Разве на моём месте ты не поступил бы так же?"
    "Если бы она только знала, как я поступал раньше…"
    "Но вдруг она не врёт?!"
    "Ведь я же встречал в этом мире других {i}людей{/i} кроме себя!"
    pi "Спасибо, если так…"
    show sl smile pioneer at center with dspr
    "Пионерка ничего не ответила, лишь улыбнулась."
    pi "Но я всё-таки не понимаю, как тогда ты…{w} То есть я тысячи раз встречал «тебя» – и все они были ботами."
    show sl normal pioneer at center with dspr
    slp "Это сложно объяснить, да и некогда сейчас!"
    pi "Некогда, ты куда-то спешишь?"
    slp "И не я одна! Скоро мы выберемся отсюда!"
    pi "В смысле – из этого витка в новый?"
    show sl angry pioneer at center with dspr
    slp "Нет же! В смысле – вообще из этого лагеря!"
    pi "Это как так?.."
    "Расплылся я в глупой улыбке."
    "Даже сама идея о том, что из этого места есть выход, уже давно казалась мне абсурдной."
    show sl serious pioneer at center with dspr
    slp "Только не говори, что хочешь остаться тут навсегда?"
    pi "Да я, вообще-то, и так тут всегда…"
    show sl angry pioneer at center with dspr
    slp "Моё дело – предложить."
    pi "Нет, подожди, ты просто не так меня поняла…"
    "Да и почему, собственное, «не так»?"
    "Неужели я действительно готов вернуться в {i}реальный{/i} мир?"
    "Сейчас он для меня чужд и враждебен, ведь мой дом теперь этот лагерь."
    "Но этот дом лежит в руинах – разграбленный и сожжённый!"
    "Смогу ли я отстроить его заново?"
    show sl serious pioneer at center with dspr
    slp "Да? Ну и что же тогда ты хочешь?"
    pi "Хорошо, но как? Ты же не предлагаешь мне просто поверить тебе на слово? Если ты действительно понимаешь мою ситуацию, то не откажешься объяснить…"
    show sl normal pioneer at center with dspr
    slp "Хорошо, только не сейчас – надо убедиться, что за нами нет погони!"
    pi "Подожди…"
    hide sl with dissolve
    "Но пионерка не слушала меня и через секунду скрылась в бушующей лесной зелени."
    stop ambience fadeout 3
    "Просто отлично…"
    window hide
    $ day_time()
    $ persistent.sprite_time = "day"
    scene cg zhenya1_dontlike
    with complexdissolve
    pause(1)
    play music music_list["just_another_summer_day"] fadein 3
    window show
    mz "Но ведь я не умею шить!"
    me "Какая досада… Серьезное упущение со стороны хорошей хозяйки!"
    mz "Ой, да кто бы говорил! Из чего кольца собрался делать? Или, может, планируешь просто проволоку из катушки индуктивности на палец намотать?"
    me "Есть пара идей…"
    show cg zhenya1 with dspr
    mz "Ну, я слушаю."
    show cg zhenya1_smile with dspr
    "Женя пристально посмотрела на меня и улыбнулась, предвкушая мой провал."
    "Однако ещё до знакомства с ней я обзавёлся совершенно разными навыками, и смастерить пару колец не составило бы для меня особого труда."
    "Вопрос только в оборудовании – в пионерлагере не найдёшь ювелирных инструментов."
    "Так что подготовить всё необходимое за неделю я бы просто не успел…"
    "Если бы не кружок кибернетики!"
    "Если перебрать значительную часть хранящегося там оборудования, то позолоты на два простеньких кольца вполне хватит."
    "А уж занять чем-нибудь на пару дней тамошних кибернетиков точно не станет проблемой – благо, мне уже не впервой!"
    me "Это сюрприз!"
    show cg zhenya1 with dspr
    mz "Даже если так…"
    "Смутилась Женя."
    mz "То через неделю они исчезнут. Ты же знаешь, что не получится ничего забрать с собой."
    me "Ну и что? Для тебя важнее два куска металла или?.."
    mz "Нет, конечно нет…"
    me "Но раз уж мы планируем делать всё как у людей, то и платье…"
    show cg zhenya1_dontlike with dspr
    "Женя сверкнула глазами."
    "С костюмом не было особых проблем – я точно знал, что как минимум у нескольких парней в лагере есть брюки и пиджак, вроде бы даже тёмно-серого цвета."
    "Летнее платье тоже бы неплохо смотрелось на Жене, но, в конце концов, это же была её идея!{w} От которой она ожидаемо тут же отказалась."
    me "Используй тюль!"
    show cg zhenya1 with dspr
    mz "Ты серьёзно?"
    "Похоже, ей уже надоело спорить."
    me "Нет… Но ты всегда можешь попросить кого-нибудь из девочек! Думаю, это лучший вариант."
    show cg zhenya1_dontlike with dspr
    "Женя покраснела, надулась и отвернулась."
    mz "Вот сам иди и проси! И мерки с себя сними, потому что сам его и наденешь!"
    mz "Ну как ты вообще себе представляешь, что я вот так просто подойду, например, к Славе и спрошу: «А не сошьёшь ли ты мне свадебное платье?»"
    me "А ты скажи, что это…{w} для конкурса костюмов!"
    me "Нет, как-то глупо…"
    me "Для костюмированного бала!"
    show cg zhenya1 with dspr
    "Женя удивилась, но сразу же спорить не стала."
    me "А я уж пробью идею у вожатой, будь спокойна! И нечего будет смущаться! Свадьба – как часть представления. Заставим Шурика с Электроником разыграть первый выход человека в открытый космос, Мику пусть косплеит Ленина на броневике…"
    me "А мы с тобой – поженимся!"
    mz "И реконструкцией какого же исторического события ты хочешь это сделать?"
    me "Да какая разница, господи? Да хоть свадьба Екатерины Второй и Петра Третьего!"
    show cg zhenya1_smile with dspr
    mz "Ооо, незавидная судьба тогда тебя ждёт, муженёк!"
    "Ухмыльнулась Женя."
    me "Неважно, это просто пример! Видишь, ты уже шутишь."
    mz "Всё равно это как-то…"
    me "Доверься мне!"
    mz "Ладно, если ты считаешь, что всё получится…"
    stop music fadeout 3
    "…"
    window hide
    scene bg ext_polyana_day
    with complexdissolve
    pause(1)
    play ambience ambience_forest_day fadein 3
    window show
    "Начало светать, лихорадка вновь напомнила о себе и даже, похоже, усилилась."
    "«Настоящая» пионерка как будто заплутала где-то в лесу – кажется, меня опять кинули…"
    "Впрочем, в этот раз я не особо и обольщался – мне хотелось лишь вернуть мир на круги своя, а не возвращаться в {i}реальность{/i}."
    "Может быть, по ту сторону прошёл всего час или десятилетия – уже неважно."
    "Я чувствовал себя коматозником, который просыпается и не узнаёт окружающий мир."
    "На востоке ярким багровым заревом пылал горизонт, поливая небо всполохами огня."
    "А вдруг в этом мире изменились не только его обитатели?"
    "Ещё каких-то несколько минут – и лучи палящего солнца, добравшись до этой маленькой полянки, сожгут меня вместе со всем чёртовым «Совёнком»!"
    "Вот бы «настоящая» пионерка вернулась!"
    "Лучше уж обживаться в {i}новом{/i} мире, чем сгореть заживо в привычном!"
    "Тем более там никто не будет знать обо всём, что случилось со мной здесь!"
    "Обо всём, что натворил я сам…"
    show pi normal at center with dissolve
    pi2 "Кажется, ты о чём-то крепко задумался?"
    "Рядом раздался знакомый голос.{w} Мой голос…"
    pi "Что тебе надо?"
    "Я удивился его появлению и даже несколько испугался – мне хватало проблем с озверевшими пионерами, и о своих двойниках я и думать забыл."
    "Хотя «своих двойниках»?..{w} Как давно я не называл их так?"
    "Точно, ведь для меня всегда существовал {i}я{/i} и существовали {i}они{/i} – ничего общего, мы разные люди, пусть даже когда-то и были одним…"
    pi2 "Может быть, ты думаешь – в какой момент всё пошло не так?"
    "Тут он ошибся – я совсем не думал об этом."
    pi2 "Терзаешься сомнениями, задаёшь себе вопросы, на которые никогда не найдёшь ответов?"
    pi "Я просто хочу, чтобы всё это прекратилось! И твоё присутствие этому вряд ли поспособствует!"
    pi2 "Всё давно прекратилось, если ты об этом…"
    pi "Да? Что-то незаметно."
    pi2 "Для всех, кроме тебя! В тот день в автобусе ты принял неверное решение и умер."
    "Я внимательно осмотрел своё тело.{w} Оно болит, а значит – я жив!"
    pi "Не очень-то я похож на мертвеца!"
    pi2 "Думаешь, на самом деле всё так просто, как в кино? Ты хочешь помнить момент, когда жизнь покинула тебя, хочешь помнить свой последний вздох? Момент перехода? Первые мгновения на новом уровне существования?"
    pi "Что-то я не понимаю. Тогда, получается, я умер ещё тогда, в {i}реальности{/i}!"
    pi2 "Нет! Тебе был дан шанс, но ты им не воспользовался и попал в свой персональный ад, лимб, если угодно!"
    pi "Ой, тоже мне, открыл Америку, а то я не знал!"
    pi2 "Это ты знал, но не знал, что теперь ты тут остался один, а выхода нет!"
    pi "Знал я…"
    "Или хотя бы предполагал."
    pi "Ну а ты тогда как же?"
    show pi smile at center with dspr
    pi2 "А меня тут нет! Я – твоя галлюцинация!"
    "И лес огласился его мерзким смехом."
    "Всё это до боли знакомо, но почему оно повторяется именно сейчас?"
    "Правду говорят, что беда не приходит одна?"
    pi "Да ради бога…"
    window hide
    show blink
    window show
    "Я закрыл глаза и для надёжности ещё и отвернулся."
    pi3 "Не надо так с ним, ведь он тоже один из нас! Или по крайней мере когда-то был…"
    "Знакомый голос звучал несколько иначе."
    window hide
    stop ambience fadeout 3
    scene bg ext_polyana_day
    show pi normal at right
    show pi2 normal at left
    show unblink
    with dissolve
    play music music_list["faceless"] fadein 3
    window show
    "На поляне передо мной стояло уже двое пионеров."
    pi2 "Клин клином вышибают!"
    pi3 "Из него уже вышибли всё, что можно!"
    pi2 "Значит, ещё не всё!"
    "Они спорили, а реальность потеряла для меня всякий смысл."
    pi3 "Смотри, он уже совсем умом тронулся!"
    pi2 "Ничего особенного, пройдёт! Как в той истории, которую мы рассказывали Ульянке, {i}подписавшись{/i} именем несуществующего друга: «Сумасшедшие возвращают себе рассудок, а нормальные обезумевают»."
    show pi smile at right with dspr
    "И опять этот дьявольский смех."
    pi2 "Думаешь, это с ним в первый раз?"
    pi3 "А разве нет?"
    show pi normal at right with dspr
    pi2 "Я точно знаю, что не в первый! Он думает, что помнит всё, что готов ко всему, что знает наперёд поведение каждого пионера! Но он забыл так много! Забыл, быть может, самое важное…"
    show uv rage at center with dissolve
    uv2 "Да хватит уже!"
    "Вдруг эти двое расступились и вперёд вылезла ушастая…"
    "Я всегда её несколько опасался, потому что мне казалось, что ничего хорошего от неё ждать не стоит."
    "Более того, где-то в глубине души она вызывала у меня какой-то животный, первобытный страх, словно боязнь темноты."
    "Да и не верил я никогда в её истории!{w} Мол, она – это наше подсознание, его скрытая часть!"
    "Что за бред!"
    uv2 "Не видите, ему плохо! Никакого толку от вас! Вот ты…"
    "Ткнула она пальцем в «злого» пионера."
    uv2 "Бегом в медпункт за таблетками!"
    pi2 "Какими ещё таблетками?.."
    "Несколько опешил он."
    uv2 "Не знаю какими! Ты же у нас тут самый умный – вот и разберись!"
    hide pi with dissolve
    "Пионер обречённо вздохнул и медленно поплёлся в сторону лагеря."
    uv2 "А ты…"
    "Она посмотрела на «доброго»."
    show uv dontlike at center with dspr
    uv2 "А ты…{w} ну…{w} тоже найди себе какое-нибудь занятие! Ей-богу, тошно слушать твоё нытье – от него только хуже!"
    pi3 "Но я ведь хотел помочь…"
    uv2 "Но ты не помогаешь! Так что, давай!"
    "Она помахала рукой и сделала такое выражение лица, что в голове промелькнула мысль – ну точно недовольная кошка!"
    hide pi2 with dissolve
    "Пионер не стал спорить и последовал за своим двойником."
    pi "И что теперь?"
    "Спросил я без особого энтузиазма."
    "Меня обманывали уже не раз – не намерен я верить ей и сейчас.{w} Тем более ей!"
    "Никогда бы не подумал, что из всех местных обитателей именно ушастая придёт мне на помощь."
    "Да хотя бы на словах – ведь она тоже помнит прошлые разы, помнит нашу ссору в автобусе."
    pi "Думаешь, опять получится сделать из меня идиота?"
    "Я из последних сил поднялся, от боли в глазах потемнело."
    "Но куда я пойду?"
    "Надо было тогда самому взять шприц…"
    "И почему вообще я решил, что самоубийство {i}здесь{/i} – это конец?"
    show uv upset at center with dspr
    uv2 "Эй!"
    "Ушастая одним прыжком подскочила ко мне и придержала, чтобы я не упал."
    pi "Ты…{w} ты действительно хочешь, чтобы я поверил, что ты мне помогаешь?!"
    show uv normal at center with dspr
    uv2 "Ну а что я, по-твоему, делаю сейчас? В конце концов, я всегда {i}вам{/i} помогаю!"
    pi "Ну да, конечно…"
    "Я вновь опустился на землю и тяжело вздохнул."
    "Идти мне в таком состоянии действительно некуда."
    pi "Ну, и когда твои пионеры вернутся?.."
    uv2 "Скоро…"
    "Неопределённо ответила она."
    pi "Хорошо, посидим-подождём, мне уже терять нечего…"
    stop music fadeout 3
    "..."
    window hide
    scene bg ext_square_day
    with complexdissolve
    pause(1)
    play music music_list["just_another_summer_day"] fadein 3
    window show
    "На площади собрался весь лагерь."
    "Ульянка гонялась за Электроником тщетно пытаясь отобрать сделанный из картона сильно помятый шлем космонавта."
    "Сценка первого выхода человека в открытый космос не обошлась без курьёзов: импровизированной ракетой кибернетикам послужил памятник Генде, с которого Шурик и навернулся в самый ответственный момент."
    "Хорошо ещё до земли лететь было несколько ближе, чем с околоземной орбиты, да и встретила она незадачливого пионера почти как в песне – «травой у дома»."
    mt "Хватит бегать! Совсем убьётесь!"
    "Причитала Ольга Дмитриевна."
    "Даже и не знаю, что в данной ситуации её волновало больше – здоровье кибернетика или имидж лагеря, где с незапамятных времен 365 дней в году без несчастных случаев."
    show mz normal glasses pioneer at center with dissolve
    "Женя, стоявшая рядом, дёргала меня за рукав, но я, слишком увлёкшись представлением, не сразу обратил на это внимание."
    show mz bukal glasses pioneer at center with dspr
    mz "Ну!"
    me "Что?"
    mz "Ты уверен, что нам стоит это делать?"
    me "Так ты же сама хотела!"
    show mz angry glasses pioneer at center with dspr
    mz "И ничего я не хотела!{w} Просто ты предложил, а я согласилась…"
    me "Мы это уже сто раз обсуждали. Да и к тому же всё не по-настоящему, сама же знаешь."
    show mz rage glasses pioneer at center with dspr
    mz "Ах, значит, теперь не по-настоящему?"
    "Грозно сказала она."
    me "Я не в том смысле… Просто мы в {i}этом{/i} мире, не забывай. Через пару дней всё повторится, никто и помнить не будет об этом."
    show mz angry glasses pioneer at center with dspr
    mz "Да, но я-то буду!"
    me "Так кого ты больше стесняешься? Окружающих или сама себя?"
    show mz shy glasses pioneer at center with dspr
    "Женя покраснела и ничего не ответила."
    mt "Ладно, идите уже одевайтесь!"
    "Скомандовала нам Ольга Дмитриевна."
    me "Готова?"
    show mz smile glasses pioneer at center with dspr
    "Женя кивнула."
    "…"
    window hide
    scene cg zhenya3
    with fade2
    window show
    "Через 10 минут на площади разыгралось странное для обычного пионерлагеря зрелище."
    "Да что там – странным оно было даже для «Совёнка»!"
    "Да и чувствовал я себя странно, стоя посреди толпы пионеров в старом советском костюме с чужого плеча."
    "Конечно, не торжественный фрак, но всяко лучше шорт и рубашки с коротким рукавом."
    "Женя же была облачена в наспех скроенное подобие свадебного платья."
    "В другой ситуации я бы сказал, что она выглядит нелепо, но только не сейчас."
    "Сейчас это платье казалось мне красивее любых нарядов из пафосных салонов мод."
    mt "Так какую сценку вы сейчас разыгрываете, я забыла?"
    "Шепнула мне на ухо вожатая."
    me "Ольга Дмитриевна, да какая уже разница! Давайте начинать!"
    mt "Ну ладно…"
    "Женя стояла красная как рак и не знала, куда спрятать глаза."
    "На меня, видимо, она смотреть решительно не хотела."
    me "Всё будет хорошо."
    "Тихо сказал я."
    "В толпе пионеров весело улыбалась Мику, она выглядела так, как будто это её собственная свадьба – может быть, немного глупо, зато искренне."
    "Лена, как обычно, краснела, но изредка бросала на нас пристальные взгляды."
    "Алиса всем своим видом пыталась дать понять, что её сюда затащили насильно и, будь её воля, она бы лучше играла на гитаре или даже просто отсыпалась."
    "А вот Ульянка была от всего представления явно в восторге: детям для счастья много не надо."
    "Славя же как будто действительно радовалась за нас и мило улыбалась."
    mz "Давай уже закончим с этим побыстрее."
    "Кажется, ещё немного и Женя засмущается насмерть."
    me "Ладно."
    me "Мы готовы."
    "Крикнул я вожатой."
    "Теперь предстояло сказать то, что обычно говорят на свадьбах."
    "Конечно, точных слов я не знал, да и всё заготовленное заранее успешно забыл."
    me "Клянусь…"
    "Начал я дрожащим голосом."
    me "И в горе, и в старости…"
    "Нет, там как-то не так было."
    us "Да что ты мямлишь! Не слышно же ничего!"
    "Весело закричала Ульянка."
    dv "Да тихо ты, а то на месте Жени окажешься."
    "Угроза подействовала на неё мгновенно, и Ульяна замолчала."
    me "В общем, это…"
    "Ещё минуту назад я был готов поклясться, что абсолютно спокоен, а сейчас не мог вымолвить ни слова."
    "Что чувствовала Женя, оставалось лишь догадываться."
    "Я собрался с духом."
    me "Клянусь быть с тобой и в горе, и в радости, и в богатстве, и в бедности до конца дней своих, пока смерть не разлучит нас!"
    "До этого весело галдящие пионеры мгновенно замолчали."
    "Наступила такая тишина, что я слышал, как бешено колотится моё сердце."
    "Женя всё так же стояла потупив взгляд."
    me "Ну, теперь ты!"
    "Она набрала воздуха и выпалила скороговоркой:"
    mz "Согласна выйти за тебя замуж, обещаю быть с тобой и в беде, и в бедности. Всё!"
    "Толпа взорвалась смехом."
    "Впрочем, для меня слова Жени прозвучали вполне серьёзно."
    mz "И давай заканчивать уже."
    me "А как же «а теперь можете поцеловать невесту»?"
    "Шутливым тоном спросил я."
    "Женя сверкнула глазами, явно давая понять, что в данной ситуации можно обойтись и без поцелуев."
    "Наверное, она права, да и для этого ещё будет время."
    mt "Молодцы! Всем спасибо!"
    "Кричала Ольга Дмитриевна. Вперёд вышел Электроник с фотоаппаратом."
    "Вид у него был такой, что, казалось, он бы сейчас с большим удовольствием сжимал в руках монтировку."
    el "Пару кадров на память…"
    mz "Ну вот ещё!"
    "Рявкнула на него Женя."
    me "Да ладно тебе – для семейного фотоальбома."
    "Она помедлила немного, но всё же состроила некое подобие улыбки."
    window hide
    with flash
    window show
    me "У нас всё получилось, как надо! Даже лучше, чем надо!"
    "Женя впервые за всё время посмотрела мне прямо в глаза, улыбнулась и сказала:"
    mz "Да, наверное."
    stop music fadeout 3
    "…"
    window hide
    scene bg ext_polyana_day
    with complexdissolve
    pause(1)
    play ambience ambience_forest_day fadein 3
    window show
    "Я очнулся, когда день уже клонился к вечеру."
    "Жар отступил, а на правой руке обнаружился след от укола."
    "Неужели ушастая действительно помогла?.."
    "Поначалу просто не верилось в то, что кто-то здесь способен на добрый поступок после всего, что случилось в последние дни."
    "Я с трудом поднялся и направился в сторону лагеря."
    "В конце концов, в лесу мне точно делать нечего, а хуже уже как будто быть и не может."
    "Раз за разом в голове мелькала лишь одна мысль – надо дотерпеть, надо пережить эту неделю, а дальше будет проще – я восстановлюсь физически, появится даже немного времени, чтобы восстановиться морально."
    "Только не отчаиваться, не опускать руки – не уподобляться {i}ему{/i}!"
    "Лучше умереть, чем так жить!"
    stop ambience fadeout 3
    "..."
    window hide
    scene bg ext_square_day
    with dissolve
    play music music_list["farewell_to_the_past_full"] fadein 3
    window show
    "По площади туда-сюда весело носились пионеры с рюкзаками, сумками и пакетами."
    "Около Генды, как маленький монумент, стояла вожатая, уперев руки в боки и грозно покрикивая."
    "Я застыл как вкопанный, не зная, чего ожидать."
    "{i}Этот{/i} мир находился в постоянном движении, меняясь на глазах: ещё вчера они хотели меня убить, а что сегодня?"
    show mt angry panama pioneer far at center with dissolve
    mtp "Эй, Семён!"
    "Крикнула вожатая, грозно посмотрев на меня."
    pi "Кто, я? Ты ко мне обращаешься?"
    mtp "Почему ещё не собрался?"
    pi "Собрался? Я скорее разобрался…"
    mtp "Сегодня последний день смены! Опять забыл?! А ну-ка марш собираться!"
    "Мне не хотелось с ней спорить – просто не было сил, – а удивляться я перестал уже давно, поэтому лишь бросил:"
    pi "А ничего, что я в таком виде?.."
    "И показал на свою рваную одежду и синяки по всему телу."
    show mt surprise panama pioneer far at center with dspr
    mtp "А что с тобой?"
    "Искренне удивилась вожатая."
    mtp "Бегал по лесу и упал?"
    pi "Что за бред? По какому ещё лесу? С какой стати мне вообще бегать по лесу?"
    show mt grin panama pioneer far at center with dspr
    mtp "Ладно, это твоё дело… Мы уезжаем через полчаса, опять опоздаешь – останешься ещё на одну смену!"
    "Ухмыльнулась она."
    "«Останусь ещё на одну смену»…"
    "Нет, это точно не входит в мои планы!"
    "Как бы там ни было, но появился шанс выбраться отсюда – пусть даже таким дурным способом!"
    hide mt with dissolve
    "Я медленно поплёлся к остановке."
    window hide
    scene bg ext_bus
    with dissolve
    window show
    "Перед автобусом столпился весь лагерь."
    "Все ждали вожатую – ведь не в её правилах следовать своим собственным правилам."
    unp "Ой, а что с тобой случилось?.."
    "Участливо поинтересовалась пионерка из медпункта."
    slp "С тобой всё в порядке? Может, пластырь дать?"
    "Ага, ещё подорожник приложи!"
    dvp "Небось налакался он и в канаву упал."
    "Ну да, кто бы говорил…"
    usp "А вдруг его волки подрали!"
    "Если только эти волки – местные пионеры…"
    "Я просто тихо сидел на бордюре, опустив голову на руки."
    "Уже не хотелось думать о том, что будет завтра – пойду ли я на новый виток или всё наконец-то закончится раз и навсегда."
    "А может быть, впереди меня ждёт что-то другое, что-то…{w} лучшее?.."
    stop music fadeout 3
    "…"
    window hide
    scene bg int_house_of_sl_day
    with complexdissolve
    pause(1)
    play ambience ambience_int_cabin_day fadein 3
    window show
    "Когда я проснулся, Жени рядом не оказалось."
    "Наверное, уже ушла по каким-то своим делам."
    "И вот сдалась ей вся эта игра в пионеров, ей-богу!"
    "Особенно в первую-то брачную ночь!"
    "Я потянулся и сладко зевнул."
    "Ну и ладно, зато смогу сделать ей сюрприз – нарву цветов в лесу."
    "Не бог весть какой подарок, но я знаю – она любит ландыши."
    "Никогда не понимал, почему женщинам нравятся цветы…"
    "Почему не крапива тогда или борщевик?"
    "Ведь это тоже растения и хороши они в своей естественной среде обитания, а не в горшках и вазах."
    "Впрочем, какая разница, если каждый раз, когда я дарил Жене ландыши, её лицо озарялось лучезарной улыбкой?"
    stop ambience fadeout 3
    "Конечно, может быть, дело не только в самих цветах…"
    window hide
    scene bg int_library_day
    with dissolve
    play ambience ambience_library_day fadein 3
    window show
    "С букетом в руках я вбежал в библиотеку, громко распахнув дверь."
    show dv normal pioneer at center with dissolve
    "За столом библиотекаря сидела хмурая Алиса и лениво листала какой-то журнал."
    show dv guilty pioneer at center with dspr
    dv "О, новобрачный припёрся."
    "Пробурчала она, глядя исподлобья."
    me "Привет, а Женя где?.."
    show dv normal pioneer at center with dspr
    dv "Не знаю. Попросила меня тут посидеть за неё, а сама куда-то ушла."
    "Ну да, моя Женя может даже Алису уговорить."
    me "Ну ладно, тогда я…"
    dv "И что-то она совсем не сияла от счастья."
    hide dv with dissolve
    "Бросила Алиса мне вслед."
    "Куда же пошла Женя?"
    "Может, тоже решила сделать мне сюрприз?"
    "Да нет, сюрпризы не по её части – наверное, просто время завтракать."
    stop ambience fadeout 3
    "Я пошёл – нет, побежал – в столовую."
    window hide
    scene bg int_dining_hall_people_day
    with dissolve
    play ambience ambience_dining_hall_full fadein 3
    window show
    "Внутри весело галдели пионеры, весело же стучала посуда, даже обычно хмурая повариха казалась сегодня необычайно веселой."
    "Я заметил Славю и подошёл к ней."
    show sl normal pioneer at center with dissolve
    me "Привет, ты не видела Женю?"
    show sl surprise pioneer at center with dspr
    "Славя посмотрела на меня удивлённо, потом слегка смутилась и отвела глаза."
    show sl sad pioneer at center with dspr
    sl "Она, кажется, пошла на остановку."
    me "На остановку? Зачем?"
    sl "Не знаю…{w} Тебе лучше спросить у неё самому. Ты успеешь, если поспешишь."
    stop ambience fadeout 3
    "Ну, на остановку – так на остановку!"
    window hide
    scene bg ext_no_bus
    with dissolve
    play music music_list["i_dont_blame_you"] fadein 3
    window show
    "Через минуту я выбежал за ворота лагеря…"
    show mz normal glasses pioneer far at center with dissolve
    "И увидел Женю, стоящую возле дороги, её взгляд был устремлён куда-то далеко к горизонту за поля и леса, вслед яркому летнему солнцу."
    "Странное выражение лица, в котором слились и грусть, и ожидание, и томления, но в то же время Женя выглядела совсем не так…{w} я не узнал её."
    window hide
    scene bg ext_bus
    with complexdissolve
    window show
    "Лучшее? Нет, в это поверить я могу ещё меньше, чем в то, что завтра я вернусь в {i}реальный{/i} мир."
    "Может быть, раньше было лучше?"
    "Кажется, тот пионер говорил, что я многое забыл…"
    "Только вот что именно?"
    window hide
    scene bg ext_no_bus
    show mz normal glasses pioneer at center
    with complexdissolve
    window show
    me "Привет, а я тебя искал."
    "Это прозвучало глупо, а мой голос заметно дребезжал – просто надо было что-то сказать, и я натянул фальшивую улыбку и попытался говорить приветливо."
    show mz bukal glasses pioneer at center with dspr
    mz "Что тебе надо?"
    "Холодно ответила Женя, не оборачиваясь."
    me "Я проснулся, а тебя нет, вот и…"
    show mz normal glasses pioneer at center with dspr
    "Женя резко развернулась и сверкнула глазами."
    mz "Я уезжаю."
    "Сказала она неожиданно спокойным тоном."
    me "Куда?"
    mz "Домой."
    me "Здесь же не ходят автобусы…"
    "Какие, к чёрту, автобусы?!"
    mz "Ходят."
    me "А я вот принёс тебе…"
    window hide
    show mz rage glasses pioneer at center with dspr
    pause(0.5)
    window hide
    "Я дрожащей рукой протянул Жене букет, который тут же полетел на землю."
    mz "Не нужно мне от тебя ничего! Ты вчера… Знать тебя не хочу! Не понимаю, что на меня нашло, но уверена, что во всём ты виноват!"
    me "В чём?"
    mz "Во всём! Свадьба эта дурацкая и то, что было ночью…"
    me "Но мы ведь договаривались… Ты сама этого хотела! Помнишь, ещё пару недель назад?"
    mz "Пару недель назад я тебя даже не знала!"
    window hide
    scene bg ext_bus
    with complexdissolve
    window show
    "Да, наверное, всё началось именно тогда."
    "Или {i}продолжилось{/i} – уже наплевать!"
    "Я решил, что могу быть счастлив с Женей, а она исчезла так же, как и появилась – внезапно."
    "{i}Женя, сидящая не в библиотеке, а на крыльце столовой{/i} – это было так давно…"
    "Однажды я уже потерял надежду, перестал быть человеком, но потом встретил её, и жизнь как будто дала мне второй шанс, пусть даже и в этом странном мире."
    "А потом она ушла, и спустя бесконечность циклов я всё забыл, я стал прежним и вновь перестал быть собой…"
    "Может быть, {i}он{/i} был прав?.."
    window hide
    scene bg ext_no_bus
    show mz rage glasses pioneer at center
    with complexdissolve
    window show
    me "Что ты такое говоришь?.. Мы знакомы уже…{w} я даже не знаю, как давно мы знакомы!"
    mz "Я с тобой не знакома и не собираюсь знакомиться! Знать тебя не хочу."
    me "Но подожди, мы ведь…"
    "На меня вдруг накатила внезапная слабость, и я опустился на колени, чтобы не упасть."
    "На безымянном пальце правой руки горело обручальное кольцо – я буквально физически чувствовал его жар."
    mz "На, забирай!"
    "Женя достала что-то из кармана и швырнула в меня."
    mz "Пойду пешком!"
    hide mz with dissolve
    "Я покрутил в руках тоненькое золотое обручальное колечко и заплакал."
    stop music fadeout 3
    "Так, как никогда не плакал раньше – ни в этом, ни в прошлом мире…"
    window hide
    scene bg ext_bus
    with complexdissolve
    play music music_list["meet_me_there"] fadein 3
    window show
    "И тогда всё и закончилось."
    "Навсегда."
    "Наверное, во мне всё же оставалось что-то человеческое, поэтому я и решил всё забыть, чтобы окончательно не сойти с ума."
    "Но теперь воспоминания вновь со мной, а с ними вернулась и боль – не такая острая, притупившаяся со временем, но всё ещё разрывающая на части."
    "Как будто меня растерзали на куски, и остался только небольшой клочок плоти, по странной случайности наделённый сознанием."
    "Не целое и даже не часть целого, а всего лишь досадная случайность, допустимая ошибка в безупречном уравнении этого мира."
    show pi normal at center with dissolve
    pi4 "Не грусти, брат!"
    "Ко мне подсел какой-то пионер."
    pi "Это опять ты?"
    pi4 "Кто – я?"
    pi "Да какая уже, к чёрту, разница?! Ты, он, этот, тот – вы все на одно лицо!"
    "Пионер ничего не ответил, лишь усмехнулся."
    pi "Пришёл поиздеваться? Лучше бы вы меня тогда убили!"
    pi4 "Но ты ведь всё вспомнил."
    pi "Вспомнил – и от этого только хуже!"
    pi4 "Ты сам во всём виноват."
    pi "В чём? В том, что тогда хотел помешать тебе уехать вместе с ушастой? Я же знаю, что в том автобусе был именно ты!"
    "Лицо пионера оставалось бесстрастным."
    pi4 "Может быть, я, а может, и нет – какая сейчас разница?"
    pi "То есть ты…{w} выбрался?"
    pi "И вернулся, только чтобы поиздеваться надо мной?"
    pi4 "А разве ты сам так не делал?"
    pi "Ой, избавь меня от своих морализаторских нравоучений, ради бога!"
    window hide
    scene bg ext_no_bus
    with complexdissolve
    window show
    "Я стоял на коленях и смотрел вслед медленно удаляющейся Жене."
    "Вот она скрылась за поворотом, и её больше не вернуть…"
    "Впрочем, я знал, что это уже не Женя – моя Женя исчезла ещё вчера, а это – бездушная кукла, лишь похожая на неё.{w} Но похожая настолько…"
    "Просто сказка не могла длиться вечно!"
    "Этот мир – настоящий ад, а я в нём – демон.{w} А демонам не суждено познать счастье."
    window hide
    scene bg ext_bus
    show pi normal at center
    with complexdissolve
    window show
    pi "Скажи мне только одно."
    "Наконец нарушил я молчание."
    pi "Почему всё именно так?"
    pi4 "У тебя был шанс, был выбор с самого начала – ты мог повести себя по-другому. Ведь многие всё сделали правильно – совсем не так, как ты и подобные тебе."
    pi "Ну да, они выбрались и теперь живут счастливо вместе со своими куклами в {i}реальном{/i} мире!"
    "Ухмыльнулся я."
    pi4 "Ты считаешь, что твоя жизнь лучше?"
    "Он сделал ударение на слове «жизнь»."
    pi "Если ты во всём виноват…{w} Если ты забрал у меня Женю…"
    "Внутри росла ярость, хотелось наброситься на него и забить до смерти!"
    "Но я даже не был уверен, что этот пионер материален."
    "Да и что бы изменилось?"
    pi4 "Ты мог бы быть счастлив с каждой из девочек, ведь именно поэтому они все здесь."
    "Такого ответа я не ожидал."
    pi "Но ведь они все нереальны! Здесь реальны только я… ты… все мы и…{w} Женя…"
    pi4 "Это только для тебя, в твоём {i}мире{/i}. Ты же знаешь, что реальностей много, и в каждой ты сам определяешь свою судьбу. Возможно, когда-то был всего один Семён, но в этом лагере перед ним открылась масса возможностей."
    pi4 "Кто-то смог выбраться и сейчас живёт счастливо, как ты выразился. А кто-то застрял – как ты, например."
    pi "Так что это за место? Кто ты такой тогда?"
    pi4 "Можешь считать меня вожатым."
    hide pi with dissolve
    "Пионер улыбнулся – искренне, без доли издёвки – и растворился в воздухе."
    "От его слов мне стало почему-то немного легче…"
    window hide
    stop music fadeout 3
    scene bg ext_no_bus
    with complexdissolve
    play ambience ambience_camp_entrance_day fadein 3
    window show
    "Мир в одну секунду словно накрыло туманом, затем перед глазами сверкнула яркая вспышка."
    "Я огляделся и понял, что исчез автобус, исчезли все пионеры."
    "Ну что опять?"
    window hide
    scene cg d6_pioneer
    with dissolve
    window show
    "Ворота тихо скрипнули, и я инстинктивно спрятался за памятником пионеру."
    "На остановку вышел Семён – один из Семёнов, но выражение его лица мне было до боли знакомо."
    "Я давно забыл, что и сам могу выглядеть так же."
    "Он долго смотрел на дорогу, затем направился назад в лагерь."
    pi "Не доверяй ему."
    "Сказал я на автомате."
    me "Ты кто?!"
    "Удивился Семён."
    pi "Стой! Не подходи!"
    me "Ладно, стою…"
    pi "Ты видел его? Разговаривал?"
    me "Ты о ком вообще?"
    pi "Ты знаешь…"
    me "Да…"
    pi "Что он тебе сказал?"
    me "Ничего особенного…"
    pi "Он давал тебе советы? Говорил, как себя вести? Угрожал?"
    me "Нет, ничего такого…{w} Конечно, он мне показался весьма странным, но не более того…"
    pi "Запомни, он может быть не один!{w} Точнее, он-то один, но ты можешь встретить здесь множество похожих на него пионеров."
    me "А ты-то кто сам? И от кого прячешься?"
    pi "Ты поймёшь…{w} Со временем…{w} Помни, главное – найти выход!"
    window hide
    scene black
    with dissolve
    play sound sfx_wind_gust
    pause(1)
    stop ambience fadeout 3
    window show
    "Вдруг поднялся настолько сильный ветер, что с деревьев полетели листья, перед глазами опять сверкнула та же вспышка..."
    window hide
    scene bg ext_bus
    with complexdissolve
    window show
    "И через мгновение словно из ниоткуда вновь возник автобус и пионеры."
    "Не знаю, зачем я всё это сказал ему…"
    "Просто посчитал это правильным."
    "Если бы я помнил, что такое угрызения совести и раскаяние, то, возможно, это именно они."
    play music music_list["reflection"] fadein 3
    mz "Пионер должен быть всегда готов!"
    "Знакомый голос прозвучал как гром среди ясного неба, а знакомый шлепок по спине вывел из состояния гроги."
    show mz smile glasses pioneer at center with dissolve
    "Передо мной стояла Женя."
    "Я сразу понял – моя Женя, а не кукла!"
    pi "Но как…"
    "Только и смог прошептать я."
    mz "Я не знаю…"
    "Она улыбалась, но её голос дрожал."
    mz "Тогда, после свадьбы, я проснулась в другом мире...{w} и уже думала, что потеряла тебя. А потом… а потом было столько витков, и я почти забыла…"
    pi "Прости."
    "Тихо сказал я."
    pi "Прости меня за всё."
    mz "Но это ничего. Потом пришёл {i}он{/i} и сказал, что сможет провести меня в тот мир, где ты сейчас. Сначала я не поверила, но…{w} вот я и здесь!"
    "Я вскочил и сжал Женю в своих объятиях."
    pi "Прости! Я забыл… Забыл всё, забыл тебя. И сделал столько плохого. Я не верил, не надеялся! Прости!"
    mz "Уф, задушишь!"
    "Женя высвободилась из моих объятий."
    mz "Но теперь-то я здесь, значит, всё в порядке!"
    show mz cry_smile glasses pioneer at center with dspr
    "Сказала она сквозь слёзы."
    pi "Как ты можешь быть так спокойна?"
    mz "Потому что я всегда знала, что мы снова будем вместе."
    "Женя подняла правую руку, и на безымянном пальце я увидел колечко, сплетённое из лепестков ландыша…"
    pi "А своё я потерял, прости…"
    show mz smile glasses pioneer at center with dspr
    mz "Ничего, купим новое!"
    "Улыбнулась она."
    mtp "Эй, садитесь в автобус, вы двое!"
    "Недовольно кричала Ольга Дмитриевна."
    "…"
    window hide
    $ night_time()
    scene bg int_bus_night
    with complexdissolve
    $ persistent.sprite_time = "night"
    window show
    "Автобус, мирно подпрыгивая на кочках, медленно ехал в сторону райцентра…{w} или куда он там едет на самом деле!"
    show mz smile glasses pioneer at center with dissolve
    pi "Знаешь, я просто не могу поверить, что всё это наконец закончится."
    "За последнюю неделю я пережил столько всего…"
    show mz bukal glasses pioneer at center with dspr
    mz "Вот так всегда – тебе самое интересное!"
    "Надулась Женя."
    pi "Не думаю, что ты хотела бы поменяться местами."
    mz "Да уж я могу представить! Только всё равно это интереснее, чем дни напролёт просиживать в библиотеке."
    pi "Странные у тебя понятия об интересности…"
    show mz smile glasses pioneer at center with dspr
    mz "А ты уже думал?"
    pi "О чём?"
    mz "Что будет потом… завтра? Нам ведь надо как-то встретиться в реальном мире!"
    pi "Да, точно, сейчас адрес свой запишу."
    show mz bukal glasses pioneer at center with dspr
    mz "Ну да, ты ещё письмо отправь!"
    "Я глупо улыбнулся."
    show mz smile glasses pioneer at center with dspr
    mz "Я запомню, говори."
    "Мы обменялись с Женей адресами и телефонами."
    "Странно, почему нам раньше не приходило в голову этого сделать?"
    "Наверное, мы и не надеялись выбраться из этого мира и просто не хотели вспоминать о прошлой жизни."
    show mz bukal glasses pioneer at center with dspr
    mz "А как оно будет, как думаешь? Как обычно? Мы просто заснём?"
    show mz smile glasses pioneer at center with dspr
    "Женя обняла мою руку и прижалась всем телом."
    pi "Надеюсь. В конце концов, это не самый плохой вариант!"
    mz "Даже один из лучших, я бы сказала."
    "Женя зевнула и закрыла глаза."
    hide mz with dissolve
    mz "Спокойной ночи. Увидимся."
    "Я ничего не ответил и лишь продолжал смотреть в окно на пролетающий мимо ночной пейзаж."
    "Лагерь «Совёнок» остался позади, и я больше никогда туда не вернусь."
    "Да, в этом я был уверен."
    "Однако он всегда будет частью моей жизни."
    "Там я изменился, изменился несколько раз."
    "По сравнению со временем, проведённым там, жалкие 50-60 лет, что мне предстоит прожить в реальном мире, кажутся мгновением, но я обязательно проживу их как настоящий человек!"
    show mz smile glasses pioneer at center with dissolve
    mz "Да, наверное, ты действительно плохой, как и говорил тот пионер…"
    "Пробурчала Женя сквозь сон."
    me "Что?"
    mz "Ничего, спи уже!"
    "Засмеялась она и больно ущипнула меня."
    "…"
    window hide
    stop music fadeout 3
    scene black
    with fade3
    pause(3)
    scene bg semen_room
    with fade3
    pause(1.5)
    window show
    "Интересно, что чувствовали другие на моём месте?"
    "Такую же потерю ориентации в первые мгновения, чувство тревоги, даже паники?"
    "Я вернулся в свою старую квартиру, но не узнавал ничего вокруг себя."
    "Действительно, такое ощущение, как будто оказался в доме, где жил много-много лет назад – вроде бы всё на своих местах, но ты уже ничего не помнишь, тебе просто кажется, что так и должно быть."
    "Я уже забыл, какое было число, когда я исчез из этого мира (да и в годе не уверен), но на улице зима, а значит, {i}здесь{/i} прошло не так уж и много по времени."
    "Да, мне теперь не 17 лет, но и на свой {i}реальный{/i} возраст я не выгляжу тоже!"
    "Получается, всё прошло нормально, переход случился без последствий?"
    "Женя…"
    "Я бросился к столу и трясущейся рукой стал записывать адрес и телефон."
    "Конечно, я никогда бы не смог их забыть, но лучше подстраховаться."
    "Ну а что дальше?"
    "Как вообще устроен этот мир?"
    "Здесь же совсем другие законы…{w} которых я, если уж быть честным, не понимал и раньше."
    "А теперь я вообще словно новорождённый, которого заставляют жить взрослой жизнью!"
    "Впрочем, это всё потом, а сейчас – надо найти Женю!"
    window hide
    play sound "zhenya/sounds/door-bell.ogg"
    pause(1)
    window show
    "В дверь позвонили…"
    "«Люди» – мелькнула мысль.{w} Реальные люди, не пионеры…"
    "Но надо открыть, ничего не поделаешь, я вернулся и теперь мне предстоит жить в этом мире."
    "Я с трудом подошёл к двери, медленно открыл замок, схватился за ручку и замер."
    play music music_list["reflection"] fadein 3
    mz "Ну! Долго мне тут стоять?"
    show mz irl at center with dissolve
    "Я рывком распахнул дверь и увидел Женю…"
    "Она выглядела почти так же, как и в лагере."
    me "Но…{w} как?"
    mz "Ты же помнишь, что я всегда появлялась в лагере на неделю раньше тебя? Вот и назад я вернулась раньше."
    "Я забыл про «Совёнок», забыл про реальный мир – главное, что мы снова вместе!"
    window hide
    with fade
    window show
    "Я подхватил Женю на руки и отнёс в комнату."
    mz "Ну, так и будем стоять?"
    me "Да, прости…"
    "Женя легко спрыгнула на пол."
    mz "Сейчас, подожди… Это надо сделать сразу, а то потом может быть не до того."
    "Она хитро улыбнулась и начала рыться в сумочке."
    mz "Дай руку."
    "Я протянул ей правую руку, и Женя надела мне на палец кольцо."
    "Совсем простое – как тогда, в лагере."
    "А у неё на пальце в тусклом свете пыльной люстры блестело маленькое золотое колечко."
    me "Наверное, это мне стоило кольца купить…"
    mz "Ну, судя по убранству твоего лежбища, не похоже, что у тебя есть на это деньги."
    "И мы засмеялись, искреннее, от души."
    "За окном падал настоящий снег, белый, пушистый, темноту ночи разрезали тысячи огней большого города, который пел на сотни голосов, напоминая, что мы всё ещё живы и всё ещё вместе."
    "Я нежно провёл рукой по щеке Жени.{w} Тёплая, настоящая…"
    me "Ведь теперь ты не исчезнешь?"
    mz "Ну уж будь уверен! Ты мне ещё за кольца должен!"
    "Я заключил Женю в объятия и поцеловал так, как никогда прежде…"
    window hide
    pause(10)
    scene black
    with fade3
    stop music fadeout 5
    pause(5)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
