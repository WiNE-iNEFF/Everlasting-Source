
python early:
    mods = {}
    mod_tags = {}
    filters = {}

init -1001:

    transform backdrop_trans:
        xalign -0.2
        linear 2.0 xalign 0.0
        pause 3.0

    transform achievement_trans:
        align (1.1, 0.97)
        ease 1.0 align (0.85, 0.97)
        ease 0.5 align (0.95, 0.97)
        pause 1.5
        ease 0.5 align (1.5, 0.97)

    transform lang_ru_ground:
        align (0.5, 0.2)
        ease 0.5 align (0.2, 0.2)
        linear 1.0 align (1.6, 0.2)

    transform lang_ru_hover:
        align (0.5, 0.2)
        pause 1.5
        ease 1.0 align (0.5, 0.2)
        linear 1.5 zoom 1.5
        pause 1.5

    transform lang_en_ground:
        align (0.5, 0.3)
        ease 0.5 align (0.2, 0.3)
        linear 1.0 align (1.6, 0.3)

    transform lang_en_hover:
        align (0.5, 0.3)
        pause 1.5
        ease 1.0 align (0.5, 0.3)
        linear 1.5 zoom 1.5
        pause 1.5

    transform lang_es_ground:
        align (0.5, 0.4)
        ease 0.5 align (0.2, 0.4)
        linear 1.0 align (1.6, 0.4)

    transform lang_es_hover:
        align (0.5, 045)
        pause 1.5
        ease 1.0 align (0.5, 0.4)
        linear 1.5 zoom 1.5
        pause 1.5

    transform lang_it_ground:
        align (0.5, 0.5)
        ease 0.5 align (0.2, 0.5)
        linear 1.0 align (1.6, 0.5)

    transform lang_it_hover:
        align (0.5, 0.5)
        pause 1.5
        ease 1.0 align (0.5, 0.5)
        linear 1.5 zoom 1.5
        pause 1.5

    transform lang_ch_ground:
        align (0.5, 0.7)
        ease 0.5 align (0.2, 0.7)
        linear 1.0 align (1.6, 0.7)

    transform lang_ch_hover:
        align (0.5, 0.7)
        pause 1.5
        ease 1.0 align (0.5, 0.7)
        linear 1.5 zoom 1.5
        pause 1.5

    transform lang_fr_ground:
        align (0.5, 0.6)
        ease 0.5 align (0.2, 0.6)
        linear 1.0 align (1.6, 0.6)

    transform lang_fr_hover:
        align (0.5, 0.6)
        pause 1.5
        ease 1.0 align (0.5, 0.6)
        linear 1.5 zoom 1.5
        pause 1.5

    image backdrop_back = "images/anim/backdrop/back.jpg"

    image backdrop_new:
        pause 0.1
        "images/anim/backdrop/1.png"
        pause 0.1
        "images/anim/backdrop/2.png"
        pause 0.1
        "images/anim/backdrop/3.png"
        pause 0.1
        "images/anim/backdrop/2.png"
        repeat

    $ style.backdrop_text = Style(style.default)
    $ style.backdrop_text.color = "#fff"
    $ style.backdrop_text.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.backdrop_text.drop_shadow_color = "#000"
    $ style.backdrop_text.italic = False
    $ style.backdrop_text.bold = False
    $ style.backdrop_text.size = 140

init 5 python:

    ach_table = {
        "main_bad" : {
            None : "main_bad",
            "english" : "main_bad",
            "spanish" : "main_bad",
            "italian" : "main_bad",
            "chinese" : "main_bad_ch",
            "latvian" : "main_bad",
            "french" : "main_bad"
            },
        "main_good" : {
            None : "main_good",
            "english" : "main_good_en",
            "spanish" : "main_good_en",
            "italian" : "main_good_en",
            "chinese" : "main_good_ch",
            "latvian" : "main_good",
            "french" : "main_good_fr"
            },
        "mi" : {
            None : "mi",
            "english" : "mi",
            "spanish" : "mi",
            "italian" : "mi",
            "chinese" : "mi_ch",
            "latvian" : "mi",
            "french" : "mi"
            },
        "un_bad" : {
            None : "un_bad",
            "english" : "un_bad_en",
            "spanish" : "un_bad_es",
            "italian" : "un_bad_it",
            "chinese" : "un_bad_ch",
            "latvian" : "un_bad",
            "french" : "un_bad_fr"
            },
        "un_good" : {
            None : "un_good",
            "english" : "un_good_en",
            "spanish" : "un_good_es",
            "italian" : "un_good_it",
            "chinese" : "un_good_ch",
            "latvian" : "un_good",
            "french" : "un_good_fr"
            },
        "us_bad" : {
            None : "us_bad",
            "english" : "us_bad_en",
            "spanish" : "us_bad_es",
            "italian" : "us_bad_it",
            "chinese" : "us_bad_ch",
            "latvian" : "us_bad",
            "french" : "us_bad_fr"
            },
        "us_good" : {
            None : "us_good",
            "english" : "us_good_en",
            "spanish" : "us_good_es",
            "italian" : "us_good_it",
            "chinese" : "us_good_ch",
            "latvian" : "us_good",
            "french" : "us_good_fr"
            },
        "dv_bad" : {
            None : "dv_bad",
            "english" : "dv_bad_en",
            "spanish" : "dv_bad_es",
            "italian" : "dv_bad_it",
            "chinese" : "dv_bad_ch",
            "latvian" : "dv_bad",
            "french" : "dv_bad_fr"
            },
        "dv_good" : {
            None : "dv_good",
            "english" : "dv_good_en",
            "spanish" : "dv_good_es",
            "italian" : "dv_good_it",
            "chinese" : "dv_good_ch",
            "latvian" : "dv_good",
            "french" : "dv_good_fr"
            },
        "sl_bad" : {
            None : "sl_bad",
            "english" : "sl_bad_en",
            "spanish" : "sl_bad_es",
            "italian" : "sl_bad_it",
            "chinese" : "sl_bad_ch",
            "latvian" : "sl_bad",
            "french" : "sl_bad_fr"
            },
        "sl_good" : {
            None : "sl_good",
            "english" : "sl_good_en",
            "spanish" : "sl_good_en",
            "italian" : "sl_good_en",
            "chinese" : "sl_good_ch",
            "latvian" : "sl_good",
            "french" : "sl_good_fr"
            },
        "uv_city" : {
            None : "uv_city",
            "english" : "uv_city",
            "spanish" : "uv_city",
            "italian" : "uv_city",
            "chinese" : "uv_city_ch",
            "latvian" : "uv_city",
            "french" : "uv_city_fr"
            },
        "uv_unknown_fucken_shit" : {
            None : "uv_good",
            "english" : "uv_good_en",
            "spanish" : "uv_good_es",
            "italian" : "uv_good_it",
            "chinese" : "uv_good_ch",
            "latvian" : "uv_good",
            "french" : "uv_good_fr"
            }
        }



    import renpy.store as store

    def show_achievement(img):
        renpy.play(sfx_achievement)
        renpy.show(ach_table[img][_preferences.language], [achievement_trans], layer="overlay")
        renpy.pause(3.5)
        renpy.hide(ach_table[img][_preferences.language])

    class FunctionCallback(Action):
        def __init__(self,function,*arguments):
            self.function=function
            self.arguments=arguments
        def __call__(self):
            return self.function(self.arguments)

    def on_load_callback(slot):
        try:
            if persistent.on_save_timeofday[slot]:
                persistent.timeofday = persistent.on_save_timeofday[slot][0]
                persistent.sprite_time = persistent.on_save_timeofday[slot][1]
                persistent.font_size = persistent.on_save_timeofday[slot][2]
                
                _preferences.volumes['music'] = persistent.on_save_timeofday[slot][3]
                _preferences.volumes['sfx'] = persistent.on_save_timeofday[slot][4]
                _preferences.volumes['voice'] = persistent.on_save_timeofday[slot][5]
        
        except:
            pass

    def on_save_callback(slot):
        if not persistent.on_save_timeofday:
            persistent.on_save_timeofday={}
        
        persistent.on_save_timeofday[slot] = (persistent.timeofday, persistent.sprite_time, persistent.font_size, _preferences.volumes['music'], _preferences.volumes['sfx'], _preferences.volumes['voice'])

    def do_rollback(cnt):
        if not d2_cardgame_block_rollback:
            k=cnt[0]
            renpy.rollback(True, k+1)



    def new_chapter(day_number,chapter_name="",mode="adv",music_stop=False):
        global save_name
        global _window_subtitle
        
        
        
        
        renpy.scene()
        renpy.show("bg black")
        renpy.pause(0.5)
        
        if backdrop == "prologue":
            
            
            
            pass
        elif backdrop == "epilogue":
            
            renpy.show("backdrop_back")
            renpy.show("day_num",what=Text(translation_new["DayX"],style=style.backdrop_text,ypos=0.46,xpos=0.46))
            renpy.show("backdrop_new")
            renpy.transition(dissolve)
            renpy.pause(1.0)
        else:
            dn = translation_new["DayN"]+u' %d'%(day_number)
            
            renpy.show("backdrop_back")
            renpy.show("day_num",what=Text(dn,style=style.backdrop_text,ypos=0.46,xpos=0.46))
            renpy.show("backdrop_new")
            renpy.transition(dissolve)
            renpy.pause(1.0)
            if backdrop == "dv":
                renpy.show("dv normal pioneer", [backdrop_trans])
                renpy.transition(dissolve)
                renpy.pause(2.0)
            if backdrop == "us":
                renpy.show("us normal pioneer", [backdrop_trans])
                renpy.transition(dissolve)
                renpy.pause(2.0)
            if backdrop == "sl":
                renpy.show("sl normal pioneer", [backdrop_trans])
                renpy.transition(dissolve)
                renpy.pause(2.0)
            if backdrop == "un":
                renpy.show("un normal pioneer", [backdrop_trans])
                renpy.transition(dissolve)
                renpy.pause(2.0)
        
        
        
        
        if music_stop:
            for i in range(0,8):
                renpy.music.stop(channel=i)
        if day_number != -1 and day_number != 0:
            dn = translation_new["DayN"]+u' %d'%(day_number)
            save_name = chapter_name
        
        
        else:
            pass
            
            save_name = chapter_name
        
        
        
        
        if  backdrop != "prologue":
            renpy.pause(3.0)
            renpy.scene()
            renpy.show("bg black")
            renpy.transition(dissolve)
            renpy.pause(2.0)
        
        if (mode=="adv") :
            set_mode_adv()
        else:
            set_mode_nvl()

    def disable_all_zones():
        store.map.disable_all_zones()
    def enable_all_zones():
        store.map.enable_all_zones()
    def set_zone(name,label):
        store.map.set_zone(name,label)
    def reset_zone(name):
        store.map.reset_zone(name)
    def enable_empty_zone(name):
        store.map.enable_empty_zone(name)
    def reset_current_zone():
        store.map.reset_current_zone()
    def disable_current_zone():
        store.map.disable_current_zone()
    def been_there():
        return store.map.been_there()
    def set_chibi(name,ch):
        store.map.set_chibi(name,ch)
    def reset_chibi(name):
        store.map.reset_chibi(name)
    def show_map():
        ui.jumps("_show_map")()

    def day_time():
        any_time('day')
        persistent.timeofday='day'
    def sunset_time():
        any_time('sunset')
        persistent.timeofday='sunset'
    def night_time():
        any_time('night')
        persistent.timeofday='night'
    def prolog_time():
        any_time('prolog')
        persistent.timeofday='prologue'


    def init_map_zones():
        init_map_zones_realization(store.map_zones,"nothing_here")

    def possible_skip(text, lbl):
        if  skip_text_blocks:
            say("",text)
            ui.jumps(lbl)()

    real_map_event = renpy.display.behavior.map_event
    my_map_event = lambda ev, name: False
    real_renpy_run = renpy.display.behavior.run
    my_renpy_run = lambda name: True

    def nonsafe_noskip_mode():
        
        
        
        
        renpy.display.behavior.map_event = my_map_event
        renpy.display.behavior.run = my_renpy_run

    def nonsafe_skip_mode():
        renpy.display.behavior.map_event = real_map_event
        renpy.display.behavior.run = real_renpy_run



    real_sound_play = renpy.sound.play




label start:
    $ renpy.music.stop()
    $ skip_text_blocks = True
    $ renpy.block_rollback()


    $ init_map_zones()

    python:
        if persistent.jump_to:
            j = persistent.jump_to
            persistent.jump_to = False
            renpy.jump(j)



    jump prologue

label splashscreen:

    python:



        if not persistent.set_volumes:
            
            persistent.lan_chosen = False
            persistent.licensed = False
            
            persistent.timeofday='prologue'
            persistent.firstrun = False
            persistent.choices = []
            
            persistent.show_achievements = True
            
            persistent.show_hentai_ach = False
            
            _preferences.language = None
            
            persistent.set_volumes = True
            persistent.achievement = True
            persistent.collector = True
            
            persistent.font_size = "small"
            persistent.hentai = False
            
            _preferences.volumes['music'] = .65
            _preferences.volumes['sfx'] = 1.0
            _preferences.volumes['voice'] = .75
            
            persistent.lmr_hide = False

    jump splashscreen_2

label splashscreen_2:

    $ prolog_time()

    if not persistent.lan_chosen:

        scene black

        python:
            ui.imagebutton("images/misc/russian_ground.png", "images/misc/russian_hover.png", clicked = ui.returns("None"), align = (0.5, 0.2))

            ui.imagebutton("images/misc/english_ground.png", "images/misc/english_hover.png", clicked = ui.returns("english"), align = (0.5, 0.3))

            ui.imagebutton("images/misc/spanish_ground.png", "images/misc/spanish_hover.png", clicked = ui.returns("spanish"), align = (0.5, 0.4))

            ui.imagebutton("images/misc/italian_ground.png", "images/misc/italian_hover.png", clicked = ui.returns("italian"), align = (0.5, 0.5))

            ui.imagebutton("images/misc/french_ground.png", "images/misc/french_hover.png", clicked = ui.returns("french"), align = (0.5, 0.6))

            ui.imagebutton("images/misc/chinese_ground.png", "images/misc/chinese_hover.png", clicked = ui.returns("chinese"), align = (0.5, 0.7))

            result = ui.interact()
            if result == "None":
                _preferences.language = None
                renpy.show("ru_hover", [lang_ru_hover])
                renpy.show("en_ground", [lang_en_ground])
                renpy.show("es_ground", [lang_es_ground])
                renpy.show("it_ground", [lang_it_ground])
                renpy.show("fr_ground", [lang_fr_ground])
                renpy.show("ch_ground", [lang_ch_ground])
            elif result == "english":
                _preferences.language = "english"
                renpy.show("ru_ground", [lang_ru_ground])
                renpy.show("en_hover", [lang_en_hover])
                renpy.show("es_ground", [lang_es_ground])
                renpy.show("it_ground", [lang_it_ground])
                renpy.show("fr_ground", [lang_fr_ground])
                renpy.show("ch_ground", [lang_ch_ground])
            elif result == "spanish":                                   
                _preferences.language = "spanish"
                renpy.show("ru_ground", [lang_ru_ground])
                renpy.show("en_ground", [lang_en_ground])
                renpy.show("es_hover", [lang_es_hover])
                renpy.show("it_ground", [lang_it_ground])
                renpy.show("fr_ground", [lang_fr_ground])
                renpy.show("ch_ground", [lang_ch_ground])
            elif result == "italian":                                   
                _preferences.language = "italian"
                renpy.show("ru_ground", [lang_ru_ground])
                renpy.show("en_ground", [lang_en_ground])
                renpy.show("es_ground", [lang_es_ground])
                renpy.show("it_hover", [lang_it_hover])
                renpy.show("fr_ground", [lang_fr_ground])
                renpy.show("ch_ground", [lang_ch_ground])
            elif result == "french":                                   
                _preferences.language = "french"
                renpy.show("ru_ground", [lang_ru_ground])
                renpy.show("en_ground", [lang_en_ground])
                renpy.show("es_ground", [lang_es_ground])
                renpy.show("it_ground", [lang_it_ground])
                renpy.show("fr_hover", [lang_fr_hover])
                renpy.show("ch_ground", [lang_ch_ground])
            elif result == "chinese":                                   
                _preferences.language = "chinese"
                renpy.show("ru_ground", [lang_ru_ground])
                renpy.show("en_ground", [lang_en_ground])
                renpy.show("es_ground", [lang_es_ground])
                renpy.show("it_ground", [lang_it_ground])
                renpy.show("fr_ground", [lang_fr_ground])
                renpy.show("ch_hover", [lang_ch_hover])




            persistent.lan_chosen = True

        $ renpy.pause(4.5, hard=True)

        if _preferences.language != None:
            $ renpy.utter_restart()

    if not persistent.licensed:


        if _preferences.language == "chinese":
            $ main_font = "fonts/STZHONGS.ttf"
            $ header_font = "fonts/STZHONGS.ttf"
            $ link_font = "fonts/STZHONGS.ttf"

        $ renpy.show_screen("license")

        $ renpy.pause(hard=True)

        scene black

        $ persistent.licensed = True




    scene black with dissolve
    pause(1)
    scene soviet_games
    with dissolve
    pause(1)

    if _preferences.language == None:
        if persistent.achievement:
            play sound sfx_achievement
            show achievement:
                align (1.1, 0.97)
                ease 1.0 align (0.85, 0.97)
                ease 0.5 align (0.95, 0.97)
                pause 1.5
                ease 0.5 align (1.5, 0.97)
            $ persistent.achievement = False

    if not persistent.firstrun and not config.developer:
        $ renpy.pause(3.5, hard = True)
    elif True:
        pause(3.5)

    if _preferences.language == None:
        scene disclaimer
        with dissolve
    elif _preferences.language == "english":
        scene disclaimer_en
        with dissolve
    elif _preferences.language == "spanish":
        scene disclaimer_es
        with dissolve
    elif _preferences.language == "italian":
        scene disclaimer_it
        with dissolve
    elif _preferences.language == "chinese":
        scene disclaimer_ch
        with dissolve
    elif _preferences.language == "french":
        scene disclaimer_fr
        with dissolve
    if not persistent.firstrun and not config.developer:
        $ renpy.pause(20, hard = True)
    elif True:
        pause(20)
    pause

    $ persistent.licensed = True

    pause(1)

    $ persistent.firstrun = True

    python:
        from time import localtime, strftime
        t = strftime("%H:%M:%S", localtime())
        hour, min, sec = t.split(":")
        hour = int(hour)

    if hour in [22,23,24,0,1,2,3,4,5,6]:
        scene splashscreen_night with dissolve:
            pos (0,0)
            linear 4.0 pos (0,-1080)
        $ renpy.pause(4)
        show logo_night with dissolve2:
            pos (400,150)
        $ renpy.pause(3)

    elif hour in [20,21] or hour in [7,8]:
        scene splashscreen_sunset with dissolve:
            pos (0,0)
            linear 4.0 pos (0,-1080)
        $ renpy.pause(4)
        show logo_sunset with dissolve2:
            pos (400,150)
        $ renpy.pause(3)
    elif True:

        scene splashscreen_day with dissolve:
            pos (0,0)
            linear 4.0 pos (0,-1080)
        $ renpy.pause(4)
        show logo_day with dissolve2:
            pos (400,150)
        $ renpy.pause(3)









    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
