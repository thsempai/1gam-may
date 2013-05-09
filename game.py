# -*- coding: utf-8 -*-

import cocos
import pyglet

from data import OLD_COLOR, NORMAL_COLOR, TRANSITION, SCREEN_SIZE
from data import SIDE_SCREEN, SLIDE_SPEED, TEST_MODE, TOP_SIDE, APPEARANCE_TIME

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

        self.inventory = Inventory()
        self.in_menu = False



        #add scheduler and inventory
        for scene in self.scene.values():
            scene.schedule(self.callback)
            scene.add(self.inventory,z=10)

        cocos.director.director.window.push_handlers(self)

    def callback(self,dt):
        if self.slide_scene:
            self.slide()


        self.inventory.appearance_time -= dt

        if not self.in_menu:
            if self.inventory.appearance_time <= 0:
                self.inventory.appearance_time = APPEARANCE_TIME
                self.inventory.appears(False)


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

        #inventory
        if y <= TOP_SIDE:
            self.in_menu = True
            if self.inventory.position[1] < 0:
                self.inventory.appears()

            self.slide_scene = 0.
            return

        self.in_menu = False

        #sliding
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
                    (0, TOP_SIDE),
                    (SCREEN_SIZE[0], TOP_SIDE)
                    ]
                ]
        for line in lines:
            line = cocos.draw.Line(line[0],line[1],color)
            self.add(line,z=10)

        #add
        self.add(self.layer,z=0)
        self.add(self.filter_layer,z=1)

class Inventory(cocos.sprite.Sprite):

    def __init__(self):
        
        image = pyglet.image.load('img/gui/menu.png')
        anchor = image.width/2,0

        position = SCREEN_SIZE[0]/2,-1 * image.height # position below the screen
        cocos.sprite.Sprite.__init__(self,image,position=position,anchor=anchor)

        self.appearance_time = APPEARANCE_TIME

    def appears(self,appears=True):
        if self.actions:
            return
        
        sens = 1
        if not appears:
            sens = -1

        delta = 0, self.image.height * sens
        move = cocos.actions.interval_actions.MoveBy(delta,duration = 0.5)
        self.do(move)


        


