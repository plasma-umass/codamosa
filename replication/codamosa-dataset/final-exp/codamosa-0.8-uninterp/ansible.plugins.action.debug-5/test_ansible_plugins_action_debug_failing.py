# Automatically generated by Pynguin.
import ansible.plugins.action.debug as module_0

def test_case_0():
    try:
        tuple_0 = ()
        bytes_0 = b'\xbc\x8cf!\x9c'
        str_0 = 'MFz9Zzv/fk\n'
        bool_0 = True
        action_module_0 = module_0.ActionModule(tuple_0, bytes_0, str_0, bool_0, str_0, bytes_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '0aNO-`4\nX6'
        dict_0 = {str_0: str_0}
        int_0 = -1024
        int_1 = 365
        set_0 = {int_0}
        str_1 = '1\x0cjJ\\l0'
        str_2 = 'T`\x0bp?PAO_Gc'
        bool_0 = True
        set_1 = {bool_0, bool_0}
        str_3 = 'wb+'
        str_4 = '1bv0\nY_|-Q'
        action_module_0 = module_0.ActionModule(dict_0, dict_0, set_1, str_3, str_4, str_2)
        str_5 = 'hnV5fYvHocAGxc#Q LO'
        list_0 = [str_5, str_0]
        bytes_0 = b'\x1d\x1a\xca\x85\xc0\x03\x11\xdc\x95\xdc\x08'
        action_module_1 = module_0.ActionModule(dict_0, str_5, list_0, bytes_0, list_0, dict_0)
        action_module_2 = module_0.ActionModule(str_2, set_1, action_module_0, action_module_0, action_module_1, set_1)
        float_0 = 1774.0
        action_module_3 = module_0.ActionModule(str_1, action_module_2, dict_0, list_0, float_0, bool_0)
        var_0 = action_module_3.run(int_1, set_0)
    except BaseException:
        pass