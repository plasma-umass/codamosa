# Automatically generated by Pynguin.
import sanic.helpers as module_0

def test_case_0():
    int_0 = 1069
    var_0 = module_0.has_message_body(int_0)

def test_case_1():
    str_0 = 'RB"&VR^'
    var_0 = module_0.is_hop_by_hop_header(str_0)

def test_case_2():
    int_0 = -493
    var_0 = module_0.has_message_body(int_0)

def test_case_3():
    dict_0 = {}
    var_0 = module_0.remove_entity_headers(dict_0)

def test_case_4():
    str_0 = 'Content-Type'
    str_1 = 'Custom-Header'
    str_2 = 'text/plain'
    str_3 = 'value'
    str_4 = {str_0: str_2, str_1: str_3}
    var_0 = None
    var_1 = lambda x: var_0
    var_2 = module_0.remove_entity_headers(str_4)
    var_3 = lambda x: var_0

def test_case_5():
    int_0 = 501
    var_0 = module_0.has_message_body(int_0)
    int_1 = 204
    var_1 = module_0.has_message_body(int_1)
    int_2 = 100
    var_2 = module_0.has_message_body(int_2)
    int_3 = 200
    var_3 = module_0.has_message_body(int_3)

def test_case_6():
    str_0 = 'content-length'
    str_1 = 'content-md5'
    str_2 = '0'
    str_3 = 'foo'
    str_4 = {str_0: str_2, str_1: str_3}
    var_0 = module_0.remove_entity_headers(str_4)
    str_5 = 'allow'
    str_6 = 'GET'
    str_7 = {str_5: str_6, str_0: str_2, str_1: str_3}
    var_1 = module_0.remove_entity_headers(str_7)
    str_8 = 'content-location'
    str_9 = '/foo/bar'
    str_10 = {str_8: str_9, str_0: str_2, str_1: str_3}
    var_2 = module_0.remove_entity_headers(str_10)