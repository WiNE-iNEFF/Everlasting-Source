init:

    image mi smile long hair night = im.MatrixColor( im.Composite((600,720), (0,0), "Azure_summer/sprites/normal/mi/mi_3_body_loo.png",(0,0), "Azure_summer/sprites/normal/mi/mi_3_casual.png",(0,0), "Azure_summer/sprites/normal/mi/mi_3_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) )    #modded: image mi smile long hair night = im.MatrixColor( im.Composite((900,1080), (0,0), "Azure_summer/sprites/normal/mi/mi_3_body_loo.png",(0,0), "Azure_summer/sprites/normal/mi/mi_3_casual.png",(0,0), "Azure_summer/sprites/normal/mi/mi_3_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) )

    image mi dress night = im.MatrixColor( im.Composite((600,720), (0,0), "Azure_summer/sprites/normal/mi/mi_3_body_loo.png",(0,0), "Azure_summer/sprites/normal/mi/mi_3_dress.png",(0,0), "Azure_summer/sprites/normal/mi/mi_3_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) )    #modded: image mi dress night = im.MatrixColor( im.Composite((900,1080), (0,0), "Azure_summer/sprites/normal/mi/mi_3_body_loo.png",(0,0), "Azure_summer/sprites/normal/mi/mi_3_dress.png",(0,0), "Azure_summer/sprites/normal/mi/mi_3_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) )
    
    image mi dress sunset = im.MatrixColor( im.Composite((600,720), (0,0), "Azure_summer/sprites/normal/mi/mi_3_body_loo.png",(0,0), "Azure_summer/sprites/normal/mi/mi_3_dress.png",(0,0), "Azure_summer/sprites/normal/mi/mi_3_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) )    #modded: image mi dress sunset = im.MatrixColor( im.Composite((900,1080), (0,0), "Azure_summer/sprites/normal/mi/mi_3_body_loo.png",(0,0), "Azure_summer/sprites/normal/mi/mi_3_dress.png",(0,0), "Azure_summer/sprites/normal/mi/mi_3_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) )
    
    image mi dress sad night = im.MatrixColor( im.Composite((600,720), (0,0), "Azure_summer/sprites/normal/mi/mi_2_body_loo.png",(0,0), "Azure_summer/sprites/normal/mi/mi_2_dress.png",(0,0), "Azure_summer/sprites/normal/mi/mi_sad_3.png"), im.matrix.tint(0.63, 0.78, 0.82) )    #modded: image mi dress sad night = im.MatrixColor( im.Composite((900,1080), (0,0), "Azure_summer/sprites/normal/mi/mi_2_body_loo.png",(0,0), "Azure_summer/sprites/normal/mi/mi_2_dress.png",(0,0), "Azure_summer/sprites/normal/mi/mi_sad_3.png"), im.matrix.tint(0.63, 0.78, 0.82) )

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
    
    image bg int_wardrobe = "Azure_summer/bg/int_wardrobe.jpg"
    
    image bg ext_warehouse2_day = "Azure_summer/bg/ext_warehouse2_day.jpg"
    
    image bg cum_room_sunset = "Azure_summer/bg/cum_room_sunset.jpg" 
    
    image bg ext_houses_night = "Azure_summer/bg/ext_houses_night.jpg"
    
    image bg palata = "Azure_summer/bg/palata.jpg"
    
    $ piano = "Azure_summer/music/sister-friede-father-ariandel.mp3"
    
    $ forest = "Azure_summer/music/IC3PEAK_-_Are_you_scared_I_am_not.mp3"
    
    $ dk = Character (u'Медсестра', color="1E90FF", what_color="E2C778")

    
label EvSuDAY_5: 
    $ backdrop = "days"
    $ new_chapter(5, u"День пятый.")
    
    $ day_time()
    $ persistent.sprite_time = 'day'
    
    play ambience ambience_int_cabin_day fadein 1
    
    scene bg cum_room_day with dissolve 
    
    "Я открыл глаза, сделал пару медленных глубоких вдохов-выдохов и протёр глаза, чтобы убедиться, что я всё ещё живой.{w} Я прокручивал в голове все свои сны с Юлей и пытался убедить себя, что это просто сны и ничего они не значат, но убеждения быстро развеялись." 
    "Я понимал, что всё это взаправду и что мне осталось недолго здесь.{w} А дальше… Смерть. А если быть точным – я исчезну.{w} Не совсем понимаю, чем это отличается от смерти.{w} Думаю, скоро у меня будет возможность это понять."
    "Я мог бы остаться здесь, даже нашёл человека, ради которого можно жить.{w} Только я не хочу жить в мире этого человека."
    "Вот такой замкнутый круг: или мир с Мику, или мир без неё.{w} Я не хочу ни того, ни другого.{w} Это мой выбор."
    
    play sound sfx_dinner_horn_processed
    
    "Провести этот последний день как обычно или заняться чем-то другим?"
    
    "Не знаю. Учитывая то, что мне недолго осталось, жизнь не проносится перед глазами.{w} Было бы чему проноситься." 
    "Может провести последние минуты или часы с Мику?{w} Но я не хочу, чтобы она грустила.{w} Ведь она действительно меня любит.{w} Хотя, если я исчезну, не показавшись ей, она тоже расстроится."
    
    "Ладно, проведу этот день как обычно.{w} Не хочу оставшееся время смотреть в потолок.{w} В шкафу я взял припрятанные наушники и телефон.{w} Заряда батареи сохранилось достаточно для прогулки."
    
    stop ambience
    
    play ambience ambience_camp_center_day fadein 1
    scene bg ext_houses_day at center with dissolve
    show sl smile pioneer far with dissolve
    
    "Я воткнул наушники в уши и пошёл к восточным воротам лагеря.{w} Я шёл, не обращая внимания на встречных мне пионеров, а в ответ ловил непонимающие и вопросительные взгляды.{w} Дорогу мне преградила Славя."
    
    sl "…"
    
    "Я вытащил наушники."
    
    me "Что ты сказала?"
    
    sl "Ты что новенький?{w} Я тебя раньше не видела в лагере, показать где столовая?{w} Сейчас как раз завтрак."
    
    th "Забыла."
    
    me "Нет, я уже оттуда."
    
    hide sl with dissolve
    
    "Она хотела продолжить разговор, но я решительно оставил её за спиной."
    
    sl "Если хочешь посмотреть лагерь, я могу…"
    
    "Я снова заткнул уши."
    
    stop ambience
    
    play ambience ambience_forest_day fadein 1

    scene bg ext_polyana_day at center with dissolve
    
    "Выйдя на поляну в лесу, я увидел сидящую на корнях дерева девочку.{w} Я подошёл к ней и вытащил наушники."
    
    show uv smile far with dissolve
    
    uv "Привет."
    
    me "Привет."
    
    uv "Гуляешь?"
    
    me "Ага.{w} Что ты тут делаешь?{w} Я думал ты только в моей голове."
    
    uv "А ты чего сюда пришёл?"
    
    me "Ну…{w} решил прогуляться.{w} Что мне ещё делать?"
    
    uv "Мог бы провести последние минуты с Мику.{w} Ведь в Харькове 21-го века её у тебя больше не будет."
    
    me "Ты ж говорила, что я не останусь ни тут, ни там."
    
    uv "Так и есть, но это не касается твоего физического состояния. Я говорила о твоём внутреннем «Я»."
    
    me "То есть я буду как живой труп?"
    
    uv "Именно.{w} Без эмоций и чувств ты будешь волочить своё существование, ибо внутри себя отверг оба мира."
    
    mi "Семён?"
    
    hide uv with dissolve
    
    show mi angry pioneer far with dissolve
    
    "Я обернулся и увидел Мику.{w} Юли больше рядом не было."
    
    me "Ты меня не забыла?"
    
    mi "Конечно нет.{w} Почему ты не захотел остаться со мной?"
    
    me "Я хотел, правда…"
    
    mi "Но ты слишком эгоистичен, чтобы пойти на компромиссы и принять мой мир."
    
    me "Прости, я…"
    
    mi "Не нужно больше ничего говорить.{w} Прощай."
    
    hide mi with dissolve
    
    scene bg black at center with dissolve
    
    stop ambience
    
    "В глазах резко потемнело.{w} Я провалился во мрак."
    
    dk "Он просыпается.{w} Пациент вышел из комы."
    
    scene bg palata with dissolve
    
    show unblink
    
    "Я медленно открыл глаза. Осмотрел всё вокруг. Я лежал на больничной койке."
    
    show blinking
    
    dk "С возвращением!{w} Около недели назад вы потеряли сознание в автобусе и вас доставили сюда…"
    
    th "Значит это был только сон.{w} Вот только зачем я проснулся?"
    
    jump EvSuPrlg
