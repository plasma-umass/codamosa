# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.transformers.dict_unpacking as module_1

def test_case_0():
    try:
        module_x_var_0 = module_0.Module()
        a_s_t_0 = module_0.AST()
        dict_unpacking_transformer_0 = module_1.DictUnpackingTransformer(a_s_t_0)
        module_x_var_1 = dict_unpacking_transformer_0.visit_Module(module_x_var_0)
    except BaseException:
        pass

def test_case_1():
    try:
        a_s_t_0 = module_0.AST()
        dict_unpacking_transformer_0 = module_1.DictUnpackingTransformer(a_s_t_0)
        list_0 = [dict_unpacking_transformer_0, dict_unpacking_transformer_0]
        dict_0 = module_0.Dict(*list_0)
        var_0 = dict_unpacking_transformer_0.visit_Dict(dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        list_0 = []
        list_1 = [list_0]
        dict_0 = module_0.Dict(*list_1)
        a_s_t_0 = module_0.AST()
        dict_unpacking_transformer_0 = module_1.DictUnpackingTransformer(a_s_t_0)
        var_0 = dict_unpacking_transformer_0.visit_Dict(dict_0)
        module_x_var_0 = module_0.Module()
        dict_1 = {}
        a_s_t_1 = module_0.AST(**dict_1)
        dict_unpacking_transformer_1 = module_1.DictUnpackingTransformer(a_s_t_1)
        module_x_var_1 = dict_unpacking_transformer_1.visit_Module(module_x_var_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'GYj?}%d=-yv\nW'
        list_0 = [str_0, str_0, str_0]
        list_1 = [list_0, list_0]
        module_x_var_0 = module_0.Module(*list_1)
        dict_0 = {}
        a_s_t_0 = module_0.AST(**dict_0)
        dict_unpacking_transformer_0 = module_1.DictUnpackingTransformer(a_s_t_0)
        module_x_var_1 = dict_unpacking_transformer_0.visit_Module(module_x_var_0)
        a_s_t_1 = module_0.AST()
        dict_unpacking_transformer_1 = module_1.DictUnpackingTransformer(a_s_t_1)
        module_x_var_2 = dict_unpacking_transformer_1.visit_Module(module_x_var_1)
        a_s_t_2 = module_0.AST()
        dict_unpacking_transformer_2 = module_1.DictUnpackingTransformer(a_s_t_2)
        module_x_var_3 = dict_unpacking_transformer_2.visit_Module(module_x_var_2)
        a_s_t_3 = module_0.AST()
        dict_unpacking_transformer_3 = module_1.DictUnpackingTransformer(a_s_t_3)
        module_x_var_4 = dict_unpacking_transformer_3.visit_Module(module_x_var_3)
        str_1 = 'X/V/-/ [\nrC\\W-/'
        str_2 = None
        dict_1 = {str_1: str_1, str_2: str_1, str_2: str_1}
        list_2 = [dict_1, str_1, str_1, dict_1]
        str_3 = 'QA'
        dict_2 = {str_1: dict_1, str_3: dict_1}
        a_s_t_4 = module_0.AST(*list_2, **dict_2)
    except BaseException:
        pass