# Automatically generated by Pynguin.
import ansible.module_utils.common.text.formatters as module_0

def test_case_0():
    try:
        dict_0 = {}
        var_0 = module_0.human_to_bytes(dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'onestart'
        var_0 = module_0.bytes_to_human(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
        int_0 = 4160
        var_0 = module_0.bytes_to_human(int_0)
        var_1 = module_0.human_to_bytes(bool_0, dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '1j0'
        var_0 = module_0.human_to_bytes(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        set_0 = set()
        str_0 = '>ufN,220x]jqLyp?'
        int_0 = -5382
        tuple_0 = (str_0, set_0, dict_0, int_0)
        tuple_1 = (dict_0, set_0, tuple_0)
        var_0 = module_0.lenient_lowercase(tuple_1)
        float_0 = 1436.0774
        str_1 = '3{L$nJLy`UvIrM'
        bytes_0 = b'1N9\x81\xb4\xec\xc6'
        var_1 = module_0.bytes_to_human(float_0, str_1, bytes_0)
        str_2 = '1024'
        var_2 = module_0.human_to_bytes(str_2)
        str_3 = '1K'
        var_3 = module_0.human_to_bytes(str_3)
        list_0 = [str_0, var_2]
        var_4 = module_0.human_to_bytes(list_0, dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '5'
        str_1 = 'mBK\t7FB%|`Y*?&wsnco'
        var_0 = module_0.human_to_bytes(str_0, str_1, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '10'
        str_1 = 'K'
        var_0 = module_0.human_to_bytes(str_0, str_1)
        var_1 = module_0.human_to_bytes(str_0, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '1024'
        var_0 = module_0.human_to_bytes(str_0)
        str_1 = '2048'
        int_0 = -1862
        var_1 = module_0.bytes_to_human(int_0)
        var_2 = module_0.human_to_bytes(str_1)
        str_2 = '10'
        str_3 = 'K'
        var_3 = module_0.human_to_bytes(str_2, str_3)
        int_1 = -2891
        str_4 = 'G'
        var_4 = module_0.bytes_to_human(int_1, str_4, str_3)
        var_5 = module_0.human_to_bytes(str_1)
        str_5 = '3M'
        var_6 = module_0.human_to_bytes(str_5)
        str_6 = '1Kb'
        bool_0 = True
        var_7 = module_0.human_to_bytes(str_6, bool_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '1024'
        var_0 = module_0.human_to_bytes(str_0)
        str_1 = '2048'
        str_2 = ':y+/k_0O&'
        var_1 = module_0.lenient_lowercase(str_2)
        int_0 = -1862
        var_2 = module_0.bytes_to_human(int_0)
        var_3 = module_0.human_to_bytes(str_1)
        str_3 = '5'
        str_4 = 'BKm\t7FB|`Y*?&wnco'
        bytes_0 = b'\xc6\x02 \x94)$\x12&'
        var_4 = module_0.lenient_lowercase(bytes_0)
        var_5 = module_0.human_to_bytes(str_3, str_4)
    except BaseException:
        pass