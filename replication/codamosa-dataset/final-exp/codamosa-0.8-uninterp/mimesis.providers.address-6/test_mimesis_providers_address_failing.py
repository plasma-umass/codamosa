# Automatically generated by Pynguin.
import mimesis.providers.address as module_0

def test_case_0():
    try:
        address_0 = module_0.Address()
        str_0 = address_0.calling_code()
        str_1 = address_0.region()
        str_2 = 'erroll'
        list_0 = [str_2, str_2, str_2]
        bytes_0 = b'w\x08U\x16\xe5\xa7'
        bool_0 = True
        list_1 = [list_0, str_2, bytes_0, bool_0]
        address_1 = module_0.Address(*list_1)
    except BaseException:
        pass

def test_case_1():
    try:
        address_0 = module_0.Address()
        str_0 = address_0.continent()
        str_1 = "vCVIp-<\n'"
        str_2 = address_0.country_code()
        str_3 = address_0.street_suffix()
        dict_0 = {str_1: str_1}
        str_4 = address_0.country_code()
        str_5 = address_0.postal_code()
        list_0 = []
        str_6 = address_0.province(*list_0)
        str_7 = address_0.street_name()
        address_1 = module_0.Address(**dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = ''
        str_1 = '\t@n "vsRAdN9aTBD$JB'
        str_2 = '+O<_&M&~y9g"ag'
        dict_0 = {str_0: str_0, str_0: str_0, str_1: str_0, str_2: str_1}
        address_0 = module_0.Address()
        str_3 = address_0.prefecture(**dict_0)
    except BaseException:
        pass