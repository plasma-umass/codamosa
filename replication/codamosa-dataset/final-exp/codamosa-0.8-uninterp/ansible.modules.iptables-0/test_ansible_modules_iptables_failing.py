# Automatically generated by Pynguin.
import ansible.modules.iptables as module_0

def test_case_0():
    try:
        dict_0 = {}
        int_0 = 232
        int_1 = 2028
        float_0 = 9.937
        var_0 = module_0.append_param(dict_0, int_0, int_1, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'mNPUf'
        str_1 = '-list'
        int_0 = 2625
        str_2 = 'bnxO\rR0QsO1"'
        bool_0 = True
        dict_0 = {str_0: str_1, str_0: bool_0, str_1: int_0}
        var_0 = module_0.append_param(int_0, str_2, bool_0, dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 2.0
        str_0 = '.wM6ykQ'
        var_0 = module_0.append_csv(float_0, str_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 2.0
        list_0 = [float_0, float_0, float_0]
        float_1 = 1320.563
        var_0 = module_0.append_match(float_0, list_0, float_1)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = -1107
        str_0 = '(L%Z'
        float_0 = None
        var_0 = module_0.append_jump(int_0, str_0, float_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'tcp'
        str_1 = '192.168.1.100-192.168.1.199'
        str_2 = '10.0.0.1-10.0.0.50'
        str_3 = 'ACCEPT'
        str_4 = '5'
        var_0 = dict(protocol=str_0, source=str_1, destination=str_2, jump=str_3, wait=str_4)
        var_1 = module_0.construct_rule(var_0)
    except BaseException:
        pass

def test_case_6():
    try:
        float_0 = 1873.97
        var_0 = module_0.construct_rule(float_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = None
        int_0 = -45
        var_0 = module_0.check_present(bool_0, bool_0, int_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = False
        float_0 = 3004.5
        str_0 = '=t>*l3I'
        var_0 = module_0.append_tcp_flags(bool_0, str_0, float_0)
        list_0 = None
        str_1 = 'BA_n+Q4M5]$,rH~e6rU\t'
        tuple_0 = (list_0, str_1, list_0)
        int_0 = -890
        var_1 = module_0.append_rule(list_0, tuple_0, int_0)
    except BaseException:
        pass

def test_case_9():
    try:
        bool_0 = False
        float_0 = 3004.52301
        str_0 = '=t>*l3I'
        var_0 = module_0.append_tcp_flags(bool_0, str_0, float_0)
        set_0 = None
        bytes_0 = b'\xc9\x1f\xbe\x12\xb0'
        float_1 = -1924.699046
        var_1 = module_0.insert_rule(set_0, bytes_0, float_1)
    except BaseException:
        pass

def test_case_10():
    try:
        float_0 = 931.0
        set_0 = {float_0}
        dict_0 = {}
        var_0 = module_0.remove_rule(float_0, set_0, dict_0)
    except BaseException:
        pass

def test_case_11():
    try:
        float_0 = None
        dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0, float_0: float_0}
        int_0 = 2923
        var_0 = module_0.flush_table(float_0, dict_0, int_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'I\x0c\\U%'
        var_0 = dict(chain=str_0, policy=str_0, table=str_0)
        var_1 = module_0.set_chain_policy(var_0, var_0, var_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'FORWARD'
        var_0 = dict(ip_version=str_0, table=str_0, chain=str_0)
        var_1 = None
        var_2 = module_0.get_chain_policy(str_0, var_1, var_0)
    except BaseException:
        pass

def test_case_14():
    try:
        bytes_0 = b'~\xcf\x11\xab\xd6.\xfa\x13\x01\x9b8\xcd\x11\xc4\xdf\x9e)\x9e\xb1'
        set_0 = {bytes_0, bytes_0}
        var_0 = module_0.get_iptables_version(bytes_0, set_0)
    except BaseException:
        pass

def test_case_15():
    try:
        bool_0 = False
        float_0 = 3004.52301
        str_0 = '=t>*l3I'
        var_0 = module_0.append_tcp_flags(bool_0, str_0, float_0)
        set_0 = set()
        dict_0 = {}
        var_1 = module_0.append_wait(dict_0, bool_0, dict_0)
        str_1 = 'Z[Tjc(\\F/_@!@'
        var_2 = module_0.append_wait(set_0, str_1, str_1)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'test'
        str_1 = 'module'
        str_2 = 'params'
        tuple_0 = None
        list_0 = None
        bytes_0 = b'\xd1\xb4\x99\xc37\xea\x98_\x9a'
        var_0 = module_0.append_tcp_flags(tuple_0, list_0, bytes_0)
        var_1 = module_0.get_chain_policy(str_0, str_1, str_2)
    except BaseException:
        pass

def test_case_17():
    try:
        dict_0 = None
        str_0 = 'c{.USf'
        tuple_0 = ()
        int_0 = None
        str_1 = "Ag(pm~<?k~'ycw!jr"
        bytes_0 = b'\x98}\xf4Fr\x9e\xdf\x0c\xb8\x86\xfd\xd74'
        bool_0 = False
        var_0 = module_0.append_tcp_flags(bytes_0, int_0, bool_0)
        float_0 = 4558.0
        var_1 = module_0.append_match_flag(str_1, str_1, float_0, tuple_0)
        str_2 = '<^gn"}&1zu~\x0b$;2pr>K'
        int_1 = -77
        var_2 = module_0.append_param(str_2, str_0, int_1, dict_0)
    except BaseException:
        pass

def test_case_18():
    try:
        float_0 = None
        tuple_0 = None
        bytes_0 = b'\xa1\xd2\x9b\x88\x7f\xec<\x06"'
        list_0 = [bytes_0, float_0, tuple_0]
        bool_0 = False
        var_0 = module_0.append_jump(list_0, bool_0, list_0)
        str_0 = '\x0bP\t09:aehdpkbNY'
        bytes_1 = b'\x16\x8a\xbd\x9d\xdf.\xac_t'
        set_0 = None
        var_1 = module_0.append_tcp_flags(str_0, bytes_1, set_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = '3'
        var_0 = dict(table=str_0, chain=str_0, rule_num=str_0, protocol=str_0, destination_port=str_0)
        str_1 = '-I'
        bool_0 = True
        var_1 = module_0.push_arguments(str_1, str_1, var_0, bool_0)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = 'filter'
        str_1 = 'INPUT'
        complex_0 = None
        str_2 = '80'
        var_0 = dict(table=str_0, chain=str_1, rule_num=complex_0, protocol=str_2, destination_port=str_2)
        str_3 = '/sbin/iptables'
        str_4 = '-I'
        bool_0 = True
        var_1 = module_0.push_arguments(str_3, str_4, var_0, bool_0)
    except BaseException:
        pass