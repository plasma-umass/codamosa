# Automatically generated by Pynguin.
import pypara.currencies as module_0
import pypara.exchange as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = '`GoI5V2rJ-GLBx'
    str_1 = 'qpT'
    int_0 = -851
    currency_type_0 = module_0.CurrencyType.CRYPTO
    decimal_0 = None
    currency_0 = module_0.Currency(str_0, str_1, int_0, currency_type_0, decimal_0, int_0)
    date_0 = None
    f_x_rate_lookup_error_0 = module_1.FXRateLookupError(currency_0, currency_0, date_0)