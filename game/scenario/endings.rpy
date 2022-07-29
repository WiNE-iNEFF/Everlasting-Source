label postscriptum:

    window show
    "У каждой истории есть начало и конец."
    "У каждой истории есть своя канва, синопсис, содержание, ключевые моменты, прологи и эпилоги."
    "И нет такой книги, в которой при каждом новом прочтении не открывались бы вещи, на которые раньше не обращал внимания."
    "У каждой истории есть начало и конец."
    "Почти у каждой…"
    window hide

    $ renpy.pause(5)

    return

init:

    transform ending_transform:
        xalign 0.5
        ypos 1.3
        linear 87.0 ypos -1.55

    $ credits_text = translation_new["credits"]

label un_good_ending:

    $ persistent.sprite_time = "day"

    scene bg black
    with dissolve2

    pause(1)

    play music music_list["opening"] fadein 3

    $ renpy.show("credits credits_text", [ending_transform], layer='widgetoverlay')

    scene bg ext_square_night_ending behind credits:
        zoom 1.2
        anchor (0.1,0.0)
        linear 12 anchor (0.0,0.0)
    show un normal pioneer behind credits:
        pos (0.7, 0)
        linear 11 pos (0.2,0)
    with dissolve2
    $ renpy.pause(8, hard=True)
    scene cg d1_grasshopper_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0,0.1)
        linear 12 anchor (0.1,0.0)
    $ renpy.pause(8, hard=True)
    scene bg ext_polyana_night_ending behind credits:
        zoom 1.2
        linear 11 zoom 1.0
    show un angry pioneer behind credits:
        xalign 0.355
        xanchor 0.5
        yanchor 0.0
        zoom 1.2
        linear 11 zoom 1.0
    show dv angry pioneer behind credits:
        xalign 0.645
        xanchor 0.5
        yanchor 0.0
        zoom 1.2
        linear 11 zoom 1.0
    with dissolve2
    $ renpy.pause(8, hard=True)
    scene cg d3_un_dance_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.1,0.1)
        linear 12 anchor (0.0,0.0)
    $ renpy.pause(8, hard=True)
    scene cg epilogue_un_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.1,0.0)
        linear 12 anchor (0.0,0.1)
    $ renpy.pause(8, hard=True)
    scene cg d5_un_island_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.1,0.1)
        linear 12 anchor (0.0,0.0)
    $ renpy.pause(8, hard=True)
    scene cg d6_un_evening_1_ending behind credits with dissolve2:
        zoom 1.1
        linear 6 zoom 1.0
    $ renpy.pause(4, hard=True)
    scene cg d6_un_evening_2_ending behind credits with dissolve
    $ renpy.pause(4, hard=True)
    scene cg epilogue_un_good_ending behind credits with flash2
    $ renpy.pause(8, hard=True)

    scene black
    with dissolve2

    stop music fadeout 3

    $ renpy.pause(4, hard=True)

    return

label un_bad_ending:

    scene bg black
    with dissolve2

    pause(1)

    play music music_list["410"] fadein 3

    $ renpy.show("credits credits_text", [ending_transform], layer='widgetoverlay')

    $ renpy.pause(8, hard=True)
    scene un_ending_bad
    with dissolve2
    $ renpy.pause(79, hard=True)

    scene bg black
    with dissolve2

    stop music fadeout 5

    $ renpy.pause(4, hard=True)

    return

label main_good_ending:

    $ persistent.sprite_time = "day"

    scene bg black
    with dissolve2

    pause(1)

    play music music_list["opening"] fadein 3

    $ renpy.show("credits credits_text", [ending_transform], layer='widgetoverlay')

    $ renpy.pause(2, hard=True)

    scene anim intro_1
    with dissolve
    $ renpy.pause(0.5, hard=True)
    scene anim intro_2
    with dissolve
    $ renpy.pause(0.5, hard=True)
    scene anim intro_3
    with dissolve
    $ renpy.pause(0.5, hard=True)
    scene anim intro_4
    with dissolve
    $ renpy.pause(0.5, hard=True)
    scene anim intro_5
    with dissolve
    $ renpy.pause(0.5, hard=True)
    scene anim intro_6
    with dissolve
    $ renpy.pause(0.5, hard=True)
    scene anim intro_8
    with dissolve
    $ renpy.pause(0.5, hard=True)
    scene anim intro_7
    with dissolve
    $ renpy.pause(0.5, hard=True)
    scene anim intro_9
    with dissolve
    $ renpy.pause(0.5, hard=True)
    scene anim intro_10
    with dissolve
    $ renpy.pause(0.5, hard=True)
    scene anim intro_11
    with dissolve
    $ renpy.pause(0.5, hard=True)
    scene anim intro_13
    with dissolve
    $ renpy.pause(0.5, hard=True)
    scene anim intro_14
    with dissolve
    $ renpy.pause(0.5, hard=True)
    scene anim intro_15
    with dissolve
    $ renpy.pause(0.5, hard=True)
    scene anim intro_16
    with dissolve
    $ renpy.pause(0.5, hard=True)

    scene op_back
    with dissolve2
    $ renpy.pause(1, hard=True)
    show op_sl
    with dissolve2
    $ renpy.pause(1, hard=True)
    show cg d6_sl_forest_ending
    with dissolve
    $ renpy.pause(0.5, hard=True)
    show cg d3_sl_library_ending
    with dissolve
    $ renpy.pause(0.5, hard=True)

    scene op_back
    show op_sl
    with dissolve2
    $ renpy.pause(1, hard=True)
    show op_un
    with dissolve2
    $ renpy.pause(1, hard=True)
    show cg d5_un_island_ending
    with dissolve
    $ renpy.pause(0.5, hard=True)
    show cg epilogue_un_ending
    with dissolve
    $ renpy.pause(0.5, hard=True)

    scene op_back
    show op_sl
    show op_un
    with dissolve2
    $ renpy.pause(1, hard=True)
    show op_us
    with dissolve2
    $ renpy.pause(1, hard=True)
    show cg d2_ussr_falling_ending
    with dissolve
    $ renpy.pause(0.5, hard=True)
    show cg d4_us_cancer_ending
    with dissolve
    $ renpy.pause(0.5, hard=True)
    show cg d3_ussr_catched_ending
    with dissolve
    $ renpy.pause(0.5, hard=True)

    scene op_back
    show op_sl
    show op_un
    show op_us
    with dissolve2
    $ renpy.pause(1, hard=True)
    show op_dv
    with dissolve2
    $ renpy.pause(1, hard=True)
    show cg d5_dv_argue_ending
    with dissolve
    $ renpy.pause(0.5, hard=True)
    show cg d2_water_dan_ending
    with dissolve
    $ renpy.pause(0.5, hard=True)

    scene op_back
    show op_sl
    show op_un
    show op_us
    show op_dv
    with dissolve2
    $ renpy.pause(1, hard=True)
    show op_mi
    with dissolve2
    $ renpy.pause(1, hard=True)
    show cg d2_miku_piano_ending
    with dissolve
    $ renpy.pause(0.5, hard=True)
    show cg d4_mi_guitar_ending
    with dissolve
    $ renpy.pause(0.5, hard=True)
    show cg epilogue_mi_1_ending
    with dissolve
    $ renpy.pause(0.5, hard=True)

    scene op_back
    show op_sl
    show op_un
    show op_us
    show op_dv
    show op_mi
    with dissolve2
    $ renpy.pause(1, hard=True)
    show op_uv
    with dissolve2
    $ renpy.pause(1, hard=True)

    scene bg ext_road_day_ending
    with dissolve2
    $ renpy.pause(1, hard=True)
    show logo_day:
        align (0.5, 0.5)
    with dissolve2

    $ renpy.pause(12, hard=True)

    scene black
    with dissolve2

    stop music fadeout 3

    $ renpy.pause(4, hard=True)

    return

label main_bad_ending:

    scene bg black
    with dissolve2

    pause(1)

    play music music_list["410"] fadein 3

    $ renpy.show("credits credits_text", [ending_transform], layer='widgetoverlay')

    $ renpy.pause(8, hard=True)
    scene black_long
    with dissolve2
    $ renpy.pause(79, hard=True)

    scene bg black
    with dissolve2

    stop music fadeout 5

    $ renpy.pause(4, hard=True)

    return

label dv_bad_ending:

    $ persistent.sprite_time = "day"

    scene bg black
    with dissolve2

    pause(1)

    play music music_list["opening"] fadein 3

    $ renpy.show("credits credits_text", [ending_transform], layer='widgetoverlay')

    scene bg ext_beach_day_ending behind credits:
        zoom 1.2
        anchor (0.1,0.0)
        linear 12 anchor (0.0,0.1)
    show dv smile pioneer2 behind credits:
        pos (0.1, 0)
        linear 12 pos (0.7,0)
    with dissolve2
    $ renpy.pause(8, hard=True)
    scene cg d2_2ch_beach_ending behind credits with dissolve2:
        pos (0,-1920)
        linear 9.0 pos (0,0)
        linear 3.0 pos (0, -250)
    $ renpy.pause(8, hard=True)
    scene bg ext_polyana_night_ending behind credits:
        zoom 1.2
        linear 11 zoom 1.0
    show un scared pioneer behind credits:
        xalign 0.645
        xanchor 0.5
        yanchor 0.0
        zoom 1.2
        linear 11 zoom 1.0
    show dv rage pioneer behind credits:
        xalign 0.355
        xanchor 0.5
        yanchor 0.0
        zoom 1.2
        linear 11 zoom 1.0
    with dissolve2
    $ renpy.pause(8, hard=True)
    scene cg d3_dv_scene_1_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.,0.1)
        linear 12 anchor (0.1,0.0)
    $ renpy.pause(8, hard=True)
    scene cg d5_dv_island_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.0,0.0)
        linear 12 anchor (0.1,0.1)
    $ renpy.pause(8, hard=True)
    scene cg d7_dv_2_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.0,0.0)
        linear 12 anchor (0.1,0.0)
    $ renpy.pause(7, hard=True)
    scene cg d6_dv_fight_ending behind credits with dissolve2:
        zoom 1.1
        linear 5 zoom 1.0
    $ renpy.pause(3, hard=True)
    scene cg d6_dv_fight_2_ending behind credits with dissolve
    $ renpy.pause(3, hard=True)
    scene cg d6_dv_fight_3_ending behind credits with dissolve
    $ renpy.pause(3, hard=True)
    scene cg epilogue_dv_2_ending behind credits with flash2
    $ renpy.pause(8, hard=True)

    scene black
    with dissolve2

    stop music fadeout 3

    $ renpy.pause(4, hard=True)

    return

label dv_good_ending:

    $ persistent.sprite_time = "day"

    scene bg black
    with dissolve2

    pause(1)

    play music music_list["opening"] fadein 3

    $ renpy.show("credits credits_text", [ending_transform], layer='widgetoverlay')

    scene bg ext_beach_day_ending behind credits:
        zoom 1.2
        anchor (0.1,0.0)
        linear 12 anchor (0.0,0.1)
    show dv smile pioneer2 behind credits:
        pos (0.1, 0)
        linear 12 pos (0.7,0)
    with dissolve2
    $ renpy.pause(8, hard=True)
    scene cg d2_2ch_beach_ending behind credits with dissolve2:
        pos (0,-1920)
        linear 9.0 pos (0,0)
        linear 3.0 pos (0, -250)
    $ renpy.pause(8, hard=True)
    scene bg ext_polyana_night_ending behind credits:
        zoom 1.2
        linear 11 zoom 1.0
    show un scared pioneer behind credits:
        xalign 0.645
        xanchor 0.5
        yanchor 0.0
        zoom 1.2
        linear 11 zoom 1.0
    show dv rage pioneer behind credits:
        xalign 0.355
        xanchor 0.5
        yanchor 0.0
        zoom 1.2
        linear 11 zoom 1.0
    with dissolve2
    $ renpy.pause(8, hard=True)
    scene cg d3_dv_scene_2_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.0,0.1)
        linear 12 anchor (0.1,0.0)
    $ renpy.pause(8, hard=True)
    scene cg d5_dv_island_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.0,0.0)
        linear 12 anchor (0.1,0.1)
    $ renpy.pause(8, hard=True)
    scene cg d7_dv_2_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.0,0.0)
        linear 12 anchor (0.1,0.0)
    $ renpy.pause(7, hard=True)
    scene cg d5_dv_argue_ending behind credits with dissolve2:
        zoom 1.1
        linear 5 zoom 1.0
    $ renpy.pause(3, hard=True)
    scene cg d5_dv_argue_2_ending behind credits with dissolve
    $ renpy.pause(3, hard=True)
    scene cg d5_dv_argue_3_ending behind credits with dissolve
    $ renpy.pause(3, hard=True)
    scene cg epilogue_dv_3_ending behind credits with flash2
    $ renpy.pause(8, hard=True)

    scene black
    with dissolve2

    stop music fadeout 3

    $ renpy.pause(4, hard=True)

    return

label sl_bad_ending:

    $ persistent.sprite_time = "day"

    scene bg black
    with dissolve2

    pause(1)

    play music music_list["opening"] fadein 3

    $ renpy.show("credits credits_text", [ending_transform], layer='widgetoverlay')

    scene bg ext_houses_day_ending behind credits:
        zoom 1.2
        anchor (0.0,0.0)
        linear 12 anchor (0.1,0.0)
    show sl smile2 pioneer behind credits:
        pos (0.2, 0)
        linear 12 pos (0.5,0)
    with dissolve2
    $ renpy.pause(8, hard=True)
    scene cg d1_sl_dinner_ending behind credits with dissolve2:
        zoom 1.1
        linear 6 zoom 1.0
    $ renpy.pause(4, hard=True)
    scene cg d1_sl_dinner_0_ending behind credits with dissolve
    $ renpy.pause(4, hard=True)
    scene cg d3_sl_dance_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.1,0.0)
        linear 12 anchor (0.0,0.0)
    $ renpy.pause(8, hard=True)
    scene cg d5_sl_sleep_ending behind credits with dissolve2:
        zoom 1.1
        linear 6 zoom 1.0
    $ renpy.pause(4, hard=True)
    scene cg d5_sl_sleep_2_ending behind credits with dissolve
    $ renpy.pause(4, hard=True)
    scene cg d3_sl_evening_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.0,0.1)
        linear 12 anchor (0.1,0.0)
    $ renpy.pause(8, hard=True)
    scene cg d6_sl_forest_2_ending behind credits with dissolve2:
        zoom 1.1
        linear 6 zoom 1.0
    $ renpy.pause(4, hard=True)
    scene cg d6_sl_forest_ending behind credits with dissolve
    $ renpy.pause(4, hard=True)
    scene cg d3_sl_library_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.0,0.0)
        linear 12 anchor (0.1,0.1)
    $ renpy.pause(8, hard=True)
    scene bg semen_room_window_ending behind credits with flash2
    $ renpy.pause(8, hard=True)

    scene black
    with dissolve2

    stop music fadeout 3

    $ renpy.pause(4, hard=True)

    return

label sl_good_ending:

    $ persistent.sprite_time = "day"

    scene bg black
    with dissolve2

    pause(1)

    play music music_list["opening"] fadein 3

    $ renpy.show("credits credits_text", [ending_transform], layer='widgetoverlay')

    scene bg ext_houses_day_ending behind credits:
        zoom 1.2
        anchor (0.0,0.0)
        linear 12 anchor (0.1,0.0)
    show sl smile2 pioneer behind credits:
        pos (0.2, 0)
        linear 12 pos (0.5,0)
    with dissolve2
    $ renpy.pause(8, hard=True)
    scene cg d1_sl_dinner_ending behind credits with dissolve2:
        zoom 1.1
        linear 6 zoom 1.0
    $ renpy.pause(4, hard=True)
    scene cg d1_sl_dinner_0_ending behind credits with dissolve
    $ renpy.pause(4, hard=True)
    scene cg d3_sl_dance_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.1,0.0)
        linear 12 anchor (0.0,0.0)
    $ renpy.pause(8, hard=True)
    scene cg d5_sl_sleep_ending behind credits with dissolve2:
        zoom 1.1
        linear 6 zoom 1.0
    $ renpy.pause(4, hard=True)
    scene cg d5_sl_sleep_2_ending behind credits with dissolve
    $ renpy.pause(4, hard=True)
    scene cg d3_sl_evening_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.0,0.1)
        linear 12 anchor (0.1,0.0)
    $ renpy.pause(8, hard=True)
    scene cg d6_sl_forest_2_ending behind credits with dissolve2:
        zoom 1.1
        linear 6 zoom 1.0
    $ renpy.pause(4, hard=True)
    scene cg d6_sl_forest_ending behind credits with dissolve
    $ renpy.pause(4, hard=True)
    scene cg d3_sl_library_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.0,0.0)
        linear 12 anchor (0.1,0.1)
    $ renpy.pause(8, hard=True)
    scene cg epilogue_sl_ending behind credits with flash2
    $ renpy.pause(4, hard=True)
    scene cg epilogue_sl_2_ending behind credits with dissolve
    $ renpy.pause(4, hard=True)

    scene black
    with dissolve2

    stop music fadeout 3

    $ renpy.pause(4, hard=True)

    return

label us_bad_ending:

    $ persistent.sprite_time = "day"

    scene bg black
    with dissolve2

    pause(1)

    play music music_list["opening"] fadein 3

    $ renpy.show("credits credits_text", [ending_transform], layer='widgetoverlay')

    scene bg ext_playground_day_ending behind credits:
        zoom 1.2
        anchor (0.0,0.1)
        linear 12 anchor (0.1,0.0)
    show us laugh sport behind credits:
        pos (0.1, 0)
        linear 12 pos (0.8,0)
    with dissolve2
    $ renpy.pause(8, hard=True)
    scene cg d2_ussr_falling_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.0,0.1)
        linear 12 anchor (0.0,0.0)
    $ renpy.pause(8, hard=True)
    scene cg d3_soccer_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.0,0.0)
        linear 12 anchor (0.1,0.1)
    $ renpy.pause(8, hard=True)
    scene cg d3_us_library_1_ending behind credits with dissolve2:
        zoom 1.1
        linear 6 zoom 1.0
    $ renpy.pause(4, hard=True)
    scene cg d3_us_library_2_ending behind credits with dissolve
    $ renpy.pause(4, hard=True)
    scene cg d3_ussr_catched_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.0,0.1)
        linear 12 anchor (0.1,0.0)
    $ renpy.pause(8, hard=True)
    scene cg d4_catac_us_ending behind credits with dissolve2:
        zoom 1.1
        linear 6 zoom 1.0
    $ renpy.pause(4, hard=True)
    scene cg d4_catac_us_2_ending behind credits with dissolve
    $ renpy.pause(4, hard=True)
    scene cg d5_us_ghost_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.0,0.1)
        linear 12 anchor (0.1,0.0)
    $ renpy.pause(8, hard=True)
    scene cg epilogue_us_ending behind credits with flash2
    $ renpy.pause(8, hard=True)

    scene black
    with dissolve2

    stop music fadeout 3

    $ renpy.pause(4, hard=True)

    return

label us_good_ending:

    $ persistent.sprite_time = "day"

    scene bg black
    with dissolve2

    pause(1)

    play music music_list["opening"] fadein 3

    $ renpy.show("credits credits_text", [ending_transform], layer='widgetoverlay')

    scene bg ext_playground_day_ending behind credits:
        zoom 1.2
        anchor (0.0,0.1)
        linear 12 anchor (0.1,0.0)
    show us laugh sport behind credits:
        pos (0.1, 0)
        linear 12 pos (0.8,0)
    with dissolve2
    $ renpy.pause(8, hard=True)
    scene cg d2_ussr_falling_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.0,0.1)
        linear 12 anchor (0.0,0.0)
    $ renpy.pause(8, hard=True)
    scene cg d3_soccer_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.0,0.0)
        linear 12 anchor (0.1,0.1)
    $ renpy.pause(8, hard=True)
    scene cg d6_us_film_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.1,0.1)
        linear 12 anchor (0.0,0.0)
    $ renpy.pause(8, hard=True)
    scene cg d3_ussr_catched_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.0,0.1)
        linear 12 anchor (0.1,0.0)
    $ renpy.pause(8, hard=True)
    scene cg d5_us_ghost_2_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.1,0.0)
        linear 12 anchor (0.0,0.0)
    $ renpy.pause(8, hard=True)
    scene cg d5_us_kiss_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.0,0.0)
        linear 12 anchor (0.1,0.0)
    $ renpy.pause(8, hard=True)
    scene cg epilogue_us_3_a_ending behind credits with flash2
    $ renpy.pause(8, hard=True)

    scene black
    with dissolve2

    stop music fadeout 3

    $ renpy.pause(4, hard=True)

    return

label mi_ending:

    $ persistent.sprite_time = "day"

    scene bg black
    with dissolve2

    pause(1)

    play music music_list["opening"] fadein 3

    $ renpy.show("credits credits_text", [ending_transform], layer='widgetoverlay')

    scene bg ext_musclub_day_ending behind credits:
        zoom 1.2
        anchor (0.0,0.0)
        linear 12 anchor (0.1,0.0)
    show mi smile pioneer behind credits:
        pos (0.6, 0)
        linear 12 pos (0.2,0)
    with dissolve2
    $ renpy.pause(8, hard=True)
    scene cg d2_miku_piano2_ending behind credits with dissolve2:
        zoom 1.1
        linear 6 zoom 1.0
    $ renpy.pause(4, hard=True)
    scene cg d2_miku_piano_ending behind credits with dissolve
    $ renpy.pause(4, hard=True)
    scene cg d4_mi_guitar_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.0,0.0)
        linear 12 anchor (0.1,0.1)
    $ renpy.pause(8, hard=True)
    scene cg d5_mi_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.1,0.1)
        linear 12 anchor (0.0,0.0)
    $ renpy.pause(8, hard=True)
    scene cg d4_mi_sing_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.0,0.1)
        linear 12 anchor (0.1,0.0)
    $ renpy.pause(8, hard=True)
    scene cg epilogue_mi_1_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.0,0.0)
        linear 12 anchor (0.1,0.1)
    $ renpy.pause(8, hard=True)
    scene bg int_musclub_day_ending behind credits:
        zoom 1.1
        linear 24 zoom 1.0
    show mi shy pioneer behind credits:
        xalign 0.5
        zoom 1.1
        linear 6 zoom 1.0
    with dissolve2
    $ renpy.pause(2, hard=True)
    show mi smile pioneer behind credits with dissolve:
        xalign 0.5
        zoom 1.1
        linear 6 zoom 1.0
    $ renpy.pause(2, hard=True)
    show mi laugh pioneer behind credits with dissolve:
        xalign 0.5
        zoom 1.1
        linear 6 zoom 1.0
    $ renpy.pause(2, hard=True)
    show mi happy pioneer behind credits with dissolve:
        xalign 0.5
        zoom 1.1
        linear 6 zoom 1.0
    $ renpy.pause(2, hard=True)
    scene cg epilogue_mi_9_ending behind credits with flash2
    $ renpy.pause(8, hard=True)

    scene black
    with dissolve2

    stop music fadeout 3

    $ renpy.pause(4, hard=True)

    return

label harem_ending:

    $ persistent.sprite_time = "day"

    scene bg black
    with dissolve2

    pause(1)

    play music music_list["opening"] fadein 3

    $ renpy.show("credits credits_text", [ending_transform], layer='widgetoverlay')

    scene cg d7_pioneers_leaving_ending behind credits with dissolve2:
        zoom 1.2
        linear 12 zoom 1.0
    $ renpy.pause(8, hard=True)
    scene bg ext_square_day_ending behind credits:
        zoom 1.1
        linear 12 zoom 1.0
    show sl smile pioneer:
        xalign 0.5
        xanchor 0.5
        yanchor 0.0
    show dv smile pioneer behind sl:
        xalign 0.355
        xanchor 0.5
        yanchor 0.0
    show un smile pioneer behind sl:
        xalign 0.645
        xanchor 0.5
        yanchor 0.0
    show us smile pioneer behind sl, dv, un:
        xalign 0.16
        xanchor 0.5
        yanchor 0.0
    show mi smile pioneer behind sl, dv, un:
        xalign 0.84
        xanchor 0.5
        yanchor 0.0
    with dissolve2
    $ renpy.pause(8, hard=True)
    scene cg d3_disco_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.1,0.1)
        linear 12 anchor (0.0,0.0)
    $ renpy.pause(8, hard=True)
    scene cg d2_lineup_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.1,0.1)
        linear 12 anchor (0.0,0.0)
    $ renpy.pause(8, hard=True)
    scene bg int_bus_people_day_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.0,0.0)
        linear 12 anchor (0.1,0.0)
    $ renpy.pause(4, hard=True)
    scene bg int_bus_people_night_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.1,0.0)
        linear 12 anchor (0.0,0.0)
    $ renpy.pause(4, hard=True)

    scene bg ext_aidpost_day_ending behind credits with dissolve_fast
    $ renpy.pause(0.0, hard=True)
    scene bg ext_boathouse_day_ending behind credits with dissolve_fast
    $ renpy.pause(0.0, hard=True)
    scene bg ext_clubs_day_ending behind credits with dissolve_fast
    $ renpy.pause(0.0, hard=True)
    scene bg ext_dining_hall_away_day_ending behind credits with dissolve_fast
    $ renpy.pause(0.0, hard=True)
    scene bg ext_house_of_mt_day_ending behind credits with dissolve_fast
    $ renpy.pause(0.0, hard=True)
    scene bg ext_island_day_ending behind credits with dissolve_fast
    $ renpy.pause(0.0, hard=True)
    scene bg ext_library_day_ending behind credits with dissolve_fast
    $ renpy.pause(0.0, hard=True)
    scene bg ext_stage_normal_day_ending behind credits with dissolve_fast
    $ renpy.pause(0.0, hard=True)
    scene bg ext_washstand_day_ending behind credits with dissolve_fast
    $ renpy.pause(0.0, hard=True)
    scene bg int_aidpost_day_ending behind credits with dissolve_fast
    $ renpy.pause(0.0, hard=True)
    scene bg int_clubs_male_day_ending behind credits with dissolve_fast
    $ renpy.pause(0.0, hard=True)
    scene bg int_dining_hall_people_day_ending behind credits with dissolve_fast
    $ renpy.pause(0.0, hard=True)
    scene bg int_house_of_dv_day_ending behind credits with dissolve_fast
    $ renpy.pause(0.0, hard=True)
    scene bg int_house_of_mt_day_ending behind credits with dissolve_fast
    $ renpy.pause(0.0, hard=True)
    scene bg int_house_of_sl_day_ending behind credits with dissolve_fast
    $ renpy.pause(0.0, hard=True)
    scene bg int_house_of_un_day_ending behind credits with dissolve_fast
    $ renpy.pause(0.0, hard=True)


    scene bg ext_beach_day_ending behind credits:
        zoom 1.1
        linear 12 zoom 1.0
    show sl smile swim:
        xalign 0.5
        xanchor 0.5
        yanchor 0.0
    show dv smile swim behind sl:
        xalign 0.355
        xanchor 0.5
        yanchor 0.0
    show un smile swim behind sl:
        xalign 0.645
        xanchor 0.5
        yanchor 0.0
    show us smile swim behind sl, dv, un:
        xalign 0.16
        xanchor 0.5
        yanchor 0.0
    show mi smile swim behind sl, dv, un:
        xalign 0.84
        xanchor 0.5
        yanchor 0.0
    with dissolve2
    $ renpy.pause(8, hard=True)

    scene cg final_all_2_ending behind credits with flash2
    $ renpy.pause(8, hard=True)

    scene black
    with dissolve2

    stop music fadeout 3

    $ renpy.pause(4, hard=True)

    return

label uv_ending:

    $ persistent.sprite_time = "day"

    scene bg black
    with dissolve2

    pause(1)

    play music music_list["opening"] fadein 3

    $ renpy.show("credits credits_text", [ending_transform], layer='widgetoverlay')

    scene bg ext_polyana_day_ending behind credits:
        zoom 1.2
        anchor (0.0,0.0)
        linear 12 anchor (0.1,0.0)
    show uv smile behind credits:
        pos (0.6, 0)
        linear 12 pos (0.2,0)
    with dissolve2
    $ renpy.pause(8, hard=True)
    scene cg d4_uv_1_ending behind credits with dissolve2:
        zoom 1.1
        linear 6 zoom 1.0
    $ renpy.pause(4, hard=True)
    scene cg d4_uv_ending behind credits with dissolve
    $ renpy.pause(4, hard=True)
    scene cg d6_uv_2_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.1,0.1)
        linear 12 anchor (0.0,0.0)
    $ renpy.pause(8, hard=True)
    scene cg d5_uv_ending behind credits with dissolve2:
        zoom 1.1
        linear 6 zoom 1.0
    $ renpy.pause(4, hard=True)
    scene cg d5_uv_2_ending behind credits with dissolve
    $ renpy.pause(4, hard=True)
    scene cg d7_uv_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.0,0.1)
        linear 12 anchor (0.1,0.0)
    $ renpy.pause(8, hard=True)
    scene cg epilogue_uv_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.0,0.0)
        linear 12 anchor (0.1,0.1)
    $ renpy.pause(4, hard=True)
    scene cg d1_uv_ending behind credits with dissolve2:
        zoom 1.2
        anchor (0.1,0.1)
        linear 12 anchor (0.0,0.0)
    $ renpy.pause(4, hard=True)
    scene cg epilogue_uv_dv_ending behind credits with flash2
    $ renpy.pause(2, hard=True)
    scene cg epilogue_uv_sl_ending behind credits with dissolve
    $ renpy.pause(2, hard=True)
    scene cg epilogue_uv_un_ending behind credits with dissolve
    $ renpy.pause(2, hard=True)
    scene cg epilogue_uv_us_ending behind credits with dissolve
    $ renpy.pause(2, hard=True)
    scene cg epilogue_uv_mi_ending behind credits with dissolve
    $ renpy.pause(2, hard=True)
    scene cg epilogue_uv_uv_ending behind credits with dissolve
    $ renpy.pause(2, hard=True)

    scene black
    with dissolve2

    stop music fadeout 3

    $ renpy.pause(4, hard=True)

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
