# Automatically generated by Pynguin.
import typed_ast.ast3 as module_0
import py_backwards.transformers.yield_from as module_1
import typed_ast._ast3 as module_2

def test_case_0():
    pass

def test_case_1():
    int_0 = 3
    str_0 = 'def foo():\n    yield from bar\n    yield from baz\n    '
    var_0 = module_0.parse(str_0)
    yield_from_transformer_0 = module_1.YieldFromTransformer(int_0)
    a_s_t_0 = yield_from_transformer_0.visit(var_0)

def test_case_2():
    int_0 = 24
    str_0 = 'def foo():\n    yield from bar\n    yield fromQaz\n    '
    yield_from_transformer_0 = module_1.YieldFromTransformer(int_0)
    str_1 = 'body'
    dict_0 = {str_1: str_1, str_0: str_1}
    a_s_t_0 = module_2.AST(**dict_0)
    a_s_t_1 = yield_from_transformer_0.visit(a_s_t_0)
    a_s_t_2 = yield_from_transformer_0.visit(a_s_t_0)