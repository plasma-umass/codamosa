# Automatically generated by Pynguin.
import pysnooper.variables as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'rb'
    attrs_0 = module_0.Attrs(str_0)

def test_case_2():
    str_0 = 'f>oo'
    indices_0 = module_0.Indices(str_0)

def test_case_3():
    str_0 = 'a'
    common_variable_0 = module_0.CommonVariable(str_0)
    int_0 = 1
    int_1 = {str_0: int_0}
    list_0 = [common_variable_0, int_1, int_1]
    var_0 = common_variable_0.__eq__(list_0)
    var_1 = common_variable_0.items(int_1)

def test_case_4():
    str_0 = 'testvar'
    common_variable_0 = module_0.CommonVariable(str_0)
    common_variable_1 = module_0.CommonVariable(str_0)
    str_1 = 'testvar2'
    common_variable_2 = module_0.CommonVariable(str_1)
    var_0 = common_variable_0.__eq__(common_variable_1)
    var_1 = common_variable_0.__eq__(common_variable_1)

def test_case_5():
    str_0 = 'foo'
    indices_0 = module_0.Indices(str_0)
    int_0 = 2
    var_0 = indices_0[int_0:int_0]

def test_case_6():
    str_0 = 'ja'
    common_variable_0 = module_0.CommonVariable(str_0)
    var_0 = common_variable_0.items(str_0)