# Automatically generated by Pynguin.
import ansible.plugins.inventory.generator as module_0

def test_case_0():
    try:
        str_0 = ':/'
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.template(str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        inventory_module_0 = module_0.InventoryModule()
        dict_0 = {inventory_module_0: inventory_module_0}
        float_0 = 1264.3
        int_0 = -2428
        var_0 = inventory_module_0.add_parents(dict_0, float_0, dict_0, int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = -1133.902
        dict_0 = {float_0: float_0}
        inventory_module_0 = module_0.InventoryModule()
        inventory_module_1 = module_0.InventoryModule()
        var_0 = inventory_module_1.parse(dict_0, inventory_module_0, float_0)
    except BaseException:
        pass

def test_case_3():
    try:
        set_0 = None
        str_0 = '9?m[G'
        bool_0 = True
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.parse(set_0, set_0, str_0, bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '_meta'
        str_1 = 'hostvars'
        var_0 = {}
        var_1 = {str_1: var_0}
        var_2 = {str_0: var_1}
        str_2 = 'name'
        inventory_module_0 = module_0.InventoryModule()
        str_3 = 'build_web'
        str_4 = 'parents'
        str_5 = '{{ operation }}'
        str_6 = 'master'
        var_3 = []
        var_4 = {str_2: str_6, str_4: var_3}
        var_5 = [var_4]
        var_6 = {str_2: str_5, str_4: var_5}
        str_7 = '{application}'
        var_7 = []
        var_8 = {str_2: str_7, str_4: var_7}
        var_9 = [var_6, var_8]
        str_8 = 'operation'
        str_9 = 'application'
        str_10 = 'build'
        str_11 = 'web'
        str_12 = {str_8: str_10, str_9: str_11}
        var_10 = inventory_module_0.add_parents(var_2, str_3, var_9, str_12)
    except BaseException:
        pass