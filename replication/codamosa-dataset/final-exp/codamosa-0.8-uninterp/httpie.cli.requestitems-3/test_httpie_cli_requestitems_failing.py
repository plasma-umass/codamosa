# Automatically generated by Pynguin.
import httpie.cli.argtypes as module_0
import httpie.cli.requestitems as module_1

def test_case_0():
    try:
        str_0 = None
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        optional_0 = module_1.process_header_arg(key_value_arg_0)
        str_1 = module_1.load_text_file(key_value_arg_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '\x0caPic^ ~WhNkHhK/,1N'
        str_1 = ')c;BLjgM`)}G3]bkO'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_1)
        str_2 = module_1.process_empty_header_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = None
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        str_1 = module_1.process_query_param_arg(key_value_arg_0)
        str_2 = module_1.process_data_embed_file_contents_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '\x0caPic^ ~WhNkHhK/,1N'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        tuple_0 = module_1.process_file_upload_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'gAiY\'\\*/3`.d"Oy; k'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        str_1 = module_1.process_data_embed_file_contents_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'KdfA:'
        str_1 = '&XYe'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_1, str_0)
        var_0 = module_1.process_data_embed_raw_json_file_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '\x0caPic^ ~WhNkHhK/,1N'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        var_0 = module_1.process_data_raw_json_embed_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'Too many redirects (--max-redirects='
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        str_1 = module_1.load_text_file(key_value_arg_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = None
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        str_1 = module_1.process_data_embed_file_contents_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '~YxNo'
        request_items_0 = module_1.RequestItems(str_0)
        str_1 = None
        key_value_arg_0 = module_0.KeyValueArg(str_1, str_1, str_1, str_0)
        str_2 = module_1.process_data_embed_file_contents_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '0'
        str_1 = '#af8700'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_1, str_0)
        optional_0 = module_1.process_header_arg(key_value_arg_0)
        key_value_arg_1 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        tuple_0 = module_1.process_file_upload_arg(key_value_arg_1)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = None
        str_1 = None
        str_2 = '8U0~w'
        str_3 = None
        str_4 = None
        str_5 = '-I'
        str_6 = 'RequestItems'
        key_value_arg_0 = module_0.KeyValueArg(str_4, str_2, str_5, str_6)
        optional_0 = module_1.process_header_arg(key_value_arg_0)
        key_value_arg_1 = module_0.KeyValueArg(str_2, str_0, str_1, str_3)
        var_0 = module_1.load_json(key_value_arg_1, str_1)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'd7N6(&D>Kj7)b`c$>'
        str_1 = None
        key_value_arg_0 = module_0.KeyValueArg(str_1, str_1, str_0, str_1)
        str_2 = module_1.process_empty_header_arg(key_value_arg_0)
        str_3 = module_1.process_data_embed_file_contents_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '0'
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        var_0 = module_1.process_data_raw_json_embed_arg(key_value_arg_0)
        tuple_0 = module_1.process_file_upload_arg(key_value_arg_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = ';type='
        key_value_arg_0 = module_0.KeyValueArg(str_0, str_0, str_0, str_0)
        tuple_0 = module_1.process_file_upload_arg(key_value_arg_0)
    except BaseException:
        pass