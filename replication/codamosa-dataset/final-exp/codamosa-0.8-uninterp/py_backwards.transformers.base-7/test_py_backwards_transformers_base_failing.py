# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.transformers.base as module_1

def test_case_0():
    try:
        import_from_0 = module_0.ImportFrom()
        a_s_t_0 = module_0.AST()
        base_import_rewrite_0 = module_1.BaseImportRewrite(a_s_t_0)
        var_0 = base_import_rewrite_0.visit_ImportFrom(import_from_0)
    except BaseException:
        pass

def test_case_1():
    try:
        import_0 = module_0.Import()
        a_s_t_0 = module_0.AST()
        base_import_rewrite_0 = module_1.BaseImportRewrite(a_s_t_0)
        var_0 = base_import_rewrite_0.visit_Import(import_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        list_0 = [bool_0, bool_0]
        import_from_0 = module_0.ImportFrom(*list_0)
        a_s_t_0 = module_0.AST()
        base_import_rewrite_0 = module_1.BaseImportRewrite(a_s_t_0)
        var_0 = base_import_rewrite_0.visit_ImportFrom(import_from_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 1578
        a_s_t_0 = None
        list_0 = [a_s_t_0, int_0, a_s_t_0]
        import_from_0 = module_0.ImportFrom(*list_0)
        a_s_t_1 = module_0.AST()
        base_import_rewrite_0 = module_1.BaseImportRewrite(a_s_t_1)
        var_0 = base_import_rewrite_0.visit_ImportFrom(import_from_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '9[Ah`W,^v?5{1vfcN'
        list_0 = [str_0, str_0]
        dict_0 = {str_0: str_0}
        import_from_0 = module_0.ImportFrom(*list_0, **dict_0)
        a_s_t_0 = module_0.AST()
        base_import_rewrite_0 = module_1.BaseImportRewrite(a_s_t_0)
        var_0 = base_import_rewrite_0.visit_ImportFrom(import_from_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = ''
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        import_0 = module_0.Import(**dict_0)
        list_0 = [import_0, str_0]
        import_from_0 = module_0.ImportFrom(*list_0, **dict_0)
        a_s_t_0 = module_0.AST()
        base_import_rewrite_0 = module_1.BaseImportRewrite(a_s_t_0)
        var_0 = base_import_rewrite_0.visit_ImportFrom(import_from_0)
    except BaseException:
        pass