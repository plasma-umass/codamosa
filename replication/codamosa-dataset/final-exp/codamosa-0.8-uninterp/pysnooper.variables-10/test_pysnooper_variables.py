# Automatically generated by Pynguin.
import pysnooper.variables as module_0

def test_case_0():
    pass

def test_case_1():
    float_0 = -1264.0
    var_0 = module_0.needs_parentheses(float_0)

def test_case_2():
    str_0 = 'a'
    attrs_0 = module_0.Attrs(str_0)

def test_case_3():
    str_0 = 'a'
    attrs_0 = module_0.Attrs(str_0)
    attrs_1 = module_0.Attrs(str_0)
    var_0 = attrs_0.__eq__(attrs_1)
    attrs_2 = module_0.Attrs(str_0)
    attrs_3 = module_0.Attrs(str_0)
    var_1 = print(str_0)

def test_case_4():
    str_0 = 't1'
    indices_0 = module_0.Indices(str_0)
    int_0 = 1
    int_1 = 3
    var_0 = indices_0[int_0:int_1]

def test_case_5():
    str_0 = 'myin_v,lue'
    indices_0 = module_0.Indices(str_0)

def test_case_6():
    str_0 = 'a'
    attrs_0 = module_0.Attrs(str_0)
    var_0 = attrs_0.items(attrs_0)

def test_case_7():
    str_0 = 'a'
    attrs_0 = module_0.Attrs(str_0)
    int_0 = 3
    float_0 = -3231.502
    var_0 = attrs_0.__eq__(float_0)
    var_1 = attrs_0.items(int_0)