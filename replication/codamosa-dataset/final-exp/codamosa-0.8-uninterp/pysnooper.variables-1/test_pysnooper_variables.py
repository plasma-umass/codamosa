# Automatically generated by Pynguin.
import pysnooper.variables as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'a'
    indices_0 = module_0.Indices(str_0)
    var_0 = indices_0.items(str_0)

def test_case_2():
    str_0 = 'a'
    indices_0 = module_0.Indices(str_0)
    indices_1 = module_0.Indices(str_0)

def test_case_3():
    str_0 = 'var'
    indices_0 = module_0.Indices(str_0)
    int_0 = 1
    int_1 = 2
    var_0 = slice(int_0, int_1)
    var_1 = indices_0.__getitem__(var_0)