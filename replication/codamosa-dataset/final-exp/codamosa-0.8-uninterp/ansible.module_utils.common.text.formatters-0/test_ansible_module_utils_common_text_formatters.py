# Automatically generated by Pynguin.
import ansible.module_utils.common.text.formatters as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'BJC1Aixa+'
    var_0 = module_0.lenient_lowercase(str_0)

def test_case_2():
    bytes_0 = b'SB\xd7J4k\x96\x89\x92\x8e\xd2\xfe\x9f\x90g\x08c$}2'
    var_0 = module_0.lenient_lowercase(bytes_0)

def test_case_3():
    float_0 = 1875.86144
    var_0 = module_0.human_to_bytes(float_0)

def test_case_4():
    bool_0 = False
    var_0 = module_0.bytes_to_human(bool_0)

def test_case_5():
    int_0 = 1048576
    bool_0 = True
    var_0 = module_0.bytes_to_human(int_0, bool_0)
    str_0 = 'Mb'
    var_1 = module_0.bytes_to_human(int_0, bool_0, str_0)
    str_1 = 'M'
    var_2 = module_0.bytes_to_human(int_0, bool_0, str_1)
    str_2 = 'b'
    var_3 = module_0.bytes_to_human(int_0, bool_0, str_2)
    str_3 = 'B'
    var_4 = module_0.bytes_to_human(int_0, bool_0, str_3)
    str_4 = 'm'
    var_5 = module_0.bytes_to_human(int_0, str_4)

def test_case_6():
    bool_0 = True
    var_0 = module_0.bytes_to_human(bool_0)

def test_case_7():
    str_0 = "test_human_to_bytes(): test '10M' - fail"
    var_0 = print(str_0)
    str_1 = '10MB'
    var_1 = module_0.human_to_bytes(str_1)
    var_2 = print(str_0)
    var_3 = print(var_1)