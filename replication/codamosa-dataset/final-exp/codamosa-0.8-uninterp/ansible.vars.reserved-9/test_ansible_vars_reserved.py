# Automatically generated by Pynguin.
import ansible.vars.reserved as module_0

def test_case_0():
    var_0 = module_0.get_reserved_names()

def test_case_1():
    bool_0 = True
    set_0 = {bool_0}
    var_0 = module_0.get_reserved_names()
    bool_1 = False
    var_1 = module_0.is_reserved_name(bool_1)
    var_2 = module_0.is_reserved_name(set_0)
    str_0 = 'x+_]}]wKtU{{O,C5Ex8'
    var_3 = module_0.warn_if_reserved(str_0)
    float_0 = 2.0
    var_4 = module_0.is_reserved_name(float_0)