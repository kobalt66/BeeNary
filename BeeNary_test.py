import interpreter as BeeNary
from classes import system
import sys as s


gettrace = getattr(s, 'gettrace', None)
if gettrace: 
    if gettrace():
        code = BeeNary.get_code("test3.b")
        BeeNary.run(code, "test3.b", "-n", "-t", "-np", "-sw", "-cp", "", "", "", "")
        exit(0)

sys = system()
argv1, argv2, argv3, argv4, argv5, argv6, argv7, argv8, argv9, argv10 = sys.process_argv_list(s.argv)

code = BeeNary.get_code(argv1)
BeeNary.run(code, argv1, argv2, argv3, argv4, argv5, argv6, argv7, argv8, argv9, argv10)