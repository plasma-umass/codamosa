# Automatically generated by Pynguin.
import mimesis.random as module_0

def test_case_0():
    try:
        str_0 = '.ls'
        random_0 = module_0.Random(str_0)
        str_1 = 'IIVL`\rn3dO;q_Z/xPI3R'
        random_1 = module_0.Random()
        str_2 = random_1.generate_string(str_1)
        int_0 = -281
        random_2 = module_0.Random()
        list_0 = random_2.randints(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        random_0 = module_0.Random()
        str_0 = random_0.randstr()
        int_0 = 2564
        int_1 = 5171
        list_0 = random_0.randints(int_0, int_1)
        bytes_0 = random_0.urandom()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'A<f:Ed=:hMufy=5:~}v'
        random_0 = module_0.Random()
        str_1 = random_0.randstr()
        random_1 = module_0.Random()
        str_2 = random_1.custom_code(str_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        random_0 = module_0.Random()
        any_0 = module_0.get_random_item(random_0)
    except BaseException:
        pass

def test_case_4():
    try:
        tuple_0 = ()
        float_0 = 10.0
        any_0 = module_0.get_random_item(tuple_0, float_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 3
        random_0 = module_0.Random(int_0)
        str_0 = '@####'
        str_1 = random_0.custom_code(str_0)
        str_2 = '@##@'
        str_3 = random_0.custom_code(str_2)
        str_4 = '##@@'
        str_5 = random_0.custom_code(str_4)
        str_6 = '###@'
        str_7 = random_0.custom_code(str_6)
        str_8 = '##@'
        str_9 = random_0.custom_code(str_8)
        str_10 = '#@#'
        str_11 = '#'
        str_12 = '@'
        str_13 = random_0.custom_code(str_10, str_11, str_12)
        str_14 = random_0.custom_code(str_10, str_11)
    except BaseException:
        pass