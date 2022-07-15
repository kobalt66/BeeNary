start:
    :src<"./libs/math.b">:

    :hive:
        honeypot b
    :hive:

    a honey 1
    b stick a
    b stick 2
    flyout "Hello World!"

    ###### inv-statement test ########################
    # inv true is false       flyout "wtf"
    # inv true is not true    flyout "true forever"
    # inv 1 is not 0          flyout "wtf"
    # inv 1 is 1              flyout "true forever"
    loop:

:end: