# Automatically generated by Pynguin.
import marshmallow.fields as module_0
import dataclasses_json.cfg as module_1

def test_case_0():
    try:
        global_config_0 = None
        field_0 = module_0.Field(load_default=global_config_0, dump_default=global_config_0, default=global_config_0)
        str_0 = ',kvqFbO'
        dict_0 = module_1.config(mm_field=field_0, undefined=str_0, field_name=str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        optional_0 = None
        dict_0 = module_1.config(bool_0, letter_case=optional_0)
    except BaseException:
        pass

def test_case_2():
    try:
        global_config_0 = module_1._GlobalConfig()
        dict_0 = {global_config_0: global_config_0, global_config_0: global_config_0}
        str_0 = ')\tk$6L.LBAT'
        callable_0 = None
        float_0 = 450.13695
        optional_0 = None
        dict_1 = module_1.config(dict_0, decoder=callable_0, letter_case=float_0, undefined=str_0, field_name=str_0, exclude=optional_0)
    except BaseException:
        pass

def test_case_3():
    try:
        callable_0 = None
        list_0 = [callable_0, callable_0, callable_0, callable_0]
        dict_0 = module_1.config(decoder=callable_0, undefined=list_0)
        global_config_0 = module_1._GlobalConfig()
        str_0 = 'field_many'
        bool_0 = True
        field_0 = module_0.Field(load_default=list_0, data_key=str_0, load_only=bool_0)
        str_1 = '\n    Choose the behavior what happens when an undefined parameter is encountered\n    during class initialization.\n    '
        dict_1 = {str_1: field_0, str_1: list_0}
        field_1 = module_0.Field(dump_default=callable_0, default=dict_0, data_key=str_0, validate=field_0, allow_none=bool_0, dump_only=bool_0, metadata=field_0, **dict_1)
    except BaseException:
        pass

def test_case_4():
    try:
        global_config_0 = module_1._GlobalConfig()
        bytes_0 = b'\xa6\xd0\xa2\x9a\x9e'
        str_0 = 'exclude'
        dict_0 = module_1.config(encoder=bytes_0, undefined=str_0, field_name=str_0)
        str_1 = None
        dict_1 = {}
        bool_0 = False
        field_0 = module_0.Field(required=bool_0, allow_none=bool_0)
        validation_error_0 = field_0.make_error(str_1, **dict_1)
    except BaseException:
        pass