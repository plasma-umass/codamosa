# Automatically generated by Pynguin.
import youtube_dl.downloader.hls as module_0

def test_case_0():
    try:
        str_0 = 'Downloading Provider Login Page'
        hls_f_d_0 = module_0.HlsFD(str_0, str_0)
        var_0 = hls_f_d_0.can_download(str_0, hls_f_d_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'm9B\xb8\t\xf8\x00'
        bool_0 = False
        str_0 = 'kmt010'
        str_1 = '!_@\x0c=(`g}'
        hls_f_d_0 = module_0.HlsFD(str_0, str_1)
        var_0 = hls_f_d_0.real_download(bytes_0, bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        str_0 = '?1q[.,6m\x0bKXPo!<'
        dict_0 = {bool_0: str_0}
        bool_1 = True
        bool_2 = True
        hls_f_d_0 = module_0.HlsFD(bool_1, bool_2)
        var_0 = hls_f_d_0.can_download(str_0, dict_0)
        str_1 = '!_'
        str_2 = 'S`C@p@a8Byz?yC'
        str_3 = '&.WFgMhG!T1jNsny<'
        set_0 = {str_3, str_1, bool_0, str_1}
        hls_f_d_1 = module_0.HlsFD(str_3, set_0)
        hls_f_d_2 = module_0.HlsFD(set_0, set_0)
        list_0 = [hls_f_d_2, hls_f_d_2, str_2]
        hls_f_d_3 = module_0.HlsFD(hls_f_d_2, list_0)
        var_1 = hls_f_d_3.can_download(str_1, str_2)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'test_HlsFD'
        str_1 = 'url'
        str_2 = 'http_headers'
        str_3 = 'http://example.com'
        var_0 = {}
        var_1 = {str_1: str_3, str_2: var_0}
        var_2 = {}
        str_4 = 'test'
        bool_0 = True
        bool_1 = {str_4: bool_0}
        hls_f_d_0 = module_0.HlsFD(var_2, bool_1)
        var_3 = hls_f_d_0.real_download(str_0, var_1)
    except BaseException:
        pass