init:

    $ mods["agr_main_menu"] = u"{font=[ag_font]}{color=#FF4500}Послесвечение: Ремастер{/font}{/color}"


label agr_main_menu:

    scene black with dissolve
    scene ag_mm_bg at agr_splashscreen
    show screen agr_splashscreen_text
    with dissolve
    $ renpy.pause(6, hard=True)
    $ agr_screens_save_activate()
    $ sunset_time()


screen agr_splashscreen_text:
    text _("AFTERGLOW: REMASTERED"):
        xalign 0.5 ypos 0.5
        size 100
        font ag_typewriter
        drop_shadow [ (2, 2), (2, 2), (2, 2), (2, 2) ]
        drop_shadow_color "#000"


transform agr_splashscreen:
    zoom 2.0 truecenter
    pause 2
    ease 4.0 zoom 1.0 
