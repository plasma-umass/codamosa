# Automatically generated by Pynguin.
import ansible.vars.plugins as module_0
import ansible.inventory.host as module_1

def test_case_0():
    try:
        var_0 = None
        var_1 = module_0.get_vars_from_path(var_0, var_0, var_0, var_0)
    except BaseException:
        pass

def test_case_1():
    try:
        set_0 = set()
        int_0 = 437
        var_0 = module_0.get_plugin_vars(set_0, set_0, int_0, int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        set_0 = None
        int_0 = 929
        str_0 = '\x0b.Bxb/Q*>EBJg_cOn+5\r'
        var_0 = module_0.get_plugin_vars(set_0, int_0, int_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'x7(\xdaG\x146\xd1\xf5\xac'
        list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
        str_0 = 'a'
        var_0 = module_0.get_vars_from_inventory_sources(list_0, str_0, list_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        set_0 = None
        str_0 = ',a'
        dict_0 = {}
        float_0 = 18.34828
        tuple_0 = (float_0, str_0, set_0, str_0)
        bytes_0 = b'\x9f\xe0@4\xd9\xf7'
        set_1 = set()
        var_0 = module_0.get_plugin_vars(dict_0, tuple_0, bytes_0, set_1)
        var_1 = module_0.get_vars_from_inventory_sources(bytes_0, str_0, set_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'x7(\xdaG\x146\xd1\xf5\xac'
        list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
        str_0 = '.Ue+c8y'
        var_0 = module_0.get_vars_from_inventory_sources(str_0, str_0, list_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'B'
        host_0 = module_1.Host()
        str_1 = 'TnP'
        list_0 = [host_0, str_0]
        int_0 = 69
        var_0 = module_0.get_vars_from_path(int_0, str_1, list_0, int_0)
    except BaseException:
        pass

def test_case_7():
    try:
        list_0 = None
        int_0 = -1287
        bool_0 = None
        dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: list_0, bool_0: bool_0}
        str_0 = "vm)'}\x0cLB29M|tE"
        str_1 = 'b9e)r(xpP'
        str_2 = 'Q/R'
        bytes_0 = b'\xb4_P\x12'
        tuple_0 = (bytes_0, list_0)
        var_0 = module_0.get_vars_from_inventory_sources(str_2, dict_0, tuple_0, int_0)
        var_1 = module_0.get_vars_from_inventory_sources(bool_0, dict_0, str_0, str_1)
        host_0 = module_1.Host(list_0, int_0)
        host_1 = module_1.Host(host_0, list_0)
        str_3 = '!`{F3Mv}%w\ryV5\x0bL9@Z'
        var_2 = module_0.get_vars_from_inventory_sources(str_3, bool_0, list_0, bool_0)
    except BaseException:
        pass