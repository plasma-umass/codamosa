# Automatically generated by Pynguin.
import httpie.plugins.base as module_0

def test_case_0():
    try:
        transport_plugin_0 = module_0.TransportPlugin()
        transport_plugin_1 = module_0.TransportPlugin()
        dict_0 = {}
        auth_plugin_0 = module_0.AuthPlugin(**dict_0)
        var_0 = auth_plugin_0.get_auth()
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = {}
        transport_plugin_0 = module_0.TransportPlugin(**dict_0)
        var_0 = transport_plugin_0.get_adapter()
    except BaseException:
        pass

def test_case_2():
    try:
        base_plugin_0 = module_0.BasePlugin()
        auth_plugin_0 = module_0.AuthPlugin()
        int_0 = -1872
        converter_plugin_0 = module_0.ConverterPlugin(int_0)
        var_0 = converter_plugin_0.convert(auth_plugin_0)
    except BaseException:
        pass

def test_case_3():
    try:
        formatter_plugin_0 = module_0.FormatterPlugin()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'format_options'
        str_1 = 'm"1(ZQ'
        dict_0 = {str_0: str_0, str_0: str_0, str_1: str_1}
        str_2 = 's!&c\x0c/cbu:1t 0'
        str_3 = '!80L;$OQ'
        formatter_plugin_0 = module_0.FormatterPlugin(**dict_0)
        str_4 = formatter_plugin_0.format_body(str_2, str_3)
        converter_plugin_0 = module_0.ConverterPlugin(dict_0)
        int_0 = None
        var_0 = converter_plugin_0.convert(int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'format_options'
        str_1 = 'm"1(ZQ'
        dict_0 = {str_0: str_0, str_0: str_0, str_1: str_1}
        str_2 = 's!&c\x0c/cbu:1t 0'
        str_3 = '!80L;$OQ'
        formatter_plugin_0 = module_0.FormatterPlugin(**dict_0)
        str_4 = 'k'
        str_5 = formatter_plugin_0.format_headers(str_4)
        str_6 = formatter_plugin_0.format_body(str_2, str_3)
        converter_plugin_0 = module_0.ConverterPlugin(dict_0)
        int_0 = None
        var_0 = converter_plugin_0.convert(int_0)
    except BaseException:
        pass