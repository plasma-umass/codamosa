# Automatically generated by Pynguin.
import httpie.output.formatters.headers as module_0

def test_case_0():
    try:
        headers_formatter_0 = module_0.HeadersFormatter()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'format_options'
        str_1 = 'headers'
        var_0 = {str_1: str_0}
        var_1 = {str_0: var_0}
        headers_formatter_0 = module_0.HeadersFormatter(**var_1)
    except BaseException:
        pass