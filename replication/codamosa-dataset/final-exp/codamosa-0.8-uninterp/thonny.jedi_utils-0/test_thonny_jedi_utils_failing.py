# Automatically generated by Pynguin.
import thonny.jedi_utils as module_0

def test_case_0():
    try:
        dict_0 = {}
        list_0 = [dict_0]
        var_0 = module_0.get_statement_of_position(dict_0, list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        thonny_completion_0 = None
        set_0 = {thonny_completion_0}
        var_0 = module_0.parse_source(set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '\x0bsK\'?JJy\tcg(h6*\x0bx@"'
        int_0 = -1660
        var_0 = module_0.get_script_completions(str_0, int_0, int_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = None
        list_0 = []
        var_0 = module_0.get_interpreter_completions(str_0, list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '+i$8'
        int_0 = -265
        var_0 = module_0.get_script_completions(str_0, int_0, int_0, str_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'z-uLd[\x0bihZ-\x0bxy5gT'
        int_0 = 1562
        var_0 = module_0.get_definitions(str_0, int_0, int_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        float_0 = 1378.37
        str_0 = 'F$Mv'
        str_1 = 'Y2IJpTI@N'
        int_0 = 1019
        set_0 = set()
        tuple_0 = (int_0, set_0)
        thonny_completion_0 = module_0.ThonnyCompletion(str_0, str_1, str_1, int_0, tuple_0, set_0)
        var_0 = thonny_completion_0.__getitem__(float_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'open('
        dict_0 = {}
        list_0 = [dict_0, dict_0, dict_0, dict_0]
        bool_0 = False
        var_0 = module_0.get_interpreter_completions(str_0, list_0, bool_0)
        str_1 = 'spacing1'
        int_0 = 100
        var_1 = module_0.get_script_completions(str_1, int_0, int_0, str_0)
    except BaseException:
        pass