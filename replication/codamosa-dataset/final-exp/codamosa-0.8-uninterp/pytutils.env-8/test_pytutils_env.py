# Automatically generated by Pynguin.
import pytutils.env as module_0

def test_case_0():
    generator_0 = module_0.parse_env_file_contents()

def test_case_1():
    str_0 = 'mJ=X~ksvAG8(2cX<o'
    str_1 = module_0.expand(str_0)

def test_case_2():
    str_0 = ''
    ordered_dict_0 = module_0.load_env_file(str_0)

def test_case_3():
    str_0 = '+T(mdH8N`gAc7[$+'
    ordered_dict_0 = module_0.load_env_file(str_0)

def test_case_4():
    str_0 = 'VAR3=This is not'
    str_1 = [str_0, str_0, str_0]
    ordered_dict_0 = module_0.load_env_file(str_1)

def test_case_5():
    str_0 = 'THISIS=~/a/test'
    generator_0 = module_0.parse_env_file_contents()
    var_0 = dict()
    list_0 = [str_0, str_0]
    mutable_mapping_0 = None
    ordered_dict_0 = module_0.load_env_file(list_0, mutable_mapping_0)

def test_case_6():
    str_0 = ''
    str_1 = [str_0]
    generator_0 = module_0.parse_env_file_contents(str_1)
    str_2 = 'a'
    str_3 = 'b'
    str_4 = [str_2, str_3]
    generator_1 = module_0.parse_env_file_contents(str_4)
    var_0 = list(generator_1)
    str_5 = 'a=1'
    str_6 = [str_5]
    generator_2 = module_0.parse_env_file_contents(str_6)
    var_1 = list(generator_2)
    str_7 = 'b=2'
    str_8 = [str_5, str_7]
    str_9 = '\x0c~\t6Ai"by1w+|NiT}'
    generator_3 = module_0.parse_env_file_contents(str_9)
    generator_4 = module_0.parse_env_file_contents(str_8)
    var_2 = list(generator_4)
    str_10 = 'a=""This is a test""'
    str_11 = [str_10]
    generator_5 = module_0.parse_env_file_contents(str_11)
    var_3 = list(generator_5)
    str_12 = [str_3]
    generator_6 = module_0.parse_env_file_contents(str_12)

def test_case_7():
    str_0 = "WORLD='hello'"
    str_1 = 'HELLO=\'hello \\"HELLO\\"\''
    str_2 = 'UNQUOTED=\'hello "HELLO"\''
    str_3 = "UNQUOTED_UNESCAPED='hello'"
    str_4 = [str_0, str_1, str_2, str_3]
    generator_0 = module_0.parse_env_file_contents(str_4)
    var_0 = list(generator_0)