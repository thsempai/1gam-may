# -*- coding: utf-8 -*-

import cocos
import pyglet

from data import OLD_COLOR, SCREEN_SIZE, TRANSITION

class GameScene(cocos.scene.Scene):

    def __init__(self):
        cocos.scene.Scene.__init__(self)
        
        self.old_layer = OldLayer()
        self.layer = cocos.layer.Layer()
        self.sprite = cocos.sprite.Sprite('img/sprite/first_image.png',anchor=(0,0))
        self.layer.add(self.sprite)

        self.add(self.layer,z=0)
        self.add(self.old_layer,z=1)

        cocos.director.director.window.push_handlers(self)

    def on_key_release(self,key,modifier):

        layer = cocos.layer.Layer()
        sprite = cocos.sprite.Sprite('img/sprite/first_image.png',anchor=(0,0))
        layer.add(sprite)

        scene = cocos.scene.Scene()
        scene.add(layer)
        scene = TRANSITION(scene)
        cocos.director.director.replace(scene)


class OldLayer(cocos.layer.util_layers.ColorLayer):
    
    def __init__(self):
        args = OLD_COLOR
        cocos.layer.util_layers.ColorLayer.__init__(self,*args)
        

