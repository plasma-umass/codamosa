# Automatically generated by Pynguin.
import pysnooper.variables as module_0

def test_case_0():
    try:
        float_0 = -2002.26
        indices_0 = module_0.Indices(float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'h7Z<QP'
        attrs_0 = module_0.Attrs(str_0)
        bool_0 = False
        var_0 = attrs_0.items(bool_0)
        complex_0 = None
        var_1 = attrs_0.items(complex_0)
        base_variable_0 = module_0.BaseVariable(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'str'
        indices_0 = module_0.Indices(str_0)
        str_1 = 'obj_str: '
        var_0 = str(indices_0)
        var_1 = str_1 + var_0
        var_2 = print(var_1)
        int_0 = 0
        int_1 = 1
        var_3 = slice(int_0, int_1)
        var_4 = indices_0[var_3]
        var_5 = str(var_4)
        float_0 = -1776.30414
        var_6 = indices_0.__getitem__(float_0)
    except BaseException:
        pass