# Automatically generated by Pynguin.
import tornado.util as module_0
import builtins as module_1

def test_case_0():
    try:
        object_dict_0 = module_0.ObjectDict()
        var_0 = module_0.timedelta_to_seconds(object_dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -33
        object_dict_0 = module_0.ObjectDict()
        str_0 = '@'
        object_dict_0.__setattr__(str_0, str_0)
        object_dict_0.__setattr__(str_0, object_dict_0)
        dict_0 = {int_0: int_0}
        var_0 = module_0.raise_exc_info(dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'r\xf4L\xbb\x99\xefg\xc3l\xfb.\xf8\xd8'
        int_0 = -541
        gzip_decompressor_0 = module_0.GzipDecompressor()
        bytes_1 = gzip_decompressor_0.decompress(bytes_0, int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'tornado.escape'
        str_1 = 'tornado.escape.utf8'
        any_0 = module_0.import_object(str_1)
        gzip_decompressor_0 = module_0.GzipDecompressor()
        bytes_0 = gzip_decompressor_0.flush()
        dict_0 = {str_1: str_1, any_0: str_0, str_0: str_0, str_0: str_1}
        str_2 = 'vhxJ\tvW\\lep5L2F'
        tuple_0 = (dict_0, str_2)
        var_0 = module_0.raise_exc_info(tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '3D[V,G'
        any_0 = module_0.import_object(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        base_exception_0 = module_1.BaseException()
        optional_0 = module_0.errno_from_exception(base_exception_0)
        str_0 = '0'
        str_1 = None
        str_2 = 'F8n?qd}KJ#8&3qfX'
        gzip_decompressor_0 = module_0.GzipDecompressor()
        bytes_0 = gzip_decompressor_0.flush()
        dict_0 = {str_0: base_exception_0, str_1: str_1, str_2: optional_0}
        set_0 = {base_exception_0, str_1}
        module_0.exec_in(base_exception_0, dict_0, set_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = ";V$~9Wjjv_4-\x0c'Y^\tL]\n"
        gzip_decompressor_0 = module_0.GzipDecompressor()
        bytes_0 = gzip_decompressor_0.flush()
        str_1 = 'g`?SuHt}9P2g'
        bytes_1 = gzip_decompressor_0.flush()
        list_0 = None
        set_0 = {list_0}
        dict_0 = {str_0: str_0, str_1: set_0, str_1: set_0}
        module_0.exec_in(str_0, dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        list_0 = []
        list_1 = [list_0, list_0]
        list_2 = [list_1, list_0, list_1, list_0]
        var_0 = module_0.raise_exc_info(list_2)
    except BaseException:
        pass

def test_case_8():
    try:
        base_exception_0 = None
        optional_0 = module_0.errno_from_exception(base_exception_0)
    except BaseException:
        pass

def test_case_9():
    try:
        configurable_0 = module_0.Configurable()
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = ''
        arg_replacer_0 = module_0.ArgReplacer(str_0, str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '[b#t/0\\1'
        str_1 = module_0.re_unescape(str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'tornado.missing_module'
        any_0 = module_0.import_object(str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        float_0 = -585.1
        list_0 = [float_0, float_0, float_0, float_0]
        list_1 = [list_0, list_0, float_0, list_0]
        list_2 = [list_1, list_0, list_1]
        list_3 = None
        list_4 = [list_2, list_3]
        var_0 = module_0.raise_exc_info(list_4)
    except BaseException:
        pass