# Automatically generated by Pynguin.
import ansible.plugins.action.copy as module_0

def test_case_0():
    try:
        int_0 = 149
        float_0 = -100.731
        float_1 = -1522.9
        bytes_0 = b'|m\nx\xbf~\xa9J<'
        action_module_0 = module_0.ActionModule(int_0, float_0, float_0, float_1, bytes_0, int_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 512.0
        set_0 = {float_0, float_0}
        bytes_0 = b'K\x853X/\xbc\xd4\x85\xc3\xd6\x19\xe3\xca>8D\x85=\xd0\xaf'
        dict_0 = {}
        str_0 = 'c\x0cGq^\x0cg'
        list_0 = []
        list_1 = [set_0, list_0, set_0, bytes_0]
        bytes_1 = b'\xb3Hf\x8e^},\x8c\xb2\xd8F'
        int_0 = 656000
        bool_0 = False
        action_module_0 = module_0.ActionModule(list_1, bytes_1, int_0, bool_0, int_0, list_0)
        var_0 = action_module_0.run(dict_0, str_0)
    except BaseException:
        pass