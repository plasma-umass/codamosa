# Automatically generated by Pynguin.
import pypara.exchange as module_0

def test_case_0():
    try:
        currency_0 = None
        date_0 = None
        f_x_rate_lookup_error_0 = module_0.FXRateLookupError(currency_0, currency_0, date_0)
        list_0 = None
        f_x_rate_0 = module_0.FXRate(*list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        iterable_0 = None
        str_0 = 'EwG,WyK2`)ae'
        str_1 = None
        str_2 = None
        dict_0 = {str_0: iterable_0, str_1: str_1, str_2: str_0}
        list_0 = [iterable_0, iterable_0, dict_0, dict_0]
        f_x_rate_0 = module_0.FXRate(*list_0)
        f_x_rate_1 = f_x_rate_0.__invert__()
    except BaseException:
        pass