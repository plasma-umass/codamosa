# Automatically generated by Pynguin.
import ansible.playbook.task as module_0
import ansible.utils.display as module_1
import ansible.playbook.block as module_2

def test_case_0():
    try:
        bytes_0 = b''
        str_0 = '|:BFo'
        tuple_0 = (str_0,)
        int_0 = -309
        int_1 = None
        list_0 = [tuple_0, int_0, int_0, int_1]
        float_0 = 1780.9
        task_0 = module_0.Task(list_0, float_0)
        var_0 = task_0.get_name(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 2870
        task_0 = module_0.Task()
        var_0 = task_0.load(int_0, task_0, int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        task_0 = module_0.Task()
        var_0 = task_0.get_vars()
        dict_0 = {task_0: var_0}
        var_1 = task_0.deserialize(dict_0)
        var_2 = task_0.load(dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        task_0 = module_0.Task()
        float_0 = None
        var_0 = task_0.post_validate(float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = -439
        task_0 = module_0.Task(int_0)
        bool_0 = False
        var_0 = task_0.post_validate(bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '>,I'
        int_0 = -2808
        task_0 = module_0.Task(str_0, int_0)
        var_0 = task_0.get_vars()
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = "_S'':g/S]03,."
        dict_0 = {str_0: str_0}
        task_0 = module_0.Task(dict_0)
        var_0 = task_0.copy()
    except BaseException:
        pass

def test_case_7():
    try:
        task_0 = module_0.Task()
        var_0 = task_0.copy()
        str_0 = 'DU]'
        var_1 = task_0.post_validate(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        display_0 = module_1.Display()
        dict_0 = {display_0: display_0, display_0: display_0}
        task_0 = module_0.Task(dict_0)
        var_0 = task_0.serialize()
    except BaseException:
        pass

def test_case_9():
    try:
        bool_0 = False
        str_0 = 'Y>9l`N}Ex~Nj8='
        bytes_0 = b'\xbc'
        task_0 = module_0.Task(str_0, bytes_0)
        var_0 = task_0.set_loader(bool_0)
    except BaseException:
        pass

def test_case_10():
    try:
        task_0 = module_0.Task()
        float_0 = None
        var_0 = task_0.all_parents_static()
        var_1 = task_0.post_validate(float_0)
    except BaseException:
        pass

def test_case_11():
    try:
        float_0 = -725.3188
        task_0 = module_0.Task(float_0)
        var_0 = task_0.all_parents_static()
    except BaseException:
        pass

def test_case_12():
    try:
        bool_0 = True
        task_0 = module_0.Task(bool_0)
        var_0 = task_0.get_first_parent_include()
    except BaseException:
        pass

def test_case_13():
    try:
        task_0 = module_0.Task()
        bytes_0 = b'\xe52D?\x93\x08\xf6H\xe7\x8d4S'
        var_0 = task_0.set_loader(bytes_0)
        list_0 = [task_0, task_0, task_0, task_0]
        str_0 = 'nf<.ut6vof*%r\r9Swx5'
        var_1 = task_0.set_loader(str_0)
        dict_0 = {}
        task_1 = module_0.Task(list_0, dict_0)
        var_2 = task_1.serialize()
    except BaseException:
        pass

def test_case_14():
    try:
        float_0 = 1565.09985
        task_0 = module_0.Task(float_0)
        dict_0 = {float_0: float_0, float_0: task_0, task_0: task_0, float_0: float_0}
        var_0 = task_0.deserialize(dict_0)
        var_1 = task_0.serialize()
    except BaseException:
        pass

def test_case_15():
    try:
        list_0 = []
        task_0 = module_0.Task(list_0)
        float_0 = 183.591
        var_0 = task_0.get_name(float_0)
        var_1 = task_0.get_include_params()
        var_2 = task_0.serialize()
        task_1 = module_0.Task()
        var_3 = task_0.preprocess_data(var_2)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'action'
        str_1 = 'args'
        str_2 = 'deleggate_to'
        str_3 = 'collections'
        str_4 = 'localhost'
        str_5 = 'my.colection'
        str_6 = [str_5]
        str_7 = {str_0: str_0, str_0: str_4, str_1: str_5, str_2: str_4, str_3: str_6}
        task_0 = module_0.Task()
        var_0 = task_0.serialize()
        var_1 = task_0.preprocess_data(str_7)
    except BaseException:
        pass

def test_case_17():
    try:
        float_0 = 3193.867117
        tuple_0 = (float_0,)
        task_0 = module_0.Task(tuple_0)
        task_1 = module_0.Task(task_0, task_0)
        var_0 = task_1.get_name()
        task_2 = module_0.Task()
        var_1 = task_2.deserialize(task_2)
    except BaseException:
        pass

def test_case_18():
    try:
        task_0 = module_0.Task()
        var_0 = task_0.__repr__()
        var_1 = task_0.get_vars()
        bool_0 = False
        tuple_0 = (bool_0,)
        int_0 = 1000
        display_0 = module_1.Display()
        block_0 = module_2.Block(display_0)
        block_1 = module_2.Block(int_0, block_0, int_0)
        block_2 = module_2.Block(tuple_0, task_0, block_1)
        str_0 = 'Tk@c~W7Mng~Y<<'
        dict_0 = {}
        task_1 = module_0.Task(block_2, str_0, dict_0)
        display_1 = module_1.Display()
        var_2 = task_1.serialize()
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = 'args'
        str_1 = 'delegate_to'
        str_2 = 'collections'
        str_3 = 'shell'
        str_4 = 'localhost'
        str_5 = 'my.colection'
        str_6 = {str_4: str_4, str_4: str_3, str_0: str_5, str_1: str_4, str_2: str_3}
        task_0 = module_0.Task()
        var_0 = task_0.preprocess_data(str_6)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = 'name'
        str_1 = 'debug'
        str_2 = 'collections'
        str_3 = 'vars'
        str_4 = 'tags'
        str_5 = 'Test Task'
        str_6 = 'var=hostvars'
        str_7 = 'my.collection'
        str_8 = [str_7]
        str_9 = 'test'
        str_10 = [str_9]
        str_11 = {str_0: str_5, str_1: str_6, str_2: str_8, str_3: str_10, str_4: str_10}
        task_0 = module_0.Task()
        var_0 = task_0.preprocess_data(str_11)
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = 'name'
        str_1 = 'args'
        str_2 = 'parent'
        str_3 = 'role'
        str_4 = 'resolved_action'
        str_5 = 'shell'
        str_6 = '_raw_params'
        str_7 = 'echo "Hello World"'
        str_8 = {str_6: str_7}
        str_9 = 'roles'
        var_0 = []
        var_1 = {str_4: var_0, str_4: str_4}
        str_10 = 'Block'
        bool_0 = False
        var_2 = {str_0: str_5, str_1: str_5, str_1: str_8, str_2: var_1, str_7: str_10, str_3: str_1, str_9: bool_0, str_4: str_5}
        task_0 = module_0.Task()
        var_3 = task_0.deserialize(var_2)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = 'ne'
        str_1 = 'args'
        str_2 = 'deegate_to'
        str_3 = 'collections'
        bool_0 = True
        task_0 = module_0.Task()
        var_0 = task_0.serialize()
        tuple_0 = (bool_0,)
        task_1 = module_0.Task(tuple_0)
        var_1 = task_1.__repr__()
        float_0 = 652.988
        var_2 = task_1.copy(float_0)
        str_4 = 'shell'
        str_5 = 'cmd'
        str_6 = 'echo "Hello World"'
        str_7 = {str_5: str_6}
        str_8 = 'my.collection'
        str_9 = [str_8]
        str_10 = {str_0: str_2, str_4: str_4, str_1: str_7, str_2: str_2, str_3: str_9}
        task_2 = module_0.Task()
        var_3 = task_2.get_first_parent_include()
        var_4 = task_2.preprocess_data(str_10)
    except BaseException:
        pass