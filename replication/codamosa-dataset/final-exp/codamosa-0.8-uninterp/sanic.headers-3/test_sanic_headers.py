# Automatically generated by Pynguin.
import sanic.headers as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'secret=no,proto=https,for=192.0.2.0:44host=example.com'
    tuple_0 = module_0.parse_content_header(str_0)

def test_case_2():
    str_0 = 'secret=no,proto=https,for=192.0.2.60:443;host=example.com'
    tuple_0 = module_0.parse_content_header(str_0)

def test_case_3():
    list_0 = []
    dict_0 = module_0.fwd_normalize(list_0)
    str_0 = '<HeG\x0cY'
    str_1 = module_0.fwd_normalize_address(str_0)

def test_case_4():
    str_0 = "f%J'HvO5p:$!YVRD"
    str_1 = module_0.fwd_normalize_address(str_0)

def test_case_5():
    str_0 = '<HeG\x0cY'
    tuple_0 = module_0.parse_host(str_0)

def test_case_6():
    str_0 = 'w'
    tuple_0 = module_0.parse_host(str_0)
    str_1 = module_0.fwd_normalize_address(str_0)
    str_2 = '3BQXV'
    str_3 = module_0.fwd_normalize_address(str_2)
    tuple_1 = module_0.parse_content_header(str_2)
    str_4 = '@sh!z/Y5'
    tuple_2 = module_0.parse_content_header(str_4)
    str_5 = 'N/zD\\\x0b)xUkaR'
    tuple_3 = module_0.parse_host(str_5)
    tuple_4 = ()
    dict_0 = module_0.fwd_normalize(tuple_4)
    int_0 = 14
    bytes_0 = module_0.format_http1_response(int_0, tuple_4)

def test_case_7():
    str_0 = '_scheme'
    str_1 = module_0.fwd_normalize_address(str_0)

def test_case_8():
    str_0 = '[0:0:0:0:0:0:0:0]'
    str_1 = module_0.fwd_normalize_address(str_0)
    str_2 = '0:0:0:0:0:0:0:0'
    str_3 = module_0.fwd_normalize_address(str_2)
    str_4 = 'localhoswt'
    str_5 = module_0.fwd_normalize_address(str_4)
    str_6 = '::1'
    str_7 = module_0.fwd_normalize_address(str_6)
    str_8 = module_0.fwd_normalize_address(str_6)
    str_9 = '127.0.0.1'
    str_10 = module_0.fwd_normalize_address(str_9)
    str_11 = '127.0.0.1:8000'
    str_12 = module_0.fwd_normalize_address(str_11)

def test_case_9():
    str_0 = 'for'
    str_1 = 'foobar'
    str_2 = (str_0, str_1)
    str_3 = [str_2]
    dict_0 = module_0.fwd_normalize(str_3)
    str_4 = 'proto'
    str_5 = 'HTTP'
    str_6 = (str_4, str_5)
    str_7 = [str_6]
    dict_1 = module_0.fwd_normalize(str_7)
    str_8 = (str_4, str_5)
    str_9 = 'HTTPS'
    str_10 = (str_4, str_9)
    str_11 = [str_8, str_10]
    dict_2 = module_0.fwd_normalize(str_11)
    str_12 = 'port'
    str_13 = '80'
    str_14 = (str_12, str_13)
    str_15 = [str_14]
    dict_3 = module_0.fwd_normalize(str_15)
    str_16 = 'path'
    str_17 = '/foo'
    str_18 = (str_16, str_17)
    str_19 = [str_18]
    dict_4 = module_0.fwd_normalize(str_19)
    str_20 = '/foo%2Fbar'
    str_21 = (str_16, str_20)
    str_22 = [str_21]
    dict_5 = module_0.fwd_normalize(str_22)
    str_23 = 'foo'
    str_24 = 'bar'
    str_25 = (str_23, str_24)
    str_26 = [str_25]
    dict_6 = module_0.fwd_normalize(str_26)

def test_case_10():
    str_0 = 'foo/bar; name="upload"; filenam="file.txt"'
    tuple_0 = module_0.parse_content_header(str_0)