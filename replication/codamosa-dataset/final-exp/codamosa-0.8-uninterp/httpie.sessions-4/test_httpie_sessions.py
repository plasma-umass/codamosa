# Automatically generated by Pynguin.
import httpie.cli.dicts as module_0
import pathlib as module_1
import httpie.sessions as module_2

def test_case_0():
    pass

def test_case_1():
    request_headers_dict_0 = module_0.RequestHeadersDict()
    path_0 = module_1.Path()
    str_0 = 'Content-Encoding'
    str_1 = 'G'
    session_0 = module_2.get_httpie_session(path_0, str_0, str_0, str_1)
    var_0 = session_0.update_headers(request_headers_dict_0)

def test_case_2():
    request_headers_dict_0 = module_0.RequestHeadersDict()
    str_0 = ''
    dict_0 = {str_0: str_0}
    path_0 = module_1.Path(**dict_0)
    str_1 = "W{D#sA)C|9'm9k"
    session_0 = module_2.get_httpie_session(path_0, str_0, str_0, str_1)
    str_2 = "2i'P<()ZCLTH=)6\x0bm`"
    session_1 = module_2.Session(str_2)
    var_0 = session_0.remove_cookies(request_headers_dict_0)

def test_case_3():
    str_0 = '6W,?2'
    session_0 = module_2.Session(str_0)

def test_case_4():
    str_0 = 'gRjfbGM{$!:s'
    str_1 = 'txv'
    dict_0 = {str_0: str_0, str_0: str_1, str_1: str_1}
    request_headers_dict_0 = module_0.RequestHeadersDict(**dict_0)
    path_0 = module_1.Path()
    session_0 = module_2.get_httpie_session(path_0, str_0, str_0, str_0)
    var_0 = session_0.update_headers(request_headers_dict_0)

def test_case_5():
    str_0 = 'path/to/session.json'
    session_0 = module_2.Session(str_0)
    var_0 = session_0.remove_cookies(str_0)

def test_case_6():
    str_0 = 'foo'
    session_0 = module_2.Session(str_0)
    str_1 = 'Accept-Language'
    str_2 = 'Content-Type'
    str_3 = 'If-Modified-Since'
    str_4 = 'User-Agent'
    str_5 = 'zh-CN,zh;q=0.9'
    str_6 = 'application/json'
    str_7 = 'Tue, 17 Apr 2018 15:08:31 GMT'
    str_8 = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    str_9 = {str_1: str_5, str_2: str_6, str_3: str_7, str_4: str_8}
    var_0 = session_0.update_headers(str_9)

def test_case_7():
    str_0 = ''
    session_0 = module_2.Session(str_0)
    str_1 = 'test'
    str_2 = {str_1: str_1}
    var_0 = session_0.update_headers(str_2)
    var_1 = None
    var_2 = {str_1: var_1}
    var_3 = session_0.update_headers(var_2)

def test_case_8():
    str_0 = 'test_Session_update_headers'
    session_0 = module_2.Session(str_0)
    str_1 = 'Accept'
    str_2 = 'User-agent'
    str_3 = 'text/html'
    str_4 = {str_1: str_3, str_2: str_1}
    var_0 = session_0.update_headers(str_4)

def test_case_9():
    str_0 = ''
    session_0 = module_2.Session(str_0)
    request_headers_dict_0 = module_0.RequestHeadersDict()
    str_1 = 'Content-Type'
    str_2 = 'If-None-Match'
    str_3 = 'text/html'
    str_4 = '1234567'
    str_5 = {str_1: str_3, str_2: str_4}
    var_0 = request_headers_dict_0.update(str_5)
    str_6 = 'User-Agent'
    str_7 = 'HTTPie/0.9.9'
    str_8 = {str_6: str_7}
    var_1 = request_headers_dict_0.update(str_8)
    var_2 = session_0.update_headers(request_headers_dict_0)
    var_3 = session_0.headers
    var_4 = print(var_3)
    str_9 = 'cookies'
    var_5 = session_0[str_9]
    var_6 = print(var_5)
    str_10 = 'headers'
    var_7 = session_0[str_10]
    var_8 = len(var_7)
    var_9 = session_0[str_9]
    var_10 = len(var_9)