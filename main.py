# -*- coding: utf-8 -*-
import cocos

from data import SCREEN_SIZE, TITLE

def initialization():
    pass
    #pyglet.resource.path.append('fonts')
    #pyglet.resource.add_font('Statix.ttf')

def main():
    cocos.director.director.init(width=SCREEN_SIZE[0], height=SCREEN_SIZE[1], caption=TITLE, do_not_scale=True)
    #add run here

if __name__ == "__main__":
    initialization()
    main()