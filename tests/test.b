start:
    :src<"./libs/math.b">:

    :hive:
        honeypot b
    :hive:

    a honey 1
    d honey take b 0
    d honey a

    flyto start

init_e: 
    #inv b is b flyout "a is c"
    #inv 1 in b inv 2 in b flyout "asfasdf"

    ###### inv-statement test ########################
    # inv true is false       flyout "wtf"
    # inv true is not true    flyout "true forever"
    # inv 1 is not 0          flyout "wtf"
    # inv 1 is 1              flyout "true forever"
loop:
    flyto init_e
    :src<"./libs/vars.b">:
    flyout pie

    flyto start
    flyto loop
:end: