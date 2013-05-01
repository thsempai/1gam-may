import pyglet
import cocos.scenes

# -*- coding: utf-8 -*-
#title
TITLE = "May's One Game A Month"
TITLE_FONT = "Crystal Deco"
TITLE_COLOR = (10,10,10,255)

#cursor
cursor = pyglet.image.load('img/mouse/mouse.png')
MOUSE_CURSOR = pyglet.window.ImageMouseCursor(cursor,cursor.width/2,cursor.height/2)

#screen

SCREEN_SIZE = 800,600

NORMAL_COLOR = 217, 217, 217, 255 
OLD_COLOR = 112, 66, 20, 120

#gl color
BG_COLOR = NORMAL_COLOR[0]/255., NORMAL_COLOR[1]/255., NORMAL_COLOR[2]/255., 255.

#menu

MENU_FONT = "Crystal Deco"
MENU_ITEM_COLOR = (50,50,50,255)
MENU_ITEM_SELECTED_COLOR = (10,10,10,255)

#transition

TRANSITION = cocos.scenes.transitions.FadeTransition
