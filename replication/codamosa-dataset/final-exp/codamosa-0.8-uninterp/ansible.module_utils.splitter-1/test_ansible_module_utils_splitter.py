# Automatically generated by Pynguin.
import ansible.module_utils.splitter as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = ')\tN 1~bTmCF`6'
    var_0 = module_0.is_quoted(str_0)

def test_case_2():
    bytes_0 = b'\xb7\xb5N\xfd\xb1\xed\xfa\x9d\xeeNc\x059o\x18'
    var_0 = module_0.unquote(bytes_0)

def test_case_3():
    set_0 = set()
    var_0 = module_0.is_quoted(set_0)

def test_case_4():
    str_0 = '"test"'
    var_0 = module_0.unquote(str_0)
    str_1 = "'test'"
    var_1 = module_0.unquote(str_1)
    str_2 = '"test'
    var_2 = module_0.unquote(str_2)
    str_3 = "'test"
    var_3 = module_0.unquote(str_3)

def test_case_5():
    str_0 = '"foo"'
    var_0 = module_0.is_quoted(str_0)
    str_1 = "'foo'"
    var_1 = module_0.is_quoted(str_1)
    str_2 = 'foo'
    var_2 = module_0.is_quoted(str_2)

def test_case_6():
    str_0 = "'foox"
    var_0 = module_0.is_quoted(str_0)