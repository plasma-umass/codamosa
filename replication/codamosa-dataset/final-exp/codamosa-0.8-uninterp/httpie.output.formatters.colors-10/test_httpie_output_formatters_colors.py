# Automatically generated by Pynguin.
import httpie.output.formatters.colors as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'F/H2r=Knq;vHs]CM3G'
    optional_0 = module_0.get_lexer(str_0)

def test_case_2():
    str_0 = 'applcation/jso'
    str_1 = '{"a":1}'
    optional_0 = module_0.get_lexer(str_0, str_1)
    var_0 = print(optional_0)
    bool_0 = True
    optional_1 = module_0.get_lexer(str_0, bool_0, str_1)
    var_1 = print(optional_1)

def test_case_3():
    str_0 = 'a5\tplicati\\n/json'
    optional_0 = module_0.get_lexer(str_0, str_0)

def test_case_4():
    str_0 = 'a5\tplicati\\n/json'
    bool_0 = True
    optional_0 = module_0.get_lexer(str_0, bool_0, str_0)

def test_case_5():
    str_0 = 'F/H2+pr=Knq;Hs]CM3G'
    optional_0 = module_0.get_lexer(str_0)

def test_case_6():
    str_0 = 'application/json'
    str_1 = '{"a":1}'
    optional_0 = module_0.get_lexer(str_0, str_1)
    var_0 = print(optional_0)
    bool_0 = True
    optional_1 = module_0.get_lexer(str_0, bool_0, str_1)
    var_1 = print(optional_1)