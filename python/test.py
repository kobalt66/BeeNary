from src.classes import system
import src.interpreter as i
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

scope_value_arg_count = 1
scope_value_arg_types = [c.L_SCOPE]
def scope_value(params):
    try:
        scope = params[0]
        i.execute_nodelist(scope)
    except Exception as e:
        sys.error_system.create_error_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()