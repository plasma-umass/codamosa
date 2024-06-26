# Automatically generated by Pynguin.
import typesystem.tokenize.tokenize_yaml as module_0
import typesystem.fields as module_1

def test_case_0():
    try:
        str_0 = '\n    test: value\n    list:\n    - item1\n   - item2\n    '
        token_0 = module_0.tokenize_yaml(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ' '
        any_0 = module_0.validate_yaml(str_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xb4`\\S\x08\x19L'
        token_0 = module_0.tokenize_yaml(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '\nname: John\nemail: john@example.com\nage: 28\n    '
        any_0 = module_0.validate_yaml(str_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'number'
        str_1 = '1.23'
        token_0 = module_0.tokenize_yaml(str_1)
        str_2 = ''
        field_0 = module_1.Field(title=str_2)
        any_0 = module_0.validate_yaml(str_0, field_0)
    except BaseException:
        pass