init python:


    import pygame
    import math


    class AgTrackCursor(renpy.Displayable):
 
        def __init__(self, child, paramod, **kwargs):
 
            super(AgTrackCursor, self).__init__()
 
            self.child = renpy.displayable(child)
            self.x = 0
            self.y = 0
            self.actual_x = 0
            self.actual_y = 0
 
            self.paramod = paramod
            self.last_st = 0
 
 
 
        def render(self, width, height, st, at):
 
            rv = renpy.Render(width, height)
            minimum_speed = 0.5
            maximum_speed = 3
            speed = 1 + minimum_speed
            mouse_distance_y = (self.y - self.actual_y)
            if self.x is not None:
                st_change = st - self.last_st
 
                self.last_st = st
                self.actual_x = self.x
                self.actual_y = self.y
 
 
                if mouse_distance_y <= minimum_speed:
                    mouse_distance_y = minimum_speed
                elif mouse_distance_y >= maximum_speed:
                    mouse_distance_y = maximum_speed
 
                cr = renpy.render(self.child, width, height, st, at)
                cw, ch = cr.get_size()
                rv.blit(cr, (self.actual_x, self.actual_y))
 
 
 
            renpy.redraw(self, 0)
            return rv
 
        def event(self, ev, x, y, st):
            hover = ev.type == pygame.MOUSEMOTION
            click = ev.type == pygame.MOUSEBUTTONDOWN
            mousefocus = pygame.mouse.get_focused()
            if hover:
 
                if (x != self.x) or (y != self.y) or click:
                    self.x = -x /self.paramod
                    self.y = -y /self.paramod



    ag_backdrop = None

    def agr_new_chapter(day_number,chapter_name="",mode="adv",music_stop=False):
        global save_name
        global _window_subtitle
        
        
        
        
        renpy.scene()
        renpy.show("bg black")
        renpy.pause(0.5)
        
        if ag_backdrop == "prologue":
            
            
            
            pass
        elif ag_backdrop == "epilogue":
            
            renpy.show("ag_backdrop_back")
            renpy.show("day_num",what=Text(chapter_name,style=style.agr_backdrop_text,textalign=0.5,ypos=0.5,xpos=0.5,yalign=0.5))

            renpy.transition(dissolve)
            renpy.pause(1.0)
        else:
            jn = " ".join(chapter_name)
            dn = jn.upper()
            
            renpy.show("ag_backdrop_back")
            renpy.show("day_num",what=Text(dn,style=style.agr_backdrop_text,textalign=0.5,ypos=0.5,xpos=0.5,yalign=0.5))

            renpy.transition(dissolve)
            renpy.pause(1.0)
            if ag_backdrop == "dv":
                renpy.show("dv normal pioneer", [backdrop_trans])
                renpy.transition(dissolve)
                renpy.pause(2.0)
            if ag_backdrop == "mi":
                renpy.show("mi normal pioneer", [backdrop_trans])
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



    def agr_meet(who, name): #смена имени
        gl = globals()
        global store
        store.names[who] = name
        gl[who+"_name"] = store.names[who]


    def agr_show_achievement(img):
        renpy.play(sfx_achievement)
        renpy.show(img, [achievement_trans], layer="overlay")
        renpy.pause(3.5)
        renpy.hide(img)


    good_ending = False
    good_gun = False
    karta = True
    karta_otkrytie = False
    search_cnt = 0
    hospital = False
    storage = False
    deadspot = False
    ring = False
    kolco = False
    aptechka = False
    pristrelit_psa = False
    instrumenty = False