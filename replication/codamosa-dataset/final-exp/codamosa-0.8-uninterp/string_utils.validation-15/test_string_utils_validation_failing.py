# Automatically generated by Pynguin.
import string_utils.validation as module_0

def test_case_0():
    try:
        str_0 = 'test@test.com'
        bool_0 = module_0.is_email(str_0)
        str_1 = 'test+test@test.com'
        bool_1 = module_0.is_email(str_1)
        str_2 = "7\x0c.|%'Ge"
        bool_2 = module_0.is_isbn(str_2, bool_0)
        list_0 = []
        bool_3 = module_0.is_url(str_0, list_0)
        str_3 = '"test\\.test"@test.com'
        bool_4 = module_0.is_email(str_3)
        str_4 = None
        bool_5 = module_0.is_isbn(str_4)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = None
        bool_0 = module_0.is_decimal(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = None
        int_0 = module_0.words_count(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '*'
        bool_0 = module_0.is_full_string(str_0)
        str_1 = '@ce&'
        bool_1 = module_0.is_palindrome(str_1, bool_0)
        str_2 = "n%e'\r#Y)BN[Q"
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_2)
        bool_2 = i_s_b_n_checker_0.is_isbn_10()
        bool_3 = module_0.is_isogram(str_0)
        bool_4 = module_0.is_isbn_13(str_1)
        bool_5 = module_0.is_string(str_1)
        bool_6 = module_0.is_credit_card(str_1, str_1)
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = 3575.179058
        bool_0 = module_0.is_string(float_0)
        bool_1 = module_0.is_ip_v4(bool_0)
        str_0 = ' T#\x0c_zrn6\x0byM\n'
        bool_2 = module_0.is_json(bool_0)
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0, bool_2)
        str_1 = None
        bool_3 = module_0.contains_html(str_1)
    except BaseException:
        pass