# Automatically generated by Pynguin.
import httpie.plugins.base as module_0

def test_case_0():
    try:
        bytes_0 = b'\xd9'
        auth_plugin_0 = module_0.AuthPlugin()
        var_0 = auth_plugin_0.get_auth(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        transport_plugin_0 = module_0.TransportPlugin()
        var_0 = transport_plugin_0.get_adapter()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = ' jR'
        int_0 = 1408
        converter_plugin_0 = module_0.ConverterPlugin(int_0)
        var_0 = converter_plugin_0.convert(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        formatter_plugin_0 = module_0.FormatterPlugin()
    except BaseException:
        pass