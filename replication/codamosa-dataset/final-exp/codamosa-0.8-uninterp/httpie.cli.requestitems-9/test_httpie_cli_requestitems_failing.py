# Automatically generated by Pynguin.
import httpie.cli.argtypes as module_0
import httpie.cli.requestitems as module_1

def test_case_0():
    try:
        str_0 = None
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        optional_0 = module_1.process_header_arg(key_value_arg_0)
        str_1 = module_1.process_data_embed_file_contents_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_1():
    try:
        tuple_0 = ()
        request_items_0 = module_1.RequestItems(tuple_0)
        str_0 = 'JUWINS&tV%Z$ZA%wCf'
        str_1 = ')\x0b'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_1)
        str_2 = module_1.process_empty_header_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_2():
    try:
        key_value_arg_0 = None
        str_0 = module_1.process_query_param_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = "'\\"
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        tuple_0 = module_1.process_file_upload_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_4():
    try:
        key_value_arg_0 = None
        str_0 = module_1.process_data_item_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = None
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        str_1 = module_1.process_data_embed_file_contents_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = ')DJN'
        str_1 = 'error'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_1, str_1)
        var_0 = module_1.process_data_embed_raw_json_file_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'P3p@6mm~Li\x0bb|U\x0bC;'
        str_1 = None
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_1)
        var_0 = module_1.load_json(key_value_arg_0, str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'G``mn7xvjaw\x0bg;@gA'
        none_type_0 = None
        str_1 = 'C*P'
        str_2 = '\n_@dHAjbZh'
        key_value_arg_0 = module_0.KeyValueArg(str_0, none_type_0, str_1, str_2)
        var_0 = module_1.process_data_raw_json_embed_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = "\n    Return the path to the httpie configuration directory.\n\n    This directory isn't guaranteed to exist, and nor are any of its\n    ancestors (only the legacy ~/.httpie, if returned, is guaranteed to exist).\n\n    XDG Base Directory Specification support:\n\n        <https://wiki.archlinux.org/index.php/XDG_Base_Directory>\n\n        $XDG_CONFIG_HOME is supported; $XDG_CONFIG_DIRS is not\n\n    "
        str_1 = '--sorted'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_1)
        request_items_0 = module_1.RequestItems(key_value_arg_0)
        tuple_0 = module_1.process_file_upload_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = './test.txt'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        var_0 = module_1.process_data_embed_raw_json_file_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = ';type='
        str_1 = 'c":y-djv)v1U &33X\t'
        str_2 = ''
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_1, str_2)
        tuple_0 = module_1.process_file_upload_arg(key_value_arg_0)
    except BaseException:
        pass