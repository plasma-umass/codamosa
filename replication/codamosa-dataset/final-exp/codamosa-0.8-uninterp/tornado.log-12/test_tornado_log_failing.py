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
        str_0 = '2\x0bnlG^'
        module_0.enable_pretty_logging()
        dict_0 = {}
        log_formatter_0 = module_0.LogFormatter(dict_0)
        dict_1 = {}
        str_1 = None
        dict_2 = {str_0: log_formatter_0, str_0: dict_1, str_1: dict_1}
        tuple_0 = (log_formatter_0, dict_2)
        logger_0 = module_1.Logger(tuple_0)
        module_0.enable_pretty_logging(logger_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 674.79
        module_0.define_logging_options(float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        list_0 = None
        dict_0 = {list_0: list_0, list_0: list_0, list_0: list_0}
        bool_0 = True
        str_0 = 'fw\\CFh!c3XNQ]X+'
        bytes_0 = b'\xb9\xb9\xac\xeeW\xa7\xe0J\xf1g\xb5\x87%\x83\xc6\x85z\x8fD'
        float_0 = 2542.0
        tuple_0 = (str_0, list_0, bytes_0, float_0)
        str_1 = 'b4SD:Ck+/oO$'
        dict_1 = {str_1: tuple_0, str_0: str_0, str_0: str_0}
        log_record_0 = module_1.LogRecord(dict_0, bool_0, str_1, dict_0, str_0, tuple_0, dict_1)
        log_formatter_0 = module_0.LogFormatter(str_1)
        str_2 = log_formatter_0.format(log_record_0)
    except BaseException:
        pass

def test_case_5():
    try:
        module_0.enable_pretty_logging()
        log_formatter_0 = module_0.LogFormatter()
        any_0 = None
        tuple_0 = ()
        logger_0 = module_1.Logger(tuple_0)
        module_0.enable_pretty_logging(any_0, logger_0)
        str_0 = 'V_L'
        bool_0 = False
        list_0 = [bool_0]
        log_formatter_1 = module_0.LogFormatter(str_0)
        list_1 = [log_formatter_0, list_0]
        var_0 = logger_0.exception(list_1)
        int_0 = 2
        int_1 = -225
        int_2 = 868
        int_3 = -1215
        int_4 = -2375
        int_5 = 1218
        dict_0 = {int_0: int_1, int_0: int_2, int_3: int_4, int_5: int_0}
        log_formatter_2 = module_0.LogFormatter(dict_0)
        module_0.define_logging_options(any_0)
    except BaseException:
        pass