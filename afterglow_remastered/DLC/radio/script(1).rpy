init 1:

    $ radio_stations = {}

    $ radio_stations["radio_noise"] =         "afterglow_remastered/DLC/radio/radio_dir/audio/noise.mp3"
    $ radio_stations["radio_red"] =           "afterglow_remastered/DLC/radio/radio_dir/red.mp3"
    $ radio_stations["radio_polyanka"] =      "afterglow_remastered/DLC/radio/radio_dir/polyanka.mp3"
    $ radio_stations["radio_suicide_guy"] =   "afterglow_remastered/DLC/radio/radio_dir/suicide_guy.mp3"
    $ radio_stations["radio_other_1"] =       "afterglow_remastered/DLC/radio/radio_dir/other_1.mp3"
    $ radio_stations["radio_other_2"] =       "afterglow_remastered/DLC/radio/radio_dir/other_2.mp3"
    $ radio_stations["radio_other_3"] =       "afterglow_remastered/DLC/radio/radio_dir/other_3.mp3"
    $ radio_stations["radio_other_4"] =       "afterglow_remastered/DLC/radio/radio_dir/other_4.mp3"
    $ radio_stations["radio_other_5"] =       "afterglow_remastered/DLC/radio/radio_dir/other_5.mp3"
    $ radio_stations["radio_other_6"] =       "afterglow_remastered/DLC/radio/radio_dir/other_6.mp3"
    $ radio_stations["radio_other_7"] =       "afterglow_remastered/DLC/radio/radio_dir/other_7.mp3"
    $ radio_stations["radio_other_8"] =       "afterglow_remastered/DLC/radio/radio_dir/other_8.mp3"
    $ radio_stations["radio_other_9"] =       "afterglow_remastered/DLC/radio/radio_dir/other_9.mp3"
    $ radio_stations["radio_other_10"] =      "afterglow_remastered/DLC/radio/radio_dir/other_10.mp3"
    $ radio_stations["radio_other_11"] =      "afterglow_remastered/DLC/radio/radio_dir/other_11.mp3"
    $ radio_stations["radio_other_12"] =      "afterglow_remastered/DLC/radio/radio_dir/other_12.mp3"
    $ radio_stations["radio_other_13"] =      "afterglow_remastered/DLC/radio/radio_dir/other_13.mp3"
    $ radio_stations["radio_other_14"] =      "afterglow_remastered/DLC/radio/radio_dir/other_14.mp3"

    $ listened = []

    $ colors['rm'] = {'night': (225, 221, 125, 255), 'sunset': (225, 221, 125, 255), 'day': (225, 221, 125, 255), 'prolog': (225, 221, 125, 255)}
    $ names['rm'] = "Радист"
    $ store.names_list.append('rm')

    image bg radio = Movie(play="afterglow_remastered/DLC/radio/images/radio.webm", image="afterglow_remastered/DLC/radio/images/radio.jpg", start_image="afterglow_remastered/DLC/radio/images/radio.jpg")

    image tip tip_1 = "afterglow_remastered/DLC/radio/images/tip_1.jpg"
    image tip tip_2 = "afterglow_remastered/DLC/radio/images/tip_2.jpg"

    image alpha_black = "afterglow_remastered/DLC/radio/images/alpha_black.png"

    python:
        import datetime
        today = datetime.datetime.today().weekday() + 1


        var = 0
        rv = None
        persistent.tips = False
        persistent.rv_chk_1 = False
        persistent.rv_chk_2 = False
        persistent.rv_chk_3 = False
        persistent.rv_chk_4 = False

        def radio_random():
            global rv
            radio_take()
            renpy.music.play(rv, channel="sound")
            listened.append(rv)
            return renpy.music.queue("afterglow_remastered/DLC/radio/radio_dir/noise.mp3", channel="sound", loop=True, clear_queue=False, tight=True)

        def radio_take():
            global rv
            rv = renpy.random.choice(radio_stations.values())
            if rv in listened:
                radio_take()
            else:
                return rv

        style.r_button = Style(style.default)
        style.r_button.size = 30
        style.r_button.selected_color = "#ffffff"
        style.r_button.hover_color = "#002aff"

screen radio:
    modal True tag menu

    $ bar_full = "afterglow_remastered/DLC/radio/images/hbar_full.png"
    $ bar_null = "afterglow_remastered/DLC/radio/images/hbar_null.png"
    $ wave = var + 100

    bar value VariableValue("var", 100) left_bar bar_full right_bar bar_null thumb "images/misc/none.png" hover_thumb "images/misc/none.png" xpos 1220 ypos 326 ymaximum 111 xmaximum 625

    frame:
        background "#0018"
        xalign 0.5 ypos 50
        text _("Волна: [wave].0 FM"):
            size 30

    textbutton "Помощь":
        background "#0018"
        xpos 0 ypos 0
        text_style "r_button"
        action Call("r_tip")

    $ renpy.music.queue("afterglow_remastered/DLC/radio/radio_dir/noise.mp3", channel="sound", loop=True, clear_queue=False, tight=True)
    if var == renpy.random.choice([i for i in range(0,25)]) and persistent.rv_chk_1 == False:
        $ persistent.rv_chk_1 = True
        $ radio_random()
    if var == renpy.random.choice([i for i in range(26,50)]) and persistent.rv_chk_2 == False:
        $ persistent.rv_chk_2 = True
        $ radio_random()
    if var == renpy.random.choice([i for i in range(51,75)]) and persistent.rv_chk_3 == False:
        $ persistent.rv_chk_3 = True
        $ radio_random()
    if var == renpy.random.choice([i for i in range(76,100)]) and persistent.rv_chk_4 == False:
        $ persistent.rv_chk_4 = True
        $ radio_random()


label agr_radio:

    $ renpy.music.stop(fadeout=3)

    if persistent.dt != today:
        $ persistent.rv_chk_1 = False
        $ persistent.rv_chk_2 = False
        $ persistent.rv_chk_3 = False
        $ persistent.rv_chk_4 = False

    $ day_time()
    play ambience ambience_int_cabin_day fadein 3
    scene bg radio with dissolve

    if persistent.tips == False:
        call r_tip
        $ persistent.tips = True

    rm "Пора проверить радио."

    $ persistent.dt = datetime.datetime.today().weekday() + 1

label r_countinue:
    stop ambience fadeout 3
    call screen radio
    jump r_countinue

label r_tip:
    show alpha_black
    show tip tip_1:
        xalign 0.5 yalign 0.5
    with dissolve
    pause(5)
    show tip tip_2:
        xalign 0.5 yalign 0.5
    with dissolve
    pause(5)
    hide tip
    hide alpha_black
    with dissolve