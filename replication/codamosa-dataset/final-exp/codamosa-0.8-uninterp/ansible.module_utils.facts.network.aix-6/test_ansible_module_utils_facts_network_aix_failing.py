# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.aix as module_0

def test_case_0():
    try:
        str_0 = 'R4CIbq '
        a_i_x_network_0 = module_0.AIXNetwork(str_0)
        dict_0 = {}
        a_i_x_network_collector_0 = module_0.AIXNetworkCollector(dict_0)
        var_0 = a_i_x_network_0.get_default_interfaces(a_i_x_network_collector_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b')\xe6w3*z\x7f`'
        bool_0 = True
        a_i_x_network_0 = module_0.AIXNetwork(bool_0)
        var_0 = a_i_x_network_0.get_interfaces_info(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        list_0 = []
        a_i_x_network_0 = module_0.AIXNetwork(bool_0, list_0)
        float_0 = -1910.039
        var_0 = a_i_x_network_0.parse_interface_line(float_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = "'9<eC"
        bytes_0 = b'\xe8\xb5(v$:U[I\x93\x1e'
        a_i_x_network_0 = module_0.AIXNetwork(bytes_0)
        a_i_x_network_collector_0 = module_0.AIXNetworkCollector()
        a_i_x_network_1 = module_0.AIXNetwork(a_i_x_network_0, a_i_x_network_collector_0)
        var_0 = a_i_x_network_1.parse_interface_line(str_0)
        a_i_x_network_collector_1 = module_0.AIXNetworkCollector()
        dict_0 = {}
        a_i_x_network_2 = module_0.AIXNetwork(dict_0)
        var_1 = a_i_x_network_2.parse_interface_line(a_i_x_network_collector_1)
    except BaseException:
        pass