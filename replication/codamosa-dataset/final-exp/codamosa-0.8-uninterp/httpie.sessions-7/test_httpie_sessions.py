# Automatically generated by Pynguin.
import pathlib as module_0
import httpie.sessions as module_1
import httpie.cli.dicts as module_2

def test_case_0():
    pass

def test_case_1():
    path_0 = module_0.Path()
    str_0 = '~L>Fuu^\x0cUnV3a<\x0cz'
    session_0 = module_1.get_httpie_session(path_0, str_0, str_0, str_0)
    var_0 = session_0.remove_cookies(str_0)

def test_case_2():
    str_0 = '$.v='
    path_0 = module_0.Path()
    str_1 = ''
    str_2 = 'PROTOCOL:PROXY_URL'
    session_0 = module_1.get_httpie_session(path_0, str_1, str_1, str_2)
    var_0 = session_0.remove_cookies(str_0)

def test_case_3():
    str_0 = "eT|Nd#YD(|Z}\nj'-"
    session_0 = module_1.Session(str_0)

def test_case_4():
    path_0 = module_0.Path()
    str_0 = 'iz~C,'
    str_1 = "UX4/'\t,9ij##"
    dict_0 = {str_0: str_0, str_1: str_0}
    request_headers_dict_0 = module_2.RequestHeadersDict(dict_0, **dict_0)
    str_2 = '\n    Content compressed (encoded) with Deflate algorithm.\n    The Content-Encoding header is set to deflate.\n\n    Compression is skipped if it appears that compression ratio is\n    negative. Compression can be forced by repeating the argument.\n\n    '
    session_0 = module_1.get_httpie_session(path_0, str_2, str_2, str_2)
    var_0 = session_0.update_headers(request_headers_dict_0)
    session_1 = module_1.Session(path_0)

def test_case_5():
    path_0 = module_0.Path()
    str_0 = ''
    session_0 = module_1.Session(str_0)
    var_0 = session_0.remove_cookies(str_0)

def test_case_6():
    bytes_0 = b'\x97\xf6\x03\xdcO\x0f\x7f\xfaTv!(\xb4i\xd0\xc7\x0f\x1b:'
    path_0 = module_0.Path()
    session_0 = module_1.Session(path_0)
    var_0 = session_0.remove_cookies(bytes_0)

def test_case_7():
    str_0 = 'Content-Type'
    str_1 = 'Accept'
    str_2 = 'application/json'
    str_3 = 'text/plain'
    str_4 = {str_0: str_2, str_1: str_3}
    request_headers_dict_0 = module_2.RequestHeadersDict(str_4)
    str_5 = 'foo.json'
    session_0 = module_1.Session(str_5)
    var_0 = session_0.update_headers(request_headers_dict_0)

def test_case_8():
    str_0 = 'test_remove_cookies.json'
    session_0 = module_1.Session(str_0)
    str_1 = 'Cookie'
    str_2 = 'test1=1; test2=2; test3=3'
    str_3 = {str_1: str_2}
    request_headers_dict_0 = module_2.RequestHeadersDict(str_3)
    var_0 = session_0.update_headers(request_headers_dict_0)
    var_1 = session_0.cookies
    var_2 = len(var_1)
    var_3 = session_0.save()

def test_case_9():
    str_0 = 'Host'
    str_1 = 'example.com'
    str_2 = (str_0, str_1)
    str_3 = 'User-Agent'
    str_4 = '\t0HTTPie/1.0.2'
    str_5 = (str_3, str_4)
    str_6 = 'Accept-Encoding'
    str_7 = 'gzip, deflate'
    str_8 = (str_6, str_7)
    str_9 = 'Connection'
    str_10 = 'keep-alive'
    str_11 = (str_9, str_10)
    str_12 = 'Accept'
    str_13 = '*/*'
    str_14 = (str_12, str_13)
    str_15 = 'Content-Length'
    str_16 = (str_15, str_1)
    str_17 = 'Content-Type'
    str_18 = 'application/x-www-form-urlencoded'
    str_19 = (str_17, str_18)
    str_20 = 'If-Modified-Since'
    str_21 = 'Mon, 27 Jul 2009 01:15:26 GMT'
    str_22 = (str_20, str_21)
    str_23 = 'C@ookie'
    dict_0 = {}
    list_0 = []
    path_0 = module_0.Path(*list_0)
    session_0 = module_1.get_httpie_session(path_0, str_4, str_17, str_13)
    var_0 = session_0.remove_cookies(dict_0)
    str_24 = 'name=value; name_two=value_two'
    str_25 = (str_23, str_24)
    str_26 = [str_2, str_5, str_8, str_11, str_14, str_16, str_19, str_22, str_25]
    request_headers_dict_0 = module_2.RequestHeadersDict(str_26)
    str_27 = '/tmp/foo'
    session_1 = module_1.get_httpie_session(path_0, str_19, str_23, str_27)
    var_1 = session_1.update_headers(request_headers_dict_0)
    str_28 = 'headers'
    var_2 = session_1[str_28]
    var_3 = len(var_2)

def test_case_10():
    str_0 = 'test_remove_cookies.json'
    session_0 = module_1.Session(str_0)
    str_1 = 'Cookie'
    str_2 = 'test1=1; test2=2; test3=3'
    str_3 = {str_1: str_2}
    request_headers_dict_0 = module_2.RequestHeadersDict(str_3)
    var_0 = session_0.update_headers(request_headers_dict_0)
    str_4 = 'test1'
    str_5 = 'test3'
    str_6 = [str_4, str_5]
    var_1 = session_0.remove_cookies(str_6)
    var_2 = session_0.cookies
    var_3 = len(var_2)
    var_4 = session_0.save()