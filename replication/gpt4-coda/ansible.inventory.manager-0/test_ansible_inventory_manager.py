# Automatically generated by Pynguin.
import ansible.inventory.manager as module_0
import ansible.utils.display as module_1

def test_case_0():
    pass

def test_case_1():
    float_0 = 2.0
    inventory_manager_0 = module_0.InventoryManager(float_0)
    var_0 = inventory_manager_0.get_hosts()

def test_case_2():
    str_0 = 'localhost,'
    inventory_manager_0 = module_0.InventoryManager(str_0, str_0)
    var_0 = inventory_manager_0.get_hosts(str_0)
    str_1 = '&MKh5p?/H.kowo'
    var_1 = inventory_manager_0.subset(str_1)
    bool_0 = False
    var_2 = inventory_manager_0.get_hosts(bool_0, inventory_manager_0)
    set_0 = {str_0, str_1}
    var_3 = module_0.split_host_pattern(set_0)
    var_4 = inventory_manager_0.list_hosts(str_0)

def test_case_3():
    int_0 = -1519
    var_0 = module_0.split_host_pattern(int_0)

def test_case_4():
    var_0 = None
    str_0 = 'localhost,'
    inventory_manager_0 = module_0.InventoryManager(var_0, str_0)
    var_1 = inventory_manager_0.parse_sources()
    var_2 = inventory_manager_0.get_hosts()
    var_3 = inventory_manager_0.add_host(str_0)
    var_4 = inventory_manager_0.get_hosts(str_0)

def test_case_5():
    str_0 = '09>yU~`\x0b]\x0c1t'
    inventory_manager_0 = module_0.InventoryManager(str_0)

def test_case_6():
    float_0 = -3714.46467
    str_0 = '[kMm$`&zK///'
    inventory_manager_0 = module_0.InventoryManager(str_0, str_0)
    var_0 = inventory_manager_0.get_hosts(float_0)

def test_case_7():
    str_0 = 'returndocs'
    tuple_0 = None
    str_1 = '73<#4<8]J*@RjL;\x0c5'
    tuple_1 = (tuple_0, str_1)
    inventory_manager_0 = module_0.InventoryManager(str_1, tuple_1)
    var_0 = inventory_manager_0.add_group(str_0)

def test_case_8():
    str_0 = 'localhost,'
    bool_0 = False
    inventory_manager_0 = module_0.InventoryManager(bool_0, str_0)
    var_0 = inventory_manager_0.get_groups_dict()

def test_case_9():
    int_0 = 255
    inventory_manager_0 = module_0.InventoryManager(int_0)
    var_0 = inventory_manager_0.reconcile_inventory()

def test_case_10():
    bytes_0 = b'*9\x1dv8\x89\x0f\x15'
    inventory_manager_0 = module_0.InventoryManager(bytes_0)
    var_0 = inventory_manager_0.remove_restriction()
    bool_0 = False
    str_0 = None
    tuple_0 = ()
    var_1 = inventory_manager_0.parse_source(str_0, tuple_0)
    var_2 = inventory_manager_0.refresh_inventory()
    var_3 = inventory_manager_0.clear_caches()
    var_4 = inventory_manager_0.clear_pattern_cache()
    inventory_manager_1 = module_0.InventoryManager(bool_0)
    bytes_1 = b'\x80\n\xf4m\xf6'
    var_5 = inventory_manager_0.get_host(bytes_1)

def test_case_11():
    tuple_0 = None
    str_0 = '73<#4<8]J*@RjL;\x0c5'
    tuple_1 = (tuple_0, str_0)
    inventory_manager_0 = module_0.InventoryManager(str_0, tuple_1)

def test_case_12():
    set_0 = None
    str_0 = 'c<,gw)mly'
    inventory_manager_0 = module_0.InventoryManager(str_0)
    var_0 = inventory_manager_0.parse_source(set_0)

def test_case_13():
    tuple_0 = ()
    inventory_manager_0 = module_0.InventoryManager(tuple_0)
    var_0 = inventory_manager_0.clear_caches()

def test_case_14():
    bytes_0 = b'\xb9\t\xbc\x8f\x94y\x89Ar\xae\xb8k\x12^'
    inventory_manager_0 = module_0.InventoryManager(bytes_0)
    var_0 = inventory_manager_0.refresh_inventory()
    var_1 = inventory_manager_0.list_hosts()
    bytes_1 = b'\xbd'
    var_2 = module_0.split_host_pattern(bytes_1)
    var_3 = inventory_manager_0.list_groups()
    var_4 = inventory_manager_0.refresh_inventory()
    str_0 = 'I'
    var_5 = inventory_manager_0.get_hosts(str_0)

def test_case_15():
    tuple_0 = ()
    inventory_manager_0 = module_0.InventoryManager(tuple_0)
    var_0 = inventory_manager_0.list_hosts()
    var_1 = inventory_manager_0.clear_caches()

def test_case_16():
    bool_0 = False
    str_0 = 'vZ\tYp\nF\nX*x@ih\tQ,{-}'
    inventory_manager_0 = module_0.InventoryManager(bool_0, str_0)
    inventory_manager_1 = module_0.InventoryManager(str_0)
    var_0 = inventory_manager_1.list_groups()

def test_case_17():
    bytes_0 = b'\x0f\xe8\x83\xec'
    inventory_manager_0 = module_0.InventoryManager(bytes_0)
    var_0 = inventory_manager_0.subset(bytes_0)

def test_case_18():
    float_0 = 0.001
    inventory_manager_0 = module_0.InventoryManager(float_0)
    var_0 = inventory_manager_0.remove_restriction()

def test_case_19():
    bool_0 = False
    set_0 = {bool_0}
    inventory_manager_0 = module_0.InventoryManager(set_0)
    var_0 = inventory_manager_0.clear_pattern_cache()
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    list_0 = []
    inventory_manager_1 = module_0.InventoryManager(bool_0, dict_0, list_0)
    bytes_0 = b'*\xd9'
    bool_1 = True
    dict_1 = {bytes_0: bool_1, bytes_0: bytes_0, bool_1: bytes_0}
    int_0 = -3525
    bool_2 = True
    int_1 = 1716
    tuple_0 = (int_0, bool_2, bool_1, int_1)
    str_0 = '*oY4!IcC~fR:&DA'
    tuple_1 = (inventory_manager_1, tuple_0, str_0)
    var_1 = module_0.split_host_pattern(tuple_1)
    inventory_manager_2 = module_0.InventoryManager(dict_1)
    var_2 = inventory_manager_2.get_host(inventory_manager_1)

def test_case_20():
    str_0 = 'group1'
    list_0 = None
    float_0 = None
    list_1 = [list_0, float_0, str_0, float_0]
    set_0 = set()
    inventory_manager_0 = module_0.InventoryManager(set_0, set_0)
    var_0 = inventory_manager_0.list_hosts(list_1)

def test_case_21():
    dict_0 = None
    str_0 = '-3019'
    str_1 = 'bLN@\nd`EH\x0bhn`}dcd'
    inventory_manager_0 = module_0.InventoryManager(str_0, str_1)
    var_0 = inventory_manager_0.restrict_to_hosts(dict_0)
    bytes_0 = b'W\x1c\x8d\xd1n\xdb\x01\xa6\n\xb5 \xfb\xccrP\x08/G'
    dict_1 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    var_1 = module_0.split_host_pattern(dict_1)

def test_case_22():
    bytes_0 = b'\xb9\t\xbc\x8f\x94y\x89Ar\xae\xb8k\x12^'
    inventory_manager_0 = module_0.InventoryManager(bytes_0)
    var_0 = inventory_manager_0.list_hosts()
    bytes_1 = b'\xbd'
    var_1 = module_0.split_host_pattern(bytes_1)
    var_2 = inventory_manager_0.list_groups()
    var_3 = inventory_manager_0.refresh_inventory()
    bytes_2 = b'dp\x88'
    var_4 = inventory_manager_0.get_hosts(inventory_manager_0, bytes_2)
    str_0 = 'I'
    var_5 = inventory_manager_0.get_hosts(str_0)

def test_case_23():
    str_0 = 'localhost,'
    inventory_manager_0 = module_0.InventoryManager(str_0, str_0)
    var_0 = inventory_manager_0.get_hosts()
    float_0 = -2295.18
    str_1 = '<ansible.inventory.manager.InventoryManager object at 0x7f1492d4ee90>'
    int_0 = -1161
    var_1 = inventory_manager_0.get_hosts(float_0, str_1, int_0)
    var_2 = inventory_manager_0.clear_pattern_cache()
    str_2 = 'll'
    var_3 = inventory_manager_0.get_hosts(str_2)
    var_4 = inventory_manager_0.get_hosts(str_0)
    str_3 = '&MKh5p?/H.kowo'
    var_5 = inventory_manager_0.subset(str_3)
    bool_0 = False
    int_1 = 2482
    var_6 = inventory_manager_0.get_hosts(int_1)
    var_7 = inventory_manager_0.get_hosts(bool_0, inventory_manager_0)
    display_0 = module_1.Display()
    float_1 = -1773.953717
    var_8 = inventory_manager_0.parse_source(float_1)

def test_case_24():
    var_0 = None
    str_0 = 'localhost,'
    inventory_manager_0 = module_0.InventoryManager(var_0, str_0)
    var_1 = inventory_manager_0.list_hosts()
    var_2 = inventory_manager_0._sources

def test_case_25():
    var_0 = None
    str_0 = 'localhost,'
    inventory_manager_0 = module_0.InventoryManager(var_0, str_0)
    var_1 = inventory_manager_0.get_hosts()
    str_1 = 'all'
    var_2 = inventory_manager_0.get_hosts(str_1)
    str_2 = [str_1, str_1]
    var_3 = inventory_manager_0.get_hosts(str_2)
    str_3 = '&MKh5p?/H.kowo'
    var_4 = inventory_manager_0.subset(str_3)
    bool_0 = True
    int_0 = 2482
    var_5 = inventory_manager_0.get_hosts(int_0)
    var_6 = inventory_manager_0.get_hosts(bool_0, inventory_manager_0)
    display_0 = module_1.Display()
    var_7 = inventory_manager_0.list_hosts(bool_0)

def test_case_26():
    str_0 = 'webservers'
    str_1 = 'dbservers'
    str_2 = [str_0, str_1]
    var_0 = module_0.order_patterns(str_2)
    str_3 = '!webservers'
    str_4 = '!dbservers'
    str_5 = [str_3, str_4]
    var_1 = module_0.order_patterns(str_5)
    str_6 = '&webservers'
    str_7 = '&dbservers'
    str_8 = [str_6, str_7]
    var_2 = module_0.order_patterns(str_8)

def test_case_27():
    var_0 = None
    str_0 = 'localhost,'
    inventory_manager_0 = module_0.InventoryManager(var_0, str_0)
    var_1 = inventory_manager_0.get_hosts()
    str_1 = 'otherhost'
    str_2 = [str_1, str_1]
    var_2 = inventory_manager_0.get_hosts(str_2)
    display_0 = module_1.Display()
    var_3 = inventory_manager_0.get_hosts(display_0)
    str_3 = 'vmh]!|Z'
    var_4 = inventory_manager_0.subset(str_3)
    int_0 = -1095
    var_5 = inventory_manager_0.get_hosts(int_0)
    float_0 = -2206.044
    var_6 = inventory_manager_0.list_hosts(float_0)

def test_case_28():
    str_0 = 'lD_hf`ChV\n~'
    inventory_manager_0 = module_0.InventoryManager(str_0, str_0)
    var_0 = inventory_manager_0.get_hosts()
    str_1 = 'll_'
    var_1 = inventory_manager_0.get_hosts(str_1)
    var_2 = inventory_manager_0.get_hosts(str_0)
    str_2 = '&MKh5p?/H.kowo'
    var_3 = inventory_manager_0.subset(str_2)
    var_4 = inventory_manager_0.remove_restriction()
    bool_0 = False
    int_0 = 2482
    var_5 = inventory_manager_0.get_hosts(int_0)
    var_6 = inventory_manager_0.get_hosts(bool_0, inventory_manager_0)
    var_7 = inventory_manager_0.get_host(int_0)
    display_0 = module_1.Display()
    var_8 = inventory_manager_0.parse_sources()
    var_9 = inventory_manager_0.list_hosts()

def test_case_29():
    bool_0 = True
    inventory_manager_0 = module_0.InventoryManager(bool_0)
    var_0 = inventory_manager_0.list_groups()
    var_1 = None
    str_0 = 'localhost,'
    inventory_manager_1 = module_0.InventoryManager(var_1, str_0)
    var_2 = inventory_manager_1.get_hosts()
    str_1 = '!tf/XM;Uzp'
    var_3 = inventory_manager_1.get_hosts(str_1)
    str_2 = [str_1, str_1]
    var_4 = inventory_manager_1.get_hosts(str_2)
    tuple_0 = None
    inventory_manager_2 = module_0.InventoryManager(tuple_0, str_2)
    set_0 = {str_1, str_0}
    inventory_manager_3 = module_0.InventoryManager(bool_0, set_0)

def test_case_30():
    bool_0 = True
    inventory_manager_0 = module_0.InventoryManager(bool_0)
    var_0 = inventory_manager_0.list_groups()
    str_0 = 'localhost,'
    str_1 = "423`}FF3 O<w'"
    inventory_manager_1 = module_0.InventoryManager(str_1, str_0)
    var_1 = inventory_manager_1.get_hosts()
    str_2 = 'a~l'
    var_2 = inventory_manager_1.get_hosts(str_2)
    str_3 = [str_0, str_0]
    var_3 = inventory_manager_1.get_hosts(str_3)
    display_0 = module_1.Display()
    var_4 = inventory_manager_1.get_hosts(display_0)
    var_5 = display_0.set_cowsay_info()
    tuple_0 = None
    inventory_manager_2 = module_0.InventoryManager(tuple_0, str_3)
    var_6 = inventory_manager_1.subset(str_3)
    var_7 = inventory_manager_1.list_hosts()
    float_0 = -2206.044
    var_8 = inventory_manager_1.list_hosts(float_0)
    set_0 = {str_2, str_2}
    inventory_manager_3 = module_0.InventoryManager(bool_0, set_0)
    var_9 = inventory_manager_2.list_hosts()

def test_case_31():
    str_0 = 'all'
    str_1 = 'group1'
    str_2 = 'group2'
    str_3 = 'hosts'
    str_4 = 'vars'
    str_5 = 'host1'
    str_6 = 'host2'
    str_7 = 'host3'
    str_8 = [str_5, str_6, str_7]
    var_0 = {}
    var_1 = {str_3: str_8, str_4: var_0}
    str_9 = [str_5]
    var_2 = {}
    var_3 = {str_3: str_9, str_4: var_2}
    str_10 = [str_6]
    var_4 = {}
    var_5 = {str_3: str_10, str_4: var_4}
    var_6 = {str_0: var_1, str_1: var_3, str_2: var_5}
    var_7 = None
    str_11 = '/dev/null'
    str_12 = [str_11]
    inventory_manager_0 = module_0.InventoryManager(var_7, str_12)
    var_8 = inventory_manager_0.parse_sources()
    var_9 = inventory_manager_0.get_hosts()
    var_10 = inventory_manager_0.get_hosts(str_5)