# Automatically generated by Pynguin.
import ansible.parsing.utils.addresses as module_0

def test_case_0():
    str_0 = '1'
    var_0 = module_0.parse_address(str_0)

def test_case_1():
    str_0 = 'example.com'
    var_0 = module_0.parse_address(str_0)
    str_1 = 'example.com:22'
    var_1 = module_0.parse_address(str_1)
    str_2 = '[example.com]:22'
    var_2 = module_0.parse_address(str_2)
    str_3 = '85.14.0.168'
    var_3 = module_0.parse_address(str_3)
    str_4 = '85.14.0.168:22'
    var_4 = module_0.parse_address(str_4)
    bool_0 = True
    var_5 = module_0.parse_address(str_4, bool_0)
    bool_1 = False
    var_6 = module_0.parse_address(str_4, bool_1)

def test_case_2():
    str_0 = '2001:db8::1'
    var_0 = module_0.parse_address(str_0)
    str_1 = '[2001:db8::1]:80'
    var_1 = module_0.parse_address(str_1)
    var_2 = module_0.parse_address(str_0)
    var_3 = module_0.parse_address(str_1)