# Automatically generated by Pynguin.
import mimesis.providers.internet as module_0
import mimesis.enums as module_1

def test_case_0():
    internet_0 = module_0.Internet()

def test_case_1():
    str_0 = '@zTP_n)`Kv|o'
    internet_0 = module_0.Internet()
    var_0 = internet_0.stock_image(str_0, str_0)
    internet_1 = module_0.Internet()
    str_1 = internet_1.ip_v6()
    int_0 = internet_1.http_status_code()
    int_1 = internet_1.port()
    str_2 = internet_1.content_type()

def test_case_2():
    internet_0 = module_0.Internet()
    str_0 = internet_0.http_status_message()
    var_0 = internet_0.hashtags()
    i_pv6_address_0 = internet_0.ip_v6_object()
    list_0 = []
    internet_1 = module_0.Internet()
    internet_2 = module_0.Internet(*list_0)
    str_1 = internet_2.emoji()

def test_case_3():
    dict_0 = {}
    internet_0 = module_0.Internet(**dict_0)
    int_0 = internet_0.http_status_code()

def test_case_4():
    internet_0 = module_0.Internet()
    str_0 = internet_0.http_method()

def test_case_5():
    internet_0 = module_0.Internet()
    var_0 = internet_0.hashtags()
    str_0 = internet_0.top_level_domain()
    internet_1 = module_0.Internet()
    int_0 = internet_0.port()
    int_1 = internet_1.http_status_code()
    str_1 = internet_1.emoji()
    str_2 = internet_1.ip_v4()
    int_2 = internet_1.http_status_code()

def test_case_6():
    internet_0 = module_0.Internet()
    str_0 = internet_0.ip_v6()
    i_pv6_address_0 = internet_0.ip_v6_object()
    str_1 = internet_0.user_agent()
    str_2 = internet_0.image_placeholder(str_1)

def test_case_7():
    dict_0 = {}
    internet_0 = module_0.Internet(**dict_0)
    str_0 = internet_0.mac_address()
    str_1 = internet_0.top_level_domain()
    str_2 = internet_0.http_method()
    internet_1 = module_0.Internet()
    int_0 = internet_1.http_status_code()
    i_pv4_address_0 = internet_1.ip_v4_object()
    internet_2 = module_0.Internet()
    i_pv6_address_0 = internet_2.ip_v6_object()
    int_1 = internet_2.http_status_code()

def test_case_8():
    internet_0 = module_0.Internet()
    str_0 = internet_0.emoji()

def test_case_9():
    internet_0 = module_0.Internet()
    bool_0 = True
    var_0 = internet_0.stock_image(bool_0)
    internet_1 = module_0.Internet()
    str_0 = internet_1.emoji()

def test_case_10():
    internet_0 = module_0.Internet()
    int_0 = 1
    var_0 = internet_0.hashtags(int_0)
    internet_1 = module_0.Internet()
    var_1 = internet_1.hashtags()

def test_case_11():
    internet_0 = module_0.Internet()
    str_0 = internet_0.http_status_message()
    str_1 = internet_0.network_protocol()
    str_2 = internet_0.image_placeholder()
    str_3 = internet_0.ip_v6()
    port_range_0 = module_1.PortRange.REGISTERED
    str_4 = internet_0.ip_v4(port_range_0)
    str_5 = internet_0.http_status_message()
    internet_1 = module_0.Internet()
    str_6 = internet_1.emoji()
    str_7 = internet_1.home_page()
    str_8 = internet_1.emoji()
    internet_2 = module_0.Internet()
    str_9 = internet_2.http_method()
    var_0 = internet_2.hashtags()
    int_0 = internet_1.port()
    str_10 = internet_1.content_type()

def test_case_12():
    internet_0 = module_0.Internet()
    int_0 = 1920
    int_1 = 1080
    str_0 = 'river'
    str_1 = 'house'
    str_2 = [str_0, str_1, str_0]
    var_0 = internet_0.stock_image(int_0, int_1, str_2)
    bool_0 = True
    var_1 = internet_0.stock_image(int_0, int_1, str_2, bool_0)