# Automatically generated by Pynguin.
import typesystem.tokenize.tokenize_yaml as module_0

def test_case_0():
    try:
        bytes_0 = b',1'
        token_0 = module_0.tokenize_yaml(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\x07}\xed1\xf3\xf6\xbd\xf4\xb0\xf9\x8a'
        token_0 = module_0.tokenize_yaml(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b''
        token_0 = module_0.tokenize_yaml(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b':\xfd\x82\x12\n\xf8&K\x06t\xd2@\xba\xe5\x93['
        any_0 = module_0.validate_yaml(bytes_0, bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'U"_'
        any_0 = module_0.validate_yaml(bytes_0, bytes_0)
    except BaseException:
        pass