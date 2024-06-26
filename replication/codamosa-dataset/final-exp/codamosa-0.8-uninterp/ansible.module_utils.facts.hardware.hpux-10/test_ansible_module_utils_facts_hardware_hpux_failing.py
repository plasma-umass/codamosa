# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.hpux as module_0

def test_case_0():
    try:
        bool_0 = True
        h_p_u_x_hardware_0 = module_0.HPUXHardware(bool_0)
        var_0 = h_p_u_x_hardware_0.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xbd\xc4\xfa\xdfl\x0e\xf7\x9b\xe3\x11\xe4\x86\x01\xd6'
        h_p_u_x_hardware_0 = module_0.HPUXHardware(bytes_0)
        var_0 = h_p_u_x_hardware_0.get_memory_facts()
    except BaseException:
        pass

def test_case_2():
    try:
        tuple_0 = ()
        set_0 = {tuple_0, tuple_0}
        list_0 = [set_0, set_0, tuple_0, tuple_0]
        h_p_u_x_hardware_0 = module_0.HPUXHardware(set_0, list_0)
        var_0 = h_p_u_x_hardware_0.get_hw_facts()
    except BaseException:
        pass

def test_case_3():
    try:
        list_0 = []
        list_1 = [list_0, list_0]
        h_p_u_x_hardware_collector_0 = module_0.HPUXHardwareCollector()
        h_p_u_x_hardware_0 = module_0.HPUXHardware(h_p_u_x_hardware_collector_0)
        var_0 = h_p_u_x_hardware_0.get_cpu_facts(list_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '6u[xI'
        dict_0 = {}
        h_p_u_x_hardware_0 = module_0.HPUXHardware(dict_0)
        var_0 = h_p_u_x_hardware_0.get_cpu_facts()
        float_0 = 327.92
        set_0 = {float_0, float_0, float_0}
        list_0 = [set_0]
        h_p_u_x_hardware_1 = module_0.HPUXHardware(list_0, list_0)
        var_1 = h_p_u_x_hardware_1.get_memory_facts(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = -872.00082
        set_0 = {float_0, float_0, float_0, float_0}
        dict_0 = {}
        h_p_u_x_hardware_0 = module_0.HPUXHardware(dict_0)
        var_0 = h_p_u_x_hardware_0.get_hw_facts(set_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'ansible_architecture'
        str_1 = 'ansible_distribution_version'
        str_2 = '9000/800'
        str_3 = 'B.11.23'
        str_4 = {str_0: str_2, str_1: str_3}
        var_0 = None
        h_p_u_x_hardware_0 = module_0.HPUXHardware(var_0)
        var_1 = h_p_u_x_hardware_0.get_cpu_facts(str_4)
    except BaseException:
        pass