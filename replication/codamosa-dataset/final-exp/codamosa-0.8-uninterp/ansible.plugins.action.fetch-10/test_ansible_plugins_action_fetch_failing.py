# Automatically generated by Pynguin.
import ansible.plugins.action.fetch as module_0

def test_case_0():
    try:
        tuple_0 = None
        dict_0 = {tuple_0: tuple_0, tuple_0: tuple_0}
        int_0 = 2333
        set_0 = {tuple_0}
        bool_0 = True
        action_module_0 = module_0.ActionModule(dict_0, int_0, set_0, bool_0, dict_0, tuple_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = "group vars, precedence entry '%s'"
        dict_0 = {str_0: str_0, str_0: str_0}
        tuple_0 = (str_0, dict_0, dict_0, str_0)
        str_1 = '<?~E \rfl@zXz'
        int_0 = -2872
        bytes_0 = b'\xbb\xd6B\xaf\xde\xcb;\t'
        str_2 = 'E'
        float_0 = 623.4
        list_0 = [str_1, tuple_0, tuple_0, str_0]
        bytes_1 = None
        action_module_0 = module_0.ActionModule(str_0, float_0, list_0, dict_0, bytes_1, dict_0)
        bool_0 = False
        action_module_1 = module_0.ActionModule(bytes_0, bytes_0, int_0, bool_0, bytes_0, dict_0)
        var_0 = action_module_1.run(str_2, action_module_0)
    except BaseException:
        pass