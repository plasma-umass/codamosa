# Automatically generated by Pynguin.
import ansible.playbook.task as module_0
import ansible.playbook.block as module_1
import ansible.playbook.role as module_2

def test_case_0():
    pass

def test_case_1():
    task_0 = module_0.Task()
    var_0 = task_0.get_name()

def test_case_2():
    task_0 = module_0.Task()
    bytes_0 = b'\x8dt'
    tuple_0 = ()
    set_0 = set()
    bool_0 = False
    float_0 = 2755.0
    block_0 = module_1.Block(set_0, bool_0, float_0)
    role_0 = module_2.Role(tuple_0, block_0)
    task_1 = module_0.Task(bytes_0, role_0)
    var_0 = task_0.set_loader(role_0)
    var_1 = task_1.get_name()

def test_case_3():
    task_0 = module_0.Task()
    var_0 = task_0.__repr__()

def test_case_4():
    task_0 = module_0.Task()
    var_0 = task_0.get_vars()

def test_case_5():
    task_0 = module_0.Task()
    var_0 = task_0.get_include_params()

def test_case_6():
    list_0 = []
    task_0 = module_0.Task(list_0)
    var_0 = task_0.copy()

def test_case_7():
    task_0 = module_0.Task()
    var_0 = task_0.serialize()

def test_case_8():
    task_0 = module_0.Task()
    var_0 = {}
    var_1 = task_0.deserialize(var_0)

def test_case_9():
    block_0 = module_1.Block()
    task_0 = module_0.Task(block_0)
    var_0 = task_0.serialize()
    var_1 = task_0.all_parents_static()

def test_case_10():
    task_0 = module_0.Task()
    task_1 = module_0.Task(task_0)
    var_0 = task_1.get_first_parent_include()

def test_case_11():
    bytes_0 = b'\x19\xb5'
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    block_0 = module_1.Block()
    bool_0 = False
    task_0 = module_0.Task(block_0, bool_0)
    var_0 = task_0.deserialize(dict_0)
    var_1 = task_0.get_first_parent_include()
    task_1 = module_0.Task()
    var_2 = task_0.serialize()
    str_0 = 'te7'
    var_3 = dict(action=str_0)
    task_2 = module_0.Task()
    var_4 = task_1.copy()
    var_5 = task_2.load(var_3)
    var_6 = task_2.get_include_params()
    var_7 = task_2.get_vars()
    var_8 = task_2.get_first_parent_include()
    var_9 = task_1.get_first_parent_include()
    var_10 = task_2.__repr__()
    str_1 = "'>>"
    task_3 = module_0.Task(str_1)
    var_11 = task_3.get_name()

def test_case_12():
    str_0 = 'test'
    var_0 = dict(action=str_0)
    task_0 = module_0.Task()
    var_1 = task_0.load(var_0)