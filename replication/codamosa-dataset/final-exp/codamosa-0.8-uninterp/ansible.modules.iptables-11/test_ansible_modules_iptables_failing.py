# Automatically generated by Pynguin.
import ansible.modules.iptables as module_0

def test_case_0():
    try:
        str_0 = 'import_timeout'
        set_0 = {str_0}
        complex_0 = None
        var_0 = module_0.append_param(set_0, complex_0, str_0, set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'1\x1b\xab\xe2\xc3\xb0\xbc\xc5\x88\x0b\xbe,@\xc1'
        str_0 = '!\rHr\tN&'
        float_0 = 1093.7712
        var_0 = module_0.append_param(bytes_0, str_0, str_0, float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        list_0 = []
        str_0 = '}g&F'
        str_1 = 'iqpx~Dp\x0chWo#"QmI'
        set_0 = {str_1}
        var_0 = module_0.append_param(str_0, str_1, list_0, set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'tF=CK>Sa8c~|(i?'
        tuple_0 = (str_0,)
        bytes_0 = b'\xbd>GR/\xb1G\xd1?z2\x84'
        var_0 = module_0.append_tcp_flags(tuple_0, bytes_0, tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 4720
        str_0 = '?X&[~db<PV)\nKoy'
        bool_0 = True
        var_0 = module_0.append_csv(int_0, str_0, bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 2803
        bool_0 = True
        int_1 = -2415
        var_0 = module_0.append_jump(int_0, bool_0, int_1)
    except BaseException:
        pass

def test_case_6():
    try:
        tuple_0 = None
        bytes_0 = b'\xd9d'
        list_0 = [tuple_0, bytes_0, bytes_0]
        int_0 = -3611
        tuple_1 = None
        var_0 = module_0.append_tcp_flags(list_0, tuple_1, bytes_0)
        var_1 = module_0.append_wait(tuple_0, list_0, int_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'table'
        str_1 = 'chain'
        str_2 = 'INP"6UT'
        int_0 = 4
        var_0 = {str_0: str_2, str_1: str_2, str_2: int_0}
        var_1 = module_0.push_arguments(str_0, str_1, var_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'human_to_bytes'
        set_0 = {str_0, str_0}
        float_0 = -1341.390139
        var_0 = module_0.flush_table(str_0, set_0, float_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'ACK'
        str_1 = 'RST'
        str_2 = [str_0, str_1]
        str_3 = 'SYN'
        str_4 = 'FIN'
        var_0 = dict(flags=str_2, flags_set=str_2)
        str_5 = '--tcp-flags'
        var_1 = module_0.append_tcp_flags(str_2, var_0, str_5)
        str_6 = [str_0, str_1, str_3]
        str_7 = [str_0, str_4]
        var_2 = dict(flags=str_6, flags_set=str_7)
        float_0 = 1626.8628
        int_0 = -1420
        bytes_0 = b'#\x0b'
        var_3 = module_0.append_rule(float_0, int_0, bytes_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bool_0 = False
        str_0 = 'xZ'
        int_0 = 255
        tuple_0 = (str_0, int_0)
        tuple_1 = (bool_0, tuple_0)
        var_0 = module_0.insert_rule(tuple_1, tuple_0, tuple_0)
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = 2082
        list_0 = []
        str_0 = '\\yG\t#'
        var_0 = module_0.remove_rule(int_0, list_0, str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        int_0 = 29
        float_0 = -2097.8
        list_0 = [int_0, float_0, float_0, int_0]
        var_0 = module_0.set_chain_policy(int_0, float_0, list_0)
    except BaseException:
        pass

def test_case_13():
    try:
        float_0 = -121.53368
        float_1 = None
        bytes_0 = b'A\x81\xdf\xcd\xc7\xb5\xcf'
        var_0 = module_0.get_chain_policy(float_0, float_1, bytes_0)
    except BaseException:
        pass

def test_case_14():
    try:
        dict_0 = {}
        bytes_0 = b'\xe9\xa0\xa0\xc4\x9b"x)\x95\xda\x16Z\x1a\x08\xd9'
        float_0 = 453.986
        var_0 = module_0.append_param(dict_0, dict_0, bytes_0, float_0)
        bytes_1 = None
        int_0 = 1124
        var_1 = module_0.get_iptables_version(bytes_1, int_0)
    except BaseException:
        pass

def test_case_15():
    try:
        list_0 = []
        float_0 = 4221.38
        var_0 = module_0.append_csv(list_0, list_0, float_0)
        tuple_0 = None
        bytes_0 = b'u^'
        int_0 = -5761
        var_1 = module_0.append_wait(tuple_0, bytes_0, int_0)
    except BaseException:
        pass

def test_case_16():
    try:
        float_0 = 0.1
        bool_0 = False
        str_0 = '9Z<T2 )OAq3l\x0c'
        var_0 = module_0.append_match(float_0, bool_0, str_0)
    except BaseException:
        pass

def test_case_17():
    try:
        dict_0 = {}
        bytes_0 = b'\xe9\xa0\xa0\xc4\x9b"x)\x95\xda\x16Z\x1a\x08\xd9'
        float_0 = 453.986
        var_0 = module_0.append_param(dict_0, dict_0, bytes_0, float_0)
        str_0 = 'X-=Xz`XUM*i)ad%z`'
        set_0 = None
        int_0 = 2114
        var_1 = module_0.check_present(str_0, set_0, int_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = '-I'
        str_1 = 'table'
        str_2 = 'chain'
        str_3 = 'rule_num'
        int_0 = 4
        var_0 = {str_1: str_3, str_2: str_2, str_3: int_0}
        float_0 = -249.0905
        set_0 = None
        str_4 = 'L'
        var_1 = module_0.append_wait(float_0, set_0, str_4)
        var_2 = module_0.push_arguments(str_2, str_0, var_0)
    except BaseException:
        pass

def test_case_19():
    try:
        dict_0 = None
        bytes_0 = None
        set_0 = {dict_0, bytes_0, dict_0, bytes_0}
        list_0 = []
        var_0 = module_0.append_param(dict_0, bytes_0, set_0, list_0)
        bool_0 = False
        var_1 = module_0.remove_rule(dict_0, bytes_0, bool_0)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = '-I'
        str_1 = 'table'
        str_2 = 'chain'
        str_3 = 'rule_num'
        int_0 = 4
        var_0 = {str_1: str_3, str_2: str_3, str_3: int_0}
        var_1 = module_0.push_arguments(str_1, str_0, var_0)
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = 'iptables'
        var_0 = None
        str_1 = 'chain'
        str_2 = 'policy'
        str_3 = 'table'
        str_4 = 'INPUT'
        str_5 = 'DROP'
        str_6 = 'filter'
        str_7 = {str_1: str_4, str_2: str_5, str_3: str_6}
        var_1 = module_0.set_chain_policy(str_0, var_0, str_7)
    except BaseException:
        pass

def test_case_22():
    try:
        var_0 = None
        str_0 = 'filter'
        str_1 = 'INPUT'
        var_1 = dict(table=str_0, chain=str_1)
        var_2 = module_0.get_chain_policy(var_0, var_0, var_1)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = '/usr/bin/iptables'
        str_1 = 'run_command'
        str_2 = 'test'
        var_0 = None
        var_1 = lambda x, y: var_0
        bool_0 = False
        var_2 = {str_1: var_1, str_2: bool_0}
        str_3 = 'table'
        str_4 = 'chain'
        str_5 = 'filter'
        str_6 = 'INPUT'
        str_7 = {str_3: str_5, str_4: str_6}
        var_3 = module_0.flush_table(str_0, var_2, str_7)
    except BaseException:
        pass