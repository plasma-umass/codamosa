# Automatically generated by Pynguin.
import httpie.plugins.base as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'format_options'
    str_1 = 'headers_only'
    bool_0 = False
    bool_1 = {str_1: bool_0}
    bool_2 = {str_0: bool_1}
    formatter_plugin_0 = module_0.FormatterPlugin(**bool_2)
    str_2 = 'Last-Modified: Tue, 22 Jan 2019 16:33:34 GMT\n    ETag: "5c467a7e-5b1"\n    Vary: Accept'
    str_3 = formatter_plugin_0.format_headers(str_2)
    str_4 = 'new_header_string after processing:'
    var_0 = print(str_4, str_3)