# Automatically generated by Pynguin.
import ansible.module_utils.common.parameters as module_0

def test_case_0():
    pass

def test_case_1():
    bool_0 = True
    dict_0 = {bool_0: bool_0}
    var_0 = module_0.remove_values(bool_0, dict_0)

def test_case_2():
    bytes_0 = b'M'
    dict_0 = {}
    var_0 = module_0.remove_values(bytes_0, dict_0)

def test_case_3():
    str_0 = '}qeQ'
    var_0 = module_0.remove_values(str_0, str_0)

def test_case_4():
    float_0 = 512.0
    list_0 = [float_0]
    bool_0 = False
    float_1 = -119.207
    list_1 = [float_0, bool_0, bool_0, float_1]
    var_0 = module_0.remove_values(list_0, list_1)
    set_0 = set()
    bytes_0 = b'Tz'
    var_1 = module_0.sanitize_keys(set_0, bytes_0)

def test_case_5():
    bool_0 = False
    bytes_0 = b''
    var_0 = module_0.remove_values(bool_0, bytes_0)

def test_case_6():
    bytes_0 = b'WYXT\xfd\xe6\xae\xae\xc4L\x15\x88B\xcf\x0f'
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    list_0 = [dict_0, dict_0, bytes_0, dict_0]
    var_0 = module_0.remove_values(dict_0, list_0)

def test_case_7():
    var_0 = {}
    list_0 = [var_0, var_0]
    str_0 = 'ubAICR'
    var_1 = module_0.sanitize_keys(list_0, str_0)

def test_case_8():
    bool_0 = True
    set_0 = {bool_0}
    var_0 = module_0.sanitize_keys(bool_0, set_0)

def test_case_9():
    str_0 = 'vA9ew'
    dict_0 = {str_0: str_0}
    bytes_0 = b'{dh4'
    var_0 = module_0.remove_values(str_0, dict_0)
    list_0 = [bytes_0, bytes_0, bytes_0, str_0]
    list_1 = [bytes_0, dict_0, list_0]
    var_1 = module_0.sanitize_keys(dict_0, bytes_0, list_1)

def test_case_10():
    str_0 = 'ANSIBLE_UNORTUNATE_VARIABLE'
    bytes_0 = b'\x14\xf1!\x89\xd5\xc1,\x13\xaf'
    set_0 = {str_0, bytes_0, str_0}
    list_0 = []
    var_0 = module_0.remove_values(set_0, list_0)

def test_case_11():
    set_0 = set()
    bytes_0 = b'Tz'
    var_0 = module_0.sanitize_keys(set_0, bytes_0)

def test_case_12():
    bytes_0 = b'\xd4\xd5p\xfe'
    float_0 = -1202.67
    set_0 = {bytes_0, float_0, float_0}
    str_0 = ''
    bool_0 = False
    tuple_0 = (str_0, set_0, bool_0)
    var_0 = module_0.sanitize_keys(tuple_0, bytes_0)

def test_case_13():
    str_0 = '_ansible_no_log'
    str_1 = 'foo'
    bool_0 = True
    str_2 = 'bar'
    str_3 = 'baz'
    str_4 = 'secret'
    str_5 = {str_3: str_4}
    str_6 = {str_2: str_5}
    var_0 = {str_0: bool_0, str_1: str_6}
    str_7 = [str_4]
    var_1 = module_0.sanitize_keys(var_0, str_7)