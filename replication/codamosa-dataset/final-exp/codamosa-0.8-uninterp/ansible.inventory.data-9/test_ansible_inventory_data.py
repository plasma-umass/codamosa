# Automatically generated by Pynguin.
import ansible.inventory.data as module_0
import ansible.inventory.host as module_1
import ansible.inventory.group as module_2

def test_case_0():
    inventory_data_0 = module_0.InventoryData()

def test_case_1():
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.serialize()

def test_case_2():
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.reconcile_inventory()

def test_case_3():
    inventory_data_0 = module_0.InventoryData()
    str_0 = '127.0.0.1'
    var_0 = inventory_data_0.get_host(str_0)

def test_case_4():
    str_0 = 'v`Ma~Cz'
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.add_host(str_0)
    var_1 = inventory_data_0.remove_group(str_0)
    inventory_data_1 = module_0.InventoryData()
    var_2 = inventory_data_1.get_groups_dict()
    var_3 = inventory_data_0.get_groups_dict()

def test_case_5():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'test'
    var_0 = inventory_data_0.add_host(str_0)

def test_case_6():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'host0'
    host_0 = module_1.Host(str_0)
    var_0 = inventory_data_0.remove_host(host_0)
    var_1 = inventory_data_0.hosts
    var_2 = len(var_1)
    host_1 = module_1.Host(str_0)
    group_0 = module_2.Group()

def test_case_7():
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.get_groups_dict()

def test_case_8():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'local'
    var_0 = inventory_data_0.add_group(str_0)
    var_1 = inventory_data_0.get_host(inventory_data_0)

def test_case_9():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'all'
    var_0 = inventory_data_0.add_group(str_0)
    str_1 = 'localhost'
    var_1 = inventory_data_0.add_host(str_1, str_0)

def test_case_10():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'g1'
    var_0 = inventory_data_0.add_group(str_0)
    var_1 = inventory_data_0.add_host(str_0)
    var_2 = inventory_data_0.reconcile_inventory()

def test_case_11():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'lalhost'
    var_0 = inventory_data_0.add_host(str_0)
    host_0 = module_1.Host()
    inventory_data_1 = module_0.InventoryData()
    var_1 = inventory_data_0.reconcile_inventory()

def test_case_12():
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.reconcile_inventory()
    str_0 = 'localhost'
    var_1 = inventory_data_0.get_host(str_0)
    inventory_data_1 = module_0.InventoryData()
    inventory_data_2 = module_0.InventoryData()
    var_2 = inventory_data_1.get_groups_dict()
    var_3 = inventory_data_1.get_groups_dict()

def test_case_13():
    str_0 = '%s=*******'
    inventory_data_0 = module_0.InventoryData()
    var_0 = inventory_data_0.add_host(str_0)
    var_1 = inventory_data_0.reconcile_inventory()
    var_2 = inventory_data_0.get_groups_dict()
    var_3 = inventory_data_0.reconcile_inventory()
    inventory_data_1 = module_0.InventoryData()
    var_4 = inventory_data_1.get_groups_dict()
    var_5 = inventory_data_0.get_groups_dict()

def test_case_14():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'a=ll'
    var_0 = inventory_data_0.add_group(str_0)
    str_1 = 'localhost'
    var_1 = inventory_data_0.add_host(str_1, str_0)

def test_case_15():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'test'
    var_0 = inventory_data_0.add_group(str_0)
    str_1 = 'localhost'
    var_1 = inventory_data_0.add_host(str_1, str_0)
    str_2 = 'test1'
    var_2 = inventory_data_0.add_group(str_2)
    str_3 = '127.0.0.1'
    var_3 = inventory_data_0.add_host(str_3, str_2)
    var_4 = inventory_data_0.get_groups_dict()

def test_case_16():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'localhost'
    var_0 = inventory_data_0.add_host(str_0)
    var_1 = inventory_data_0.get_host(str_0)
    var_2 = var_1.name
    str_1 = '127.0.0.1'
    var_3 = inventory_data_0.get_host(str_1)

def test_case_17():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'test_group'
    var_0 = inventory_data_0.add_group(str_0)
    str_1 = 'test_host1'
    var_1 = inventory_data_0.add_host(str_1, var_0)
    var_2 = inventory_data_0.add_host(str_1, var_0)
    var_3 = inventory_data_0.get_host(str_1)
    var_4 = inventory_data_0.reconcile_inventory()
    var_5 = inventory_data_0.get_host(str_1)
    str_2 = 'j_|*hMtcT(yg'
    var_6 = inventory_data_0.get_host(str_2)

def test_case_18():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'test_group'
    var_0 = inventory_data_0.add_group(str_0)
    var_1 = inventory_data_0.add_host(str_0, var_0)
    var_2 = inventory_data_0.reconcile_inventory()

def test_case_19():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'h1'
    var_0 = inventory_data_0.add_host(str_0)
    str_1 = 'h2'
    var_1 = inventory_data_0.add_host(str_1)
    str_2 = 'h3'
    var_2 = inventory_data_0.add_host(str_2)
    str_3 = 'g1'
    var_3 = inventory_data_0.add_group(str_3)
    str_4 = 'g2'
    var_4 = inventory_data_0.add_group(str_4)
    str_5 = 'g3'
    var_5 = inventory_data_0.reconcile_inventory()
    var_6 = inventory_data_0.add_group(str_5)
    var_7 = inventory_data_0.add_child(str_3, str_0)
    var_8 = inventory_data_0.add_child(str_5, str_2)
    var_9 = inventory_data_0.reconcile_inventory()

def test_case_20():
    inventory_data_0 = module_0.InventoryData()
    str_0 = 'all'
    var_0 = inventory_data_0.add_group(str_0)
    str_1 = 'ungrouped'
    var_1 = inventory_data_0.add_group(str_1)
    var_2 = inventory_data_0.add_child(str_0, str_1)
    str_2 = 'host1'
    var_3 = inventory_data_0.add_host(str_2, str_0)
    str_3 = 'host2'
    var_4 = inventory_data_0.add_host(str_3, str_0)
    str_4 = 'host3'
    var_5 = inventory_data_0.add_host(str_4, str_1)
    var_6 = inventory_data_0.reconcile_inventory()
    var_7 = inventory_data_0.hosts[str_2]