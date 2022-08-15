counting:
    count honey 0
    loop:
        inv lt<count, 1000> is true count honey add<count, 1>
        other flyto after_counting
        
        flyout count
    flyto loop

init:
    # import libraries
    :trace: :src<"[CURRDIR]/libs/std.b">:
    :trace: :src<"[CURRDIR]/libs/math.b">:

    start_time honey time<>

    # init constants
    @readonly a honey 1
    @readonly hello_world honey "Hello World!"
    ret

start: 
    flyto init

    flyout hello_world
    flyout a

    # @threaded sleep<10>
    # a honey 0

    inv a is 0 flyout "readonly doesn't work :("
    other flyout "everything's fine :)"

    flyto counting
    after_counting:

    end_time honey time<>
    flyout string_format<"\nTime needed to process the code: {0} sec\n", sub<end_time, start_time>>
:end<"exit with code 0">: