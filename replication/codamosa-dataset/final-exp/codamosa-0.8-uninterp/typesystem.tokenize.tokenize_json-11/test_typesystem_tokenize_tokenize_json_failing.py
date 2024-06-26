# Automatically generated by Pynguin.
import typesystem.tokenize.tokenize_json as module_0
import typesystem.fields as module_1
import typesystem.tokenize.tokens as module_2

def test_case_0():
    try:
        bytes_0 = b'{v\xc3\xebg\xce\xe3\xc2\xa6\xefQv\xf7[r'
        token_0 = module_0.tokenize_json(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'N'
        token_0 = module_0.tokenize_json(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'0+s\x19\xf6\xe9(^\xb4\xc2&\xe1\xb4 \\'
        token_0 = module_0.tokenize_json(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        tokenizing_decoder_0 = module_0._TokenizingDecoder()
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'\x93\x8f\x80'
        token_0 = module_0.tokenize_json(bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '@gaWfEz(4"IyY'
        any_0 = module_0.validate_json(str_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '{'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'n;S"3'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'tel'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'f>p,\x0bYtfX^K1\\#UQn/f'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '\n    {\n        "first_name": "John",\n        "last_name": "Doe",\n        "age": 42,\n        "address": {\n            "city": "Chicago",\n            "state": "Illinois"\n        },\n        "phone_numbers": [\n            {\n                "type": "work",\n                "number": "555-1212"\n            },\n            {\n                "type": "home",\n                "number": "555-1234"\n            }\n        ]\n    }\n    '
        field_0 = module_1.Field()
        any_0 = module_0.validate_json(str_0, field_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '{"foo" "bar"'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '{"foo": "bar", "baz": [, 2, 3]}'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '{"": 1,"bub, ":3'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '{"foo":bar"}'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = '{"foo": "bar",="baz": [1, 2, Z]}'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '{}'
        token_0 = module_0.tokenize_json(str_0)
        var_0 = {}
        int_0 = 0
        int_1 = 1
        dict_token_0 = module_2.DictToken()
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '{"y": 1,"bub, ":'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = '['
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = '\n    {\n        "foo": [{"bar": [1,2, 3.14e10, true, false, null]}],\n        "baz": "qux"\n    }'
        token_0 = module_0.tokenize_json(str_0)
        var_0 = len(token_0)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = '{"u": \n\r1,"b0nb, ":'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass