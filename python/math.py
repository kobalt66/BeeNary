import src.constants as c

add_arg_count = 2
add_arg_types = [c.L_NUMBER, c.L_NUMBER]
def add(params):
    a = params[0]
    b = params[1]
    return a + b

test_arg_count = 0
test_arg_types = []
def test(params):
    count = 0
    while count < 100:
        print(count)
        count += 1

lenghtof_arg_count = 1
lenghtof_arg_types = [c.L_ANY]
def lenghtof(params):
    list = params[0]
    return len(list)
