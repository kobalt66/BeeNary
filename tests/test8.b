start:

    :src<"[CURRDIR]/libs/test_lib.b">:
    :src<"[CURRDIR]/libs/std.b">:
    :src<"[CURRDIR]/libs/math.b">:

    :hive:
        honeypot _list
    :hive:

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

    #@threaded test honey delay<"Multi-threading in beenary!">
    #@await inv test is true inv 1 is 1 sting test

    #@await flyout test
    #@await flyout test
    #@await flyout test
    #@await flyout test
    #@await flyout test
    #@await flyout test

    #@await _list stick test
    #@await flyout add<add<test, 1>, 1>
    #@await sleep<add<add<test, 1>, 1>>
:end: