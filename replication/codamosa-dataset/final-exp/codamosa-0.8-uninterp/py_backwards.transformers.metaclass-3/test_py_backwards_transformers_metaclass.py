# Automatically generated by Pynguin.
import typed_ast.ast3 as module_0
import py_backwards.transformers.metaclass as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = 'class A(B): pass'
    var_0 = module_0.parse(str_0)
    metaclass_transformer_0 = module_1.MetaclassTransformer(var_0)
    var_1 = metaclass_transformer_0.visit(var_0)
    str_1 = 'class A(metaclass=B): pass'
    var_2 = module_0.parse(str_1)
    var_3 = metaclass_transformer_0.visit(var_2)