start:
:src<"./libs/math.b">:

:hive:
    honeypot list
:hive:

list stick -1

loop:

    a honey lenghtof<list>
    list stick a
    flyout a

    inv a is 100 flyto end_section
    inv a is 200 flyto end_section

flyto loop

end_section:
    list stick a
    c honey 100
    inv a in list inv c is a flyto loop
    :end: