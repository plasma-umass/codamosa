# Automatically generated by Pynguin.
import ansible.module_utils.common.dict_transformations as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'sim`leTet'
    str_1 = {str_0: str_0, str_0: str_0, str_0: str_0}
    str_2 = {str_0: str_1}
    var_0 = module_0.camel_dict_to_snake_dict(str_2)

def test_case_2():
    str_0 = '=^}b3fLb`T]vG}f]*AY\\'
    var_0 = module_0.snake_dict_to_camel_dict(str_0)

def test_case_3():
    dict_0 = {}
    var_0 = module_0.snake_dict_to_camel_dict(dict_0)

def test_case_4():
    str_0 = '8+D$'
    str_1 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    str_2 = {str_0: str_1, str_0: str_1}
    float_0 = 232.4114
    str_3 = '1:\tg6sz~QoNzPT'
    var_0 = module_0.dict_merge(float_0, str_3)
    str_4 = None
    list_0 = [str_4]
    var_1 = module_0.snake_dict_to_camel_dict(list_0)
    str_5 = 'FeW X0%_'
    var_2 = module_0.camel_dict_to_snake_dict(str_2, str_4, str_5)

def test_case_5():
    bool_0 = None
    str_0 = '_silent'
    var_0 = module_0.snake_dict_to_camel_dict(bool_0, str_0)

def test_case_6():
    str_0 = '`$l(Yx8|g\rgH?P'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    str_1 = 'r}/h-<-O'
    var_0 = module_0.snake_dict_to_camel_dict(dict_0)
    var_1 = module_0.snake_dict_to_camel_dict(dict_0, str_1)

def test_case_7():
    str_0 = 'Connection plugin does noE allow the connection timeout to be overridden'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    bytes_0 = b'\xeb}xU\xbcy\xb3\xbb\x9c\x88.'
    var_0 = module_0.camel_dict_to_snake_dict(dict_0, bytes_0, str_0)

def test_case_8():
    bytes_0 = b'\x86\xcc)Z\xb8\x1d\xe03P*y?\xf6}\xa6T'
    int_0 = 771
    var_0 = module_0.dict_merge(bytes_0, int_0)

def test_case_9():
    str_0 = 'Connection plugin does not allow the connection timeout to be overridden'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.recursive_diff(dict_0, dict_0)

def test_case_10():
    str_0 = 'value'
    str_1 = 'value2'
    str_2 = 'another_one'
    str_3 = {str_0: str_0, str_2: str_1}
    str_4 = 'outerKey'
    str_5 = {str_4: str_0}
    str_6 = {str_4: str_5}
    var_0 = module_0.camel_dict_to_snake_dict(str_6)
    var_1 = module_0.snake_dict_to_camel_dict(str_3)

def test_case_11():
    str_0 = ';U'
    str_1 = {str_0: str_0}
    str_2 = {str_0: str_1}
    set_0 = set()
    list_0 = [str_0, str_2, str_1, set_0]
    dict_0 = {}
    var_0 = module_0.dict_merge(list_0, dict_0)
    var_1 = module_0.camel_dict_to_snake_dict(str_2)

def test_case_12():
    str_0 = 'a'
    str_1 = 'b'
    str_2 = 'x'
    int_0 = 1
    int_1 = {str_2: int_0}
    int_2 = 2
    int_3 = {str_0: int_1, str_1: int_2}
    str_3 = 'y'
    int_4 = 3
    int_5 = {str_3: int_4}
    str_4 = 'c'
    int_6 = 4
    int_7 = {str_4: int_6}
    int_8 = {str_0: int_5, str_1: int_7}
    var_0 = module_0.dict_merge(int_3, int_8)

def test_case_13():
    int_0 = 1
    str_0 = 'b'
    int_1 = {str_0: int_0}
    int_2 = 2
    int_3 = {str_0: int_2}
    var_0 = module_0.recursive_diff(int_1, int_3)
    int_4 = {str_0: int_0}
    int_5 = {str_0: int_4}
    int_6 = {str_0: int_2}
    int_7 = {str_0: int_6}
    var_1 = module_0.recursive_diff(int_5, int_7)

def test_case_14():
    var_0 = {}
    var_1 = {}
    var_2 = module_0.recursive_diff(var_0, var_1)
    str_0 = 'a'
    int_0 = 1
    int_1 = {str_0: int_0}
    int_2 = {str_0: int_0}
    var_3 = module_0.recursive_diff(int_1, int_2)
    str_1 = 'b'
    int_3 = {str_1: int_0}
    int_4 = {str_0: int_3}
    int_5 = {str_0: int_1}
    var_4 = module_0.recursive_diff(int_4, int_5)

def test_case_15():
    var_0 = {}
    var_1 = {}
    var_2 = module_0.recursive_diff(var_0, var_1)
    str_0 = 'a'
    int_0 = 1
    int_1 = {str_0: int_0}
    int_2 = {str_0: int_0}
    var_3 = module_0.recursive_diff(int_1, int_2)
    int_3 = {str_0: int_0}
    str_1 = 'b'
    int_4 = {str_1: int_0}
    var_4 = module_0.recursive_diff(int_3, int_4)
    int_5 = {str_0: int_0}
    int_6 = 2
    int_7 = {str_0: int_6}
    var_5 = module_0.recursive_diff(int_5, int_7)
    int_8 = {str_1: int_0}
    int_9 = {str_0: int_8}
    var_6 = module_0.recursive_diff(int_9, int_7)

def test_case_16():
    var_0 = {}
    var_1 = {}
    var_2 = module_0.recursive_diff(var_0, var_1)
    int_0 = 1
    str_0 = 'b'
    int_1 = {str_0: int_0}
    int_2 = 1
    int_3 = {str_0: int_2}
    var_3 = module_0.recursive_diff(int_1, int_3)
    int_4 = {str_0: int_0}
    int_5 = {str_0: int_4}
    int_6 = {str_0: int_2}
    int_7 = {str_0: int_6}
    var_4 = module_0.recursive_diff(int_5, int_7)

def test_case_17():
    var_0 = {}
    var_1 = {}
    var_2 = module_0.recursive_diff(var_0, var_1)
    str_0 = 'a'
    int_0 = 1
    int_1 = {str_0: int_0}
    int_2 = {str_0: int_0}
    var_3 = module_0.recursive_diff(int_1, int_2)
    int_3 = {str_0: int_0}
    var_4 = module_0.recursive_diff(int_2, int_3)
    int_4 = {str_0: int_0}
    int_5 = 2
    var_5 = module_0.recursive_diff(int_4, int_4)
    int_6 = {}
    int_7 = {str_0: int_5}
    int_8 = {str_0: int_7}
    var_6 = module_0.recursive_diff(int_6, int_8)

def test_case_18():
    str_0 = 'simpleTest'
    str_1 = 'value'
    str_2 = 'vale2'
    str_3 = {str_0: str_1, str_0: str_2}
    str_4 = 'aterm_'
    str_5 = {str_1: str_1, str_4: str_2}
    var_0 = module_0.camel_dict_to_snake_dict(str_3)
    str_6 = 'outerKey'
    str_7 = {str_1: str_1}
    str_8 = {str_6: str_7}
    var_1 = module_0.camel_dict_to_snake_dict(str_8)
    var_2 = module_0.snake_dict_to_camel_dict(str_5)

def test_case_19():
    str_0 = '_uM7H ;u.\\^PN\nZ7F\rL$'
    str_1 = {str_0: str_0, str_0: str_0}
    str_2 = {str_0: str_1, str_0: str_1}
    var_0 = module_0.camel_dict_to_snake_dict(str_2)

def test_case_20():
    str_0 = '8+D$'
    str_1 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    str_2 = {str_0: str_1, str_0: str_1}
    var_0 = module_0.camel_dict_to_snake_dict(str_2, str_1, str_2)