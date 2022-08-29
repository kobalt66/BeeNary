init:
    :src<"[CURRDIR]/libs/std.b">:
    :src<"[CURRDIR]/libs/math.b">:
    :src<"[CURRDIR]/libs/test_lib.b">:
    ret

start:
    flyto init

    scope (
        start_time honey time<>
        flyout "Hello from inside a scope!"
        end_time honey time<>
        flyout sub<end_time, start_time>
    )

    scope<>
    scope<>
    scope<>
    scope<>
    scope<>
    scope<>

:end: