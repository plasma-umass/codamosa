# Automatically generated by Pynguin.
import ansible.plugins.inventory.host_list as module_0

def test_case_0():
    try:
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.verify_file(inventory_module_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = None
        str_0 = 'DNS'
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.parse(int_0, int_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 1565.0
        int_0 = None
        str_0 = 'l`,v\x0c'
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.verify_file(str_0)
        str_1 = 'DNS'
        inventory_module_1 = module_0.InventoryModule()
        var_1 = inventory_module_1.parse(float_0, int_0, str_1, str_1)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = None
        str_0 = '>'
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.parse(int_0, int_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = 712.4806
        int_0 = None
        inventory_module_0 = module_0.InventoryModule()
        str_0 = '\t,K'
        var_0 = inventory_module_0.parse(float_0, int_0, str_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = 1695.5805254764778
        int_0 = None
        inventory_module_0 = module_0.InventoryModule()
        inventory_module_1 = module_0.InventoryModule()
        str_0 = ''
        var_0 = inventory_module_1.parse(inventory_module_1, int_0, str_0)
        str_1 = 'i/YGy"caIJl\x0bun>rJ'
        var_1 = inventory_module_1.parse(float_0, int_0, str_1, str_1)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '/sys/devices/virtual/dmi/id/product_version'
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.verify_file(str_0)
        inventory_module_1 = module_0.InventoryModule()
        str_1 = '8+:\x0b('
        dict_0 = {str_0: str_1}
        var_1 = inventory_module_1.verify_file(dict_0)
        inventory_module_2 = module_0.InventoryModule()
        list_0 = None
        str_2 = "The error appears to be in '%s': line %s, column %s, but may\nbe elsewhere in the file depending on the exact syntax problem.\n"
        int_0 = 2963
        var_2 = inventory_module_0.parse(dict_0, list_0, str_2, int_0)
    except BaseException:
        pass