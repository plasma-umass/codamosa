# Automatically generated by Pynguin.
import ansible.utils.color as module_0

def test_case_0():
    try:
        str_0 = 'A\n(#'
        var_0 = module_0.parsecolor(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = None
        var_0 = module_0.parsecolor(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = ';k k9mwM}^'
        bool_0 = False
        set_0 = {str_0, bool_0}
        tuple_0 = None
        var_0 = module_0.stringc(set_0, tuple_0)
        float_0 = -2764.86453
        var_1 = module_0.colorize(str_0, bool_0, float_0)
        str_1 = '%Tx)Q?&jN'
        set_1 = {str_1, str_1}
        var_2 = module_0.parsecolor(set_1)
    except BaseException:
        pass