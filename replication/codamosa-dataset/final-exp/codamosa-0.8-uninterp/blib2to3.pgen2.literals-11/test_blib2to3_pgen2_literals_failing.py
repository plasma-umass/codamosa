# Automatically generated by Pynguin.
import blib2to3.pgen2.literals as module_0
import re as module_1

def test_case_0():
    try:
        str_0 = '\n        Initializer.\n\n        Takes a type constant (a token number < 256), a string value, and an\n        optional context keyword argument.\n        '
        str_1 = module_0.evalString(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '\'wqs;Wm\'e^A"'
        str_1 = module_0.evalString(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        module_0.test()
        str_0 = "'''"
        str_1 = module_0.evalString(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = "'\\x0O\\n\\T'"
        str_1 = module_0.evalString(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '\\\\(x.{i,2}|[[.7]{,3})'
        var_0 = module_1.match(str_0, str_0)
        str_1 = module_0.escape(var_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '\\\\(.{0,2}|[0-7]{1,3})'
        str_1 = '\\12'
        var_0 = module_1.match(str_0, str_1)
        str_2 = module_0.escape(var_0)
        module_0.test()
        str_3 = '\\35'
        var_1 = module_1.match(str_0, str_3)
        str_4 = '\\x1)3'
        var_2 = module_1.match(str_0, str_4)
        str_5 = module_0.escape(var_2)
    except BaseException:
        pass