# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.netbsd as module_0

def test_case_0():
    pass

def test_case_1():
    var_0 = {}
    net_b_s_d_hardware_0 = module_0.NetBSDHardware(var_0)
    var_1 = net_b_s_d_hardware_0.get_cpu_facts()

def test_case_2():
    str_0 = '?Rz0Oxv~(nBl\n)/OVU'
    net_b_s_d_hardware_0 = module_0.NetBSDHardware(str_0)
    var_0 = net_b_s_d_hardware_0.get_memory_facts()