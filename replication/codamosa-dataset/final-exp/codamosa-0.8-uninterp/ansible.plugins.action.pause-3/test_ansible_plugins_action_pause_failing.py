# Automatically generated by Pynguin.
import ansible.plugins.action.pause as module_0

def test_case_0():
    try:
        int_0 = -3084
        dict_0 = None
        var_0 = module_0.timeout_handler(int_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -105
        var_0 = module_0.clear_line(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = -4837.0342
        str_0 = 'J$C)3~n'
        list_0 = [float_0, float_0, str_0]
        list_1 = [list_0]
        action_module_0 = module_0.ActionModule(float_0, float_0, str_0, list_0, list_1, list_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_3():
    try:
        var_0 = module_0.is_interactive()
        bytes_0 = b'\x84'
        list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
        str_0 = 'xs'
        str_1 = 'D9w-8o'
        str_2 = None
        dict_0 = {str_2: bytes_0}
        tuple_0 = ()
        float_0 = 100.0
        bool_0 = False
        ansible_timeout_exceeded_0 = module_0.AnsibleTimeoutExceeded()
        action_module_0 = module_0.ActionModule(str_1, dict_0, tuple_0, float_0, bool_0, ansible_timeout_exceeded_0)
        var_1 = action_module_0.run(list_0, str_0)
    except BaseException:
        pass