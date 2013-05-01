import cocos

from data import MENU_FONT, MENU_ITEM_COLOR, MENU_ITEM_SELECTED_COLOR


class Menu(cocos.menu.Menu):

    def __init__(self,commands):

        cocos.menu.Menu.__init__(self)

        #menu construction

        self.font_item['font_name'] = MENU_FONT 
        self.font_item['color'] = MENU_ITEM_COLOR     
        self.font_item['font_size'] = 45
        self.font_item_selected['font_name'] = MENU_FONT
        self.font_item_selected['color'] = MENU_ITEM_SELECTED_COLOR
        self.font_item_selected['font_size'] = 50 
        self.menu_valign = cocos.menu.BOTTOM
        self.menu_halign = cocos.menu.CENTER
        self.y = 100

        l = []

        for cmd in commands:
            l.append(cocos.menu.MenuItem(cmd[0], cmd[1],*cmd[2]))

        self.create_menu(l, None, None)

    def on_quit(self):
              pass