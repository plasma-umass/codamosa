# Automatically generated by Pynguin.
import ansible.module_utils.splitter as module_0

def test_case_0():
    try:
        str_0 = '3)V<$\rSVir}>'
        var_0 = module_0.split_args(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'h\x85\x97\x9ck\x160J\x1bs\xf8\xf6\x18m\x8c'
        var_0 = module_0.split_args(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = None
        var_0 = module_0.unquote(bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = {}
        var_0 = module_0.unquote(dict_0)
        str_0 = "?*^lVa#sk7'A9X]%E"
        var_1 = module_0.split_args(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = "'"
        var_0 = module_0.unquote(str_0)
        var_1 = module_0.split_args(str_0)
    except BaseException:
        pass