# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.transformers.starred_unpacking as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = '%PW tvL>l+6TB\x0c#xH+'
    list_0 = [str_0, str_0]
    list_1 = module_0.List(*list_0)
    a_s_t_0 = module_0.AST()
    starred_unpacking_transformer_0 = module_1.StarredUnpackingTransformer(a_s_t_0)
    list_2 = starred_unpacking_transformer_0.visit_List(list_1)

def test_case_2():
    bytes_0 = b'\xb1e\xfbt\xfb\xab\xd0\xc7\x8f'
    list_0 = [bytes_0, bytes_0]
    call_0 = module_0.Call(*list_0)
    a_s_t_0 = module_0.AST()
    starred_unpacking_transformer_0 = module_1.StarredUnpackingTransformer(a_s_t_0)
    call_1 = starred_unpacking_transformer_0.visit_Call(call_0)