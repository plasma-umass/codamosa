# Automatically generated by Pynguin.
import ansible.plugins.action.wait_for_connection as module_0

def test_case_0():
    try:
        int_0 = None
        timed_out_exception_0 = module_0.TimedOutException()
        float_0 = -1273.6
        str_0 = 'nevra'
        str_1 = '#,3Q'
        dict_0 = {str_0: int_0, str_1: float_0}
        float_1 = -1658.0733
        bytes_0 = b''
        dict_1 = {int_0: int_0}
        list_0 = [dict_1, dict_1]
        bool_0 = False
        list_1 = [bool_0, int_0, list_0]
        action_module_0 = module_0.ActionModule(dict_1, list_0, dict_1, bool_0, dict_1, list_1)
        var_0 = action_module_0.do_until_success_or_timeout(timed_out_exception_0, float_0, dict_0, float_1, bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        timed_out_exception_0 = module_0.TimedOutException()
        set_0 = {timed_out_exception_0, timed_out_exception_0, timed_out_exception_0}
        bool_0 = False
        bool_1 = True
        list_0 = [bool_0, timed_out_exception_0]
        action_module_0 = module_0.ActionModule(timed_out_exception_0, set_0, bool_0, set_0, bool_1, list_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = None
        set_0 = {int_0, int_0, int_0}
        float_0 = 0.1
        timed_out_exception_0 = module_0.TimedOutException()
        bytes_0 = b'\n\x810\xa0\x19\x1fm\xca\x16\xb9D.'
        str_0 = ';t%qbVTQ\t8'
        int_1 = -1758
        str_1 = 'SUhQL\\\ngF8MG>z(TR'
        str_2 = '!QOjZ4{i4fJ\nH"}*F\tq.'
        str_3 = '/>m9Av\'"Si\n\\FMux'
        dict_0 = {str_1: str_1, str_2: int_1, str_3: int_1, str_0: str_3}
        str_4 = 'H;DO'
        int_2 = 196
        bool_0 = True
        action_module_0 = module_0.ActionModule(str_0, int_1, dict_0, str_4, int_2, bool_0)
        var_0 = action_module_0.do_until_success_or_timeout(set_0, float_0, timed_out_exception_0, bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        action_module_0 = None
        set_0 = {action_module_0, action_module_0, action_module_0, action_module_0}
        list_0 = [set_0]
        dict_0 = {}
        timed_out_exception_0 = module_0.TimedOutException(*list_0, **dict_0)
        list_1 = [list_0]
        str_0 = 'n_\x0c?.jPI$d)*a)A%k+'
        float_0 = -2341.255
        bytes_0 = b"\x17\x85jM\x92\xa7\xa13C\xb6\x14'\\:\xdc\x9f\xed\xef|"
        dict_1 = {bytes_0: set_0}
        action_module_1 = module_0.ActionModule(set_0, action_module_0, bytes_0, dict_1, timed_out_exception_0, list_1)
        var_0 = action_module_1.run(str_0, float_0)
    except BaseException:
        pass