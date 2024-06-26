# Automatically generated by Pynguin.
import string_utils.validation as module_0

def test_case_0():
    str_0 = 'y+u(:zKM:-(\x0c'
    bool_0 = module_0.is_string(str_0)

def test_case_1():
    str_0 = '`U`d%@TreQ8Dq`k'
    bool_0 = module_0.is_isbn(str_0)

def test_case_2():
    str_0 = '\rI3P+1@4{+^/8'
    bool_0 = module_0.is_isbn_13(str_0)

def test_case_3():
    str_0 = ')GF\x0c\x0bLbIB#'
    bool_0 = module_0.is_isbn_10(str_0)
    bytes_0 = b'3!\x18\xce)\x02w9S\xe3{\xe9'
    bool_1 = module_0.is_ip_v4(bytes_0)

def test_case_4():
    bool_0 = True
    bool_1 = module_0.is_pangram(bool_0)

def test_case_5():
    str_0 = '42'
    bool_0 = module_0.is_decimal(str_0)

def test_case_6():
    str_0 = ';Wjc\x0cTo3vn`>K7ra_3BM'
    bool_0 = module_0.is_json(str_0)
    str_1 = '`\t)N)=WH'
    bool_1 = module_0.is_ip_v4(str_0)
    bool_2 = module_0.is_integer(str_1)

def test_case_7():
    str_0 = 'G.P\t'
    bool_0 = module_0.is_ip_v4(str_0)
    bool_1 = module_0.is_json(str_0)
    bool_2 = module_0.is_url(bool_1)
    bool_3 = module_0.is_ip_v4(str_0)
    bool_4 = module_0.is_integer(str_0)

def test_case_8():
    str_0 = '255.200.100.75'
    bool_0 = module_0.is_email(str_0)

def test_case_9():
    var_0 = None
    bool_0 = module_0.is_email(var_0)

def test_case_10():
    str_0 = '\n:G5_Ml4H8D\x0cKK:V}'
    bool_0 = module_0.is_ip(str_0)
    bool_1 = module_0.is_credit_card(str_0)
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_2 = i_s_b_n_checker_0.is_isbn_10()

def test_case_11():
    bool_0 = False
    bool_1 = module_0.is_credit_card(bool_0)

def test_case_12():
    str_0 = '4111111111111111'
    bool_0 = module_0.is_credit_card(str_0)
    str_1 = '4111111111111'
    bool_1 = module_0.is_credit_card(str_1)
    str_2 = '4012888888881881'
    bool_2 = module_0.is_credit_card(str_2)
    str_3 = '378282246310005'
    bool_3 = module_0.is_credit_card(str_3)
    str_4 = '6011111111111117'
    bool_4 = module_0.is_credit_card(str_4)
    str_5 = '5105105105105100'
    bool_5 = module_0.is_credit_card(str_5)
    str_6 = '5105 1051 0510 5106'
    bool_6 = module_0.is_credit_card(str_6)
    str_7 = '9111111111111111'
    bool_7 = module_0.is_credit_card(str_7)
    str_8 = '5105105105105106'
    bool_8 = module_0.is_credit_card(str_8)
    bool_9 = module_0.is_credit_card(str_7)
    str_9 = 'VISA'
    bool_10 = module_0.is_credit_card(str_0, str_9)

def test_case_13():
    list_0 = None
    bool_0 = module_0.is_camel_case(list_0)
    str_0 = '\rI3P+1@4{+^/8'
    bool_1 = module_0.is_isbn_13(str_0)

def test_case_14():
    str_0 = '8Oau9imw@3'
    list_0 = [str_0, str_0, str_0, str_0]
    bool_0 = module_0.is_snake_case(list_0)

def test_case_15():
    tuple_0 = ()
    bool_0 = module_0.is_ip(tuple_0)
    str_0 = '@vqL$'
    bool_1 = module_0.is_snake_case(str_0, str_0)

def test_case_16():
    str_0 = '{"name": "Peter"}'
    bool_0 = module_0.is_json(str_0)

def test_case_17():
    str_0 = '{nope}'
    bool_0 = module_0.is_json(str_0)

def test_case_18():
    str_0 = '%eW>ci-e>CO-\n4$\r'
    str_1 = '|X'
    str_2 = 'Input must be a non empty string'
    bool_0 = module_0.is_integer(str_2)
    int_0 = module_0.words_count(str_1)
    bool_1 = module_0.is_uuid(str_0)
    int_1 = module_0.words_count(str_0)
    bool_2 = module_0.is_ip_v6(str_0)
    bool_3 = module_0.is_decimal(str_1)
    bool_4 = module_0.is_email(str_0)

def test_case_19():
    bytes_0 = b'\xa4\n\x07_\x80,'
    str_0 = '0Y1h(g5W.f{'
    bool_0 = module_0.is_isbn(str_0)
    bool_1 = module_0.is_snake_case(bytes_0)
    str_1 = 'OvjX/xDa`O9'
    bool_2 = module_0.is_isogram(str_1)
    str_2 = 'R~osx3_5e\nI'
    str_3 = 'iBgxT~#@U2KY6w!8'
    bool_3 = module_0.is_isbn_13(str_3, bool_2)
    bool_4 = module_0.is_number(str_2)
    bool_5 = module_0.is_number(str_1)
    bool_6 = True
    bool_7 = module_0.is_uuid(str_3, bool_6)

def test_case_20():
    str_0 = '1.2.3'
    bool_0 = module_0.is_ip(str_0)

def test_case_21():
    float_0 = -2638.5
    bool_0 = module_0.is_ip_v6(float_0)

def test_case_22():
    str_0 = 'firstname+lastname@domain.com'
    bool_0 = module_0.is_email(str_0)
    bool_1 = module_0.is_palindrome(str_0)
    bool_2 = module_0.is_email(str_0)
    str_1 = "\r6M6'\x0b)*E:!uXP:7QD^"
    bool_3 = True
    bool_4 = module_0.is_isbn(str_1, bool_3)
    str_2 = ','
    bool_5 = module_0.is_isogram(str_2)

def test_case_23():
    float_0 = -3568.09
    str_0 = '^[a-z]{2}_[a-z]{2}$'
    bool_0 = True
    bool_1 = module_0.is_palindrome(str_0, bool_0)
    bool_2 = True
    bool_3 = True
    bool_4 = module_0.is_palindrome(float_0, bool_2, bool_3)
    str_1 = 'j6B8xXp&{`8)i&.v'
    bool_5 = module_0.is_isbn_10(str_1)
    bool_6 = module_0.is_uuid(float_0)
    bool_7 = module_0.is_pangram(float_0)
    str_2 = 'fH)n\r!ReRnDZqG!'
    str_3 = 'Q'
    str_4 = '\n    Returns a string of the specified size containing random characters (uppercase/lowercase ascii letters and digits).\n\n    *Example:*\n\n    >>> random_string(9) # possible output: "cx3QQbzYg"\n\n    :param size: Desired string size\n    :type size: int\n    :return: Random string\n    '
    list_0 = [str_2, str_2, str_3, str_4]
    bool_8 = module_0.is_url(bool_4, list_0)
    bool_9 = module_0.is_string(str_1)
    bool_10 = module_0.is_camel_case(bool_4)

def test_case_24():
    str_0 = 'Id0C#oHce\\`05z['
    bool_0 = module_0.is_pangram(str_0)

def test_case_25():
    str_0 = ')GF\x0c\x0bLbIB#'
    bool_0 = module_0.is_isbn_10(str_0)
    bytes_0 = b'3!\x18\xce)\x02w9S\xe3{\xe9'
    bool_1 = module_0.is_ip_v4(bytes_0)
    list_0 = None
    bool_2 = module_0.is_url(list_0)
    bool_3 = module_0.is_isogram(list_0)
    bool_4 = module_0.is_pangram(bool_2)

def test_case_26():
    str_0 = '9780312498580'
    bool_0 = module_0.is_slug(str_0, str_0)
    bool_1 = module_0.is_isbn(str_0)
    str_1 = '978-0312498580'
    bool_2 = module_0.is_isbn(str_1)
    str_2 = '1506715214'
    bool_3 = module_0.is_isbn(str_2)
    str_3 = '978-0312498580'
    bool_4 = False
    bool_5 = module_0.is_isbn(str_3, bool_4)

def test_case_27():
    float_0 = -1452.893
    bool_0 = module_0.is_slug(float_0)

def test_case_28():
    str_0 = ',lBdTZAx4Af\x0bHj<{F'
    bool_0 = module_0.contains_html(str_0)

def test_case_29():
    str_0 = '$'
    bool_0 = True
    bool_1 = module_0.is_isbn_13(str_0, bool_0)
    tuple_0 = ()
    str_1 = '9~PT [FV'
    int_0 = module_0.words_count(str_1)
    bool_2 = module_0.is_url(tuple_0)

def test_case_30():
    str_0 = 'msRJ}_vw\rD\n>l'
    bool_0 = module_0.is_isbn_10(str_0)

def test_case_31():
    str_0 = 'y+ua(:zKM:-(\x0c'
    str_1 = 'XS1oTJpw`yz"YQlZS;G'
    bool_0 = False
    bool_1 = module_0.is_isbn(str_1, bool_0)
    bool_2 = module_0.is_string(str_0)
    bool_3 = module_0.is_decimal(str_0)
    bool_4 = module_0.is_slug(bool_0)

def test_case_32():
    str_0 = '9780312498580'
    bool_0 = module_0.is_isbn(str_0)
    str_1 = '978-0312498580'
    bool_1 = module_0.is_isbn(str_1)
    str_2 = '1506715214'
    bool_2 = module_0.is_isbn(str_2)
    str_3 = '978-0312498580'
    bool_3 = False
    bool_4 = module_0.is_isbn(str_3, bool_3)

def test_case_33():
    str_0 = '.'
    bool_0 = module_0.contains_html(str_0)
    str_1 = ')+\t\x0bc$\x0b, @:L_i'
    str_2 = '3Cl\x0bm|\\J70C|\rsf\nV '
    str_3 = 'Invalid token found: "{}"'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_3)
    bool_1 = i_s_b_n_checker_0.is_isbn_10()
    i_s_b_n_checker_1 = module_0.__ISBNChecker(str_2)
    bool_2 = module_0.is_snake_case(str_1)
    bool_3 = module_0.is_uuid(str_1)
    bool_4 = module_0.is_number(str_0)
    bool_5 = module_0.is_isbn(str_1)
    bool_6 = module_0.is_pangram(str_1)
    bool_7 = module_0.is_snake_case(bool_6)
    bool_8 = True
    bool_9 = module_0.is_snake_case(bool_6)
    bool_10 = module_0.is_isbn_10(str_1, bool_8)
    str_4 = "$'3Q~swM n"
    bool_11 = module_0.is_number(str_4)
    str_5 = '\x0c|:;<'
    str_6 = '0'
    bool_12 = module_0.is_pangram(bool_7)
    bool_13 = module_0.is_integer(str_6)
    bool_14 = module_0.is_decimal(str_5)

def test_case_34():
    str_0 = '\nL-:lLk\tlxk'
    str_1 = ',9wou`W'
    bool_0 = module_0.is_url(str_1)
    bool_1 = module_0.is_decimal(str_1)
    bool_2 = module_0.is_decimal(str_0)
    bool_3 = module_0.is_isbn(str_1)
    bool_4 = module_0.is_ip_v4(str_1)

def test_case_35():
    str_0 = 'is_full_string'
    bool_0 = True
    bool_1 = module_0.is_isbn_10(str_0, bool_0)
    str_1 = 'xHu'
    bool_2 = module_0.is_camel_case(str_0)
    list_0 = [str_1, str_1, str_1, str_1]
    bool_3 = module_0.is_ip(str_0)
    bool_4 = module_0.is_url(str_0, list_0)

def test_case_36():
    str_0 = '+rCK?+k}?\n'
    bool_0 = module_0.is_json(str_0)

def test_case_37():
    str_0 = 'foo@bar.com'
    bool_0 = module_0.is_email(str_0)
    str_1 = 'foo@bar.co'
    bool_1 = module_0.is_email(str_1)
    str_2 = 'foo.bar_123@bar.co'
    bool_2 = module_0.is_email(str_2)
    str_3 = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@bar.com'
    bool_3 = module_0.is_email(str_3)
    bool_4 = module_0.is_json(bool_2)

def test_case_38():
    str_0 = '255.200.100.75'
    bool_0 = module_0.is_ip_v4(str_0)
    bool_1 = module_0.is_email(bool_0)
    str_1 = 'u|T\t/h<'
    bool_2 = module_0.is_isbn(str_1)
    bool_3 = module_0.is_isogram(str_0)

def test_case_39():
    str_0 = '"email"@domain.com'
    bool_0 = module_0.is_email(str_0)

def test_case_40():
    str_0 = 'firstname+lastname@domain.com'
    bool_0 = module_0.is_email(str_0)
    str_1 = '1234567890@domain.com'
    bool_1 = module_0.is_ip(str_0)
    bool_2 = module_0.is_email(str_1)

def test_case_41():
    str_0 = 'my.email@the-provider.com'
    bool_0 = module_0.is_email(str_0)
    str_1 = '@gmail.com'
    bool_1 = module_0.is_email(str_1)
    str_2 = '.gmail.com'
    bool_2 = module_0.is_email(str_2)
    str_3 = 'my name@gmail.com'
    bool_3 = module_0.is_email(str_3)
    str_4 = 'my.....name@gmail.com'
    bool_4 = module_0.is_email(str_4)
    str_5 = 'm'
    int_0 = 320
    var_0 = str_5 * int_0
    var_1 = var_0 + str_1
    bool_5 = module_0.is_email(var_1)
    str_6 = 'my.name'
    int_1 = 10
    var_2 = str_6 * int_1
    var_3 = var_2 + str_1
    bool_6 = module_0.is_email(var_3)
    str_7 = '"very.unusual.@.unusual.com"@gmail.com'
    bool_7 = module_0.is_email(str_7)

def test_case_42():
    str_0 = 'w'
    bool_0 = module_0.is_pangram(str_0)
    bool_1 = module_0.is_isogram(str_0)
    str_1 = '\t1l\x0b$8ouR|T\\m!}A'
    int_0 = module_0.words_count(str_1)
    bool_2 = module_0.is_ip(bool_1)
    bool_3 = module_0.is_palindrome(str_1)
    bool_4 = module_0.is_ip_v6(bool_3)
    str_2 = 'vj:I`]-g1EFDk1_:i"'
    bool_5 = module_0.contains_html(str_2)
    bool_6 = module_0.is_palindrome(str_0)
    bool_7 = module_0.is_slug(bool_1)

def test_case_43():
    var_0 = None
    bool_0 = module_0.is_credit_card(var_0)
    str_0 = '378282246310005'
    bool_1 = module_0.is_credit_card(var_0)
    str_1 = '6011111111111117'
    bool_2 = module_0.is_credit_card(str_1)
    bool_3 = module_0.is_credit_card(str_1)
    str_2 = '5105 1051 0510 5106'
    bool_4 = module_0.is_credit_card(str_2)
    bool_5 = module_0.is_credit_card(str_2)
    bool_6 = module_0.is_credit_card(bool_2)
    bool_7 = module_0.is_credit_card(bool_0, str_0)
    bool_8 = module_0.is_credit_card(bool_0)

def test_case_44():
    str_0 = '255.200.100.75'
    bool_0 = module_0.is_ip_v4(str_0)
    bool_1 = module_0.is_ip(bool_0)
    str_1 = 'nope'
    bool_2 = module_0.is_email(str_1)

def test_case_45():
    str_0 = '255.200.100.75'
    bool_0 = module_0.is_ip_v4(str_0)
    str_1 = 'nope'
    bool_1 = module_0.is_ip_v4(str_1)
    str_2 = '255.200.100.999'
    bool_2 = module_0.is_ip_v4(str_2)

def test_case_46():
    str_0 = 'd'
    i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
    bool_0 = module_0.is_json(i_s_b_n_checker_0)
    str_1 = '255.200.100.75'
    bool_1 = module_0.is_ip_v4(str_1)
    bool_2 = module_0.is_email(str_1)
    str_2 = '.c(h/8[r1x0\x0b $'
    bool_3 = module_0.is_email(str_2)
    str_3 = 'email@123.123.123.123'
    bool_4 = module_0.is_email(str_3)
    str_4 = '0f?WjFPlIvzL'
    bool_5 = module_0.is_isbn(str_4)

def test_case_47():
    str_0 = '[1, 2, 3]'
    str_1 = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz@bar.com'
    bool_0 = module_0.is_email(str_0)
    bool_1 = module_0.is_email(str_1)

def test_case_48():
    str_0 = 'user'
    bool_0 = module_0.is_email(str_0)
    str_1 = 'm111@example'
    bool_1 = module_0.is_email(str_1)
    str_2 = 'q@example.com'
    bool_2 = module_0.is_email(str_2)
    str_3 = 'a.b@example.com'
    bool_3 = module_0.is_email(str_3)
    str_4 = 'user.aa@example.com'
    bool_4 = module_0.is_email(str_4)
    str_5 = 'user.a.a.a@example.com'
    bool_5 = module_0.is_email(str_5)
    str_6 = 'user.1@example.com'
    bool_6 = module_0.is_email(str_6)
    str_7 = 'user.1.2@example.com'
    bool_7 = module_0.is_email(str_7)
    str_8 = 'user.1.2.3@example.com'
    bool_8 = module_0.is_email(str_8)
    str_9 = 'user.1..3@example.com'
    bool_9 = module_0.is_email(str_9)
    str_10 = 'user.1asdasd.3@example.com'
    bool_10 = module_0.is_email(str_10)

def test_case_49():
    str_0 = '255.200.100.75'
    bool_0 = module_0.is_ip(str_0)
    str_1 = '2001:db8:85a3:0000:0000:8a2e:370:7334'
    bool_1 = module_0.is_ip(str_1)
    str_2 = '1.2.3'
    bool_2 = module_0.is_ip(str_2)

def test_case_50():
    str_0 = '5.2.1.75'
    bool_0 = module_0.is_ip_v4(str_0)
    bool_1 = module_0.is_json(str_0)
    bool_2 = module_0.is_ip_v4(bool_1)
    bool_3 = module_0.is_full_string(bool_0)
    bool_4 = module_0.is_email(str_0)
    str_1 = '"emil@domain.comD'
    bool_5 = module_0.is_email(bool_1)
    dict_0 = {}
    bool_6 = module_0.is_json(dict_0)
    str_2 = '1s5FV@S*F!)/Y'
    bool_7 = module_0.is_email(str_1)
    bool_8 = module_0.is_email(str_2)
    bool_9 = module_0.is_isbn(str_2)
    bool_10 = module_0.is_email(str_0)
    str_3 = 'is_isbn_10'
    bool_11 = module_0.is_isbn_10(str_3)
    bool_12 = module_0.is_ip(bool_7)
    bool_13 = module_0.is_ip(bool_7)
    bool_14 = module_0.is_ip(bool_8)
    bool_15 = module_0.is_ip_v6(bool_12)
    bool_16 = module_0.is_json(str_0)
    bool_17 = module_0.is_json(str_0)
    bool_18 = module_0.is_ip_v4(bool_12)
    bool_19 = module_0.is_json(bool_2)

def test_case_51():
    str_0 = '{"name": "Peter"}'
    bool_0 = module_0.is_json(str_0)
    str_1 = '[1, 2, 3]'
    bool_1 = module_0.is_json(str_1)
    str_2 = '{nope}'
    bool_2 = module_0.is_json(str_2)
    str_3 = 'http://mysite.com'
    list_0 = [str_2]
    bool_3 = module_0.is_url(str_3, list_0)
    int_0 = 3
    bool_4 = module_0.is_url(int_0)
    bool_5 = module_0.is_url(str_3)

def test_case_52():
    str_0 = 'my.email@the-provider.com'
    bool_0 = module_0.is_email(str_0)
    str_1 = '@gmail.com'
    bool_1 = module_0.is_email(str_1)
    str_2 = '@gmail'
    bool_2 = module_0.is_email(str_2)
    str_3 = 'gmail@'
    bool_3 = module_0.is_email(str_3)
    str_4 = 'gmail@gmail'
    bool_4 = module_0.is_email(str_4)
    bool_5 = module_0.is_email(str_0)
    str_5 = 'my.email.@the-provider.com'
    bool_6 = module_0.is_email(str_5)