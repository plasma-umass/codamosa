# Automatically generated by Pynguin.
import ansible.executor.task_result as module_0
import ansible.parsing.dataloader as module_1

def test_case_0():
    try:
        float_0 = 958.03
        task_result_0 = module_0.TaskResult(float_0, float_0, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 958.6151832620758
        bytes_0 = b'[\xe8\x8bS3\xe9\x9455\xce\xdd\xb7\x14\x19'
        dict_0 = {}
        task_result_0 = module_0.TaskResult(float_0, bytes_0, dict_0)
        var_0 = task_result_0.clean_copy()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'failed'
        str_1 = 'unreachable'
        bool_0 = True
        bool_1 = {str_0: bool_0, str_1: bool_0, str_1: bool_0}
        task_result_0 = module_0.TaskResult(str_1, str_1, bool_1)
        bool_2 = True
        var_0 = task_result_0.needs_debugger()
        bool_3 = {str_0: bool_2, str_0: bool_0, str_1: bool_0}
        var_1 = task_result_0.is_changed()
        task_result_1 = module_0.TaskResult(bool_2, bool_2, bool_3)
        var_2 = task_result_1.clean_copy()
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 958.6151832620758
        bytes_0 = b'[\xe8\x8bS3\xe9\x9455\xce\xdd\xb7\x14\x19'
        dict_0 = {}
        task_result_0 = module_0.TaskResult(float_0, bytes_0, dict_0)
        var_0 = task_result_0.is_failed()
        var_1 = task_result_0.clean_copy()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'test_host'
        var_0 = None
        str_1 = 'ansible_host'
        str_2 = {str_1: str_1}
        var_1 = None
        task_result_0 = module_0.TaskResult(str_0, var_0, str_2, var_1)
        var_2 = task_result_0.is_unreachable()
        var_3 = task_result_0.clean_copy()
    except BaseException:
        pass

def test_case_5():
    try:
        set_0 = None
        tuple_0 = (set_0,)
        float_0 = 2101.0847602802537
        dict_0 = {tuple_0: set_0, tuple_0: set_0, tuple_0: float_0, set_0: float_0, set_0: tuple_0}
        str_0 = '1.0.0'
        task_result_0 = module_0.TaskResult(set_0, dict_0, str_0)
        var_0 = task_result_0.needs_debugger(task_result_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b'<\xe7'
        task_result_0 = None
        tuple_0 = (task_result_0, task_result_0)
        str_0 = "A path is required to load argument specs for role '%s'"
        task_result_1 = module_0.TaskResult(bytes_0, tuple_0, str_0)
        var_0 = task_result_1.is_skipped()
    except BaseException:
        pass

def test_case_7():
    try:
        var_0 = None
        str_0 = 'ansible_host'
        var_1 = None
        task_result_0 = module_0.TaskResult(str_0, var_0, str_0, var_1)
        var_2 = task_result_0.clean_copy()
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'unreachable'
        bool_0 = True
        bool_1 = {str_0: bool_0, str_0: bool_0, str_0: bool_0}
        task_result_0 = module_0.TaskResult(bool_1, bool_1, bool_1)
        bool_2 = False
        var_0 = task_result_0.is_changed()
        set_0 = {bool_2, bool_2}
        var_1 = task_result_0.needs_debugger(set_0)
        data_loader_0 = module_1.DataLoader()
        task_result_1 = module_0.TaskResult(bool_1, data_loader_0, task_result_0, data_loader_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'failed'
        str_1 = 'unreachable'
        bool_0 = True
        bool_1 = {str_0: bool_0, str_1: bool_0, str_1: bool_0}
        task_result_0 = module_0.TaskResult(str_1, str_1, bool_1)
        bool_2 = False
        var_0 = task_result_0.is_changed()
        set_0 = {bool_2, bool_2}
        var_1 = task_result_0.needs_debugger(set_0)
        data_loader_0 = module_1.DataLoader()
        task_result_1 = module_0.TaskResult(bool_1, data_loader_0, task_result_0, data_loader_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'failed'
        bool_0 = True
        bool_1 = {}
        task_result_0 = module_0.TaskResult(bool_0, bool_0, bool_1)
        bool_2 = {str_0: bool_0}
        task_result_1 = module_0.TaskResult(bool_0, bool_0, bool_2)
        var_0 = task_result_0.is_failed()
        var_1 = task_result_1.needs_debugger(bool_0)
        var_2 = task_result_1.is_failed()
        var_3 = {}
        task_result_2 = module_0.TaskResult(var_3, var_3, var_3)
        var_4 = task_result_2.is_failed()
        str_1 = 'results'
        bool_3 = {str_0: bool_0}
        var_5 = task_result_2.needs_debugger()
        var_6 = {str_1: bool_3}
        task_result_3 = module_0.TaskResult(bool_0, bool_0, var_6)
        var_7 = task_result_3.is_failed()
        var_8 = task_result_3.clean_copy()
    except BaseException:
        pass