# Automatically generated by Pynguin.
import ansible.plugins.action.fail as module_0

def test_case_0():
    try:
        float_0 = 1692.0
        bool_0 = True
        bytes_0 = b'9E\x8d\x95\xe64\x99Y8\xe7\x04k7\x00\x1a3U'
        float_1 = 1.5
        list_0 = []
        action_module_0 = module_0.ActionModule(float_0, bool_0, bytes_0, float_0, float_1, list_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        tuple_0 = ()
        str_0 = '(k\x0c>ew54'
        bytes_0 = b'\xbc+\xe4"\x9f\x1dyh\x95v\xd7"'
        str_1 = 'j'
        int_0 = -2407
        str_2 = 'R1:]X+C%k(9\x0c)hyhe ^v'
        bytes_1 = b'\xa8'
        action_module_0 = module_0.ActionModule(bytes_0, str_0, str_1, int_0, str_2, bytes_1)
        dict_0 = {tuple_0: str_0}
        set_0 = {action_module_0, int_0}
        var_0 = action_module_0.run(dict_0, set_0)
    except BaseException:
        pass