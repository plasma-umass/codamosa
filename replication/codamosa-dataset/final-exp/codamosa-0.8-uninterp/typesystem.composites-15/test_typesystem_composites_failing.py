# Automatically generated by Pynguin.
import typesystem.composites as module_0
import typesystem.fields as module_1

def test_case_0():
    try:
        str_0 = '/r$\t'
        bytes_0 = b'/\x10@\x8a\x10\xb5\xa0\x85\x97q\x90\xd7q'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: bytes_0}
        never_match_0 = module_0.NeverMatch(**dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xa2\x14\xe9,K\xee1\x1b\xddG\xf0M\x95\x93\xa3'
        never_match_0 = module_0.NeverMatch()
        any_0 = never_match_0.validate(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        list_0 = []
        one_of_0 = module_0.OneOf(list_0)
        any_0 = one_of_0.validate(one_of_0)
    except BaseException:
        pass

def test_case_3():
    try:
        list_0 = []
        str_0 = '*r\\LvnX{'
        dict_0 = {str_0: str_0}
        all_of_0 = module_0.AllOf(list_0)
        any_0 = all_of_0.validate(str_0)
        never_match_0 = module_0.NeverMatch(**dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        list_0 = []
        all_of_0 = module_0.AllOf(list_0)
        str_0 = ''
        field_0 = module_1.Field(description=str_0)
        str_1 = '_;8fP'
        bool_0 = False
        field_1 = module_1.Field(description=str_1, allow_null=bool_0)
        list_1 = [field_0, field_0, field_0, field_1]
        all_of_1 = module_0.AllOf(list_1)
        any_0 = all_of_1.validate(all_of_0)
    except BaseException:
        pass

def test_case_5():
    try:
        any_0 = module_1.Any()
        not_0 = module_0.Not(any_0)
        any_1 = not_0.validate(any_0)
    except BaseException:
        pass

def test_case_6():
    try:
        any_0 = module_1.Any()
        any_1 = module_1.Any()
        any_2 = module_1.Any()
        any_3 = [any_0, any_1, any_2]
        one_of_0 = module_0.OneOf(any_3)
        int_0 = 8
        any_4 = one_of_0.validate(int_0)
    except BaseException:
        pass

def test_case_7():
    try:
        never_match_0 = module_0.NeverMatch()
        any_0 = module_1.Any()
        any_1 = [any_0, never_match_0, any_0]
        one_of_0 = module_0.OneOf(any_1)
        bool_0 = True
        field_0 = module_1.Field(allow_null=bool_0)
        not_0 = module_0.Not(field_0)
        str_0 = 'toto'
        any_2 = one_of_0.validate(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        field_0 = module_1.Field()
        str_0 = 'allow_null'
        dict_0 = {str_0: field_0, str_0: str_0}
        if_then_else_0 = module_0.IfThenElse(field_0, **dict_0)
    except BaseException:
        pass