# Automatically generated by Pynguin.
import string_utils.generation as module_0

def test_case_0():
    str_0 = module_0.uuid()

def test_case_1():
    bool_0 = True
    str_0 = module_0.uuid(bool_0)

def test_case_2():
    int_0 = 7
    generator_0 = module_0.roman_range(int_0)
    str_0 = module_0.random_string(int_0)
    var_0 = list(generator_0)

def test_case_3():
    int_0 = 7
    generator_0 = module_0.roman_range(int_0)
    str_0 = module_0.secure_random_hex(int_0)
    var_0 = list(generator_0)

def test_case_4():
    int_0 = 7
    generator_0 = module_0.roman_range(int_0)
    var_0 = list(generator_0)