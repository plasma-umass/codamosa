# Automatically generated by Pynguin.
import string_utils.validation as module_0

def test_case_0():
    try:
        set_0 = None
        bool_0 = module_0.is_palindrome(set_0)
        str_0 = None
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
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
        bytes_0 = b'\xe8\xe4\x17\xad'
        bool_0 = True
        bool_1 = False
        str_0 = '~qnvP-2--5uFA2DNl'
        tuple_0 = (bool_0, bool_1, str_0)
        tuple_1 = (bytes_0, tuple_0)
        bool_2 = module_0.is_snake_case(tuple_1)
        str_1 = '9D){(06=hTn'
        str_2 = "O_BNQT'BOwu"
        bool_3 = module_0.is_ip_v4(str_2)
        bool_4 = module_0.is_ip_v6(str_1)
        str_3 = 'L'
        bool_5 = module_0.is_integer(str_3)
        str_4 = 'Qr_3]w*zR?\rPD'
        bool_6 = module_0.is_credit_card(str_4, str_4)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = None
        bool_1 = module_0.is_string(bool_0)
        str_0 = 'gEQ2x'
        bool_2 = module_0.is_isbn_10(str_0)
        str_1 = 'w&K6vR8:G0bQ&Pu'
        bool_3 = True
        bool_4 = module_0.is_palindrome(str_1, bool_3, bool_3)
        str_2 = 's'
        bool_5 = module_0.is_decimal(str_2)
        bool_6 = module_0.is_credit_card(str_1)
        bool_7 = module_0.is_credit_card(str_1, str_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '<)a*q'
        bool_0 = module_0.is_isbn_13(str_0)
        str_1 = None
        bool_1 = module_0.contains_html(str_1)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = -345
        str_0 = "|v'[tEH-"
        bool_0 = module_0.is_json(int_0)
        int_1 = module_0.words_count(str_0)
        bool_1 = module_0.is_decimal(str_0)
        str_1 = None
        int_2 = module_0.words_count(str_1)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '42.0'
        bool_0 = module_0.is_decimal(str_0)
        bool_1 = module_0.is_url(str_0)
        str_1 = 'https://www.website.com:8080'
        bytes_0 = b'\xa1\xc9\xce%&\xa3,\xeb\xfe\x06\\\xeeGP\xa5\xdaHN\xc5'
        bool_2 = module_0.is_url(str_1, bytes_0)
    except BaseException:
        pass