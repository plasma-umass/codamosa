# Automatically generated by Pynguin.
import ansible.module_utils.common.text.formatters as module_0

def test_case_0():
    try:
        bool_0 = False
        var_0 = module_0.lenient_lowercase(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        set_0 = set()
        var_0 = module_0.human_to_bytes(set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '1dU\nX3'
        var_0 = module_0.bytes_to_human(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 2533
        var_0 = module_0.bytes_to_human(int_0)
        dict_0 = {int_0: var_0}
        var_1 = module_0.lenient_lowercase(dict_0)
        str_0 = '4c'
        str_1 = '1KB'
        var_2 = module_0.human_to_bytes(str_1)
        var_3 = module_0.human_to_bytes(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '4c'
        var_0 = module_0.human_to_bytes(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 2709
        bytes_0 = b'\x12~\xc4\x8eW\x10\x19\x98\x12~`\xc8\xeag\xf1\x04:'
        list_0 = [int_0]
        str_0 = 'f!S\x0cK<^o++j'
        var_0 = module_0.bytes_to_human(bytes_0, list_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '10MB'
        var_0 = module_0.human_to_bytes(str_0)
        str_1 = '10m'
        var_1 = module_0.human_to_bytes(str_1)
        str_2 = '10mb'
        var_2 = module_0.human_to_bytes(str_2)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '8'
        tuple_0 = (str_0,)
        var_0 = module_0.lenient_lowercase(tuple_0)
        str_1 = '1KB'
        var_1 = module_0.human_to_bytes(str_1)
        set_0 = {str_1}
        bytes_0 = b'\xef\xf8\x1c'
        var_2 = module_0.human_to_bytes(str_1, set_0, bytes_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '8'
        int_0 = 2531
        var_0 = module_0.bytes_to_human(int_0)
        dict_0 = {int_0: var_0}
        var_1 = module_0.lenient_lowercase(dict_0)
        tuple_0 = (str_0,)
        var_2 = module_0.lenient_lowercase(tuple_0)
        str_1 = '1bS'
        var_3 = module_0.human_to_bytes(str_1)
    except BaseException:
        pass