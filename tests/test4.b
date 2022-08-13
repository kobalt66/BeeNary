start:

:hive:
    honeypot _list
:hive:

a honey "hello"
b honey a
a honey true

_list stick 0
_list stick b

c honey _list<1>
b honey c

flyout a
flyout b
flyout c

take _list 1

c honey _list<0>
flyout c

:src<"[CURRDIR]/libs/math.b">:
:src<"[CURRDIR]/libs/std.b">:

flyout pi

take _list 0

flyout lengthof<_list>
a honey add<1, 1>

flyout a

a honey add<a, a>
flyout a

:end: