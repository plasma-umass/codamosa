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
    dict_0 = {}
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)

def test_case_3():
    except_handler_0 = module_0.ExceptHandler()
    str_0 = '(2/P8z),'
    str_1 = None
    dict_0 = {str_0: str_0, str_0: str_0, str_1: str_0}
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    except_handler_1 = variables_replacer_0.visit_ExceptHandler(except_handler_0)
    str_2 = 'urlunparse'
    dict_1 = {str_2: str_2}
    variables_replacer_1 = module_1.VariablesReplacer(dict_1)
    except_handler_2 = variables_replacer_1.visit_ExceptHandler(except_handler_1)
    snippet_0 = module_1.snippet(except_handler_2)

def test_case_4():
    arg_0 = module_0.arg()
    dict_0 = {}
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    arg_1 = variables_replacer_0.visit_arg(arg_0)

def test_case_5():
    str_0 = '\nif True:\n    let(a)\n    a += 1\n    let(y)\n    y = 1\n'
    var_0 = module_2.parse(str_0)
    a_s_t_0 = module_0.AST()
    dict_0 = {str_0: a_s_t_0}
    list_0 = [dict_0, str_0]
    except_handler_0 = module_0.ExceptHandler(*list_0)
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    except_handler_1 = variables_replacer_0.visit_ExceptHandler(except_handler_0)
    module_1.extend_tree(a_s_t_0, dict_0)
    iterable_0 = module_1.find_variables(var_0)

def test_case_6():
    list_0 = []
    name_0 = module_0.Name(*list_0)
    dict_0 = {}
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    name_1 = variables_replacer_0.visit_Name(name_0)
    str_0 = '\nif True:\n    let(a)\n    a += 1\n    let(y)\n    y = 1\n'
    var_0 = module_2.parse(str_0)
    a_s_t_0 = module_0.AST()
    dict_1 = {str_0: a_s_t_0}
    module_1.extend_tree(a_s_t_0, dict_1)
    iterable_0 = module_1.find_variables(var_0)

def test_case_7():
    str_0 = '\nif True:\n    zet(a)\n    a += 1\n    let(y)\n    y = 1\n'
    var_0 = module_2.parse(str_0)
    a_s_t_0 = module_0.AST()
    dict_0 = {str_0: a_s_t_0}
    module_1.extend_tree(a_s_t_0, dict_0)
    module_1.extend(str_0)
    iterable_0 = module_1.find_variables(var_0)
    function_def_0 = module_0.FunctionDef()
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    function_def_1 = variables_replacer_0.visit_FunctionDef(function_def_0)

def test_case_8():
    a_s_t_0 = module_0.AST()
    str_0 = '\x0c,xLoePu!L;aQ3+'
    dict_0 = {str_0: str_0}
    keyword_0 = module_0.keyword()
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    keyword_1 = variables_replacer_0.visit_keyword(keyword_0)
    variables_replacer_1 = module_1.VariablesReplacer(dict_0)
    keyword_2 = variables_replacer_1.visit_keyword(keyword_1)
    module_1.extend_tree(a_s_t_0, dict_0)

def test_case_9():
    str_0 = 'F\r0?4)mx3B?_Z\\_</FN'
    str_1 = '(6c]8'
    callable_0 = None
    snippet_0 = module_1.snippet(callable_0)
    dict_0 = {str_0: str_0, str_1: snippet_0, str_0: snippet_0, str_1: str_0}
    class_def_0 = module_0.ClassDef(**dict_0)
    str_2 = 'BqBu_u>R=`'
    str_3 = "]F3@\nwQG@'1^O/ez$mX"
    str_4 = 'uses_params'
    str_5 = 'W\rg%od1oQL'
    dict_1 = {str_2: str_2, str_3: str_2, str_4: str_2, str_5: str_2}
    variables_replacer_0 = module_1.VariablesReplacer(dict_1)
    class_def_1 = variables_replacer_0.visit_ClassDef(class_def_0)

def test_case_10():
    int_0 = 0
    str_0 = 'import random'
    var_0 = module_2.parse(str_0)
    var_1 = var_0.body[int_0]
    var_2 = var_1.names[int_0]
    str_1 = 'random'
    str_2 = 'sys'
    str_3 = {str_1: str_2}
    variables_replacer_0 = module_1.VariablesReplacer(str_3)
    alias_0 = variables_replacer_0.visit_alias(var_2)

def test_case_11():
    str_0 = None
    list_0 = [str_0]
    except_handler_0 = module_0.ExceptHandler(*list_0)
    str_1 = 'Initial ast:\n{}'
    dict_0 = {}
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    dict_1 = {str_1: str_1, str_1: str_1}
    variables_replacer_1 = module_1.VariablesReplacer(dict_1)
    except_handler_1 = variables_replacer_1.visit_ExceptHandler(except_handler_0)

def test_case_12():
    str_0 = 'def test(x):\n    let(x)\n    x += 1\n    y = 1'
    var_0 = module_2.parse(str_0)
    var_1 = var_0.body
    var_2 = module_2.parse(str_0)
    module_1.extend_tree(var_2, var_0)

def test_case_13():
    dict_0 = {}
    snippet_0 = module_1.snippet(dict_0)

def test_case_14():
    bytes_0 = b'\x18M\x1b\rx\xfb\x8b46)\x8b\xd6'
    module_1.let(bytes_0)
    str_0 = 'def test(x):\n    let(x)\n    x += 1\n    y = 1'
    str_1 = 'reload_module'
    var_0 = module_2.parse(str_1)
    var_1 = var_0.body
    var_2 = module_2.parse(str_0)
    var_3 = {}
    module_1.extend_tree(var_2, var_3)

def test_case_15():
    str_0 = '\nif True:\n    let(a)\n    a += 1\n    let(y)\n    y = 1\n'
    var_0 = module_2.parse(str_0)
    module_1.extend(str_0)
    iterable_0 = module_1.find_variables(var_0)

def test_case_16():
    str_0 = 'def test(x):\n    let(x)\n    x += 1\n    y = 1'
    list_0 = [str_0]
    str_1 = "%'SET\rcftJ{(;\\wGrMl"
    str_2 = 'let'
    dict_0 = {str_1: str_0, str_2: str_2}
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    a_s_t_0 = module_0.AST()
    iterable_0 = module_1.find_variables(a_s_t_0)
    str_3 = '!'
    import_from_0 = module_0.ImportFrom(*list_0)
    import_from_1 = variables_replacer_0.visit_ImportFrom(import_from_0)
    variables_replacer_1 = module_1.VariablesReplacer(dict_0)
    str_4 = 'wl7yi'
    str_5 = None
    function_def_0 = module_0.FunctionDef()
    function_def_1 = variables_replacer_1.visit_FunctionDef(function_def_0)
    dict_1 = {str_0: str_4, str_4: str_0, str_3: str_4, str_5: str_3}
    variables_replacer_2 = module_1.VariablesReplacer(dict_1)
    var_0 = module_2.parse(str_0)
    module_1.extend_tree(var_0, variables_replacer_2)

def test_case_17():
    str_0 = 'def test(x):\n    let(x)\n    x += 1\n    y = 1'
    module_1.extend(str_0)
    list_0 = [str_0]
    str_1 = '_py_backwards_{}_{}'
    dict_0 = {str_0: str_0, str_1: list_0, str_1: str_1, str_1: list_0}
    import_from_0 = module_0.ImportFrom(*list_0, **dict_0)
    str_2 = '"'
    dict_1 = {str_2: str_0, str_2: str_1, str_2: str_2, str_0: str_2, str_0: str_0, str_0: str_2, str_2: str_0}
    variables_replacer_0 = module_1.VariablesReplacer(dict_1)
    import_from_1 = variables_replacer_0.visit_ImportFrom(import_from_0)
    variables_replacer_1 = module_1.VariablesReplacer(dict_1)
    var_0 = module_2.parse(str_0)
    module_1.extend_tree(var_0, variables_replacer_1)

def test_case_18():
    str_0 = 'extend(var)'
    var_0 = module_2.parse(str_0)
    str_1 = 'var'
    str_2 = 'x = 1'
    var_1 = module_2.parse(str_2)
    var_2 = {str_1: var_1}
    module_1.extend_tree(var_0, var_2)
    str_3 = 'x = 2'
    var_3 = module_2.parse(str_3)
    var_4 = {str_1: var_3}
    module_1.extend_tree(var_0, var_4)
    var_5 = str(var_0)

def test_case_19():
    str_0 = '\nif True:\n    let(a)\n    a += 1\n    let(y)\n    y = 1\n'
    var_0 = module_2.parse(str_0)
    iterable_0 = module_1.find_variables(var_0)

def test_case_20():
    str_0 = 'def test(x):\n    let(x)\n    x += 1\n    y = 1'
    module_1.extend(str_0)
    list_0 = [str_0]
    alias_0 = module_0.alias(*list_0)
    str_1 = '[z?`exH7nB:Ig'
    dict_0 = {str_0: str_0, str_1: str_0}
    variables_replacer_0 = module_1.VariablesReplacer(dict_0)
    alias_1 = variables_replacer_0.visit_alias(alias_0)
    list_1 = None
    dict_1 = {str_0: list_1}
    variables_replacer_1 = module_1.VariablesReplacer(dict_1)
    alias_2 = variables_replacer_1.visit_alias(alias_1)
    class_def_0 = module_0.ClassDef(*list_0)
    variables_replacer_2 = module_1.VariablesReplacer(dict_1)
    class_def_1 = variables_replacer_2.visit_ClassDef(class_def_0)
    a_s_t_0 = module_0.AST()
    iterable_0 = module_1.find_variables(a_s_t_0)
    str_2 = '_py_backwarxds_{_{}'
    str_3 = '!'
    dict_2 = {str_3: str_0, str_3: str_2, str_3: str_3, str_0: str_3, str_0: str_0, str_0: str_3, str_3: str_0}
    class_def_2 = variables_replacer_0.visit_ClassDef(class_def_1)
    variables_replacer_3 = module_1.VariablesReplacer(dict_2)
    str_4 = None
    function_def_0 = module_0.FunctionDef()
    function_def_1 = variables_replacer_3.visit_FunctionDef(function_def_0)
    function_def_2 = variables_replacer_3.visit_FunctionDef(function_def_1)
    dict_3 = {str_0: str_3, str_3: str_0, str_3: str_3, str_4: str_3}
    variables_replacer_4 = module_1.VariablesReplacer(dict_3)
    var_0 = module_2.parse(str_0)
    module_1.extend_tree(var_0, variables_replacer_4)

def test_case_21():
    str_0 = '\nif True:\n    zet(a)\n    a += 1\n    let(y)\n    y = 1\n'
    var_0 = module_2.parse(str_0)
    a_s_t_0 = module_0.AST()
    dict_0 = {str_0: a_s_t_0}
    module_1.extend_tree(a_s_t_0, dict_0)
    module_1.extend(str_0)
    iterable_0 = module_1.find_variables(var_0)