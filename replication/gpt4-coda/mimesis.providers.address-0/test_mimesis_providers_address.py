# Automatically generated by Pynguin.
import mimesis.providers.address as module_0

def test_case_0():
    pass

def test_case_1():
    address_0 = module_0.Address()
    var_0 = address_0.longitude()

def test_case_2():
    bool_0 = True
    list_0 = []
    address_0 = module_0.Address(*list_0)
    dict_0 = address_0.coordinates(bool_0)

def test_case_3():
    bool_0 = True
    address_0 = module_0.Address()
    var_0 = address_0.latitude(bool_0)

def test_case_4():
    address_0 = module_0.Address()
    str_0 = address_0.address()

def test_case_5():
    bool_0 = True
    address_0 = module_0.Address()
    str_0 = address_0.state(bool_0)

def test_case_6():
    address_0 = module_0.Address()
    dict_0 = {}
    address_1 = module_0.Address()
    str_0 = address_0.calling_code()
    str_1 = address_1.calling_code()
    str_2 = address_1.country_code()
    address_2 = module_0.Address(**dict_0)
    str_3 = address_2.street_name()
    str_4 = address_2.zip_code()
    bool_0 = True
    var_0 = address_0.longitude(bool_0)
    str_5 = address_1.province()
    str_6 = address_0.province()
    str_7 = address_1.address()
    str_8 = address_1.street_number()

def test_case_7():
    dict_0 = {}
    address_0 = module_0.Address(**dict_0)
    dict_1 = address_0.coordinates()
    var_0 = address_0.latitude()
    str_0 = address_0.country_code()
    str_1 = address_0.address()
    str_2 = address_0.street_name()
    str_3 = address_0.federal_subject(**dict_0)

def test_case_8():
    address_0 = module_0.Address()
    str_0 = address_0.zip_code()
    dict_0 = {}
    address_1 = module_0.Address()
    str_1 = address_1.calling_code()
    address_2 = module_0.Address()
    str_2 = address_2.prefecture(**dict_0)
    address_3 = module_0.Address(**dict_0)
    str_3 = address_3.city()

def test_case_9():
    address_0 = module_0.Address()
    str_0 = address_0.postal_code()
    list_0 = []
    address_1 = module_0.Address(*list_0)
    var_0 = address_1.latitude()
    str_1 = address_1.state()
    var_1 = address_1.longitude()

def test_case_10():
    address_0 = module_0.Address()
    str_0 = address_0.state()
    str_1 = address_0.zip_code()
    address_1 = module_0.Address()
    str_2 = address_0.postal_code()
    str_3 = address_1.address()
    str_4 = address_1.calling_code()

def test_case_11():
    address_0 = module_0.Address()
    str_0 = address_0.country_code()

def test_case_12():
    address_0 = module_0.Address()
    str_0 = address_0.address()
    str_1 = address_0.prefecture()
    str_2 = address_0.country()
    bool_0 = True
    str_3 = address_0.city()
    str_4 = address_0.postal_code()
    str_5 = address_0.continent(bool_0)
    dict_0 = address_0.coordinates()

def test_case_13():
    address_0 = module_0.Address()
    str_0 = address_0.city()

def test_case_14():
    bool_0 = True
    address_0 = module_0.Address()
    var_0 = address_0.latitude(bool_0)

def test_case_15():
    bool_0 = True
    list_0 = []
    address_0 = module_0.Address(*list_0)
    dict_0 = address_0.coordinates(bool_0)

def test_case_16():
    address_0 = module_0.Address()
    str_0 = address_0.address()
    str_1 = address_0.prefecture()
    str_2 = address_0.country()
    bool_0 = False
    str_3 = address_0.city()
    str_4 = address_0.postal_code()
    str_5 = address_0.continent(bool_0)
    dict_0 = address_0.coordinates()