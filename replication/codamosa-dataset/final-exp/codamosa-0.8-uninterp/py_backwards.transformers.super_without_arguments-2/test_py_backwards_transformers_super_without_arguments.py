# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.transformers.super_without_arguments as module_1
import typed_ast.ast3 as module_2

def test_case_0():
    pass

def test_case_1():
    a_s_t_0 = module_0.AST()
    list_0 = [a_s_t_0, a_s_t_0]
    call_0 = module_0.Call(*list_0)
    super_without_arguments_transformer_0 = module_1.SuperWithoutArgumentsTransformer(a_s_t_0)
    call_1 = super_without_arguments_transformer_0.visit_Call(call_0)

def test_case_2():
    str_0 = 'N#T)\x0cm8s4fpQpx:BN'
    var_0 = module_2.parse(str_0)
    var_1 = str(var_0)
    var_2 = module_2.parse(str_0)
    super_without_arguments_transformer_0 = module_1.SuperWithoutArgumentsTransformer(var_2)
    var_3 = super_without_arguments_transformer_0.visit(var_2)
    var_4 = str(var_2)
    str_1 = 'super(arg1, arg2)'
    var_5 = module_2.parse(str_1)
    super_without_arguments_transformer_1 = module_1.SuperWithoutArgumentsTransformer(var_5)
    var_6 = super_without_arguments_transformer_1.visit(var_5)