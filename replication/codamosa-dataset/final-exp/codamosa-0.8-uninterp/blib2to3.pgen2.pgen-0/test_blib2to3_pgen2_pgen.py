# Automatically generated by Pynguin.
import blib2to3.pgen2.pgen as module_0

def test_case_0():
    pass

def test_case_1():
    n_f_a_state_0 = module_0.NFAState()

def test_case_2():
    n_f_a_state_0 = module_0.NFAState()
    dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
    d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
    str_0 = 'o3;-'
    d_f_a_state_0.addarc(d_f_a_state_0, str_0)

def test_case_3():
    n_f_a_state_0 = module_0.NFAState()
    dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
    d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
    str_0 = '2U^_O?!B,+|-ZZr'
    d_f_a_state_0.addarc(d_f_a_state_0, str_0)
    d_f_a_state_0.unifystate(d_f_a_state_0, d_f_a_state_0)
    bool_0 = d_f_a_state_0.__eq__(d_f_a_state_0)

def test_case_4():
    n_f_a_state_0 = module_0.NFAState()
    dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
    d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
    str_0 = '2U^_O?!B,+|-ZZr'
    d_f_a_state_0.addarc(d_f_a_state_0, str_0)
    bool_0 = d_f_a_state_0.__eq__(d_f_a_state_0)

def test_case_5():
    n_f_a_state_0 = module_0.NFAState()
    dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
    d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
    str_0 = '2U^_O?!B,+|-ZZr'
    d_f_a_state_0.addarc(d_f_a_state_0, str_0)
    d_f_a_state_1 = None
    d_f_a_state_0.unifystate(d_f_a_state_1, d_f_a_state_0)
    bool_0 = d_f_a_state_0.__eq__(d_f_a_state_0)

def test_case_6():
    n_f_a_state_0 = module_0.NFAState()
    n_f_a_state_1 = module_0.NFAState()
    dict_0 = {n_f_a_state_0: n_f_a_state_0}
    d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
    n_f_a_state_0.addarc(n_f_a_state_0)
    n_f_a_state_2 = module_0.NFAState()
    str_0 = 'getrefcount'
    dict_1 = {n_f_a_state_1: str_0, n_f_a_state_1: str_0, n_f_a_state_1: n_f_a_state_1, n_f_a_state_1: n_f_a_state_1}
    d_f_a_state_1 = module_0.DFAState(dict_1, n_f_a_state_0)
    bool_0 = d_f_a_state_1.__eq__(d_f_a_state_0)

def test_case_7():
    n_f_a_state_0 = module_0.NFAState()
    n_f_a_state_0.addarc(n_f_a_state_0)
    dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
    d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
    str_0 = '2U^_O?!B,+|-ZZr'
    d_f_a_state_0.addarc(d_f_a_state_0, str_0)
    pgen_grammar_0 = module_0.PgenGrammar()
    str_1 = 'PatternGrammar.txT'
    dict_1 = {n_f_a_state_0: str_1, n_f_a_state_0: str_1, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
    d_f_a_state_1 = module_0.DFAState(dict_1, n_f_a_state_0)
    d_f_a_state_0.unifystate(d_f_a_state_1, d_f_a_state_0)
    bool_0 = d_f_a_state_1.__eq__(d_f_a_state_0)