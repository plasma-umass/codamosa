# Automatically generated by Pynguin.
import mimesis.providers.choice as module_0

def test_case_0():
    choice_0 = module_0.Choice()
    str_0 = 'abc'
    int_0 = 2
    var_0 = choice_0.__call__(str_0, int_0)

def test_case_1():
    str_0 = None
    list_0 = [str_0, str_0, str_0]
    choice_0 = module_0.Choice()
    var_0 = choice_0.__call__(list_0)
    list_1 = [str_0, str_0, str_0]
    int_0 = 1899
    choice_1 = module_0.Choice()
    var_1 = choice_1.__call__(list_1, int_0)

def test_case_2():
    choice_0 = module_0.Choice()
    str_0 = 'abc'
    int_0 = 1
    list_0 = [choice_0, str_0]
    bool_0 = True
    var_0 = choice_0.__call__(list_0, int_0, bool_0)