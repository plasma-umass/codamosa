# Automatically generated by Pynguin.
import blib2to3.pgen2.literals as module_0
import re as module_1

def test_case_0():
    try:
        str_0 = 'blib2to3.pgen2.literals'
        str_1 = module_0.evalString(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        module_0.test()
        module_0.test()
        module_0.test()
        module_0.test()
        module_0.test()
        str_0 = '"YTo9NuYI!.x'
        str_1 = module_0.evalString(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '\\\\(.|$)'
        str_1 = '\\x41'
        var_0 = module_1.match(str_0, str_1)
        str_2 = module_0.escape(var_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = "'\\007\\x07\\x0G7'"
        str_1 = module_0.evalString(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '"\\""'
        str_1 = module_0.evalString(str_0)
        str_2 = "'''"
        module_0.test()
        str_3 = module_0.evalString(str_2)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '\\\\(m|)'
        var_0 = module_1.match(str_0, str_0)
        str_1 = module_0.escape(var_0)
    except BaseException:
        pass

def test_case_6():
    try:
        module_0.test()
        str_0 = 'R\\\\(m|)'
        var_0 = module_1.match(str_0, str_0)
        str_1 = module_0.escape(var_0)
    except BaseException:
        pass