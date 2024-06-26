# Automatically generated by Pynguin.
import typesystem.json_schema as module_0
import typesystem.schemas as module_1
import typesystem.fields as module_2
import typesystem.composites as module_3
import decimal as module_4

def test_case_0():
    pass

def test_case_1():
    dict_0 = {}
    field_0 = module_0.from_json_schema(dict_0)

def test_case_2():
    dict_0 = {}
    schema_definitions_0 = module_1.SchemaDefinitions()
    field_0 = module_0.type_from_json_schema(dict_0, schema_definitions_0)

def test_case_3():
    str_0 = 'enum'
    str_1 = {str_0: str_0}
    schema_definitions_0 = module_1.SchemaDefinitions()
    field_0 = module_0.enum_from_json_schema(str_1, schema_definitions_0)
    var_0 = field_0.__class__

def test_case_4():
    str_0 = 'oneOf'
    str_1 = 'const'
    int_0 = 1
    int_1 = {str_1: int_0}
    int_2 = 2
    int_3 = {str_1: int_2}
    int_4 = [int_1, int_3]
    int_5 = {str_0: int_4}
    schema_definitions_0 = module_1.SchemaDefinitions()
    field_0 = module_0.one_of_from_json_schema(int_5, schema_definitions_0)

def test_case_5():
    tuple_0 = ()
    dict_0 = {tuple_0: tuple_0, tuple_0: tuple_0}
    schema_definitions_0 = module_1.SchemaDefinitions()
    field_0 = module_0.type_from_json_schema(dict_0, schema_definitions_0)
    var_0 = module_0.to_json_schema(field_0)

def test_case_6():
    str_0 = 'not'
    str_1 = 'string'
    str_2 = {str_0: str_1}
    field_0 = module_0.from_json_schema(str_2)

def test_case_7():
    dict_0 = {}
    schema_definitions_0 = module_1.SchemaDefinitions()
    field_0 = module_0.from_json_schema(dict_0, schema_definitions_0)
    field_1 = module_0.type_from_json_schema(dict_0, schema_definitions_0)
    field_2 = module_0.from_json_schema(dict_0, schema_definitions_0)

def test_case_8():
    dict_0 = {}
    field_0 = module_0.from_json_schema(dict_0)
    var_0 = module_0.to_json_schema(field_0)

def test_case_9():
    tuple_0 = ()
    bool_0 = True
    dict_0 = {tuple_0: tuple_0, tuple_0: tuple_0}
    schema_definitions_0 = module_1.SchemaDefinitions()
    field_0 = module_0.from_json_schema(dict_0, schema_definitions_0)
    validation_result_0 = field_0.validate_or_error(tuple_0, strict=bool_0)
    str_0 = 'object'
    field_1 = module_0.from_json_schema_type(dict_0, str_0, bool_0, schema_definitions_0)
    var_0 = module_0.to_json_schema(field_1)

def test_case_10():
    str_0 = '$ref'
    str_1 = '#/definitions/Person'
    str_2 = {str_0: str_1}
    field_0 = module_0.from_json_schema(str_2)
    reference_0 = module_1.Reference(str_1)
    bool_0 = True
    field_1 = module_0.from_json_schema(bool_0)
    any_0 = module_2.Any()
    bool_1 = False
    field_2 = module_0.from_json_schema(bool_1)
    never_match_0 = module_3.NeverMatch()
    str_3 = 'type'
    str_4 = 'null'
    str_5 = {str_3: str_4}
    field_3 = module_0.from_json_schema(str_5)
    var_0 = None
    const_0 = module_2.Const(var_0)
    str_6 = 'boolean'
    str_7 = {str_3: str_6}
    field_4 = module_0.from_json_schema(str_7)
    boolean_0 = module_2.Boolean()
    str_8 = 'number'
    str_9 = {str_3: str_8}
    field_5 = module_0.from_json_schema(str_9)
    float_0 = module_2.Float()
    str_10 = 'integer'
    str_11 = {str_3: str_10}
    field_6 = module_0.from_json_schema(str_11)
    integer_0 = module_2.Integer()

def test_case_11():
    str_0 = 'type'
    str_1 = 'properties'
    str_2 = 'object'
    str_3 = 'name'
    str_4 = 'age'
    str_5 = 'string'
    str_6 = {str_0: str_5}
    str_7 = 'integer'
    str_8 = {str_0: str_7}
    str_9 = {str_3: str_6, str_4: str_8}
    str_10 = {str_0: str_2, str_1: str_9}
    field_0 = module_0.from_json_schema(str_10)
    string_0 = module_2.String()
    integer_0 = module_2.Integer()
    var_0 = {str_3: string_0, str_4: integer_0}
    object_0 = module_2.Object(properties=var_0)

def test_case_12():
    str_0 = 'allOf'
    str_1 = '$ref'
    str_2 = '#/definitions/item1'
    str_3 = {str_1: str_2}
    str_4 = 'type'
    str_5 = 'minimum'
    str_6 = 'maximum'
    str_7 = 'number'
    int_0 = 5
    int_1 = 10
    var_0 = {str_4: str_7, str_5: int_0, str_6: int_1}
    var_1 = [str_3, var_0]
    var_2 = {str_0: var_1}
    str_8 = 'item1'
    str_9 = 'minLength'
    str_10 = 'string'
    int_2 = 2
    var_3 = {str_4: str_10, str_9: int_2}
    var_4 = {str_8: var_3}
    field_0 = module_0.all_of_from_json_schema(var_2, var_4)
    reference_0 = module_1.Reference(str_2)
    number_0 = module_2.Number(minimum=int_0, maximum=int_1)
    var_5 = [reference_0, number_0]
    all_of_0 = module_3.AllOf(var_5)

def test_case_13():
    str_0 = 'allOf'
    str_1 = '#/definitions/item1'
    str_2 = {str_0: str_1}
    str_3 = 'type'
    str_4 = 'minimum'
    str_5 = 'maximum'
    str_6 = 'number'
    int_0 = 5
    int_1 = 10
    var_0 = {str_3: str_6, str_4: int_0, str_5: int_1}
    var_1 = [str_2, var_0]
    var_2 = {str_0: var_1}
    str_7 = 'minLength'
    field_0 = module_0.all_of_from_json_schema(var_2, str_7)
    reference_0 = module_1.Reference(str_1)
    number_0 = module_2.Number(minimum=int_0, maximum=int_1)
    var_3 = [reference_0, number_0]
    all_of_0 = module_3.AllOf(var_3)

def test_case_14():
    str_0 = 'anyOf'
    str_1 = '"z{Jjy@\''
    str_2 = 'maxLength'
    str_3 = 'Helo orld!{'
    var_0 = {str_0: str_2, str_1: str_3}
    var_1 = {}
    field_0 = module_0.any_of_from_json_schema(var_0, var_1)

def test_case_15():
    str_0 = 'if'
    str_1 = 'then'
    dict_0 = {str_0: str_1}
    schema_definitions_0 = module_1.SchemaDefinitions()
    field_0 = module_0.from_json_schema(dict_0, schema_definitions_0)
    field_1 = module_0.type_from_json_schema(dict_0, schema_definitions_0)
    var_0 = module_0.to_json_schema(field_0, dict_0)
    field_2 = module_0.if_then_else_from_json_schema(dict_0, schema_definitions_0)

def test_case_16():
    never_match_0 = module_3.NeverMatch()
    list_0 = [never_match_0]
    var_0 = module_0.to_json_schema(never_match_0, list_0)

def test_case_17():
    str_0 = 'anyOf'
    str_1 = '"z{Jjy@\''
    str_2 = 'maxLength'
    str_3 = 'string'
    int_0 = 100
    var_0 = {str_0: str_1, str_2: int_0, str_1: str_0}
    str_4 = 'integer'
    int_1 = 46
    var_1 = {str_3: str_4, str_1: int_1}
    var_2 = [var_0, var_1]
    var_3 = {str_0: var_2, str_1: str_3}
    var_4 = {str_1: var_2, str_1: str_0}
    field_0 = module_0.any_of_from_json_schema(var_3, var_4)

def test_case_18():
    bool_0 = True
    field_0 = module_0.from_json_schema(bool_0)
    any_0 = module_2.Any()
    bool_1 = False
    field_1 = module_0.from_json_schema(bool_1)
    never_match_0 = module_3.NeverMatch()
    str_0 = 'type'
    str_1 = 'string'
    str_2 = {str_0: str_1}
    field_2 = module_0.from_json_schema(str_2)
    string_0 = module_2.String()
    str_3 = '$ref'
    str_4 = 'definitions'
    str_5 = '#/definitions/Person'
    str_6 = 'Person'
    str_7 = 'properties'
    str_8 = 'object'
    str_9 = 'name'
    str_10 = 'age'
    str_11 = {str_0: str_1}
    str_12 = 'integer'
    str_13 = {str_0: str_12}
    str_14 = {str_9: str_11, str_10: str_13}
    str_15 = {str_0: str_8, str_7: str_14}
    str_16 = {str_6: str_15}
    str_17 = {str_3: str_5, str_4: str_16}
    field_3 = module_0.from_json_schema(str_17)

def test_case_19():
    str_0 = 'type'
    str_1 = 'properties'
    str_2 = 'object'
    str_3 = 'answer'
    str_4 = 'foo'
    str_5 = 'bar'
    str_6 = 'number'
    str_7 = {str_0: str_6}
    str_8 = 'string'
    str_9 = {str_0: str_8}
    str_10 = 'items'
    str_11 = 'array'
    str_12 = {str_0: str_6}
    str_13 = {str_0: str_11, str_10: str_12}
    str_14 = {str_3: str_7, str_4: str_9, str_5: str_13}
    str_15 = {str_0: str_2, str_1: str_14}
    field_0 = module_0.from_json_schema(str_15)

def test_case_20():
    int_0 = 4
    string_0 = module_2.String(max_length=int_0, min_length=int_0)
    schema_definitions_0 = module_1.SchemaDefinitions()
    var_0 = module_0.to_json_schema(schema_definitions_0)

def test_case_21():
    bool_0 = True
    field_0 = module_0.from_json_schema(bool_0)
    any_0 = module_2.Any()
    bool_1 = False
    field_1 = module_0.from_json_schema(bool_1)
    never_match_0 = module_3.NeverMatch()
    str_0 = 'type'
    str_1 = 'string'
    str_2 = {str_0: str_1}
    field_2 = module_0.from_json_schema(str_2)
    string_0 = module_2.String()
    str_3 = 'integer'
    str_4 = {str_0: str_3}
    field_3 = module_0.from_json_schema(str_4)
    integer_0 = module_2.Integer()
    str_5 = 'number'
    str_6 = {str_0: str_5}
    field_4 = module_0.from_json_schema(str_6)
    decimal_0 = module_4.Decimal()
    str_7 = 'boolean'
    str_8 = {str_0: str_7}
    field_5 = module_0.from_json_schema(str_8)
    boolean_0 = module_2.Boolean()
    str_9 = 'array'
    str_10 = {str_0: str_9}
    field_6 = module_0.from_json_schema(str_10)
    any_1 = module_2.Any()
    array_0 = module_2.Array(any_1)
    str_11 = 'object'
    str_12 = {str_0: str_11}
    field_7 = module_0.from_json_schema(str_12)
    object_0 = module_2.Object()
    str_13 = 'enum'
    int_0 = 2
    int_1 = 3
    var_0 = [bool_0, int_0, int_1]
    var_1 = {str_13: var_0}
    field_8 = module_0.from_json_schema(var_1)

def test_case_22():
    bool_0 = False
    string_0 = module_2.String()
    var_0 = module_0.to_json_schema(string_0)

def test_case_23():
    bool_0 = True
    integer_0 = module_2.Integer()
    var_0 = module_0.to_json_schema(integer_0)
    string_0 = module_2.String()
    integer_1 = module_2.Integer()

def test_case_24():
    var_0 = {}
    str_0 = 'boolean'
    bool_0 = False
    schema_definitions_0 = module_1.SchemaDefinitions()
    field_0 = module_0.from_json_schema_type(var_0, str_0, bool_0, schema_definitions_0)
    boolean_0 = module_2.Boolean(allow_null=bool_0)
    var_1 = {}
    bool_1 = True
    schema_definitions_1 = module_1.SchemaDefinitions()
    field_1 = module_0.from_json_schema_type(var_1, str_0, bool_1, schema_definitions_1)
    boolean_1 = module_2.Boolean(allow_null=bool_1)
    var_2 = {}
    str_1 = 'integer'
    schema_definitions_2 = module_1.SchemaDefinitions()
    field_2 = module_0.from_json_schema_type(var_2, str_1, bool_0, schema_definitions_2)
    integer_0 = module_2.Integer()
    var_3 = {}
    schema_definitions_3 = module_1.SchemaDefinitions()
    field_3 = module_0.from_json_schema_type(var_3, str_1, bool_1, schema_definitions_3)
    var_4 = module_0.to_json_schema(field_1)