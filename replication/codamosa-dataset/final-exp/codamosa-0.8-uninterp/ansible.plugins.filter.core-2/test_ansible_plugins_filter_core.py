# Automatically generated by Pynguin.
import ansible.plugins.filter.core as module_0
import glob as module_1

def test_case_0():
    pass

def test_case_1():
    var_0 = module_0.regex_replace()
    str_0 = 'DSSf#v>x1U~'
    var_1 = module_0.fileglob(str_0)
    list_0 = []
    var_2 = module_0.to_yaml(list_0)

def test_case_2():
    list_0 = []
    str_0 = 'list_merge'
    bool_0 = None
    list_1 = [bool_0]
    var_0 = module_0.to_nice_yaml(list_1)
    var_1 = module_0.subelements(list_0, str_0, bool_0)
    filter_module_0 = module_0.FilterModule()
    var_2 = module_0.regex_findall(filter_module_0, str_0)
    dict_0 = None
    var_3 = module_0.to_json(dict_0)

def test_case_3():
    str_0 = '/etc/*/*'
    var_0 = module_0.fileglob(str_0)
    var_1 = module_1.glob(str_0)

def test_case_4():
    var_0 = module_0.regex_replace()

def test_case_5():
    int_0 = -1183
    var_0 = module_0.from_yaml_all(int_0)

def test_case_6():
    float_0 = 1546343600.0
    str_0 = '%Y-%m-%d %H:%M:%S'
    var_0 = module_0.strftime(str_0)
    var_1 = module_0.strftime(str_0, float_0)
    str_1 = '%Y-%m-%d'
    var_2 = module_0.strftime(str_1, float_0)
    str_2 = None
    dict_0 = {str_1: var_2, str_2: str_1}
    var_3 = module_0.regex_escape(dict_0)
    filter_module_0 = module_0.FilterModule()
    str_3 = '/usr/bin/zypper'
    var_4 = module_0.from_yaml_all(str_3)
    var_5 = module_0.regex_escape(filter_module_0)

def test_case_7():
    bool_0 = True
    var_0 = module_0.randomize_list(bool_0)

def test_case_8():
    str_0 = 'hexdigest'
    var_0 = module_0.randomize_list(str_0)
    filter_module_0 = module_0.FilterModule()
    var_1 = module_0.regex_search(filter_module_0, str_0)

def test_case_9():
    filter_module_0 = None
    var_0 = module_0.get_hash(filter_module_0)
    var_1 = module_0.regex_replace()
    str_0 = 'DSSf#v>x1U~'
    var_2 = module_0.fileglob(str_0)
    list_0 = None
    tuple_0 = ()
    var_3 = module_0.mandatory(tuple_0, list_0)

def test_case_10():
    str_0 = 'GHR$k'
    str_1 = '"uuvk+\t,I['
    var_0 = module_0.to_bool(str_1)
    list_0 = [str_0, str_0, str_0]
    var_1 = module_0.to_uuid(list_0)

def test_case_11():
    str_0 = 'Hello'
    var_0 = module_0.mandatory(str_0)

def test_case_12():
    str_0 = "u<mZKxSsP'uy,"
    var_0 = module_0.comment(str_0)

def test_case_13():
    str_0 = '>t i^t5p|QKxn{'
    var_0 = module_0.flatten(str_0)

def test_case_14():
    list_0 = []
    var_0 = module_0.subelements(list_0, list_0)

def test_case_15():
    list_0 = []
    str_0 = 'pthnq.'
    bool_0 = None
    var_0 = module_0.subelements(list_0, str_0, bool_0)

def test_case_16():
    str_0 = 'Hello'
    var_0 = module_0.regex_search(str_0, str_0)

def test_case_17():
    bool_0 = True
    var_0 = module_0.to_bool(bool_0)
    float_0 = -3832.886205
    var_1 = module_0.from_yaml(float_0)

def test_case_18():
    bool_0 = None
    var_0 = module_0.to_uuid(bool_0)
    filter_module_0 = module_0.FilterModule()
    bytes_0 = b'\xdb\x03\xb6}v\xe5\x02!2'
    var_1 = module_0.b64encode(bytes_0)
    list_0 = [var_0, var_0, bool_0, bool_0]
    var_2 = module_0.flatten(list_0)

def test_case_19():
    int_0 = 1722
    str_0 = 'b(_8u=`"\\Vp\nP\'c:<qGm'
    var_0 = module_0.rand(int_0, str_0)

def test_case_20():
    str_0 = 'hexdigest'
    filter_module_0 = module_0.FilterModule()
    var_0 = module_0.regex_search(filter_module_0, str_0)

def test_case_21():
    str_0 = 'hexdigest'
    var_0 = module_0.randomize_list(str_0)
    filter_module_0 = module_0.FilterModule()
    str_1 = '=|n\tYn aaFQj~k;=AZG'
    list_0 = [var_0, filter_module_0, str_0, str_1]
    var_1 = module_0.flatten(list_0)
    var_2 = module_0.combine()

def test_case_22():
    str_0 = 'abcdefg^'
    str_1 = 'def'
    str_2 = 'DEF'
    bool_0 = True
    var_0 = module_0.regex_replace(str_0, str_1, str_2, bool_0)
    bool_1 = False
    var_1 = module_0.regex_replace(str_0, str_1, str_2, bool_1)
    var_2 = module_0.regex_replace(str_0, str_1, str_2, bool_0, bool_0)
    var_3 = module_0.regex_replace(str_0, str_1, str_2, bool_1, bool_0)

def test_case_23():
    str_0 = '&b'
    var_0 = module_0.path_join(str_0)
    str_1 = 'hexdigest'
    var_1 = module_0.randomize_list(str_1)
    bool_0 = False
    var_2 = module_0.randomize_list(bool_0)

def test_case_24():
    float_0 = 1546343600.0
    str_0 = '%Y-%m-%d %H:%M:%S'
    bool_0 = True
    var_0 = module_0.rand(float_0, bool_0)
    var_1 = module_0.strftime(str_0)
    var_2 = module_0.strftime(str_0, float_0)
    var_3 = module_0.strftime(str_0, float_0)

def test_case_25():
    str_0 = '\\g<0>'
    filter_module_0 = None
    str_1 = '3<v0\tj8E8HuK'
    list_0 = [str_0]
    var_0 = module_0.regex_search(filter_module_0, str_1, *list_0)

def test_case_26():
    str_0 = 'abcdefabcdefabcdef'
    str_1 = 'abc'
    var_0 = module_0.regex_findall(str_0, str_1)
    str_2 = 'ABCDEFabcdefabcdef'
    bool_0 = True
    bool_1 = True
    var_1 = module_0.regex_findall(str_2, str_1, bool_1)
    var_2 = module_0.regex_findall(str_2, str_1, bool_0, bool_0)
    var_3 = module_0.regex_findall(str_2, str_1, bool_0, bool_1)

def test_case_27():
    str_0 = 'name'
    str_1 = 'groups'
    str_2 = 'authorized'
    str_3 = 'alice'
    str_4 = [str_1]
    str_5 = '/tmp/alice/onekey.pub'
    str_6 = {str_0: str_3, str_1: str_4, str_2: str_5}
    str_7 = [str_6]
    var_0 = module_0.subelements(str_7, str_1)