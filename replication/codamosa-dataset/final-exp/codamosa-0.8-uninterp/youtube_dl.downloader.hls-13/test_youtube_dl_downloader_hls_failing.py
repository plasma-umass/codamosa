# Automatically generated by Pynguin.
import youtube_dl.downloader.hls as module_0

def test_case_0():
    try:
        str_0 = 'j'
        bool_0 = False
        hls_f_d_0 = module_0.HlsFD(bool_0, str_0)
        var_0 = hls_f_d_0.can_download(str_0, hls_f_d_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'q\t>MXhKr)f#400\x0bYv19'
        float_0 = 478.8083
        int_0 = -794
        set_0 = {str_0, str_0, float_0, float_0}
        float_1 = 1009.6284
        bool_0 = False
        dict_0 = {}
        bool_1 = False
        tuple_0 = (bool_0, dict_0, bool_1)
        hls_f_d_0 = module_0.HlsFD(float_1, tuple_0)
        hls_f_d_1 = module_0.HlsFD(int_0, set_0)
        set_1 = {str_0, str_0, float_0, str_0}
        dict_1 = None
        str_1 = '?XE4vnp}AV\x0cw'
        str_2 = 'cz]z4qF)\nD'
        dict_2 = {float_0: str_1}
        int_1 = 3132
        hls_f_d_2 = module_0.HlsFD(float_0, dict_1)
        hls_f_d_3 = module_0.HlsFD(int_1, hls_f_d_2)
        var_0 = hls_f_d_3.can_download(str_2, dict_2)
        var_1 = hls_f_d_2.real_download(str_0, set_1)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 1974.7483
        int_0 = 3375
        float_1 = 3307.6
        int_1 = 1482541200
        str_0 = 'data-application="([^"]+)"'
        tuple_0 = (int_1, str_0)
        hls_f_d_0 = module_0.HlsFD(float_1, tuple_0)
        var_0 = hls_f_d_0.real_download(float_0, int_0)
    except BaseException:
        pass