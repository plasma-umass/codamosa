# Automatically generated by Pynguin.
import ansible.plugins.inventory.host_list as module_0

def test_case_0():
    inventory_module_0 = module_0.InventoryModule()

def test_case_1():
    str_0 = 'Error when getting collection version metadata for %s.%s:%s from %s (%s)'
    inventory_module_0 = module_0.InventoryModule()
    var_0 = inventory_module_0.verify_file(str_0)

def test_case_2():
    inventory_module_0 = module_0.InventoryModule()
    str_0 = 'dumy, dummy'
    var_0 = inventory_module_0.verify_file(str_0)

def test_case_3():
    inventory_module_0 = module_0.InventoryModule()
    str_0 = 'dummy,dummy'
    var_0 = inventory_module_0.verify_file(str_0)
    var_1 = inventory_module_0.verify_file(str_0)
    str_1 = '10.0.0.1, 10.0.0.2, 10.0.0.3'
    var_2 = inventory_module_0.verify_file(str_1)
    str_2 = '10.0.0.1,10.0.0.2, 10.0.0.3'
    var_3 = inventory_module_0.verify_file(str_2)
    str_3 = '10.0.0.1, 10.0.0.2 ,10.0.0.3'
    var_4 = inventory_module_0.verify_file(str_3)
    str_4 = '/etc/resolv.conf'
    var_5 = inventory_module_0.verify_file(str_4)