# Automatically generated by Pynguin.
import typesystem.tokenize.tokenize_yaml as module_0

def test_case_0():
    try:
        str_0 = '@RhkWA'
        token_0 = module_0.tokenize_yaml(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = None
        token_0 = module_0.tokenize_yaml(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xea'
        token_0 = module_0.tokenize_yaml(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '25!<4=U!nZ6\r;<w'
        any_0 = module_0.validate_yaml(str_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'|\x84\x18\xbch+\xeb}\xf9\xea\x10V\xb5\x16\xadR\x06\xb6"'
        token_0 = module_0.tokenize_yaml(bytes_0)
    except BaseException:
        pass