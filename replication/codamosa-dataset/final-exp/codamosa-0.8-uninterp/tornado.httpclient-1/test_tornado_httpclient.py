# Automatically generated by Pynguin.
import tornado.httpclient as module_0

def test_case_0():
    pass

def test_case_1():
    h_t_t_p_client_0 = module_0.HTTPClient()

def test_case_2():
    h_t_t_p_client_0 = module_0.HTTPClient()

def test_case_3():
    h_t_t_p_client_0 = module_0.HTTPClient()

def test_case_4():
    str_0 = 'url'
    h_t_t_p_request_0 = module_0.HTTPRequest(str_0)

def test_case_5():
    str_0 = 'http://www.google.com/'
    h_t_t_p_client_0 = module_0.HTTPClient()
    h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0)

def test_case_6():
    str_0 = 'url'
    h_t_t_p_request_0 = module_0.HTTPRequest(str_0)
    int_0 = 207
    h_t_t_p_response_0 = module_0.HTTPResponse(h_t_t_p_request_0, int_0, str_0)
    h_t_t_p_response_0.rethrow()

def test_case_7():
    int_0 = -299
    h_t_t_p_client_error_0 = module_0.HTTPClientError(int_0)

def test_case_8():
    int_0 = -1795
    str_0 = 'XL{T>!1VF%uX(Zo'
    h_t_t_p_client_error_0 = module_0.HTTPClientError(int_0, str_0, str_0)
    str_1 = h_t_t_p_client_error_0.__str__()