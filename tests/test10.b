init:
    :src<"[CURRDIR]/libs/std.b">:
    :src<"[CURRDIR]/libs/math.b">:
    ret

start:
    flyto init

    scope (
        :src<"[CURRDIR]/libs/std.b">:
        :src<"[CURRDIR]/libs/math.b">:
        start_time honey time<>
        flyout "Hello from inside a scope!"
        end_time honey time<>
        flyout sub<end_time, start_time>
    )

    execute_scope<scope>

    start_time honey time<>
    flyout "Hello from inside a scope!"
    end_time honey time<>
    flyout sub<end_time, start_time>
:end: