# Automatically generated by Pynguin.
import ansible.cli.inventory as module_0

def test_case_0():
    try:
        str_0 = '`'
        inventory_c_l_i_0 = module_0.InventoryCLI(str_0)
        var_0 = inventory_c_l_i_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '+Y]Jt>M$'
        set_0 = {str_0, str_0, str_0}
        bool_0 = True
        inventory_c_l_i_0 = module_0.InventoryCLI(bool_0)
        var_0 = inventory_c_l_i_0.dump(set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'X\x10'
        inventory_c_l_i_0 = module_0.InventoryCLI(bytes_0)
        var_0 = inventory_c_l_i_0.inventory_graph()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'remote_src'
        inventory_c_l_i_0 = module_0.InventoryCLI(str_0)
        set_0 = {inventory_c_l_i_0}
        bytes_0 = b'\xd3W\x81'
        bool_0 = True
        tuple_0 = (set_0, bytes_0, bool_0)
        var_0 = inventory_c_l_i_0.json_inventory(tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'aJ)o'
        str_1 = 's?h\x0b07'
        inventory_c_l_i_0 = module_0.InventoryCLI(str_1)
        var_0 = inventory_c_l_i_0.yaml_inventory(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        tuple_0 = None
        str_0 = 'y|z'
        inventory_c_l_i_0 = module_0.InventoryCLI(str_0)
        var_0 = inventory_c_l_i_0.toml_inventory(tuple_0)
    except BaseException:
        pass