# Automatically generated by Pynguin.
import ansible.playbook.block as module_0

def test_case_0():
    pass

def test_case_1():
    block_0 = module_0.Block()
    var_0 = block_0.get_dep_chain()

def test_case_2():
    float_0 = 2983.893
    list_0 = [float_0, float_0, float_0]
    block_0 = module_0.Block(float_0, list_0)
    var_0 = block_0.__repr__()

def test_case_3():
    str_0 = 't^2]/fx\x0bA'
    block_0 = module_0.Block(str_0)
    block_1 = module_0.Block(block_0)
    var_0 = block_1.get_vars()

def test_case_4():
    int_0 = 126
    set_0 = set()
    block_0 = module_0.Block(set_0)
    var_0 = block_0.preprocess_data(int_0)

def test_case_5():
    block_0 = module_0.Block()
    var_0 = {}
    var_1 = block_0.filter_tagged_tasks(var_0)

def test_case_6():
    bool_0 = False
    block_0 = module_0.Block(bool_0)
    var_0 = block_0.copy()

def test_case_7():
    str_0 = 'wY,'
    dict_0 = {str_0: str_0, str_0: str_0}
    tuple_0 = (str_0, dict_0)
    block_0 = module_0.Block(str_0)
    float_0 = 4049.453746
    var_0 = block_0.get_dep_chain()
    block_1 = module_0.Block(block_0, block_0, float_0)
    var_1 = block_1.filter_tagged_tasks(tuple_0)

def test_case_8():
    float_0 = 982.9
    tuple_0 = ()
    block_0 = module_0.Block(float_0, tuple_0)
    var_0 = block_0.serialize()

def test_case_9():
    block_0 = module_0.Block()
    var_0 = dict()
    var_1 = block_0.deserialize(var_0)

def test_case_10():
    block_0 = module_0.Block()
    var_0 = block_0.set_loader(block_0)

def test_case_11():
    dict_0 = None
    float_0 = 0.0001
    block_0 = module_0.Block(float_0)
    var_0 = block_0.get_first_parent_include()
    set_0 = {dict_0, dict_0}
    dict_1 = {}
    list_0 = []
    bool_0 = True
    block_1 = module_0.Block(bool_0, block_0)
    block_2 = module_0.Block(dict_1, list_0, block_1)
    var_1 = block_2.copy(set_0)

def test_case_12():
    bool_0 = True
    block_0 = module_0.Block(bool_0)
    var_0 = block_0.copy()

def test_case_13():
    block_0 = module_0.Block()
    var_0 = block_0.has_tasks()

def test_case_14():
    bytes_0 = b'\x08\x1f\xb0\xb2\x0f\xa9\x8b\x830\x80\xe5)G\xcd\x90\xd3\xe2'
    block_0 = module_0.Block(bytes_0)
    var_0 = block_0.get_include_params()
    float_0 = -235.902636
    block_1 = module_0.Block(float_0)
    var_1 = block_1.has_tasks()

def test_case_15():
    bool_0 = True
    bytes_0 = b'\x11\x93\x8bx\xe1\xf3hv\xa8\xe4\x89\xf5\x8av\xdc\xba\xcet\x1e'
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    block_0 = module_0.Block(list_0)
    var_0 = block_0.set_loader(bytes_0)
    block_1 = module_0.Block(bool_0)
    var_1 = block_1.all_parents_static()
    var_2 = block_1.all_parents_static()

def test_case_16():
    str_0 = "^hN^_38u'tOq\x0cn"
    float_0 = -4122.1
    tuple_0 = ()
    block_0 = module_0.Block(str_0, float_0, tuple_0)
    var_0 = block_0.filter_tagged_tasks(str_0)

def test_case_17():
    str_0 = 'i_ge}qOc+*B#?{=6-D9'
    tuple_0 = ()
    set_0 = {tuple_0}
    block_0 = module_0.Block(tuple_0, set_0)
    var_0 = block_0.__ne__(block_0)
    dict_0 = {}
    var_1 = block_0.filter_tagged_tasks(dict_0)
    int_0 = 2655
    block_1 = module_0.Block()
    var_2 = block_1.all_parents_static()
    block_2 = module_0.Block()
    var_3 = block_1.serialize()
    float_0 = 2.0
    block_3 = module_0.Block()
    block_4 = module_0.Block(int_0, str_0, float_0, block_3)
    var_4 = block_3.__repr__()
    var_5 = block_4.copy()

def test_case_18():
    int_0 = None
    block_0 = module_0.Block()
    var_0 = block_0.is_block(int_0)
    tuple_0 = ()
    set_0 = set()
    block_1 = module_0.Block(tuple_0, set_0)
    var_1 = block_1.__ne__(block_0)
    dict_0 = {}
    block_2 = module_0.Block(set_0)
    bool_0 = False
    block_3 = module_0.Block(bool_0, tuple_0)
    var_2 = block_3.filter_tagged_tasks(dict_0)
    int_1 = 2655
    var_3 = block_3.get_dep_chain()
    str_0 = '__path__'
    tuple_1 = (str_0,)
    var_4 = block_2.preprocess_data(int_1)
    var_5 = block_1.get_dep_chain()
    block_4 = module_0.Block(tuple_1, block_3)
    block_5 = module_0.Block()
    var_6 = block_3.__repr__()
    var_7 = block_4.serialize()

def test_case_19():
    int_0 = None
    block_0 = module_0.Block()
    list_0 = [block_0]
    bytes_0 = b'\xfbi\nR\xd7\xe5\xf9\xfd\xbb\xb5'
    var_0 = block_0.get_first_parent_include()
    var_1 = block_0.is_block(int_0)
    str_0 = 'i_ge}qOc+*B#?{=6-D9'
    dict_0 = {str_0: list_0, bytes_0: var_1}
    var_2 = block_0.deserialize(dict_0)
    tuple_0 = ()
    set_0 = set()
    block_1 = module_0.Block(tuple_0, set_0)
    var_3 = block_1.__ne__(block_0)
    dict_1 = {}
    block_2 = module_0.Block(dict_1)
    var_4 = block_2.filter_tagged_tasks(block_2)
    var_5 = block_0.get_dep_chain()
    block_3 = module_0.Block()
    var_6 = block_2.all_parents_static()
    float_0 = 1916.34017
    bool_0 = False
    block_4 = module_0.Block(bool_0, tuple_0, block_2)
    block_5 = module_0.Block(float_0)
    str_1 = '+TlLYo>.D5P#^I+A6U4A'
    str_2 = '0242ac11-0009-8a42-f155-000000000670'
    block_6 = module_0.Block(tuple_0, str_1, str_2)
    var_7 = block_4.__repr__()
    var_8 = block_3.copy()
    var_9 = block_4.serialize()

def test_case_20():
    block_0 = module_0.Block()
    str_0 = 'dep_chain'
    str_1 = 'some string'
    str_2 = [str_1]
    str_3 = {str_0: str_2}
    var_0 = block_0.deserialize(str_3)
    str_4 = 'role'
    str_5 = '_role_path'
    str_6 = {str_5: str_1}
    str_7 = {str_4: str_6}
    var_1 = block_0.deserialize(str_7)

def test_case_21():
    block_0 = module_0.Block()
    str_0 = 'parent'
    str_1 = 'parent_type'
    bool_0 = True
    bool_1 = {str_1: bool_0}
    str_2 = 'Block'
    var_0 = {str_0: bool_1, str_1: str_2}
    var_1 = block_0.deserialize(var_0)