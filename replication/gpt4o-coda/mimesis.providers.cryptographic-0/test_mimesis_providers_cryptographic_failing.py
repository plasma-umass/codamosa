# Automatically generated by Pynguin.
import mimesis.providers.cryptographic as module_0

def test_case_0():
    try:
        optional_0 = None
        cryptographic_0 = module_0.Cryptographic()
        str_0 = cryptographic_0.hash(optional_0)
        str_1 = 't ( b5tm*1s Ig>*'
        dict_0 = {}
        cryptographic_1 = module_0.Cryptographic(**dict_0)
        cryptographic_2 = module_0.Cryptographic()
        var_0 = cryptographic_2.uuid()
        bool_0 = True
        var_1 = cryptographic_2.uuid(bool_0)
        cryptographic_3 = module_0.Cryptographic(**dict_0)
        var_2 = cryptographic_3.uuid()
        dict_1 = {str_1: str_1}
        var_3 = cryptographic_3.token_urlsafe()
        cryptographic_4 = module_0.Cryptographic(**dict_1)
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = []
        cryptographic_0 = module_0.Cryptographic(*list_0)
        var_0 = cryptographic_0.uuid()
        cryptographic_1 = module_0.Cryptographic()
        bytes_0 = cryptographic_1.token_bytes()
        int_0 = -1070
        var_1 = cryptographic_1.token_urlsafe()
        str_0 = cryptographic_1.token_hex(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        cryptographic_0 = module_0.Cryptographic()
        str_0 = cryptographic_0.token_hex()
        int_0 = 1075
        var_0 = cryptographic_0.token_urlsafe(int_0)
        str_1 = 'jn-\x0bl_Q?XQ{\\'
        int_1 = -329
        str_2 = cryptographic_0.mnemonic_phrase(int_1, str_0)
        dict_0 = {str_1: str_1, str_1: str_1}
        str_3 = cryptographic_0.hash()
        list_0 = [dict_0, str_1, dict_0, str_1]
        bytes_0 = cryptographic_0.token_bytes()
        set_0 = set()
        list_1 = [str_1, str_1, list_0, set_0]
        cryptographic_1 = module_0.Cryptographic(*list_1)
    except BaseException:
        pass