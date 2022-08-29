from src.classes import system
import src.constants as c
import time

sys = system("", "test_lib.b", True)
sys.error_system.constants_module = c

delay_arg_count = 1
delay_arg_types = [c.L_STRING]
def delay(params):
    time.sleep(5)
    print(params[0])
    return 1

