# Automatically generated by Pynguin.
import ansible.plugins.inventory.auto as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'hYTN#\\/wV/'
    inventory_module_0 = module_0.InventoryModule()
    var_0 = inventory_module_0.verify_file(str_0)

def test_case_2():
    inventory_module_0 = module_0.InventoryModule()
    str_0 = 'test.yml'
    var_0 = inventory_module_0.verify_file(str_0)
    str_1 = 'test'
    var_1 = inventory_module_0.verify_file(str_1)

def test_case_3():
    inventory_module_0 = module_0.InventoryModule()
    str_0 = 'test.yaml'
    var_0 = inventory_module_0.verify_file(str_0)
    str_1 = 'test'
    var_1 = inventory_module_0.verify_file(str_1)