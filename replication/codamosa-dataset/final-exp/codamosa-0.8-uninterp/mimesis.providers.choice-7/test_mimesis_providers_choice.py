# Automatically generated by Pynguin.
import mimesis.providers.choice as module_0

def test_case_0():
    str_0 = 'centrefolds'
    int_0 = 9877
    choice_0 = module_0.Choice()
    var_0 = choice_0.__call__(str_0, int_0)

def test_case_1():
    str_0 = 'Ts-$#F#m'
    bool_0 = False
    dict_0 = {}
    choice_0 = module_0.Choice(**dict_0)
    var_0 = choice_0.__call__(str_0, bool_0)

def test_case_2():
    choice_0 = module_0.Choice()
    list_0 = [choice_0]
    int_0 = 408
    var_0 = choice_0.__call__(list_0, int_0)

def test_case_3():
    choice_0 = module_0.Choice()
    str_0 = 'a'
    str_1 = 'b'
    str_2 = 'c'
    str_3 = [str_0, str_1, str_2]
    var_0 = choice_0.__call__(str_3)
    var_1 = choice_0.__call__(str_3)
    var_2 = choice_0.__call__(str_3)
    int_0 = 1
    var_3 = choice_0.__call__(str_3, int_0)
    str_4 = 'abc'
    int_1 = 2
    var_4 = choice_0.__call__(str_4, int_1)
    str_5 = (str_0, str_1, str_2)
    int_2 = 5
    var_5 = choice_0.__call__(str_5, int_2)
    str_6 = 'aabbbccccddddd'
    int_3 = 4
    bool_0 = True
    var_6 = choice_0.__call__(str_6, int_3, bool_0)