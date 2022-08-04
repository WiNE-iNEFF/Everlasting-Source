init python:

    def agr_screens_save():
        renpy.display.screen.screens[("agr_old_main_menu", None)] = renpy.display.screen.screens[("main_menu", None)]
        renpy.display.screen.screens[("agr_old_say", None)] = renpy.display.screen.screens[("say", None)]

    def agr_screens_activate():
        config.window_title = u"Послесвечение: Ремастер"
        config.main_menu_music = "afterglow_remastered/sound/music/my_silent_angel.mp3"

        renpy.display.screen.screens[("main_menu", None)] = renpy.display.screen.screens[("agr_main_menu", None)]
        renpy.display.screen.screens[("say", None)] = renpy.display.screen.screens[("agr_say", None)]
        
        renpy.music.stop("ambience")
        renpy.music.stop("music")
        renpy.music.stop("sound")
        renpy.play(silent_angel, channel = "music")

    def agr_screens_default():
        config.window_title = u"Бесконечное лето"
        config.main_menu_music = "afterglow_remastered/sound/music/blow_with_the_fires.ogg"

        renpy.display.screen.screens[("main_menu", None)] = renpy.display.screen.screens[("agr_old_main_menu", None)]
        renpy.display.screen.screens[("say", None)] = renpy.display.screen.screens[("agr_old_say", None)]
        
        renpy.music.stop("ambience")
        renpy.music.stop("music")
        renpy.music.stop("sound")
        renpy.play(music_list["blow_with_the_fires"], channel = "music")

    def agr_screens_save_activate():
        agr_screens_save()
        agr_screens_activate()


    def agr_meanwhile(text="",mode="adv",music_stop=False):
        global _window_subtitle

        renpy.scene()
        renpy.show("bg black")
        renpy.pause(0.5)
        renpy.show("meanwhile",what=Text(text,style=style.agr_backdrop_text,ypos=0.5,xpos=0.5,yalign=0.5))
        renpy.transition(dissolve)
        renpy.pause(3.0)

        if music_stop:
            for i in range(0,8):
                renpy.music.stop(channel=i)

        if (mode=="adv") :
            set_mode_adv()
        else:
            set_mode_nvl()


    def try_radio():
        if renpy.has_label("agr_radio"):
            renpy.jump_out_of_context("agr_radio")
        else:
            renpy.notify("Радио-мод не установлен")


    style.agr_backdrop_text =                             Style(style.default)
    style.agr_backdrop_text.font =                        "afterglow_remastered/fonts/corbell.ttf"
    style.agr_backdrop_text.color =                       "#fff"
    style.agr_backdrop_text.drop_shadow =                 [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    style.agr_backdrop_text.drop_shadow_color =           "#000"
    style.agr_backdrop_text.italic =                      False
    style.agr_backdrop_text.bold =                        False
    style.agr_backdrop_text.size =                        140

    style.agr_credit_text =                             Style(style.default)
    style.agr_credit_text.drop_shadow =                 [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    style.agr_credit_text.drop_shadow_color =           "#000"


screen agr_main_menu:

    modal True tag menu

    add "afterglow_remastered/images/gui/mm_bg_ussr.jpg"
    add "afterglow_remastered/images/gui/text.png"

    imagebutton:
        auto "afterglow_remastered/images/gui/semen_%s.png"
        hover_sound "afterglow_remastered/sound/sfx/click_1.ogg"
        activate_sound "afterglow_remastered/sound/sfx/click_1.ogg"
        xpos 354
        ypos 393
        action [Hide("agr_main_menu", Fade(0.2, 0.0, 0.5, color="#fff")), Start("agr_semen_route")]

    imagebutton:
        auto "afterglow_remastered/images/gui/load_%s.png"
        hover_sound "afterglow_remastered/sound/sfx/click_1.ogg"
        activate_sound "afterglow_remastered/sound/sfx/click_1.ogg"
        xpos 235
        ypos 531
        action ShowMenu('load')

    imagebutton:
        auto "afterglow_remastered/images/gui/pref_%s.png"
        hover_sound "afterglow_remastered/sound/sfx/click_1.ogg"
        activate_sound "afterglow_remastered/sound/sfx/click_1.ogg"
        xpos 235
        ypos 597
        action ShowMenu('preferences')

    imagebutton:
        auto "afterglow_remastered/images/gui/quit_%s.png"
        hover_sound "afterglow_remastered/sound/sfx/click_1.ogg"
        activate_sound "afterglow_remastered/sound/sfx/click_1.ogg"
        xpos 1269
        ypos 454
        action [Hide("agr_main_menu", Fade(0.2, 0.0, 0.5, color="#fff")), (Function(agr_screens_default)), ShowMenu("main_menu")]

    imagebutton:
        auto "afterglow_remastered/images/gui/vk_%s.png"
        hover_sound "afterglow_remastered/sound/sfx/click_1.ogg"
        activate_sound "afterglow_remastered/sound/sfx/click_1.ogg"
        xpos 1212
        ypos 807
        action OpenURL("https://m.vk.com/poslesvet1989")

    imagebutton:
        auto "afterglow_remastered/images/gui/radio_%s.png"
        hover_sound "afterglow_remastered/sound/sfx/click_1.ogg"
        activate_sound "afterglow_remastered/sound/sfx/click_1.ogg"
        xpos 1443
        ypos 39
        action [Function(try_radio)]

    add AgTrackCursor("afterglow_remastered/images/gui/dust_1.png", 14):
        zoom 1.2
    
screen agr_say:

    window background None id "window":

        $ timeofday = persistent.timeofday

        if persistent.font_size == "large":

            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/backward_%s.png") xpos 38 ypos 924 action ShowMenu("text_history")

            add get_image("gui/dialogue_box/"+timeofday+"/dialogue_box_large.png") xpos 174 ypos 866

            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/hide_%s.png") xpos 1508 ypos 883 action HideInterface()
            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/save_%s.png") xpos 1567 ypos 883 action ShowMenu('save')
            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/menu_%s.png") xpos 1625 ypos 883 action ShowMenu('game_menu_selector')
            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/load_%s.png") xpos 1682 ypos 883 action ShowMenu('load')

            if not config.skipping:
                imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/forward_%s.png") xpos 1768 ypos 924 action Skip()
            else:
                imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/fast_forward_%s.png") xpos 1768 ypos 924 action Skip()

            text what id "what" xpos 194 ypos 914 xmaximum 1541 size 35 line_spacing 1
            if who:
                text who id "who" xpos 194 ypos 877 size 35 line_spacing 1

        elif persistent.font_size == "small":

            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/backward_%s.png") xpos 38 ypos 949 action ShowMenu("text_history")

            add get_image("gui/dialogue_box/"+timeofday+"/dialogue_box.png") xpos 174 ypos 916

            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/hide_%s.png") xpos 1508 ypos 933 action HideInterface()
            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/save_%s.png") xpos 1567 ypos 933 action ShowMenu('save')
            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/menu_%s.png") xpos 1625 ypos 933 action ShowMenu('game_menu_selector')
            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/load_%s.png") xpos 1682 ypos 933 action ShowMenu('load')

            if not config.skipping:
                imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/forward_%s.png") xpos 1768 ypos 949 action Skip()
            else:
                imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/fast_forward_%s.png") xpos 1768 ypos 949 action Skip()

            text what id "what" xpos 194 ypos 964 xmaximum 1541 size 28 line_spacing 2
            if who:
                text who id "who" xpos 194 ypos 931 size 28 line_spacing 2

    if karta_otkrytie == True:
        key "m" action ShowMenu("agr_map")
        key "M" action ShowMenu("agr_map")
        key "ь" action ShowMenu("agr_map")
        key "Ь" action ShowMenu("agr_map")

screen agr_map:
    modal False tag map

    if karta == True:
        add "afterglow_remastered/images/misc/karta_lagerya.png" at map_atl
    else:
        add "afterglow_remastered/images/misc/karta_lagerya_2.png" at map_atl

    key "K_ESCAPE" action Return()
    key "m" action Return()
    key "M" action Return()
    key "ь" action Return()
    key "Ь" action Return()

screen agr_scripted_map:
    modal True tag map

    imagemap:
        auto "afterglow_remastered/images/misc/village_map_%s.png" at map_atl

        if ring == False:
            hotspot(284,248,257,224) clicked Jump("w_dome_kolco")
        if hospital == False:
            hotspot(1294,121,204,287) clicked Jump("bolnica_lekarstwa")
        if storage == False:
            hotspot(1510,408,96,96) clicked Jump("sklad")

transform map_atl:
    xalign 0.5 yalign 0.5 ypos 1
    ease 0.6 ypos 0.5
