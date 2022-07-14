:meadow:

wax some_constant 123123
wax pi 3.14159265359
wax prase "This is constant"

:functionptr:
wax test :python<"std.py">:

wax obj :honeycomb<a, b, c>:

start:
:src<".lib/test.lib">:

test honey obj<1, 2, "Test">

res honey test<2>
flyout res