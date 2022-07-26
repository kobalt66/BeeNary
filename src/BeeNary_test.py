import sys as s
from interpreter import get_code, run 
from classes import system


gettrace = getattr(s, 'gettrace', None)
if gettrace: 
    if gettrace():
        code = get_code("tests/test6.b")
        run(code, "tests/test6.b", "", "", "", "-sw", "", "", "", "", "")
        exit(0)

sys = system()
argv1, argv2, argv3, argv4, argv5, argv6, argv7, argv8, argv9, argv10 = sys.process_argv_list(s.argv)

code = get_code(argv1)
run(code, argv1, argv2, argv3, argv4, argv5, argv6, argv7, argv8, argv9, argv10)