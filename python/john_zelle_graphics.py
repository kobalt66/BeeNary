from .graphics import *
import src.constants as c

window = None

create_window_arg_count = 4
create_window_arg_types = [c.L_STRING, c.L_INT, c.L_INT, c.L_BOOL]
def create_window(params):
    global window
    title     = params[0]
    width     = params[1]
    height    = params[2]
    autoflush = params[3]

    window = GraphWin(title, width, height, autoflush)

win_getMouse_arg_count = 0
win_getMouse_arg_types = []
def win_getMouse(params):
    global window
    window.getMouse()

win_close_arg_count = 0
win_close_arg_types = []
def win_close(params):
    global window
    window.close()

background_color_arg_count = 3
background_color_arg_types = [c.L_INT, c.L_INT, c.L_INT]
def background_color(params):
    r = params[0]
    g = params[1]
    b = params[2]

    color = color_rgb(r, g, b)
    window.setBackground(color)
