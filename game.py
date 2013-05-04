# -*- coding: utf-8 -*-

import cocos
import pyglet

from data import OLD_COLOR, NORMAL_COLOR, TRANSITION, SCREEN_SIZE, SIDE_SCREEN, SLIDE_SPEED

class MultiScene(object):

    def __init__(self,name):
        
        self.scene = {}

        past = 'img/bg/' + name + '_past.png'
        present = 'img/bg/' + name + '_present.png'

        self.scene['past'] = GameScene(past,old=True)
        self.scene['present'] = GameScene(present)
        
        self.active = 'present'
        self.position = 0,0

        cocos.director.director.window.push_handlers(self)

    def get_active_scene(self):
        return self.scene[self.active]

    def on_key_release(self,key,modifier):
        
        if self.active == 'present':
            self.active = 'past'
        else:
            self.active = 'present'

        scene = TRANSITION(self.get_active_scene())
        
        self.refresh_view()

        cocos.director.director.replace(scene)

    def refresh_view(self):
        pos = self.position + SCREEN_SIZE
        self.get_active_scene().layer.set_view(*pos)

    def on_mouse_motion(self,x,y,dx,dy):

        if x <= SIDE_SCREEN:
            self.slide(-1)
        elif x >= SCREEN_SIZE[0] - SIDE_SCREEN:
            self.slide(1)
        self.refresh_view()

    def slide(self,sens):
         self.position = self.position[0] + SLIDE_SPEED * sens, self.position[1]


class GameScene(cocos.scene.Scene):

    def __init__(self,background,old=False):
        cocos.scene.Scene.__init__(self)
        
        color = NORMAL_COLOR
        if old:
            color = OLD_COLOR

        self.filter_layer = cocos.layer.util_layers.ColorLayer(*color)
        self.layer = cocos.layer.scrolling.ScrollableLayer()
        self.layer.set_view(0,0,*SCREEN_SIZE)

        self.sprite = cocos.sprite.Sprite(background,anchor=(0,0))
        self.layer.add(self.sprite)

        self.add(self.layer,z=0)
        self.add(self.filter_layer,z=1)