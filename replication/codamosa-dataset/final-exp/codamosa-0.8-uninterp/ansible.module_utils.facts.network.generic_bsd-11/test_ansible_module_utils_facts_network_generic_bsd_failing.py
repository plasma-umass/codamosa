# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.generic_bsd as module_0

def test_case_0():
    try:
        int_0 = -1302
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(int_0)
        str_0 = 'O3\x0cmAxeWBP&H2]:K23J '
        str_1 = 'i28:.bS/*'
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(str_0, str_1)
        var_0 = generic_bsd_ifconfig_network_1.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'VW%aym\x0bTF"Z>SK z\\B'
        str_1 = 'TERM'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_1)
        var_0 = generic_bsd_ifconfig_network_0.detect_type_media(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 2569.52977
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(float_0)
        var_0 = generic_bsd_ifconfig_network_0.get_default_interfaces(float_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '_raw'
        int_0 = -840
        complex_0 = None
        dict_0 = {int_0: str_0, complex_0: str_0, str_0: int_0, complex_0: complex_0}
        bool_0 = False
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0)
        float_0 = 0.2
        var_0 = generic_bsd_ifconfig_network_0.merge_default_interface(dict_0, generic_bsd_ifconfig_network_0, float_0)
        bytes_0 = None
        str_1 = '?'
        set_0 = {var_0, str_1, float_0}
        tuple_0 = (str_1, dict_0, dict_0, set_0)
        str_2 = 'releaselevel'
        var_1 = generic_bsd_ifconfig_network_0.parse_ether_line(tuple_0, dict_0, str_2)
        var_2 = generic_bsd_ifconfig_network_0.get_interfaces_info(bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'mzmKjCJN3'
        bool_0 = None
        float_0 = -836.68
        list_0 = [str_0, str_0]
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(list_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_options_line(bool_0, float_0, bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = "pPA'\r!\ttC]6s"
        bool_0 = True
        int_0 = -794
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0, int_0)
        bytes_0 = b'V\xc3\xe3\xef\x0bP\xdd\x8bO\xb84\x1bH\xcb\xc0\xe9\xac\x89'
        var_0 = generic_bsd_ifconfig_network_0.get_options(str_0)
        str_1 = ''
        list_0 = [str_1, bytes_0]
        int_1 = None
        tuple_0 = (bytes_0, str_1, list_0, int_1)
        tuple_1 = None
        float_0 = 1134.3738
        list_1 = []
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(list_1)
        var_1 = generic_bsd_ifconfig_network_1.parse_nd6_line(tuple_0, tuple_1, float_0)
    except BaseException:
        pass

def test_case_6():
    try:
        float_0 = -1149.651
        dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0, float_0: float_0}
        list_0 = []
        float_1 = 593.786
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(float_1)
        var_0 = generic_bsd_ifconfig_network_0.parse_media_line(float_0, dict_0, list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = None
        int_0 = -1512
        set_0 = {int_0, bool_0, bool_0}
        bytes_0 = b'0\x91\xb7sc\xa1\x11;\x1fc'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bytes_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_status_line(bool_0, int_0, set_0)
    except BaseException:
        pass

def test_case_8():
    try:
        generic_bsd_ifconfig_network_0 = None
        bool_0 = None
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(generic_bsd_ifconfig_network_0, bool_0)
        float_0 = -1842.22733
        str_0 = 'i586'
        tuple_0 = ()
        set_0 = set()
        tuple_1 = (tuple_0, str_0, float_0, set_0)
        bytes_0 = b'\xaci\xee\xb6\x83$g\x83\xea\x83\x8e\xfc<'
        tuple_2 = (float_0, str_0, tuple_1, bytes_0)
        float_1 = 0.0
        bytes_1 = b'\xbcl\xb9'
        generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(bytes_1)
        var_0 = generic_bsd_ifconfig_network_2.parse_lladdr_line(generic_bsd_ifconfig_network_1, tuple_2, float_1)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'tI)Xa;e^7>*'
        bool_0 = False
        list_0 = [bool_0]
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_inet_line(str_0, bool_0, list_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'check_mode_markers'
        dict_0 = {}
        bool_0 = True
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_inet6_line(str_0, dict_0, bool_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = None
        str_1 = 'end'
        str_2 = '\x0b{`9$h>KI'
        bytes_0 = b'\x08\xaf\xa6^*\xa4\xc7\t\xe7\xe1\x7f\xb5!m6'
        list_0 = [bytes_0, bytes_0, bytes_0]
        int_0 = 125
        tuple_0 = (list_0, int_0)
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bytes_0, tuple_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_tunnel_line(str_0, str_1, str_2)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '>Z'
        int_0 = -1815
        set_0 = {str_0, int_0, int_0, int_0}
        int_1 = 636
        bool_0 = False
        dict_0 = {int_1: bool_0, int_1: int_1, bool_0: bool_0, int_1: int_1}
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(dict_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_inet6_line(str_0, int_0, set_0)
    except BaseException:
        pass

def test_case_13():
    try:
        bool_0 = True
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0)
        str_0 = 'Z0-eY#'
        bool_1 = False
        set_0 = {bool_0}
        var_0 = generic_bsd_ifconfig_network_0.parse_inet_line(str_0, bool_1, set_0)
    except BaseException:
        pass

def test_case_14():
    try:
        tuple_0 = ()
        str_0 = '//'
        str_1 = '*%E)F5VC-LfC'
        int_0 = -501
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(int_0)
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(generic_bsd_ifconfig_network_0)
        var_0 = generic_bsd_ifconfig_network_1.parse_inet_line(str_0, str_1, tuple_0)
    except BaseException:
        pass

def test_case_15():
    try:
        int_0 = -738
        tuple_0 = ()
        str_0 = 'action_groups'
        bool_0 = True
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(tuple_0, bool_0)
        str_1 = '5<uG?a6%zZ'
        var_0 = generic_bsd_ifconfig_network_0.parse_interface_line(str_1)
        list_0 = [tuple_0, generic_bsd_ifconfig_network_0]
        str_2 = 'Z0-eY#'
        var_1 = generic_bsd_ifconfig_network_0.merge_default_interface(str_2, str_0, generic_bsd_ifconfig_network_0)
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(list_0)
        str_3 = 'auth__rl'
        dict_0 = {str_3: str_3, int_0: tuple_0}
        var_2 = generic_bsd_ifconfig_network_0.detect_type_media(dict_0)
        bool_1 = False
        var_3 = generic_bsd_ifconfig_network_1.parse_unknown_line(dict_0, bool_1, generic_bsd_ifconfig_network_1)
        float_0 = -1864.5
        var_4 = generic_bsd_ifconfig_network_1.parse_media_line(list_0, dict_0, float_0)
        float_1 = -4074.168
        var_5 = generic_bsd_ifconfig_network_1.merge_default_interface(dict_0, float_1, list_0)
        var_6 = generic_bsd_ifconfig_network_0.get_default_interfaces(tuple_0)
    except BaseException:
        pass

def test_case_16():
    try:
        var_0 = None
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(var_0)
        str_0 = 'interface'
        str_1 = 'address'
        str_2 = 'lo0'
        str_3 = '0.0.0.0'
        str_4 = {str_0: str_2, str_1: str_3}
        str_5 = 'ipv6'
        str_6 = [str_4]
        str_7 = {str_0: str_6, str_5: str_1}
        str_8 = {str_2: str_7}
        var_1 = generic_bsd_ifconfig_network_0.merge_default_interface(str_4, str_8, str_8)
    except BaseException:
        pass

def test_case_17():
    try:
        var_0 = None
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(var_0)
        str_0 = 'interface'
        str_1 = 'addess'
        str_2 = 'lo0'
        str_3 = {str_0: str_2, str_1: str_1}
        str_4 = 'ipv4'
        str_5 = 'ipv6'
        str_6 = [str_5]
        str_7 = '(::1'
        str_8 = {str_1: str_7}
        str_9 = [str_8]
        str_10 = {str_4: str_6, str_5: str_9}
        str_11 = {str_2: str_10}
        var_1 = generic_bsd_ifconfig_network_0.merge_default_interface(str_3, str_11, str_4)
    except BaseException:
        pass