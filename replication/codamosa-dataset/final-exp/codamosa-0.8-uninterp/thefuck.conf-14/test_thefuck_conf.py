# Automatically generated by Pynguin.
import thefuck.conf as module_0

def test_case_0():
    pass

def test_case_1():
    settings_0 = module_0.Settings()
    var_0 = settings_0.init()

def test_case_2():
    settings_0 = module_0.Settings()
    var_0 = settings_0.init(settings_0)

def test_case_3():
    settings_0 = module_0.Settings()
    str_0 = 'args'
    var_0 = ()
    str_1 = 'debug'
    str_2 = 'yes'
    str_3 = 'repeat'
    bool_0 = True
    int_0 = 3
    var_1 = {str_1: bool_0, str_2: bool_0, str_3: int_0}
    var_2 = type(str_0, var_0, var_1)
    var_3 = settings_0.init(var_2)