# Automatically generated by Pynguin.
import ansible.utils.context_objects as module_0

def test_case_0():
    pass

def test_case_1():
    complex_0 = None
    dict_0 = {complex_0: complex_0}
    c_l_i_args_0 = module_0.CLIArgs(dict_0)

def test_case_2():
    str_0 = 'test1'
    int_0 = 1234
    str_1 = '='
    str_2 = 'test3'
    int_1 = 1
    int_2 = 2
    int_3 = 3
    int_4 = [int_1, int_2, int_3]
    int_5 = {str_2: int_4}
    var_0 = [str_0, str_1, int_5]
    var_1 = {str_0: int_0, int_2: int_3, str_1: var_0}
    c_l_i_args_0 = module_0.CLIArgs(var_1)

def test_case_3():
    str_0 = 'foo'
    str_1 = 'bar'
    str_2 = {str_0: str_1}
    c_l_i_args_0 = module_0.CLIArgs(str_2)

def test_case_4():
    str_0 = 'test1'
    str_1 = 'test2'
    int_0 = 1230
    str_2 = 'a'
    str_3 = 'b'
    str_4 = 'test3'
    int_1 = 1
    int_2 = 2
    int_3 = 3
    int_4 = [int_1, int_2, int_3]
    int_5 = {str_4: int_4, str_1: int_3, int_1: int_3}
    var_0 = [str_2, str_3, int_5]
    var_1 = {str_0: int_0, str_1: var_0}
    c_l_i_args_0 = module_0.CLIArgs(var_1)

def test_case_5():
    str_0 = 'y'
    int_0 = 47
    str_1 = 'b'
    str_2 = {str_1: str_1, str_1: str_1}
    str_3 = {str_1, str_1}
    var_0 = {str_0: int_0, str_1: str_2, str_1: str_3}
    c_l_i_args_0 = module_0.CLIArgs(var_0)
    var_1 = frozenset(str_3)

def test_case_6():
    str_0 = 'x'
    str_1 = 'y'
    str_2 = 'z'
    str_3 = 'z2'
    int_0 = 42
    str_4 = 'a'
    str_5 = 'b'
    str_6 = {str_4: str_4, str_5: str_5}
    str_7 = [str_4, str_2, str_5]
    str_8 = {str_3, str_4, str_5, str_5, int_0}
    var_0 = {str_0: int_0, str_1: str_6, str_2: str_7, str_3: str_8}
    c_l_i_args_0 = module_0.CLIArgs(var_0)
    str_9 = {str_4, str_5}
    var_1 = frozenset(str_9)