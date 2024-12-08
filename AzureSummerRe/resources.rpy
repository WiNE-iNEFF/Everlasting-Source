init 2:
    #LAZUR SUMMER BG

    image bg ext_boathouse_sunset = "mods/LS/bg/lazur_summer/ext_boathouse_sunset.jpg"
    image bg ext_houses_night = "mods/LS/bg/lazur_summer/ext_houses_night.jpg"
    image bg ext_house_of_mi_night = "mods/LS/bg/lazur_summer/ext_house_of_mi_night.jpg"
    image bg ext_mimusicclub_night = "mods/LS/bg/lazur_summer/ext_mimusicclub_night.jpg"
    image bg ext_music_club_verandah_day = "mods/LS/bg/lazur_summer/ext_music_club_verandah_day.jpg"
    image bg ext_playground_sunset = "mods/LS/bg/lazur_summer/ext_playground_sunset.jpg"
    image bg ext_warehouse2_day = "mods/LS/bg/lazur_summer/ext_warehouse2_day.jpg"
    image bg houses_night = "mods/LS/bg/lazur_summer/houses_night.jpg"
    image bg inside_music_club_sunset = "mods/LS/bg/lazur_summer/inside_music_club_sunset.jpg"
    image bg int_wardrobe = "mods/LS/bg/lazur_summer/int_wardrobe.jpg"
    image bg lake = "mods/LS/bg/lazur_summer/lake.jpg"
    image bg palata = "mods/LS/bg/lazur_summer/palata.jpg"

    image bg cum_room = ConditionSwitch(
    "persistent.sprite_time=='sunset'", "mods/LS/bg/lazur_summer/cum_room_sunset.jpg",
    "persistent.sprite_time=='day'", "mods/LS/bg/lazur_summer/cum_room_day.jpg",
    "persistent.sprite_time=='light_night'", "mods/LS/bg/lazur_summer/cum_room_light_night.jpg",
    "persistent.sprite_time=='night'", "mods/LS/bg/lazur_summer/cum_room_night.jpg",
    True, "mods/LS/bg/lazur_summer/cum_room.jpg")
    image bg cum_hata = ConditionSwitch(
    "persistent.sprite_time=='sunset'", "mods/LS/bg/lazur_summer/cum_hata_sunset.jpg",
    "persistent.sprite_time=='day'", "mods/LS/bg/lazur_summer/cum_hata_day.jpg",
    "persistent.sprite_time=='night'", "mods/LS/bg/lazur_summer/cum_hata_night.jpg")
    image bg road_out_camp = ConditionSwitch(
    "persistent.sprite_time=='day'", "mods/LS/bg/lazur_summer/road_out_camp_day.jpg",
    "True", "mods/LS/bg/lazur_summer/road_out_camp.jpg")

    #LAZUR SUMMER MUSIC
    $ music_list["piano-sister-friede-father-ariandel"] = "mods/LS/sound/music/lazur_summer/sister-friede-father-ariandel.mp3"
    $ music_list["forest-IC3PEAK_-_Are_you_scared_I_am_not"] = "mods/LS/sound/music/lazur_summer/IC3PEAK_-_Are_you_scared_I_am_not.mp3"
    
    