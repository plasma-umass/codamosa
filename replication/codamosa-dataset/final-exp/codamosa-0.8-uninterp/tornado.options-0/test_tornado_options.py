# Automatically generated by Pynguin.
import tornado.options as module_0
import typing as module_1

def test_case_0():
    pass

def test_case_1():
    option_parser_0 = module_0.OptionParser()
    var_0 = [type(opt) for opt in option_parser_0]
    var_1 = set(var_0)

def test_case_2():
    module_0.print_help()
    str_0 = 'Schedules the given callback to be called periodically.\n\n    The callback is called every ``callback_time`` milliseconds.\n    Note that the timeout is given in milliseconds, while most other\n    time-related functions in Tornado use seconds.\n\n    If ``jitter`` is specified, each callback time will be randomly selected\n    within a window of ``jitter * callback_time`` milliseconds.\n    Jitter can be used to reduce alignment of events with similar periods.\n    A jitter of 0.1 means allowing a 10% variation in callback time.\n    The window is centered on ``callback_time`` so the total number of calls\n    within a given interval should not be significantly affected by adding\n    jitter.\n\n    If the callback runs for longer than ``callback_time`` milliseconds,\n    subsequent invocations will be skipped to get back on schedule.\n\n    `start` must be called after the `PeriodicCallback` is created.\n\n    .. versionchanged:: 5.0\n       The ``io_loop`` argument (deprecated since version 4.1) has been removed.\n\n    .. versionchanged:: 5.1\n       The ``jitter`` argument is added.\n    '
    option_parser_0 = module_0.OptionParser()
    mockable_0 = option_parser_0.mockable()
    bool_0 = option_parser_0.__contains__(str_0)

def test_case_3():
    option_parser_0 = module_0.OptionParser()
    set_0 = option_parser_0.groups()

def test_case_4():
    callable_0 = None
    module_0.add_parse_callback(callable_0)
    str_0 = '/ou'
    option_parser_0 = module_0.OptionParser()
    dict_0 = option_parser_0.group_dict(str_0)

def test_case_5():
    option_parser_0 = module_0.OptionParser()
    dict_0 = option_parser_0.as_dict()

def test_case_6():
    option_parser_0 = module_0.OptionParser()
    module_0.print_help()
    str_0 = 'fof$^\tIW&bE\x0b}7ht+'
    option_parser_1 = module_0.OptionParser()
    option_parser_1.run_parse_callbacks()
    bool_0 = option_parser_1.__contains__(str_0)
    bool_1 = option_parser_1.__contains__(str_0)
    dict_0 = option_parser_1.group_dict(str_0)

def test_case_7():
    option_parser_0 = module_0.OptionParser()
    iterable_0 = option_parser_0.items()
    option_parser_1 = module_0.OptionParser()

def test_case_8():
    str_0 = '/input/tornado/log.py'
    option_parser_0 = module_0.OptionParser()
    option_parser_0.parse_config_file(str_0)
    option_parser_1 = module_0.OptionParser()
    option_parser_2 = module_0.OptionParser()
    str_1 = 'JaxaBse'
    dict_0 = option_parser_0.group_dict(str_1)
    option_parser_3 = module_0.OptionParser()
    option_parser_4 = module_0.OptionParser()
    mockable_0 = option_parser_2.mockable()
    option_parser_5 = module_0.OptionParser()

def test_case_9():
    option_parser_0 = module_0.OptionParser()
    option_parser_0.print_help()
    set_0 = option_parser_0.groups()
    option_parser_1 = module_0.OptionParser()
    text_i_o_0 = module_1.TextIO()
    text_i_o_1 = text_i_o_0.__enter__()
    option_parser_2 = module_0.OptionParser()
    option_parser_2.print_help(text_i_o_1)
    list_0 = [text_i_o_0, option_parser_1, text_i_o_0]
    error_0 = module_0.Error(*list_0)
    str_0 = 'YyIh%^)'
    optional_0 = None
    option_parser_0.define(str_0, optional_0)
    option_parser_3 = module_0.OptionParser()
    set_1 = option_parser_1.groups()
    option_parser_4 = module_0.OptionParser()
    str_1 = 'd[X2'
    bool_0 = option_parser_2.__contains__(str_1)
    option_parser_5 = module_0.OptionParser()
    mockable_0 = option_parser_0.mockable()
    list_1 = []
    list_2 = module_0.parse_command_line(list_1, bool_0)

def test_case_10():
    option_parser_0 = module_0.OptionParser()
    str_0 = 'test2'
    int_0 = 3
    option_parser_0.define(str_0, int_0)
    str_1 = 'test1'
    int_1 = 1
    option_parser_0.define(str_1, int_1)
    str_2 = 'test3'
    str_3 = ''
    option_parser_0.define(str_2, str_3)
    option_parser_0.print_help()
    str_4 = 'test4'
    str_5 = 'test'
    option_parser_0.define(str_4, str_5)
    str_6 = 'test5'
    int_2 = 0
    option_parser_0.define(str_6, int_2)
    str_7 = 'test6'
    bool_0 = True
    option_parser_0.define(str_7, bool_0)
    str_8 = 'test7'
    bool_1 = False
    option_parser_0.define(str_8, bool_1)
    str_9 = 'test8'
    str_10 = 'False'
    option_parser_0.define(str_9, str_10)