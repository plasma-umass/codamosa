# Automatically generated by Pynguin.
import ansible.utils.color as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'oLWDQ'
    int_0 = -278
    var_0 = module_0.stringc(str_0, int_0)

def test_case_2():
    str_0 = 'nLv[i+O'
    bool_0 = None
    var_0 = module_0.colorize(str_0, bool_0, bool_0)

def test_case_3():
    int_0 = 287
    var_0 = module_0.hostcolor(int_0, int_0)

def test_case_4():
    str_0 = 'blue'
    var_0 = module_0.parsecolor(str_0)
    str_1 = 'gray2'
    var_1 = module_0.parsecolor(str_1)

def test_case_5():
    str_0 = 'green'
    var_0 = module_0.parsecolor(str_0)
    var_1 = module_0.parsecolor(str_0)
    str_1 = 'blue'
    var_2 = module_0.parsecolor(str_1)
    str_2 = 'magenta'
    var_3 = module_0.parsecolor(str_2)
    var_4 = module_0.parsecolor(str_0)
    var_5 = module_0.parsecolor(str_0)
    str_3 = 'color15'
    var_6 = module_0.parsecolor(str_3)

def test_case_6():
    str_0 = 'blue'
    var_0 = module_0.parsecolor(str_0)
    str_1 = 'rgb124'
    var_1 = module_0.parsecolor(str_1)