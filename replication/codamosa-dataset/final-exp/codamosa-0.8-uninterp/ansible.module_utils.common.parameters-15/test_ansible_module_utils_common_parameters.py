# Automatically generated by Pynguin.
import ansible.module_utils.common.parameters as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = 1757
    dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
    var_0 = module_0.remove_values(int_0, dict_0)

def test_case_2():
    tuple_0 = ()
    bytes_0 = b'\xa8\xb4\x1e\x1f\x08\x9c\x05dC\t|\x03\xac\xb8\x99\xd0V\xe6'
    list_0 = [tuple_0, tuple_0, tuple_0, bytes_0]
    var_0 = module_0.remove_values(list_0, bytes_0)

def test_case_3():
    list_0 = None
    bytes_0 = b'\xbb\x7f\x05>I6\x81&\xee\x0e\xdf\xc4_\xe9\xadrdX'
    var_0 = module_0.remove_values(list_0, bytes_0)

def test_case_4():
    dict_0 = {}
    tuple_0 = ()
    var_0 = module_0.remove_values(dict_0, tuple_0)

def test_case_5():
    list_0 = None
    bytes_0 = b'\xbb\x7f\x05>I6\x81&\xee\x0e\xdf\xc4_\xe9\xadrdX'
    var_0 = module_0.remove_values(list_0, bytes_0)
    set_0 = {var_0, list_0, var_0}
    str_0 = 'N|KAfX5Cf9q7L6+mQ'
    var_1 = module_0.remove_values(set_0, str_0)

def test_case_6():
    dict_0 = {}
    tuple_0 = (dict_0,)
    float_0 = 1261.8
    var_0 = module_0.sanitize_keys(tuple_0, tuple_0, float_0)

def test_case_7():
    int_0 = None
    dict_0 = {}
    var_0 = module_0.sanitize_keys(int_0, dict_0)

def test_case_8():
    str_0 = 'Validate env_fallback function'
    set_0 = {str_0, str_0, str_0, str_0}
    var_0 = module_0.sanitize_keys(set_0, set_0)

def test_case_9():
    str_0 = 'Q4R mQR~K&\x0bUuK>!'
    str_1 = 'sqRy`v^o08vgT'
    dict_0 = {str_1: str_1, str_0: str_0, str_1: str_1, str_1: str_1}
    bytes_0 = b''
    var_0 = module_0.sanitize_keys(dict_0, bytes_0)

def test_case_10():
    int_0 = None
    dict_0 = {}
    dict_1 = {int_0: int_0, int_0: int_0}
    list_0 = [int_0, int_0, dict_0, int_0]
    var_0 = module_0.remove_values(dict_1, list_0)

def test_case_11():
    str_0 = 'head_is_empty'
    float_0 = 2075.75
    set_0 = {float_0, float_0, str_0}
    var_0 = module_0.remove_values(set_0, set_0)

def test_case_12():
    str_0 = '6f2C-cg +)F)lyc[\\'
    str_1 = 'ct9N X*/^5E"{\rgq'
    list_0 = [str_0, str_0, str_1, str_1]
    var_0 = module_0.remove_values(str_0, list_0)

def test_case_13():
    int_0 = 1206
    dict_0 = {}
    var_0 = module_0.set_fallbacks(dict_0, int_0)