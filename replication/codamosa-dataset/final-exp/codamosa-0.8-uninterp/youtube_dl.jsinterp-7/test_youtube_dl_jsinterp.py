# Automatically generated by Pynguin.
import youtube_dl.jsinterp as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = "a='hello'; b=a+1; return a.split(K' .reverse()vjoin('');"
    j_s_interpreter_0 = module_0.JSInterpreter(str_0)

def test_case_2():
    str_0 = '20190803'
    list_0 = []
    j_s_interpreter_0 = module_0.JSInterpreter(str_0, list_0)

def test_case_3():
    str_0 = '\n        var c = function(a,b){\n            return a-b;\n        }\n        var d = c(e,f);\n        '
    var_0 = {}
    j_s_interpreter_0 = module_0.JSInterpreter(str_0, var_0)
    str_1 = 'e'
    str_2 = 'f'
    int_0 = 6
    int_1 = 2
    int_2 = {str_1: int_0, str_2: int_1}
    str_3 = 'c(e,f)'
    int_3 = 5
    var_1 = j_s_interpreter_0.interpret_expression(str_3, int_2, int_3)

def test_case_4():
    int_0 = 1
    j_s_interpreter_0 = module_0.JSInterpreter(int_0, int_0)
    str_0 = '(1)'
    str_1 = '(1 + 2) * 3'
    var_0 = j_s_interpreter_0.interpret_expression(str_1, int_0, int_0)
    var_1 = j_s_interpreter_0.interpret_expression(str_0, int_0, int_0)
    var_2 = j_s_interpreter_0.interpret_expression(str_1, int_0, int_0)