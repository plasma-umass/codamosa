# Automatically generated by Pynguin.
import ansible.plugins.lookup.ini as module_0

def test_case_0():
    try:
        lookup_module_0 = module_0.LookupModule()
        list_0 = None
        float_0 = None
        var_0 = lookup_module_0.get_value(lookup_module_0, list_0, lookup_module_0, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        lookup_module_0 = None
        str_0 = 'ZmkX'
        bytes_0 = b'\xe1"5\x9f\xe1\x0c\xb2\xd4;D'
        set_0 = {bytes_0, lookup_module_0}
        lookup_module_1 = module_0.LookupModule()
        var_0 = lookup_module_1.get_value(lookup_module_0, str_0, lookup_module_0, set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        list_0 = []
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(list_0)
    except BaseException:
        pass