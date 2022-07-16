start:
    :src<"./libs/math.b">:

    :hive:
        honeypot b
    :hive:

    a honey 1
    c honey 1
    take b 0
    flyout "Hello World!"

    inv 1 is c flyout "a is c"

    ###### inv-statement test ########################
    # inv true is false       flyout "wtf"
    # inv true is not true    flyout "true forever"
    # inv 1 is not 0          flyout "wtf"
    # inv 1 is 1              flyout "true forever"
    loop:
       
:end: