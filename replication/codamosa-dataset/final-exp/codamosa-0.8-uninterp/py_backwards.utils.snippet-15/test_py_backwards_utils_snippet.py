# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.utils.snippet as module_1
import typed_ast.ast3 as module_2

def test_case_0():
    pass

def test_case_1():
    a_s_t_0 = module_0.AST()
    iterable_0 = module_1.find_variables(a_s_t_0)

def test_case_2():
    str_0 = ''
    dict_0 = {str_0: str_0}
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)

def test_case_3():
    keyword_0 = module_0.keyword()
    str_0 = None
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    keyword_1 = variables_replacer_0.visit_keyword(keyword_0)

def test_case_4():
    dict_0 = {}
    function_def_0 = module_0.FunctionDef(**dict_0)
    str_0 = None
    str_1 = '#LdO{rY:FRU]?P=;PV'
    dict_1 = {str_0: str_0, str_0: str_0, str_0: str_0, str_1: str_1}
    variables_replacer_0 = module_1.VariablesReplacer(dict_1)
    function_def_1 = variables_replacer_0.visit_FunctionDef(function_def_0)
    str_2 = '\na = 5\nextend(vars)\nb = 3\n        '
    var_0 = module_2.parse(str_2)
    str_3 = 'vars'
    var_1 = {str_3: str_2}
    module_1.extend_tree(var_0, var_1)

def test_case_5():
    keyword_0 = module_0.keyword()
    str_0 = '<Eh1bv\x0brI R'
    str_1 = '\\~h'
    str_2 = None
    dict_0 = {str_0: str_0, str_1: str_0, str_2: str_1, str_2: str_2}
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    keyword_1 = variables_replacer_0.visit_keyword(keyword_0)
    dict_1 = {str_0: str_0}
    except_handler_0 = module_0.ExceptHandler(**dict_1)
    variables_replacer_1 = module_1.VariablesReplacer(dict_0)
    except_handler_1 = variables_replacer_1.visit_ExceptHandler(except_handler_0)
    keyword_2 = variables_replacer_0.visit_keyword(keyword_1)

def test_case_6():
    str_0 = ':$>gG?s<|W(N95}:1\t\n'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    a_s_t_0 = module_0.AST()
    module_1.extend_tree(a_s_t_0, dict_0)

def test_case_7():
    a_s_t_0 = module_0.AST()
    iterable_0 = module_1.find_variables(a_s_t_0)
    module_1.let(iterable_0)

def test_case_8():
    float_0 = 215.8458
    module_1.extend(float_0)
    str_0 = None
    str_1 = '#+])T\x0bM-N5%xK2Z`\n'
    class_def_0 = module_0.ClassDef()
    list_0 = [str_1, class_def_0, str_0]
    import_from_0 = module_0.ImportFrom(*list_0)
    dict_0 = {str_0: str_0}
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    import_from_1 = variables_replacer_0.visit_ImportFrom(import_from_0)
    str_2 = None
    dict_1 = {str_2: str_1, str_0: str_0}
    variables_replacer_1 = module_1.VariablesReplacer(dict_1)
    import_from_2 = variables_replacer_1.visit_ImportFrom(import_from_1)
    str_3 = None
    dict_2 = {str_1: str_3}
    variables_replacer_2 = module_1.VariablesReplacer(dict_2)
    import_from_3 = variables_replacer_2.visit_ImportFrom(import_from_2)
    str_4 = None
    dict_3 = {str_4: str_4}
    variables_replacer_3 = module_1.VariablesReplacer(dict_3)
    class_def_1 = variables_replacer_3.visit_ClassDef(class_def_0)
    bool_0 = True
    snippet_0 = module_1.snippet(bool_0)
    str_5 = '85UF'
    str_6 = ''
    dict_4 = {str_6: str_6, str_6: str_1}
    variables_replacer_4 = module_1.VariablesReplacer(dict_4)
    str_7 = '\nkaP\\R'
    dict_5 = {str_5: str_5, str_6: str_5, str_7: str_5, str_7: str_5}
    variables_replacer_5 = module_1.VariablesReplacer(dict_5)

def test_case_9():
    str_0 = 'let(x)\nxB= 5\ny =llet(y)\ny += x\n'
    var_0 = module_2.parse(str_0)
    iterable_0 = module_1.find_variables(var_0)