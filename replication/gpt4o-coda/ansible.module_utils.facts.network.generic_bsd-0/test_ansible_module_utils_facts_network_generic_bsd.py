# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.generic_bsd as module_0

def test_case_0():
    str_0 = '3Y* >iHTMm;\t=un@ESz'
    float_0 = 1257.439519438273
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(float_0)
    tuple_0 = ()
    dict_0 = {float_0: tuple_0, generic_bsd_ifconfig_network_0: str_0}
    var_0 = generic_bsd_ifconfig_network_0.detect_type_media(dict_0)

def test_case_1():
    str_0 = '--security'
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
    var_0 = generic_bsd_ifconfig_network_0.parse_interface_line(str_0)

def test_case_2():
    str_0 = '8\r!9U'
    bytes_0 = b'\xc4\xcf\x19;\xff\xb8\x9fl{<\x8e=Sxa'
    dict_0 = {bytes_0: str_0, str_0: bytes_0}
    bool_0 = False
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0)
    list_0 = None
    tuple_0 = (list_0,)
    float_0 = 1.5
    int_0 = 1071
    var_0 = generic_bsd_ifconfig_network_0.parse_unknown_line(tuple_0, float_0, int_0)
    var_1 = generic_bsd_ifconfig_network_0.parse_nd6_line(str_0, dict_0, dict_0)

def test_case_3():
    str_0 = 'vFD]-x&qt?'
    bool_0 = True
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
    var_0 = generic_bsd_ifconfig_network_0.merge_default_interface(str_0, bool_0, generic_bsd_ifconfig_network_0)

def test_case_4():
    str_0 = 'r<MsYW'
    bool_0 = False
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0, str_0)
    var_0 = generic_bsd_ifconfig_network_0.get_options(str_0)

def test_case_5():
    float_0 = 1257.43952
    generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(float_0)
    tuple_0 = ()
    var_0 = generic_bsd_ifconfig_network_0.detect_type_media(tuple_0)
    str_0 = '`:1'
    set_0 = {str_0, str_0}
    str_1 = 'i~nN>,l'
    var_1 = generic_bsd_ifconfig_network_0.parse_interface_line(str_1)
    str_2 = '4'
    generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(str_2)
    bool_0 = False
    str_3 = '}.n*\x0c>p:K16<wjWM'
    var_2 = generic_bsd_ifconfig_network_1.get_options(str_3)
    generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(set_0)
    generic_bsd_ifconfig_network_3 = module_0.GenericBsdIfconfigNetwork(generic_bsd_ifconfig_network_1)
    str_4 = '1\rX^+~$hQpB(`yIiDL'
    var_3 = generic_bsd_ifconfig_network_2.merge_default_interface(str_4, set_0, bool_0)