# Automatically generated by Pynguin.
import ansible.playbook.block as module_0

def test_case_0():
    pass

def test_case_1():
    block_0 = module_0.Block()

def test_case_2():
    str_0 = "'append' is set, but no 'groups' are specified. Use 'groups' for appending new groups.This will change to an error in Ansible 2.14."
    bool_0 = False
    dict_0 = {str_0: str_0, str_0: str_0, str_0: bool_0, bool_0: str_0}
    str_1 = '\n        Iterates over the roles/tasks in a play, using the given (or default)\n        strategy for queueing tasks. The default is the linear strategy, which\n        operates like classic Ansible by keeping all hosts in lock-step with\n        a given task (meaning no hosts move on to the next task until all hosts\n        are done with the current task).\n        '
    tuple_0 = (str_1,)
    tuple_1 = (dict_0,)
    block_0 = module_0.Block(str_0, str_0, dict_0, tuple_0, tuple_1)
    var_0 = block_0.__repr__()

def test_case_3():
    bool_0 = True
    float_0 = 100.0
    block_0 = module_0.Block(bool_0, float_0)
    var_0 = block_0.filter_tagged_tasks(bool_0)

def test_case_4():
    bool_0 = False
    block_0 = module_0.Block(bool_0)
    var_0 = block_0.get_vars()

def test_case_5():
    var_0 = None
    bool_0 = False
    block_0 = module_0.Block(var_0, var_0, var_0, var_0, bool_0, var_0)
    int_0 = 1
    int_1 = 2
    int_2 = 3
    int_3 = [int_0, int_1, int_2]
    var_1 = block_0.get_vars()
    var_2 = dict(block=int_3)
    var_3 = block_0.preprocess_data(var_2)
    var_4 = dict(a=int_0)
    var_5 = block_0.preprocess_data(var_4)
    int_4 = [int_0, int_1, int_2]
    var_6 = block_0.preprocess_data(int_4)
    var_7 = dict()
    var_8 = block_0.preprocess_data(var_7)
    var_9 = dict(block=var_8)

def test_case_6():
    float_0 = 100.0
    str_0 = '7M<Ky0=}5\r[k-touM'
    list_0 = []
    block_0 = module_0.Block(str_0, list_0)
    var_0 = block_0.is_block(float_0)

def test_case_7():
    float_0 = 4045.4
    block_0 = module_0.Block(float_0)
    var_0 = block_0.copy()

def test_case_8():
    block_0 = module_0.Block()
    var_0 = block_0.get_dep_chain()

def test_case_9():
    block_0 = module_0.Block()
    float_0 = 3.677606864643743
    block_1 = module_0.Block()
    block_2 = module_0.Block(float_0, block_1)
    var_0 = block_1.get_vars()
    var_1 = block_1.serialize()
    list_0 = None
    float_1 = -437.37
    block_3 = module_0.Block(float_1, list_0)
    var_2 = block_2.copy()
    var_3 = block_0.serialize()

def test_case_10():
    bool_0 = False
    int_0 = -1890
    str_0 = 'V'
    list_0 = [int_0, int_0, str_0]
    block_0 = module_0.Block(int_0, str_0, list_0)
    var_0 = block_0.filter_tagged_tasks(bool_0)

def test_case_11():
    block_0 = module_0.Block()
    var_0 = block_0.serialize()

def test_case_12():
    dict_0 = {}
    block_0 = module_0.Block()
    block_1 = module_0.Block(block_0)
    var_0 = block_1.deserialize(dict_0)

def test_case_13():
    str_0 = ' f=\x0c\x0cML\'kq%7&"-oq[Ke'
    block_0 = module_0.Block()
    var_0 = block_0.set_loader(str_0)

def test_case_14():
    block_0 = module_0.Block()
    int_0 = 461
    float_0 = 1.5
    block_1 = module_0.Block()
    block_2 = module_0.Block(float_0, block_1)
    str_0 = 'Vkw|c/]'
    tuple_0 = (str_0, float_0)
    var_0 = block_1.get_vars()
    var_1 = block_1.filter_tagged_tasks(tuple_0)
    var_2 = block_1.serialize()
    var_3 = block_2.set_loader(int_0)
    var_4 = block_2.filter_tagged_tasks(int_0)
    var_5 = block_1.copy()
    var_6 = block_2.serialize()

def test_case_15():
    block_0 = module_0.Block()
    var_0 = block_0.has_tasks()

def test_case_16():
    str_0 = ']%WSPDYn6WDHZu^!u4-'
    block_0 = module_0.Block(str_0)
    var_0 = block_0.filter_tagged_tasks(block_0)
    var_1 = block_0.get_include_params()

def test_case_17():
    block_0 = module_0.Block()
    var_0 = block_0.copy()
    var_1 = block_0.all_parents_static()

def test_case_18():
    str_0 = '-T&`\n5;q,Y'
    list_0 = [str_0, str_0, str_0, str_0]
    block_0 = module_0.Block(list_0)
    var_0 = block_0.get_first_parent_include()
    var_1 = block_0.get_dep_chain()

def test_case_19():
    float_0 = -250.0
    block_0 = module_0.Block(float_0)
    block_1 = module_0.Block(block_0)
    var_0 = block_1.copy()

def test_case_20():
    bool_0 = True
    dict_0 = {bool_0: bool_0}
    float_0 = 3606.98
    block_0 = module_0.Block(float_0)
    block_1 = module_0.Block(float_0, block_0)
    var_0 = block_1.deserialize(dict_0)
    block_2 = module_0.Block(bool_0, float_0)
    var_1 = block_1.serialize()

def test_case_21():
    str_0 = "p3qsR_Uap>n'2m"
    block_0 = module_0.Block()
    var_0 = block_0.get_dep_chain()
    block_1 = module_0.Block(var_0, str_0, block_0, block_0, var_0)
    var_1 = block_1.__repr__()
    var_2 = block_1.copy()
    var_3 = block_1.serialize()
    var_4 = block_0.get_first_parent_include()
    bool_0 = True
    block_2 = module_0.Block(bool_0, bool_0)
    set_0 = None
    bytes_0 = b'\xfe\x83\xba\x8cjt.r\xf5i\x03r\xc6\xe5\x80%\xf1F'
    var_5 = block_2.filter_tagged_tasks(bytes_0)
    var_6 = block_1.copy(set_0)
    var_7 = block_0.serialize()

def test_case_22():
    block_0 = module_0.Block()
    str_0 = 'rescue'
    str_1 = 'always'
    str_2 = 'no_log'
    str_3 = 'name'
    str_4 = 'when'
    str_5 = 'other_attribute'
    str_6 = 'dep_chain'
    str_7 = 'role'
    str_8 = 'parent'
    str_9 = 'parent_type'
    var_0 = []
    var_1 = []
    bool_0 = False
    str_10 = 'foo'
    str_11 = 'False'
    str_12 = 'ignore_me'
    var_2 = None
    str_13 = 'static'
    str_14 = 'test'
    bool_1 = True
    var_3 = {str_3: str_14, str_13: bool_1}
    var_4 = {str_3: str_14, str_13: bool_0}
    str_15 = 'TaskInclude'
    var_5 = {str_0: var_0, str_1: var_1, str_2: bool_0, str_3: str_10, str_4: str_11, str_5: str_12, str_6: var_2, str_7: var_3, str_8: var_4, str_9: str_15}
    var_6 = block_0.deserialize(var_5)
    var_7 = block_0._parent