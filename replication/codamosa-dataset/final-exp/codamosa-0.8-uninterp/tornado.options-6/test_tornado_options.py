# Automatically generated by Pynguin.
import tornado.options as module_0

def test_case_0():
    pass

def test_case_1():
    iterator_0 = None
    option_parser_0 = module_0.OptionParser()
    option_parser_0.run_parse_callbacks()
    str_0 = '@'
    bool_0 = True
    iterator_1 = option_parser_0.__iter__()
    option_0 = module_0._Option(str_0, bool_0, str_0, str_0)
    option_0.set(iterator_0)

def test_case_2():
    option_parser_0 = module_0.OptionParser()
    dict_0 = option_parser_0.as_dict()
    option_parser_1 = module_0.OptionParser()
    iterable_0 = option_parser_1.items()

def test_case_3():
    str_0 = 'L'
    option_parser_0 = module_0.OptionParser()
    dict_0 = option_parser_0.group_dict(str_0)

def test_case_4():
    option_parser_0 = module_0.OptionParser()
    dict_0 = option_parser_0.as_dict()

def test_case_5():
    option_parser_0 = module_0.OptionParser()
    mockable_0 = option_parser_0.mockable()

def test_case_6():
    option_parser_0 = module_0.OptionParser()
    mockable_0 = module_0._Mockable(option_parser_0)

def test_case_7():
    iterator_0 = None
    str_0 = '@'
    bool_0 = True
    option_0 = module_0._Option(str_0, bool_0, str_0, str_0)
    option_0.set(iterator_0)

def test_case_8():
    str_0 = '.#lVn'
    none_type_0 = None
    option_parser_0 = module_0.OptionParser()
    option_parser_0.define(str_0, none_type_0)
    str_1 = "!f\x0b_zb\tW=2'Z"
    option_parser_0.__setattr__(str_0, str_0)
    option_parser_0.run_parse_callbacks()
    option_parser_1 = module_0.OptionParser()
    option_parser_2 = module_0.OptionParser()
    bool_0 = option_parser_1.__contains__(str_1)