# Automatically generated by Pynguin.
import ansible.module_utils.common.process as module_0

def test_case_0():
    try:
        str_0 = '.AD?@}[tsA;NeE| '
        var_0 = module_0.get_bin_path(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'c.,[ol7'
        var_0 = module_0.get_bin_path(str_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'sh'
        var_0 = module_0.get_bin_path(str_0)
        bool_0 = False
        bool_1 = False
        dict_0 = {bool_1: var_0}
        var_1 = module_0.get_bin_path(bool_0, dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 512.0
        bool_0 = None
        tuple_0 = (bool_0,)
        var_0 = module_0.get_bin_path(float_0, tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = ''
        var_0 = module_0.get_bin_path(str_0, str_0)
    except BaseException:
        pass