# Automatically generated by Pynguin.
import ansible.executor.task_result as module_0

def test_case_0():
    try:
        float_0 = 1943.441834
        str_0 = '7\t*'
        task_result_0 = module_0.TaskResult(float_0, str_0, str_0)
        var_0 = task_result_0.clean_copy()
    except BaseException:
        pass

def test_case_1():
    try:
        tuple_0 = ()
        bool_0 = False
        set_0 = {tuple_0, bool_0}
        bytes_0 = b'?\x1b-\xb9'
        str_0 = ''
        task_result_0 = module_0.TaskResult(set_0, bytes_0, str_0)
        var_0 = task_result_0.is_changed()
    except BaseException:
        pass

def test_case_2():
    try:
        tuple_0 = ()
        bool_0 = False
        set_0 = {tuple_0, bool_0}
        bytes_0 = b'?\x1b-\xb9'
        str_0 = ''
        task_result_0 = module_0.TaskResult(set_0, bytes_0, str_0)
        var_0 = task_result_0.is_unreachable()
    except BaseException:
        pass

def test_case_3():
    try:
        list_0 = None
        int_0 = 521
        str_0 = 'nE.=\x0b\\\x0bW4Ar'
        str_1 = 'w\rdm|gW70kDZN1y-}'
        bool_0 = False
        task_result_0 = module_0.TaskResult(int_0, str_0, str_1, bool_0)
        var_0 = task_result_0.needs_debugger(list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'\xdc"'
        bytes_1 = b'5\xaeMz\xe0\x89s)h[\x14\xf9\xda\xa0\xe6'
        set_0 = {bytes_1, bytes_1}
        str_0 = "tg>&\rh'z,g*"
        task_result_0 = module_0.TaskResult(bytes_0, set_0, str_0)
        var_0 = task_result_0.is_skipped()
    except BaseException:
        pass

def test_case_5():
    try:
        tuple_0 = ()
        bool_0 = False
        set_0 = {tuple_0, bool_0}
        str_0 = ''
        bytes_0 = None
        task_result_0 = module_0.TaskResult(set_0, bytes_0, str_0, bytes_0)
        var_0 = task_result_0.clean_copy()
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = ''
        complex_0 = None
        str_1 = '=Alp&w,'
        float_0 = -1858.9712
        task_result_0 = module_0.TaskResult(complex_0, str_0, str_1, float_0)
        var_0 = task_result_0.clean_copy()
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'localhost'
        str_1 = 'setup'
        str_2 = ''
        int_0 = 1
        int_1 = {str_2: int_0}
        int_2 = {str_1: int_1}
        str_3 = 'name'
        str_4 = 'debugger'
        str_5 = 'on_failed'
        str_6 = {str_3: str_1, str_4: str_5}
        task_result_0 = module_0.TaskResult(str_0, str_1, int_2, str_6)
        bool_0 = True
        var_0 = task_result_0.needs_debugger(bool_0)
        str_7 = 'failed'
        bool_1 = True
        bool_2 = False
        bool_3 = {str_7: bool_1, str_4: bool_2}
        bool_4 = {str_1: bool_3}
        task_result_1 = module_0.TaskResult(str_0, str_1, bool_4, str_0)
        bool_5 = True
        var_1 = task_result_1.needs_debugger(bool_5)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'always'
        bool_0 = True
        var_0 = dict(debugger=str_0, ignore_errors=bool_0)
        var_1 = dict()
        task_result_0 = module_0.TaskResult(str_0, var_1, str_0, var_0)
        bool_1 = False
        var_2 = task_result_0.needs_debugger(bool_1)
        task_result_1 = module_0.TaskResult(bool_1, var_1, bool_1, var_0)
    except BaseException:
        pass