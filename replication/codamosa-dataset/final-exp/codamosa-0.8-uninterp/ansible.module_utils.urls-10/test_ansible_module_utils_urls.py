# Automatically generated by Pynguin.
import ansible.module_utils.urls as module_0
import urllib.parse as module_1

def test_case_0():
    pass

def test_case_1():
    int_0 = -2145
    list_0 = [int_0, int_0, int_0]
    unix_h_t_t_p_handler_0 = module_0.UnixHTTPHandler(list_0)
    var_0 = module_0.get_channel_binding_cert_hash(unix_h_t_t_p_handler_0)

def test_case_2():
    parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()
    var_0 = module_0.prepare_multipart(parse_result_dotted_dict_0)

def test_case_3():
    parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()
    var_0 = parse_result_dotted_dict_0.as_list()
    var_1 = module_0.prepare_multipart(parse_result_dotted_dict_0)

def test_case_4():
    str_0 = 'Darwin'
    var_0 = module_0.generic_urlparse(str_0)

def test_case_5():
    str_0 = 'GVX:-j1JA@j=z\t'
    s_s_l_validation_handler_0 = module_0.SSLValidationHandler(str_0, str_0, str_0)
    var_0 = s_s_l_validation_handler_0.detect_no_proxy(str_0)

def test_case_6():
    str_0 = '.E}'
    dict_0 = {}
    request_0 = module_0.Request(dict_0, str_0, dict_0)

def test_case_7():
    str_0 = '.'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    request_0 = module_0.Request(dict_0, str_0, dict_0)

def test_case_8():
    str_0 = 'j{0k$h v4\x0c.B7\r_6f;'
    var_0 = module_0.generic_urlparse(str_0)

def test_case_9():
    s_s_l_validation_error_0 = module_0.SSLValidationError()
    var_0 = module_0.get_channel_binding_cert_hash(s_s_l_validation_error_0)

def test_case_10():
    dict_0 = {}
    proxy_error_0 = module_0.ProxyError(**dict_0)
    list_0 = []
    list_1 = []
    bytes_0 = b'K\xfc\x13\x9e(\xbf\xe7G~\xe4\x85*\xd2V\xe9\x8bU\xf5\xd9'
    s_s_l_validation_error_0 = module_0.SSLValidationError()
    s_s_l_validation_handler_0 = module_0.SSLValidationHandler(list_1, bytes_0)
    var_0 = s_s_l_validation_handler_0.make_context(list_0, dict_0)

def test_case_11():
    bool_0 = True
    var_0 = module_0.atexit_remove_file(bool_0)

def test_case_12():
    str_0 = 'gkz(d~7f\rq'
    var_0 = module_0.atexit_remove_file(str_0)
    s_s_l_validation_error_0 = module_0.SSLValidationError()
    proxy_error_0 = module_0.ProxyError()

def test_case_13():
    str_0 = 'J[e?t'
    list_0 = [str_0]
    dict_0 = {}
    custom_h_t_t_p_s_connection_0 = module_0.CustomHTTPSConnection(*list_0, **dict_0)
    h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler()

def test_case_14():
    str_0 = 'http://www.google.com'
    request_with_method_0 = module_0.RequestWithMethod(str_0, str_0)
    var_0 = request_with_method_0.get_method()
    no_s_s_l_error_0 = module_0.NoSSLError()
    h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler()

def test_case_15():
    str_0 = 'https://baz:8080/path/to?arg=1#fragment'
    var_0 = module_1.urlparse(str_0)
    var_1 = module_0.generic_urlparse(var_0)