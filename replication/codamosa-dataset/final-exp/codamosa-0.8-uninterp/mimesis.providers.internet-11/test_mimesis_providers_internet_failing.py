# Automatically generated by Pynguin.
import mimesis.providers.internet as module_0
import mimesis.enums as module_1

def test_case_0():
    try:
        internet_0 = module_0.Internet()
        i_pv4_address_0 = internet_0.ip_v4_object()
        str_0 = internet_0.ip_v4()
        str_1 = internet_0.mac_address()
        str_2 = internet_0.mac_address()
        str_3 = internet_0.mac_address()
        str_4 = internet_0.ip_v6()
        list_0 = [i_pv4_address_0, internet_0]
        i_pv6_address_0 = internet_0.ip_v6_object()
        internet_1 = module_0.Internet(*list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '?xZcQ7CKL=&e[OiF7y'
        str_1 = 'V`1yj{8F'
        tuple_0 = ()
        internet_0 = module_0.Internet()
        port_range_0 = module_1.PortRange.EPHEMERAL
        str_2 = internet_0.ip_v4(port_range_0)
        str_3 = internet_0.content_type()
        dict_0 = {str_0: str_0, str_1: tuple_0, str_0: str_0}
        str_4 = internet_0.http_method()
        internet_1 = module_0.Internet(**dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        internet_0 = module_0.Internet()
        int_0 = internet_0.port()
        bool_0 = True
        var_0 = internet_0.stock_image(int_0, int_0, bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        internet_0 = module_0.Internet()
        str_0 = internet_0.http_status_message()
        internet_1 = module_0.Internet()
        str_1 = internet_1.emoji()
        port_range_0 = None
        int_0 = internet_1.port(port_range_0)
    except BaseException:
        pass

def test_case_4():
    try:
        internet_0 = module_0.Internet()
        str_0 = internet_0.content_type()
        str_1 = '6p/'
        str_2 = '8%-dSM(=~zRmI.('
        str_3 = 'DNg4b{o3'
        list_0 = [str_2, str_3, str_0]
        bool_0 = True
        var_0 = internet_0.stock_image(str_1, str_2, list_0, bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        internet_0 = module_0.Internet()
        internet_1 = module_0.Internet()
        str_0 = internet_1.top_level_domain()
        str_1 = internet_1.emoji()
        str_2 = '6p/'
        str_3 = '8%-dSM(=~zRmI.('
        list_0 = [str_3, str_3, str_3]
        bool_0 = True
        var_0 = internet_0.stock_image(str_2, str_0, list_0, bool_0)
    except BaseException:
        pass