# Automatically generated by Pynguin.
import ansible.plugins.action.set_fact as module_0

def test_case_0():
    try:
        tuple_0 = ()
        int_0 = 254
        list_0 = [tuple_0, int_0, int_0]
        str_0 = 'Auto-installing missing dependency without updating cache: %s'
        action_module_0 = module_0.ActionModule(tuple_0, int_0, int_0, list_0, tuple_0, str_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b''
        str_0 = '"'
        float_0 = -2002.384261
        str_1 = '?QY([]"\r'
        dict_0 = {float_0: float_0, str_1: float_0, str_1: str_1, float_0: float_0}
        set_0 = {float_0, str_1, float_0}
        int_0 = 340
        float_1 = 0.5
        bool_0 = True
        int_1 = 346
        str_2 = '{{CWD}}'
        bytes_1 = None
        action_module_0 = module_0.ActionModule(bool_0, int_0, int_1, str_2, bytes_1, int_0)
        bool_1 = True
        float_2 = -5633.465
        float_3 = 2412.0
        tuple_0 = (bytes_0, dict_0)
        tuple_1 = (tuple_0, dict_0)
        action_module_1 = module_0.ActionModule(float_2, bool_1, float_3, dict_0, int_0, tuple_1)
        str_3 = ';!*W'
        bytes_2 = b'\x05\x98U\x90\xe1'
        tuple_2 = (bool_1, set_0, str_3, bytes_2)
        action_module_2 = module_0.ActionModule(float_0, dict_0, set_0, int_0, float_1, tuple_2)
        var_0 = action_module_2.run(bytes_0, str_0)
    except BaseException:
        pass