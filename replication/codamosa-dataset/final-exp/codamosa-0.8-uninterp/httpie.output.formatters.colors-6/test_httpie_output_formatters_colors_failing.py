# Automatically generated by Pynguin.
import httpie.context as module_0
import httpie.output.formatters.colors as module_1
import pygments.formatters.terminal as module_2
import pygments.lexers as module_3

def test_case_0():
    try:
        environment_0 = module_0.Environment()
        color_formatter_0 = module_1.ColorFormatter(environment_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'N~=brax/\x0b'
        terminal_formatter_0 = module_2.TerminalFormatter()
        optional_0 = module_1.get_lexer(str_0, str_0, terminal_formatter_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'text/plain'
        bool_0 = True
        optional_0 = module_1.get_lexer(str_0)
        str_1 = 'b;T~"PM'
        dict_0 = {str_1: bool_0}
        var_0 = module_3.get_lexer_by_name(dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'foo/bar'
        bool_0 = False
        optional_0 = module_1.get_lexer(str_0, bool_0)
        str_1 = 'foo/bar+json'
        optional_1 = module_1.get_lexer(str_1)
        environment_0 = module_0.Environment()
        color_formatter_0 = module_1.ColorFormatter(environment_0)
    except BaseException:
        pass