# Automatically generated by Pynguin.
import cookiecutter.prompt as module_0
import collections as module_1

def test_case_0():
    try:
        int_0 = -809
        str_0 = 'ask'
        var_0 = module_0.read_user_variable(int_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 766
        str_0 = '45<H Qu.g>C&'
        var_0 = module_0.read_user_yes_no(int_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'V)K\x0cLMo3\t'
        var_0 = module_0.read_repo_password(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        list_0 = []
        var_0 = module_0.read_user_choice(list_0, list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 1148
        var_0 = module_0.read_user_choice(int_0, int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = False
        var_0 = module_0.process_json(bool_0)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = 81
        var_0 = module_0.read_user_dict(int_0, int_0)
    except BaseException:
        pass

def test_case_7():
    try:
        set_0 = set()
        float_0 = -889.89
        bytes_0 = b'v\xf8e\xd2\x0e\\=\xcf\xb4\xfe\xa9f\xb8'
        var_0 = module_0.render_variable(set_0, float_0, bytes_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'EM"XP?/5'
        set_0 = {str_0, str_0, str_0}
        bytes_0 = None
        tuple_0 = (bytes_0, bytes_0, str_0)
        str_1 = 'ipry;97p\t5'
        var_0 = module_0.prompt_choice_for_config(set_0, set_0, tuple_0, tuple_0, str_1)
    except BaseException:
        pass

def test_case_9():
    try:
        ordered_dict_0 = module_1.OrderedDict()
        bytes_0 = b'U\x8e\x96'
        list_0 = [ordered_dict_0, ordered_dict_0]
        var_0 = module_0.render_variable(bytes_0, list_0, list_0)
        var_1 = module_0.process_json(ordered_dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        int_0 = None
        bytes_0 = b'\xcdx-\xb5\xc7\x86\x15h\x9c>\xda\xbaL'
        dict_0 = {int_0: bytes_0}
        int_1 = -1683
        var_0 = module_0.render_variable(bytes_0, dict_0, int_1)
    except BaseException:
        pass

def test_case_11():
    try:
        tuple_0 = None
        str_0 = 'WARNING'
        list_0 = [tuple_0, str_0, tuple_0]
        var_0 = module_0.prompt_for_config(list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = ''
        dict_0 = {str_0: str_0, str_0: str_0}
        list_0 = [str_0, dict_0, str_0, dict_0]
        var_0 = module_0.read_user_choice(dict_0, list_0)
    except BaseException:
        pass

def test_case_13():
    try:
        dict_0 = {}
        var_0 = module_0.read_user_dict(dict_0, dict_0)
    except BaseException:
        pass

def test_case_14():
    try:
        int_0 = 1
        list_0 = [int_0, int_0, int_0]
        tuple_0 = (list_0,)
        set_0 = set()
        bool_0 = False
        var_0 = module_0.prompt_choice_for_config(int_0, tuple_0, list_0, set_0, bool_0)
    except BaseException:
        pass

def test_case_15():
    try:
        bool_0 = False
        bool_1 = False
        str_0 = '<{Z'
        list_0 = []
        bytes_0 = b'fL\xa3q\xe0#\xe7^\xf7\\\x87\x13'
        var_0 = module_0.prompt_choice_for_config(bool_0, bool_1, str_0, list_0, bytes_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '["invalid json dict"]'
        var_0 = module_0.process_json(str_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '{"sample": "valid json"}'
        var_0 = module_0.process_json(str_0)
        float_0 = 277.65
        var_1 = module_0.process_json(float_0)
    except BaseException:
        pass