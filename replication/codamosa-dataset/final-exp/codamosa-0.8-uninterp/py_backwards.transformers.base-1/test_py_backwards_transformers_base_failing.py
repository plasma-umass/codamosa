# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.transformers.base as module_1

def test_case_0():
    try:
        a_s_t_0 = None
        list_0 = [a_s_t_0, a_s_t_0]
        str_0 = 'baz'
        dict_0 = {str_0: str_0}
        import_from_0 = module_0.ImportFrom(*list_0, **dict_0)
        base_import_rewrite_0 = module_1.BaseImportRewrite(a_s_t_0)
        base_import_rewrite_1 = module_1.BaseImportRewrite(a_s_t_0)
        var_0 = base_import_rewrite_1.visit_ImportFrom(import_from_0)
    except BaseException:
        pass