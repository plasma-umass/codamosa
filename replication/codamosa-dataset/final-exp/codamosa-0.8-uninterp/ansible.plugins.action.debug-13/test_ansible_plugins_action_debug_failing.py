# Automatically generated by Pynguin.
import ansible.plugins.action.debug as module_0

def test_case_0():
    try:
        str_0 = 'bT#cWyr\x0cu|=JU'
        float_0 = 1.0
        dict_0 = {float_0: str_0, str_0: str_0, float_0: float_0, float_0: str_0}
        int_0 = 8
        str_1 = None
        set_0 = {str_0, str_1, int_0}
        action_module_0 = module_0.ActionModule(str_0, float_0, dict_0, int_0, int_0, set_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = {}
        list_0 = []
        int_0 = 1777
        str_0 = 'PI'
        set_0 = {str_0, int_0, str_0, str_0}
        complex_0 = None
        str_1 = 'gentoo-release'
        bool_0 = False
        tuple_0 = ()
        bool_1 = True
        action_module_0 = module_0.ActionModule(list_0, bool_0, tuple_0, dict_0, tuple_0, bool_1)
        action_module_1 = module_0.ActionModule(str_0, list_0, set_0, complex_0, dict_0, str_1)
        float_0 = -1688.693156
        bool_2 = False
        var_0 = action_module_1.run(float_0, bool_2)
    except BaseException:
        pass