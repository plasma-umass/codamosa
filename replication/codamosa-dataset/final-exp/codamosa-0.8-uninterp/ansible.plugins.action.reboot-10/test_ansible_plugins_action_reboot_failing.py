# Automatically generated by Pynguin.
import ansible.plugins.action.reboot as module_0
import ansible.utils.display as module_1

def test_case_0():
    try:
        action_module_0 = module_0.ActionModule()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'gEpo'
        list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
        action_module_0 = module_0.ActionModule(*list_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = "\\$14\x0c3'%w`:LP8+"
        list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
        action_module_0 = module_0.ActionModule(*list_0)
        var_0 = action_module_0.deprecated_args()
        var_1 = action_module_0.get_system_boot_time(action_module_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'gEpo'
        list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
        action_module_0 = module_0.ActionModule(*list_0)
        set_0 = None
        var_0 = action_module_0.get_shutdown_command(str_0, set_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'gEpo'
        list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
        action_module_0 = module_0.ActionModule(*list_0)
        float_0 = -66.0
        str_1 = 'OmniOS'
        str_2 = 'cost'
        str_3 = 'cmd'
        tuple_0 = ()
        dict_0 = {str_0: action_module_0, str_1: str_2, str_3: tuple_0, str_0: action_module_0}
        list_1 = [float_0, dict_0]
        var_0 = action_module_0.run_test_command(list_1)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'gEpo'
        list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
        action_module_0 = module_0.ActionModule(*list_0)
        float_0 = -66.0
        str_1 = 'OmniOS'
        dict_0 = {str_1: float_0}
        bytes_0 = b'\xbd\x1b\x89L\xd6\xd3\x05\x18\x19\xfc\tA\xdeS\xf5\xaa9\xdb'
        var_0 = action_module_0.validate_reboot(dict_0, bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'gEpo'
        list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
        action_module_0 = module_0.ActionModule(*list_0)
        list_1 = [action_module_0, str_0]
        var_0 = action_module_0.perform_reboot(list_1, action_module_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'gEpo'
        list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
        action_module_0 = module_0.ActionModule(*list_0)
        var_0 = action_module_0.deprecated_args()
        var_1 = action_module_0.get_shutdown_command_args(list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'gEpo'
        list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
        float_0 = 872.242172
        bool_0 = True
        str_1 = 'm/]d-oy'
        list_1 = []
        dict_0 = {str_0: list_0, str_1: bool_0, str_1: list_1, str_1: str_0}
        display_0 = module_1.Display(dict_0)
        tuple_0 = (display_0,)
        action_module_0 = module_0.ActionModule(*list_0)
        var_0 = action_module_0.do_until_success_or_timeout(float_0, bool_0, tuple_0, list_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = "\\$14\x0c3'%w`:LP8+"
        list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
        action_module_0 = module_0.ActionModule(*list_0)
        var_0 = action_module_0.deprecated_args()
        timed_out_exception_0 = module_0.TimedOutException(*list_0)
        list_1 = [str_0]
        tuple_0 = (list_1,)
        var_1 = action_module_0.check_boot_time(timed_out_exception_0, tuple_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'gEpo'
        list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
        action_module_0 = module_0.ActionModule(*list_0)
        bytes_0 = b'\xd4O\xe0\x89\xff\x9a\x1c>\xed\xef'
        var_0 = action_module_0.get_distribution(bytes_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'gEpo'
        list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
        float_0 = 872.242172
        bool_0 = False
        str_1 = 'S/]d:ty'
        list_1 = []
        dict_0 = {str_0: list_0, str_1: bool_0, str_1: list_1, str_1: str_0}
        display_0 = module_1.Display(dict_0)
        tuple_0 = (display_0,)
        action_module_0 = module_0.ActionModule(*list_0)
        var_0 = action_module_0.do_until_success_or_timeout(float_0, bool_0, tuple_0, list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = "\\$14\x0c3'%w*B`:LP8+"
        list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
        action_module_0 = module_0.ActionModule(*list_0)
        str_1 = 'EG>)'
        dict_0 = {str_0: str_0, str_0: list_0, str_1: action_module_0, str_1: str_0}
        bool_0 = True
        set_0 = set()
        timed_out_exception_0 = module_0.TimedOutException()
        var_0 = action_module_0.do_until_success_or_timeout(dict_0, bool_0, set_0, set_0, timed_out_exception_0)
    except BaseException:
        pass