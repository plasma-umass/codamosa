# Automatically generated by Pynguin.
import httpie.plugins.base as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'format_options'
    var_0 = {}
    var_1 = {str_0: var_0}
    formatter_plugin_0 = module_0.FormatterPlugin(**var_1)
    str_1 = 'text'
    str_2 = 'text/html'
    str_3 = formatter_plugin_0.format_body(str_1, str_2)

def test_case_2():
    str_0 = 'format_options'
    var_0 = {}
    var_1 = {str_0: var_0}
    formatter_plugin_0 = module_0.FormatterPlugin(**var_1)
    str_1 = 'UUznF'
    str_2 = formatter_plugin_0.format_headers(str_1)
    str_3 = 'TT1t7\x0b,M=vQ7st>#q<Z>'
    converter_plugin_0 = module_0.ConverterPlugin(str_3)
    base_plugin_0 = module_0.BasePlugin()
    str_4 = formatter_plugin_0.format_headers(str_1)
    tuple_0 = ()
    converter_plugin_1 = module_0.ConverterPlugin(tuple_0)