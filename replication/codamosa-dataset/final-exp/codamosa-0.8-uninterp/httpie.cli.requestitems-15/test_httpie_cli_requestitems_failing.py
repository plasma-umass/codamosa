# Automatically generated by Pynguin.
import httpie.cli.argtypes as module_0
import httpie.cli.requestitems as module_1

def test_case_0():
    try:
        str_0 = 'y('
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        optional_0 = module_1.process_header_arg(key_value_arg_0)
        tuple_0 = module_1.process_file_upload_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'x\\(dsc%F|a"x:1s\reX;d'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        str_1 = module_1.process_empty_header_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = ''
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        tuple_0 = module_1.process_file_upload_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = None
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        str_1 = module_1.process_data_embed_file_contents_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = ":L~v9E\tR='s"
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        var_0 = module_1.process_data_embed_raw_json_file_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = ":L~v9E\tR='s"
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        var_0 = module_1.process_data_raw_json_embed_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = None
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        str_1 = module_1.load_text_file(key_value_arg_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '..'
        str_1 = module_1.load_text_file(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bytes_0 = b'\xa0\xfc6$}\xdb\nd\x06\xdd'
        request_items_0 = module_1.RequestItems(bytes_0)
        str_0 = 'ZsH'
        str_1 = ';8'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_1, str_1)
        tuple_0 = module_1.process_file_upload_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = ''
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        optional_0 = module_1.process_header_arg(key_value_arg_0)
        tuple_0 = module_1.process_file_upload_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = None
        str_1 = 'xqMm)7bS|['
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_1, str_1)
        var_0 = module_1.load_json(key_value_arg_0, str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = ''
        str_1 = None
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_1)
        optional_0 = module_1.process_header_arg(key_value_arg_0)
        str_2 = module_1.process_empty_header_arg(key_value_arg_0)
        tuple_0 = module_1.process_file_upload_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '--json'
        str_1 = ''
        str_2 = '{ "a": "b"}'
        str_3 = '_\nr*YxJw%Uz-8H\nGo D'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_2, str_3, str_0)
        var_0 = module_1.process_data_raw_json_embed_arg(key_value_arg_0)
        str_4 = 'data'
        str_5 = "'(@"
        key_value_arg_1 = module_0.KeyValueArg(str_5, str_1, str_4, str_5)
        var_1 = module_1.process_data_raw_json_embed_arg(key_value_arg_1)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '\n    Optional key-value pairs to be included in the request. The separator used\n    determines the type:\n\n    \':\' HTTP headers:\n\n        Referer:http://httpie.org  Cookie:foo=bar  User-Agent:bacon/1.0\n\n    \'==\' URL parameters to be appended to the request URI:\n\n        search==httpie\n\n    \'=\' Data fields to be serialized into a JSON object (with --json, -j)\n        or form data (with --form, -f):\n\n        name=HTTPie  language=Python  description=\'CLI HTTP client\'\n\n    \':=\' Non-string JSON data fields (only with --json, -j):\n\n        awesome:=true  amount:=42  colors:=\'["red", "green", "blue"]\'\n\n    \'@\' Form file fields (only with --form or --multipart):\n\n        cv@~/Documents/CV.pdf\n        cv@\'~/Documents/CV.pdf;type=application/pdf\'\n\n    \'=@\' A data field like \'=\', but takes a file path and embeds its content:\n\n         essay=@Documents/essay.txt\n\n    \':=@\' A raw JSON field like \':=\', but takes a file path and embeds its content:\n\n        package:=@./package.json\n\n    You can use a backslash to escape a colliding separator in the field name:\n\n        field-name-with\\:colon=value\n\n    '
        str_1 = '"#nKDmSR%h"$j|x"NI'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_1, str_1)
        tuple_0 = module_1.process_file_upload_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'w'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        str_1 = module_1.process_data_embed_file_contents_arg(key_value_arg_0)
        tuple_0 = module_1.process_file_upload_arg(key_value_arg_0)
        str_2 = 'tuW\\yk@OO#'
        key_value_arg_1 = module_0.KeyValueArg(str_1, str_1, str_2, str_2)
        tuple_1 = module_1.process_file_upload_arg(key_value_arg_1)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'w'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        tuple_0 = module_1.process_file_upload_arg(key_value_arg_0)
        str_1 = module_1.load_text_file(key_value_arg_0)
        var_0 = module_1.process_data_embed_raw_json_file_arg(key_value_arg_0)
    except BaseException:
        pass