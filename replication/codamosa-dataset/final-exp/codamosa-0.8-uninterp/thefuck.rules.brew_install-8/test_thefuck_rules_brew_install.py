# Automatically generated by Pynguin.
import thefuck.rules.brew_install as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = ''
    var_0 = ()
    str_1 = 'script'
    str_2 = 'output'
    str_3 = 'brew install foobar'
    str_4 = 'Error: No avaiable formula for foobar'
    str_5 = {str_1: str_3, str_2: str_4}
    var_1 = type(str_0, var_0, str_5)
    var_2 = module_0.match(var_1)