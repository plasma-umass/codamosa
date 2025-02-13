# Automatically generated by Pynguin.
import string_utils.validation as module_0

def test_case_0():
    try:
        str_0 = None
        bool_0 = True
        bool_1 = module_0.is_isbn_10(str_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = None
        bool_0 = module_0.is_number(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'D:5O/'
        bool_0 = module_0.is_url(str_0)
        bool_1 = module_0.is_string(str_0)
        bool_2 = module_0.is_credit_card(str_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'A%5>13rzMCS'
        bytes_0 = b'\x91 \x93\xf4\xb8y\xdb\xfb^.'
        bool_0 = module_0.is_url(str_0, bytes_0)
        str_1 = None
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'E\tOQj?")p"M,K@_X`'
        bool_0 = module_0.is_snake_case(str_0)
        list_0 = []
        bool_1 = module_0.is_camel_case(list_0)
        str_1 = None
        bool_2 = True
        bool_3 = module_0.is_isbn_13(str_1, bool_2)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '9upE]sq#3\r'
        int_0 = module_0.words_count(str_0)
        bool_0 = module_0.is_email(str_0)
        bool_1 = module_0.is_isbn_10(str_0)
        str_1 = '\n    Remove html code contained into the given string.\n\n    *Examples:*\n\n    >>> strip_html(\'test: <a href="foo/bar">click here</a>\') # returns \'test: \'\n    >>> strip_html(\'test: <a href="foo/bar">click here</a>\', keep_tag_content=True) # returns \'test: click here\'\n\n    :param input_string: String to manipulate.\n    :type input_string: str\n    :param keep_tag_content: True to preserve tag content, False to remove tag and its content too (default).\n    :type keep_tag_content: bool\n    :return: String with html removed.\n    '
        bool_2 = module_0.is_integer(str_0)
        bool_3 = module_0.contains_html(str_1)
        bool_4 = module_0.is_pangram(str_0)
        dict_0 = {bool_4: bool_2}
        bool_5 = module_0.is_credit_card(dict_0)
        bool_6 = module_0.is_ip(str_0)
        bool_7 = module_0.is_palindrome(str_0, bool_3)
        bool_8 = module_0.is_credit_card(str_1, str_1)
    except BaseException:
        pass

def test_case_6():
    try:
        float_0 = -4176.0
        str_0 = ''
        bool_0 = module_0.contains_html(str_0)
        bool_1 = module_0.is_integer(str_0)
        bool_2 = module_0.is_uuid(float_0)
        list_0 = None
        str_1 = '_@+!`|\x0c'
        bool_3 = module_0.is_isogram(bool_2)
        int_0 = module_0.words_count(str_1)
        str_2 = '#'
        bool_4 = module_0.is_ip(float_0)
        bool_5 = module_0.is_slug(list_0)
        bool_6 = module_0.is_ip_v4(list_0)
        bool_7 = module_0.is_pangram(bool_4)
        str_3 = 'ignore'
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_2, bool_2)
        bool_8 = i_s_b_n_checker_0.is_isbn_13()
        bool_9 = module_0.is_isbn_13(str_3)
        str_4 = None
        int_1 = module_0.words_count(str_4)
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b'KA\xe3'
        bool_0 = module_0.is_email(bytes_0)
        str_0 = '#\\tHFy<OW8'
        bool_1 = module_0.is_isbn_10(str_0)
        float_0 = -133.67
        bool_2 = module_0.is_url(bool_1, float_0)
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
        bool_3 = i_s_b_n_checker_0.is_isbn_13()
        str_1 = ",(&\n{8~o'G~F"
        bool_4 = i_s_b_n_checker_0.is_isbn_13()
        bool_5 = i_s_b_n_checker_0.is_isbn_13()
        bool_6 = module_0.is_slug(bytes_0, str_1)
        str_2 = "'1j'E,^?i1]HQ{5oLZ#"
        bool_7 = module_0.is_isbn_10(str_2)
        bool_8 = i_s_b_n_checker_0.is_isbn_13()
        bool_9 = module_0.is_ip_v4(bytes_0)
        str_3 = None
        bool_10 = module_0.contains_html(str_3)
    except BaseException:
        pass