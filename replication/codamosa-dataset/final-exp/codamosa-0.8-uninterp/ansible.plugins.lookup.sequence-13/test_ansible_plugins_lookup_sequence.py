# Automatically generated by Pynguin.
import ansible.plugins.lookup.sequence as module_0

def test_case_0():
    lookup_module_0 = module_0.LookupModule()

def test_case_1():
    lookup_module_0 = module_0.LookupModule()
    str_0 = 'start'
    str_1 = 'end'
    str_2 = 'stride'
    str_3 = 'format'
    str_4 = '0'
    str_5 = '10'
    str_6 = '2'
    str_7 = '%s'
    str_8 = {str_0: str_4, str_1: str_5, str_2: str_6, str_3: str_7}
    var_0 = lookup_module_0.parse_kv_args(str_8)

def test_case_2():
    lookup_module_0 = module_0.LookupModule()
    var_0 = lookup_module_0.reset()
    str_0 = '4'
    var_1 = lookup_module_0.parse_simple_args(str_0)
    str_1 = '4-12/2'
    var_2 = lookup_module_0.parse_simple_args(str_1)

def test_case_3():
    lookup_module_0 = module_0.LookupModule()
    var_0 = lookup_module_0.reset()
    str_0 = '4:testuser%02x'
    var_1 = lookup_module_0.parse_simple_args(str_0)
    str_1 = '4-12/2'
    var_2 = lookup_module_0.parse_simple_args(str_1)