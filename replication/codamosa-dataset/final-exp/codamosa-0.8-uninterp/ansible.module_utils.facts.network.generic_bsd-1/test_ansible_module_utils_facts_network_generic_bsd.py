# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.generic_bsd as module_0

def test_case_0():
    pass

def test_case_1():
    tuple_0 = ()
    float_0 = 0.001
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(float_0)
    var_0 = generic_bsd_ifconfig_network_0.detect_type_media(tuple_0)

def test_case_2():
    float_0 = -1579.72111
    tuple_0 = None
    set_0 = {float_0}
    int_0 = -4681
    list_0 = [int_0]
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(list_0, list_0)
    var_0 = generic_bsd_ifconfig_network_0.parse_unknown_line(float_0, tuple_0, set_0)

def test_case_3():
    str_0 = 'bo"\x0c9P{<%h4gX'
    bytes_0 = b'\x96o'
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0, bytes_0)
    var_0 = generic_bsd_ifconfig_network_0.get_options(str_0)

def test_case_4():
    var_0 = None
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(var_0, var_0)
    var_1 = dict()
    var_2 = dict()
    str_0 = 'ipv6'
    var_3 = generic_bsd_ifconfig_network_0.merge_default_interface(var_1, var_2, str_0)