# Automatically generated by Pynguin.
import youtube_dl.aes as module_0
import youtube_dl.utils as module_1

def test_case_0():
    str_0 = 'Md5Be5r5rKj5p3qe3qH26qH2'
    int_0 = 16
    var_0 = module_0.aes_decrypt_text(str_0, str_0, int_0)

def test_case_1():
    str_0 = 'YELLO SUBMARINE'
    var_0 = module_1.bytes_to_intlist(str_0)
    var_1 = module_0.key_expansion(var_0)

def test_case_2():
    bytes_0 = b'"g6\x13rk\xe2\xead\xb2\x01'
    var_0 = module_0.sub_bytes_inv(bytes_0)

def test_case_3():
    bytes_0 = b'\xc56\x8d<o\x07\xef\x14^\xab\x0b\x7f\x19kA\x90\xde'
    var_0 = module_0.mix_columns(bytes_0)

def test_case_4():
    float_0 = -669.2
    bool_0 = False
    var_0 = module_0.rijndael_mul(float_0, bool_0)

def test_case_5():
    str_0 = '9XHyiF/Nk/j45BupwZMVaIx/nh6UHKe6+AOMyX9/QkM='
    str_1 = 'Md5Be5r5rKj5p3qe3qH26qH2'
    int_0 = 16
    var_0 = module_0.aes_decrypt_text(str_0, str_1, int_0)

def test_case_6():
    tuple_0 = ()
    var_0 = module_0.inc(tuple_0)

def test_case_7():
    str_0 = 'smKLHV7QA9gYiIeBkf0+qA=='
    var_0 = module_1.bytes_to_intlist(str_0)
    var_1 = module_0.key_expansion(var_0)
    var_2 = module_0.aes_decrypt(var_0, var_1)

def test_case_8():
    bytes_0 = b'1234567890123456'
    var_0 = module_1.bytes_to_intlist(bytes_0)
    var_1 = module_1.bytes_to_intlist(bytes_0)
    bytes_1 = b'\x00decrypted_data\x00'
    var_2 = module_1.bytes_to_intlist(bytes_1)
    bytes_2 = b'\x00encrypted_data\x00'
    var_3 = module_1.bytes_to_intlist(bytes_2)
    var_4 = module_0.aes_cbc_encrypt(var_2, var_0, var_1)
    var_5 = module_0.aes_cbc_decrypt(var_3, var_0, var_1)

def test_case_9():
    int_0 = 256
    int_1 = [int_0, int_0, int_0]
    var_0 = module_0.inc(int_1)

def test_case_10():
    int_0 = 255
    int_1 = [int_0, int_0, int_0]
    var_0 = module_0.inc(int_1)

def test_case_11():
    str_0 = '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'
    var_0 = module_1.bytes_to_intlist(str_0)
    str_1 = 'Basic CBC mode encryption needs padding.'
    var_1 = module_1.bytes_to_intlist(str_1)
    int_0 = 17
    int_1 = [int_0]
    int_2 = 15
    var_2 = int_1 * int_2
    var_3 = var_1 + var_2
    str_2 = '140b41b22a29beb4061bda66b6747e14'
    var_4 = module_1.bytes_to_intlist(str_2)
    str_3 = '4ca00ff4c898d61e1edbf1800618fb28'
    var_5 = module_1.bytes_to_intlist(str_3)
    var_6 = module_0.aes_cbc_decrypt(var_0, var_4, var_5)