# Automatically generated by Pynguin.
import ansible.playbook.included_file as module_0

def test_case_0():
    pass

def test_case_1():
    set_0 = None
    set_1 = {set_0}
    bool_0 = False
    str_0 = 'aR~T"'
    bytes_0 = b'\xe9\t'
    tuple_0 = ()
    str_1 = '~\x0b5y!%+^N+hnS#p%'
    bool_1 = False
    included_file_0 = module_0.IncludedFile(tuple_0, str_1, set_1, tuple_0, bool_1)
    included_file_1 = module_0.IncludedFile(str_0, bytes_0, tuple_0, included_file_0, bytes_0)
    included_file_2 = module_0.IncludedFile(set_1, bool_0, str_0, included_file_1, tuple_0)
    var_0 = included_file_2.__repr__()

def test_case_2():
    float_0 = 0.0
    tuple_0 = ()
    float_1 = 8.0
    float_2 = -3788.23542
    int_0 = 484
    included_file_0 = module_0.IncludedFile(tuple_0, tuple_0, float_1, float_2, int_0)
    set_0 = set()
    bytes_0 = b'\xf9o\x0c\xbd9\xf8\xbc\xfa\xfa\r'
    var_0 = included_file_0.process_include_results(set_0, float_1, bytes_0, set_0)
    int_1 = 79
    included_file_1 = module_0.IncludedFile(included_file_0, int_1, tuple_0, int_1)
    var_1 = included_file_1.add_host(float_0)

def test_case_3():
    bytes_0 = b'@\xd0d\xa1\xe7\x1b\x8fx\xee.\xd2\x89E'
    float_0 = 100.0
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: float_0}
    float_1 = -1264.0
    str_0 = 'download_dir'
    bool_0 = False
    tuple_0 = ()
    str_1 = ',v\'"2#IR^m%\x0b tDH`'
    list_0 = [float_1]
    included_file_0 = module_0.IncludedFile(list_0, str_1, dict_0, dict_0, tuple_0)
    int_0 = 603
    included_file_1 = module_0.IncludedFile(dict_0, str_1, included_file_0, int_0, float_0)
    tuple_1 = (bool_0, tuple_0, included_file_1, tuple_0)
    included_file_2 = module_0.IncludedFile(dict_0, float_1, str_0, tuple_1, dict_0)
    str_2 = '`jp_yMDbnxvb'
    str_3 = 'TaSTXj\n.*'
    tuple_2 = ()
    str_4 = 'DN|$e'
    bool_1 = True
    list_1 = [str_4, bool_1, str_4, str_3]
    included_file_3 = module_0.IncludedFile(str_2, str_3, tuple_2, list_1)
    var_0 = included_file_3.__eq__(included_file_2)

def test_case_4():
    str_0 = 'filename'
    str_1 = 'args'
    str_2 = 'task'
    str_3 = 'is_role'
    included_file_0 = module_0.IncludedFile(str_0, str_1, str_3, str_2, str_3)
    str_4 = 'hosts'
    var_0 = included_file_0.add_host(str_4)
    included_file_1 = module_0.IncludedFile(str_0, str_1, str_2, str_2, str_3)
    var_1 = included_file_1.add_host(str_4)
    var_2 = included_file_0.__eq__(included_file_1)

def test_case_5():
    str_0 = '\x0cW'
    str_1 = 'task'
    str_2 = 'is_role'
    included_file_0 = module_0.IncludedFile(str_0, str_2, str_2, str_1, str_2)
    str_3 = 'hosts'
    var_0 = included_file_0.add_host(str_3)
    included_file_1 = module_0.IncludedFile(str_0, str_3, str_1, str_1, str_2)
    var_1 = included_file_0.__eq__(included_file_1)