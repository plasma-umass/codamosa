# Automatically generated by Pynguin.
import ansible.plugins.lookup.together as module_0

def test_case_0():
    try:
        lookup_module_0 = module_0.LookupModule()
        var_0 = []
        var_1 = lookup_module_0.run(var_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'b,u'
        int_0 = 1000
        tuple_0 = (str_0, int_0)
        dict_0 = {str_0: str_0}
        lookup_module_0 = module_0.LookupModule()
        var_0 = lookup_module_0.run(tuple_0, **dict_0)
    except BaseException:
        pass