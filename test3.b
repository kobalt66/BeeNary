start:
    inv 1 is 2 flyout 1
    inv 1 is not 2 flyto test_two

test_one:
    :end<"Ended the program at 'test_one'">:

test_two:
    flyout "Hello World!"
    inv a is b flyout "a is indeed 1"

    wax test true

    b honey a<1, 2, b, 1, "Hello World", hello_world, true>
    b honey "hello world"
    flyout b

    :trace:

    sting b

    take list 0

:hive: 
    honeypot b 
:hive:

start:
    a honey 1
    b stick a 
    b stick 2
    flyout "Hello World!"
:end: