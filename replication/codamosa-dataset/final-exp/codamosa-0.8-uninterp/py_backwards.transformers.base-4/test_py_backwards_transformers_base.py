# Automatically generated by Pynguin.
import py_backwards.transformers.base as module_0
import typed_ast.ast3 as module_1

def test_case_0():
    pass

def test_case_1():
    a_s_t_0 = None
    base_import_rewrite_0 = module_0.BaseImportRewrite(a_s_t_0)

def test_case_2():
    str_0 = 'import six'
    var_0 = module_1.parse(str_0)
    base_import_rewrite_0 = module_0.BaseImportRewrite(var_0)
    var_1 = base_import_rewrite_0.visit(var_0)

def test_case_3():
    str_0 = 'from a import b\n'
    var_0 = module_1.parse(str_0)
    base_import_rewrite_0 = module_0.BaseImportRewrite(var_0)
    var_1 = base_import_rewrite_0.visit(var_0)
    base_import_rewrite_1 = module_0.BaseImportRewrite(str_0)