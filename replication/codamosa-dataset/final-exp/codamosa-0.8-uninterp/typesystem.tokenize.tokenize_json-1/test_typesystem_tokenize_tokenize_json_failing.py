# Automatically generated by Pynguin.
import typesystem.tokenize.tokenize_json as module_0
import typesystem.fields as module_1

def test_case_0():
    try:
        tokenizing_decoder_0 = module_0._TokenizingDecoder()
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b"\x01\xf7\x8ba\xe0'\x122\xd3\x19\xfdk"
        token_0 = module_0.tokenize_json(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\x8c'
        any_0 = module_0.validate_json(bytes_0, bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'naC4Wq\rq}'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '[vHWl&}zWOr='
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'\xb0f'
        token_0 = module_0.tokenize_json(bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '\n    {\n      "foo": "bar",\n      "bar": "foo",\n      "baz": {\n        "baz": "baz",\n        "foo": false,\n        "bar": true,\n      },\n      "qux": [\n        { "qux": "qux" },\n        null,\n        false,\n        true,\n        "string1",\n        "string2",\n        "string3",\n        1,\n        2,\n        3,\n        -1\n      ]\n    }\n    '
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '\n    {\n      "foo": "bar",\n      "bar": "foo",\n      "bz": {\n        "baz": "baz",\n        "foo": false,\n        "bar": tre,\n      },\n      "qux": [\n        { "qux": "qux" },\n        null,\n        false,\n        true,\n        "string1",\n        "string2",\n        "string3",\n        1,\n        2,\n        3,\n        -1\n      ]\n    }\n    '
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = False
        str_0 = '59'
        field_0 = module_1.Field(description=str_0, allow_null=bool_0)
        any_0 = module_0.validate_json(str_0, field_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '{'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '{"a":[1,2,3], "c": {"b": 4}}'
        token_0 = module_0.tokenize_json(str_0)
        str_1 = '{3a":[1,2,3], "c": {"b": 4}'
        token_1 = module_0.tokenize_json(str_1)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '{"a":[1,2,3], "c": {"b": 4}'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '{"a":[1,2,3], "c": {"b" 4}'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '{}'
        token_0 = module_0.tokenize_json(str_0)
        token_1 = module_0.tokenize_json(str_0)
        str_1 = '100'
        token_2 = module_0.tokenize_json(str_1)
        str_2 = '""'
        token_3 = module_0.tokenize_json(str_2)
        str_3 = 'foo'
        token_4 = module_0.tokenize_json(str_3)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '\n    {\n      "foo": "bar",\n      "bar": "foo",\n      "baz": {\n        "baz": "baz",\n        "foo": false,\n        "bar": true\n      },\n      "qux": [\n        { "qux": "qux" },\n        null,\n        false,\n        true,\n        "string1",\n        "string2",\n        "string3",\n >      1,\n       i2:\n        3,\n        -1\n      ]\n    }\n    '
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = '['
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '9E6\x0cy=\nlPD#=<%bP=4T\t'
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '{"":[1,2,3], "c":{"b": '
        token_0 = module_0.tokenize_json(str_0)
    except BaseException:
        pass