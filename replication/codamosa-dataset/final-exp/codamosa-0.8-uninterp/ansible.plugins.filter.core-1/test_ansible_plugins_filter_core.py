# Automatically generated by Pynguin.
import ansible.plugins.filter.core as module_0

def test_case_0():
    pass

def test_case_1():
    list_0 = None
    var_0 = module_0.to_bool(list_0)

def test_case_2():
    str_0 = ''
    var_0 = module_0.to_bool(str_0)

def test_case_3():
    str_0 = 'Mandriva'
    var_0 = module_0.strftime(str_0)

def test_case_4():
    list_0 = []
    var_0 = module_0.quote(list_0)

def test_case_5():
    bytes_0 = b'b\xd5\xe6!'
    var_0 = module_0.fileglob(bytes_0)

def test_case_6():
    bool_0 = False
    var_0 = module_0.regex_replace(bool_0)

def test_case_7():
    list_0 = []
    filter_module_0 = module_0.FilterModule(*list_0)
    str_0 = '\n'
    var_0 = module_0.regex_findall(filter_module_0, str_0)

def test_case_8():
    bytes_0 = b'whfDD).'
    set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
    var_0 = module_0.quote(set_0)
    list_0 = [var_0, bytes_0, var_0]
    filter_module_0 = None
    bytes_1 = b'h\xc7AQx\xce\x96\xc2\xc9\xf8\xbbZ1\xc1+\xe0\xac]\xc9'
    var_1 = module_0.ternary(list_0, filter_module_0, bytes_1)

def test_case_9():
    bool_0 = True
    int_0 = -801
    bytes_0 = None
    list_0 = [int_0, bool_0, bool_0, bytes_0, bytes_0]
    bytes_1 = None
    float_0 = 3711.2772
    var_0 = module_0.ternary(bytes_1, list_0, float_0)

def test_case_10():
    str_0 = '/etc/passwd'
    set_0 = {str_0, str_0, str_0}
    list_0 = [str_0, str_0, set_0]
    var_0 = module_0.regex_escape(list_0)
    var_1 = module_0.fileglob(str_0)

def test_case_11():
    str_0 = "3$'(6Ow&~{^^M,"
    var_0 = module_0.from_yaml(str_0)

def test_case_12():
    tuple_0 = None
    int_0 = 285
    var_0 = module_0.randomize_list(tuple_0, int_0)

def test_case_13():
    dict_0 = {}
    var_0 = module_0.get_hash(dict_0)

def test_case_14():
    str_0 = 'os.%C)~aSF'
    var_0 = module_0.to_uuid(str_0)

def test_case_15():
    float_0 = None
    var_0 = module_0.mandatory(float_0)

def test_case_16():
    var_0 = module_0.combine()

def test_case_17():
    int_0 = 1375
    list_0 = [int_0]
    var_0 = module_0.combine(*list_0)

def test_case_18():
    str_0 = '}\nR+-hAQ 0mn'
    dict_0 = {str_0: str_0}
    var_0 = module_0.comment(str_0, **dict_0)

def test_case_19():
    dict_0 = {}
    var_0 = module_0.b64decode(dict_0)

def test_case_20():
    str_0 = '}5\x0c\rArF7wO6<;'
    var_0 = module_0.flatten(str_0)

def test_case_21():
    filter_module_0 = module_0.FilterModule()
    var_0 = filter_module_0.filters()
    bytes_0 = b'M\x9c\x01\xf0\x8a\xef\xafI\x10'
    str_0 = '< rGVVCG<'
    var_1 = module_0.get_hash(str_0)
    var_2 = module_0.b64encode(bytes_0)

def test_case_22():
    str_0 = '(?P<spam>(.*)) and (?P<eggs>(.*))'
    var_0 = module_0.regex_search(str_0, str_0)

def test_case_23():
    dict_0 = {}
    var_0 = module_0.b64decode(dict_0)
    list_0 = []
    filter_module_0 = module_0.FilterModule(*list_0)
    float_0 = 1093.0433862149646
    str_0 = None
    bool_0 = False
    tuple_0 = (str_0, float_0, bool_0, list_0)
    str_1 = 'PYLH2S\x0cj}'
    str_2 = "'F^f\x0c\\7"
    tuple_1 = (tuple_0, str_1, str_2, dict_0)
    var_1 = module_0.flatten(tuple_1)

def test_case_24():
    int_0 = 3326
    var_0 = module_0.mandatory(int_0)
    dict_0 = {}
    str_0 = 'python'
    var_1 = module_0.subelements(dict_0, str_0)

def test_case_25():
    str_0 = 'test'
    str_1 = 'some'
    var_0 = module_0.regex_replace(str_0, str_0, str_1)
    str_2 = '[a-z]{4}'
    var_1 = module_0.regex_replace(str_0, str_2, str_1)
    str_3 = 'Test'
    var_2 = module_0.regex_replace(str_3, str_2, str_1)
    bool_0 = True
    str_4 = '[A-Z]{4}'
    var_3 = module_0.regex_replace(str_3, str_4, str_1, bool_0)

def test_case_26():
    int_0 = 1
    int_1 = 2
    int_2 = 3
    int_3 = [int_0, int_1, int_2]
    var_0 = module_0.flatten(int_3)
    int_4 = 4
    int_5 = 5
    int_6 = [int_2, int_4, int_5]
    int_7 = [int_0, int_1, int_6]
    var_1 = module_0.flatten(int_7)
    int_8 = [int_5]
    int_9 = [int_2, int_4, int_8]
    int_10 = [int_0, int_1, int_9]
    var_2 = module_0.flatten(int_10)
    int_11 = [int_5]
    int_12 = [int_2, int_4, int_11]
    int_13 = [int_0, int_1, int_12]
    var_3 = module_0.flatten(int_13, int_1)
    int_14 = [int_5]
    int_15 = [int_2, int_4, int_14]
    int_16 = [int_0, int_1, int_15]
    var_4 = module_0.flatten(int_16, int_0)
    int_17 = [int_5]
    int_18 = [int_2, int_4, int_17]
    int_19 = [int_0, int_1, int_18]
    int_20 = 0
    var_5 = module_0.flatten(int_19, int_20)

def test_case_27():
    str_0 = '/etc/passwd'
    var_0 = module_0.fileglob(str_0)

def test_case_28():
    str_0 = '/tmp/'
    var_0 = module_0.fileglob(str_0)

def test_case_29():
    str_0 = 'test'
    var_0 = module_0.comment(str_0)
    str_1 = 'xml'
    var_1 = module_0.comment(str_0, str_1)
    str_2 = 'cblock'
    var_2 = module_0.comment(str_0, str_2)
    str_3 = '\r\n'
    var_3 = module_0.comment(str_0)
    var_4 = module_0.comment(str_0, str_1)
    var_5 = module_0.comment(str_0, str_2)
    str_4 = '; '
    var_6 = module_0.comment(str_0)