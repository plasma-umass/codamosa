# Automatically generated by Pynguin.
import typesystem.fields as module_0

def test_case_0():
    pass

def test_case_1():
    date_0 = module_0.Date()

def test_case_2():
    bool_0 = True
    any_0 = module_0.Any(allow_null=bool_0)
    text_0 = module_0.Text()

def test_case_3():
    str_0 = 'r)<O].?&5O\nVImR{W'
    boolean_0 = module_0.Boolean(title=str_0, default=str_0)

def test_case_4():
    bool_0 = True
    string_0 = module_0.String(allow_blank=bool_0)

def test_case_5():
    time_0 = module_0.Time()
    str_0 = '#6'
    field_0 = module_0.Field(description=str_0)
    any_0 = field_0.get_default_value()

def test_case_6():
    field_0 = module_0.Field()
    union_0 = field_0.__or__(field_0)

def test_case_7():
    string_0 = module_0.String()
    str_0 = '?Y'
    any_0 = string_0.serialize(str_0)
    any_1 = string_0.validate(str_0)

def test_case_8():
    string_0 = module_0.String()
    any_0 = string_0.serialize(string_0)

def test_case_9():
    number_0 = module_0.Number()

def test_case_10():
    float_0 = 364.6641353890635
    number_0 = module_0.Number()
    any_0 = number_0.validate(float_0)

def test_case_11():
    choice_0 = module_0.Choice()

def test_case_12():
    object_0 = module_0.Object()

def test_case_13():
    int_0 = 1709
    dict_0 = {}
    date_0 = module_0.Date(**dict_0)
    object_0 = module_0.Object(additional_properties=date_0, max_properties=int_0)
    any_0 = object_0.validate(dict_0)

def test_case_14():
    dict_0 = {}
    object_0 = module_0.Object()
    any_0 = object_0.validate(dict_0)

def test_case_15():
    array_0 = module_0.Array()

def test_case_16():
    time_0 = module_0.Time()

def test_case_17():
    choice_0 = module_0.Choice()
    const_0 = module_0.Const(choice_0)

def test_case_18():
    int_0 = -1039
    none_type_0 = None
    string_0 = module_0.String(max_length=int_0, min_length=none_type_0)

def test_case_19():
    string_0 = module_0.String()

def test_case_20():
    none_type_0 = None
    int_0 = 1664
    object_0 = module_0.Object(pattern_properties=none_type_0, max_properties=int_0)

def test_case_21():
    bool_0 = False
    string_0 = module_0.String()
    int_0 = 1664
    object_0 = module_0.Object(additional_properties=bool_0, min_properties=int_0)

def test_case_22():
    field_0 = module_0.Field()
    int_0 = 4336
    array_0 = module_0.Array(field_0, field_0, int_0, int_0)

def test_case_23():
    int_0 = None
    number_0 = module_0.Number(exclusive_maximum=int_0, multiple_of=int_0)
    field_0 = module_0.Field()
    bool_0 = True
    field_1 = module_0.Field(allow_null=bool_0)
    union_0 = field_1.__or__(field_0)
    any_0 = union_0.validate(int_0)

def test_case_24():
    bytes_0 = b'+\x10\xafnt\xe5v\xb1\x9f\xa3\xa1\x1c\xff\xf8<J6\x05\x12'
    choice_0 = module_0.Choice()
    choice_1 = module_0.Choice(choices=bytes_0)

def test_case_25():
    bool_0 = False
    array_0 = module_0.Array()
    any_0 = array_0.serialize(bool_0)
    field_0 = module_0.Field()

def test_case_26():
    float_0 = 364.6641353890635
    number_0 = module_0.Number(minimum=float_0, maximum=float_0)
    any_0 = number_0.validate(float_0)

def test_case_27():
    str_0 = ''
    bool_0 = True
    int_0 = 3349
    string_0 = module_0.String(allow_blank=bool_0, max_length=int_0, pattern=str_0, format=str_0)
    any_0 = string_0.validate(str_0)

def test_case_28():
    object_0 = module_0.Object()
    int_0 = 1698
    str_0 = 'M\n*&&alFTT'
    string_0 = module_0.String(max_length=int_0, min_length=int_0, pattern=str_0)

def test_case_29():
    string_0 = module_0.String()
    bool_0 = True
    object_0 = module_0.Object(properties=string_0, additional_properties=bool_0)
    str_0 = '>}&'
    str_1 = {str_0: str_0}
    any_0 = object_0.validate(str_1)

def test_case_30():
    bool_0 = True
    int_0 = 1707
    dict_0 = {}
    object_0 = module_0.Object(additional_properties=bool_0, max_properties=int_0, **dict_0)
    any_0 = object_0.validate(dict_0)

def test_case_31():
    bool_0 = True
    str_0 = ' s an invJlid keywordag$mn for '
    field_0 = module_0.Field()
    dict_0 = {str_0: field_0, str_0: field_0, str_0: field_0}
    object_0 = module_0.Object(pattern_properties=dict_0, additional_properties=bool_0)
    any_0 = object_0.validate(dict_0, strict=bool_0)

def test_case_32():
    str_0 = '%'
    choice_0 = module_0.Choice(choices=str_0)
    validation_result_0 = choice_0.validate_or_error(str_0)
    string_0 = module_0.String(pattern=str_0)
    any_0 = string_0.validate(str_0)

def test_case_33():
    str_0 = 'QVM'
    field_0 = module_0.Field()
    dict_0 = {str_0: field_0, str_0: field_0, str_0: field_0}
    int_0 = 1684
    object_0 = module_0.Object(properties=dict_0, additional_properties=field_0, min_properties=int_0)

def test_case_34():
    bool_0 = False
    int_0 = 1707
    dict_0 = {}
    object_0 = module_0.Object(additional_properties=bool_0, max_properties=int_0, **dict_0)
    any_0 = object_0.validate(dict_0)

def test_case_35():
    int_0 = 1664
    dict_0 = {}
    bool_0 = None
    object_0 = module_0.Object(additional_properties=bool_0, max_properties=int_0, **dict_0)
    any_0 = object_0.validate(dict_0)

def test_case_36():
    bool_0 = True
    str_0 = '6t!-+|Q)w1n'
    string_0 = module_0.String(allow_blank=bool_0, format=str_0)
    validation_result_0 = string_0.validate_or_error(str_0, strict=bool_0)

def test_case_37():
    bool_0 = False
    list_0 = []
    array_0 = module_0.Array(list_0, bool_0, bool_0)
    any_0 = array_0.validate(list_0)

def test_case_38():
    choice_0 = None
    array_0 = module_0.Array()
    any_0 = array_0.serialize(choice_0)
    bool_0 = True
    str_0 = '6ta!-+|Q)w1n'
    string_0 = module_0.String(allow_blank=bool_0, format=str_0)
    any_1 = string_0.validate(choice_0)

def test_case_39():
    int_0 = 1671
    dict_0 = {}
    int_1 = -2327
    date_0 = module_0.Date()
    dict_1 = {}
    object_0 = module_0.Object(properties=date_0, pattern_properties=dict_1, min_properties=int_1, max_properties=int_0)
    any_0 = object_0.validate(dict_0)

def test_case_40():
    dict_0 = {}
    str_0 = ' is an Xnvalid keyword argument,for '
    field_0 = module_0.Field(description=str_0)
    str_1 = "Eo+S-ZW(T\nUy\r^km.>'"
    dict_1 = {str_0: field_0, str_0: field_0, str_1: field_0, str_1: field_0}
    object_0 = module_0.Object(properties=dict_1)
    any_0 = object_0.validate(dict_0)

def test_case_41():
    float_0 = 688.4773
    number_0 = module_0.Number(multiple_of=float_0)
    any_0 = number_0.validate(float_0)

def test_case_42():
    int_0 = 1668
    str_0 = None
    number_0 = module_0.Number(minimum=int_0, precision=str_0, multiple_of=int_0)
    any_0 = number_0.validate(int_0)

def test_case_43():
    int_0 = None
    number_0 = module_0.Number(maximum=int_0, exclusive_minimum=int_0, multiple_of=int_0)
    choice_0 = module_0.Choice()
    validation_result_0 = choice_0.validate_or_error(int_0)

def test_case_44():
    str_0 = ''
    str_1 = [str_0, str_0, str_0]
    choice_0 = module_0.Choice(choices=str_1)
    validation_result_0 = choice_0.validate_or_error(str_0)

def test_case_45():
    int_0 = 1467
    integer_0 = module_0.Integer(minimum=int_0, maximum=int_0)
    integer_1 = [integer_0]
    union_0 = module_0.Union(integer_1)
    any_0 = union_0.validate(int_0)

def test_case_46():
    integer_0 = module_0.Integer()
    integer_1 = module_0.Integer()
    integer_2 = [integer_0, integer_1]
    integer_3 = module_0.Integer()
    bool_0 = True
    int_0 = 2
    int_1 = 3
    array_0 = module_0.Array(integer_2, integer_3, int_0, int_1, bool_0)
    int_2 = 1
    int_3 = 2
    int_4 = 3
    int_5 = 4
    int_6 = [int_2, int_3, int_4, int_5]
    any_0 = array_0.serialize(int_6)

def test_case_47():
    str_0 = 'choice1'
    str_1 = (str_0, str_0)
    str_2 = (str_1, str_1)
    str_3 = [str_1, str_2]
    choice_0 = module_0.Choice(choices=str_3)
    str_4 = 'al9%\x0c\\y\t]UBz'
    var_0 = Exception(str_4)

def test_case_48():
    bool_0 = True
    str_0 = 'This is an array.'
    int_0 = 5
    string_0 = module_0.String()
    int_1 = 10
    string_1 = module_0.String(max_length=int_1)
    string_2 = [string_0, string_1, string_1]
    string_3 = module_0.String()
    array_0 = module_0.Array(string_2, string_3, bool_0, int_0)
    var_0 = array_0.items
    var_1 = len(var_0)

def test_case_49():
    string_0 = module_0.String()
    number_0 = module_0.Number()
    var_0 = [string_0, string_0, number_0, number_0]
    array_0 = module_0.Array()
    any_0 = array_0.validate(var_0)

def test_case_50():
    int_0 = 553
    integer_0 = module_0.Integer(minimum=int_0, maximum=int_0)
    integer_1 = [integer_0, integer_0]
    union_0 = module_0.Union(integer_1)
    bool_0 = True
    str_0 = 'QE*.;.~Dooe7NyvHq{\x0c'
    bool_1 = False
    any_0 = module_0.Any(description=str_0, allow_null=bool_1)
    array_0 = module_0.Array(any_0, bool_1)
    any_1 = array_0.validate(integer_1, strict=bool_0)

def test_case_51():
    choice_0 = None
    bool_0 = True
    str_0 = '6t!-+|Q)w1n'
    string_0 = module_0.String(allow_blank=bool_0, format=str_0)
    any_0 = string_0.validate(choice_0)

def test_case_52():
    string_0 = module_0.String()
    string_1 = module_0.String()
    var_0 = string_0 | string_1
    integer_0 = module_0.Integer()
    string_2 = module_0.String()
    var_1 = integer_0 | string_2
    var_2 = var_1 | var_0

def test_case_53():
    str_0 = 'abc'
    string_0 = module_0.String()
    string_1 = {str_0: string_0}
    bool_0 = False
    object_0 = module_0.Object(properties=string_1, additional_properties=bool_0)
    str_1 = 'test'
    str_2 = {str_0: str_1}
    any_0 = object_0.validate(str_2)

def test_case_54():
    list_0 = []
    union_0 = module_0.Union(list_0)
    int_0 = 55
    integer_0 = module_0.Integer(minimum=int_0, maximum=int_0)
    integer_1 = [integer_0]
    union_1 = module_0.Union(integer_1)
    union_2 = module_0.Union(list_0)
    float_0 = 86.145316
    number_0 = module_0.Number(maximum=float_0, exclusive_maximum=float_0)
    any_0 = number_0.validate(int_0)