# Automatically generated by Pynguin.
import pypara.dcc as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = ':1'
    d_c_c_registry_machinery_0 = module_0.DCCRegistryMachinery()
    list_0 = [str_0, str_0, str_0, d_c_c_registry_machinery_0]
    d_c_c_0 = module_0.DCC(*list_0)
    d_c_c_registry_machinery_0.register(d_c_c_0)
    optional_0 = d_c_c_registry_machinery_0.find(str_0)