# Automatically generated by Pynguin.
import typed_ast._ast3 as module_0
import py_backwards.utils.tree as module_1
import typed_ast.ast3 as module_2

def test_case_0():
    try:
        a_s_t_0 = module_0.AST()
        a_s_t_1 = module_1.get_parent(a_s_t_0, a_s_t_0)
    except BaseException:
        pass

def test_case_1():
    try:
        a_s_t_0 = module_0.AST()
        tuple_0 = module_1.get_non_exp_parent_and_index(a_s_t_0, a_s_t_0)
    except BaseException:
        pass

def test_case_2():
    try:
        a_s_t_0 = module_0.AST()
        int_0 = 2064
        module_1.insert_at(int_0, a_s_t_0, a_s_t_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = -3306
        str_0 = 'CompilationResult'
        bytes_0 = b'\x84\xe7z\xb5\x94&q\xcb'
        str_1 = 'T?\x0c'
        str_2 = 'FTPHandler'
        dict_0 = {str_0: bytes_0, str_0: int_0, str_1: str_1, str_2: str_0}
        a_s_t_0 = module_0.AST(**dict_0)
        module_1.replace_at(int_0, a_s_t_0, a_s_t_0)
    except BaseException:
        pass

def test_case_4():
    try:
        a_s_t_0 = module_0.AST()
        float_0 = 690.1442721938979
        var_0 = module_1.get_closest_parent_of(a_s_t_0, a_s_t_0, float_0)
    except BaseException:
        pass

def test_case_5():
    try:
        a_s_t_0 = module_0.AST()
        int_0 = 4096
        list_0 = [a_s_t_0, a_s_t_0, a_s_t_0]
        module_1.insert_at(int_0, a_s_t_0, list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        a_s_t_0 = module_0.AST()
        int_0 = 3374
        a_s_t_1 = None
        list_0 = []
        module_1.insert_at(int_0, a_s_t_1, list_0)
        a_s_t_2 = module_1.get_parent(a_s_t_0, a_s_t_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '\nif a:\n    a = 1\nelse:\n    a = 2\na = a\n'
        var_0 = module_2.parse(str_0)
        int_0 = 0
        var_1 = var_0.body[int_0]
        var_2 = var_1.body[int_0]
        tuple_0 = module_1.get_non_exp_parent_and_index(var_0, var_1)
        a_s_t_0 = module_0.AST()
        bool_0 = True
        a_s_t_1 = module_1.get_parent(a_s_t_0, a_s_t_0, bool_0)
    except BaseException:
        pass