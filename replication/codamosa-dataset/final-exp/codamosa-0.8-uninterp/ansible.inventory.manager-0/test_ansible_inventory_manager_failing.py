# Automatically generated by Pynguin.
import ansible.inventory.manager as module_0

def test_case_0():
    try:
        int_0 = 1047
        set_0 = None
        int_1 = -427
        tuple_0 = ()
        inventory_manager_0 = module_0.InventoryManager(int_1, tuple_0)
        var_0 = inventory_manager_0.add_host(int_0, set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ''
        bytes_0 = b'5\x94S\x0exSE\xfe'
        inventory_manager_0 = module_0.InventoryManager(bytes_0)
        set_0 = {inventory_manager_0, inventory_manager_0, bytes_0, str_0}
        var_0 = inventory_manager_0.add_group(set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '.'
        inventory_manager_0 = module_0.InventoryManager(str_0, str_0)
        var_0 = inventory_manager_0.get_groups_dict()
        var_1 = inventory_manager_0.list_groups()
        inventory_manager_1 = module_0.InventoryManager(str_0)
        dict_0 = {str_0: var_0}
        var_2 = inventory_manager_1.add_host(dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'vu^/\x0c!gJ;]UW@M8gn2'
        str_1 = '_from'
        str_2 = ';'
        tuple_0 = ()
        bytes_0 = None
        set_0 = {str_0, str_1, bytes_0}
        tuple_1 = (tuple_0, set_0)
        inventory_manager_0 = module_0.InventoryManager(str_2, tuple_1)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b"\xf5\xbd\xd5'!\xd4z\x02&{w\xb2\xa6:\x9dYg"
        tuple_0 = ()
        set_0 = set()
        inventory_manager_0 = module_0.InventoryManager(tuple_0, set_0)
        var_0 = inventory_manager_0.restrict_to_hosts(bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'webservers'
        set_0 = {str_0}
        bool_0 = False
        str_1 = '4OBm\\"GSz$J,'
        inventory_manager_0 = module_0.InventoryManager(bool_0, str_1)
        inventory_manager_1 = module_0.InventoryManager(set_0, inventory_manager_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'vu^/\x0c!gJ;]UW@M8gn2'
        str_1 = '_from'
        str_2 = ''
        tuple_0 = ()
        bytes_0 = None
        set_0 = {str_0, str_1, bytes_0}
        tuple_1 = (tuple_0, set_0)
        inventory_manager_0 = module_0.InventoryManager(str_2, tuple_1)
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = False
        dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
        int_0 = 263
        inventory_manager_0 = module_0.InventoryManager(int_0)
        tuple_0 = (bool_0, dict_0, inventory_manager_0)
        var_0 = module_0.order_patterns(tuple_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'loc~alhost'
        inventory_manager_0 = module_0.InventoryManager(str_0, str_0)
        str_1 = ']~{fl(=w\x0c9.\t?9V]'
        str_2 = '&V~F|;~-@%ck'
        list_0 = [str_1, str_2, str_2, str_0]
        var_0 = inventory_manager_0.list_hosts(list_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '"BZW'
        inventory_manager_0 = module_0.InventoryManager(str_0, str_0)
        list_0 = []
        inventory_manager_1 = module_0.InventoryManager(list_0)
        var_0 = inventory_manager_1.get_hosts(str_0, list_0, inventory_manager_1, str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'RzRsrD'
        list_0 = [str_0]
        inventory_manager_0 = module_0.InventoryManager(str_0, list_0)
        var_0 = inventory_manager_0.clear_caches()
        str_1 = 'M]@u~xDkWDUS'
        var_1 = inventory_manager_0.subset(str_1)
    except BaseException:
        pass