# Automatically generated by Pynguin.
import youtube_dl.downloader.fragment as module_0

def test_case_0():
    try:
        dict_0 = None
        str_0 = 'atK\'F"<'
        float_0 = -356.994535
        int_0 = -842
        http_quiet_downloader_0 = module_0.HttpQuietDownloader(float_0, int_0)
        dict_1 = {}
        str_1 = 'mvId'
        str_2 = '!('
        http_quiet_downloader_1 = module_0.HttpQuietDownloader(str_1, str_2)
        fragment_f_d_0 = module_0.FragmentFD(dict_0, http_quiet_downloader_1)
        var_0 = fragment_f_d_0.report_retry_fragment(str_0, dict_0, http_quiet_downloader_0, dict_1)
    except BaseException:
        pass

def test_case_1():
    try:
        set_0 = None
        http_quiet_downloader_0 = None
        http_quiet_downloader_1 = module_0.HttpQuietDownloader(set_0, http_quiet_downloader_0)
        fragment_f_d_0 = None
        dict_0 = {fragment_f_d_0: fragment_f_d_0, fragment_f_d_0: fragment_f_d_0, fragment_f_d_0: fragment_f_d_0, fragment_f_d_0: fragment_f_d_0}
        str_0 = 'mOE@_Ul(\t?w4+'
        fragment_f_d_1 = module_0.FragmentFD(dict_0, str_0)
        var_0 = fragment_f_d_1.report_skip_fragment(http_quiet_downloader_1)
    except BaseException:
        pass