# Automatically generated by Pynguin.
import ansible.module_utils.common.text.converters as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = None
    var_0 = module_0.to_bytes(bytes_0)

def test_case_2():
    str_0 = '鶒橛'
    var_0 = module_0.to_bytes(str_0)
    str_1 = '鶒橛'
    str_2 = 'ascii'
    var_1 = module_0.to_bytes(str_1, str_2)
    bytes_0 = b'\x89\x90\xa3\xf1*k\xe0\xb6"'
    bytes_1 = b'\x0bj\xb0\xf0r\xb1\xb5\xa9V3'
    var_2 = module_0.to_bytes(bytes_0, bytes_1)

def test_case_3():
    bytes_0 = b'\xc4c\xeeF\xd8Q\x8f\x0c\xd8\x9ex{<'
    var_0 = module_0.container_to_text(bytes_0)

def test_case_4():
    dict_0 = {}
    var_0 = module_0.to_text(dict_0)

def test_case_5():
    bool_0 = True
    set_0 = {bool_0, bool_0, bool_0, bool_0}
    var_0 = module_0.jsonify(set_0)

def test_case_6():
    bytes_0 = None
    var_0 = module_0.jsonify(bytes_0)

def test_case_7():
    list_0 = []
    var_0 = module_0.container_to_bytes(list_0)

def test_case_8():
    float_0 = 995.982826
    set_0 = {float_0, float_0, float_0}
    bool_0 = False
    var_0 = module_0.container_to_bytes(set_0, bool_0)

def test_case_9():
    str_0 = '\\iGa>W[/3TXn82z-I.Ql'
    var_0 = module_0.container_to_bytes(str_0)

def test_case_10():
    float_0 = 1914.75
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0, float_0, tuple_0]
    var_0 = module_0.container_to_bytes(list_0)
    var_1 = module_0.jsonify(float_0)

def test_case_11():
    list_0 = []
    var_0 = module_0.container_to_text(list_0)

def test_case_12():
    bool_0 = True
    var_0 = module_0.container_to_text(bool_0)

def test_case_13():
    dict_0 = {}
    var_0 = module_0.jsonify(dict_0)

def test_case_14():
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0]
    var_0 = module_0.jsonify(list_0)

def test_case_15():
    bool_0 = False
    complex_0 = None
    var_0 = module_0.container_to_bytes(bool_0, complex_0)
    bool_1 = True
    var_1 = module_0.jsonify(bool_1)
    var_2 = module_0.to_text(bool_0, bool_0, bool_0)

def test_case_16():
    bytes_0 = b'\xfae\xa34\xd9\x92\xecg\xe2M\xc7'
    var_0 = module_0.container_to_text(bytes_0)
    bool_0 = True
    str_0 = '\tA k6tx#I'
    dict_0 = {bool_0: bool_0, str_0: bool_0}
    tuple_0 = (bool_0, dict_0)
    var_1 = module_0.jsonify(tuple_0)

def test_case_17():
    str_0 = '鶒橛'
    var_0 = module_0.to_bytes(str_0)
    str_1 = '鶒橛'
    str_2 = 'ascii'
    var_1 = module_0.to_bytes(str_1, str_2)