
init python:


    # Спрайты

    ag_img = "afterglow_remastered/images/"
    ag_es_img = "images/"

    persistent.easter_egg = False # Оч важная херь. Лучше не трогать

    ag_tint = {
        "sunset":im.matrix.tint(0.94, 0.82, 1.0),
        "night":im.matrix.tint(0.63, 0.78, 0.82)
    }


    emotion_to_pose = {
        'dv': {
            'cry': 1, 'scared': 1, 'shocked': 1, 'surprise': 1, 'grin': 2, 'guilty': 3, 'shy': 3, 'sad': 3, 'shy_smile': 3, 'laugh': 4, 'normal': 4, 'smile': 4, 'angry': 5, 'rage': 5,
        },
        'cs': {
            'normal': 1, 'shy': 1, 'smile': 1, 'sad': 1, 'fear': 1,
        },
        'ba': {
            'normal': 1, 'angry': 1, 'rage': 1, 'serious': 1, 'smile': 1,
        },
        'el': {
            'hs_normal': 1, 'hs_smile': 1, 'normal': 1, 'grin': 1, 'smile': 1, 'fingal': 2, 'sad': 2, 'scared': 2, 'shocked': 2, 'surprise': 2, 'upset': 2, 'angry': 3, 'laugh': 3, 'serious': 3,
        },
        'sh': {
            'laugh': 1, 'scared': 1, 'smile': 1, 'upset': 1, 'cry': 2, 'normal_smile': 2, 'rage': 2, 'normal': 3, 'serious': 3, 'surprise': 3,
        },
        'sl': {
            'normal': 1, 'serious': 1, 'smile': 1, 'happy': 2, 'laugh': 2, 'shy': 2, 'smile2': 2, 'angry': 3, 'sad': 3, 'surprise': 3, 'scared': 4, 'tender': 4,
        },
        'un': {
            'normal': 1, 'angry': 1, 'evil_smile': 1, 'shy': 1, 'smile': 1, 'smile2': 1, 'cry': 2, 'cry_smile': 2, 'sad': 2, 'scared': 2, 'shocked': 2, 'surprise': 2, 'angry2': 3, 'grin': 3, 'laugh': 3, 'rage': 3, 'serious': 3, 'smile3': 3,
        },
        'mi': {
            'cry': 1, 'dontlike': 1, 'laugh': 1, 'scared': 1, 'shocked': 1, 'surprise': 1, 'shy': 1, 'grin': 2, 'cry_smile': 2, 'sad': 2, 'happy': 2, 'smile': 2, 'angry': 3, 'normal': 3, 'rage': 3, 'serious': 3, 'upset': 3,
        },
        'mt': {
            'normal': 1, 'sad': 1, 'smile': 1, 'surprise': 1, 'angry': 2, 'rage': 2, 'shocked': 2, 'grin': 3, 'laugh': 3, 'scared': 3,
        },
        'ir': {
            'normal': 1, 'shock': 1, 'surprise': 1,
        },
    }


    distance_to_position = {
        "far": (630, 1080),
        "normal": (900, 1080),
        "close": (1050, 1080)
    }


    def _sprite_for_all_times(full_sprite_name, composite_image):
        """
        Объявляем спрайт для всех времен суток
        """
        renpy.image(
            full_sprite_name,
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(composite_image, ag_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(composite_image, ag_tint["night"]),
                True, composite_image,
            )
        )


    def make_sprites_for(character, sprite_name, layers, emotions=None, distances=None, exclude=None, sprite_define_func=None, default=True):
        """
        Позволяет объявить почти любой спрайт, состоящий из нескольких слоев,
        каждый слой может идти либо из мода, либо из оригинала.
        Картинки должны класться в папки строго как в оригинале, чтобы это работало.
        Честно спизжено с мода Булки, Кефир и Рок'н Ролл
        """

        if emotions is None:
            emotions = emotion_to_pose[character].keys()
        if distances is None:
            distances = distance_to_position.keys()
        if sprite_define_func is None:
            sprite_define_func = _sprite_for_all_times

        for emotion in emotions:
            if exclude and emotion in exclude:
                continue

            pose = emotion_to_pose[character][emotion]

            for distance in distances:
                # Получаем название спрайта
                full_sprite_name = '%s %s %s' % (character, emotion, sprite_name)
                if not sprite_name:
                    full_sprite_name = '%s %s' % (character, emotion)  # Не у всех есть одежда
                if distance != 'normal':
                    full_sprite_name += ' ' + distance

                # Комбинируем изображение
                image_parts = [distance_to_position[distance]]
                for layer in layers:
                    source, file_name = layer.split(':')
                    base_path = ag_img if source == 'mod' else ag_es_img
                    if default:
                        image_path = base_path + "sprites/%s/%s/%s_%s_%s.png" % (
                            distance, character, character, pose, file_name if file_name != '<emotion>' else emotion,
                        )
                    else:
                        image_path = base_path + "sprites/%s/%s/old/%s_%s_%s.png" % (
                            distance, character, character, pose, file_name if file_name != '<emotion>' else emotion,
                        )
                    image_parts += [(0, 0), image_path]
                composite_image = im.Composite(*image_parts)

                # Объявляем спрайт
                sprite_define_func(full_sprite_name, composite_image)


    def make_sprites_with_custom_emotions(custom_emotions, *args):
        """
        Удобно, когда нужно объявить новую эмоцию
        """
        args = list(args)
        assert args[-1][-1] == 'es:<emotion>'
        make_sprites_for(*args, exclude=custom_emotions)
        args[-1][-1] = 'mod:<emotion>'
        make_sprites_for(*args, emotions=custom_emotions)


    # Объявляем спрайты

    make_sprites_for('dv', 'coat', ['es:body', 'mod:coat', 'es:<emotion>'])
    make_sprites_for('dv', 'coat gasmask', ['es:body', 'mod:coat', 'es:<emotion>', 'mod:gasmask'])
    make_sprites_for('dv', 'booba', ['es:body', 'mod:booba', 'es:<emotion>'])
    make_sprites_for('dv', 'ag_sport', ['es:body', 'mod:ag_sport', 'es:<emotion>'])

    make_sprites_for('sl', 'coat', ['es:body', 'mod:coat', 'es:<emotion>'])

    make_sprites_for('un', 'coat', ['es:body', 'mod:coat', 'es:<emotion>'])

    make_sprites_for('mi', 'jacket', ['es:body', 'mod:jacket', 'es:<emotion>'])

    make_sprites_for('mt', 'sport', ['es:body', 'mod:sport', 'es:<emotion>'])

    make_sprites_for('ba', 'uniform', ['mod:body', 'mod:uniform', 'mod:<emotion>'], distances=['normal'])

    make_sprites_for('cs', 'ag_civil', ['mod:ag_civil', 'es:<emotion>'])

    make_sprites_for('ir', 'pioneer', ['mod:body', 'mod:pioneer', 'mod:<emotion>'])

    make_sprites_for('sh', 'shirt', ['mod:shirt', 'es:<emotion>'])

    make_sprites_for('el', 'hazmat_suit', ['mod:hs', 'mod:<emotion>'], distances=['normal'])
    make_sprites_for('el', 'gas_mask', ['mod:hs', 'mod:<emotion>', 'mod:gasmask'], distances=['normal'])
    make_sprites_for('el', 'shirt', ['mod:shirt', 'es:<emotion>'])



    make_sprites_with_custom_emotions(['shy_smile'], 'dv', 'booba', ['es:body', 'mod:booba', 'es:<emotion>'])
    make_sprites_with_custom_emotions(['shy_smile'], 'dv', 'ag_sport', ['es:body', 'mod:ag_sport', 'es:<emotion>'])
    make_sprites_with_custom_emotions(['shy_smile'], 'dv', 'coat', ['es:body', 'mod:coat', 'es:<emotion>'])

    make_sprites_with_custom_emotions(['fear'], 'cs', 'med_gown', ['es:body', 'es:<emotion>'])



init 1:

    # Однослойные спрайты или те которые я заебался объявлять через функцию и они не работали

    image sh normal gas_mask = im.MatrixColor(im.Composite((900,1080), (0,0), ag_img + "sprites/other/sh_3_gas_mask.png"), im.matrix.tint(0.63, 0.78, 0.82))
    image sh2 normal gas_mask = im.MatrixColor(im.Composite((900,1080), (0,0), ag_img + "sprites/other/sh_3_gas_mask.png"), im.matrix.opacity(0.35))

    image sh2 normal pioneer_opas = im.MatrixColor(im.Composite((900,1080), (0,0), "images/sprites/normal/sh/sh_3_body.png",(0,0), "images/sprites/normal/sh/sh_3_normal.png"), im.matrix.opacity(0.35))

    image dv anim_shy pioneer:
        "dv shy pioneer" with dspr
        pause(4)
        "dv sad pioneer" with dspr
        pause(0.75)
        "dv guilty pioneer" with dspr
        pause(5)
        "dv shy pioneer" with dspr
        pause(1.75)
        "dv guilty pioneer" with dspr
        pause(3)
        repeat

    image boy dead pi = im.MatrixColor(ag_img + "sprites/other/white_pioneer_boy.png", ag_tint["night"])
    image girl dead pi = im.MatrixColor(ag_img + "sprites/other/white_pioneer_girl.png", ag_tint["night"])



    image dv cry pioneer = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(ag_img + "sprites/other/dv_cry2_pioneer.png", ag_tint["sunset"]),
        "persistent.sprite_time == 'night'", im.MatrixColor(ag_img + "sprites/other/dv_cry2_pioneer.png", ag_tint["night"]),
        True, ag_img + "sprites/other/dv_cry2_pioneer.png")

    image dv sad wet_pioneer = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(ag_img + "sprites/other/dv_sad_pioneer3.png", ag_tint["sunset"]),
        "persistent.sprite_time == 'night'", im.MatrixColor(ag_img + "sprites/other/dv_sad_pioneer3.png", ag_tint["night"]),
        True, ag_img + "sprites/other/dv_sad_pioneer3.png")


    image sh normal hazmat_suit = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/sh/sh_hs_normal.png"), ag_tint["sunset"]),
        "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/sh/sh_hs_normal.png"), ag_tint["night"]),
        True,im.Composite((900,1080), (0,0), ag_img + "sprites/normal/sh/sh_hs_normal.png") )

    image sh serious hazmat_suit = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/sh/sh_hs_serious.png"), ag_tint["sunset"]),
        "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/sh/sh_hs_serious.png"), ag_tint["night"]),
        True,im.Composite((900,1080), (0,0), ag_img + "sprites/normal/sh/sh_hs_serious.png") )

    image sh surprise hazmat_suit = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/sh/sh_hs_surprise.png"), ag_tint["sunset"]),
        "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/sh/sh_hs_surprise.png"), ag_tint["night"]),
        True,im.Composite((900,1080), (0,0), ag_img + "sprites/normal/sh/sh_hs_surprise.png") )

    image sh scared hazmat_suit = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/sh/sh_hs_scared.png"), ag_tint["sunset"]),
        "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/sh/sh_hs_scared.png"), ag_tint["night"]),
        True,im.Composite((900,1080), (0,0), ag_img + "sprites/normal/sh/sh_hs_scared.png") )

    image sh normal_smile hazmat_suit = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/sh/sh_hs_normal_smile.png"), ag_tint["sunset"]),
        "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/sh/sh_hs_normal_smile.png"), ag_tint["night"]),
        True,im.Composite((900,1080), (0,0), ag_img + "sprites/normal/sh/sh_hs_normal_smile.png") )

    image sh normal gas_mask_on = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/sh/sh_hs_normal_mask_on.png"), ag_tint["sunset"]),
        "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/sh/sh_hs_normal_mask_on.png"), ag_tint["night"]),
        True,im.Composite((900,1080), (0,0), ag_img + "sprites/normal/sh/sh_hs_normal_mask_on.png") )

    image sh serious gas_mask_on = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/sh/sh_hs_serious_mask_on.png"), ag_tint["sunset"]),
        "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/sh/sh_hs_serious_mask_on.png"), ag_tint["night"]),
        True,im.Composite((900,1080), (0,0), ag_img + "sprites/normal/sh/sh_hs_serious_mask_on.png") )

    image sh normal gas_mask_on close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), ag_img + "sprites/close/sh/sh_hs_normal_mask_on.png"), ag_tint["sunset"]),
        "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), ag_img + "sprites/close/sh/sh_hs_normal_mask_on.png"), ag_tint["night"]),
        True,im.Composite((1050,1080), (0,0), ag_img + "sprites/close/sh/sh_hs_normal_mask_on.png") )

    image sh serious gas_mask_on close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), ag_img + "sprites/close/sh/sh_hs_serious_mask_on.png"), ag_tint["sunset"]),
        "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), ag_img + "sprites/close/sh/sh_hs_serious_mask_on.png"), ag_tint["night"]),
        True,im.Composite((1050,1080), (0,0), ag_img + "sprites/close/sh/sh_hs_serious_mask_on.png") )


    image hl laugh_1 = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_1.png"), ag_tint["sunset"]),
        "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_1.png"), ag_tint["night"]),
        True,im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_1.png") )

    image hl idle_1 = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_1.png",(0,0), ag_img + "sprites/normal/hl/hl_idle.png"), ag_tint["sunset"]),
        "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_1.png",(0,0), ag_img + "sprites/normal/hl/hl_idle.png"), ag_tint["night"]),
        True,im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_1.png",(0,0), ag_img + "sprites/normal/hl/hl_idle.png"))

    image hl moody_1 = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_1.png",(0,0), ag_img + "sprites/normal/hl/hl_moody.png"), ag_tint["sunset"]),
        "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_1.png",(0,0), ag_img + "sprites/normal/hl/hl_moody.png"), ag_tint["night"]),
        True,im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_1.png",(0,0), ag_img + "sprites/normal/hl/hl_moody.png"))

    image hl smile_1 = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_1.png",(0,0), ag_img + "sprites/normal/hl/hl_smile.png"), ag_tint["sunset"]),
        "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_1.png",(0,0), ag_img + "sprites/normal/hl/hl_smile.png"), ag_tint["night"]),
        True,im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_1.png",(0,0), ag_img + "sprites/normal/hl/hl_smile.png"))

    image hl surprise_1 = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_1.png",(0,0), ag_img + "sprites/normal/hl/hl_surprise.png"), ag_tint["sunset"]),
        "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_1.png",(0,0), ag_img + "sprites/normal/hl/hl_surprise.png"), ag_tint["night"]),
        True,im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_1.png",(0,0), ag_img + "sprites/normal/hl/hl_surprise.png"))

    image hl wink_1 = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_1.png",(0,0), ag_img + "sprites/normal/hl/hl_wink.png"), ag_tint["sunset"]),
        "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_1.png",(0,0), ag_img + "sprites/normal/hl/hl_wink.png"), ag_tint["night"]),
        True,im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_1.png",(0,0), ag_img + "sprites/normal/hl/hl_wink.png"))

    image hl laugh_2 = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_2.png"), ag_tint["sunset"]),
        "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_2.png"), ag_tint["night"]),
        True,im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_2.png") )

    image hl idle_2 = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_2.png",(0,0), ag_img + "sprites/normal/hl/hl_idle.png"), ag_tint["sunset"]),
        "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_2.png",(0,0), ag_img + "sprites/normal/hl/hl_idle.png"), ag_tint["night"]),
        True,im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_2.png",(0,0), ag_img + "sprites/normal/hl/hl_idle.png"))

    image hl moody_2 = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_2.png",(0,0), ag_img + "sprites/normal/hl/hl_moody.png"), ag_tint["sunset"]),
        "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_2.png",(0,0), ag_img + "sprites/normal/hl/hl_moody.png"), ag_tint["night"]),
        True,im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_2.png",(0,0), ag_img + "sprites/normal/hl/hl_moody.png"))

    image hl smile_2 = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_2.png",(0,0), ag_img + "sprites/normal/hl/hl_smile.png"), ag_tint["sunset"]),
        "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_2.png",(0,0), ag_img + "sprites/normal/hl/hl_smile.png"), ag_tint["night"]),
        True,im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_2.png",(0,0), ag_img + "sprites/normal/hl/hl_smile.png"))

    image hl surprise_2 = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_2.png",(0,0), ag_img + "sprites/normal/hl/hl_surprise.png"), ag_tint["sunset"]),
        "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_2.png",(0,0), ag_img + "sprites/normal/hl/hl_surprise.png"), ag_tint["night"]),
        True,im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_2.png",(0,0), ag_img + "sprites/normal/hl/hl_surprise.png"))

    image hl wink_2 = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_2.png",(0,0), ag_img + "sprites/normal/hl/hl_wink.png"), ag_tint["sunset"]),
        "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_2.png",(0,0), ag_img + "sprites/normal/hl/hl_wink.png"), ag_tint["night"]),
        True,im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_2.png",(0,0), ag_img + "sprites/normal/hl/hl_wink.png"))

    image hl ghost = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor(im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_1.png",(0,0), ag_img + "sprites/normal/hl/hl_idle.png"), ag_tint["sunset"]), im.matrix.opacity(0.35)),
        "persistent.sprite_time=='night'",im.MatrixColor(im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_1.png",(0,0), ag_img + "sprites/normal/hl/hl_idle.png"), ag_tint["night"]), im.matrix.opacity(0.35)),
        True,im.MatrixColor(im.Composite((900,1080), (0,0), ag_img + "sprites/normal/hl/hl_1.png",(0,0), ag_img + "sprites/normal/hl/hl_idle.png"), im.matrix.opacity(0.35)))


    image og normal pioneer = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/og/og_1_default.png"), ag_tint["sunset"]),
        "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/og/og_1_default.png"), ag_tint["night"]),
        True,im.Composite((900,1080), (0,0), ag_img + "sprites/normal/og/og_1_default.png"))


    image ac normal pioneer = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/ac/ac_1_normal.png"), ag_tint["sunset"]),
        "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/ac/ac_1_normal.png"), ag_tint["night"]),
        True,im.Composite((900,1080), (0,0), ag_img + "/sprites/normal/ac/ac_1_normal.png"))

    image ac cry pioneer = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/ac/ac_2_cry.png"), ag_tint["sunset"]),
        "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/ac/ac_2_cry.png"), ag_tint["night"]),
        True,im.Composite((900,1080), (0,0), ag_img + "sprites/normal/ac/ac_2_cry.png"))

    image ac fear pioneer = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/ac/ac_2_fear.png"), ag_tint["sunset"]),
        "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), ag_img + "sprites/normal/ac/ac_2_fear.png"), ag_tint["night"]),
        True,im.Composite((900,1080), (0,0), ag_img + "sprites/normal/ac/ac_2_fear.png"))
