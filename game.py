# -*- coding: utf-8 -*-

import cocos
import pyglet

from data import OLD_COLOR, NORMAL_COLOR, TRANSITION, SCREEN_SIZE, SIDE_SCREEN, SLIDE_SPEED, TEST_MODE

class MultiScene(object):

    def __init__(self,name):
        
        self.scene = {}

        past = 'img/bg/' + name + '_past.png'
        present = 'img/bg/' + name + '_present.png'

        self.scene['past'] = GameScene(past,old=True)
        self.scene['present'] = GameScene(present)
        
        self.active = 'present'
        self.position = 0,0
        self.slide_scene = 0.

        #add scheduler
        for scene in self.scene.values():
            scene.schedule(self.callback)

        cocos.director.director.window.push_handlers(self)

    def callback(self,dt):
        if self.slide_scene:
            self.slide()

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

        SLIDE_SPEED
        steps = range(SLIDE_SPEED,0,-1)

        if x <= SIDE_SCREEN:
            self.slide_scene = -1 * steps[int(x/float(SIDE_SCREEN) * (SLIDE_SPEED-1))]
        elif x >= SCREEN_SIZE[0] - SIDE_SCREEN:
            self.slide_scene = 1 * steps[int((SCREEN_SIZE[0] - x)/float(SIDE_SCREEN) * (SLIDE_SPEED-1))]
        else:
            self.slide_scene = 0.

    def slide(self):
        self.position = self.position[0] + self.slide_scene, self.position[1]
        self.refresh_view()

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

        #lines for test
        color = 0,0,0,255
        lines = [
                    [
                    (SIDE_SCREEN,0),
                    (SIDE_SCREEN,SCREEN_SIZE[1])
                    ],
                    [
                    (SCREEN_SIZE[0] - SIDE_SCREEN,0),
                    (SCREEN_SIZE[0] - SIDE_SCREEN,SCREEN_SIZE[1])
                    ],
                    [
                    (0, TOP_SIDE[1]),
                    (SCREEN_SIZE[0], TOP_SIDE[1])
                    ]
                ]
        for line in lines:
            line = cocos.draw.Line(line[0],line[1],color)

        self.add(linev1,z=10)
        self.add(linev2,z=10)

        #add
        self.add(self.layer,z=0)
        self.add(self.filter_layer,z=1)

class Inventory(cocos.layer.Layer):

    def __init__(self):
        cocos.layer.Layer.__init__(self)

    def appears(self,visible = True):
        pass


