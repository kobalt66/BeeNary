start:
    :src<"./libs/math.b">:

    :hive:
        honeypot b
    :hive:

    a honey 1
    d honey take b 0
    d honey a

    flyto loop

init_e:
    wax e :python<"asdf">:

    #inv b is b flyout "a is c"
    #inv 1 in b inv 2 in b flyout "asfasdf"

    ###### inv-statement test ########################
    # inv true is false       flyout "wtf"
    # inv true is not true    flyout "true forever"
    # inv 1 is not 0          flyout "wtf"
    # inv 1 is 1              flyout "true forever"
loop:
    flyto init_e
    e<a, pi>
    :src<"./libs/vars.b">:
    flyout pie

    :src<"./libs/test2.b">:
    test_ honey obj<1, 2, "Test">

    flyto start
    flyto loop
:end: