from src.classes import system
import src.constants as c
import sys as s
import os, os.path, shutil

sys = system("", "std.b", True)
sys.error_system.constants_module = c

read_input_arg_count = 0
read_input_arg_types = []
def read_input(params):
    try:
        str = input()
        return str
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

stdout_write_arg_count = 1
stdout_write_arg_types = [c.L_STRING]
def stdout_write(params):
    try:
        str = params[0]
        s.stdout.write(str)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()

stdout_flush_arg_count = 0
stdout_flush_arg_types = []
def stdout_flush(params):
    try: s.stdout.flush()
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()

to_str_arg_count = 1
to_str_arg_types = [c.L_ANY]
def to_str(params):
    try:
        res = str(params[0])
        if res in ["True", "False"]:
            res = res.lower()
        return res 
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

is_string_arg_count = 1
is_string_arg_types = [c.L_ANY]
def is_string(params):
    try: return True if isinstance(params[0], str) else False
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

is_number_arg_count = 1
is_number_arg_types = [c.L_ANY]
def is_number(params):
    try: return True if isinstance(params[0], (int, float)) else False
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

join_str_arg_count = 2
join_str_arg_types = [c.L_STRING, c.L_ANY]
def join_str(params):
    try:
        original = params[0]
        value    = params[1]
        return original + str(value)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False    

replace_str_arg_count = 3
replace_str_arg_types = [c.L_STRING, c.L_STRING, c.L_STRING]
def replace_str(params):
    try:
        str = params[0]
        tmp = params[1]
        val = params[2]

        return str.replace(tmp, val)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

curr_dir_arg_count = 0
curr_dir_arg_types = []
def curr_dir(params):
    try: return os.getcwd()
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

read_file_arg_count = 1
read_file_arg_types = [c.L_STRING]
def read_file(params):
    try:
        path = params[0]
        file = open(path, "r")
        data = file.read()
        file.close()
        return data
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

write_file_arg_count = 2
write_file_arg_types = [c.L_STRING, c.L_STRING]
def write_file(params):
    try:
        path = params[0]
        data = params[1]
        file = open(path, "w")
        file.write(data)
        file.close()
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()

create_file_arg_count = 1
create_file_arg_types = [c.L_STRING]
def create_file(params):
    try:
        path = params[0]
        file = open(path, "x")
        file.close()
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()

exists_arg_count = 1
exists_arg_types = [c.L_STRING]
def exists(params):
    try: return True if os.path.exists(params[0]) else False
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

del_file_arg_count = 1
del_file_arg_types = [c.L_STRING]
def del_file(params):
    try: os.remove(params[0])
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()

create_dir_arg_count = 1
create_dir_arg_types = [c.L_STRING]
def create_dir(params):
    try: os.mkdir(params[0])
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()

del_dir_arg_count = 1
del_dir_arg_types = [c.L_STRING]
def del_dir(params):
    try: shutil.rmtree(params[0])
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
