init:

    $ mods["EvSuPrlg"]=u"Лазурное лето. С нуля."
    
    image bg cum_room = "Azure_summer/bg/cum_room.jpg"
   
label EvSuPrlg:
    $ sunset_time()
    $ persistent.sprite_time = 'sunset'
    scene bg cum_room
    play music music_list["drown"]
    
    $ set_mode_nvl()
    "Часы показывали 18:00 {w}{p}
    Пора собираться. Сдался мне тот день рождения.{w} Абсолютно бессмысленная дата. Зачем мне вообще туда идти?{w} Было бы что отмечать, просто рандомный день, в который ты явился свету, что никак от тебя не зависело. Как не хочется идти в ту веселую, шумную компанию моих знакомых.{w} Зачем вообще меня звать? Похоже для очередного ежегодного обмена купюрами, вот зачем.{w}{p}
    Живу себе сам и чувствую себя отлично. А как доходит дело до общения или знакомства с новыми людьми - сразу настроение скатывается до нуля.{w} Не люблю я этого. Не потому, что сказать нечего или страшно, просто не хочу.{w} Такой я человек. И что?{w} Зато осуждения со стороны родственников и других знакомых. Нельзя так в четырёх стенах сидеть, ничем не интересоваться, ничем не увлекаться, нельзя так жить.{w} Почему нельзя? Где это указанно и кем придумано? Человеку для жизни достаточно дышать, есть, пить, спать. Всё остальное – субъективщина, навязанная большинством, которую во многих закладывают с ранних лет.{w} Если мне нравится сидеть в тишине и покое, почему бы меня так не оставить?{w}{p} 
    Нет, я не отрицаю “насыщенную” социальную жизнь и плохого в ней ничего не вижу.{w} Просто каждому своё. Однако, многие считают лишь свое виденье правильным, единственно верным.{w} Нет ничего плохого в асоциальности."
    
    nvl clear
    
    "Я никого не осуждаю, никому не мешаю и ни к кому не лезу в жизнь – в общем живу никоим образом не затрагивая окружающих. Зато стоит кому-либо узнать мои взгляды на бытие - тут же неприязнь в глазах, тут же летит совет что мне делать.{w}{p} 
    В чём-то я похож на изолированное племя. Они живут в своем мире, знать не зная, что «за пределами» леса, есть другой мир.{w} В своём лесу они «вершина эволюции», для них известно лишь то, что достижимо им. Только я скован смирением.{w} Есть в жизни недостижимые вещи, и ничего с этим не поделать. Живя на определенном социальном уровне, на нем можно творить, менять, приобретать, а проще просто существовать, но выше не подняться.{w}{p} 
    Наверное, проще провести аналогию с ММОРПГ-играми.{w} Вот у тебя персонаж - воин, маг, целитель, лучник и у каждого своя ветка развития.
    Воину можно стать физически сильнее, лучнику точнее. {w}Но магу не сменить посох на секиру, целитель не начнет стрелять из лука.{w}
    Так и художник не споёт оперу, а певец не нарисует Мона Лизу.{w}{p}"
    $ set_mode_adv()
    
    $ set_mode_nvl()
    "Я согласен, что так жить не хорошо, главное – что не плохо.{w} Мне этого достаточно. Вот посередине этих двух крайностей мне и комфортно.{w}{p}
    А может всё из-за моего противного характера? Сегодня дружба, жвачка – завтра мне этот человек будет противен.{w} Нахожу новое увлечение, проходит неделя - заинтересованность испаряется. {w}Теперь я делаю то, что хочется сейчас и ничего с собой не могу поделать.{w} Много раз пересиливал себя, находил мотивацию, выстраивал какие-то режимы и распорядки дня – и всё без толку.{w} Начинал биться головой об стену, мной же выстроенную.{w} Но как только я расслабился, перестал насиловать себя - стало лучше, исчезло волнения о том, что будет завтра, что обо мне подумают и не пройдёт ли жизнь в пустую.{w} Плевать.{w} В реинкарнацию я не верю, в бога с дьяволом тоже. Осталось только «существовать» и ждать момента, когда всё закончится и потухнет экран… С каждым днем моей двадцатитрёхлетней жизни эта мысль становится только крепче.{p}{w}
    На часах 18:19 {p}{w} 
    И чего я опять философствую?{w} С такими мыслями и до петли недалеко… Эх, ладно. Уже немного опаздываю. Тем лучше - меньше сидеть придётся.{p}{w}
    Я оделся."
    $ set_mode_adv()
    
    th "Всё, пошёл на контакт с миром" 
    
    "Я выбрался из своего постсоветского подъезда и двинул на остановку 410-го автобуса."
    
    $ day_time()
    $ persistent.sprite_time = 'sunset'  
    scene bg bus_stop with dissolve
    
    "К счастью, жил я возле конечной, поэтому транспорт приходил относительно вовремя и без пассажиров."
    
    stop music
    
    $ day_time()
    $ persistent.sprite_time = 'sunset'
    play sound sfx_bus_stop  
    scene bg bus_stop with dissolve
   
    "Подъехал пустой 410-й."
    
    $ day_time()
    $ persistent.sprite_time = 'sunset'
    play sound sfx_bus_interior_moving 
    scene bg intro_xx with dissolve
   
    "Войдя, я уселся где-то посередине, у окна.{w} Наушники в уши, поехали." 
    "За окном пролетали серые, казалось бы, уже отслужившие своё блеклые здания, разнились они лишь магазинами, кафешками, салонами и прочими заведениями на первых этажах."
    "Каждая вывеска как будто пыталась быть ярче других.{w} На фоне советских шедевров архитектуры вид был, мягко говоря, так себе."
    "А может стоит переехать, если мне тут не нравиться? {w}Была ж ведь такая мысль и раньше." 
    "Другую страну я вряд ли потянул бы, но город вполне, а район уж точно.{w} Однако сейчас совершенно нет желания этим заниматься, похоже виною всему моя абсолютная прокрастинация."
    "С первого своего рабочего дня деньги на счету хоть и не преумножались, но непрерывно, малу-помалу скапливались." 
    "Тратился я не шибко много. Раз в год купить то ли процессор, то ли видеокарту, либо заменить что-то с периферии."
    "Раз в месяц заплатить за коммуналку, интернет, прикупить пару книг и что-нибудь поесть.{w} Большего мне как обычно не хотелось." 
    "Из-за моего сбившегося режима сна, (а точнее его отсутствия) меня начало клонить в сон, однако вздремнуть в транспорте я не боялся, так как по неведомой мне силе, организм всегда просыпался за одну-две остановки до выхода."
    "Не прошло и пяти минут моего самокопания как я задремал."  
    
    show blink
    
    stop sound
    
    play sound sfx_intro_bus_transition
    
    $ renpy.movie_cutscene("Azure_summer/OP/op1.webm")

    jump EvSuDAY_1
