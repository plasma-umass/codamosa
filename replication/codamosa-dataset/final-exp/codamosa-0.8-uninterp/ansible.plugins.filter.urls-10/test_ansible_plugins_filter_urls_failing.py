# Automatically generated by Pynguin.
import ansible.plugins.filter.urls as module_0

def test_case_0():
    try:
        bytes_0 = b'\x8e8\xb7\x82\x04\x17A\xdc\xbdM\x8f\xc0\x93[D\x13T'
        var_0 = module_0.do_urldecode(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -1699
        float_0 = 0.1
        list_0 = [float_0, int_0]
        var_0 = module_0.unicode_urlencode(float_0, list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        filter_module_0 = module_0.FilterModule()
        var_0 = module_0.do_urlencode(filter_module_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\xb8k`d\xb4l\t\xa3\xf6\xd8\xf6\x8f\x08\xf6^{\x00'
        var_0 = module_0.do_urlencode(bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = None
        str_1 = 'i-qucH|Y~X>^7'
        filter_module_0 = module_0.FilterModule()
        var_0 = filter_module_0.filters()
        var_1 = module_0.do_urldecode(str_1)
        dict_0 = {}
        var_2 = module_0.do_urlencode(dict_0)
        var_3 = filter_module_0.filters()
        var_4 = module_0.do_urlencode(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        filter_module_0 = module_0.FilterModule()
        str_0 = 'd{>y\r$}2?LLG#\x0b'
        dict_0 = {str_0: filter_module_0, str_0: str_0}
        var_0 = module_0.do_urlencode(dict_0)
        var_1 = module_0.unicode_urldecode(filter_module_0)
    except BaseException:
        pass