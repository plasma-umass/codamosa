# Automatically generated by Pynguin.
import ansible.plugins.inventory.constructed as module_0

def test_case_0():
    try:
        set_0 = set()
        str_0 = 'async_watchdog'
        int_0 = 999
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.get_all_host_vars(set_0, str_0, int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 2483.97773
        dict_0 = {float_0: float_0}
        list_0 = [float_0, float_0, float_0, float_0]
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.host_vars(float_0, dict_0, list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '(CQ4`8(0h'
        inventory_module_0 = module_0.InventoryModule()
        bytes_0 = b''
        inventory_module_1 = module_0.InventoryModule()
        var_0 = inventory_module_1.parse(str_0, inventory_module_0, bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        inventory_module_0 = module_0.InventoryModule()
        bytes_0 = b'\\\xddU\xe0\xd5\xfb\x0c\xe5}\xa9'
        tuple_0 = ()
        var_0 = inventory_module_0.parse(bytes_0, tuple_0, bytes_0)
    except BaseException:
        pass