# Automatically generated by Pynguin.
import ansible.plugins.inventory.generator as module_0
import ansible.plugins.inventory as module_1

def test_case_0():
    try:
        inventory_module_0 = module_0.InventoryModule()
        dict_0 = {inventory_module_0: inventory_module_0}
        set_0 = set()
        var_0 = inventory_module_0.template(dict_0, set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        inventory_module_0 = module_0.InventoryModule()
        list_0 = [inventory_module_0, inventory_module_0, inventory_module_0]
        str_0 = 'r"tY?i.& RXh'
        bytes_0 = b';'
        var_0 = inventory_module_0.add_parents(list_0, inventory_module_0, str_0, bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xd9\xa4d{\x82\xce9~\x94\x807{\xef\xeb\xa1\xa4\xf8\xf9'
        int_0 = -1075
        str_0 = '-:Pd.17(l1p<\rBWs#*YE'
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.parse(bytes_0, int_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        inventory_module_0 = module_0.InventoryModule()
        float_0 = -4046.86
        tuple_0 = ()
        var_0 = inventory_module_0.parse(float_0, tuple_0, tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 988
        bool_0 = False
        set_0 = set()
        inventory_module_0 = module_0.InventoryModule()
        var_0 = inventory_module_0.add_parents(int_0, bool_0, set_0, inventory_module_0)
        bytes_0 = b'\xce\xa3'
        str_0 = 'g'
        var_1 = inventory_module_0.add_parents(bool_0, int_0, bytes_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        base_inventory_plugin_0 = module_1.BaseInventoryPlugin()
        inventory_module_0 = module_0.InventoryModule()
        str_0 = 'name'
        str_1 = 'child'
        str_2 = {str_0: str_1}
        str_3 = 'parent'
        str_4 = {str_0: str_3}
        str_5 = [str_4]
        str_6 = 'test'
        str_7 = 'value'
        str_8 = {str_6: str_7}
        var_0 = inventory_module_0.add_parents(base_inventory_plugin_0, str_2, str_5, str_8)
    except BaseException:
        pass