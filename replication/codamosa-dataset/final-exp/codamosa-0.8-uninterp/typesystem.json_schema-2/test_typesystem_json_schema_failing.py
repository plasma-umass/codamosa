# Automatically generated by Pynguin.
import typesystem.schemas as module_0
import typesystem.json_schema as module_1
import typesystem.fields as module_2

def test_case_0():
    try:
        bool_0 = True
        dict_0 = {bool_0: bool_0, bool_0: bool_0}
        schema_definitions_0 = module_0.SchemaDefinitions()
        field_0 = module_1.type_from_json_schema(dict_0, schema_definitions_0)
        schema_definitions_1 = module_0.SchemaDefinitions()
        field_1 = module_1.not_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'type'
        str_1 = {str_0: str_0}
        field_0 = module_1.from_json_schema(str_1)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'M\xce/'
        dict_0 = {bytes_0: bytes_0}
        schema_definitions_0 = module_0.SchemaDefinitions()
        field_0 = module_1.ref_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
        schema_definitions_0 = module_0.SchemaDefinitions()
        field_0 = module_1.type_from_json_schema(dict_0, schema_definitions_0)
        any_0 = field_0.validate(bool_0)
        dict_1 = {bool_0: bool_0, any_0: field_0}
        field_1 = module_1.enum_from_json_schema(dict_1, schema_definitions_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        schema_definitions_0 = module_0.SchemaDefinitions()
        field_0 = module_1.const_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_5():
    try:
        dict_0 = None
        dict_1 = {dict_0: dict_0, dict_0: dict_0, dict_0: dict_0}
        field_0 = module_1.from_json_schema(dict_1)
        dict_2 = module_1.get_standard_properties(field_0)
        dict_3 = {}
        schema_definitions_0 = module_0.SchemaDefinitions(**dict_3)
        field_1 = module_1.all_of_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_6():
    try:
        dict_0 = {}
        list_0 = []
        schema_definitions_0 = module_0.SchemaDefinitions(*list_0)
        field_0 = module_1.any_of_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = True
        dict_0 = {bool_0: bool_0}
        str_0 = '~lu5\x0bm#G'
        str_1 = ",N.0O{{>t2r@']\rJx"
        dict_1 = {str_0: dict_0, str_0: str_0, str_1: str_0, str_0: str_1}
        schema_definitions_0 = module_0.SchemaDefinitions(**dict_1)
        field_0 = module_1.one_of_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_8():
    try:
        dict_0 = {}
        schema_definitions_0 = module_0.SchemaDefinitions()
        field_0 = module_1.type_from_json_schema(dict_0, schema_definitions_0)
        var_0 = module_1.to_json_schema(field_0, dict_0)
        field_1 = module_1.if_then_else_from_json_schema(dict_0, schema_definitions_0)
    except BaseException:
        pass

def test_case_9():
    try:
        bool_0 = True
        var_0 = None
        dict_0 = {bool_0: var_0, var_0: bool_0, bool_0: var_0}
        var_1 = module_1.to_json_schema(var_0, dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        dict_0 = {}
        schema_definitions_0 = module_0.SchemaDefinitions(**dict_0)
        var_0 = module_1.to_json_schema(schema_definitions_0)
        dict_1 = None
        schema_definitions_1 = module_0.SchemaDefinitions(**dict_1)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'Sr(M~S;\t;\x0bP+a:N'
        dict_0 = {str_0: str_0}
        schema_definitions_0 = module_0.SchemaDefinitions(**dict_0)
        var_0 = module_1.to_json_schema(schema_definitions_0)
    except BaseException:
        pass

def test_case_12():
    try:
        dict_0 = {}
        schema_definitions_0 = module_0.SchemaDefinitions()
        field_0 = module_1.type_from_json_schema(dict_0, schema_definitions_0)
        var_0 = module_1.to_json_schema(field_0, dict_0)
        field_1 = module_1.from_json_schema(dict_0)
        dict_1 = None
        schema_definitions_1 = module_0.SchemaDefinitions(**dict_1)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'if'
        str_1 = 'Q}z3=(z4F8dlTwSS,un^'
        field_0 = module_2.Field(title=str_1, description=str_0)
        var_0 = module_1.to_json_schema(field_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'allOf'
        str_1 = 'default'
        str_2 = 'type'
        str_3 = 'string'
        str_4 = {str_2: str_3}
        str_5 = 'enum'
        str_6 = 'yes'
        str_7 = 'no'
        str_8 = [str_6, str_7]
        str_9 = {str_5: str_8}
        str_10 = [str_4, str_9]
        str_11 = {str_0: str_10, str_1: str_6}
        schema_definitions_0 = module_0.SchemaDefinitions()
        field_0 = module_1.all_of_from_json_schema(str_11, schema_definitions_0)
        any_0 = field_0.validate(str_6)
        any_1 = field_0.validate(str_7)
        any_2 = field_0.validate(str_5)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'enum'
        str_1 = 'default'
        int_0 = 1
        int_1 = 3
        int_2 = [int_0, int_1, int_1]
        int_3 = {str_0: int_2, str_1: int_0}
        field_0 = module_1.enum_from_json_schema(int_3, int_2)
        any_0 = field_0.validate(int_2)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '$ref'
        str_1 = '#/definitions/foo'
        str_2 = {str_0: str_1}
        field_0 = module_1.ref_from_json_schema(str_2, str_0)
        var_0 = {}
        field_1 = module_1.ref_from_json_schema(str_2, var_0)
        var_1 = field_1.to
        var_2 = {}
        field_2 = module_1.ref_from_json_schema(str_2, var_2)
        var_3 = field_2.definitions
        str_3 = 'foo'
        str_4 = {str_0: str_3}
        var_4 = {}
        field_3 = module_1.ref_from_json_schema(str_4, var_4)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '$ref'
        str_1 = '#/definitions/foo'
        str_2 = {str_0: str_1}
        field_0 = module_1.ref_from_json_schema(str_2, str_0)
        var_0 = {}
        field_1 = module_1.ref_from_json_schema(str_2, var_0)
        var_1 = field_1.to
        var_2 = {}
        field_2 = module_1.ref_from_json_schema(str_2, var_2)
        var_3 = field_2.definitions
        var_4 = module_1.to_json_schema(field_2)
    except BaseException:
        pass