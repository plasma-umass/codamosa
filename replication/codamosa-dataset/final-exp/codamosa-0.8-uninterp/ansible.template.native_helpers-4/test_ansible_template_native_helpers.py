# Automatically generated by Pynguin.
import ansible.template.native_helpers as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'qbQ\t4~\\5\\'
    var_0 = module_0.ansible_native_concat(str_0)

def test_case_2():
    str_0 = '^'
    var_0 = module_0.ansible_native_concat(str_0)
    var_1 = module_0.ansible_native_concat(str_0)
    str_1 = '/ +'
    float_0 = -725.405
    list_0 = [str_0]
    complex_0 = None
    str_2 = '{0!r} (FD {1}) is already registered'
    bytes_0 = b'\x85\n'
    tuple_0 = (complex_0, str_2, complex_0, bytes_0)
    tuple_1 = (str_1, float_0, list_0, tuple_0)
    var_2 = module_0.ansible_native_concat(tuple_1)

def test_case_3():
    int_0 = 1
    list_0 = [int_0]
    var_0 = module_0.ansible_native_concat(list_0)

def test_case_4():
    set_0 = set()
    var_0 = module_0.ansible_native_concat(set_0)

def test_case_5():
    str_0 = 'getent_%s'
    dict_0 = {str_0: str_0}
    var_0 = module_0.ansible_native_concat(dict_0)