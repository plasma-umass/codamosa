# Automatically generated by Pynguin.
import ansible.vars.plugins as module_0
import ansible.inventory.host as module_1

def test_case_0():
    try:
        str_0 = 'inven1o%1'
        var_0 = module_0.get_vars_from_path(str_0, str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xd1\x03C\xbd?^\xf3\xce'
        str_0 = '1Bp'
        var_0 = module_0.get_plugin_vars(bytes_0, str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 1169.0
        set_0 = {float_0}
        str_0 = ',_ZW2ZikJo9sNISj&'
        var_0 = module_0.get_vars_from_inventory_sources(set_0, str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = None
        float_0 = 2829.77293
        float_1 = None
        var_0 = module_0.get_plugin_vars(dict_0, float_0, float_0, float_1)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = None
        float_0 = -1525.9529
        list_0 = [bool_0, float_0]
        dict_0 = {}
        var_0 = module_0.get_vars_from_inventory_sources(bool_0, list_0, bool_0, dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = 1169.0
        set_0 = {float_0}
        str_0 = '.a5\r|oXL4'
        str_1 = 'itrm'
        bytes_0 = b"Q\xe7/s\xb5Dq\xdck\xebg\xcb'\x92!"
        str_2 = ''
        var_0 = module_0.get_plugin_vars(bytes_0, set_0, set_0, str_2)
        var_1 = module_0.get_vars_from_inventory_sources(set_0, str_0, str_0, str_1)
    except BaseException:
        pass

def test_case_6():
    try:
        float_0 = None
        host_0 = module_1.Host()
        var_0 = host_0.__str__()
        bytes_0 = None
        tuple_0 = None
        host_1 = module_1.Host(tuple_0)
        list_0 = [host_1, float_0, tuple_0, tuple_0]
        var_1 = module_0.get_vars_from_path(host_0, bytes_0, list_0, tuple_0)
    except BaseException:
        pass