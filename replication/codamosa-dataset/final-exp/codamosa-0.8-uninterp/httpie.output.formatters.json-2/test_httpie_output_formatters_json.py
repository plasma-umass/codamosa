# Automatically generated by Pynguin.
import httpie.output.formatters.json as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'explicit_json'
    str_1 = 'format_options'
    bool_0 = True
    str_2 = 'json'
    str_3 = 'format'
    str_4 = 'indent'
    str_5 = 'sort_keys'
    int_0 = 4
    var_0 = {str_3: bool_0, str_4: int_0, str_5: bool_0}
    var_1 = {str_2: var_0}
    var_2 = {str_0: bool_0, str_1: var_1}
    j_s_o_n_formatter_0 = module_0.JSONFormatter(**var_2)
    str_6 = j_s_o_n_formatter_0.format_body(str_2, str_4)

def test_case_2():
    str_0 = 'explicit_json'
    str_1 = 'format_options'
    bool_0 = False
    str_2 = 'json'
    str_3 = 'format'
    str_4 = 'indent'
    str_5 = 'sort_keys'
    int_0 = 4
    var_0 = {str_3: bool_0, str_4: int_0, str_5: bool_0}
    var_1 = {str_2: var_0}
    var_2 = {str_0: bool_0, str_1: var_1}
    j_s_o_n_formatter_0 = module_0.JSONFormatter(**var_2)
    str_6 = j_s_o_n_formatter_0.format_body(str_2, str_4)
    str_7 = '4mwm"'
    str_8 = j_s_o_n_formatter_0.format_body(str_7, str_7)

def test_case_3():
    str_0 = 'explicit_json'
    str_1 = 'format_options'
    bool_0 = False
    str_2 = 'json'
    str_3 = 'format'
    str_4 = 'K'
    str_5 = 'sort_k/ysA]'
    int_0 = 4
    var_0 = {str_3: bool_0, str_4: int_0, str_5: bool_0}
    var_1 = {str_2: var_0}
    var_2 = {str_0: bool_0, str_1: var_1}
    j_s_o_n_formatter_0 = module_0.JSONFormatter(**var_2)
    str_6 = '3qT'
    str_7 = j_s_o_n_formatter_0.format_body(str_2, str_6)
    str_8 = ''
    str_9 = 'Q}pNdj,TP#G0.blX_I['
    str_10 = j_s_o_n_formatter_0.format_body(str_8, str_9)
    str_11 = 'ngw\x0bBS:|8'
    str_12 = j_s_o_n_formatter_0.format_body(str_11, str_2)

def test_case_4():
    str_0 = 'json'
    str_1 = 'explicit_json'
    str_2 = 'format_options'
    bool_0 = False
    bool_1 = True
    str_3 = 'format'
    str_4 = 'indent'
    str_5 = 'sort_keys'
    int_0 = 2
    var_0 = {str_3: bool_1, str_4: int_0, str_5: bool_0}
    var_1 = {str_0: var_0}
    var_2 = {str_0: bool_0, str_1: bool_1, str_2: var_1}
    j_s_o_n_formatter_0 = module_0.JSONFormatter(**var_2)
    str_6 = '\n{\n    "a": [\n        1,\n        2\n    ],\n    "b": 3.14\n}\n    '
    str_7 = 'application/json'
    str_8 = j_s_o_n_formatter_0.format_body(str_6, str_7)