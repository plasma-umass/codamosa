# Automatically generated by Pynguin.
import ansible.playbook.included_file as module_0

def test_case_0():
    pass

def test_case_1():
    bool_0 = None
    set_0 = {bool_0}
    float_0 = -745.62
    list_0 = None
    included_file_0 = module_0.IncludedFile(bool_0, set_0, float_0, list_0)

def test_case_2():
    float_0 = None
    str_0 = None
    dict_0 = {float_0: float_0, float_0: str_0, float_0: str_0}
    bytes_0 = b'P\x1d\n\x82f;\xa7\x9c\xdd\xf4\xdf\xb3>'
    bytes_1 = b'\x15\x02"\xc2\xc1A\xcd\x7f\xf2'
    set_0 = {bytes_0, bytes_0, bytes_1}
    tuple_0 = (float_0, set_0)
    included_file_0 = module_0.IncludedFile(bytes_0, tuple_0, tuple_0, dict_0)
    included_file_1 = module_0.IncludedFile(dict_0, included_file_0, str_0, set_0)
    var_0 = included_file_1.__repr__()

def test_case_3():
    dict_0 = {}
    float_0 = None
    int_0 = -2050
    bool_0 = False
    bytes_0 = b'\x1a\x9a\xbc\x91'
    str_0 = '%e12"BtjK#d%G6,*7'
    included_file_0 = module_0.IncludedFile(int_0, bool_0, bytes_0, str_0)
    var_0 = included_file_0.process_include_results(dict_0, dict_0, bool_0, float_0)

def test_case_4():
    str_0 = '/tmp/test.yml'
    str_1 = 'val1'
    str_2 = 'val2'
    str_3 = 'var1'
    str_4 = 'var2'
    str_5 = {str_3: str_1, str_4: str_2}
    var_0 = None
    bool_0 = False
    included_file_0 = module_0.IncludedFile(str_0, str_2, str_5, var_0, bool_0)
    included_file_1 = module_0.IncludedFile(str_0, str_3, str_5, var_0, bool_0)
    str_6 = 'Object 1: '
    var_1 = str(included_file_0)
    var_2 = str_6 + var_1
    str_7 = 'Object 2: '
    var_3 = str(included_file_1)
    var_4 = str_7 + var_3
    str_8 = 'Object 1 __eq__ Object 2? '
    set_0 = set()
    var_5 = included_file_0.add_host(set_0)
    var_6 = included_file_0.__eq__(included_file_1)
    var_7 = str(var_6)
    var_8 = str_8 + var_7
    var_9 = print(var_8)
    str_9 = ''
    var_10 = print(str_9)