# Automatically generated by Pynguin.
import tornado.httpclient as module_0
import _io as module_1
import tornado.httputil as module_2
import concurrent.futures._base as module_3
import tornado.ioloop as module_4
import datetime as module_5

def test_case_0():
    try:
        str_0 = 'HA(N1'
        h_t_t_p_client_0 = module_0.HTTPClient()
        h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'tw~wrTbpN BZn`X'
        h_t_t_p_client_0 = module_0.HTTPClient()
        dict_0 = {}
        h_t_t_p_client_0.close()
        bytes_i_o_0 = module_1.BytesIO(**dict_0)
        bool_0 = True
        h_t_t_p_request_0 = module_0.HTTPRequest(str_0, str_0, h_t_t_p_client_0, str_0, bytes_i_o_0, str_0, str_0, bool_0, bool_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'http://www.google.com'
        h_t_t_p_client_0 = module_0.HTTPClient()
        h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 9
        str_0 = 'eKK\np!|qkc*S'
        str_1 = '4b(D6t\\\r"dYBGY-<qL\'<'
        bool_0 = False
        h_t_t_p_request_0 = module_0.HTTPRequest(str_0, str_0, str_1, str_0, bool_0, bool_0)
        bytes_i_o_0 = module_1.BytesIO()
        int_1 = 2467
        float_0 = -454.69726
        h_t_t_p_response_0 = module_0.HTTPResponse(h_t_t_p_request_0, int_1, str_0, float_0)
        dict_0 = {}
        tuple_0 = (h_t_t_p_response_0, h_t_t_p_response_0, dict_0)
        h_t_t_p_response_1 = module_0.HTTPResponse(h_t_t_p_request_0, int_0, bytes_i_o_0, str_1, tuple_0)
        h_t_t_p_client_error_0 = module_0.HTTPClientError(int_0, h_t_t_p_response_1)
        str_2 = h_t_t_p_client_error_0.__str__()
        list_0 = []
        h_t_t_p_client_error_1 = module_0.HTTPClientError(int_1, list_0)
        int_2 = 1413
        h_t_t_p_client_error_2 = module_0.HTTPClientError(int_2)
        str_3 = ''
        h_t_t_p_client_0 = module_0.HTTPClient()
        h_t_t_p_client_0.close()
        h_t_t_p_response_2 = h_t_t_p_client_0.fetch(str_3)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = -274
        set_0 = {int_0, int_0, int_0, int_0}
        h_t_t_p_client_error_0 = module_0.HTTPClientError(int_0, set_0)
        str_0 = h_t_t_p_client_error_0.__str__()
        h_t_t_p_client_0 = module_0.HTTPClient()
        h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = -190
        int_1 = 9
        str_0 = 'eKt\np!qkc*>'
        bool_0 = False
        h_t_t_p_request_0 = module_0.HTTPRequest(str_0, str_0, str_0, str_0, bool_0, bool_0)
        bytes_i_o_0 = module_1.BytesIO()
        float_0 = -454.69726
        h_t_t_p_response_0 = module_0.HTTPResponse(h_t_t_p_request_0, int_0, str_0, float_0)
        dict_0 = {}
        tuple_0 = (h_t_t_p_response_0, h_t_t_p_response_0, dict_0)
        h_t_t_p_response_1 = module_0.HTTPResponse(h_t_t_p_request_0, int_1, bytes_i_o_0, str_0, tuple_0)
        h_t_t_p_client_error_0 = module_0.HTTPClientError(int_1, h_t_t_p_response_1)
        str_1 = h_t_t_p_client_error_0.__str__()
        list_0 = []
        h_t_t_p_client_error_1 = module_0.HTTPClientError(int_0, list_0)
        module_0.main()
    except BaseException:
        pass

def test_case_6():
    try:
        h_t_t_p_headers_0 = module_2.HTTPHeaders()
        module_0.main()
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'HA(N1'
        bytes_0 = b'\xab'
        list_0 = [str_0, str_0, str_0, bytes_0, bytes_0]
        str_1 = "#FObIk'^(l\r)muk7/C"
        str_2 = 'k$!5X(:6K'
        str_3 = "\t.JXcXxGYA\x0c%'UM"
        dict_0 = {str_1: list_0, str_2: bytes_0, str_3: list_0, str_1: str_0}
        h_t_t_p_client_0 = module_0.HTTPClient(list_0, **dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        async_h_t_t_p_client_0 = module_0.AsyncHTTPClient()
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'HA(N1'
        optional_0 = None
        bool_0 = True
        h_t_t_p_request_0 = module_0.HTTPRequest(str_0, str_0, optional_0, optional_0, str_0, bool_0, str_0, str_0)
        str_1 = 'GET'
        str_2 = 'J'
        dict_0 = {str_1: bool_0, str_1: str_1, str_2: h_t_t_p_request_0}
        h_t_t_p_client_0 = module_0.HTTPClient()
        h_t_t_p_response_0 = h_t_t_p_client_0.fetch(h_t_t_p_request_0, **dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '?l@OL5pfc r2,.T.F*{0'
        str_1 = 'DQ9l{;P1VRQxx?i2N#]'
        bool_0 = False
        float_0 = -559.0
        h_t_t_p_request_0 = module_0.HTTPRequest(str_1, str_0, str_1, str_0, bool_0, str_1, bool_0, float_0, str_1, bool_0, str_1, bool_0)
        int_0 = 4352
        list_0 = [str_0]
        str_2 = '!K6,oyaDC195'
        dict_0 = {str_1: float_0, str_2: float_0}
        h_t_t_p_response_0 = module_0.HTTPResponse(h_t_t_p_request_0, int_0, list_0, float_0, dict_0)
        h_t_t_p_response_0.rethrow()
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = 2369
        h_t_t_p_client_error_0 = module_0.HTTPClientError(int_0)
        str_0 = h_t_t_p_client_error_0.__str__()
        str_1 = '@'
        executor_0 = module_3.Executor()
        i_o_loop_0 = module_4.IOLoop()
        timedelta_0 = module_5.timedelta()
        dict_0 = {str_0: executor_0, str_0: executor_0, str_1: h_t_t_p_client_error_0}
        async_h_t_t_p_client_0 = module_0.AsyncHTTPClient()
        async_h_t_t_p_client_0.initialize()
        async_h_t_t_p_client_1 = module_0.AsyncHTTPClient(**dict_0)
        async_h_t_t_p_client_2 = module_0.AsyncHTTPClient()
        i_o_loop_0.clear_current()
        async_h_t_t_p_client_3 = async_h_t_t_p_client_2.__new__(async_h_t_t_p_client_1, **dict_0)
    except BaseException:
        pass

def test_case_12():
    try:
        int_0 = 2369
        h_t_t_p_client_error_0 = module_0.HTTPClientError(int_0)
        str_0 = h_t_t_p_client_error_0.__str__()
        str_1 = '@'
        executor_0 = module_3.Executor()
        i_o_loop_0 = module_4.IOLoop()
        timedelta_0 = module_5.timedelta()
        bool_0 = True
        dict_0 = {str_0: executor_0, str_0: executor_0, str_1: h_t_t_p_client_error_0}
        async_h_t_t_p_client_0 = module_0.AsyncHTTPClient()
        async_h_t_t_p_client_0.initialize()
        async_h_t_t_p_client_1 = async_h_t_t_p_client_0.__new__(timedelta_0, bool_0, **dict_0)
    except BaseException:
        pass