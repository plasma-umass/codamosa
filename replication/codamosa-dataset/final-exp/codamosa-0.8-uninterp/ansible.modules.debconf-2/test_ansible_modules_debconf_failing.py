# Automatically generated by Pynguin.
import ansible.modules.debconf as module_0

def test_case_0():
    try:
        str_0 = 'Z0LqXs?'
        bool_0 = None
        var_0 = module_0.get_selections(str_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = None
        bool_0 = False
        bool_1 = None
        str_0 = '~'
        float_0 = 131.812717
        set_0 = {bool_1, float_0, int_0}
        var_0 = module_0.set_selection(int_0, bool_0, bool_1, int_0, str_0, set_0)
    except BaseException:
        pass