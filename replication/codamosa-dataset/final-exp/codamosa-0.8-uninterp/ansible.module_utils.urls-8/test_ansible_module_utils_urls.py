# Automatically generated by Pynguin.
import ansible.module_utils.urls as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'https://pypi.python.org/pypi/'
    var_0 = module_0.open_url(str_0)

def test_case_2():
    h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler()
    dict_0 = {}
    var_0 = module_0.prepare_multipart(dict_0)

def test_case_3():
    str_0 = 'https://pypi.python.org/pypi/'
    var_0 = module_0.open_url(str_0)
    set_0 = set()
    bytes_0 = b'\xda7\xf9\x82\xa2\xba7C\xdf\t\x0e'
    unix_h_t_t_p_handler_0 = module_0.UnixHTTPHandler(bytes_0)
    list_0 = [var_0, set_0, unix_h_t_t_p_handler_0, set_0]
    proxy_error_0 = module_0.ProxyError(*list_0)

def test_case_4():
    parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()

def test_case_5():
    int_0 = 37
    h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler(int_0)
    parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()
    var_0 = parse_result_dotted_dict_0.as_list()
    s_s_l_validation_handler_0 = module_0.SSLValidationHandler(h_t_t_p_s_client_auth_handler_0, parse_result_dotted_dict_0)
    var_1 = s_s_l_validation_handler_0.get_ca_certs()
    var_2 = s_s_l_validation_handler_0.detect_no_proxy(int_0)

def test_case_6():
    str_0 = '/etc/ssl/certs'
    var_0 = module_0.atexit_remove_file(str_0)
    proxy_error_0 = module_0.ProxyError()

def test_case_7():
    int_0 = 2
    h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler(int_0)
    parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()
    s_s_l_validation_handler_0 = module_0.SSLValidationHandler(h_t_t_p_s_client_auth_handler_0, parse_result_dotted_dict_0)
    var_0 = s_s_l_validation_handler_0.detect_no_proxy(int_0)

def test_case_8():
    bool_0 = False
    var_0 = module_0.get_channel_binding_cert_hash(bool_0)

def test_case_9():
    dict_0 = {}
    var_0 = module_0.prepare_multipart(dict_0)

def test_case_10():
    custom_h_t_t_p_s_handler_0 = None
    str_0 = '>J'
    dict_0 = {str_0: custom_h_t_t_p_s_handler_0, str_0: custom_h_t_t_p_s_handler_0, str_0: str_0}
    parse_result_dotted_dict_0 = module_0.ParseResultDottedDict(**dict_0)
    var_0 = module_0.prepare_multipart(parse_result_dotted_dict_0)

def test_case_11():
    str_0 = 'LLMAb[`'
    connection_error_0 = module_0.ConnectionError()
    var_0 = module_0.generic_urlparse(str_0)

def test_case_12():
    str_0 = 'L%MAb[`'
    var_0 = module_0.generic_urlparse(str_0)

def test_case_13():
    str_0 = 'https://pypi.python.org/pypi/'
    var_0 = module_0.open_url(str_0)
    bool_0 = True
    var_1 = module_0.getpeercert(var_0, bool_0)

def test_case_14():
    int_0 = 2001
    int_1 = 11
    int_2 = 9
    int_3 = 1
    int_4 = 8
    int_5 = 47
    int_6 = 4
    int_7 = (int_0, int_1, int_2, int_3, int_4, int_5, int_6)
    str_0 = '-0000'
    var_0 = module_0.rfc2822_date_string(int_7, str_0)