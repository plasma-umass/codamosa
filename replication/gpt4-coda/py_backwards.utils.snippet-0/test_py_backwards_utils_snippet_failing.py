# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.utils.snippet as module_1

def test_case_0():
    try:
        import_from_0 = module_0.ImportFrom()
        str_0 = '6:D[ROt?<f?hQKpH'
        dict_0 = {str_0: str_0}
        variables_replacer_0 = module_1.VariablesReplacer(dict_0)
        import_from_1 = variables_replacer_0.visit_ImportFrom(import_from_0)
    except BaseException:
        pass

def test_case_1():
    try:
        alias_0 = None
        str_0 = '6iss>o%2xq8WA.'
        str_1 = None
        dict_0 = {str_0: str_0, str_1: str_1}
        variables_replacer_0 = module_1.VariablesReplacer(dict_0)
        alias_1 = variables_replacer_0.visit_alias(alias_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xd8\xc6\x04\xe1|'
        snippet_0 = module_1.snippet(bytes_0)
        list_0 = snippet_0.get_body()
    except BaseException:
        pass

def test_case_3():
    try:
        except_handler_0 = module_0.ExceptHandler()
        str_0 = None
        str_1 = 'sources root'
        list_0 = [str_1]
        snippet_0 = module_1.snippet(list_0)
        function_def_0 = None
        str_2 = None
        dict_0 = {str_2: str_0}
        variables_replacer_0 = module_1.VariablesReplacer(dict_0)
        function_def_1 = variables_replacer_0.visit_FunctionDef(function_def_0)
    except BaseException:
        pass

def test_case_4():
    try:
        attribute_0 = module_0.Attribute()
        str_0 = 'K\x0b"u{zP{"l'
        list_0 = [str_0, attribute_0]
        alias_0 = module_0.alias(*list_0)
        str_1 = 'cfr'
        dict_0 = {str_1: str_0}
        variables_replacer_0 = module_1.VariablesReplacer(dict_0)
        alias_1 = variables_replacer_0.visit_alias(alias_0)
        dict_1 = None
        variables_replacer_1 = module_1.VariablesReplacer(dict_1)
        attribute_1 = variables_replacer_1.visit_Attribute(attribute_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'aj'
        list_0 = [str_0, str_0, str_0]
        import_from_0 = module_0.ImportFrom(*list_0)
        a_s_t_0 = None
        dict_0 = {}
        a_s_t_1 = module_0.AST(**dict_0)
        list_1 = [a_s_t_0, a_s_t_1, a_s_t_1]
        str_1 = 'Hrkm=O$3`(9'
        dict_1 = {str_0: list_1, str_1: a_s_t_1}
        variables_replacer_0 = module_1.VariablesReplacer(dict_1)
        import_from_1 = variables_replacer_0.visit_ImportFrom(import_from_0)
        dict_2 = {str_0: str_0}
        a_s_t_2 = module_0.AST(**dict_2)
        dict_3 = None
        module_1.extend_tree(a_s_t_2, dict_3)
        snippet_0 = module_1.snippet(dict_2)
        list_2 = snippet_0.get_body()
    except BaseException:
        pass