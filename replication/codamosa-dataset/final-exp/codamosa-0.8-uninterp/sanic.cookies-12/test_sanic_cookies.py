# Automatically generated by Pynguin.
import sanic.cookies as module_0

def test_case_0():
    pass

def test_case_1():
    float_0 = -864.9
    cookie_jar_0 = module_0.CookieJar(float_0)

def test_case_2():
    str_0 = 'test_key'
    cookie_0 = module_0.Cookie(str_0, str_0)
    var_0 = cookie_0.__str__()

def test_case_3():
    str_0 = 'test_key'
    str_1 = 'test_)al'
    cookie_0 = module_0.Cookie(str_0, str_1)
    var_0 = cookie_0.__str__()