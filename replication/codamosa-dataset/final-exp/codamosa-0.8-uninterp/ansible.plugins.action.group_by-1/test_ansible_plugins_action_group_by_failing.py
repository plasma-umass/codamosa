# Automatically generated by Pynguin.
import ansible.plugins.action.group_by as module_0

def test_case_0():
    try:
        bytes_0 = b'\x8b\xb4\xe8'
        bytes_1 = None
        dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_1}
        int_0 = -1561
        bytes_2 = b'\xf3\xc5B\xcbz\xd5'
        list_0 = [bytes_0]
        str_0 = 'VcCn56"'
        action_module_0 = module_0.ActionModule(bytes_0, dict_0, int_0, bytes_2, list_0, str_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        bytes_0 = b'\xbfkv'
        str_0 = 'bxS'
        str_1 = 'absent'
        str_2 = 'zJ(}1>>^'
        str_3 = '1\t'
        str_4 = '$wnssZ^B=;k'
        dict_0 = {str_4: str_4, bool_0: str_3}
        float_0 = None
        bytes_1 = b'\\\xf6f\xe0\x82'
        action_module_0 = module_0.ActionModule(str_3, str_4, dict_0, float_0, dict_0, bytes_1)
        tuple_0 = (action_module_0, action_module_0, str_1, float_0)
        action_module_1 = module_0.ActionModule(str_1, str_2, tuple_0, tuple_0, dict_0, float_0)
        var_0 = action_module_1.run(bytes_0, str_0)
    except BaseException:
        pass