# Automatically generated by Pynguin.
import mimesis.providers.address as module_0

def test_case_0():
    address_0 = module_0.Address()

def test_case_1():
    address_0 = module_0.Address()
    str_0 = address_0.street_number()

def test_case_2():
    address_0 = module_0.Address()
    str_0 = address_0.address()

def test_case_3():
    address_0 = module_0.Address()
    str_0 = address_0.federal_subject()
    dict_0 = address_0.coordinates()
    address_1 = module_0.Address()
    str_1 = address_1.province()
    str_2 = address_1.street_number()

def test_case_4():
    address_0 = module_0.Address()
    var_0 = address_0.latitude()
    list_0 = [address_0]
    var_1 = address_0.longitude()
    dict_0 = {}
    address_1 = module_0.Address()
    str_0 = address_1.region(*list_0, **dict_0)
    str_1 = address_0.city()
    str_2 = address_0.calling_code()

def test_case_5():
    address_0 = module_0.Address()
    str_0 = address_0.country()
    str_1 = address_0.postal_code()
    address_1 = module_0.Address()
    str_2 = address_0.postal_code()
    str_3 = address_0.postal_code()
    str_4 = address_0.prefecture()
    var_0 = address_0.latitude()
    str_5 = address_0.region()

def test_case_6():
    address_0 = module_0.Address()
    var_0 = address_0.latitude()
    str_0 = address_0.country_code()
    bool_0 = True
    dict_0 = address_0.coordinates(bool_0)
    var_1 = address_0.longitude()
    str_1 = address_0.city()

def test_case_7():
    bool_0 = True
    address_0 = module_0.Address()
    var_0 = address_0.latitude(bool_0)

def test_case_8():
    address_0 = module_0.Address()
    var_0 = address_0.latitude()
    str_0 = address_0.country_code()
    str_1 = address_0.region()
    bool_0 = True
    dict_0 = address_0.coordinates(bool_0)
    var_1 = address_0.longitude()
    address_1 = module_0.Address()
    str_2 = address_1.state()
    str_3 = address_0.calling_code()
    var_2 = address_1.longitude()
    str_4 = address_1.continent()
    address_2 = module_0.Address()
    str_5 = address_2.postal_code()

def test_case_9():
    bool_0 = True
    address_0 = module_0.Address()
    var_0 = address_0.latitude(bool_0)

def test_case_10():
    bool_0 = True
    address_0 = module_0.Address()
    str_0 = address_0.calling_code()
    str_1 = address_0.street_number()
    str_2 = address_0.postal_code()
    address_1 = module_0.Address()
    str_3 = address_0.continent()
    str_4 = address_0.country_code()
    str_5 = address_0.postal_code()
    str_6 = address_1.city()
    str_7 = address_0.state()
    str_8 = address_0.region()
    bool_1 = True
    str_9 = address_1.region()
    var_0 = address_0.longitude()
    str_10 = address_0.street_number()
    str_11 = address_0.address()
    str_12 = address_0.address()
    address_2 = module_0.Address()
    var_1 = address_2.latitude(bool_1)
    str_13 = address_0.state()
    str_14 = address_2.calling_code()
    var_2 = address_0.longitude(bool_1)
    str_15 = address_0.continent(bool_0)
    str_16 = address_0.postal_code()

def test_case_11():
    address_0 = module_0.Address()
    var_0 = address_0.latitude()
    str_0 = address_0.country_code()
    str_1 = address_0.region()
    bool_0 = True
    dict_0 = address_0.coordinates(bool_0)
    list_0 = [address_0]
    var_1 = address_0.longitude()
    dict_1 = {}
    str_2 = address_0.region(*list_0, **dict_1)
    str_3 = address_0.city()