# Automatically generated by Pynguin.
import ansible.plugins.inventory.generator as module_0

def test_case_0():
    pass

def test_case_1():
    inventory_module_0 = module_0.InventoryModule()

def test_case_2():
    float_0 = 1.0
    inventory_module_0 = module_0.InventoryModule()
    var_0 = inventory_module_0.verify_file(float_0)

def test_case_3():
    tuple_0 = ()
    inventory_module_0 = module_0.InventoryModule()
    bool_0 = True
    inventory_module_1 = module_0.InventoryModule()
    var_0 = inventory_module_1.add_parents(tuple_0, inventory_module_0, tuple_0, bool_0)
    float_0 = 1.0
    inventory_module_2 = module_0.InventoryModule()
    var_1 = inventory_module_2.verify_file(float_0)

def test_case_4():
    inventory_module_0 = module_0.InventoryModule()
    str_0 = '/'
    var_0 = inventory_module_0.verify_file(str_0)