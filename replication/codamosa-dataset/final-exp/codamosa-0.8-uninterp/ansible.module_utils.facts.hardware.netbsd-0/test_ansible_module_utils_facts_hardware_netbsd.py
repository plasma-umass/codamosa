# Automatically generated by Pynguin.
import ansible.module_utils.facts.hardware.netbsd as module_0

def test_case_0():
    net_b_s_d_hardware_collector_0 = module_0.NetBSDHardwareCollector()

def test_case_1():
    bytes_0 = b'\xf4Fvg\xa05\x0e\xcd\xed6\x0e\xb6\x8d\x94\xa9\x94\xd2\xd4'
    set_0 = {bytes_0}
    net_b_s_d_hardware_0 = module_0.NetBSDHardware(set_0)
    var_0 = net_b_s_d_hardware_0.get_cpu_facts()

def test_case_2():
    tuple_0 = ()
    net_b_s_d_hardware_0 = module_0.NetBSDHardware(tuple_0)
    var_0 = net_b_s_d_hardware_0.get_memory_facts()