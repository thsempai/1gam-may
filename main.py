# -*- coding: utf-8 -*-
import cocos
import pyglet

from data import SCREEN_SIZE, TITLE, TITLE_FONT, TITLE_COLOR, MOUSE_CURSOR, BG_COLOR, TRANSITION
from menu import Menu
from game import GameScene


def start_game():
    gs = GameScene()
    gs = TRANSITION(gs,duration=2)
    cocos.director.director.push(gs)

def quit():
    cocos.director.director.terminate_app = True

def callback(dt):
    #backgroung
    pyglet.gl.glClearColor(*BG_COLOR)

def main():
    # initialization
    pyglet.resource.path.append('fonts')
    pyglet.resource.reindex()
    pyglet.resource.add_font('Crystal_Deco.ttf')

    
    start_menu =    [
                    ('New Game',start_game,[]),
                    ('Quit',quit,[])
                    ]

    cocos.director.director.init(width=SCREEN_SIZE[0], height=SCREEN_SIZE[1], caption=TITLE, do_not_scale=True)
    cocos.director.director.window.set_mouse_cursor(MOUSE_CURSOR)

    #start scene
    start_scene = cocos.scene.Scene()
    start_menu = Menu(start_menu)
    start_scene.add(start_menu)

    #add title
    position = SCREEN_SIZE[0]/2,SCREEN_SIZE[1]-200
    title = cocos.text.Label(text = TITLE,position = position, font_name = TITLE_FONT, color= TITLE_COLOR , font_size = 60, anchor_x = 'center')
    start_scene.add(title)

    #for backgroung color
    start_scene.schedule(callback)

    #run application
    
    cocos.director.director.run(start_scene)

if __name__ == "__main__":
    main()