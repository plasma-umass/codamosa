# Automatically generated by Pynguin.
import blib2to3.pgen2.grammar as module_0
import blib2to3.pgen2.parse as module_1

def test_case_0():
    try:
        grammar_0 = module_0.Grammar()
        grammar_1 = module_0.Grammar()
        int_0 = -507
        none_type_0 = None
        str_0 = 'iD[^('
        int_1 = None
        tuple_0 = (int_0, int_1)
        tuple_1 = (str_0, tuple_0)
        set_0 = {str_0, str_0, str_0}
        tuple_2 = (int_0, none_type_0, tuple_1, set_0)
        var_0 = module_1.lam_sub(grammar_1, tuple_2)
    except BaseException:
        pass

def test_case_1():
    try:
        grammar_0 = module_0.Grammar()
        tuple_0 = None
        var_0 = module_1.lam_sub(grammar_0, tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 467
        grammar_0 = module_0.Grammar()
        bool_0 = False
        parser_0 = module_1.Parser(grammar_0, bool_0)
        parser_0.setup(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0)
        parser_0.setup()
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = -1069
        str_0 = '[Ti}=G.2i$vQin;BS\n@k'
        tuple_0 = None
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0)
        bool_0 = parser_0.addtoken(int_0, str_0, tuple_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'D f.0dH)E'
        tuple_0 = None
        int_0 = None
        int_1 = 2848
        tuple_1 = (str_0, tuple_0)
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0)
        parser_0.shift(int_0, str_0, int_1, tuple_1)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = 442
        list_0 = []
        int_1 = 28
        int_2 = 554
        dict_0 = {int_0: int_1, int_0: int_2}
        tuple_0 = (list_0, dict_0)
        int_3 = 3970
        str_0 = 'v0H\t:aC-Y-_p\x0c'
        int_4 = -1595
        tuple_1 = (int_4, int_1)
        tuple_2 = (str_0, tuple_1)
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0)
        parser_0.push(int_0, tuple_0, int_3, tuple_2)
    except BaseException:
        pass

def test_case_7():
    try:
        grammar_0 = module_0.Grammar()
        grammar_1 = module_0.Grammar()
        int_0 = -1378
        parser_0 = module_1.Parser(grammar_1, int_0)
        parser_0.pop()
    except BaseException:
        pass

def test_case_8():
    try:
        grammar_0 = module_0.Grammar()
        var_0 = grammar_0.copy()
        int_0 = -1789
        str_0 = '&*+PV'
        str_1 = 'P4v'
        int_1 = 1112
        tuple_0 = (int_0, int_1)
        tuple_1 = (str_1, tuple_0)
        list_0 = None
        tuple_2 = (int_0, str_0, tuple_1, list_0)
        var_1 = module_1.lam_sub(grammar_0, tuple_2)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = "EeQe'\\c7;shD|E"
        tuple_0 = None
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0, grammar_0)
        int_0 = True
        bool_0 = parser_0.addtoken(int_0, str_0, tuple_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '[Ti}=G.2i$vki3;B;\n@k'
        tuple_0 = None
        grammar_0 = module_0.Grammar()
        parser_0 = module_1.Parser(grammar_0)
        int_0 = True
        bool_0 = parser_0.addtoken(int_0, str_0, tuple_0)
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = 1
        str_0 = 'def'
        str_1 = 'WZ.x<_,VnN{/'
        int_1 = 702
        tuple_0 = (int_0, int_1)
        tuple_1 = (str_1, tuple_0)
        grammar_0 = module_0.Grammar()
        parse_error_0 = module_1.ParseError(str_0, int_0, str_1, tuple_1)
        parser_0 = module_1.Parser(grammar_0, parse_error_0)
        str_2 = None
        parser_1 = module_1.Parser(grammar_0)
        bool_0 = parser_1.addtoken(int_0, str_2, tuple_1)
    except BaseException:
        pass