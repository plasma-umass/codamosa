# Automatically generated by Pynguin.
import ansible.modules.systemd as module_0

def test_case_0():
    try:
        int_0 = 82
        var_0 = module_0.is_running_service(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 2933.0057
        var_0 = module_0.is_deactivating_service(float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = None
        var_0 = module_0.parse_systemctl_show(bytes_0)
    except BaseException:
        pass