# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.darwin as module_0

def test_case_0():
    try:
        bytes_0 = b'\xa2'
        str_0 = 'Q^>MiFbL;n\\ux\nCw:F'
        list_0 = [str_0]
        set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
        darwin_hardware_0 = module_0.DarwinHardware(set_0)
        var_0 = darwin_hardware_0.populate(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = {}
        darwin_hardware_0 = module_0.DarwinHardware(dict_0)
        var_0 = darwin_hardware_0.get_system_profile()
    except BaseException:
        pass

def test_case_2():
    try:
        darwin_hardware_collector_0 = module_0.DarwinHardwareCollector()
        bytes_0 = b'\x8c\x98f\xe3\x03\xdd\xef'
        tuple_0 = ()
        tuple_1 = (bytes_0, tuple_0)
        darwin_hardware_0 = module_0.DarwinHardware(tuple_1)
        darwin_hardware_1 = module_0.DarwinHardware(darwin_hardware_collector_0, darwin_hardware_0)
        var_0 = darwin_hardware_1.get_mac_facts()
    except BaseException:
        pass

def test_case_3():
    try:
        tuple_0 = ()
        set_0 = {tuple_0}
        darwin_hardware_0 = module_0.DarwinHardware(set_0)
        var_0 = darwin_hardware_0.get_cpu_facts()
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = -1724
        int_1 = -2215
        bytes_0 = None
        dict_0 = {int_1: int_0, int_0: int_1, int_0: bytes_0, int_1: int_1}
        darwin_hardware_0 = module_0.DarwinHardware(int_1, dict_0)
        var_0 = darwin_hardware_0.get_memory_facts()
    except BaseException:
        pass

def test_case_5():
    try:
        darwin_hardware_collector_0 = module_0.DarwinHardwareCollector()
        int_0 = 1024
        bool_0 = False
        tuple_0 = (darwin_hardware_collector_0, int_0, bool_0)
        set_0 = {int_0, bool_0, bool_0, int_0}
        darwin_hardware_0 = module_0.DarwinHardware(tuple_0, set_0)
        var_0 = darwin_hardware_0.get_uptime_facts()
    except BaseException:
        pass