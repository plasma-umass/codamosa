# Automatically generated by Pynguin.
import ansible.plugins.action.set_stats as module_0

def test_case_0():
    try:
        int_0 = 5334
        set_0 = set()
        str_0 = "B{EOV(F3uSc]'NoJY{"
        bool_0 = False
        str_1 = '>$'
        dict_0 = {int_0: str_0, int_0: str_0, bool_0: bool_0, int_0: str_1}
        tuple_0 = (bool_0, set_0, dict_0)
        float_0 = -1981.1
        str_2 = '}e\\T'
        list_0 = [str_0, str_2, int_0]
        str_3 = 'm S-:k1,TL\\%B`'
        action_module_0 = module_0.ActionModule(str_2, list_0, str_3, float_0, set_0, str_1)
        action_module_1 = module_0.ActionModule(int_0, set_0, str_0, tuple_0, int_0, float_0)
        var_0 = action_module_1.run()
    except BaseException:
        pass

def test_case_1():
    try:
        complex_0 = None
        bool_0 = True
        bytes_0 = b'B'
        bool_1 = False
        str_0 = 'E[kG0S*'
        list_0 = [bool_1, bytes_0, bytes_0]
        int_0 = None
        int_1 = 4116
        str_1 = '!);"W}2j9@xO2w('
        float_0 = -3214.0
        action_module_0 = module_0.ActionModule(int_0, int_1, str_1, float_0, int_1, int_0)
        tuple_0 = (action_module_0,)
        tuple_1 = (tuple_0, tuple_0, action_module_0)
        float_1 = 674.2363
        action_module_1 = module_0.ActionModule(bytes_0, bool_1, str_0, list_0, tuple_1, float_1)
        var_0 = action_module_1.run(complex_0, bool_0)
    except BaseException:
        pass