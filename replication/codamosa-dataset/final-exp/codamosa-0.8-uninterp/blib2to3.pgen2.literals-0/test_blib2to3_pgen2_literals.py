# Automatically generated by Pynguin.
import blib2to3.pgen2.literals as module_0

def test_case_0():
    pass

def test_case_1():
    module_0.test()

def test_case_2():
    str_0 = '"\\"\'\\\\`\\a\\b\\f\\n\\r\\t\\v\\0\\01\\011\\0111\\x01\\x011\\x1111\\u1234\\u01234\\u001234\\U00001234"'
    str_1 = module_0.evalString(str_0)

def test_case_3():
    str_0 = "'''abc\\ndef'''"
    str_1 = module_0.evalString(str_0)
    str_2 = "'abc\\ndef'"
    str_3 = module_0.evalString(str_2)
    str_4 = "'abc\\x20def'"
    str_5 = module_0.evalString(str_4)
    str_6 = "'abc\\u0020def'"
    str_7 = module_0.evalString(str_6)
    str_8 = '"abc\\ndef"'
    str_9 = module_0.evalString(str_8)
    str_10 = '"abc\\x20def"'
    str_11 = module_0.evalString(str_10)