start:

:hive:
    honeypot list
:hive:

a honey "hello"
b honey a
a honey true

list stick 0
list stick b

c honey list<1>
b honey c

flyout a
flyout b
flyout c

take list 1

c honey list<0>
flyout c

:src<"./libs/math.b">:

flyout pi

lenghtof<list>
a honey add<1, 1>

flyout a

a honey add<a, a>
flyout a

:end: