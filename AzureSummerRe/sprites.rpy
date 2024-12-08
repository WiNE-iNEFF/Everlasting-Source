init 2:
    #LAZUR SUMMER SPRITES

    image mi smile long hair night = im.MatrixColor( im.Composite((900,1080), (0,0), "mods/LS/sprites/lazur_summer/normal/mi/mi_3_body_loo.png",(0,0), "mods/LS/sprites/lazur_summer/normal/mi/mi_3_casual.png",(0,0), "mods/LS/sprites/lazur_summer/normal/mi/mi_3_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) )
    image mi dress sad night = im.MatrixColor( im.Composite((900,1080), (0,0), "mods/LS/sprites/lazur_summer/normal/mi/mi_2_body_loo.png",(0,0), "mods/LS/sprites/lazur_summer/normal/mi/mi_2_dress.png",(0,0), "mods/LS/sprites/lazur_summer/normal/mi/mi_sad_3.png"), im.matrix.tint(0.63, 0.78, 0.82) )

    image mi dress = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900,1080), (0,0), "mods/LS/sprites/lazur_summer/normal/mi/mi_3_body_loo.png",(0,0), "mods/LS/sprites/lazur_summer/normal/mi/mi_3_dress.png",(0,0), "mods/LS/sprites/lazur_summer/normal/mi/mi_3_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900,1080), (0,0), "mods/LS/sprites/lazur_summer/normal/mi/mi_3_body_loo.png",(0,0), "mods/LS/sprites/lazur_summer/normal/mi/mi_3_dress.png",(0,0), "mods/LS/sprites/lazur_summer/normal/mi/mi_3_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ))