start:

    :src<"[CURRDIR]/libs/test_lib.b">:
    :src<"[CURRDIR]/libs/std.b">:

    #@threaded test honey delay<"Multi-threading in beenary!">
    #@threaded test1 honey delay<"Multi-threading in beenary!">
    #@threaded test2 honey delay<"Multi-threading in beenary!">
    #@threaded test3 honey delay<"Multi-threading in beenary!">
    #@threaded inv true is delay<"check..."> flyout delay<"Flyout on a thread">

    #inv true is delay<"check..."> flyout delay<"Flyout on a thread">
    #@threaded inv true is delay<"check..."> flyout delay<"Flyout on a thread">
    #@threaded inv true is delay<"check..."> flyout delay<"Flyout on a thread">
    #@threaded inv true is delay<"check..."> flyout delay<"Flyout on a thread">

    #a honey 2
    #flyout a

    #@readonly
    #a honey 1

    #flyout a
    #a honey 2
    #flyout a

    #@onetime b honey 1
    #flyout b
    #flyout b

:end: