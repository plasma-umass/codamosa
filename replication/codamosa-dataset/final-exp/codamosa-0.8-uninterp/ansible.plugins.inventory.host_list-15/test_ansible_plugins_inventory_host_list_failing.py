# Automatically generated by Pynguin.
import ansible.plugins.inventory.host_list as module_0

def test_case_0():
    try:
        bool_0 = False
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.verify_file(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        inventory_module_0 = module_0.InventoryModule()
        int_0 = None
        var_0 = inventory_module_0.parse(int_0, int_0, inventory_module_0)
    except BaseException:
        pass

def test_case_2():
    try:
        inventory_module_0 = module_0.InventoryModule()
        var_0 = None
        str_0 = '10.10.2.6, 10.10.2.4, 10.10.2.3'
        var_1 = inventory_module_0.parse(var_0, var_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        inventory_module_0 = module_0.InventoryModule()
        var_0 = None
        str_0 = "@gc8f_gy#4'YDU5"
        var_1 = inventory_module_0.parse(var_0, var_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        inventory_module_0 = module_0.InventoryModule()
        var_0 = None
        str_0 = ',mLPny]@bzYt9'
        var_1 = inventory_module_0.parse(var_0, var_0, str_0)
    except BaseException:
        pass