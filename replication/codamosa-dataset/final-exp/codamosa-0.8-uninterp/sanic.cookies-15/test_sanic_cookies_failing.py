# Automatically generated by Pynguin.
import sanic.cookies as module_0

def test_case_0():
    try:
        bytes_0 = b'\xef\xbf\x8cj\xd6\x8aaI\x03\x94'
        cookie_jar_0 = module_0.CookieJar(bytes_0)
        var_0 = cookie_jar_0.__delitem__(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xef\xbf\x8cj\xd6\x8aaI\x03\x94'
        cookie_jar_0 = module_0.CookieJar(bytes_0)
        str_0 = 'main_sart'
        var_0 = cookie_jar_0.__delitem__(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xef\xbf{j\xd6\x8aaI\x03\xde'
        cookie_jar_0 = module_0.CookieJar(bytes_0)
        str_0 = '@O)YD]4'
        var_0 = cookie_jar_0.__delitem__(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        tuple_0 = None
        float_0 = -1367.344
        str_0 = '5B'
        bytes_0 = b'j\x03\x7fte\xd4\xab\x04\xee'
        cookie_0 = module_0.Cookie(str_0, bytes_0)
        var_0 = cookie_0.__setitem__(tuple_0, float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'foo'
        str_1 = 'bar'
        cookie_0 = module_0.Cookie(str_0, str_1)
        var_0 = cookie_0.__str__()
        var_1 = cookie_0.__str__()
        cookie_jar_0 = module_0.CookieJar(cookie_0)
        str_2 = 'expires'
        var_2 = cookie_jar_0.__delitem__(str_2)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'\xef\xbf\x8cj\xd6\x8aaI\x03\x94'
        cookie_jar_0 = module_0.CookieJar(bytes_0)
        float_0 = 2684.4713
        str_0 = 'Ik|_'
        dict_0 = {}
        cookie_0 = module_0.Cookie(str_0, dict_0)
        var_0 = cookie_0.encode(float_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '5mM1ba9v*U&`w#'
        bytes_0 = None
        cookie_0 = module_0.Cookie(str_0, bytes_0)
        var_0 = cookie_0.__str__()
        bool_0 = False
        var_1 = cookie_0.encode(bool_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'foo'
        str_1 = 'bar'
        cookie_0 = module_0.Cookie(str_0, str_1)
        str_2 = 'expires'
        var_0 = cookie_0.__setitem__(str_2, str_0)
    except BaseException:
        pass