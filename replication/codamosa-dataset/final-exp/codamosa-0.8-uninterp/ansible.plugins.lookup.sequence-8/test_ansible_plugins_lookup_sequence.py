# Automatically generated by Pynguin.
import ansible.plugins.lookup.sequence as module_0
import ansible.parsing.splitter as module_1

def test_case_0():
    pass

def test_case_1():
    dict_0 = {}
    lookup_module_0 = module_0.LookupModule()
    var_0 = lookup_module_0.parse_kv_args(dict_0)

def test_case_2():
    lookup_module_0 = module_0.LookupModule()
    str_0 = '1'
    str_1 = '2'
    str_2 = '%d'
    var_0 = dict(start=str_0, end=str_1, format=str_2)
    var_1 = lookup_module_0.parse_kv_args(var_0)
    str_3 = '0x10'
    str_4 = '0x12'
    var_2 = dict(start=str_3, end=str_4, format=str_2)
    var_3 = lookup_module_0.parse_kv_args(var_2)
    var_4 = dict(start=str_3, end=str_1, format=str_2)

def test_case_3():
    lookup_module_0 = module_0.LookupModule()
    var_0 = lookup_module_0.reset()
    str_0 = 'start=10 end=0 stride=-1'
    var_1 = module_1.parse_kv(str_0)
    var_2 = lookup_module_0.parse_kv_args(var_1)
    var_3 = lookup_module_0.sanity_check()