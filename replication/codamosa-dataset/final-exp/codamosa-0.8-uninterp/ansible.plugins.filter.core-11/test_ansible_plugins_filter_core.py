# Automatically generated by Pynguin.
import ansible.plugins.filter.core as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'}?(\x02\xf0gY\x91\x865\xfb\xd4\x1fqS\xa3\x12\xac\xb4:'
    var_0 = module_0.from_yaml(bytes_0)
    int_0 = 2488
    str_0 = ''
    bool_0 = True
    list_0 = [int_0, str_0, bool_0]
    var_1 = module_0.to_nice_yaml(int_0, *list_0)

def test_case_2():
    list_0 = None
    str_0 = '-3icmpv6EtyL5?|e'
    dict_0 = {}
    var_0 = module_0.to_nice_json(dict_0, list_0, **dict_0)
    var_1 = module_0.regex_search(list_0, str_0)

def test_case_3():
    str_0 = ''
    var_0 = module_0.to_bool(str_0)

def test_case_4():
    str_0 = '#'
    var_0 = module_0.fileglob(str_0)
    var_1 = module_0.combine()

def test_case_5():
    var_0 = module_0.regex_replace()

def test_case_6():
    list_0 = None
    str_0 = '--icmpv6-type'
    var_0 = module_0.regex_search(list_0, str_0)

def test_case_7():
    filter_module_0 = module_0.FilterModule()
    var_0 = module_0.regex_escape(filter_module_0)

def test_case_8():
    list_0 = []
    var_0 = module_0.from_yaml(list_0)
    list_1 = None
    str_0 = '-3icmp|9j~6Eyy\t5?|e'
    var_1 = module_0.regex_search(list_1, str_0)

def test_case_9():
    str_0 = None
    var_0 = module_0.randomize_list(str_0)

def test_case_10():
    dict_0 = None
    var_0 = module_0.to_uuid(dict_0)

def test_case_11():
    str_0 = 'yAy'
    var_0 = module_0.mandatory(str_0)

def test_case_12():
    var_0 = module_0.combine()

def test_case_13():
    str_0 = 't+%,SazlH)Y"7|'
    var_0 = module_0.comment(str_0)

def test_case_14():
    str_0 = 'f'
    var_0 = module_0.flatten(str_0, str_0)

def test_case_15():
    str_0 = 'posix_extended'
    var_0 = module_0.regex_replace()
    var_1 = module_0.rand(str_0, str_0)
    filter_module_0 = module_0.FilterModule()
    var_2 = filter_module_0.filters()

def test_case_16():
    int_0 = -810
    var_0 = module_0.to_bool(int_0)
    str_0 = '\\~'
    var_1 = module_0.fileglob(str_0)

def test_case_17():
    str_0 = 'python'
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0, str_0]
    var_0 = module_0.combine(*list_0)
    var_1 = module_0.quote(tuple_0)

def test_case_18():
    str_0 = '\n'
    float_0 = None
    set_0 = {str_0, float_0}
    list_0 = [str_0, str_0, str_0]
    bytes_0 = b'_\xe9Li\xb2\xc81\x00V\xaf\x05!/\xf5\xbd\xef\xae\x9c'
    var_0 = module_0.ternary(set_0, list_0, set_0, bytes_0)

def test_case_19():
    set_0 = None
    var_0 = module_0.regex_replace(set_0)
    var_1 = module_0.b64encode(set_0)

def test_case_20():
    str_0 = 'posix_extended'
    var_0 = module_0.regex_replace()
    var_1 = module_0.rand(str_0, str_0)

def test_case_21():
    str_0 = "&xU'&;"
    var_0 = module_0.combine()
    list_0 = [var_0]
    int_0 = -50
    var_1 = module_0.subelements(list_0, str_0, int_0)

def test_case_22():
    str_0 = '\n'
    var_0 = module_0.combine()
    float_0 = None
    set_0 = {str_0, float_0}
    list_0 = []
    bool_0 = None
    var_1 = module_0.ternary(list_0, set_0, bool_0)

def test_case_23():
    str_0 = '\n'
    var_0 = module_0.combine()
    list_0 = [str_0]
    var_1 = module_0.combine(*list_0)

def test_case_24():
    list_0 = None
    str_0 = '-3icmpv6EtyL5?|e'
    var_0 = module_0.regex_search(list_0, str_0)

def test_case_25():
    str_0 = '^$'
    var_0 = module_0.regex_escape(str_0)
    str_1 = 'posix_basic'
    var_1 = module_0.regex_escape(str_0, str_1)
    str_2 = '\\a'
    var_2 = module_0.regex_escape(str_2, str_1)
    str_3 = '\\|'
    var_3 = module_0.regex_escape(str_3)
    str_4 = 'foo'
    var_4 = module_0.regex_escape(str_4)
    str_5 = 'foo.*'
    var_5 = module_0.regex_escape(str_5)
    var_6 = module_0.regex_escape(str_5, str_1)
    str_6 = 'foo.\\'
    var_7 = module_0.regex_escape(str_6)
    var_8 = module_0.regex_escape(str_6, str_1)

def test_case_26():
    str_0 = ''
    var_0 = module_0.comment(str_0)
    str_1 = 'test'
    str_2 = 'plain'
    var_1 = module_0.comment(str_1, str_2)
    str_3 = 'cblock'
    var_2 = module_0.comment(str_0, str_3)
    var_3 = module_0.comment(str_1, str_3)
    dict_0 = {str_2: var_3}
    var_4 = module_0.mandatory(dict_0)

def test_case_27():
    str_0 = ''
    var_0 = module_0.fileglob(str_0)
    str_1 = '/dev/null'
    var_1 = module_0.fileglob(str_1)
    str_2 = 'somefHle'
    var_2 = module_0.fileglob(str_2)
    var_3 = module_0.fileglob(str_2)
    str_3 = '1wBW'
    var_4 = module_0.regex_escape(str_3)

def test_case_28():
    int_0 = 1
    int_1 = 2
    int_2 = 3
    int_3 = [int_0, int_1, int_2]
    int_4 = 4
    int_5 = 5
    int_6 = 6
    int_7 = [int_5, int_6]
    int_8 = [int_3, int_4, int_7]
    var_0 = module_0.flatten(int_8)
    int_9 = [int_0, int_1, int_2]
    int_10 = [int_5, int_6]
    int_11 = [int_9, int_4, int_10]
    var_1 = module_0.flatten(int_11, int_1)
    int_12 = [int_2, int_4]
    int_13 = [int_0, int_1, int_12]
    int_14 = [int_6]
    int_15 = [int_13, int_5, int_14]
    var_2 = module_0.flatten(int_15)
    int_16 = [int_2, int_4]
    int_17 = [int_0, int_1, int_16]
    int_18 = [int_6]
    int_19 = [int_17, int_5, int_18]
    var_3 = module_0.flatten(int_19, int_1)

def test_case_29():
    dict_0 = {}
    list_0 = [dict_0, dict_0, dict_0]
    var_0 = module_0.combine(*list_0)
    bytes_0 = None
    bool_0 = True
    str_0 = '{y-C/o'
    str_1 = 't5T\n;x#DC(s!'
    str_2 = None
    str_3 = ')L'
    str_4 = None
    set_0 = {str_1, str_0, bool_0}
    dict_1 = {str_1: list_0, str_2: str_1, str_3: str_1, str_4: set_0}
    var_1 = module_0.to_bool(dict_1)
    var_2 = module_0.ternary(bytes_0, bool_0, str_0)

def test_case_30():
    str_0 = 'vars'
    var_0 = {}
    var_1 = {str_0: var_0}
    int_0 = 10
    var_2 = module_0.rand(var_1, int_0)
    var_3 = range(int_0)
    int_1 = 2
    var_4 = module_0.rand(var_1, int_0, int_1, int_1)
    int_2 = 0
    var_5 = module_0.rand(var_1, int_0, int_1, int_1, int_2)
    var_6 = range(int_1, int_0, int_1)
    var_7 = range(int_1, int_0, int_1)
    var_8 = range(int_1, int_0, int_1)
    int_3 = 1
    int_4 = 3
    int_5 = 4
    int_6 = 5
    int_7 = [int_3, int_1, int_4, int_5, int_6]
    var_9 = module_0.rand(var_1, int_7)

def test_case_31():
    str_0 = 'name'
    str_1 = 'groups'
    str_2 = 'authorized'
    str_3 = 'alice'
    str_4 = 'wheel'
    str_5 = [str_4]
    str_6 = '/tmp/alice/onekey.pub'
    str_7 = [str_6]
    str_8 = {str_0: str_3, str_1: str_5, str_2: str_7}
    str_9 = [str_8]
    var_0 = module_0.subelements(str_9, str_1)