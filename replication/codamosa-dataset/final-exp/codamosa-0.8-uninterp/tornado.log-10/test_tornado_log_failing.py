# Automatically generated by Pynguin.
import tornado.log as module_0
import logging as module_1

def test_case_0():
    try:
        log_formatter_0 = module_0.LogFormatter()
        str_0 = log_formatter_0.format(log_formatter_0)
    except BaseException:
        pass

def test_case_1():
    try:
        module_0.define_logging_options()
    except BaseException:
        pass

def test_case_2():
    try:
        log_formatter_0 = module_0.LogFormatter()
        module_0.define_logging_options()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '4'
        str_1 = 'login_url'
        bool_0 = True
        log_formatter_0 = module_0.LogFormatter(str_0, str_1, bool_0)
        dict_0 = {str_0: log_formatter_0, str_0: bool_0}
        logger_0 = module_1.Logger(dict_0)
        module_0.enable_pretty_logging(logger_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'j`KyeT(1):V!E\\K}'
        bool_0 = None
        log_formatter_0 = module_0.LogFormatter(str_0)
        log_formatter_1 = module_0.LogFormatter(bool_0)
        log_formatter_2 = module_0.LogFormatter()
        module_0.define_logging_options(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '.'
        dict_0 = {}
        log_formatter_0 = module_0.LogFormatter(str_0, dict_0)
        module_0.enable_pretty_logging()
        str_1 = None
        bool_0 = False
        dict_1 = None
        log_formatter_1 = module_0.LogFormatter(str_1, str_1, bool_0, dict_1)
        module_0.enable_pretty_logging()
        str_2 = '\\:\nr3\x0b'
        log_formatter_2 = module_0.LogFormatter(str_2)
        str_3 = log_formatter_2.format(log_formatter_2)
    except BaseException:
        pass

def test_case_6():
    try:
        optional_0 = None
        str_0 = None
        logger_0 = module_1.Logger(str_0)
        module_0.enable_pretty_logging(optional_0, logger_0)
        log_formatter_0 = None
        var_0 = logger_0.exception(log_formatter_0)
        module_0.define_logging_options()
    except BaseException:
        pass

def test_case_7():
    try:
        optional_0 = None
        str_0 = None
        logger_0 = module_1.Logger(str_0)
        module_0.enable_pretty_logging(optional_0, logger_0)
        var_0 = logger_0.addHandler(logger_0)
        log_formatter_0 = None
        var_1 = logger_0.exception(log_formatter_0)
    except BaseException:
        pass