# Automatically generated by Pynguin.
import youtube_dl.downloader.fragment as module_0

def test_case_0():
    try:
        list_0 = None
        dict_0 = {list_0: list_0, list_0: list_0}
        tuple_0 = (dict_0,)
        list_1 = None
        bytes_0 = None
        http_quiet_downloader_0 = module_0.HttpQuietDownloader(list_1, bytes_0)
        list_2 = [list_0, tuple_0, dict_0, tuple_0]
        str_0 = 'http://cdn.playwire.com/11625/embed/85228.html'
        http_quiet_downloader_1 = module_0.HttpQuietDownloader(str_0, tuple_0)
        bool_0 = False
        dict_1 = {str_0: http_quiet_downloader_1}
        http_quiet_downloader_2 = module_0.HttpQuietDownloader(http_quiet_downloader_1, http_quiet_downloader_1)
        var_0 = http_quiet_downloader_2.to_screen(**dict_1)
        bytes_1 = b'\x83JI~&\xe5/\xf7\x07\xd2\xb8\x92\xf6\xcc\xc6'
        http_quiet_downloader_3 = module_0.HttpQuietDownloader(bool_0, bytes_1)
        fragment_f_d_0 = module_0.FragmentFD(http_quiet_downloader_3, bytes_1)
        var_1 = fragment_f_d_0.report_retry_fragment(list_0, list_2, tuple_0, http_quiet_downloader_1)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = {}
        list_0 = [dict_0, dict_0, dict_0, dict_0]
        bool_0 = True
        bytes_0 = b'\xfa\xdc\xb5\xc3\xe1\x8f\x82\x8a\xd40\xb4\x04'
        bytes_1 = b' \xd0\xad\xe8\xd0\x14'
        set_0 = {bytes_1}
        fragment_f_d_0 = module_0.FragmentFD(bytes_1, set_0)
        var_0 = fragment_f_d_0.report_retry_fragment(list_0, bool_0, bool_0, bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'm>IVVVYwb<Ib=7Tj%gR'
        set_0 = set()
        float_0 = -2839.684063
        fragment_f_d_0 = module_0.FragmentFD(set_0, float_0)
        var_0 = fragment_f_d_0.report_skip_fragment(str_0)
    except BaseException:
        pass