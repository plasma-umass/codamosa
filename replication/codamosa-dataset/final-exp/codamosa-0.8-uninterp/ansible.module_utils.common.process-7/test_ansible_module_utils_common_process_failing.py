# Automatically generated by Pynguin.
import ansible.module_utils.common.process as module_0

def test_case_0():
    try:
        str_0 = '2Y`X'
        var_0 = module_0.get_bin_path(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        set_0 = {bool_0, bool_0, bool_0, bool_0}
        var_0 = module_0.get_bin_path(bool_0, set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '/&~'
        var_0 = module_0.get_bin_path(str_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        set_0 = set()
        var_0 = module_0.get_bin_path(set_0, set_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = ''
        var_0 = module_0.get_bin_path(str_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'python'
        var_0 = module_0.get_bin_path(str_0)
        float_0 = None
        bool_0 = False
        bool_1 = True
        dict_0 = None
        tuple_0 = (bool_0, bool_1, dict_0)
        var_1 = module_0.get_bin_path(float_0, tuple_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'ls'
        var_0 = module_0.get_bin_path(str_0)
        var_1 = module_0.get_bin_path(str_0, str_0)
        str_1 = '/sys/devices/virtual/dmi/id/board_name'
        var_2 = module_0.get_bin_path(str_1)
    except BaseException:
        pass