# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.sunos as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'iMh5c\\|DDFAM\t'
    set_0 = {str_0}
    sun_o_s_network_0 = module_0.SunOSNetwork(set_0, str_0)
    var_0 = sun_o_s_network_0.parse_interface_line(str_0, str_0, set_0)