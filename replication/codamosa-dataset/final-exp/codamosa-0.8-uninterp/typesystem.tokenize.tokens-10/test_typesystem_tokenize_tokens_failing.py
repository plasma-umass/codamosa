# Automatically generated by Pynguin.
import typesystem.tokenize.tokens as module_0

def test_case_0():
    try:
        str_0 = "C'&8z&`\r.nAn"
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        int_0 = -1617
        token_0 = module_0.Token(dict_0, int_0, int_0)
        int_1 = -12
        scalar_token_0 = module_0.ScalarToken(int_1, int_1, int_1)
        bool_0 = scalar_token_0.__eq__(scalar_token_0)
        list_0 = [str_0, str_0]
        token_1 = token_0.lookup_key(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'bf9{'
        int_0 = 4
        int_1 = {}
        int_2 = -255
        list_0 = [int_1, int_0, str_0]
        dict_token_0 = module_0.DictToken(*list_0)
        int_3 = 1592
        list_1 = [int_3]
        int_4 = -12
        str_1 = '2~RvvY]ILgBFAQ!4'
        token_0 = module_0.Token(int_2, int_3, int_4, str_1)
        token_1 = token_0.lookup_key(list_1)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'value'
        int_0 = 1
        int_1 = 1
        str_1 = 'content'
        token_0 = module_0.Token(str_0, int_0, int_1, str_1)
        var_0 = token_0.end
        var_1 = []
        token_1 = token_0.lookup(var_1)
        var_2 = []
        token_2 = token_0.lookup_key(var_2)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_token_0 = module_0.DictToken()
    except BaseException:
        pass

def test_case_4():
    try:
        var_0 = int()
        var_1 = int()
        token_0 = module_0.Token(var_0, var_0, var_1)
        var_2 = int()
        bool_0 = token_0.__eq__(var_2)
        var_3 = int()
        var_4 = int()
        bool_1 = token_0.__eq__(token_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'b'
        int_0 = 4
        int_1 = {str_0: int_0, str_0: int_0}
        list_0 = [int_1, int_0, str_0]
        dict_token_0 = module_0.DictToken(*list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = 1
        scalar_token_0 = module_0.ScalarToken(int_0, int_0, int_0)
        str_0 = 'z:'
        dict_0 = {str_0: int_0, str_0: str_0, str_0: scalar_token_0, str_0: scalar_token_0}
        list_token_0 = module_0.ListToken(dict_0, int_0, int_0)
        bool_0 = scalar_token_0.__eq__(list_token_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'm!^ 6iWV'
        int_0 = -1086
        scalar_token_0 = module_0.ScalarToken(str_0, int_0, int_0)
        int_1 = -1422
        int_2 = None
        scalar_token_1 = module_0.ScalarToken(scalar_token_0, int_1, int_2)
        str_1 = 'b'
        int_3 = {scalar_token_0: int_0}
        int_4 = -255
        list_0 = [int_3, int_3, str_1]
        dict_token_0 = module_0.DictToken(*list_0)
        int_5 = -1769
        list_token_0 = module_0.ListToken(int_4, int_5, int_3)
        scalar_token_2 = module_0.ScalarToken(int_3, int_3, int_5)
        bool_0 = scalar_token_2.__eq__(dict_token_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'a'
        int_0 = 1
        int_1 = {str_0: int_0}
        int_2 = 0
        list_0 = [int_1, int_1, int_2, int_2]
        int_3 = 14
        int_4 = 2651
        str_1 = '9fHZ,,'
        list_token_0 = module_0.ListToken(int_0, int_3, int_4, str_1)
        token_0 = list_token_0.lookup_key(list_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'value'
        int_0 = -30
        int_1 = 1
        str_1 = 'input_type'
        token_0 = module_0.Token(str_0, int_0, int_1, str_1)
        var_0 = token_0.start
        var_1 = int_1.end
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '123'
        int_0 = 0
        int_1 = 2
        str_1 = 'abc'
        list_token_0 = module_0.ListToken(str_0, int_0, int_1, str_1)
        var_0 = list_token_0.value
    except BaseException:
        pass