import src.constants as c

tuple_arg_count = 0
tuple_arg_types = []
def tuple(params):
    return (1, 2, "Hello World - from the extern tuple function :)")

give_obj_arg_count = 1
give_obj_arg_types = [c.L_OBJECT]
def give_obj(params):
    list = params[0]

    [print(v) for v in list]