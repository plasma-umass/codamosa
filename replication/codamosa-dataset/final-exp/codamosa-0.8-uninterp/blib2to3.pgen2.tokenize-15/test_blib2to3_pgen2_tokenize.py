# Automatically generated by Pynguin.
import blib2to3.pgen2.tokenize as module_0

def test_case_0():
    pass

def test_case_1():
    untokenizer_0 = module_0.Untokenizer()

def test_case_2():
    int_0 = -2861
    tuple_0 = (int_0, int_0)
    untokenizer_0 = module_0.Untokenizer()
    untokenizer_0.add_whitespace(tuple_0)

def test_case_3():
    var_0 = module_0.group()
    untokenizer_0 = module_0.Untokenizer()
    token_error_0 = module_0.TokenError()
    str_0 = 'A!d'
    untokenizer_1 = module_0.Untokenizer()
    dict_0 = {var_0: str_0}
    str_1 = untokenizer_0.untokenize(dict_0)

def test_case_4():
    str_0 = '\t'
    var_0 = iter(str_0)
    var_1 = var_0.__next__
    iterator_0 = module_0.generate_tokens(var_1)
    untokenizer_0 = module_0.Untokenizer()
    str_1 = untokenizer_0.untokenize(iterator_0)
    var_2 = list(iterator_0)
    var_3 = print(var_2)

def test_case_5():
    int_0 = True
    str_0 = ']V[D+fA?>O)hxz'
    tuple_0 = (int_0, str_0)
    callable_0 = None
    int_1 = -127
    int_2 = 4755
    tuple_1 = (int_1, int_2)
    untokenizer_0 = module_0.Untokenizer()
    untokenizer_0.add_whitespace(tuple_1)
    untokenizer_0.add_whitespace(tuple_1)
    list_0 = [tuple_0, str_0, int_1]
    iterator_0 = module_0.generate_tokens(callable_0, list_0)
    untokenizer_1 = module_0.Untokenizer()
    list_1 = [tuple_0]
    untokenizer_1.compat(tuple_0, list_1)

def test_case_6():
    str_0 = 'BGyT+L\x0b'
    var_0 = iter(str_0)
    var_1 = var_0.__next__
    iterator_0 = module_0.generate_tokens(var_1)
    var_2 = list(iterator_0)

def test_case_7():
    str_0 = '\t'
    var_0 = iter(str_0)
    var_1 = var_0.__next__
    iterator_0 = module_0.generate_tokens(var_1)
    var_2 = list(iterator_0)
    var_3 = print(iterator_0)

def test_case_8():
    str_0 = ' '
    var_0 = iter(str_0)
    var_1 = var_0.__next__
    iterator_0 = module_0.generate_tokens(var_1)
    var_2 = list(iterator_0)
    var_3 = print(var_2)

def test_case_9():
    str_0 = '#'
    var_0 = iter(str_0)
    var_1 = var_0.__next__
    iterator_0 = module_0.generate_tokens(var_1)
    var_2 = list(iterator_0)
    var_3 = print(var_2)

def test_case_10():
    str_0 = '\\\r\n'
    var_0 = iter(str_0)
    var_1 = var_0.__next__
    iterator_0 = module_0.generate_tokens(var_1)
    var_2 = list(iterator_0)

def test_case_11():
    str_0 = 'BGy9T+L\x0b'
    var_0 = iter(str_0)
    var_1 = var_0.__next__
    iterator_0 = module_0.generate_tokens(var_1)
    var_2 = list(iterator_0)

def test_case_12():
    str_0 = 'BGyT+L\x0b'
    str_1 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = iter(str_1)
    var_1 = var_0.__next__
    iterator_0 = module_0.generate_tokens(var_1)
    var_2 = list(iterator_0)

def test_case_13():
    str_0 = 'mA9$1aU\r@:W75m.\n>'
    var_0 = iter(str_0)
    var_1 = module_0.maybe()
    var_2 = var_0.__next__
    iterator_0 = module_0.generate_tokens(var_2)
    var_3 = list(iterator_0)
    var_4 = print(var_3)

def test_case_14():
    str_0 = '<L=G]*`|#42|'
    str_1 = 'E\r'
    str_2 = '9L\r{A1TZh\\ss\nL8'
    str_3 = [str_1, str_0, str_1, str_2, str_1]
    var_0 = iter(str_3)
    var_1 = var_0.__next__
    untokenizer_0 = module_0.Untokenizer()
    iterator_0 = module_0.generate_tokens(var_1)
    var_2 = list(iterator_0)
    untokenizer_1 = module_0.Untokenizer()
    var_3 = print(var_2)

def test_case_15():
    untokenizer_0 = module_0.Untokenizer()
    int_0 = 0
    str_0 = 'foo'
    var_0 = (int_0, str_0)
    int_1 = 1
    str_1 = '+'
    var_1 = (int_1, str_1)
    str_2 = 'bar'
    var_2 = (int_0, str_2)
    int_2 = 4
    str_3 = '\n'
    var_3 = (int_2, str_3)
    str_4 = 'baz'
    var_4 = (int_0, str_4)
    str_5 = '='
    var_5 = (int_1, str_5)
    var_6 = [var_0, var_1, var_2, var_3, var_4, var_5]
    var_7 = (int_0, str_0)
    var_8 = iter(var_6)
    untokenizer_0.compat(var_7, var_8)