# Automatically generated by Pynguin.
import ansible.module_utils.common.network as module_0

def test_case_0():
    try:
        str_0 = ";(PEB)j\\/6'DyT8"
        var_0 = module_0.to_bits(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 400
        var_0 = module_0.to_masklen(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 2589.535
        var_0 = module_0.to_netmask(float_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'XvTd&d\ry19'
        var_0 = module_0.to_netmask(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '2Q5.25P.255.Y'
        var_0 = module_0.to_masklen(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '1l92.168.1.1'
        var_0 = module_0.to_subnet(str_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = None
        var_0 = module_0.to_ipv6_subnet(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = True
        var_0 = module_0.to_ipv6_network(bool_0)
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = 1927
        var_0 = module_0.is_mac(int_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'o|'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        var_0 = module_0.to_netmask(dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '=oob?j#?c4]\n'
        tuple_0 = ()
        var_0 = module_0.to_subnet(str_0, tuple_0)
    except BaseException:
        pass