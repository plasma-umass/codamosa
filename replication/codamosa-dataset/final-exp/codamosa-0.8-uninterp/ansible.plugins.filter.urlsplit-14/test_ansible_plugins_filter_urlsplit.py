# Automatically generated by Pynguin.
import ansible.plugins.filter.urlsplit as module_0

def test_case_0():
    filter_module_0 = module_0.FilterModule()

def test_case_1():
    str_0 = 'https://www.example.com:443/foo?bar=baz#quux'
    str_1 = 'port'
    var_0 = module_0.split_url(str_0, str_1)
    var_1 = module_0.split_url(str_0)

def test_case_2():
    filter_module_0 = module_0.FilterModule()
    var_0 = filter_module_0.filters()