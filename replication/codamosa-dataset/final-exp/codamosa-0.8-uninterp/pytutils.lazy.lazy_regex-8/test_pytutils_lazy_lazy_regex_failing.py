# Automatically generated by Pynguin.
import pytutils.lazy.lazy_regex as module_0

def test_case_0():
    try:
        str_0 = "Return a member from the proxied regex object.\n\n        If the regex hasn't been compiled yet, compile it\n        "
        invalid_pattern_0 = module_0.InvalidPattern(str_0)
        var_0 = invalid_pattern_0.__str__()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ''
        invalid_pattern_0 = module_0.InvalidPattern(str_0)
        var_0 = invalid_pattern_0.__unicode__()
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 84.3
        invalid_pattern_0 = module_0.InvalidPattern(float_0)
        var_0 = invalid_pattern_0.__repr__()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '-sW0\x0cO'
        invalid_pattern_0 = module_0.InvalidPattern(str_0)
        float_0 = 1333.0
        var_0 = invalid_pattern_0.__eq__(float_0)
        var_1 = invalid_pattern_0.__str__()
    except BaseException:
        pass

def test_case_4():
    try:
        lazy_regex_0 = module_0.LazyRegex()
        str_0 = '?\x0b3fQ"L1*Q/?<M'
        var_0 = lazy_regex_0.__getattr__(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        lazy_regex_0 = module_0.LazyRegex()
        invalid_pattern_0 = module_0.InvalidPattern(lazy_regex_0)
        var_0 = lazy_regex_0.__getstate__()
        var_1 = invalid_pattern_0.__str__()
    except BaseException:
        pass

def test_case_6():
    try:
        lazy_regex_0 = module_0.LazyRegex()
        bool_0 = True
        lazy_regex_1 = module_0.LazyRegex(bool_0)
        var_0 = lazy_regex_1.__setstate__(lazy_regex_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = "WoR\n'\twc/"
        int_0 = -204
        var_0 = module_0.install_lazy_compile()
        var_1 = module_0.finditer_public(str_0, int_0)
    except BaseException:
        pass

def test_case_8():
    try:
        lazy_regex_0 = module_0.LazyRegex()
        set_0 = None
        var_0 = module_0.finditer_public(lazy_regex_0, set_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = "\n    Update and/or insert query parameters in a URL.\n\n    >>> update_query_params('http://example.com?foo=bar&biz=baz', dict(foo='stuff'))\n    'http://example.com?...foo=stuff...'\n\n    :param url: URL\n    :type url: str\n    :param kwargs: Query parameters\n    :type kwargs: dict\n    :return: Modified URL\n    :rtype: str\n    "
        str_1 = '<+[-J-n/uD"k4JWY}l'
        set_0 = {str_0, str_0}
        dict_0 = {}
        lazy_regex_0 = module_0.LazyRegex(set_0, dict_0)
        var_0 = lazy_regex_0.__getattr__(str_1)
    except BaseException:
        pass

def test_case_10():
    try:
        int_0 = 16
        tuple_0 = (int_0,)
        lazy_regex_0 = module_0.LazyRegex()
        var_0 = lazy_regex_0.__getstate__()
        invalid_pattern_0 = module_0.InvalidPattern(tuple_0)
        invalid_pattern_1 = module_0.InvalidPattern(tuple_0)
        var_1 = invalid_pattern_1.__eq__(invalid_pattern_0)
        var_2 = invalid_pattern_0.__unicode__()
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '[\nB_'
        set_0 = {str_0, str_0}
        lazy_regex_0 = module_0.LazyRegex(set_0)
        var_0 = lazy_regex_0.__getattr__(set_0)
    except BaseException:
        pass