# Automatically generated by Pynguin.
import mimesis.builtins.ru as module_0
import builtins as module_1

def test_case_0():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    str_0 = russia_spec_provider_0.series_and_number()

def test_case_1():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    str_0 = russia_spec_provider_0.generate_sentence()
    str_1 = russia_spec_provider_0.passport_series()

def test_case_2():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    str_0 = russia_spec_provider_0.generate_sentence()
    str_1 = russia_spec_provider_0.patronymic()
    float_0 = 3668.4481
    str_2 = russia_spec_provider_0.passport_series(float_0)
    str_3 = russia_spec_provider_0.series_and_number()
    russia_spec_provider_1 = module_0.RussiaSpecProvider()
    str_4 = russia_spec_provider_1.bic()
    str_5 = russia_spec_provider_0.snils()
    str_6 = russia_spec_provider_1.passport_series()

def test_case_3():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    str_0 = russia_spec_provider_0.snils()

def test_case_4():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    str_0 = russia_spec_provider_0.snils()
    str_1 = russia_spec_provider_0.snils()
    russia_spec_provider_1 = module_0.RussiaSpecProvider()
    str_2 = russia_spec_provider_1.snils()
    int_0 = russia_spec_provider_0.passport_number()
    str_3 = russia_spec_provider_0.patronymic()
    str_4 = russia_spec_provider_0.snils()
    russia_spec_provider_2 = module_0.RussiaSpecProvider()
    str_5 = russia_spec_provider_1.inn()
    str_6 = russia_spec_provider_0.kpp()
    str_7 = russia_spec_provider_2.passport_series()
    str_8 = russia_spec_provider_2.kpp()
    str_9 = russia_spec_provider_1.snils()
    str_10 = russia_spec_provider_2.bic()
    str_11 = russia_spec_provider_2.snils()
    str_12 = russia_spec_provider_2.snils()

def test_case_5():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    bytes_0 = b'\xb9k[\xc4\xcc\xc9\x99\xad8\x00\xe7D'
    russia_spec_provider_1 = module_0.RussiaSpecProvider(bytes_0)
    russia_spec_provider_2 = module_0.RussiaSpecProvider()
    str_0 = russia_spec_provider_1.snils()
    str_1 = russia_spec_provider_2.kpp()
    int_0 = -3288
    str_2 = russia_spec_provider_2.passport_series(int_0)
    str_3 = russia_spec_provider_1.snils()
    str_4 = russia_spec_provider_1.bic()
    str_5 = russia_spec_provider_1.snils()
    str_6 = russia_spec_provider_0.snils()

def test_case_6():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    str_0 = russia_spec_provider_0.snils()
    bytearray_0 = module_1.bytearray()
    russia_spec_provider_1 = module_0.RussiaSpecProvider(bytearray_0)
    str_1 = russia_spec_provider_1.snils()
    str_2 = russia_spec_provider_1.inn()

def test_case_7():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    str_0 = russia_spec_provider_0.ogrn()

def test_case_8():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    russia_spec_provider_1 = module_0.RussiaSpecProvider()
    str_0 = russia_spec_provider_1.bic()

def test_case_9():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    str_0 = russia_spec_provider_0.series_and_number()
    russia_spec_provider_1 = module_0.RussiaSpecProvider()
    str_1 = russia_spec_provider_1.kpp()

def test_case_10():
    russia_spec_provider_0 = module_0.RussiaSpecProvider()
    str_0 = russia_spec_provider_0.snils()
    str_1 = russia_spec_provider_0.snils()
    str_2 = russia_spec_provider_0.passport_series(russia_spec_provider_0)