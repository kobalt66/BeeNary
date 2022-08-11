from src.classes import system
from numpy import sqrt as math_sqrt, sinc as math_sin, sinh as math_sinh, arcsin as math_arcsin, tanh as math_tan, arctan as math_arctan, cosh as math_cos, arccos as math_arccos
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
        return a ** b
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

arccos_arg_count = 1
arccos_arg_types = [c.L_NUMBER]
def arccos(params):
    try:
        num = params[0]
        return math_arccos(num)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()


vec2_arg_count = 2
vec2_arg_types = [c.L_NUMBER, c.L_NUMBER]
def vec2(params):
    try:
        x = params[0]
        y = params[1]

        return (x, y)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

vec3_arg_count = 3
vec3_arg_types = [c.L_NUMBER, c.L_NUMBER, c.L_NUMBER]
def vec3(params):
    try:
        x = params[0]
        y = params[1]
        z = params[2]

        return (x, y, z)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

vec4_arg_count = 4
vec4_arg_types = [c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER]
def vec4(params):
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

add_vec2_arg_count = 2
add_vec2_arg_types = [c.L_OBJECT, c.L_OBJECT]
def add_vec2(params):
    try:
        vec1 = params[0]
        vec2 = params[1]

        if not len(vec1) == len(vec2):
            sys.error_system.create_error(c.INVALID_ARGUMENT_EXCEPTION, c.LIBRARY, "The 2 given vectors have to be the same type.", -1)
            sys.cast_all_exceptions()
            return False

        res = (vec1[0] + vec2[0], vec1[1] + vec2[1])
        return res
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

sub_vec2_arg_count = 2
sub_vec2_arg_types = [c.L_OBJECT, c.L_OBJECT]
def sub_vec2(params):
    try:
        vec1 = params[0]
        vec2 = params[1]

        if not len(vec1) == len(vec2):
            sys.error_system.create_error(c.INVALID_ARGUMENT_EXCEPTION, c.LIBRARY, "The 2 given vectors have to be the same type.", -1)
            sys.cast_all_exceptions()
            return False

        res = (vec1[0] - vec2[0], vec1[1] - vec2[1])
        return res
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

div_vec2_arg_count = 2
div_vec2_arg_types = [c.L_OBJECT, c.L_NUMBER]
def div_vec2(params):
    try:
        vec1 = params[0]
        num = params[1]

        return (vec1[0] / num, vec1[1] / num)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

mul_vec2_arg_count = 2
mul_vec2_arg_types = [c.L_OBJECT, c.L_NUMBER]
def mul_vec2(params):
    try:
        vec1 = params[0]
        num = params[1]

        return (vec1[0] * num, vec1[1] * num)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

add_vec3_arg_count = 2
add_vec3_arg_types = [c.L_OBJECT, c.L_OBJECT]
def add_vec3(params):
    try:
        vec1 = params[0]
        vec2 = params[1]

        if not len(vec1) == len(vec2):
            sys.error_system.create_error(c.INVALID_ARGUMENT_EXCEPTION, c.LIBRARY, "The 2 given vectors have to be the same type.", -1)
            sys.cast_all_exceptions()
            return False

        res = (vec1[0] + vec2[0], vec1[1] + vec2[1], vec1[2] + vec2[2])
        return res
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

sub_vec3_arg_count = 2
sub_vec3_arg_types = [c.L_OBJECT, c.L_OBJECT]
def sub_vec3(params):
    try:
        vec1 = params[0]
        vec2 = params[1]

        if not len(vec1) == len(vec2):
            sys.error_system.create_error(c.INVALID_ARGUMENT_EXCEPTION, c.LIBRARY, "The 2 given vectors have to be the same type.", -1)
            sys.cast_all_exceptions()
            return False

        res = (vec1[0] - vec2[0], vec1[1] - vec2[1], vec1[2] - vec2[2])
        return res
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

div_vec3_arg_count = 2
div_vec3_arg_types = [c.L_OBJECT, c.L_NUMBER]
def div_vec3(params):
    try:
        vec1 = params[0]
        num = params[1]

        return (vec1[0] / num, vec1[1] / num, vec1[2] / num)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

mul_vec3_arg_count = 2
mul_vec3_arg_types = [c.L_OBJECT, c.L_NUMBER]
def mul_vec3(params):
    try:
        vec1 = params[0]
        num = params[1]

        return (vec1[0] * num, vec1[1] * num, vec1[2] * num)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

add_vec4_arg_count = 2
add_vec4_arg_types = [c.L_OBJECT, c.L_OBJECT]
def add_vec4(params):
    try:
        vec1 = params[0]
        vec2 = params[1]

        if not len(vec1) == len(vec2):
            sys.error_system.create_error(c.INVALID_ARGUMENT_EXCEPTION, c.LIBRARY, "The 2 given vectors have to be the same type.", -1)
            sys.cast_all_exceptions()
            return False

        res = (vec1[0] + vec2[0], vec1[1] + vec2[1], vec1[2] + vec2[2], vec1[3] + vec2[3])
        return res
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

sub_vec4_arg_count = 2
sub_vec4_arg_types = [c.L_OBJECT, c.L_OBJECT]
def sub_vec4(params):
    try:
        vec1 = params[0]
        vec2 = params[1]

        if not len(vec1) == len(vec2):
            sys.error_system.create_error(c.INVALID_ARGUMENT_EXCEPTION, c.LIBRARY, "The 2 given vectors have to be the same type.", -1)
            sys.cast_all_exceptions()
            return False

        res = (vec1[0] + vec2[0], vec1[1] + vec2[1], vec1[2] + vec2[2], vec1[3] + vec2[3])
        return res
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

div_vec4_arg_count = 2
div_vec4_arg_types = [c.L_OBJECT, c.L_NUMBER]
def div_vec4(params):
    try:
        vec1 = params[0]
        num = params[1]

        return (vec1[0] / num, vec1[1] / num, vec1[2] / num, vec1[3] / num)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

mul_vec4_arg_count = 2
mul_vec4_arg_types = [c.L_OBJECT, c.L_NUMBER]
def mul_vec4(params):
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

        if len(vec) == 2: return div_vec2([vec, magnitude])  
        if len(vec) == 3: return div_vec3([vec, magnitude])  
        if len(vec) == 4: return div_vec4([vec, magnitude])  
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

flyout_vector_arg_count = 1
flyout_vector_arg_types = [c.L_OBJECT]
def flyout_vector(params):
    try:
        vec = params[0]
        [print(e) for e in vec]
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
 
mat2X2_identity_arg_count = 0
mat2X2_identity_arg_types = []
def mat2X2_identity(params):
    try: return [1, 0, 0, 1]
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

mat2X2_arg_count = 4
mat2X2_arg_types = [c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER]
def mat2X2(params):
    try:
        a1, a2 = params[0], params[1]
        b1, b2 = params[2], params[3] 
        return [a1, a2, b1, b2]
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

mat2X3_arg_count = 6
mat2X3_arg_types = [c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER]
def mat2X3(params):
    try:
        a1, a2, a3 = params[0], params[1], params[2]
        b1, b2, b3 = params[3], params[4], params[5]
        return [a1, a2, a3, b1, b2, b3]
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

mat3X3_identity_arg_count = 0
mat3X3_identity_arg_types = []
def mat3X3_identity(params):
    try: return [1, 0, 0, 0, 1, 0, 0, 0, 1]
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

mat3X3_arg_count = 9
mat3X3_arg_types = [c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER]
def mat3X3(params):
    try:
        a1, a2, a3 = params[0], params[1], params[2]
        b1, b2, b3 = params[3], params[4], params[5]
        c1, c2, c3 = params[6], params[7], params[8]
        return [a1, a2, a3, b1, b2, b3, c1, c2, c3]
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

mat3X4_arg_count = 12
mat3X4_arg_types = [c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER]
def mat3X4(params):
    try:
        a1, a2, a3, a4 = params[0],  params[1], params[2],  params[3]
        b1, b2, b3, b4 = params[4],  params[5], params[6],  params[7]
        c1, c2, c3, c4 = params[8],  params[9], params[10], params[11]
        return [a1, a2, a3, a4, b1, b2, b3, b4, c1, c2, c3, c4]
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

mat4X4_identity_arg_count = 0
mat4X4_identity_arg_types = []
def mat4X4_identity(params):
    try: return [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

mat4X4_arg_count = 16
mat4X4_arg_types = [c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER, c.L_NUMBER]
def mat4X4(params):
    try:
        a1, a2, a3, a4 = params[0],  params[1],  params[2],  params[3]
        b1, b2, b3, b4 = params[4],  params[5],  params[6],  params[7]
        c1, c2, c3, c4 = params[8],  params[9],  params[10], params[11]
        d1, d2, d3, d4 = params[12], params[13], params[14], params[15]
        return [a1, a2, a3, a4, b1, b2, b3, b4, c1, c2, c3, c4, d1, d2, d3, d4]
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

flyout_matrix_arg_count = 1
flyout_matrix_arg_types = [c.L_OBJECT]
def flyout_matrix(params):
    try:
        mat = params[0]

        string = ""
        if len(mat) == 4:
            for i in range(4):
                if i % 2 == 0:
                    string += "\n"
                string += f"{mat[i]}\t"
            print(string)
            return
        if len(mat) == 6:
            for i in range(6):
                if i % 3 == 0:
                    string += "\n"
                string += f"{mat[i]}\t"
            print(string)
            return
        if len(mat) == 9:
            for i in range(9):
                if i % 3 == 0:
                    string += "\n"
                string += f"{mat[i]}\t"
            print(string)
            return
        if len(mat) == 12:
            for i in range(12):
                if i % 4 == 0:
                    string += "\n"
                string += f"{mat[i]}\t"
            print(string)
            return
        if len(mat) == 16:
            for i in range(16):
                if i % 4 == 0:
                    string += "\n"
                string += f"{mat[i]}\t"
            print(string)
            return
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()

def get_matrix_row_column_size(mat):
    if len(mat) == 4:     return 2, 2 
    if len(mat) == 6:     return 2, 3 
    if len(mat) == 9:     return 3, 3 
    if len(mat) == 12:    return 3, 4  
    if len(mat) == 16:    return 4, 4
def convert_matrix_for_b(mat):
    result = []
    for row in mat:
        for e in row:
            result.append(e)
    return result
def convert_matrix_for_op(mat, size):
    result  = []
    new_row = []
    count   = 0
    for e in mat:
        new_row.append(e)
        count += 1

        if count % size[0] == 0:
            result.append(new_row)
            new_row = []

    return result

mul_matrices_arg_count = 2
mul_matrices_arg_types = [c.L_OBJECT, c.L_OBJECT]
def mul_matrices(params):
    try:
        matA = params[0]
        matB = params[1]

        rowA, columnA = get_matrix_row_column_size(matA)
        rowB, columnB = get_matrix_row_column_size(matB)
        A = convert_matrix_for_op(matA, (rowA, columnA))
        B = convert_matrix_for_op(matB, (rowB, columnB))

        result = [[sum(a * b for a, b in zip(A_row, B_col))
                    for B_col in zip(*B)]
                        for A_row in A]

        return convert_matrix_for_b(result)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

add_matrices_arg_count = 2
add_matrices_arg_types = [c.L_OBJECT, c.L_OBJECT]
def add_matrices(params):
    try:
        matA = params[0]
        matB = params[1]

        rowA, columnA = get_matrix_row_column_size(matA)
        rowB, columnB = get_matrix_row_column_size(matB)
        A = convert_matrix_for_op(matA, (rowA, columnA))
        B = convert_matrix_for_op(matB, (rowB, columnB))

        result = [[A[i][j] + B[i][j]  for j in range(len(B[0]))] for i in range(len(A))]

        return convert_matrix_for_b(result)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False

sub_matrices_arg_count = 2
sub_matrices_arg_types = [c.L_OBJECT, c.L_OBJECT]
def sub_matrices(params):
    try:
        matA = params[0]
        matB = params[1]

        rowA, columnA = get_matrix_row_column_size(matA)
        rowB, columnB = get_matrix_row_column_size(matB)
        A = convert_matrix_for_op(matA, (rowA, columnA))
        B = convert_matrix_for_op(matB, (rowB, columnB))

        result = [[A[i][j] - B[i][j]  for j in range(len(B[0]))] for i in range(len(A))]

        return convert_matrix_for_b(result)
    except Exception as e:
        sys.error_system.create_warning_from_exception(e, c.PYTHON_EXCEPTION, c.LIBRARY, -1)
        sys.cast_all_exceptions()
        return False
