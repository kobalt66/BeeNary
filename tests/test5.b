start:
    :src<"[CURRDIR]/libs/honeycomb.b">:

    a honey obj<1, 2, 3>

    b honey a<2>
    c honey obj<1123123123, "hello world", true>
    d honey c<2>

    t honey tuple<>
    tt honey t
    msg honey tt<2>

    give_obj<tt>

    flyout b
    flyout d
    flyout msg
:end: