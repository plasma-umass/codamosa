# Automatically generated by Pynguin.
import pymonet.lazy as module_0

def test_case_0():
    try:
        str_0 = 'G'
        lazy_0 = module_0.Lazy(str_0)
        var_0 = lazy_0.to_validation()
    except BaseException:
        pass

def test_case_1():
    try:
        set_0 = None
        list_0 = [set_0]
        float_0 = 3009.37992
        lazy_0 = module_0.Lazy(set_0)
        var_0 = lazy_0.ap(float_0)
        list_1 = []
        lazy_1 = module_0.Lazy(list_1)
        var_1 = lazy_0.to_either(*list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'=u7'
        lazy_0 = module_0.Lazy(bytes_0)
        var_0 = lazy_0.to_box()
    except BaseException:
        pass

def test_case_3():
    try:
        var_0 = lambda v: v
        lazy_0 = module_0.Lazy(var_0)
        var_1 = lazy_0.to_either()
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = False
        lazy_0 = module_0.Lazy(int_0)
        var_0 = lazy_0.to_maybe()
    except BaseException:
        pass

def test_case_5():
    try:
        var_0 = lambda v: v
        lazy_0 = module_0.Lazy(var_0)
        lazy_1 = module_0.Lazy(var_0)
        bool_0 = lazy_0.__eq__(lazy_1)
        int_0 = -2675
        list_0 = [lazy_0]
        var_1 = lazy_1.to_either(*list_0)
        tuple_0 = (int_0,)
        list_1 = [var_0, tuple_0, lazy_1, lazy_1]
        lazy_2 = module_0.Lazy(list_1)
        str_0 = lazy_2.__str__()
        var_2 = lazy_1.to_either(*list_1)
        bytes_0 = None
        lazy_3 = module_0.Lazy(bytes_0)
        var_3 = lazy_0.to_either(*list_1)
    except BaseException:
        pass

def test_case_6():
    try:
        var_0 = lambda v: v
        lazy_0 = module_0.Lazy(var_0)
        list_0 = [lazy_0]
        var_1 = lazy_0.to_maybe(*list_0)
        lazy_1 = module_0.Lazy(var_0)
        bool_0 = lazy_0.__eq__(lazy_1)
        var_2 = lazy_1.to_maybe()
    except BaseException:
        pass