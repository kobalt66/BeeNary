start:
    :src<"./libs/math.b">:

    :hive:
        honeypot b
    :hive:

    b stick 1

    a honey 1
    d honey b<0>
    d honey a

init_e: 
    inv b is b flyout "a is c"
    inv 1 in b inv 2 in b flyout "asfasdf"

    inv true is false       flyout "wtf"
    inv true is not true    flyout "true forever"
    inv 1 is not 0          flyout "wtf"
    inv 1 is 1              flyout "true forever"
loop:
:end: