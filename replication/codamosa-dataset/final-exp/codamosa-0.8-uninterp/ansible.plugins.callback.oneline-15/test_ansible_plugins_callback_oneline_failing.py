# Automatically generated by Pynguin.
import ansible.plugins.callback.oneline as module_0

def test_case_0():
    try:
        bytes_0 = None
        int_0 = -388
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_failed(bytes_0, int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '"3$-.PS yk5*T\tx\\t*,'
        tuple_0 = ()
        list_0 = [tuple_0, str_0, str_0]
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_ok(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = ''
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_unreachable(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'Lo\x85\x99\x85w\x0fb\x99\xa3\xa2\xadz'
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_skipped(bytes_0)
    except BaseException:
        pass