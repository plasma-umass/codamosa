# Automatically generated by Pynguin.
import ansible.utils.color as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'gray1'
    var_0 = module_0.parsecolor(str_0)

def test_case_2():
    dict_0 = {}
    bytes_0 = b'\x14Wd\x1f'
    var_0 = module_0.stringc(dict_0, bytes_0)

def test_case_3():
    set_0 = None
    str_0 = 'Qm.~|'
    var_0 = module_0.colorize(set_0, str_0, set_0)

def test_case_4():
    bool_0 = False
    str_0 = "i'>F@A$\rb MpJl\n"
    var_0 = module_0.hostcolor(bool_0, str_0)

def test_case_5():
    int_0 = -3645
    float_0 = -473.225694
    str_0 = 't6\nKmkWISPx0&tO.qF'
    var_0 = module_0.colorize(int_0, float_0, str_0)
    bytes_0 = b''
    str_1 = '34z%;PPeh@YX'
    bool_0 = False
    var_1 = module_0.stringc(bytes_0, str_1, bool_0)
    int_1 = 804
    float_1 = 2184.9782
    var_2 = module_0.hostcolor(int_1, float_1)
    tuple_0 = ()
    float_2 = 3628.0
    dict_0 = {bool_0: int_1, int_1: bytes_0, var_1: float_1, int_1: str_1}
    str_2 = 'ppoG'
    var_3 = module_0.colorize(float_2, dict_0, str_2)
    var_4 = module_0.colorize(tuple_0, str_1, int_1)
    str_3 = 'vm_stat'
    bool_1 = True
    var_5 = module_0.colorize(str_3, bool_0, bool_1)

def test_case_6():
    str_0 = 'color10'
    var_0 = module_0.parsecolor(str_0)
    str_1 = 'gray1'
    var_1 = module_0.parsecolor(str_1)
    var_2 = module_0.parsecolor(str_0)

def test_case_7():
    str_0 = 'green'
    var_0 = module_0.parsecolor(str_0)
    str_1 = 'color2'
    var_1 = module_0.parsecolor(str_1)
    str_2 = 'color10'
    var_2 = module_0.parsecolor(str_2)
    str_3 = 'gray1'
    var_3 = module_0.parsecolor(str_3)
    str_4 = 'gray10'
    var_4 = module_0.parsecolor(str_4)
    str_5 = 'rgb322'
    var_5 = module_0.parsecolor(str_5)
    str_6 = 'rgb333'
    var_6 = module_0.parsecolor(str_6)