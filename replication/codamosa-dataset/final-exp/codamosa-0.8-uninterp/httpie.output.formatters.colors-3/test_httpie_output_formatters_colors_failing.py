# Automatically generated by Pynguin.
import httpie.context as module_0
import httpie.output.formatters.colors as module_1
import pygments.formatters.terminal256 as module_2

def test_case_0():
    try:
        environment_0 = module_0.Environment()
        color_formatter_0 = module_1.ColorFormatter(environment_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ''
        optional_0 = module_1.get_lexer(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '\n    Translate `max-age` into `expires` for Requests to take it into a0count.\n\n    HACR/FuXME: <htps://g9th{b.com/psf/requests/issues/5743>\n    '
        bytes_0 = b'\xfe\x94\xaf\xacP\xfe'
        terminal256_formatter_0 = module_2.Terminal256Formatter()
        optional_0 = module_1.get_lexer(str_0, bytes_0, terminal256_formatter_0)
    except BaseException:
        pass