# Automatically generated by Pynguin.
import ansible.module_utils.facts.network.generic_bsd as module_0

def test_case_0():
    try:
        float_0 = 1985.36802
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(float_0)
        var_0 = generic_bsd_ifconfig_network_0.populate()
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        int_0 = 1138
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(int_0)
        var_0 = generic_bsd_ifconfig_network_0.detect_type_media(bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '\x0cTfZN=9BS'
        bytes_0 = b'Nb8\x9d4j\xd56R\xccpA\x16}\xc1\xd7\xe3\xf2\t\xfb'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
        var_0 = generic_bsd_ifconfig_network_0.get_default_interfaces(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = -2023.45607
        dict_0 = {float_0: float_0}
        bool_0 = None
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(dict_0)
        var_0 = generic_bsd_ifconfig_network_0.get_interfaces_info(bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'u7TAv'
        str_1 = 'v=wQ]pS{@=kgov'
        dict_0 = {str_0: str_1, str_1: str_0, str_1: str_0}
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_1, dict_0)
        list_0 = [str_0]
        set_0 = {str_1, str_1}
        int_0 = -2499
        str_2 = 'Ji\t'
        var_0 = generic_bsd_ifconfig_network_0.get_options(str_2)
        var_1 = generic_bsd_ifconfig_network_0.parse_unknown_line(dict_0, set_0, str_1)
        tuple_0 = (list_0, set_0, set_0, int_0)
        bytes_0 = b'\xd37I\xf6\x1b\x85M\x1b\xb7,\xa3na[\x98\xdb\x01'
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(generic_bsd_ifconfig_network_0)
        tuple_1 = (generic_bsd_ifconfig_network_0, tuple_0, bytes_0)
        generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(tuple_1)
        complex_0 = None
        var_2 = generic_bsd_ifconfig_network_2.parse_options_line(tuple_0, complex_0, str_2)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '5o&kFc]'
        str_1 = '_[3><$'
        dict_0 = {str_0: str_1, str_1: str_0, str_1: str_0}
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_1, dict_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_interface_line(str_1)
        var_1 = generic_bsd_ifconfig_network_0.get_options(str_1)
        complex_0 = None
        var_2 = generic_bsd_ifconfig_network_0.detect_type_media(dict_0)
        var_3 = generic_bsd_ifconfig_network_0.merge_default_interface(dict_0, complex_0, str_1)
        set_0 = {str_0, generic_bsd_ifconfig_network_0}
        str_2 = ',$'
        float_0 = None
        dict_1 = {str_2: str_2, var_3: set_0}
        str_3 = ':aTKS$$'
        dict_2 = {}
        list_0 = [str_2, var_1, complex_0, dict_2]
        tuple_0 = (dict_1, list_0, float_0)
        var_4 = generic_bsd_ifconfig_network_0.parse_nd6_line(str_3, dict_0, tuple_0)
        complex_1 = None
        var_5 = generic_bsd_ifconfig_network_0.get_default_interfaces(complex_1)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'e/nV1(_9O0o3n-(SNK=%'
        set_0 = {str_0, str_0, str_0, str_0}
        bytes_0 = b'\x0cu\xd9\xbb\xad\xc3\xee'
        float_0 = 2.0
        bool_0 = False
        tuple_0 = (set_0, bytes_0, float_0, bool_0)
        str_1 = 'N(EPY='
        dict_0 = {bool_0: str_1}
        list_0 = [str_0, str_0, str_0]
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(list_0)
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(str_0, generic_bsd_ifconfig_network_0)
        var_0 = generic_bsd_ifconfig_network_1.parse_ether_line(tuple_0, dict_0, bool_0)
        set_1 = {str_0}
        bool_1 = False
        int_0 = 947
        list_1 = [int_0, int_0]
        generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(int_0, list_1)
        int_1 = 255
        str_2 = 'q'
        generic_bsd_ifconfig_network_3 = module_0.GenericBsdIfconfigNetwork(int_1, str_2)
        var_1 = generic_bsd_ifconfig_network_3.parse_status_line(set_1, bool_1, generic_bsd_ifconfig_network_2)
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b'\x02\xc6gh\xdc\xd9\x06'
        dict_0 = {}
        str_0 = 'w|!PHhQ'
        str_1 = 'bdf%\x0cs#H,:'
        dict_1 = {str_1: str_1}
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(dict_1)
        var_0 = generic_bsd_ifconfig_network_0.parse_media_line(bytes_0, dict_0, str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = ':Vr\\Ql"{gJX~=<2xD1'
        bytes_0 = b'\x1a'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bytes_0)
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(generic_bsd_ifconfig_network_0)
        set_0 = {str_0, generic_bsd_ifconfig_network_0, generic_bsd_ifconfig_network_0, generic_bsd_ifconfig_network_0}
        list_0 = []
        generic_bsd_ifconfig_network_2 = module_0.GenericBsdIfconfigNetwork(list_0)
        bool_0 = None
        float_0 = -1670.02263
        dict_0 = {bool_0: float_0}
        generic_bsd_ifconfig_network_3 = module_0.GenericBsdIfconfigNetwork(generic_bsd_ifconfig_network_2, dict_0)
        var_0 = generic_bsd_ifconfig_network_3.parse_status_line(str_0, generic_bsd_ifconfig_network_1, set_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '5o&kFc]'
        str_1 = '_[3>?<$'
        dict_0 = {str_0: str_1, str_1: str_0, str_1: str_0}
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_1, dict_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_interface_line(str_1)
        set_0 = {str_1, str_1}
        int_0 = 2988
        var_1 = generic_bsd_ifconfig_network_0.get_options(str_1)
        var_2 = generic_bsd_ifconfig_network_0.parse_unknown_line(dict_0, set_0, str_1)
        complex_0 = None
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(int_0)
        var_3 = generic_bsd_ifconfig_network_1.detect_type_media(dict_0)
        var_4 = generic_bsd_ifconfig_network_1.merge_default_interface(dict_0, complex_0, str_1)
        var_5 = generic_bsd_ifconfig_network_0.parse_lladdr_line(dict_0, set_0, generic_bsd_ifconfig_network_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '1'
        list_0 = [str_0, str_0, str_0]
        int_0 = 12
        bytes_0 = b'\x08M}b\xa8\xe6\x01\x84\xf4/\xe5'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bytes_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_inet_line(list_0, str_0, int_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = "\nco'M"
        list_0 = []
        tuple_0 = (str_0, list_0)
        int_0 = -1348
        complex_0 = None
        set_0 = {complex_0, complex_0}
        str_1 = 'sxx&en'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(set_0, str_1)
        var_0 = generic_bsd_ifconfig_network_0.parse_inet6_line(tuple_0, int_0, tuple_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '5o<&kFc]'
        str_1 = '_[><'
        dict_0 = {str_0: str_1, str_1: str_0, str_1: str_0}
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_1, dict_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_interface_line(str_1)
        set_0 = {str_1, str_1}
        var_1 = generic_bsd_ifconfig_network_0.get_options(str_1)
        var_2 = generic_bsd_ifconfig_network_0.parse_unknown_line(dict_0, set_0, str_1)
        complex_0 = None
        float_0 = None
        var_3 = generic_bsd_ifconfig_network_0.parse_media_line(str_1, dict_0, float_0)
        var_4 = generic_bsd_ifconfig_network_0.detect_type_media(dict_0)
        var_5 = generic_bsd_ifconfig_network_0.merge_default_interface(dict_0, complex_0, str_1)
        float_1 = None
        tuple_0 = None
        tuple_1 = (float_1, tuple_0, complex_0)
        str_2 = 'A*m./X}-vCX/{Q'
        var_6 = generic_bsd_ifconfig_network_0.parse_tunnel_line(tuple_1, str_2, complex_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'u7TAv'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0, dict_0)
        set_0 = {str_0, str_0}
        str_1 = 'Ji\t'
        var_0 = generic_bsd_ifconfig_network_0.get_options(str_1)
        var_1 = generic_bsd_ifconfig_network_0.parse_unknown_line(dict_0, set_0, str_1)
        generic_bsd_ifconfig_network_1 = module_0.GenericBsdIfconfigNetwork(generic_bsd_ifconfig_network_0)
        var_2 = generic_bsd_ifconfig_network_0.get_default_interfaces(dict_0)
    except BaseException:
        pass

def test_case_14():
    try:
        bytes_0 = b'\x9dS\x18\t\xc1\x00\x8e\xcak\xe3d\x9e_\x8f'
        int_0 = 1456
        bytes_1 = b'\x19{\xcbX\xa2\xd3V&\xb8\x19\xa4\xc5&\xcc'
        bool_0 = True
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bool_0)
        var_0 = generic_bsd_ifconfig_network_0.merge_default_interface(bytes_0, int_0, bytes_1)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'u7TAv'
        str_1 = 'vwQ]pS{@=Wgov'
        dict_0 = {str_0: str_1, str_1: str_0, str_1: str_0}
        bool_0 = False
        int_0 = -2499
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(int_0)
        var_0 = generic_bsd_ifconfig_network_0.detect_type_media(dict_0)
        var_1 = generic_bsd_ifconfig_network_0.get_default_interfaces(bool_0)
    except BaseException:
        pass

def test_case_16():
    try:
        set_0 = set()
        str_0 = 'Bp)?1\\+}!'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_interface_line(set_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '1'
        list_0 = [str_0, str_0, str_0, str_0, str_0]
        int_0 = 12
        bytes_0 = b'\x08M}b\xa8\xe6\x01\x84\xf4/\xe5'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(bytes_0)
        var_0 = generic_bsd_ifconfig_network_0.parse_inet_line(list_0, str_0, int_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = ',TFzp,\\-O (b=s;'
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(str_0)
        str_1 = 'oU \ndqL=d)vBs'
        int_0 = -1155
        var_0 = generic_bsd_ifconfig_network_0.parse_inet6_line(str_1, generic_bsd_ifconfig_network_0, int_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = '5o&kFc]'
        int_0 = -2499
        str_1 = '"argument_spec" arg is required in args: %s'
        float_0 = None
        str_2 = 'D/jWlUc6(_~G!AU'
        list_0 = [str_1, int_0]
        dict_0 = {int_0: str_2, float_0: list_0, str_0: str_1}
        generic_bsd_ifconfig_network_0 = module_0.GenericBsdIfconfigNetwork(int_0, str_1)
        var_0 = generic_bsd_ifconfig_network_0.parse_inet6_line(str_2, list_0, dict_0)
    except BaseException:
        pass