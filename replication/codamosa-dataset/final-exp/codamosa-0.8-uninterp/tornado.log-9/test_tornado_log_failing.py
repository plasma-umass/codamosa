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
        log_formatter_0 = module_0.LogFormatter()
        module_0.define_logging_options()
    except BaseException:
        pass

def test_case_2():
    try:
        module_0.define_logging_options()
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = -678.7
        module_0.enable_pretty_logging(float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = -190.4
        module_0.define_logging_options(float_0)
    except BaseException:
        pass

def test_case_5():
    try:
        module_0.enable_pretty_logging()
        str_0 = 'yf+qEm\x0b:&V'
        bool_0 = False
        log_formatter_0 = module_0.LogFormatter(str_0, bool_0)
        stream_handler_0 = module_1.StreamHandler()
        float_0 = 0.3
        str_1 = 'w6/;|Fh*'
        str_2 = ' ZTR8e,dK'
        dict_0 = {str_0: float_0, str_1: float_0, str_2: float_0, str_1: bool_0}
        log_formatter_1 = module_0.LogFormatter()
        dict_1 = {log_formatter_1: str_0, log_formatter_1: float_0, bool_0: log_formatter_0}
        str_3 = 'j`G[h(MQ2I}"_\x0b,^ZP^'
        int_0 = -2655
        list_0 = [int_0, log_formatter_0]
        log_record_0 = module_1.LogRecord(float_0, log_formatter_0, str_0, stream_handler_0, dict_0, dict_1, str_3, list_0)
        str_4 = ''
        stream_handler_1 = module_1.StreamHandler(str_4)
        list_1 = [list_0]
        log_record_1 = module_1.LogRecord(log_formatter_0, stream_handler_0, log_record_0, stream_handler_0, log_formatter_0, dict_0, str_4, stream_handler_1, list_1)
        str_5 = log_formatter_0.format(log_record_1)
        dict_2 = {}
        log_formatter_2 = module_0.LogFormatter(str_0, str_4, bool_0, dict_2)
        str_6 = log_formatter_2.format(list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        log_formatter_0 = module_0.LogFormatter()
        str_0 = 'M_(B</vk8AXHhl3CSuQ'
        int_0 = 86
        log_record_0 = module_1.LogRecord(str_0, str_0, str_0, int_0, str_0, str_0, str_0)
        str_1 = log_formatter_0.format(log_record_0)
    except BaseException:
        pass

def test_case_7():
    try:
        module_0.enable_pretty_logging()
        str_0 = 'yf+qEm\x0b:&V'
        none_type_0 = None
        log_formatter_0 = module_0.LogFormatter()
        logger_0 = module_1.Logger(log_formatter_0)
        module_0.enable_pretty_logging(none_type_0, logger_0)
        bool_0 = False
        log_formatter_1 = module_0.LogFormatter(str_0, bool_0)
        stream_handler_0 = module_1.StreamHandler()
        float_0 = 0.3
        str_1 = 'w6/;|Fh*'
        str_2 = ' ZTR8e,dK'
        dict_0 = {str_0: float_0, str_1: float_0, str_2: float_0, str_1: bool_0}
        log_formatter_2 = module_0.LogFormatter()
        dict_1 = {log_formatter_2: str_0, log_formatter_2: float_0, bool_0: log_formatter_1}
        str_3 = 'j`G[h(MQ2I}"_\x0b,^ZP^'
        int_0 = -2655
        list_0 = [int_0, log_formatter_1]
        log_record_0 = module_1.LogRecord(float_0, log_formatter_1, str_0, stream_handler_0, dict_0, dict_1, str_3, list_0)
        str_4 = ''
        stream_handler_1 = module_1.StreamHandler(str_4)
        list_1 = [str_4, dict_0, str_3]
        list_2 = [list_1]
        log_record_1 = module_1.LogRecord(log_formatter_1, stream_handler_0, log_record_0, stream_handler_0, log_formatter_1, dict_0, str_4, stream_handler_1, list_2)
        str_5 = log_formatter_1.format(log_record_1)
        module_0.define_logging_options(dict_1)
    except BaseException:
        pass