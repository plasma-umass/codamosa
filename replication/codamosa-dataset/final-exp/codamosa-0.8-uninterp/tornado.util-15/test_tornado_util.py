# Automatically generated by Pynguin.
import builtins as module_0
import tornado.util as module_1

def test_case_0():
    pass

def test_case_1():
    base_exception_0 = module_0.BaseException()
    optional_0 = module_1.errno_from_exception(base_exception_0)

def test_case_2():
    base_exception_0 = module_0.BaseException()
    list_0 = [base_exception_0, base_exception_0, base_exception_0]
    list_1 = [list_0]
    base_exception_1 = module_0.BaseException(*list_1)
    optional_0 = module_1.errno_from_exception(base_exception_1)
    timeout_error_0 = module_1.TimeoutError()

def test_case_3():
    str_0 = 'os'
    any_0 = module_1.import_object(str_0)
    any_1 = module_1.import_object(str_0)
    str_1 = 'tornado.escape'
    any_2 = module_1.import_object(str_1)