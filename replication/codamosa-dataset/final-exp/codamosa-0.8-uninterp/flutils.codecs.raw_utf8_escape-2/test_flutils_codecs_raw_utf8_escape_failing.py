# Automatically generated by Pynguin.
import flutils.codecs.raw_utf8_escape as module_0
import collections as module_1
import codecs as module_2

def test_case_0():
    try:
        module_0.register()
        bytes_0 = b'\x84\x92Q\x99%}\x00f\x9a\xbe\\\x0f\xb1\x06\xf8\x8a'
        int_0 = None
        tuple_0 = (bytes_0, int_0)
        user_string_0 = module_1.UserString(tuple_0)
        var_0 = user_string_0.__len__()
        tuple_1 = module_0.encode(user_string_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '-S?)jQohW,W !@\x0ctIo'
        tuple_0 = module_0.encode(str_0)
        str_1 = '3w\tJD\nm+'
        tuple_1 = module_0.decode(str_1, str_1)
    except BaseException:
        pass

def test_case_2():
    try:
        module_0.register()
        str_0 = '>MB/7VL}2v1;'
        tuple_0 = module_0.encode(str_0)
        list_0 = [str_0, str_0]
        tuple_1 = module_0.encode(str_0, str_0)
        tuple_2 = module_0.encode(str_0)
        tuple_3 = module_0.encode(str_0)
        user_string_0 = module_1.UserString(list_0)
        str_1 = 'W]#A7&4d-'
        dict_0 = {str_0: user_string_0, str_0: str_1, user_string_0: user_string_0}
        user_string_1 = module_1.UserString(dict_0)
        user_string_2 = module_1.UserString(user_string_1)
        list_1 = [user_string_2, user_string_2]
        bytes_0 = b"\xd1f\\'i8"
        int_0 = 2572
        tuple_4 = (bytes_0, int_0)
        tuple_5 = (str_0, user_string_0, list_1, tuple_4)
        user_string_3 = module_1.UserString(tuple_5)
        tuple_6 = module_0.encode(user_string_3)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = -1
        str_0 = '.'
        var_0 = __name__.split(str_0)[int_0]
        var_1 = module_2.getdecoder(var_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'mCj'
        module_0.register()
        tuple_0 = module_0.encode(str_0, str_0)
        tuple_1 = module_0.encode(str_0, str_0)
        tuple_2 = module_0.encode(str_0)
        tuple_3 = None
        tuple_4 = module_0.encode(str_0)
        tuple_5 = module_0.decode(tuple_3)
    except BaseException:
        pass

def test_case_5():
    try:
        module_0.register()
        str_0 = '#?)Onr\x0b#Y-?WZppS~u\x0b('
        tuple_0 = module_0.encode(str_0)
        bytes_0 = b'\xda\xfby\x92&d\xbc\xacA0\xf5Wh\x91\xf6\xe5S'
        user_string_0 = module_1.UserString(bytes_0)
        user_string_1 = module_1.UserString(user_string_0)
        tuple_1 = module_0.encode(user_string_1, user_string_0)
    except BaseException:
        pass

def test_case_6():
    try:
        module_0.register()
        module_0.register()
        bytes_0 = b'\xc2\xbf6\xdb\x84\xe3\xde\xf1\x93l\x89\x97\x9d\xb4\xd9\xf4\x18'
        tuple_0 = module_0.decode(bytes_0)
    except BaseException:
        pass

def test_case_7():
    try:
        module_0.register()
        module_0.register()
        module_0.register()
        str_0 = '#?)Onr\x0b#Y-?WZppS~u\x0b('
        bytes_0 = b'm\xf8Ji\x9fY#'
        tuple_0 = module_0.decode(bytes_0, str_0)
    except BaseException:
        pass