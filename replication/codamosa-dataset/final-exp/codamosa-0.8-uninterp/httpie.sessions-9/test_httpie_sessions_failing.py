# Automatically generated by Pynguin.
import httpie.cli.dicts as module_0
import pathlib as module_1
import httpie.sessions as module_2

def test_case_0():
    try:
        str_0 = '"SmaLB/zfz;'
        request_headers_dict_0 = module_0.RequestHeadersDict()
        path_0 = module_1.Path()
        session_0 = module_2.get_httpie_session(path_0, str_0, str_0, str_0)
        var_0 = session_0.update_headers(request_headers_dict_0)
        iterable_0 = None
        var_1 = session_0.remove_cookies(iterable_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ''
        set_0 = {str_0}
        path_0 = module_1.Path()
        str_1 = '\\_!{PNk'
        session_0 = module_2.get_httpie_session(path_0, str_1, str_0, str_1)
        var_0 = session_0.remove_cookies(set_0)
        str_2 = 'YNs '
        str_3 = 'Cookie'
        str_4 = 'localhost'
        str_5 = 'x'
        str_6 = {str_2: str_4, str_3: str_5}
        var_1 = session_0.update_headers(str_6)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '#+sy;ac'
        dict_0 = {str_0: str_0, str_0: str_0}
        path_0 = module_1.Path(**dict_0)
        iterable_0 = None
        path_1 = module_1.Path()
        str_1 = 'explicit_json'
        session_0 = module_2.get_httpie_session(path_1, str_1, str_1, str_0)
        dict_1 = {str_0: iterable_0}
        request_headers_dict_0 = module_0.RequestHeadersDict(**dict_1)
        var_0 = session_0.update_headers(request_headers_dict_0)
        var_1 = session_0.remove_cookies(iterable_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '_test'
        session_0 = module_2.Session(str_0)
        str_1 = 'Host'
        str_2 = 'Cookie'
        str_3 = {str_0: str_0, str_1: str_2, str_2: str_1, str_2: session_0}
        var_0 = session_0.update_headers(str_3)
    except BaseException:
        pass

def test_case_4():
    try:
        iterable_0 = None
        str_0 = 'qd'
        session_0 = module_2.Session(str_0)
        var_0 = session_0.remove_cookies(iterable_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'st'
        session_0 = module_2.Session(str_0)
        str_1 = 'Cookie'
        str_2 = {str_0: str_0, str_1: str_1}
        var_0 = session_0.update_headers(str_2)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = ''
        session_0 = module_2.Session(str_0)
        str_1 = 'a'
        str_2 = 'b'
        str_3 = {str_1: str_2}
        var_0 = session_0.update_headers(str_3)
        str_4 = 'B'
        str_5 = {str_4: str_1}
        var_1 = session_0.update_headers(str_5)
        str_6 = 'HTTPie/0.9.9'
        str_7 = {str_6: str_1}
        var_2 = session_0.update_headers(str_7)
        str_8 = 'coOkie'
        str_9 = '*=d'
        str_10 = {str_8: str_9}
        var_3 = session_0.update_headers(str_10)
    except BaseException:
        pass