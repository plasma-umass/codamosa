# Automatically generated by Pynguin.
import pysnooper.variables as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'OqfG *rX'
    common_variable_0 = module_0.CommonVariable(str_0)

def test_case_2():
    str_0 = 'aj'
    attrs_0 = module_0.Attrs(str_0)
    var_0 = attrs_0.items(attrs_0)
    set_0 = {attrs_0, attrs_0, str_0}
    var_1 = attrs_0.items(set_0)

def test_case_3():
    str_0 = 'OqfG *rX'
    common_variable_0 = module_0.CommonVariable(str_0)
    common_variable_1 = module_0.CommonVariable(str_0)

def test_case_4():
    str_0 = 'aj'
    attrs_0 = module_0.Attrs(str_0)
    var_0 = attrs_0.items(str_0)

def test_case_5():
    str_0 = 'a'
    int_0 = 1
    int_1 = 2
    int_2 = (int_0, int_1)
    indices_0 = module_0.Indices(str_0, int_2)
    var_0 = indices_0[:int_1]
    var_1 = None
    var_2 = slice(var_1, int_1)