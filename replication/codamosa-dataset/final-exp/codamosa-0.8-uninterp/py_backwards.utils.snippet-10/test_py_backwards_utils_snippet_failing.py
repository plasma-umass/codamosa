# Automatically generated by Pynguin.
import py_backwards.utils.snippet as module_0
import typed_ast._ast3 as module_1

def test_case_0():
    try:
        str_0 = 'x'
        arg_0 = None
        str_1 = None
        dict_0 = {str_0: str_0, str_1: str_1}
        variables_replacer_0 = module_0.VariablesReplacer(dict_0)
        arg_1 = variables_replacer_0.visit_arg(arg_0)
    except BaseException:
        pass

def test_case_1():
    try:
        attribute_0 = None
        str_0 = 'D<-:n'
        str_1 = 'FCv"vcB8Icww\\'
        dict_0 = {str_0: str_0, str_1: str_0}
        variables_replacer_0 = module_0.VariablesReplacer(dict_0)
        attribute_1 = variables_replacer_0.visit_Attribute(attribute_0)
    except BaseException:
        pass

def test_case_2():
    try:
        a_s_t_0 = module_1.AST()
        iterable_0 = module_0.find_variables(a_s_t_0)
        str_0 = 'zrL\rlR^+ /'
        dict_0 = {str_0: str_0, str_0: str_0}
        variables_replacer_0 = module_0.VariablesReplacer(dict_0)
        variables_replacer_1 = module_0.VariablesReplacer(dict_0)
        import_from_0 = module_1.ImportFrom()
        variables_replacer_2 = module_0.VariablesReplacer(dict_0)
        import_from_1 = variables_replacer_2.visit_ImportFrom(import_from_0)
    except BaseException:
        pass

def test_case_3():
    try:
        arg_0 = module_1.arg()
        str_0 = '9[\x0b,br\rl?$k'
        str_1 = '(2&j!W\\'
        dict_0 = {str_0: str_0, str_1: str_0, str_1: str_0}
        variables_replacer_0 = module_0.VariablesReplacer(dict_0)
        arg_1 = variables_replacer_0.visit_arg(arg_0)
        snippet_0 = module_0.snippet(arg_1)
        list_0 = snippet_0.get_body()
    except BaseException:
        pass

def test_case_4():
    try:
        except_handler_0 = module_1.ExceptHandler()
        str_0 = None
        dict_0 = {str_0: str_0}
        variables_replacer_0 = module_0.VariablesReplacer(dict_0)
        except_handler_1 = variables_replacer_0.visit_ExceptHandler(except_handler_0)
        snippet_0 = module_0.snippet(except_handler_1)
        name_0 = module_1.Name()
        name_1 = variables_replacer_0.visit_Name(name_0)
    except BaseException:
        pass