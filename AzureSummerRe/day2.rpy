label EvSuDAY_2: 
    $ backdrop = "days"
    $ new_chapter(2, u"День второй.")
    $ day_time()
    $ persistent.sprite_time = 'day'
    
    play ambience ambience_int_cabin_day fadein 1
    scene bg cum_room with dissolve 