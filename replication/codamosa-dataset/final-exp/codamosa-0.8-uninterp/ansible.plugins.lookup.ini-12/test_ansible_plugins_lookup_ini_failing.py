# Automatically generated by Pynguin.
import ansible.plugins.lookup.ini as module_0

def test_case_0():
    try:
        bool_0 = False
        str_0 = 'default'
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.get_value(str_0, str_0, str_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'w]g_HalCd'
        int_0 = -2936
        float_0 = -2350.58
        dict_0 = {float_0: str_0}
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.get_value(str_0, int_0, float_0, dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'Manage an Ansible Galaxy role.'
        float_0 = 0.2
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(str_0, float_0)
    except BaseException:
        pass