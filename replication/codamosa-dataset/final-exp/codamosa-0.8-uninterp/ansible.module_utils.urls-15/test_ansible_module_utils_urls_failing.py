# Automatically generated by Pynguin.
import ansible.module_utils.urls as module_0

def test_case_0():
    try:
        str_0 = 'https://localhost'
        var_0 = module_0.open_url(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '  hosts (%d):'
        dict_0 = {str_0: str_0}
        list_0 = [str_0, str_0, dict_0, str_0]
        proxy_error_0 = module_0.ProxyError(*list_0)
        int_0 = -1751
        s_s_l_validation_handler_0 = module_0.SSLValidationHandler(proxy_error_0, int_0)
        float_0 = 2070.078
        h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler(dict_0, float_0, dict_0)
        var_0 = h_t_t_p_s_client_auth_handler_0.https_open(s_s_l_validation_handler_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '.%pGufUUn\n'
        unix_h_t_t_p_s_connection_0 = module_0.UnixHTTPSConnection(str_0)
        var_0 = unix_h_t_t_p_s_connection_0.connect()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'fetch_url_tZt.txt'
        var_0 = module_0.atexit_remove_file(str_0)
        list_0 = [str_0, str_0, str_0, str_0]
        unix_h_t_t_p_connection_0 = module_0.UnixHTTPConnection(list_0)
        var_1 = module_0.getpeercert(unix_h_t_t_p_connection_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'http://ocalhot'
        var_0 = module_0.open_url(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'*\x1b$\xba\x8c\xf29zV\xa4I\xdb\xa7\xde'
        float_0 = -1182.092152
        connection_error_0 = module_0.ConnectionError()
        tuple_0 = (connection_error_0,)
        set_0 = {float_0, tuple_0}
        unix_h_t_t_p_handler_0 = module_0.UnixHTTPHandler(set_0)
        s_s_l_validation_handler_0 = module_0.SSLValidationHandler(float_0, unix_h_t_t_p_handler_0)
        var_0 = module_0.get_channel_binding_cert_hash(bytes_0)
        unix_h_t_t_p_connection_0 = module_0.UnixHTTPConnection(s_s_l_validation_handler_0)
        var_1 = unix_h_t_t_p_connection_0.__call__()
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '\r)wRR<\tqKbt'
        float_0 = 900.9
        unix_h_t_t_p_handler_0 = module_0.UnixHTTPHandler(float_0)
        str_1 = 'vmkernel'
        str_2 = None
        str_3 = 'izTY~_(te'
        dict_0 = {str_0: unix_h_t_t_p_handler_0, str_1: unix_h_t_t_p_handler_0, str_2: unix_h_t_t_p_handler_0, str_3: float_0}
        parse_result_dotted_dict_0 = module_0.ParseResultDottedDict(**dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        dict_0 = {}
        parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()
        no_s_s_l_error_0 = module_0.NoSSLError(**dict_0)
        str_0 = 'H'
        var_0 = parse_result_dotted_dict_0.as_list()
        custom_h_t_t_p_s_connection_0 = None
        s_s_l_validation_handler_0 = module_0.SSLValidationHandler(str_0, custom_h_t_t_p_s_connection_0)
        str_1 = '-eb|8+jcpe#h'
        var_1 = s_s_l_validation_handler_0.get_ca_certs()
        request_0 = module_0.Request(dict_0, str_1)
        var_2 = request_0.patch(dict_0, **dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = -4952
        var_0 = module_0.generic_urlparse(int_0)
    except BaseException:
        pass

def test_case_9():
    try:
        no_s_s_l_error_0 = module_0.NoSSLError()
        unix_h_t_t_p_handler_0 = None
        dict_0 = {unix_h_t_t_p_handler_0: unix_h_t_t_p_handler_0, unix_h_t_t_p_handler_0: unix_h_t_t_p_handler_0, unix_h_t_t_p_handler_0: unix_h_t_t_p_handler_0}
        var_0 = module_0.rfc2822_date_string(dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bytes_0 = b';h{\xac:M\x1e\xaf\xe3c\xcaA\x9ce'
        list_0 = [bytes_0]
        list_1 = [bytes_0, bytes_0, bytes_0]
        str_0 = 'nodump'
        request_0 = module_0.Request(bytes_0, list_0, list_0, list_1, str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        dict_0 = {}
        h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler(**dict_0)
        int_0 = -1234
        no_s_s_l_error_0 = module_0.NoSSLError()
        var_0 = module_0.basic_auth_header(int_0, no_s_s_l_error_0)
        list_0 = None
        custom_h_t_t_p_s_connection_0 = module_0.CustomHTTPSConnection(*list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        dict_0 = {}
        parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()
        no_s_s_l_error_0 = module_0.NoSSLError(**dict_0)
        str_0 = 'H'
        custom_h_t_t_p_s_connection_0 = None
        s_s_l_validation_handler_0 = module_0.SSLValidationHandler(str_0, custom_h_t_t_p_s_connection_0)
        var_0 = module_0.url_argument_spec()
        str_1 = '-eb|8+9jcpe#h'
        var_1 = s_s_l_validation_handler_0.get_ca_certs()
        request_0 = module_0.Request(dict_0, str_1)
        var_2 = request_0.patch(s_s_l_validation_handler_0)
    except BaseException:
        pass

def test_case_13():
    try:
        request_0 = module_0.Request()
        str_0 = 'GET'
        str_1 = 'https://ww.google.com'
        var_0 = request_0.open(str_0, str_1)
        str_2 = 'ftp'
        unix_h_t_t_p_handler_0 = module_0.UnixHTTPHandler(str_2)
        parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()
        h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler(parse_result_dotted_dict_0)
        connection_error_0 = module_0.ConnectionError()
        unix_h_t_t_p_connection_0 = module_0.UnixHTTPConnection(connection_error_0)
        bytes_0 = b'\x13#'
        float_0 = 512.0
        request_with_method_0 = module_0.RequestWithMethod(unix_h_t_t_p_connection_0, str_2, bytes_0, float_0)
    except BaseException:
        pass

def test_case_14():
    try:
        dict_0 = {}
        bool_0 = False
        str_0 = '@ut3:!uC9%j+!t.'
        bytes_0 = b'n\xdc\x0c\xf9w\xf1\xe4\x9e\xb7\xf3\xea\xc4;\x92\x97{\xb8'
        str_1 = '!f|:yBA=AQyWRf!$E\x0b$A'
        unix_h_t_t_p_s_connection_0 = module_0.UnixHTTPSConnection(bytes_0)
        var_0 = module_0.open_url(bytes_0, dict_0, bool_0, str_0, str_1, bytes_0, unix_h_t_t_p_s_connection_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = '5'
        bool_0 = False
        list_0 = []
        s_s_l_validation_handler_0 = module_0.SSLValidationHandler(str_0, list_0)
        var_0 = s_s_l_validation_handler_0.http_request(bool_0)
    except BaseException:
        pass

def test_case_16():
    try:
        dict_0 = {}
        request_0 = module_0.Request(dict_0, dict_0)
        var_0 = request_0.patch(dict_0, **dict_0)
    except BaseException:
        pass

def test_case_17():
    try:
        float_0 = 5197.53671
        proxy_error_0 = module_0.ProxyError()
        tuple_0 = ()
        s_s_l_validation_error_0 = module_0.SSLValidationError()
        bytes_0 = b'\xcd\xd1\xbf\xa6\x038I\x16W['
        var_0 = module_0.fetch_url(float_0, proxy_error_0, tuple_0, s_s_l_validation_error_0, bytes_0)
    except BaseException:
        pass

def test_case_18():
    try:
        dict_0 = {}
        unix_h_t_t_p_connection_0 = module_0.UnixHTTPConnection(dict_0)
        str_0 = '\\*Joz2ur4q&'
        list_0 = [dict_0, str_0, str_0]
        unix_h_t_t_p_s_connection_0 = module_0.UnixHTTPSConnection(list_0)
        s_s_l_validation_handler_0 = module_0.SSLValidationHandler(unix_h_t_t_p_connection_0, dict_0, unix_h_t_t_p_s_connection_0)
        var_0 = s_s_l_validation_handler_0.get_ca_certs()
    except BaseException:
        pass

def test_case_19():
    try:
        custom_h_t_t_p_s_handler_0 = module_0.CustomHTTPSHandler()
        str_0 = 'caCb9?JYuSl'
        str_1 = '^v!X[HQlI#'
        dict_0 = {str_1: str_0, str_1: str_0}
        var_0 = module_0.build_ssl_validation_error(custom_h_t_t_p_s_handler_0, custom_h_t_t_p_s_handler_0, dict_0)
    except BaseException:
        pass

def test_case_20():
    try:
        proxy_error_0 = module_0.ProxyError()
        list_0 = [proxy_error_0, proxy_error_0, proxy_error_0]
        s_s_l_validation_error_0 = module_0.SSLValidationError(*list_0)
        bool_0 = False
        connection_error_0 = module_0.ConnectionError()
        unix_h_t_t_p_handler_0 = module_0.UnixHTTPHandler(bool_0)
        dict_0 = {}
        list_1 = [dict_0, connection_error_0]
        no_s_s_l_error_0 = module_0.NoSSLError(*list_1)
        request_0 = module_0.Request(bool_0, connection_error_0, unix_h_t_t_p_handler_0, dict_0, no_s_s_l_error_0)
        var_0 = request_0.post(s_s_l_validation_error_0)
    except BaseException:
        pass

def test_case_21():
    try:
        float_0 = 512.0
        list_0 = []
        s_s_l_validation_error_0 = module_0.SSLValidationError(*list_0)
        str_0 = ':#b[xz2E.?7@vQ'
        proxy_error_0 = module_0.ProxyError(*list_0)
        s_s_l_validation_handler_0 = module_0.SSLValidationHandler(s_s_l_validation_error_0, str_0)
        set_0 = set()
        dict_0 = None
        var_0 = s_s_l_validation_handler_0.make_context(set_0, dict_0)
        s_s_l_validation_handler_1 = module_0.SSLValidationHandler(float_0, s_s_l_validation_handler_0)
        var_1 = s_s_l_validation_handler_0.get_ca_certs()
        float_1 = -2368.99466
        list_1 = [var_1, float_1]
        var_2 = module_0.get_channel_binding_cert_hash(list_1)
        no_s_s_l_error_0 = module_0.NoSSLError(*list_0)
        custom_h_t_t_p_s_handler_0 = module_0.CustomHTTPSHandler()
        var_3 = s_s_l_validation_handler_1.detect_no_proxy(s_s_l_validation_handler_1)
        h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler(custom_h_t_t_p_s_handler_0)
        unix_h_t_t_p_connection_0 = module_0.UnixHTTPConnection(list_1)
        var_4 = module_0.url_argument_spec()
        unix_h_t_t_p_s_connection_0 = module_0.UnixHTTPSConnection(h_t_t_p_s_client_auth_handler_0)
        tuple_0 = (unix_h_t_t_p_s_connection_0, list_1)
        request_0 = module_0.Request(set_0, tuple_0)
        var_5 = unix_h_t_t_p_s_connection_0.__call__(*list_0)
    except BaseException:
        pass

def test_case_22():
    try:
        request_0 = module_0.Request()
        str_0 = 'V{8?<g\nt*DB//=-<X}'
        var_0 = request_0.open(str_0, request_0, str_0, str_0)
    except BaseException:
        pass

def test_case_23():
    try:
        unix_h_t_t_p_connection_0 = None
        float_0 = 882.642447
        s_s_l_validation_error_0 = module_0.SSLValidationError()
        dict_0 = {s_s_l_validation_error_0: s_s_l_validation_error_0}
        s_s_l_validation_handler_0 = module_0.SSLValidationHandler(s_s_l_validation_error_0, dict_0)
        s_s_l_validation_handler_1 = module_0.SSLValidationHandler(float_0, float_0, s_s_l_validation_handler_0)
        var_0 = s_s_l_validation_handler_1.validate_proxy_response(unix_h_t_t_p_connection_0)
    except BaseException:
        pass

def test_case_24():
    try:
        float_0 = 512.0
        list_0 = [float_0]
        str_0 = ' T]D].o'
        var_0 = module_0.generic_urlparse(str_0)
        no_s_s_l_error_0 = module_0.NoSSLError(*list_0)
        bytes_0 = b'\x08c\x85\xa3 e\xc9\xd5\xcc\xae\xceK\xf8\x81\x07'
        float_1 = -5879.259248
        unix_h_t_t_p_s_connection_0 = module_0.UnixHTTPSConnection(float_1)
        unix_h_t_t_p_connection_0 = module_0.UnixHTTPConnection(unix_h_t_t_p_s_connection_0)
        missing_module_error_0 = module_0.MissingModuleError(bytes_0, unix_h_t_t_p_connection_0)
        unix_h_t_t_p_connection_1 = module_0.UnixHTTPConnection(missing_module_error_0)
        var_1 = unix_h_t_t_p_connection_1.connect()
    except BaseException:
        pass

def test_case_25():
    try:
        dict_0 = {}
        parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()
        no_s_s_l_error_0 = module_0.NoSSLError(**dict_0)
        str_0 = 'H'
        bool_0 = True
        list_0 = [no_s_s_l_error_0, str_0, no_s_s_l_error_0]
        unix_h_t_t_p_handler_0 = module_0.UnixHTTPHandler(list_0)
        var_0 = unix_h_t_t_p_handler_0.http_open(bool_0)
    except BaseException:
        pass

def test_case_26():
    try:
        request_0 = module_0.Request()
        str_0 = 'GET'
        str_1 = 'https://ww.google.com'
        var_0 = request_0.open(str_0, str_1)
        list_0 = [str_0, var_0, str_0, request_0]
        float_0 = 3497.831
        str_2 = 'ftp'
        unix_h_t_t_p_handler_0 = module_0.UnixHTTPHandler(str_2)
        int_0 = -849
        parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()
        h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler(parse_result_dotted_dict_0)
        dict_0 = {h_t_t_p_s_client_auth_handler_0: str_2, float_0: list_0, int_0: float_0}
        str_3 = 'X)o.[a\x0b/GHw1LWaR@'
        str_4 = 'Ek"!'
        connection_error_0 = module_0.ConnectionError()
        unix_h_t_t_p_connection_0 = module_0.UnixHTTPConnection(connection_error_0)
        dict_1 = {str_3: str_2, str_4: unix_h_t_t_p_connection_0}
        var_1 = module_0.fetch_file(unix_h_t_t_p_handler_0, int_0, dict_0, dict_1)
    except BaseException:
        pass

def test_case_27():
    try:
        str_0 = 'C 4<\x0c Dq'
        var_0 = module_0.open_url(str_0)
    except BaseException:
        pass

def test_case_28():
    try:
        float_0 = 512.0
        list_0 = [float_0]
        s_s_l_validation_error_0 = module_0.SSLValidationError(*list_0)
        proxy_error_0 = module_0.ProxyError(*list_0)
        dict_0 = None
        list_1 = [list_0]
        var_0 = module_0.get_channel_binding_cert_hash(list_1)
        no_s_s_l_error_0 = module_0.NoSSLError(*list_0)
        bytes_0 = b'\xae\xd1\xd2Z|\xe6J\xba\xfc\xf2\xa7\xbc4c+\x8c\xca\xa9\xc7\xa9'
        missing_module_error_0 = module_0.MissingModuleError(dict_0, bytes_0)
        unix_h_t_t_p_s_connection_0 = module_0.UnixHTTPSConnection(missing_module_error_0)
        var_1 = module_0.prepare_multipart(unix_h_t_t_p_s_connection_0)
    except BaseException:
        pass

def test_case_29():
    try:
        float_0 = 511.7549736855975
        list_0 = [float_0]
        dict_0 = {}
        no_s_s_l_error_0 = module_0.NoSSLError(*list_0)
        custom_h_t_t_p_s_handler_0 = module_0.CustomHTTPSHandler()
        parse_result_dotted_dict_0 = module_0.ParseResultDottedDict(**dict_0)
        bytes_0 = b'A\xf8\x03r<%'
        request_0 = module_0.Request(parse_result_dotted_dict_0, custom_h_t_t_p_s_handler_0, bytes_0, float_0, list_0, list_0, parse_result_dotted_dict_0, no_s_s_l_error_0)
        str_0 = 'K:*3'
        var_0 = request_0.patch(str_0)
    except BaseException:
        pass

def test_case_30():
    try:
        str_0 = ')H]w%z1\x0bz\t'
        var_0 = module_0.getpeercert(str_0)
    except BaseException:
        pass

def test_case_31():
    try:
        float_0 = 2517.8
        list_0 = [float_0]
        dict_0 = {}
        no_s_s_l_error_0 = module_0.NoSSLError(*list_0)
        bytes_0 = b"bN\x190\xdb\xb5J\xbaY\xe9'"
        var_0 = module_0.atexit_remove_file(bytes_0)
        custom_h_t_t_p_s_handler_0 = module_0.CustomHTTPSHandler()
        parse_result_dotted_dict_0 = module_0.ParseResultDottedDict(**dict_0)
        bytes_1 = b'u\xf8k\xe9<%'
        request_0 = module_0.Request(parse_result_dotted_dict_0, custom_h_t_t_p_s_handler_0, bytes_1, float_0, list_0, list_0, parse_result_dotted_dict_0, no_s_s_l_error_0)
        var_1 = request_0.put(bytes_1)
    except BaseException:
        pass

def test_case_32():
    try:
        dict_0 = {}
        str_0 = 'k'
        request_0 = module_0.Request(dict_0, str_0)
        str_1 = 'kQB@}2\r%H'
        var_0 = request_0.options(str_1, **dict_0)
    except BaseException:
        pass

def test_case_33():
    try:
        parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()
        int_0 = 254
        bool_0 = True
        str_0 = '4$='
        s_s_l_validation_handler_0 = module_0.SSLValidationHandler(bool_0, str_0)
        var_0 = s_s_l_validation_handler_0.make_context(parse_result_dotted_dict_0, int_0)
    except BaseException:
        pass

def test_case_34():
    try:
        request_0 = module_0.Request()
        str_0 = 'GET'
        str_1 = 'https://www.google.com'
        var_0 = request_0.open(str_0, str_1)
        list_0 = [str_0, var_0, str_0, request_0]
        var_1 = request_0.get(list_0)
    except BaseException:
        pass

def test_case_35():
    try:
        float_0 = 512.0
        list_0 = [float_0]
        s_s_l_validation_error_0 = module_0.SSLValidationError(*list_0)
        dict_0 = {}
        str_0 = 'i#b[xTz2E\n?7@vQ'
        proxy_error_0 = module_0.ProxyError(*list_0)
        s_s_l_validation_handler_0 = module_0.SSLValidationHandler(s_s_l_validation_error_0, str_0)
        set_0 = set()
        dict_1 = None
        var_0 = s_s_l_validation_handler_0.make_context(set_0, dict_1)
        s_s_l_validation_handler_1 = module_0.SSLValidationHandler(float_0, s_s_l_validation_handler_0)
        var_1 = s_s_l_validation_handler_0.get_ca_certs()
        no_s_s_l_error_0 = module_0.NoSSLError(*list_0)
        custom_h_t_t_p_s_handler_0 = module_0.CustomHTTPSHandler()
        h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler(custom_h_t_t_p_s_handler_0)
        list_1 = []
        unix_h_t_t_p_connection_0 = module_0.UnixHTTPConnection(list_1)
        proxy_error_1 = module_0.ProxyError(**dict_0)
        var_2 = module_0.url_argument_spec()
        unix_h_t_t_p_s_connection_0 = module_0.UnixHTTPSConnection(h_t_t_p_s_client_auth_handler_0)
        tuple_0 = (unix_h_t_t_p_s_connection_0, list_1)
        request_0 = module_0.Request(set_0, tuple_0)
        var_3 = request_0.delete(set_0)
    except BaseException:
        pass

def test_case_36():
    try:
        float_0 = 512.0
        list_0 = [float_0]
        s_s_l_validation_error_0 = module_0.SSLValidationError(*list_0)
        str_0 = ':#b[xz2E\n?7@vQ'
        proxy_error_0 = module_0.ProxyError(*list_0)
        s_s_l_validation_handler_0 = module_0.SSLValidationHandler(s_s_l_validation_error_0, str_0)
        s_s_l_validation_handler_1 = module_0.SSLValidationHandler(float_0, s_s_l_validation_handler_0)
        var_0 = s_s_l_validation_handler_0.get_ca_certs()
        float_1 = -2368.99466
        list_1 = [var_0, float_1]
        var_1 = module_0.get_channel_binding_cert_hash(list_1)
        no_s_s_l_error_0 = module_0.NoSSLError(*list_0)
        custom_h_t_t_p_s_handler_0 = module_0.CustomHTTPSHandler()
        var_2 = s_s_l_validation_handler_1.detect_no_proxy(s_s_l_validation_handler_1)
        list_2 = []
        unix_h_t_t_p_connection_0 = module_0.UnixHTTPConnection(list_2)
        var_3 = module_0.url_argument_spec()
        missing_module_error_0 = module_0.MissingModuleError(no_s_s_l_error_0, list_1)
        var_4 = module_0.build_ssl_validation_error(list_1, custom_h_t_t_p_s_handler_0, list_1, list_0)
    except BaseException:
        pass

def test_case_37():
    try:
        var_0 = module_0.unix_socket_patch_httpconnection_connect()
        set_0 = set()
        custom_h_t_t_p_s_handler_0 = module_0.CustomHTTPSHandler()
        list_0 = []
        var_1 = module_0.url_argument_spec()
        h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler()
        unix_h_t_t_p_s_connection_0 = module_0.UnixHTTPSConnection(h_t_t_p_s_client_auth_handler_0)
        tuple_0 = (unix_h_t_t_p_s_connection_0, list_0)
        request_0 = module_0.Request(set_0, tuple_0)
        parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()
        s_s_l_validation_error_0 = module_0.SSLValidationError()
        var_2 = request_0.head(s_s_l_validation_error_0)
    except BaseException:
        pass

def test_case_38():
    try:
        float_0 = 512.0
        list_0 = [float_0]
        var_0 = module_0.unix_socket_patch_httpconnection_connect()
        s_s_l_validation_error_0 = module_0.SSLValidationError(*list_0)
        str_0 = 'i#b[xTz2E\n?7@vQ'
        proxy_error_0 = module_0.ProxyError(*list_0)
        s_s_l_validation_handler_0 = module_0.SSLValidationHandler(list_0, str_0, var_0)
        set_0 = set()
        dict_0 = None
        var_1 = s_s_l_validation_handler_0.make_context(set_0, dict_0)
    except BaseException:
        pass

def test_case_39():
    try:
        dict_0 = {}
        str_0 = ''
        request_0 = module_0.Request(dict_0, str_0)
        var_0 = request_0.patch(str_0)
    except BaseException:
        pass

def test_case_40():
    try:
        float_0 = 513.0334163015897
        list_0 = [float_0]
        set_0 = set()
        no_s_s_l_error_0 = module_0.NoSSLError(*list_0)
        custom_h_t_t_p_s_handler_0 = module_0.CustomHTTPSHandler()
        list_1 = None
        parse_result_dotted_dict_0 = module_0.ParseResultDottedDict()
        bytes_0 = b'A\xf8\x03r<%'
        str_0 = ''
        s_s_l_validation_error_0 = module_0.SSLValidationError(*list_0)
        s_s_l_validation_handler_0 = module_0.SSLValidationHandler(bytes_0, set_0)
        request_0 = module_0.Request(str_0, list_1, s_s_l_validation_error_0, s_s_l_validation_handler_0, list_1)
        var_0 = request_0.patch(str_0, s_s_l_validation_handler_0)
    except BaseException:
        pass

def test_case_41():
    try:
        no_s_s_l_error_0 = module_0.NoSSLError()
        float_0 = 482.5352259685467
        str_0 = ':#b&[z2E\n?7@vQ'
        int_0 = -2048
        s_s_l_validation_handler_0 = module_0.SSLValidationHandler(int_0, str_0)
        var_0 = s_s_l_validation_handler_0.get_ca_certs()
        custom_h_t_t_p_s_handler_0 = None
        dict_0 = None
        bool_0 = False
        list_0 = [float_0, float_0]
        h_t_t_p_s_client_auth_handler_0 = module_0.HTTPSClientAuthHandler(bool_0, list_0, custom_h_t_t_p_s_handler_0)
        custom_h_t_t_p_s_handler_1 = module_0.CustomHTTPSHandler(bool_0)
        unix_h_t_t_p_handler_0 = module_0.UnixHTTPHandler(float_0)
        dict_1 = {str_0: dict_0}
        var_1 = module_0.open_url(h_t_t_p_s_client_auth_handler_0, no_s_s_l_error_0, h_t_t_p_s_client_auth_handler_0, custom_h_t_t_p_s_handler_0, custom_h_t_t_p_s_handler_1, dict_0, int_0, unix_h_t_t_p_handler_0, dict_1)
    except BaseException:
        pass

def test_case_42():
    try:
        float_0 = 512.0
        list_0 = [float_0]
        str_0 = ' \n3DZ.'
        var_0 = module_0.generic_urlparse(str_0)
        no_s_s_l_error_0 = module_0.NoSSLError(*list_0)
        bytes_0 = b'\x08c\x85\xa3 e\xc9\xd5\xcc\xae\xceK\xf8\x81\x07'
        float_1 = -5879.259248
        unix_h_t_t_p_s_connection_0 = module_0.UnixHTTPSConnection(float_1)
        unix_h_t_t_p_connection_0 = module_0.UnixHTTPConnection(unix_h_t_t_p_s_connection_0)
        missing_module_error_0 = module_0.MissingModuleError(bytes_0, unix_h_t_t_p_connection_0)
        unix_h_t_t_p_connection_1 = module_0.UnixHTTPConnection(missing_module_error_0)
        var_1 = unix_h_t_t_p_connection_1.connect()
    except BaseException:
        pass

def test_case_43():
    try:
        request_0 = module_0.Request()
        str_0 = 'https://www.google.com'
        var_0 = request_0.open(str_0, str_0)
    except BaseException:
        pass