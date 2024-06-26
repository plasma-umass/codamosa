# Automatically generated by Pynguin.
import string_utils.validation as module_0

def test_case_0():
    try:
        str_0 = None
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '\n    Compress the given string by returning a shorter one that can be safely used in any context (like URL) and\n    restored back to its original state using `decompress()`.\n\n    **Bear in mind:**\n    Besides the provided `compression_level`, the compression result (how much the string is actually compressed\n    by resulting into a shorter string) depends on 2 factors:\n\n    1. The amount of data (string size): short strings might not provide a significant compression result    or even be longer than the given input string (this is due to the fact that some bytes have to be embedded    into the compressed string in order to be able to restore it later on)\n    2. The content type: random sequences of chars are very unlikely to be successfully compressed, while the best    compression result is obtained when the string contains several recurring char sequences (like in the example).\n\n    Behind the scenes this method makes use of the standard Python\'s zlib and base64 libraries.\n\n    *Examples:*\n\n    >>> n = 0 # <- ignore this, it\'s a fix for Pycharm (not fixable using ignore comments)\n    >>> # "original" will be a string with 169 chars:\n    >>> original = \' \'.join([\'word n{}\'.format(n) for n in range(20)])\n    >>> # "compressed" will be a string of 88 chars\n    >>> compressed = compress(original)\n\n    :param input_string: String to compress (must be not empty or a ValueError will be raised).\n    :type input_string: str\n    :param encoding: String encoding (default to "utf-8").\n    :type encoding: str\n    :param compression_level: A value between 0 (no compression) and 9 (best compression), default to 9.\n    :type compression_level: int\n    :return: Compressed string.\n    '
        bool_0 = module_0.is_email(str_0)
        bool_1 = module_0.contains_html(str_0)
        str_1 = None
        bool_2 = module_0.is_url(bool_1)
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_1)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'sf'
        bool_0 = module_0.is_pangram(str_0)
        bool_1 = module_0.is_string(str_0)
        bool_2 = module_0.is_json(bool_0)
        bool_3 = module_0.is_full_string(bool_0)
        bool_4 = module_0.is_credit_card(str_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'true'
        bool_0 = module_0.contains_html(str_0)
        int_0 = 1423
        tuple_0 = (int_0,)
        bool_1 = module_0.is_ip(tuple_0)
        str_1 = '&7dMuo\nO+1oEtWCuJ\rb\n'
        bool_2 = module_0.is_snake_case(str_1, str_1)
        bool_3 = module_0.is_decimal(str_0)
        bool_4 = module_0.is_decimal(str_1)
        str_2 = 'd$7Gem'
        bool_5 = module_0.is_isbn(str_2)
        str_3 = None
        bool_6 = module_0.contains_html(str_3)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = None
        int_0 = module_0.words_count(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'P52#;vx&6B$I>'
        bool_0 = module_0.is_isbn_13(str_0)
        str_1 = 'zeW:"1TX75A'
        bool_1 = module_0.is_pangram(str_1)
        bool_2 = module_0.is_ip_v4(str_1)
        bool_3 = module_0.is_url(str_0, bool_2)
        bool_4 = module_0.is_integer(str_1)
        bool_5 = module_0.is_slug(bool_2, str_0)
        str_2 = ' '
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_2)
        bool_6 = i_s_b_n_checker_0.is_isbn_10()
        str_3 = None
        bool_7 = module_0.is_number(str_3)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'test@test.com'
        str_1 = 'me@gmail.com'
        bool_0 = module_0.is_email(str_0)
        str_2 = 'me.@gmail.com'
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_2)
        bool_1 = i_s_b_n_checker_0.is_isbn_10()
        bool_2 = module_0.is_email(bool_0)
        str_3 = '"me.@gmail.com"@gmail.com'
        bool_3 = module_0.is_email(str_3)
        str_4 = 'ascii'
        bool_4 = i_s_b_n_checker_0.is_isbn_13()
        bool_5 = module_0.is_string(bool_2)
        bool_6 = module_0.is_json(str_3)
        bool_7 = module_0.is_credit_card(str_1, str_4)
    except BaseException:
        pass