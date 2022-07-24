from src.classes import system
from math import sqrt as math_sqrt, sin as math_sin, sinh as math_sinh, asin as math_arcsin, tan as math_tan, tanh as math_tanh, atan as math_arctan, cos as math_cos, cosh as math_cosh, acos as math_arccos
import src.constants as c

to_int = int
to_float = float

sys = system("", "math.b", True)
sys.error_system.constants_module = c

int_arg_count = 1
int_arg_types = [c.L_ANY]
def int(params):
    try:
        value = params[0]
        return to_int(value)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

float_arg_count = 1
float_arg_types = [c.L_ANY]
def float(params):
    try:
        value = params[0]
        return to_float(value)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

add_arg_count = 2
add_arg_types = [c.L_NUMBER, c.L_NUMBER]
def add(params):
    try:
        a = params[0]
        b = params[1]
        return a + b
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

sub_arg_count = 2
sub_arg_types = [c.L_NUMBER, c.L_NUMBER]
def sub(params):
    try:
        a = params[0]
        b = params[1]
        return a - b
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

div_arg_count = 2
div_arg_types = [c.L_NUMBER, c.L_NUMBER]
def div(params):
    try:
        a = params[0]
        b = params[1]
        return a / b
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

mul_arg_count = 2
mul_arg_types = [c.L_NUMBER, c.L_NUMBER]
def mul(params):
    try:
        a = params[0]
        b = params[1]
        return a * b
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

pow_arg_count = 2
pow_arg_types = [c.L_NUMBER, c.L_NUMBER]
def pow(params):
    try:
        a = params[0]
        b = params[1]

        res = 1
        for i in range(b):
            res *= a

        return res
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

sqrt_arg_count = 1
sqrt_arg_types = [c.L_NUMBER]
def sqrt(params):
    try:
        num = params[0]
        return math_sqrt(num)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

lt_arg_count = 2
lt_arg_types = [c.L_NUMBER, c.L_NUMBER]
def lt(params):
    try:
        a = params[0]
        b = params[1]

        return a < b
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

gt_arg_count = 2
gt_arg_types = [c.L_NUMBER, c.L_NUMBER]
def gt(params):
    try:
        a = params[0]
        b = params[1]

        return a > b
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

sqrt_arg_count = 1
sqrt_arg_types = [c.L_NUMBER]
def sqrt(params):
    try:
        num = params[0]
        return math_sqrt(num)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()

sin_arg_count = 1
sin_arg_types = [c.L_NUMBER]
def sin(params):
    try:
        num = params[0]
        return math_sin(num)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()

sinh_arg_count = 1
sinh_arg_types = [c.L_NUMBER]
def sinh(params):
    try:
        num = params[0]
        return math_sinh(num)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()

arcsin_arg_count = 1
arcsin_arg_types = [c.L_NUMBER]
def arcsin(params):
    try:
        num = params[0]
        return math_arcsin(num)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()

tan_arg_count = 1
tan_arg_types = [c.L_NUMBER]
def tan(params):
    try:
        num = params[0]
        return math_tan(num)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()

tanh_arg_count = 1
tanh_arg_types = [c.L_NUMBER]
def tanh(params):
    try:
        num = params[0]
        return math_tanh(num)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()

arctan_arg_count = 1
arctan_arg_types = [c.L_NUMBER]
def arctan(params):
    try:
        num = params[0]
        return math_arctan(num)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()

cos_arg_count = 1
cos_arg_types = [c.L_NUMBER]
def cos(params):
    try:
        num = params[0]
        return math_cos(num)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()

cosh_arg_count = 1
cosh_arg_types = [c.L_NUMBER]
def cosh(params):
    try:
        num = params[0]
        return math_cosh(num)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()

arccos_arg_count = 1
arccos_arg_types = [c.L_NUMBER]
def arccos(params):
    try:
        num = params[0]
        return math_arccos(num)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()


vectwo_arg_count = 2
vectwo_arg_types = [c.L_NUMBER, c.L_NUMBER]
def vectwo(params):
    try:
        x = params[0]
        y = params[1]

        return (x, y)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

vecthree_arg_count = 3
vecthree_arg_types = [c.L_NUMBER, c.L_NUMBER, c.L_NUMBER]
def vecthree(params):
    try:
        x = params[0]
        y = params[1]
        z = params[2]

        return (x, y, z)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

vecfour_arg_count = 4
vecfour_arg_types = [c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER]
def vecfour(params):
    try:
        x = params[0]
        y = params[1]
        z = params[2]
        w = params[3]

        return (x, y, z, w)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

add_vectwo_arg_count = 2
add_vectwo_arg_types = [c.L_OBJECT, c.L_OBJECT]
def add_vectwo(params):
    try:
        vec1 = params[0]
        vec2 = params[1]

        if not len(vec1) == len(vec2):
            sys.error_system.create_error(c.INVALID_ARGUMENT_EXCEPTION, c.LIBRARY, "The two given vectors have to be the same type.", -1)
            sys.cast_all_exceptions()
            return False

        res = (vec1[0] + vec2[0], vec1[1] + vec2[1])
        return res
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

sub_vectwo_arg_count = 2
sub_vectwo_arg_types = [c.L_OBJECT, c.L_OBJECT]
def sub_vectwo(params):
    try:
        vec1 = params[0]
        vec2 = params[1]

        if not len(vec1) == len(vec2):
            sys.error_system.create_error(c.INVALID_ARGUMENT_EXCEPTION, c.LIBRARY, "The two given vectors have to be the same type.", -1)
            sys.cast_all_exceptions()
            return False

        res = (vec1[0] - vec2[0], vec1[1] - vec2[1])
        return res
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

div_vectwo_arg_count = 2
div_vectwo_arg_types = [c.L_OBJECT, c.L_NUMBER]
def div_vectwo(params):
    try:
        vec1 = params[0]
        num = params[1]

        return (vec1[0] / num, vec1[1] / num)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

mul_vectwo_arg_count = 2
mul_vectwo_arg_types = [c.L_OBJECT, c.L_NUMBER]
def mul_vectwo(params):
    try:
        vec1 = params[0]
        num = params[1]

        return (vec1[0] * num, vec1[1] * num)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

add_vecthree_arg_count = 2
add_vecthree_arg_types = [c.L_OBJECT, c.L_OBJECT]
def add_vecthree(params):
    try:
        vec1 = params[0]
        vec2 = params[1]

        if not len(vec1) == len(vec2):
            sys.error_system.create_error(c.INVALID_ARGUMENT_EXCEPTION, c.LIBRARY, "The two given vectors have to be the same type.", -1)
            sys.cast_all_exceptions()
            return False

        res = (vec1[0] + vec2[0], vec1[1] + vec2[1], vec1[2] + vec2[2])
        return res
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

sub_vecthree_arg_count = 2
sub_vecthree_arg_types = [c.L_OBJECT, c.L_OBJECT]
def sub_vecthree(params):
    try:
        vec1 = params[0]
        vec2 = params[1]

        if not len(vec1) == len(vec2):
            sys.error_system.create_error(c.INVALID_ARGUMENT_EXCEPTION, c.LIBRARY, "The two given vectors have to be the same type.", -1)
            sys.cast_all_exceptions()
            return False

        res = (vec1[0] - vec2[0], vec1[1] - vec2[1], vec1[2] - vec2[2])
        return res
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

div_vecthree_arg_count = 2
div_vecthree_arg_types = [c.L_OBJECT, c.L_NUMBER]
def div_vecthree(params):
    try:
        vec1 = params[0]
        num = params[1]

        return (vec1[0] / num, vec1[1] / num, vec1[2] / num)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

mul_vecthree_arg_count = 2
mul_vecthree_arg_types = [c.L_OBJECT, c.L_NUMBER]
def mul_vecthree(params):
    try:
        vec1 = params[0]
        num = params[1]

        return (vec1[0] * num, vec1[1] * num, vec1[2] * num)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

add_vecfour_arg_count = 2
add_vecfour_arg_types = [c.L_OBJECT, c.L_OBJECT]
def add_vecfour(params):
    try:
        vec1 = params[0]
        vec2 = params[1]

        if not len(vec1) == len(vec2):
            sys.error_system.create_error(c.INVALID_ARGUMENT_EXCEPTION, c.LIBRARY, "The two given vectors have to be the same type.", -1)
            sys.cast_all_exceptions()
            return False

        res = (vec1[0] + vec2[0], vec1[1] + vec2[1], vec1[2] + vec2[2], vec1[3] + vec2[3])
        return res
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

sub_vecfour_arg_count = 2
sub_vecfour_arg_types = [c.L_OBJECT, c.L_OBJECT]
def sub_vecfour(params):
    try:
        vec1 = params[0]
        vec2 = params[1]

        if not len(vec1) == len(vec2):
            sys.error_system.create_error(c.INVALID_ARGUMENT_EXCEPTION, c.LIBRARY, "The two given vectors have to be the same type.", -1)
            sys.cast_all_exceptions()
            return False

        res = (vec1[0] + vec2[0], vec1[1] + vec2[1], vec1[2] + vec2[2], vec1[3] + vec2[3])
        return res
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

div_vecfour_arg_count = 2
div_vecfour_arg_types = [c.L_OBJECT, c.L_NUMBER]
def div_vecfour(params):
    try:
        vec1 = params[0]
        num = params[1]

        return (vec1[0] / num, vec1[1] / num, vec1[2] / num, vec1[3] / num)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

mul_vecfour_arg_count = 2
mul_vecfour_arg_types = [c.L_OBJECT, c.L_NUMBER]
def mul_vecfour(params):
    try:
        vec1 = params[0]
        num = params[1]

        return (vec1[0] * num, vec1[1] * num, vec1[2] * num, vec1[3] * num)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

mag_arg_count = 1
mag_arg_types = [c.L_OBJECT]
def mag(params):
    try:
        vec = params[0]

        if len(vec) == 2: return math_sqrt(vec[0] + vec[1])
        if len(vec) == 3: return math_sqrt(vec[0] + vec[1] + vec[2])
        if len(vec) == 4: return math_sqrt(vec[0] + vec[1] + vec[2] + vec[3])
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

norm_arg_count = 1
norm_arg_types = [c.L_OBJECT]
def norm(params):
    try:
        vec       = params[0]
        magnitude = mag(params)

        if len(vec) == 2: return div_vectwo([vec, magnitude])  
        if len(vec) == 3: return div_vecthree([vec, magnitude])  
        if len(vec) == 4: return div_vecfour([vec, magnitude])  
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False
