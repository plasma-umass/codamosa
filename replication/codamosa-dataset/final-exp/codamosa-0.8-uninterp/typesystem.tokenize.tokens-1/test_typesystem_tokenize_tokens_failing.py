# Automatically generated by Pynguin.
import typesystem.tokenize.tokens as module_0

def test_case_0():
    try:
        int_0 = -3529
        int_1 = -872
        token_0 = module_0.Token(int_0, int_1, int_1)
        list_0 = [int_1]
        int_2 = 1285
        int_3 = -1396
        token_1 = module_0.Token(list_0, int_2, int_3)
        token_2 = token_0.lookup(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = None
        list_0 = [str_0]
        list_1 = []
        int_0 = 60
        int_1 = 1134
        str_1 = 'GaKJyHi%'
        token_0 = module_0.Token(list_1, int_0, int_1, str_1)
        token_1 = token_0.lookup_key(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = -3529
        int_1 = -872
        token_0 = module_0.Token(int_0, int_1, int_1)
        bool_0 = token_0.__eq__(token_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = ' to JSON Schema'
        int_0 = 145
        list_0 = []
        int_1 = 2957
        token_0 = module_0.Token(list_0, int_1, int_0)
        token_1 = token_0.lookup(list_0)
        dict_0 = {str_0: str_0, str_0: str_0}
        str_1 = token_1.__repr__()
        token_2 = token_1.lookup(list_0)
        str_2 = token_1.__repr__()
        list_1 = [dict_0, token_2, int_1, token_0]
        dict_token_0 = module_0.DictToken(*list_1)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 1
        scalar_token_0 = module_0.ScalarToken(int_0, int_0, int_0)
        var_0 = scalar_token_0 == scalar_token_0
        int_1 = 2
        scalar_token_1 = module_0.ScalarToken(int_0, int_1, int_0)
        scalar_token_2 = module_0.ScalarToken(int_0, int_0, int_1)
        var_1 = scalar_token_2 == scalar_token_2
        scalar_token_3 = module_0.ScalarToken(int_1, int_0, int_0)
        var_2 = scalar_token_3 == scalar_token_2
        list_token_0 = module_0.ListToken(scalar_token_1, int_0, int_0)
        var_3 = list_token_0 == scalar_token_3
    except BaseException:
        pass