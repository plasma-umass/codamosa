# Automatically generated by Pynguin.
import httpie.output.formatters.json as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'format_options'
    str_1 = 'explicit_json'
    str_2 = 'json'
    str_3 = 'colors'
    str_4 = 'format'
    str_5 = 'indent'
    bool_0 = True
    int_0 = 4
    var_0 = {str_4: bool_0, str_3: bool_0, str_5: int_0}
    bool_1 = False
    var_1 = {str_2: var_0, str_3: bool_1}
    var_2 = {str_0: var_1, str_1: bool_0}
    j_s_o_n_formatter_0 = module_0.JSONFormatter(**var_2)
    str_6 = 'application/json'
    str_7 = j_s_o_n_formatter_0.format_body(str_5, str_6)
    str_8 = 'b~!hXSqnI:=0'
    str_9 = j_s_o_n_formatter_0.format_body(str_8, str_2)

def test_case_2():
    str_0 = 'format_options'
    str_1 = 'explicit_json'
    str_2 = 'json'
    str_3 = 'colors'
    str_4 = 'format'
    str_5 = 'sort_keys'
    str_6 = 'indent'
    bool_0 = True
    int_0 = 4
    var_0 = {str_4: bool_0, str_5: bool_0, str_6: int_0}
    bool_1 = False
    var_1 = {str_2: var_0, str_3: bool_1}
    var_2 = {str_0: var_1, str_1: bool_0}
    j_s_o_n_formatter_0 = module_0.JSONFormatter(**var_2)
    str_7 = '{"foo":"bar"}'
    str_8 = 'application/json'
    str_9 = j_s_o_n_formatter_0.format_body(str_7, str_8)
    str_10 = '{}'
    str_11 = j_s_o_n_formatter_0.format_body(str_10, str_8)
    str_12 = j_s_o_n_formatter_0.format_body(str_11, str_6)