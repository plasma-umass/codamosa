# Automatically generated by Pynguin.
import pypara.monetary as module_0
import pypara.currencies as module_1
import decimal as module_2

def test_case_0():
    pass

def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.abs()
    money_1 = money_0.add(money_0)
    none_money_0 = module_0.NoneMoney()
    money_2 = none_money_0.abs()
    money_3 = money_2.positive()

def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    list_1 = [bool_0, bool_0, list_0]
    some_price_0 = module_0.SomePrice(*list_1)
    price_0 = some_price_0.round()
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.abs()
    bool_1 = some_money_0.gt(money_0)
    bool_2 = money_0.__le__(money_0)
    money_1 = money_0.__abs__()
    money_2 = money_0.add(money_1)
    dict_0 = {}
    none_price_0 = module_0.NonePrice(**dict_0)
    price_1 = price_0.__pos__()
    price_2 = none_price_0.add(price_0)

def test_case_3():
    var_0 = None
    none_price_0 = module_0.NonePrice()
    price_0 = none_price_0.multiply(var_0)

def test_case_4():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.abs()
    money_1 = money_0.add(money_0)
    var_0 = None
    none_money_0 = module_0.NoneMoney()
    money_2 = none_money_0.divide(var_0)

def test_case_5():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.abs()
    bool_1 = some_money_0.gt(money_0)
    money_1 = money_0.__abs__()
    money_2 = money_0.add(money_1)
    dict_0 = {}
    none_price_0 = module_0.NonePrice(**dict_0)
    price_0 = none_price_0.multiply(dict_0)
    price_1 = price_0.abs()

def test_case_6():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    none_price_0 = module_0.NonePrice()
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.abs()
    money_1 = money_0.__abs__()
    bool_1 = none_price_0.as_boolean()
    money_2 = money_0.__sub__(money_0)

def test_case_7():
    date_0 = None
    dict_0 = {}
    price_0 = module_0.Price(**dict_0)
    none_price_0 = module_0.NonePrice()
    price_1 = price_0.with_dov(date_0)
    price_2 = none_price_0.positive()

def test_case_8():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    list_1 = [bool_0, bool_0, list_0]
    some_price_0 = module_0.SomePrice(*list_1)
    price_0 = some_price_0.round()
    none_price_0 = module_0.NonePrice()
    bool_1 = none_price_0.gt(price_0)
    some_money_0 = module_0.SomeMoney(*list_0)
    none_money_0 = module_0.NoneMoney()
    money_0 = none_money_0.abs()
    bool_2 = some_money_0.gt(money_0)
    money_1 = money_0.add(money_0)
    money_2 = money_0.positive()
    money_3 = none_money_0.abs()

def test_case_9():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.abs()
    money_1 = money_0.add(money_0)

def test_case_10():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.negative()
    money_1 = money_0.add(money_0)

def test_case_11():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.positive()
    money_1 = money_0.add(money_0)

def test_case_12():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.abs()
    bool_1 = some_money_0.gt(money_0)
    money_1 = money_0.add(money_0)
    money_2 = money_1.positive()

def test_case_13():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    list_1 = [bool_0, bool_0, list_0]
    some_price_0 = module_0.SomePrice(*list_1)
    price_0 = some_price_0.round()
    none_price_0 = module_0.NonePrice()
    bool_1 = none_price_0.gt(price_0)
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.abs()
    bool_2 = some_money_0.gt(money_0)
    price_1 = price_0.abs()

def test_case_14():
    str_0 = ')IuE<Jio}!wo:\t;'
    int_0 = -2406
    currency_type_0 = module_1.CurrencyType.METAL
    list_0 = []
    decimal_0 = module_2.Decimal(*list_0)
    currency_0 = module_1.Currency(str_0, str_0, int_0, currency_type_0, decimal_0, int_0)
    none_money_0 = module_0.NoneMoney()
    money_0 = none_money_0.with_ccy(currency_0)
    money_1 = money_0.negative()
    none_money_1 = module_0.NoneMoney()
    bool_0 = none_money_1.gte(money_1)
    bool_1 = True
    list_1 = [bool_1, bool_1, bool_1]
    some_money_0 = module_0.SomeMoney(*list_1)
    money_2 = some_money_0.positive()
    bool_2 = some_money_0.gt(money_2)
    money_3 = money_2.__abs__()
    money_4 = money_2.add(money_3)
    money_5 = money_4.positive()

def test_case_15():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    some_price_0 = module_0.SomePrice(*list_0)
    price_0 = some_price_0.round()
    bool_1 = some_price_0.lt(price_0)
    bool_2 = price_0.__le__(price_0)
    price_1 = some_price_0.subtract(price_0)
    price_2 = some_price_0.add(price_1)
    bool_3 = price_1.gte(price_2)

def test_case_16():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.abs()
    bool_1 = some_money_0.gt(money_0)
    money_1 = money_0.subtract(money_0)
    money_2 = money_1.positive()

def test_case_17():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    some_price_0 = module_0.SomePrice(*list_0)
    price_0 = some_price_0.round()
    bool_1 = price_0.__bool__()
    price_1 = some_price_0.add(price_0)
    price_2 = some_price_0.subtract(price_1)
    bool_2 = price_2.__gt__(price_2)
    monetary_operation_exception_0 = module_0.MonetaryOperationException()

def test_case_18():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    list_1 = [bool_0, bool_0, list_0]
    some_price_0 = module_0.SomePrice(*list_1)
    price_0 = some_price_0.round()
    none_price_0 = module_0.NonePrice()
    bool_1 = none_price_0.gt(price_0)
    some_money_0 = module_0.SomeMoney(*list_0)
    bool_2 = none_price_0.lte(price_0)
    money_0 = some_money_0.abs()
    bool_3 = some_money_0.gt(money_0)
    money_1 = money_0.__abs__()
    money_2 = money_0.add(money_1)
    bool_4 = none_price_0.as_boolean()
    bool_5 = price_0.__bool__()
    decimal_0 = module_2.Decimal()
    money_3 = money_2.__sub__(money_2)

def test_case_19():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    list_1 = [bool_0, bool_0, list_0]
    some_price_0 = module_0.SomePrice(*list_1)
    price_0 = some_price_0.negative()
    none_price_0 = module_0.NonePrice()
    bool_1 = none_price_0.gt(price_0)
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.abs()
    bool_2 = some_money_0.gt(money_0)
    money_1 = money_0.__abs__()
    money_2 = money_0.add(money_1)
    dict_0 = {}
    none_price_1 = module_0.NonePrice(**dict_0)
    price_1 = price_0.__pos__()
    price_2 = price_1.abs()

def test_case_20():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.abs()
    bool_1 = some_money_0.is_equal(list_0)
    money_1 = money_0.add(money_0)

def test_case_21():
    str_0 = '\x0c/{*scR"fA"'
    int_0 = 0
    currency_type_0 = module_1.CurrencyType.MONEY
    decimal_0 = module_2.Decimal()
    str_1 = '\n        Returns same monetary value if *defined*, itself otherwise.\n        '
    int_1 = 1630
    currency_0 = module_1.Currency(str_1, str_0, int_1, currency_type_0, decimal_0, int_0)
    none_price_0 = module_0.NonePrice()
    price_0 = none_price_0.round()
    price_1 = price_0.with_ccy(currency_0)
    bool_0 = price_1.__bool__()
    currency_type_1 = module_1.CurrencyType.METAL
    decimal_1 = module_2.Decimal()
    currency_1 = module_1.Currency(str_0, str_0, int_0, currency_type_1, decimal_1, int_1)
    str_2 = 'kR)kL4D(LBK{7c'
    int_2 = -1020
    int_3 = -929
    currency_2 = module_1.Currency(str_2, str_2, int_2, currency_type_0, decimal_1, int_3)
    incompatible_currency_error_0 = module_0.IncompatibleCurrencyError(currency_1, currency_2, str_2)

def test_case_22():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    none_price_0 = module_0.NonePrice()
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.abs()
    bool_1 = some_money_0.gt(money_0)
    bool_2 = money_0.__lt__(money_0)
    money_1 = money_0.add(money_0)

def test_case_23():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    none_price_0 = module_0.NonePrice()
    int_0 = 2
    price_0 = none_price_0.round(int_0)
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.abs()
    bool_1 = some_money_0.gt(money_0)
    bool_2 = money_0.__lt__(money_0)
    money_1 = money_0.add(money_0)

def test_case_24():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    list_1 = [bool_0, bool_0, list_0]
    some_price_0 = module_0.SomePrice(*list_1)
    price_0 = some_price_0.round()
    none_price_0 = module_0.NonePrice()
    bool_1 = none_price_0.gt(price_0)
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.abs()
    bool_2 = some_money_0.gt(money_0)
    bool_3 = money_0.__lt__(money_0)
    bool_4 = price_0.__le__(price_0)
    money_1 = some_money_0.abs()
    money_2 = money_0.add(money_1)
    decimal_0 = module_2.Decimal()
    str_0 = None
    int_0 = -2996
    int_1 = 1
    currency_type_0 = module_1.CurrencyType.METAL
    int_2 = 365
    currency_0 = module_1.Currency(str_0, str_0, int_1, currency_type_0, decimal_0, int_2)
    money_3 = money_0.__sub__(money_2)
    str_1 = 'e3kV]B`<Fyes1:@,5P'
    int_3 = 1891
    currency_1 = module_1.Currency(str_0, str_1, int_0, currency_type_0, decimal_0, int_3)
    none_money_0 = module_0.NoneMoney()
    money_4 = none_money_0.with_ccy(currency_0)
    money_5 = money_2.add(money_4)
    money_6 = money_3.__sub__(money_0)

def test_case_25():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    some_price_0 = module_0.SomePrice(*list_0)
    price_0 = some_price_0.round()
    none_price_0 = module_0.NonePrice()
    bool_1 = none_price_0.gt(price_0)
    bool_2 = price_0.__bool__()
    price_1 = some_price_0.add(price_0)
    bool_3 = some_price_0.is_equal(none_price_0)
    price_2 = some_price_0.subtract(price_1)
    bool_4 = price_2.__gt__(price_2)
    monetary_operation_exception_0 = module_0.MonetaryOperationException()

def test_case_26():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    some_price_0 = module_0.SomePrice(*list_0)
    price_0 = some_price_0.round()
    bool_1 = some_price_0.lt(price_0)
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.abs()
    bool_2 = some_money_0.gt(money_0)
    bool_3 = money_0.__lt__(money_0)
    bool_4 = price_0.__le__(price_0)
    money_1 = money_0.add(money_0)
    bool_5 = money_1.__lt__(money_1)
    bool_6 = price_0.__le__(price_0)
    money_2 = money_0.add(money_0)
    bool_7 = money_2.__eq__(money_1)
    decimal_0 = module_2.Decimal()
    price_1 = price_0.with_qty(decimal_0)
    price_2 = price_1.abs()
    price_3 = some_price_0.add(price_2)
    bool_8 = price_0.gte(price_0)
    some_money_1 = module_0.SomeMoney(*list_0)
    bool_9 = some_money_1.gt(money_0)
    money_3 = money_0.add(money_1)
    money_4 = money_2.positive()

def test_case_27():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    list_1 = [list_0, bool_0, bool_0]
    some_price_0 = module_0.SomePrice(*list_1)
    price_0 = some_price_0.round()
    none_price_0 = module_0.NonePrice()
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.abs()
    bool_1 = some_money_0.gt(money_0)
    bool_2 = money_0.__lt__(money_0)
    bool_3 = price_0.__le__(price_0)
    money_1 = some_money_0.abs()
    money_2 = money_0.add(money_1)
    bool_4 = money_2.is_equal(money_2)
    int_0 = -2980
    bool_5 = money_2.__eq__(some_price_0)
    price_1 = some_price_0.add(price_0)
    currency_type_0 = module_1.CurrencyType.METAL
    str_0 = 'XR'
    int_1 = -2121
    decimal_0 = None
    currency_0 = module_1.Currency(str_0, str_0, int_1, currency_type_0, decimal_0, int_0)
    bool_6 = money_2.__eq__(int_1)
    money_3 = money_2.__sub__(money_0)
    bool_7 = price_0.__bool__()
    price_2 = price_0.abs()
    price_3 = none_price_0.negative()
    price_4 = some_price_0.add(price_3)
    price_5 = some_price_0.add(price_2)

def test_case_28():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    some_price_0 = module_0.SomePrice(*list_0)
    price_0 = some_price_0.round()
    bool_1 = some_price_0.lt(price_0)
    none_price_0 = module_0.NonePrice()
    int_0 = 7
    price_1 = none_price_0.round(int_0)
    some_money_0 = module_0.SomeMoney(*list_0)
    bool_2 = price_0.gt(price_0)
    bool_3 = price_0.__le__(price_0)
    bool_4 = price_1.__bool__()
    date_0 = None
    price_2 = some_price_0.with_dov(date_0)
    price_3 = some_price_0.negative()
    price_4 = some_price_0.add(price_3)
    price_5 = some_price_0.add(price_3)

def test_case_29():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    some_price_0 = module_0.SomePrice(*list_0)
    price_0 = module_0.Price()
    price_1 = price_0.__pos__()
    price_2 = some_price_0.round()
    bool_1 = some_price_0.lt(price_2)
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.abs()
    bool_2 = some_money_0.gt(money_0)
    bool_3 = money_0.__lt__(money_0)
    bool_4 = price_2.__le__(price_2)
    money_1 = money_0.add(money_0)
    str_0 = None
    bool_5 = money_1.__eq__(some_price_0)
    price_3 = price_2.abs()
    price_4 = some_price_0.add(price_3)
    bool_6 = price_3.gte(price_4)
    bool_7 = price_3.gt(price_4)
    currency_type_0 = module_1.CurrencyType.METAL
    int_0 = -2832
    bool_8 = money_1.__ge__(money_1)
    price_5 = price_3.__sub__(price_3)
    decimal_0 = None
    str_1 = '@b1f_wJBH+$>*X)#z'
    int_1 = -190
    currency_0 = module_1.Currency(str_1, str_0, int_0, currency_type_0, decimal_0, int_1)
    money_2 = money_1.__sub__(money_1)
    money_3 = some_money_0.positive()
    var_0 = price_4.__round__()
    bool_9 = some_money_0.lte(money_2)
    bool_10 = some_money_0.lt(money_1)
    monetary_operation_exception_0 = module_0.MonetaryOperationException()
    price_6 = price_0.with_ccy(currency_0)

def test_case_30():
    price_0 = module_0.Price()
    str_0 = None
    currency_type_0 = module_1.CurrencyType.METAL
    money_0 = module_0.Money()
    bool_0 = money_0.__bool__()
    int_0 = -2832
    decimal_0 = None
    str_1 = 'Lilangeni'
    int_1 = -190
    currency_0 = module_1.Currency(str_1, str_0, int_0, currency_type_0, decimal_0, int_1)
    monetary_operation_exception_0 = module_0.MonetaryOperationException()

def test_case_31():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    some_price_0 = module_0.SomePrice(*list_0)
    bool_1 = True
    price_0 = module_0.Price()
    price_1 = price_0.__mul__(bool_1)
    price_2 = some_price_0.round()
    bool_2 = some_price_0.lt(price_2)
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.abs()
    bool_3 = some_money_0.gt(money_0)
    bool_4 = money_0.__lt__(money_0)
    bool_5 = price_2.__le__(price_2)
    bool_6 = price_0.__eq__(bool_5)
    money_1 = money_0.add(money_0)
    bool_7 = money_1.__eq__(some_price_0)
    price_3 = price_2.abs()
    price_4 = some_price_0.add(price_3)
    bool_8 = price_3.gte(price_4)
    bool_9 = price_3.gt(price_4)
    bool_10 = money_1.__ge__(money_1)
    price_5 = price_3.__sub__(price_3)
    int_0 = price_5.__int__()
    money_2 = money_1.__sub__(money_1)
    money_3 = some_money_0.positive()
    var_0 = price_4.__round__()
    bool_11 = some_money_0.lte(money_2)
    bool_12 = some_money_0.lt(money_1)
    monetary_operation_exception_0 = module_0.MonetaryOperationException()