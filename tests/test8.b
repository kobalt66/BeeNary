start:

    :src<"[CURRDIR]/libs/test_lib.b">:
    :src<"[CURRDIR]/libs/std.b">:
    :src<"[CURRDIR]/libs/math.b">:

    #:hive:
    #    honeypot _list
    #:hive:

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

    #@await inv 1 is 1 flyout add<test, add<add<test, 1>, 1>>
    #string honey "987 9879 797 ads 9 88"
    #group honey replace_regex<"[0-9]+", string, " NUMBER ">
    #group honey get_regex<"[0-9]+", string>
    
    #flyout group

    #idx honey 0
    #loop:
    #    flyout group<idx>
    #    inv idx is not sub<lengthof<group>, 1> idx honey add<idx, 1>
    #    other flyto _end
    #flyto loop

    #inv false not is true flyout ":)"
    #other flyout ":("

    #inv 0 is false alert FALSE_SYNTAX_EXCEPTION<"Message.">
    #@threaded 
    #inv true is delay<"..."> flyout "!"
    #other alert FALSE_SYNTAX_EXCEPTION<"Message.">
    #@threaded 
    #inv true is not delay<"..."> flyout "!"
    #other alert FALSE_SYNTAX_EXCEPTION<"Message.">
    #@threaded 
    #inv true is delay<"..."> flyout "!"
    #other alert FALSE_SYNTAX_EXCEPTION<"Message.">
    #@threaded 
    #inv true is not delay<"..."> flyout "!"
    #other alert FALSE_SYNTAX_EXCEPTION<"Message.">
    #@threaded 
    #inv true is delay<"..."> flyout "!"
    #other alert FALSE_SYNTAX_EXCEPTION<"Message.">
    #@threaded 
    #inv true is not delay<"..."> flyout "!"
    #other alert FALSE_SYNTAX_EXCEPTION<"Message.">

    #@threaded alert NO_VALUE_EXCEPTION<"Gime value!">
    #@threaded alert NO_VALUE_EXCEPTION<"Gime value!">
    #@threaded alert NO_VALUE_EXCEPTION<"Gime value!">
    #@threaded alert NO_VALUE_EXCEPTION<"Gime value!">
    #@threaded alert NO_VALUE_EXCEPTION<"Gime value!">
    #@threaded alert NO_VALUE_EXCEPTION<"Gime value!">
    #@threaded alert NO_VALUE_EXCEPTION<"Gime value!">
    #@threaded alert NO_VALUE_EXCEPTION<"Gime value!">
    #@threaded alert NO_VALUE_EXCEPTION<"Gime value!">
    #@threaded alert NO_VALUE_EXCEPTION<"Gime value!">
    #@threaded alert NO_VALUE_EXCEPTION<"Gime value!">
    
_end:
:end: