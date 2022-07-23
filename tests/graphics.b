init_window:

    title honey "graphics-test" 
    width honey 640
    height honey 450 
    autoflush honey true

    create_window<title, width, height, autoflush>
    background_color<255, 123, 23>

    create_point<"point", 100, 100>
    new_coords honey vec_two<90, 150>
    set_point<"point", new_coords>

    point honey get_point<"point">
    circle honey create_circle<point, 100>
    circle_draw<circle>

    win_getMouse<>
    win_close<>

    flyto after_init_window

start:
    :src<"[CURRDIR]/libs/john_zelle_graphics.b">:

    flyto init_window
    after_init_window:

:end: