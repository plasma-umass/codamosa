# Automatically generated by Pynguin.
import youtube_dl.downloader.f4m as module_0
import youtube_dl.compat as module_1

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'\x00\x00\x00\x18asrt\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02'
    list_0 = [bytes_0]
    flv_reader_0 = module_0.FlvReader(*list_0)
    var_0 = flv_reader_0.read_string()

def test_case_2():
    str_0 = '<manifest xmlns="http://ns.adobe.com/f4m/2.0"></manifest>'
    var_0 = module_1.compat_etree_fromstring(str_0)
    str_1 = '<manifest xmlns="http://ns.adobe.com/f4m/1.0">    <baseURL>http://example.com/</baseURL></manifest>'
    var_1 = module_1.compat_etree_fromstring(str_1)
    var_2 = module_0.get_base_url(var_1)

def test_case_3():
    str_0 = '<manifest xmlns="http://ns.adobe.com/f4m/1.0"></manifest>'
    var_0 = module_1.compat_etree_fromstring(str_0)
    var_1 = module_0.get_base_url(var_0)
    str_1 = '<manifest xmlns="http://ns.adobe.com/f4m/2.0"></manifest>'
    var_2 = module_1.compat_etree_fromstring(str_1)
    var_3 = module_0.get_base_url(var_2)
    str_2 = '<manifest xmlns="http://ns.adobe.com/f4m/1.0">    <baseURL>http://example.com/</baseURL></manifest>'
    var_4 = module_1.compat_etree_fromstring(str_2)
    var_5 = module_0.get_base_url(var_4)

def test_case_4():
    bytes_0 = b'\x1d\xa72B0\x9b\xb3\x96C\x00\xebt\xf5\xea'
    list_0 = [bytes_0]
    flv_reader_0 = module_0.FlvReader(*list_0)
    var_0 = flv_reader_0.read_string()