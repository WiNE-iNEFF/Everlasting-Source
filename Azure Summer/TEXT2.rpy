init:

    image mi smile long hair night = im.MatrixColor( im.Composite((600,720), (0,0), "Azure_summer/sprites/normal/mi/mi_3_body_loo.png",(0,0), "Azure_summer/sprites/normal/mi/mi_3_casual.png",(0,0), "Azure_summer/sprites/normal/mi/mi_3_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) )    #modded: image mi smile long hair night = im.MatrixColor( im.Composite((900,1080), (0,0), "Azure_summer/sprites/normal/mi/mi_3_body_loo.png",(0,0), "Azure_summer/sprites/normal/mi/mi_3_casual.png",(0,0), "Azure_summer/sprites/normal/mi/mi_3_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) )

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
    
    image bg cum_hata_day = "Azure_summer/bg/cum_hata_day.jpg"
    
    image bg cum_hata_sunset = "Azure_summer/bg/cum_hata_sunset.jpg"
    
    image bg ext_playground_sunset = "Azure_summer/bg/ext_playground_sunset.jpg"
    
label EvSuDAY_2: 
    $ backdrop = "days"
    $ new_chapter(2, u"День второй.")
    
    $ day_time()
    $ persistent.sprite_time = 'day'
    
    play ambience ambience_int_cabin_day fadein 1
    
    scene bg cum_room_day with dissolve 
    
    "Проснулся,{w} встал,{w} взглянул на часы – 6:56."
    
    th "Давно я так рано не просыпался."
    
    "Сел обратно на кровать, уставившись взглядом в никуда, параллельно думая, что делать.{w} Линейка начинается в 8."
    "Идти на неё нет ни малейшего желания, а потому нужно где-то отсидеться."
    "Раз уж я так рано проснулся, пойду умоюсь и почищу зубы.{w} Знать бы только куда идти.{w} Буду искать «на ощупь»."
    
    play sound sfx_open_door_2
    
    play ambience ambience_camp_center_day fadein 1
    
    scene bg ext_houses_day with dissolve
    
    "Взял пакетик, оставленный вожатой, полотенце и вышел на улицу.{w} Шёл и думал."
    "Мне точно что-то снилось, что-то интересное. Вспомнить бы что."
    "Из раздумий меня вывел голос за спиной."

    sl "Доброе утро!"
    
    show sl smile sport with dissolve
    
    "Она поравнялась со мной."
    
    "Славя, была в обтягивающем спортивном костюме, очень привлекательном,{w} да и чёрный цвет был ей к лицу."
    
    me "Доброе."
    
    sl "Ты чего так рано?{w} Ещё минимум полчасика можно спать."
    
    me "Да как-то просто выспался уже.{w} Ты часом не знаешь где тут можно умыться?"
    
    sl "Знаю конечно, идём, мне тоже туда."
    
    me "А ты почему так рано?"
    
    sl "Для меня не рано, а в самый раз.{w} Я всегда начинаю утро с пробежки."
    
    me "То есть в этом лагере принудительной зарядки нету?"
    
    sl "Есть конечно.{w} А пробежки нету, вот я сама и бегаю.{w} Тебе спорт не нравится?"
    
    me "Нравится, но в своём порядке, а не принудительном."
    
    sl "Придётся потерпеть."
    
    scene bg ext_washstand_day with dissolve
    
    show sl smile sport with dissolve
    
    sl "Вот рукомойники, а дальше за ними душевые.{w} Ещё есть баня, могу как-нибудь показать."
    
    me "Спасибо."
    
    play sound sfx_open_water_sink
    
    scene bg ext_washstand2_day with dissolve
    
    "Я почистил зубы и умылся, холодной водой само собой;{w} раздалась мелодия."
    
    play sound sfx_close_water_sink
    
    play sound sfx_dinner_horn_processed
    
    scene bg ext_washstand_day with dissolve
    
    show sl smile sport with dissolve
    
    me "Это к чему?"
    
    sl "Подъём, уже видимо пол восьмого."
    
    me "Зачем тогда вожатая просила меня завести будильник, если есть общий?"
    
    hide sl with dissolve
    
    show sl smile2 sport with dissolve
    
    sl "Видимо ей просто нравиться над тобой подшучивать."
    
    me "Похоже на то. Ладно, я пойду."
    
    sl "Хорошо, только про линейку не забудь."
    
    hide sl with dissolve
    
    scene bg ext_houses_day with dissolve
    
    "Я думал вернуться к себе и полчасика попялиться в потолок, но встретил кибернетиков."
    
    show el normal pioneer at cleft with dissolve
    
    show sh normal pioneer at cright with dissolve
    
    sh "Привет, товарищ!{w} Ты что пораньше встал?"
    
    me "Так получилось.{w} Слушайте, а на линейку обязательно являться?"
    
    el "Да, хоть её здесь и никто не любит.{w} Такие правила."
    
    me "А если всё же не прийти?"
    
    sh "То очень расстроишь Ольгу Дмитриевну.{w} Алиса с Ульяной пробовали пару раз,{w} потом вожатая их или на кухне оставляла картошку чистить,{w} или территорию убирать."
    
    me "Спасибо, учту."
    
    el "Ага, давай не опаздывай."
    
    scene bg cum_room_day with dissolve 
    
    play sound sfx_open_door_2
    
    play ambience ambience_int_cabin_day fadein 1
    
    "Вернувшись в домик и повалявшись пару минут на кровати,{w} я все решил сходить на линейку.{w} Соц. работы меня не привлекали."   
    
    play ambience ambience_camp_center_day fadein 1
    
    scene cg d2_lineup with dissolve
    
    "На площади все выстроились в ровные ряды.{w} Ольга Дмитриевна огласила распорядок дня.{w} Затем пригласила желающего провести утреннюю зарядку,{w} но из-за недостатка добровольцев пришлось просить Славю. "

    "Большинство пионеров, включая меня, шевелили конечностями просто для галочки,{w} а стараться начинали лишь поймав на себе взгляд вожатой.{w} После этого звук из громкоговорителя уведомил о начале завтрака."
    
    play sound sfx_dinner_horn_processed
    
    scene bg ext_dining_hall_away_day with dissolve
    
    "На пути в столовую ко мне присоединились Мику и Лена."
    
    show un smile pioneer at cleft with dissolve
    
    show mi smile pioneer at cright with dissolve
    
    mi "Доброе утро, Семён!{w} Как спалось на новом месте?"
    
    me "Я хорошо выспался и довольно рано проснулся."
    
    mi "А мы вот чуть не проспали, почти пол ночи проболтали…{w} А, в общем, не важно."
    
    hide un with dissolve
    
    show un grin pioneer at cleft with dissolve
    
    "Лена тихонько хихикнула." 
    
    hide un with dissolve
    
    show un smile pioneer at cleft with dissolve
    
    un "Позавтракаем вместе?"
    
    me "Давайте."

    play ambience ambience_dining_hall_full fadein 1
    
    scene bg int_dining_hall_people_day with dissolve
    
    show un normal pioneer at cleft with dissolve

    show mi normal pioneer at cright with dissolve
    
    "Мы втроём заняли столик."
    
    mi "На пляж идёшь?"
    
    me "Наверное.{w} Разве у меня есть выбор?"
    
    mi "А ты что, не хочешь?"
    
    me "Да как-то не особо."
    
    mi "Почему?{w} Солнце, песочек, водичка.{w} Разве не здорово?"
    
    me "Может быть."

    mi "Тем более вчера не ходили,{w} сегодня точно нельзя упускать такую возможность!"
    
    "Всё это она говорила с таким блеском в глазах, что спорить с ней было невозможно.{w} А что?{w} Может действительно сама вселенная дала мне возможность начать жизнь заново.{w} Раз есть такая возможность, почему хотя бы не попробовать?"
    
    me "А знаешь, ты, наверное, права."
    
    "И вправду.{w} Сам не заметил, как смотря на Мику начал лыбиться.{w} Стало неловко."
    
    mi "Ты, кстати, не встречал Алису и Ульяной?"
    
    me "С вчерашнего дня нет, а что?"
    
    mi "Мы с Леной их тоже не видели, интересно просто где они."
    
    un "Может, как раз пытаются заработать себе на исправительный срок."
    
    mi "Такое возможно.{w} Хотела Ульку попросить мяч у кого-то из младших одолжить."
    
    me "Забываю спросить всё,{w} почему Ульяну в этот отряд определили?{w} Разве она не младше нас?"
    
    un "Она всего на год младше нас с Мику,{w} просто выглядит так, вот и всё." 
    
    "Спрашивать сколько им лет я не решился.{w} Но осмелюсь предположить, что в районе 16."
    
    un "Ну я позавтракала.{w} Меня Женя звала с утра зайти в библиотеку.{w} Поэтому я пошла, а ты, Мику, составь компанию Семёну."
    
    mi "Стой, я тоже почти всё.{w} Я с тобой пойду, может помощь понадобиться.{w} Сень если хочешь идём с нами."
    
    hide un with dissolve
    
    show un smile pioneer at cleft with dissolve
    
    un "Ми-ку.{w} Мы с Женей сами справимся.{w} Ты забыла о чём мы вчера говорили?"
    
    mi "Да нет, причем тут это, просто…"
    
    un "Всё, я пошла."
    
    "Перебила её Лена и быстро удалилась."
    
    hide un with dissolve
    
    hide mi with dissolve
    
    show mi normal pioneer at center with dissolve
    
    th "Ничего не понял, но ладно."
    
    "Доедали молча. Повисла неловкая пауза."
    
    th "Что же мне у неё спросить?"
    
    me "Слушай, не хочешь пройтись куда-нибудь?{w} Вы вчера мне так всё и не показали."
    
    hide mi with dissolve
    
    show mi smile pioneer at center with dissolve
    
    mi "Да, конечно, идём.{w} Сама думала предложить."
    
    hide mi with dissolve
    
    play ambience ambience_camp_center_day fadein 1
    
    scene bg ext_dining_hall_near_day with dissolve
    
    "На выходе из столовой нас перехватила Славя."
    
    show mi normal pioneer at cleft with dissolve
    
    show sl normal pioneer at cright with dissolve
    
    sl "О, Семён, ты вовремя.{w} У меня есть просьба."
    
    me "Какая?"
    
    sl "Только что привезли различные медикаменты, нужно это всё отнести в медпункт, Виола уже ждёт.{w} Я бы сама, но ещё даже не завтракала."
    
    me "Да не вопрос.{w} Откуда брать?"
    
    hide sl with dissolve
    
    show sl smile pioneer at cright with dissolve
    
    sl "Спасибо большое.{w} Возле лагерных ворот стоят две коробки, не пропустишь.{w} Мику, может с ним сходишь?{w} Покажешь дорогу в медпункт, если он там ещё не был."
    
    mi "Да, с удовольствием.{w} Мы тогда пошли."
    
    scene bg ext_houses_day with dissolve
    
    show mi normal pioneer at center with dissolve
    
    me "Слушай, я могу сам справиться. Можешь идти к Лене."
    
    mi "Да всё нормально.{w} Я с радостью помогу тебе."
    
    me "Если что, можешь говорить мне как есть, я не обижусь. Тем более вы вчера что-то обговаривали, не нужно из-за меня свои планы рушить."
    
    hide mi with dissolve
    
    show mi dontlike pioneer at center with dissolve
    
    mi "Я же сказала, что всё нормально!{w} Никуда я не уйду.{w} Говорю как есть.{w} Ничего мы вчера не планировали.{w} Может, я просто хочу узнать тебя получше."
    
    me "В смысле, узнать получше?"
    
    hide mi with dissolve
    
    show mi shy pioneer at center with dissolve
    
    mi "А?{w} Ничего не значит.{w} То есть, просто, может будем друзьями, ну, если ты хочешь, конечно."
    
    me "Я не против быть друзьями."
    
    hide mi with dissolve
    
    show mi surprise pioneer at center with dissolve
    
    mi "Правда!? "
    
    me "Конечно."
    
    th "Кажется она мне даже нравится."
    
    stop ambience
    
    play ambience ambience_camp_entrance_day fadein 1
    
    scene bg ext_camp_entrance_day with dissolve

    show mi normal pioneer far at center with dissolve
    
    mi "Наверное о них говорила Славя."
    
    "Она указала на две коробки рядом с воротами и схватила одну из них.{w} Я тоже подобрал одну."
    
    me "Я могу взять обе."
    
    mi "Нет.{w} Друзья должны делиться поровну.{w} Так что идём, покажу где медпункт."
    
    "Мы пошли."
    
    stop ambience
    
    play ambience ambience_camp_center_day fadein 1
    
    scene bg ext_aidpost_day with dissolve
    
    show mi normal pioneer far at center with dissolve
    
    mi "Сразу предупрежу, наша медсестра немного необычная, поэтому не удивляйся."
    
    me "Что значит необычная?"
    
    th "Что ещё может быть необычного после прошедших двух дней?"
    
    mi "Она не ведёт себя как обычный взрослый, как Ольга Дмитриевна, например.{w} Виолетта Церновна часто бывает фамильярной и может говорить загадками или двусмысленными фразами.{w} Но несмотря на это, она хороший врач."
    
    me "Хорошо, буду иметь ввиду."
    
    stop ambience
    
    play ambience ambience_medstation_inside_day fadein 1

    scene bg int_aidpost_day with dissolve
    
    play sound sfx_medpunkt_door_open

    show mi normal pioneer at cleft with dissolve
    
    show cs smile at cright with dissolve
    
    mi "Доброе утро!"

    me "Доброе утро,{w} Виолетта Церновна?{w} Это к вам просили отнести."
    
    hide cs with dissolve
    
    show cs shy at cright with dissolve
    
    cs "Для тебя, дорогой мой, только Виола.{w} Или ты намекаешь, что я старая?"
    
    me "Да нет, что вы.{w} Виола, так Виола."
    
    hide cs with dissolve
    
    show cs smile at cright with dissolve
    
    cs "Ты мне нравишься!{w} Быстро схватываешь.{w} Твои товарищи обычно спорят и отнекиваются.{w} Ставьте уже коробки куда-нибудь.{w} Как тебя зовут, пионер?"
    
    me "Семён."
    
    cs "Сеня значит.{w} Проходи дорогой, садись на койку, начнём осмотр.{w} Мику, закрой дверки, чтобы нам не мешали,{w} можешь с этой стороны, если тебе интересно поприсутствовать."
    
    "Мой инстинкт самосохранения забил тревогу."
    
    th "С этой женщиной опасно оставаться один на один."
    
    hide mi with dissolve
    
    show mi rage pioneer at cleft with dissolve
    
    "Я перевел взгляд на Мику.{w} Не собирается ли она меня оставить на растерзание этому доктору.{w} Внезапно для меня, она перешла на повышенный тон."
    
    mi "Виола, хватит уже соблазнять пионеров!{w} Вы ко всем пристаёте!{w} Как вы так можете?{w} Нельзя так себя вести, тем более на рабочем месте!{w} Что вы себе позволяете!?"
    
    cs "Ха-ха-ха! Как завелась. Ладно-ладно, так бы и сказала, что он твой."
    
    mi "Вы опять?"
    
    cs "Ну всё, всё.{w} Спокойно.{w} Но осмотреть я его всё равно должна, мало ли заразу какую-нибудь в лагерь привёз.{w} Присаживайся на стул, осмотрю тебя."
    
    hide mi with dissolve
    
    hide cs with dissolve
    
    stop ambience
    
    play music music_list ['gentle_predator'] fadein 1
    
    scene cg d5_cs with dissolve
    
    th "Специально ведь так делает?{w} Что у нее в голове?"
    
    mi "Семён, я снаружи постою."
    
    cs "Открывай широко рот, говори АААА"
    
    me "АААА"
    
    cs "Так, теперь расстегни рубашку, я тебя послушаю.{w} Так, хорошо.{w} По-моему, здоров."
    
    stop music
    
    play ambience ambience_medstation_inside_day fadein 1
    
    scene bg int_aidpost_day with dissolve
    
    show cs normal at center with dissolve
    
    "Я встал, застегивая рубашку."
    
    me "Спасибо, я пойду тогда."

    cs "Погоди, не спеши.{w} Если понадобятся, скажем, средства контрацепции - приходи, не стесняйся."
    
    me "Спасибо, думаю не понадобятся.{w} Не переживайте."
    
    cs "Я сейчас не шучу, а вполне серьёзно.{w} Мне кажется ты ей нравишься, вон как вспыхнула от моего флирта.{w} А ты, что о ней думаешь?"
    
    me "Я?{w} Да… ничего…{w} Вы к чему это вообще?{w} Вам какая разница, что я думаю?"
    
    hide cs with dissolve
    
    show cs smile at center with dissolve

    cs "Ладно, иди уже.{w} Но если что-то понадобится - обращайся.{w} Всего доброго!"
    
    me "И вам. До свидания."
    
    stop ambience
    
    play ambience ambience_camp_center_day fadein 1
    
    scene bg ext_aidpost_day with dissolve
    
    show mi normal pioneer at cleft with dissolve
    
    show us normal pioneer at cright with dissolve
    
    "Я вышел на улицу, где стояла Мику с Ульяной."
    
    us "Ну как?{w} Прошёл осмотр?"
    
    me "Да.{w} А ты почему здесь?"
    
    us "Живот что-то побаливает, пришла к Виоле за таблеткой."

    mi "Где вы с утра с Алисой были?{w} Я сначала хотела к вам зайти, но потом как-то из головы вылетело."
    
    hide us with dissolve
    
    show us upset pioneer at cright with dissolve
    
    us "Немного проспали, не привыкли ещё к режиму.{w} Ольга Дмитриевна за это определила нас в обед на кухне помогать."
    
    mi "Не повезло вам.{w} Хочешь, я с вами пойду?{w} Втроём быстрее управимся."
    
    hide us with dissolve
    
    show us normal pioneer at cright with dissolve
    
    us "Спасибо Микуля, но мы сами как-нибудь.{w} К тому же у тебя всё с рук валится, кроме музыкальных инструментов.{w} Ну ладно, я пошла."
    
    hide us with dissolve
    
    hide mi with dissolve
    
    show mi dontlike pioneer at center with dissolve
    
    mi "Ничего у мня не валится из рук!!!"
    
    hide mi with dissolve
    
    show mi shy pioneer at center with dissolve

    mi "Слушай, всё у меня нормально с руками…{w} Может, у меня далеко не всё выходит, но я всегда очень стараюсь."
    
    me "Это главное."
    
    mi "Правда так думаешь?"
    
    me "Конечно.{w} Мне кажется ты очень способная."
    
    mi "Ой, да ладно тебе.{w} Скажешь тоже…"
    
    me "Говорю как есть."
    
    hide mi with dissolve
    
    show mi smile pioneer at center with dissolve 
    
    mi "Спасибо.{w} Ладно!{w} Пора на пляж собираться.{w} Идём?"
    
    me "Да, пошли."
    
    scene bg cum_hata_day with dissolve
    
    show mi normal pioneer with dissolve
    
    "Мы пошли к своим домикам и остановились возле моего."
    
    mi "Как переоденемся встретимся здесь?"
    
    me "Хорошо."
    
    stop ambience
    
    play ambience ambience_int_cabin_day fadein 1
    
    scene bg cum_room_day with dissolve
    
    play sound sfx_open_door_2

    "Я вошёл в домик, натянул плавки, подброшенные Ольгой Дмитриевной.{w} Процедура заняла меньше минуты.{w} Мику наверняка только зашла к себе и переодеваться ей явно дольше чем мне.{w} Я решил пару минут посидеть. "
    
    th "Аж не терпится увидеть её в купальнике. Больше, чем кого-либо из девочек."
    
    "Она меня действительно зацепила.{w} Открытая, искренняя.{w} Даже наивная как ребёнок, но эта её наивность сплошная милота.{w} И внешностью природа её не обделила." 
    "Взяв полотенце под руку, я вышел на улицу."
    
    stop ambience
    
    play ambience ambience_camp_center_day fadein 1
    
    scene bg cum_hata_day with dissolve
    
    "Через минуту увидел вдалеке Мику, вышедшую из своего домика,{w} и она с улыбкой пошла ко мне на встречу."
    
    show mi normal pioneer far at center with dissolve

    hide mi with dissolve
    
    show mi normal pioneer at center with dissolve

    mi "Долго ждёшь?{w} Я старалась побыстрее."
    
    me "Нет, только вышел.{w} Идём?"
    
    mi "Ага.{w} Окунуться побыстрее бы, жара невыносимая."
    
    scene bg ext_square_day with dissolve
    
    mt "Так, почти все в сборе.{w} Ждём ещё Лену с Женей."
    
    show mi normal pioneer at center with dissolve
    
    show dv smile pioneer at fright with dissolve
    
    show us smile pioneer at fleft with dissolve
    
    dv "А чё это вы вдвоём пришли?{w} Где были?{w} Чем занимались?"
    
    hide mi with dissolve
    
    show mi shy pioneer at center with dissolve
    
    mi "Да что ты себе уже придумала?"
    
    us "Действительно, чего ты, Алис?{w} Тебе-то какое дело?{w} Не лезь куда не просят."
    
    hide dv with dissolve
    
    show dv grin pioneer at fright with dissolve
    
    dv "Мику, а что есть куда влезть?{w} Просто интересно."

    hide mi with dissolve
    
    show mi dontlike pioneer at center with dissolve
    
    mi "Да что вы заладили!"
    
    "Воспользовавшись их диалогом, я отошёл к кибернетикам,{w} которые очень увлечённо следили за происходящим."
    
    hide us with dissolve
    
    hide mi with dissolve
    
    hide dv with dissolve
    
    show el normal pioneer at cleft with dissolve
    
    show sh normal pioneer at cright with dissolve
    
    me "Привет."
    
    el "Привет, друг."
    
    sh "Что, тяжко в женском коллективе?"
    
    me "Не особо.{w} А что?"
    
    el "Да так.{w} Есть планы завтра на вечер?"
    
    me "Ты имеешь ввиду танцы или дискотеку?{w} Как у вас принято говорить?"
    
    sh "Без разницы. Так есть что-то на уме?"
    
    me "Не особо."
    
    mt "Так!{w} Все в сборе.{w} Разбиваемся на пары и дружно идём на пляж."
    
    hide el with dissolve
    
    hide sh with dissolve
    
    "Все быстро нашли себе компаньона:{w} Славя, во главе колоны с вожатой, Лена с Женей, Алиса с Ульяной, кибернетики, ну и я с Мику."
    
    stop ambience
    
    play ambience ambience_lake_shore_day fadein 1
    
    scene bg ext_beach_day with dissolve
    
    "Спустя несколько минут мы пришли на пляж. Расстелив полотенце и сбросив с себя одежду, я принялся осматривать местность вокруг."
    
    show mi shy swim at center with dissolve
    
    "Ко мне подошла Мику. Выглядела она потрясающе. Мы молча смотрели друг на друга. Наконец она прервала молчание."
    
    mi "Идёшь плавать?{w} Ульянка мяч принесла."
    
    me "Да, сейчас иду."
    
    hide mi with dissolve
    
    "Мику пошла вперёд, а рядом со мной из неоткуда появилась Лена."
    
    show un smile swim at center with dissolve
    
    un "Ты должен был сказать, что ей идёт купальник,{w} или что она хорошо выглядит."
    
    me "Да что-то я, это самое…{w} Не знаю."
    
    un "Думаю у тебя будет ещё возможность."
    
    "Она хихикнула."
    
    hide un with dissolve
    
    "Может и ей стоило такое сказать?{w} Она тоже хорошо выглядит.{w} Хотя не знаю, что-то сложно это всё.{w} Пора окунуться."
    "Проплавав минут 5, мы с остальными перебросились мячом, побрызгались и подурачились.{w} Это, с непривычки, меня очень утомило."
    "Я выбрался на берег, оделся.{w} Выбрав удобный момент, ушёл."
    "Может стоило уведомить вожатую,{w} но мне не хотелось привлекать к себе ещё больше внимания."
    
    stop ambience
    
    play ambience ambience_soccer_play_background fadein 1
    
    scene bg ext_playground_day with dissolve
    
    "Ноги завели меня на стадион.{w} Присев на землю под деревом, я начал размышлять."
    
    "Столько всего происходит и я не успеваю даже задуматься об этом всём как следует.{w} Вряд ли я найду причину моего попадания сюда.{w} Но мне кажется, что я здесь не навсегда."
    
    "Даже не кажется.{w} Я чувствую это.{w} Не знаю почему.{w} Как будто что-то тянет меня обратно."
    
    "Именно поэтому я не хочу заводить здесь “новую жизнь”.{w} Может вместе с концом смены закончится и мое пребывание в этом лагере."
    
    "Однако к одному человеку меня тянет.{w} Больше, чем к кому-либо.{w} Это – Мику."
    
    "Два неполных дня знакомы и уже влюбился.{w} Прям как подросток, коим по факту я сейчас и являюсь."
    
    "Я не знаю стоит ли мне с ней заводить отношения.{w} Потому что в один момент я могу просто исчезнуть так же, как и появился.{w} Стоит попробовать."
    
    "Но не сказать же ей что могу однажды просто пропасть навсегда.{w} Ничего не рассказать тоже не могу.{w} Если я просто исчезну, неверное подумает, что для меня она не была важна.{w} Мерзкое чувство от такого сценария."
    
    "Впрочем, может она вовсе не испытывает ко мне того же, что я к ней."
    
    "Безвыходная ситуация. Но глупо было бы тратить вторую жизнь просто следуя за течением."
    
    "Это у меня было в первой.{w} К ней я могу вернуться в любой момент.{w} Значит…"
    
    "Надо мной нависла тень."
    
    play music music_list['forest_maiden'] fadein 1
    
    show un normal sport at center with dissolve

    un "Что-то случилось?{w} Грустный какой-то сидишь."
    
    me "Ничего.{w} Просто задумался."
    
    un "Можно присесть рядом?"
    
    me "Пожалуйста."
    
    hide un with dissolve
    
    show un normal sport close at center with dissolve
    
    un "Хочешь поговорить?{w} Если я ничем и не помогу, то другое мнение может подтолкнуть тебя к нужному решению."
    
    me "Даже не знаю как сказать.{w} Понимаешь, до лагеря у меня был совершенно другой образ жизни.{w} Попав сюда, я думаю стоит ли что-то менять.{w} Пробовать жить иначе."
    
    un "Банально было бы ответить – конечно.{w} А что тебе здесь нравиться?"
    
    me "Атмосфера.{w} Лёгкая и непринуждённая.{w} Хотя, рано или поздно нужно будет уезжать.{w} Не буду же я тут вечно."
    
    un "Это как посмотреть."
    
    me "То есть?"
    
    un "Сохрани эту атмосферу внутри себя и живи с ней, где б ты не был."
    
    me "Может ты и права."
    
    hide un with dissolve
    
    show un smile sport close at center with dissolve
    
    un "Буду рада, если помогла."
    
    "Посидев пару минут, Лена нарушила тишину."
    
    un "Ты ушёл, потому что не нравится проводить время в большой компании?"
    
    me "Я бы сказал некомфортно."
    
    un "Если надумаешь ещё уходить, предупреждай Ольгу Дмитриевну.{w} Она может казаться строгой, но всегда идёт на встречу."
    
    me "Забыл сказать ей, извини."
    
    un "Я тут при чём?{w} Перед ней извиняться будешь."

    me "Точно.{w} А ты почему сюда пришла?"
    
    un "Люблю воланчик побросать.{w} Увидела тебя скучающего и решила подойти."
    
    me "Одна в бадминтон играешь?"
    
    un "Тебя это удивляет?"
    
    me "Да нет.{w} Понимаю даже."
    
    un "Я люблю о чём-то одна задуматься.{w} А ракетка что-то вроде чёток, руки занять."
    
    hide un with dissolve
    
    stop music fadeout 1
    
    "Мы продолжили сидеть в тишине.{w} Смотрели на колышущиеся высокие деревья, плывущие облака и бегающих по площадке пионеров."
    
    "Хоть Лену я знаю чуть ли не меньше всех остальных девочек в лагере, с ней сидеть было в удовольствие.{w} И пока мы общались, она умело подбирала слова."
    
    "Я повернул к ней голову – она уснула.{w} Не было никакого желания её так оставлять.{w} Через какое-то время глаза начали слипаться."
    
    show blinking
    
    "Не дал мне погрузиться в сон раздражающий звук."
    
    play sound sfx_dinner_horn_processed
    
    "Всю сонливость сняло как рукой."
    
    th "Если дьявол существует, это явно его изобретение."
    
    show un shy sport close at center with dissolve
    
    un "Ой, я что, уснула?"
    
    "Она залилась румянцем.{w} Не дожидаясь ответа, она улыбнулась и продолжила."
    
    hide un with dissolve
    
    show un smile sport close at center with dissolve
    
    un "Спасибо, что не оставил беззащитную девушку одну."
    
    me "Я и сам чуть не задремал.{w} Не за что благодарить."
    
    un "Но ты ведь мог уйти?"
    
    "Я только отвел глаза в сторону.{w} Она, снова не дожидаясь ответа, продолжила."
    
    un "Надеюсь нас никто не видел из отряда, а то слухи пойдут, страшно представить какие."
    
    me "Даже думать не хочу об этом."
    
    un "Пусть это будет наш секрет."
    
    me "Согласен."
    
    "Мы не спеша отправились в столовую."
    
    stop ambience
    
    play ambience ambience_camp_center_day fadein 1
    
    scene bg ext_houses_day with dissolve
    
    "Секрет секретом, но не расскажет ли она об этом Мику?{w} Они, конечно, подруги, но я понятия не имею как у девочек устроены секреты."
    
    "Ещё моя обеспокоенность только подтверждает мне, что Мику для меня не безразлична."
    
    stop ambience
    
    play ambience ambience_dining_hall_full fadein 1
    
    scene bg int_dining_hall_people_day with dissolve
    
    "Ни возле и ни внутри столовой я не встретил вожатую.{w} Это не может не радовать.{w} Лучше получить выговор один на один, чем у всех на виду.{w} Зато основной источник звука в помещении Ульяна и её рыжая подруга на месте."
    
    "Они сидели за одним столом со Славей и Женей.{w} Я бы сказал это самое странное сочетание характеров в одном месте."
    
    "За дальним столиком у окна сидели Шурик с Электроником. Взяв себе поднос с едой, Лена пошла за столик к девочкам, а я отправился к “браткам”."
    
    me "Разрешите присоединиться?"
    
    show el normal pioneer close at left with dissolve
    
    show sh normal pioneer close at right with dissolve
    
    sh "Конечно, присаживайся."
    
    "Я сел."
    
    el "Всё нормально? Ты смылся рановато."
    
    me "Всё нормально, утомился немного, вот и ушёл."
    
    sh "От чего утомился?{w} Плескаться в воде и лежать на солнышке, но дело твоё."
    
    el "Можешь сказать, что задолбался. Все свои."
    
    me "Я бы сказал это не мой стиль отдыха."
    
    el "Понимаю, я бы предпочёл продолжить работу над рацией."
    
    sh "Согласен, может мы на пороге чего-то великого.{w} Но приходится хлюпаться в речке."
    
    hide el with dissolve
    
    show el grin pioneer close at left with dissolve
    
    el "Дааа, хотя и на красивых девочек в купальниках тоже не грех иногда полюбоваться."
    
    hide sh with dissolve
    
    show sh normal_smile pioneer close at right with dissolve
    
    sh "И это правда."

    me "Так рацию уже придумали.{w} Разве нет?"
    
    hide el with dissolve
    
    hide sh with dissolve
    
    show el normal pioneer close at left with dissolve
    
    show sh normal pioneer close at right with dissolve
    
    el "Да.{w} Только мы работаем над новой моделью.{w} Может даже над следующей её ступенью, если так можно выразиться."
    
    me "Объясните."
    
    sh "Смотри.{w} Представь, что у рации нет ограничения по дальности.{w} Точнее, настроить её дальность связи на территорию всей страны и раздать всем желающим.{w} Проще говоря, это телефон без провода и в идеале меньший в размерах.{w} Правда пока у нас это на стадии планирования."
    
    "Ничего себе.{w} Знал бы он, что описывает мобильный телефон."
    
    el "Ну как тебе идея?"
    
    me "Слушай, а неплохо придумано.{w} Звучит интересно."
    
    sh "А то! Я же говорил тебе к нам нужно вступать."
    
    hide el with dissolve
    
    hide sh with dissolve
    
    "Мы доели.{w} Потом разошлись." 
    
    stop ambience
    
    play ambience ambience_int_cabin_day fadein 1
    
    scene bg cum_room_day 
    
    "Я пошёл к себе в домик, завалился на кровать и решил подремать."
    
    show blink
    
    play sound sfx_knock_door2
    
    "Стоило мне закрыть глаза, как раздался стук в дверь."
    
    th "Неужели вожатая таки меня вычислила?"
    
    show unblink 
    
    play sound sfx_open_door_2

    stop ambience
    
    play ambience ambience_camp_center_day fadein 1

    scene bg cum_hata_day with dissolve
    
    show un normal pioneer with dissolve
    
    un "Не отвлекаю?"
    
    me "Нет.{w} Что-то случилось?"
    
    un "Хм… С чего бы начать?{w} Разговор у меня не простой.{w} Тебе будет проще прогуляться или мне зайти?"
    
    me "Проходи раз дело серьёзное."
    
    stop ambience
    
    play sound sfx_open_door_2
    
    play ambience ambience_int_cabin_day fadein 1
    
    scene bg cum_room_day 
    
    "Мы сели за столик у окна."
    
    show un normal pioneer close with dissolve
    
    me "Ну, рассказывай."
    
    un "Ты заметил, что Мику не было после пляжа?"
    
    me "Да."
    
    un "В общем, когда ты слинял, через минут пятнадцать она отпросилась у вожатой на площадку.{w} Дальше ты знаешь."
    
    me "Ближе к делу.{w} Не пойму к чему ты ведёшь."
    
    un "Так вот. Мику увидела, как мы по очереди уходим и её это заинтересовало,{w} и она пошла за нами и увидела, как мы, с её слов: “Мило беседовали под деревом”."
    
    un "Она очень расстроилась и с тех пор сидит подавленная в нашем домике."
    
    me "Ну, во-первых, мы с тобой просто разговаривали,{w} а во-вторых, почему это её так задело?"
    
    "Мне кажется я уже знаю ответ."
    
    hide un with dissolve
    
    show un smile pioneer close with dissolve
    
    un "Потому что ты ей нравишься, балда.{w} Ты, конечно, не обязан отвечать взаимностью, но выполни мою просьбу.{w} Иди поговори с ней, чтобы девочка не страдала."
    
    un "Сделаешь?"
    
    me "Я схожу к ней.{w} Только дай мне пару минут."
    
    un "Спасибо.{w} Я пойду тогда."
    
    hide un with dissolve
    
    play sound sfx_open_door_2
    
    "Вот так новости.{w} Даже не верю, что со мной такое может произойти.{w} Чтобы я нравился девушке, а она мне."
    
    "Хоть это и так, пойти к ней и заговорить об этом проще не становиться.{w} Но раз уж я решил воспринимать свою телепортацию как вторую жизнь, то почему я до сих пор здесь?"
    
    "Вперёд."
    
    stop ambience
    
    play ambience ambience_camp_center_day fadein 1
    
    scene bg ext_houses_day with dissolve
    
    "Я пошёл к Мику.{w} Шёл как можно медленнее, по дороге подбирая слова.{w} Хоть и знаю, что бы я не запланировал, всё пойдет не по плану."
    
    scene bg ext_house_of_un_day with dissolve
    
    "И вот я на пороге, стучусь."
    
    play sound sfx_knock_door2
    
    "Дверь открыла Мику."
    
    "Вид у неё действительно грустный.{w} Нет даже легкой улыбки.{w} В глазах нету привычного им блеска.{w} На белках видно красные вены."
    
    show mi dontlike pioneer far with dissolve
    
    mi "Привет.{w} Что-то нужно?"
    
    me "Да, хотел поговорить."
    
    mi "Говори."
    
    "В голове у меня каша из мыслей.{w} В груди всё сжалось, в руках легкая дрожь."
    
    "Первый раз у меня в жизни такая ситуация. Первый раз в обеих жизнях.{w} Поняв, что не смогу составить красивую речь, я решил сказать прямо."

    me "Мику, ты мне нравишься."
    
    hide mi with dissolve
    
    show mi shocked pioneer far with dissolve
    
    "Я приложил все усилия чтобы мой голос не дрожал и звучал уверенно."
    
    "Секундная пауза."
    
    mi "Что?{w} Ты о чём?"
    
    me "Ты как думаешь?"
    
    hide mi with dissolve
    
    show mi dontlike pioneer far with dissolve
    
    mi "Тебя Лена прислала?"
    
    me "Врать не буду, она заходила ко мне.{w} И её визит к сказанному мной не имеет никакого отношения.{w} А то, что ты видела на площадке - просто беседа.{w} Нравишься мне - ты."
    
    "Снова короткая пауза. На глазах Мику начали появляться слёзы."
    
    hide mi with dissolve
    
    show mi cry pioneer far with dissolve
    
    "Что я не так сказал?{w} От нервов и волнения хочется сквозь землю провалится."
    
    mi "И ты мне...{w} Тоже нравишься.{w} Мне очень жаль, что о моих чувствах ты узнал не от меня.{w} Нужно было самой всё сказать."
    
    me "Я прекрасно понимаю, как это сложно."
    
    mi "Однако мне сейчас сложно ответить тебе.{w} То есть ты мне тоже нравишься, но тебя прислала Лена…{w} И поэтому я не могу поверить, что ты говоришь искренне."
    
    mi "Пока не могу.{w}  Мне нужно время, ты так внезапно пришёл и в общем…{w} Мне нужно всё обдумать, и ты тоже подумай!"
    
    hide mi with dissolve
    
    play sound sfx_slam_door_campus
    
    "Она захлопнула передо мной дверь.{w} Сложно описать, что я сейчас чувствую."
    
    scene bg ext_houses_day with dissolve
    
    "Обратно я шёл ещё медленнее."
    
    scene bg cum_hata_day with dissolve
    
    "Возле своего домика я встретил Алису."
    
    show dv smile pioneer2 with dissolve
    
    dv "О! Я как раз к тебе шла.{w} Где ты пропадал?"
    
    me "Нигде.{w} Что ты хотела?"
    
    dv "Скучно просто, вот вас и искала."
    
    me "А Ульяна где?"
    
    dv "Играет с другими отрядами на стадионе."
    
    me "Так иди к ней."
    
    hide dv with dissolve
    
    show dv angry pioneer2 with dissolve
    
    dv "Слышь, что такое?{w}  Что я тебе сделала?"
    
    me "Ничего.{w} Я не в настроении."
    
    hide dv with dissolve
    
    "Сказал я, проходя мимо неё и добавил вслед."
    
    me "Если что Мику нет дома."
    
    dv "Да что вообще происходит!?"
    
    "Прокричала мне в спину Алиса, но я её проигнорировал."
    
    scene bg ext_houses_day with dissolve

    "К себе я не пошёл.{w} Вряд ли Алиса отстанет и мало ли кто ещё придёт."

    "Сначала я хотел найти укромное местечко, чтобы посидеть там и подумать о случившемся в одиночестве.{w} Но что тут думать?"
    
    "Идти ещё раз к Мику точно не стоит.{w} Нужно подождать пока она всё переварит, а там видно будет."
    
    scene bg ext_clubs_day with dissolve
    
    "Значит мне нужно скоротать время.{w} Так я и оказался на пороге у кибернетиков."
    
    stop ambience
    
    play ambience ambience_clubs_inside_day fadein 1
    
    play sound sfx_open_door_clubs
    
    scene bg int_clubs_male_day with dissolve
    
    me "Здорова."
    
    show el smile pioneer at left with dissolve
    
    show sh normal pioneer at right with dissolve
    
    el "Какая приятная неожиданность!"
    
    hide el with dissolve
    
    show el normal pioneer at left with dissolve
    
    el "Проходи.{w} Что кислый такой?"
    
    me "Сложились определённые обстоятельства."
    
    sh "Поделись тогда с нами, раз пришёл."
    
    "Мне вспомнились сегодняшние слова Лены про альтернативное мнение, и я решил им всё рассказать."
    
    sh "Поняяяяятно.{w} Но тут из меня такой себе помощник.{w} Серый, а ты что скажешь?"
    
    el "Я, конечно, не гуру в таких делах.{w} Но на твоем месте я бы ничего сейчас не делал.{w} Ждал бы пока она сама подойдёт, а если нет, то завтра сам подошёл бы и спросил, что да как."
    
    me "И я так же думаю сделать."
    
    sh "Может лучше если до завтра ничего не произойдёт?"
    
    me "То есть?"
    
    sh "Смотри.{w} Завтра дискотека.{w} Пригласишь её пойти с тобой, а там и романтика.{w} В общем разберётесь."
    
    me "А если она не согласится пойти?"
    
    el "Да согласится.{w} Девочки любят такое, вроде как.{w} К тому же, она тебя не отшила и не дала пощечину."
    
    hide sh with dissolve
    
    show sh upset pioneer at right with dissolve
    
    sh "Раз пошла такая беседа, то мне нравится Лена. Завтра хочу пригласить её на танец ну и… Вы поняли."
    
    hide el with dissolve
    
    show el surprise pioneer at left with dissolve
    
    el "Ничего себе, удивил."
    
    sh "Что такого?"
    
    el "Всё нормально, просто не думал, что тебе Лена нравится."
    
    sh "Ну вот как есть."
    
    hide sh with dissolve
    
    show sh normal_smile pioneer at right with dissolve
    
    sh "Сам-то будешь признаваться?"
    
    hide el with dissolve
    
    show el shocked pioneer at left with dissolve
    
    el "О чём ты?"
    
    "Электроник, сделал удивленный вид, за который ему можно Оскар выдать.{w} А мы продолжали пристально смотреть на него." 
    
    hide el with dissolve
    
    hide sh with dissolve
    
    show el normal pioneer at left with dissolve
    
    show sh normal pioneer at right with dissolve
    
    el "Ладно-ладно, сдаюсь.{w} Славя."
    
    me "И?"
    
    el "Что и?"
    
    me "Удиви нас своим оригинальным планом."
    
    el "Да какой план…{w} Такой же, как и у вас."
    
    me "Кстати, вы вообще танцевать умеете?"
    
    "Они отрицательно покачали головами."
    
    sh "На самом деле особо и не нужно уметь.{w} Беретесь за руки, ну как-то двигаетесь в такт музыке.{w} Главное же атмосфера.{w} А ну ещё важно по ногам девушке не топтаться, чтобы не убить эту атмосферу."
    
    me "Ты так уверенно это рассказываешь, на практике проверял?"
    
    sh "Один раз, в прошлом году.{w} Я тогда с Алисой танцевал.{w} Нас вожатая поставила вместе, как она сказала: “Чтобы никто не скучал”.{w} Но тем не менее мне понравилось, признаю."
    
    me "Получается и тебя запрягли? С кем был?"
    
    "Я посмотрел на Серёжу."
    
    el "Со Славей. Но, я бы не сказал, что тогда она мне нравилась. Да и…"
    
    me "Ты дал заднюю тогда."
    
    "Перебил я его."
    
    el "Да."
    
    "Честно сознался он."
    
    sh "На счёт заброшенного лагеря, в который мы идём после дискотеки."
    
    me "Так вы тоже идёте? Мне не говорили."
    
    el "Естественно."
    
    sh "Так вот, Семён, ты там ещё не был, поэтому рассказываю.{w} Там только одно здание и пройтись по нему всей нашей толпой будет не интересно."
    
    me "Ну да, никакого хоррора не будет."
    
    el "Чего не будет?"
    
    me "Страшной атмосферы."
    
    el "Сань, ты предлагаешь идти парами по очереди?"
    
    me "А по парам мы разобьёмся непосредственно на дискотеке?"
    
    sh "Схватываете на лету."
    
    me "План конечно красив, но что если что-то пойдёт не так?{w} Например, у кого-то не сложится."
    
    sh "Значит нам остается только не облажаться."
    
    me "Секундочку.{w} Серёж, ты в тот лагерь собрался со Славей идти?"
    
    el "Ну да.{w} А что?"
    
    me "Так она же у вожатой главная помощница или что-то в этом роде."
    
    el "Это ничего не значит.{w} Ты просто её мало знаешь.{w} Она никакая не “правильная” зануда.{w} Славя такая же, как и мы, просто помогает вожатой, не знаю она сама так захотела или её назначили,{w} но суть в том, что она не такая как тебе показалось."
    
    me "Извиняюсь, не знал. Её уже уведомили об этом походе?"
    
    el "Да, мы сказали ей, она идёт."
    
    sh "В таком случае с планом на завтра определились.{w} Хуже всего будет если кому-то одному откажут.{w} Даже думать об этом не хочу."
    
    el "Эт да.{w} Прогуляться никто не хочет?"
    
    me "Хорошая идея.{w} А куда?{w} По лагерю я не сильно хочу шататься."
    
    sh "Можно на один из островов сгонять."
    
    me "Куда-куда?"
    
    el "На один из островов.{w} Ты что не видел их с берега сегодня?"
    
    me "Видел, но вы что вплавь предлагаете?"
    
    sh "Нет, конечно.{w} На лодке."
    
    me "А где мы её возьмём?"
    
    sh "Сопрём."
    
    me "Ты предлагаешь украсть лодку?"

    el "Да расслабься, рядом с пляжем есть пристань со складом.{w} По плану там должен быть сторож, но его нет.{w} Пришёл, сел, поплыл.{w} Главное вожатой на глаза не попасться."
    
    "Признаться, эти двое меня удивили.{w} Я не особо верил в примерных и порядочных пионеров, но такого не ожидал." 
    
    me "Ну пошли, раз всё так просто."
    
    sh "Проще простого, мы уже так делали."
    
    stop ambience
    
    play ambience ambience_boat_station_day fadein 1
    
    scene bg ext_boathouse_day with dissolve
    
    "Мы отправились на пристань.{w} По пути мы оглядывались чтоб не встретить Ольгу Дмитриевну.{w} Придя на берег, Шурик взял вёсла из будки.{w} Ещё раз оглядевшись по сторонам, мы отшвартовали лодку, сели и поплыли."
    
    scene bg ext_beach_day with dissolve

    "На веслах сидел Электроник."
    
    me "Я могу подменить."
    
    el "Не нужно.{w} Первая поездка бесплатно."
    
    "Через минут 15 мы приплыли на остров."
    
    scene bg ext_island_day with dissolve
    
    show el normal pioneer at left with dissolve
    
    show sh normal pioneer at right with dissolve
    
    sh "Добро пожаловать на остров Ближний."
    
    me "Он действительно так называется?"
    
    sh "Да.{w} Потому что ближе к берегу чем соседний."
    
    "Мы уселись на берегу в тени деревьев."
    
    el "Эх хороша погодка!{w} Вздремнуть бы сейчас."
    
    sh "Было бы неплохо, но до ужина не так много осталось."
    
    me "Кто-то засёк сколько у нас времени осталось?"
    
    el "Часа два точно есть."
    
    me "Кстати, вы я так понимаю из одной школы?"
    
    el "Да.{w} Наши семьи дружат, вот и мы считай с пелёнок вместе."
    
    me "Круто.{w} Я даже завидую немного."
    
    el "Чему?"
    
    me "Как чему? Тому, что у вас обоих всегда был рядом человек с которым можно поговорить, разделить невзгоды, поделиться переживаниями, получить поддержку или просто поболтать о какой-нибудь ерунде."
    
    me "Иными словами: у вас всегда был хотя бы один друг."
    
    sh "Хочешь сказать у тебя нету друзей или даже одного лучшего друга?"

    me "Именно так.{w} И, что главное, до приезда сюда я думал это вполне нормально,{w} но сейчас я начал на это смотреть с другого ракурса."
    
    sh "Я рад, что ты изменил своё мнение.{w} Но как это у тебя не было друзей?{w} Вообще никогда?"
    
    me "Если вкладывать в слово “друг” то, что описал я, то нет.{w} Были, конечно, люди с которыми я общался и проводил время, но с ними я просто коротал время."
    
    hide el with dissolve
    
    show el laugh pioneer at left with dissolve
    
    el "Значит эти тёмные времена теперь для тебя позади. Добро пожаловать в нашу компанию, друг."
    
    me "С честью приму ваше предложение."
    
    el "Это не предложение, а утверждение."
    
    hide el with dissolve
    
    hide sh with dissolve
    
    "Ещё немного поболтав, мы вернулись на пристань. Недалеко от неё, мы встретили Славю."
    
    stop ambience
    
    play ambience ambience_camp_center_day fadein 1
    
    scene bg ext_houses_day with dissolve
    
    show el normal pioneer at fleft with dissolve

    show sh normal pioneer at fright with dissolve

    show sl smile pioneer with dissolve
    
    sl "Привет, где это вы были?{w} Я вас искала."
    
    sh "На остров плавали.{w} Ты же никому не скажешь?"
    
    sl "Нет, конечно.{w} При условии, что в следующий раз меня с собой возьмёте."
    
    el "Без проблем.{w} Зачем искала?"
    
    sl "Вожатая приказала музкружку приготовить на завтра всю аппаратуру.{w} Только я Мику не могу найти.{w} Семён ты её не видел?"
    
    me "Нет."
    
    sl "Тогда найди, её и передай информацию. Раз вы двое тоже тут, можете помочь Семёну."
    
    el "Хорошо, только давай может уже завтра с утра?{w} Там дел то."
    
    sl "Ну смотрите.{w} Это и на моей ответственности тоже, не подставьте."
    
    sh "Всё будет в лучшем виде."
    
    sl "Рассчитываю на вас."
    
    hide sl with dissolve
    
    hide el with dissolve
    
    hide sh with dissolve
    
    show el normal pioneer at cleft with dissolve
    
    show sh normal pioneer at cright with dissolve
    
    el "Неудобная ситуация складывается."
    
    me "Что же делать теперь?{w} Мне ужасно некомфортно будет работать, делая вид, что ничего и не было."
    
    sh "Успокойся.{w} До завтра ещё ситуация может сто раз изменится,{w} а если не изменится мы с Серёгой пойдём возьмём у неё ключ и с тобой без её участия всё сделаем."
    
    el "Можно вообще у Слави взять запасной ключ."
    
    sh "Или так.{w} Скоро уже звонок на ужин будет.{w} Пошли у столовой подождём."
    
    stop ambience
    
    play ambience ambience_camp_center_evening fadein 1
    
    scene bg ext_dining_hall_near_sunset with dissolve
    
    "Мы пошли к столовой.{w} Через некоторое время заиграла знакомая мелодия и появилась Ольга Дмитриевна."
    
    show mt smile pioneer with dissolve
    
    show el normal pioneer at fleft with dissolve
    
    show sh normal pioneer at fright with dissolve
    
    mt "Добрый вечер, молодые люди.{w} Семён, давненько я тебя не видела.{w} Шурик с Серёжей могут идти, а тебя попрошу задержаться."
    
    el "Мы займём тебе место."
    
    hide el with dissolve
    
    hide sh with dissolve
    
    hide mt with dissolve
    
    show mt angry pioneer with dissolve
    
    mt "Значит так. Куда это ты пропал?"
    
    me "Я к себе в домик ушёл, извините, не подумал вам сказать."
    
    mt "Семён, что это за самоволка?{w} Какой пример ты подаёшь другим?"
    
    me "Первый и последний раз я подал плохой пример."
    
    mt "Очень на это надеюсь.{w} Я заходила к тебе, но в домике было пусто.{w} Как это объяснишь?{w} Где тебя носило до вечера?"
    
    me "Ну я потом ушёл к кибернетикам.{w} У них в клубе был."
    
    mt "Там я тоже была.{w} Они были без тебя."
    
    th "Эх, дорогуша.{w} Если ты к ним заходила, они бы мне сказали, что меня ищут."
    
    me "Не было вас там."
    
    hide mt with dissolve
    
    show mt smile pioneer with dissolve

    mt "Что ж, ты прошёл проверку.{w} Подытожим.{w} За чистосердечное, тебе полагается легкая форма наказания.{w}  Завтра добровольно поможешь Славе с уборкой после дискотеки."
    
    mt "И, Семён, я вожатая, а не надзиратель, если тебе что-то не нравиться мне можно сказать.{w} Вместе постараемся найти альтернативу."
    
    me "Понял."
    
    mt "Вот и славно."
    
    stop ambience
    
    play ambience ambience_dining_hall_full fadein 1
    
    scene bg int_dining_hall_people_day with dissolve

    "Мы вошли в столовую.{w} Ольга села за стол с Виолой.{w} Я пошёл к моим новым друзьям.{w} За одним из столиков, я так же увидел Мику в компании Лены. "
    
    show el normal pioneer close at cleft with dissolve
    
    show sh normal pioneer close at cright with dissolve
    
    sh "Как прошла беседа?"
    
    me "Нормально.{w} Всего-то нужно заняться уборкой после дискотеки."
    
    el "Пф, этим и так будет заниматься весь наш отряд.{w} Так что тебя вообще не наказали."
    
    sh "Заметил Мику?"
    
    me "Конечно."
    
    sh "Раз они сидят за одним столиком, прогнозы у меня весьма оптимистичные."
    
    me "Чё так?"
    
    sh "Сам посуди.{w} Если они поссорились из-за тебя, вряд ли бы ели вместе."
    
    me "Что ж, ты прав."
    
    sh "А раз они дружат, думаю и мои шансы с Леной ненулевые."
    
    me "Кстати о завтра.{w} Не хотелось бы идти вонючим.{w} Где тут душ можно принять?"
    
    el "За умывальниками есть душевые.{w}  Ещё топят баньку, она находится чуть дальше по тропинке от библиотеки.{w} У каждого отряда свой день посещения.{w} Сегодня как раз наш день."
    
    me "Понятно, во сколько можно приходить?"
    
    el "С пол девятого идут девочки, потом мы.{w} По 10-15 минут на человека.{w} Мы идём где-то с пол десятого.{w} В камень-ножницы-бумагу решим кто за кем."
    
    me "Принято."
    
    stop ambience
    
    $ sunset_time()
    $ persistent.sprite_time = 'sunset'
    
    play ambience ambience_camp_center_evening fadein 1
    
    scene bg cum_hata_sunset with dissolve
    
    "После ужина мы разошлись по домам.{w} По дороге меня перехватила Лена."
    
    show un smile pioneer with dissolve
    
    un "Привет, как дела?"
    
    me "Пока никак.{w} А у тебя как?{w} И у Мику."
    
    un "У меня неплохо, а как у Мику скоро узнаешь.{w} Я и так тебе много сказала."
    
    me "Для чего ты мне всё рассказала?"
    
    un "Во-первых, Мику сама приревновала тебя ко мне и мне пришлось подтолкнуть тебя."
    
    un "Во-вторых, я разве не похожа на добрую девушку, что хочет помочь своей лучшей подруге?"
    
    me "Получается с утра в столовой ты специально нас вдвоём оставила?"
    
    un "Получается, что так.{w} Но лезть в ваши отношения я больше не буду.{w} Если, конечно, никто меня снова не вплетёт."
    
    me "Раз вы лучшие подруги, то почему в разных клубах?"
    
    un "В Ленинграде мы каждый день видимся.{w} Даже самым близким друзьям нужно отдыхать друг от друга.{w} Да и музыкант из меня плохой."
    
    hide un with dissolve
    
    show un normal pioneer at left with dissolve
    
    show dv normal pioneer at cright with dissolve
    
    dv "Не отвлекаю?"
    
    "Не пойми откуда появилась Алиса."
    
    un "Нет, я как раз собиралась уходить."
    
    dv "Вот и хорошо.{w} Семён пройдемся?"
    
    me "Ну ладно."
    
    scene bg ext_houses_sunset with dissolve
    
    show dv normal pioneer with dissolve
    
    dv "Что это днём было?"
    
    me "Ничего.{w} Извини я не в настроении был."
    
    dv "Ясно.{w} Знаешь, что самое интересное?"
    
    me "Что?"
    
    dv "Что Мику меня примерно так же послала.{w} И зачем ты сказал, что её нет дома, если она там была?"
    
    me "Странно, я думал её там нет."
    
    dv "Хорош врать. Говори из-за чего вы поссорились?"
    
    me "Ничего мы не ссорились.{w} Я не знаю, что с ней."
    
    dv "Ладно, раз так - идём и узнаем, что у неё случилось."
    
    me "Никуда я не пойду.{w} Может ей одной хочется побыть."
    
    hide dv with dissolve
    
    show dv angry pioneer with dissolve
    
    dv "Семён, повторяю: хорош врать.{w} Я бы погрубее сказала, но даме не положено."
    
    me "Давай так.{w} Мы с ней не ссорились.{w} Просто… давай не сейчас."
    
    dv "Нет сейчас.{w} Давай рассказывай."
    
    me "Не хочу."
    
    dv "Кому говорю рассказывай."
    
    me "Нет.{w} Послушай, я с ней не ссорился и ни я, ни кто другой её не обижал.{w} Она сказала ей нужно некоторое время побыть одной."
    
    "Я тут же пожалел о сказанном.{w} Алиса медленно расплылась в улыбке."
    
    hide dv with dissolve
    
    show dv laugh pioneer with dissolve
    
    dv "Ааааааа, есть у меня одна догадка."
    
    "Схватив меня за руку и подтянув к себе, прошептала мне на ухо."
    
    dv "Ты что, втрескался в Микулю?"

    "Отпустив меня, она перешла на обычный тон."
    
    dv "Предполагаю, она сказала: “Мне надо подумать.”?"
    
    me "Да."
    
    "Ответил я, не видя смысла продолжать сопротивление."
    
    dv "Хочешь я пойду скажу, что ты места себе не находишь?"
    
    me "Нет."
    
    dv "Может, тогда показать где цветов нарвать?"
    
    "Продолжила издеваться Алиса."
    
    me "Заткнись."
    
    dv "Давай научу на гитаре играть.{w} Удивишь её."

    me "За-мол-чи."
    
    "Внезапно в Алису прилетел мяч, а следом появилась Ульяна."
    
    stop ambience
    
    play ambience ambience_soccer_play_background fadein 1
    
    scene bg ext_playground_sunset with dissolve
    
    show us laugh sport at cright with dissolve
    
    show dv rage pioneer at cleft with dissolve
    
    dv "Ты чё, мелкая!?"
    
    us "Ничё, по сторонам смотри.{w} А вы что тут делаете?"
    
    "Мы с Алисой посмотрели друг на друга."
    
    hide dv with dissolve
    
    hide us with dissolve
    
    show us normal sport at cright with dissolve
    
    show dv laugh pioneer at cleft with dissolve

    dv "Ты представляешь!?"
    
    "Я приготовился к худшему."
    
    dv "Семён хочет сыграть в волейбол."
    
    hide us with dissolve
    
    show us grin sport at cright with dissolve
    
    us "Это запросто!{w} Сейчас созову людей."
    
    hide us with dissolve
    
    dv "Делай, что скажут и никто не пострадает!"
    
    "Расхохоталась она."
    
    stop ambience
    
    $ night_time()
    $ persistent.sprite_time = 'night'
    
    play ambience ambience_int_cabin_night fadein 1
    
    scene bg cum_room_light_night with dissolve
    
    "Вернулся в домик я потный и весь в пыли.{w} По результатам игры с Шуриком и Электроником я шёл в баню первым."
    
    
    play sound sfx_open_cupboard
    
    "Дождавшись своего времени, взяв со шкафа такую же, но чистую форму, непонятно откуда взявшуюся бутылку шампуня (видимо вожатая принесла), я пошёл."
    
    stop ambience
    
    play ambience ambience_grasshoper_clean fadein 1
    
    scene bg ext_bathhouse_night with dissolve
    
    "Тропинку за библиотекой я нашёл сразу.{w} Пойдя по ней, я увидел идущий ко мне на встречу силуэт." 
    
    play music music_list ['raindrops'] fadein 1
    
    show mi smile long hair night with dissolve
    
    "Этим силуэтом оказалась Мику."
    
    "Распущенные волосы были чуть длиннее талии.{w} От неё ещё веяло теплом.{w} Её запах по-настоящему пьянил."
    
    "Рядом с ней хотелось дышать на полную грудь, а взгляд не хотелось отводить."
    
    mi "Привет.{w} Похоже я что-то долго засиделась."
    
    "Она слегка улыбнулась."
    
    me "Да нет, я же только пришёл.{w} Насчёт сегодняшнего… "
    
    mi "Давай не сейчас и не здесь.{w} Неподходящая обстановка.{w} До завтра и спокойной ночи."
    
    me "Спокойной ночи."
    
    hide mi smile long hair night with dissolve
    
    stop music fadeout 1
    
    "Она быстро зашагала прочь."
    
    stop ambience
    
    play ambience ambience_int_cabin_night fadein 1
    
    scene bg cum_room_night with dissolve
    
    "Вымывшись, я вернулся к себе в домик.{w} Я лежал, укутавшись в одеяло.{w} Мне, как ребёнку перед днём рождения, хотелось побыстрее уснуть."
    
    stop ambience
    
    $ day_time()
    $ persistent.sprite_time = 'day'
    
    play music music_list['door_to_nightmare'] fadein 1
    
    show prologue_dream
    
    show uv smile far with dissolve
    
    uv "Тебе здесь нравиться?"
    
    me "Ты уже спрашивала."
    
    uv "А ты не ответил.{w} Хочешь здесь остаться?"
    
    me "Ещё не знаю.{w} Почему на утро я забыл тебя и весь сон?"
    
    uv "Потому что это не сон."
    
    me "Что тогда?"
    
    uv "Твоё подсознание, что застряло между мирами."
    
    me "Кто ты такая?"
    
    hide uv with dissolve
    
    show uv laugh far with dissolve

    uv "Юля."
    
    me "Смеёшься?"
    
    hide uv with dissolve
    
    show uv smile far with dissolve
    
    uv "Нет, я и вправду Юля."
    
    me "Ладно, забыли."
    
    uv "Ты хочешь здесь остаться?"
    
    me "В лагере?"
    
    uv "В лагере и том, что будет после него."
    
    me "Что меня ждёт после лагеря?"
    
    uv "Новая жизнь.{w} Линия, которую ты должен выбрать."
    
    me "Да как мне её выбрать!?"
    
    uv "Избавься от страха нового."
    
    me "Какого ещё страха?"
    
    uv "Ты боишься, что вернешься обратно.{w} Сомневаешься, что останешься здесь.{w} Избавься от этих чувств."
    
    hide prologue_dream
    
    stop music fadeout 1
    
    jump EvSuDAY_3
    
    
    
    
   
    
