from re import T
from .graphics import *
from src.classes import system
import src.constants as c
import random

window = None
points = {"zero" : (0, 0)}
objects = {}

sys = system("", "john_zelle_graphics.b", True)
sys.error_system.constants_module = c

def cast_all_exceptions():
    global sys
    sys.error_system.throw_errors()
    sys.error_system.throw_warnings()

####################################################################################################

create_window_arg_count = 4
create_window_arg_types = [c.L_STRING, c.L_INT, c.L_INT, c.L_BOOL]
def create_window(params):
    try:
        global window
        title     = params[0]
        width     = params[1]
        height    = params[2]
        autoflush = params[3]

        window = GraphWin(title, width, height, autoflush)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        cast_all_exceptions()

win_getMouse_arg_count = 0
win_getMouse_arg_types = []
def win_getMouse(params):
    try:
        global window
        window.getMouse()
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        cast_all_exceptions()

win_close_arg_count = 0
win_close_arg_types = []
def win_close(params):
    try:
        global window
        window.close()
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        cast_all_exceptions()

background_color_arg_count = 3
background_color_arg_types = [c.L_INT, c.L_INT, c.L_INT]
def background_color(params):
    try:
        r = params[0]
        g = params[1]
        b = params[2]

        color = color_rgb(r, g, b)
        window.setBackground(color)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        cast_all_exceptions()

####################################################################################################

def get_object(name):
    if not name in objects.keys():
        sys.error_system.create_error(c.PYTHON_EXCEPTION, c.LIBRARY, f"The object called '{name}' doesn't exist.")
        cast_all_exceptions()
    return objects[name]
def point_to_object(point):
    return Point(point[0], point[1])

create_point_arg_count = 3
create_point_arg_types = [c.L_STRING, c.L_INT, c.L_INT]
def create_point(params):
    try:
        name    = params[0]
        x       = params[1]
        y       = params[2]

        points[name] = (x, y)
        return (x, y)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        cast_all_exceptions()
        return False

delete_point_arg_count = 1
delete_point_arg_types = [c.L_STRING]
def delete_point(params):
    try:
        name = params[0]
        if name in points.keys():
            del points[name]
            return True
        return False
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        cast_all_exceptions()
        return False

set_point_arg_count = 2
set_point_arg_types = [c.L_STRING, c.L_OBJECT]
def set_point(params):
    try:
        name  = params[0]
        tuple = params[1]
        if name in points.keys():
            points[name] = tuple
            return True
        return False
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        cast_all_exceptions()
        return False

get_point_arg_count = 1
get_point_arg_types = [c.L_STRING]
def get_point(params):
    try:
        name = params[0]
        if name in points.keys():
            return points[name]
        return False
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        cast_all_exceptions()
        return False

create_circle_arg_count = 2
create_circle_arg_types = [c.L_OBJECT, c.L_INT]
def create_circle(params):
    try:
        point  = point_to_object(params[0])
        radius = params[1] 
        name   = '%08x' % random.randrange(8**16)

        c = Circle(point, radius)
        objects[name] = c
        return name
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        cast_all_exceptions()
        return False

circle_draw_arg_count = 1
circle_draw_arg_types = [c.L_STRING]
def circle_draw(params):
    try:
        global window
        name = params[0]
        circle = get_object(name)
        if not isinstance(circle, Circle):
            sys.error_system.create_error(c.PYTHON_EXCEPTION, c.LIBRARY, "The object you are trying to reference is not a circle.")
            cast_all_exceptions()
        
        circle.draw(window)
        return True
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        cast_all_exceptions()
        return False