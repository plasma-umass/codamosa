# Automatically generated by Pynguin.
import ansible.plugins.action.include_vars as module_0
import ansible.errors as module_1

def test_case_0():
    try:
        tuple_0 = ()
        str_0 = '!KC_39[\\U)Zv\\f'
        bytes_0 = b'\x17O;!\x95K'
        action_module_0 = module_0.ActionModule(tuple_0, str_0, str_0, tuple_0, tuple_0, bytes_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 50
        set_0 = {int_0, int_0}
        bool_0 = False
        str_0 = '/*.fact'
        tuple_0 = (set_0, str_0, str_0)
        action_module_0 = None
        float_0 = None
        str_1 = '|(Zf+d\r!_~da'
        dict_0 = {}
        str_2 = 'v\tuyqf Z+EXH<_W"\rV'
        float_1 = -1695.19994
        action_module_1 = module_0.ActionModule(str_0, set_0, bool_0, float_1, set_0, int_0)
        float_2 = -3477.0
        int_1 = 2545
        action_module_2 = module_0.ActionModule(str_2, action_module_0, tuple_0, int_0, float_2, int_1)
        bool_1 = False
        action_module_3 = module_0.ActionModule(action_module_0, float_0, str_1, dict_0, bool_0, bool_1)
        tuple_1 = ()
        list_0 = [action_module_2, tuple_1, tuple_1, action_module_2]
        var_0 = action_module_3.run(set_0, list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        ansible_error_0 = module_1.AnsibleError()
        int_0 = 655979
        list_0 = [ansible_error_0, int_0, int_0]
        str_0 = 't'
        action_module_0 = module_0.ActionModule(int_0, str_0, int_0, int_0, list_0, list_0)
        action_module_1 = module_0.ActionModule(ansible_error_0, int_0, int_0, list_0, action_module_0, str_0)
        var_0 = action_module_1.run()
    except BaseException:
        pass