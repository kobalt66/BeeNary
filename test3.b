start:
    inv 1 is 2 flyout 1
    inv 1 is not 1 flyto test_two

    a honey 1


:hive: 
    honeypot b
:hive:

test_one:
    :end<"Ended the program at 'test_one'">:

test_two:
    flyout "Hello World!"
    inv a is b flyout "a is indeed 1"

    wax test true

    b honey a<1, 2, b, 1, "Hello World", true>
    b honey "hello world"
    flyout b

    :trace:

    sting b

    b stick a 
    b stick 2
    flyout "Hello World!"
:end: