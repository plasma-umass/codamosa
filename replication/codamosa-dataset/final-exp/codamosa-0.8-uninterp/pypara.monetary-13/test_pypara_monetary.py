# Automatically generated by Pynguin.
import pypara.monetary as module_0
import decimal as module_1
import pypara.currencies as module_2

def test_case_0():
    pass

def test_case_1():
    money_0 = module_0.Money()
    var_0 = None
    money_1 = money_0.__floordiv__(var_0)
    bool_0 = money_0.__le__(money_0)

def test_case_2():
    dict_0 = {}
    none_money_0 = module_0.NoneMoney()
    money_0 = none_money_0.floor_divide(dict_0)
    var_0 = money_0.__round__()

def test_case_3():
    none_money_0 = module_0.NoneMoney()
    money_0 = none_money_0.positive()
    money_1 = money_0.__add__(money_0)
    bool_0 = money_0.__lt__(money_0)
    money_2 = money_0.__sub__(money_0)
    bool_1 = money_2.__lt__(money_1)
    str_0 = "NO<IF9.#0+$:~h?'u["
    money_3 = money_2.__truediv__(str_0)

def test_case_4():
    int_0 = 29
    bytes_0 = b'\xbf\xc7\x81Z\x0c\xd9\x89\x99'
    none_money_0 = module_0.NoneMoney()
    money_0 = none_money_0.multiply(bytes_0)
    money_1 = money_0.scalar_subtract(int_0)

def test_case_5():
    bytes_0 = b'\xc3a\xa0\xdf|@&\x13A\x96\xec\x88O'
    none_price_0 = module_0.NonePrice()
    price_0 = none_price_0.round()
    price_1 = price_0.__truediv__(bytes_0)
    bool_0 = price_0.__lt__(price_1)

def test_case_6():
    bytes_0 = b'\xbf\xc7\x81Z\x0c\xd9\x89\x99'
    none_money_0 = module_0.NoneMoney()
    money_0 = none_money_0.multiply(bytes_0)
    bool_0 = money_0.lte(money_0)

def test_case_7():
    str_0 = '\npI]a-7vY?SjX-{wa'
    int_0 = 4
    list_0 = [str_0, int_0, str_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    bool_0 = some_money_0.is_equal(str_0)
    list_1 = []
    decimal_0 = module_1.Decimal(*list_1)
    money_0 = some_money_0.positive()
    date_0 = None
    money_1 = money_0.add(money_0)
    money_2 = money_1.with_dov(date_0)

def test_case_8():
    money_0 = module_0.Money()
    money_1 = money_0.__neg__()
    list_0 = []
    none_money_0 = module_0.NoneMoney(*list_0)

def test_case_9():
    str_0 = '\npI]a-7vY?SjX-{wa'
    str_1 = 'Kenyan Shilling'
    int_0 = 4
    currency_type_0 = None
    list_0 = [str_0, int_0, str_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    bool_0 = some_money_0.is_equal(str_0)
    str_2 = "kFBL`\t&NxL:_oF''"
    int_1 = -1156
    list_1 = []
    decimal_0 = module_1.Decimal(*list_1)
    currency_0 = module_2.Currency(str_0, str_2, int_1, currency_type_0, decimal_0, int_0)
    decimal_1 = currency_0.quantize(decimal_0)
    currency_1 = module_2.Currency(str_0, str_1, int_0, currency_type_0, decimal_1, int_1)
    money_0 = some_money_0.positive()
    none_price_0 = module_0.NonePrice()
    price_0 = none_price_0.negative()
    price_1 = price_0.__pos__()
    none_money_0 = module_0.NoneMoney()
    money_1 = none_money_0.with_ccy(currency_0)
    bool_1 = money_0.__gt__(money_1)
    money_2 = some_money_0.with_ccy(currency_1)

def test_case_10():
    price_0 = module_0.Price()
    none_price_0 = module_0.NonePrice()
    price_1 = none_price_0.add(price_0)
    price_2 = price_1.__abs__()

def test_case_11():
    str_0 = '\npIa-7vY?SjX-{a'
    int_0 = 4
    list_0 = [str_0, int_0, str_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.positive()
    bool_0 = some_money_0.gt(money_0)
    some_price_0 = module_0.SomePrice(*list_0)

def test_case_12():
    dict_0 = {}
    none_money_0 = module_0.NoneMoney()
    money_0 = none_money_0.floor_divide(dict_0)
    money_1 = money_0.round()
    var_0 = money_1.__round__()
    none_money_1 = module_0.NoneMoney()
    money_2 = money_0.__pos__()
    date_0 = None
    money_3 = money_2.__sub__(money_0)
    money_4 = money_0.with_dov(date_0)

def test_case_13():
    date_0 = None
    none_price_0 = module_0.NonePrice()
    price_0 = none_price_0.with_dov(date_0)
    none_price_1 = module_0.NonePrice()
    price_1 = none_price_1.round()
    price_2 = price_1.__sub__(price_0)

def test_case_14():
    int_0 = -24
    list_0 = [int_0, int_0, int_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    some_price_0 = module_0.SomePrice(*list_0)
    price_0 = some_price_0.abs()
    money_0 = some_money_0.abs()
    none_money_0 = module_0.NoneMoney()
    bool_0 = some_money_0.gte(money_0)
    price_1 = price_0.negative()
    money_1 = some_money_0.positive()
    price_2 = price_1.subtract(price_1)
    money_2 = some_money_0.positive()
    price_3 = price_0.__add__(price_2)
    bool_1 = some_money_0.gt(money_2)
    bool_2 = some_money_0.lt(money_2)
    float_0 = some_money_0.as_float()
    money_3 = some_money_0.add(money_2)
    price_4 = price_1.add(price_3)

def test_case_15():
    str_0 = '\npI]a-7vY?SjX-{wa'
    str_1 = 'Kenyan Shil7ing'
    int_0 = 4
    currency_type_0 = None
    list_0 = [str_0, int_0, str_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    bool_0 = some_money_0.is_equal(str_0)
    int_1 = -1175
    list_1 = []
    decimal_0 = module_1.Decimal(*list_1)
    currency_0 = module_2.Currency(str_0, str_1, int_1, currency_type_0, decimal_0, int_0)
    decimal_1 = currency_0.quantize(decimal_0)
    currency_1 = module_2.Currency(str_0, str_1, int_0, currency_type_0, decimal_1, int_1)
    money_0 = some_money_0.positive()
    none_price_0 = module_0.NonePrice()
    price_0 = none_price_0.with_ccy(currency_1)
    none_price_1 = module_0.NonePrice()
    price_1 = none_price_1.negative()
    str_2 = "4`Gb>']eb%;7"
    money_1 = money_0.divide(str_2)
    price_2 = price_0.__pos__()
    some_price_0 = module_0.SomePrice(*list_0)
    price_3 = some_price_0.add(price_2)

def test_case_16():
    dict_0 = {}
    none_money_0 = module_0.NoneMoney()
    money_0 = none_money_0.floor_divide(dict_0)
    money_1 = money_0.round()
    var_0 = money_1.__round__()
    none_money_1 = module_0.NoneMoney()
    bool_0 = money_0.__eq__(var_0)

def test_case_17():
    int_0 = -24
    list_0 = [int_0, int_0, int_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    some_price_0 = module_0.SomePrice(*list_0)
    price_0 = some_price_0.abs()
    money_0 = some_money_0.abs()
    price_1 = price_0.negative()
    price_2 = price_1.subtract(price_1)
    bool_0 = price_1.gt(price_1)

def test_case_18():
    str_0 = '\npIa-7\x0cvY?SjX-{a'
    int_0 = -18
    list_0 = [str_0, int_0, str_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.positive()
    bool_0 = some_money_0.gt(money_0)
    bool_1 = some_money_0.lt(money_0)
    some_price_0 = module_0.SomePrice(*list_0)
    money_1 = money_0.__add__(money_0)
    money_2 = money_1.subtract(money_1)

def test_case_19():
    str_0 = '\npI]a-7vY?SjX-{wa'
    str_1 = 'Kenyan Shilling'
    int_0 = 4
    currency_type_0 = None
    list_0 = [str_0, int_0, str_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    bool_0 = some_money_0.is_equal(str_0)
    str_2 = "kFBL`\t&NxL:_oF''"
    int_1 = -1175
    list_1 = []
    decimal_0 = module_1.Decimal(*list_1)
    currency_0 = module_2.Currency(str_0, str_2, int_1, currency_type_0, decimal_0, int_0)
    decimal_1 = currency_0.quantize(decimal_0)
    currency_1 = module_2.Currency(str_0, str_1, int_0, currency_type_0, decimal_1, int_1)
    money_0 = some_money_0.positive()
    none_price_0 = module_0.NonePrice()
    price_0 = none_price_0.negative()
    price_1 = price_0.__pos__()
    currency_type_1 = module_2.CurrencyType.ALTERNATIVE
    none_money_0 = module_0.NoneMoney()
    money_1 = none_money_0.multiply(currency_type_1)
    bool_1 = money_0.__gt__(money_1)
    money_2 = some_money_0.with_ccy(currency_1)

def test_case_20():
    str_0 = '\npIa-7\x0cvY?SjX-{a'
    int_0 = -18
    list_0 = [str_0, int_0, str_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.positive()
    bool_0 = some_money_0.gt(money_0)
    bool_1 = some_money_0.gt(money_0)
    bool_2 = some_money_0.lt(money_0)
    money_1 = some_money_0.add(money_0)
    some_price_0 = module_0.SomePrice(*list_0)
    money_2 = money_0.__add__(money_0)
    dict_0 = {}
    none_price_0 = module_0.NonePrice(**dict_0)
    price_0 = none_price_0.negative()
    price_1 = price_0.__pos__()
    some_price_1 = module_0.SomePrice(*list_0)
    price_2 = some_price_1.add(price_1)

def test_case_21():
    str_0 = '\npIa-7\x0cvY?SjX-{a'
    int_0 = -18
    list_0 = [str_0, int_0, str_0]
    some_price_0 = module_0.SomePrice(*list_0)
    price_0 = some_price_0.abs()
    price_1 = price_0.__floordiv__(int_0)
    price_2 = price_0.__add__(price_0)

def test_case_22():
    str_0 = 'Kenyan Shilling'
    int_0 = 4
    currency_type_0 = None
    list_0 = [str_0, int_0, str_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    bool_0 = some_money_0.is_equal(str_0)
    int_1 = -1175
    list_1 = []
    decimal_0 = module_1.Decimal(*list_1)
    currency_0 = module_2.Currency(str_0, str_0, int_1, currency_type_0, decimal_0, int_0)
    decimal_1 = currency_0.quantize(decimal_0)
    currency_1 = module_2.Currency(str_0, str_0, int_0, currency_type_0, decimal_1, int_1)
    money_0 = some_money_0.positive()
    some_money_1 = None
    list_2 = [list_0, some_money_1, list_1]
    none_price_0 = module_0.NonePrice()
    bool_1 = money_0.as_boolean()
    price_0 = none_price_0.divide(list_2)
    none_price_1 = module_0.NonePrice()
    price_1 = none_price_1.negative()
    str_1 = "4`Gb>']eb%;7"
    money_1 = money_0.divide(str_1)
    price_2 = price_0.__pos__()
    some_price_0 = module_0.SomePrice(*list_0)
    price_3 = some_price_0.add(price_2)

def test_case_23():
    int_0 = -24
    list_0 = [int_0, int_0, int_0]
    some_price_0 = module_0.SomePrice(*list_0)
    price_0 = some_price_0.abs()
    none_money_0 = module_0.NoneMoney()
    price_1 = price_0.negative()
    price_2 = price_1.subtract(price_1)
    price_3 = price_0.__add__(price_2)
    float_0 = price_3.__float__()

def test_case_24():
    int_0 = -24
    list_0 = [int_0, int_0, int_0]
    some_price_0 = module_0.SomePrice(*list_0)
    price_0 = some_price_0.abs()
    price_1 = price_0.negative()
    price_2 = price_1.subtract(price_1)
    price_3 = price_2.negative()
    currency_0 = None
    price_4 = some_price_0.with_ccy(currency_0)
    str_0 = None
    price_5 = price_3.__sub__(price_2)
    currency_type_0 = module_2.CurrencyType.ALTERNATIVE
    bool_0 = price_1.__lt__(price_0)
    decimal_0 = None
    int_1 = 12
    str_1 = 'iy={g'
    int_2 = 1718
    currency_1 = module_2.Currency(str_1, str_0, int_1, currency_type_0, decimal_0, int_2)

def test_case_25():
    str_0 = '\npIa-7\x0cvY?SjX-{a'
    int_0 = 4
    list_0 = [str_0, int_0, str_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.positive()
    bool_0 = some_money_0.gt(money_0)
    bool_1 = some_money_0.lt(money_0)
    some_price_0 = module_0.SomePrice(*list_0)
    price_0 = some_price_0.positive()

def test_case_26():
    str_0 = '\npIa-7\x0cvY?SjX-{a'
    int_0 = 4
    list_0 = [str_0, int_0, str_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.positive()
    bool_0 = some_money_0.gt(money_0)
    bool_1 = some_money_0.lt(money_0)
    bool_2 = some_money_0.gte(money_0)

def test_case_27():
    str_0 = '\npIa-7\x0cvY?SjX-{a'
    int_0 = -18
    list_0 = [str_0, int_0, str_0]
    some_price_0 = module_0.SomePrice(*list_0)
    price_0 = some_price_0.negative()
    bool_0 = price_0.__eq__(some_price_0)
    price_1 = some_price_0.positive()
    price_2 = price_0.subtract(price_1)
    bool_1 = False
    price_3 = some_price_0.floor_divide(bool_1)
    price_4 = price_2.positive()
    price_5 = price_4.__add__(price_4)
    some_price_1 = module_0.SomePrice(*list_0)
    str_1 = "[JcfRt`'-gOi"
    currency_type_0 = module_2.CurrencyType.CRYPTO
    dict_0 = {}
    decimal_0 = module_1.Decimal(**dict_0)
    currency_0 = module_2.Currency(str_0, str_1, int_0, currency_type_0, decimal_0, int_0)

def test_case_28():
    str_0 = '\npIa-7\x0cvY?SjX-{a'
    int_0 = -18
    list_0 = [str_0, int_0, str_0]
    none_price_0 = module_0.NonePrice()
    some_money_0 = module_0.SomeMoney(*list_0)
    some_price_0 = module_0.SomePrice(*list_0)
    none_price_1 = module_0.NonePrice()
    price_0 = none_price_1.negative()
    price_1 = price_0.__pos__()
    bool_0 = True
    price_2 = some_price_0.floor_divide(bool_0)
    price_3 = some_price_0.abs()
    money_0 = some_money_0.abs()
    price_4 = price_3.__add__(price_3)
    bool_1 = some_money_0.gt(money_0)
    bool_2 = some_money_0.gt(money_0)
    bool_3 = some_money_0.lt(money_0)
    money_1 = some_money_0.add(money_0)
    str_1 = '#.fB'
    str_2 = 'DbH{W`{'
    bool_4 = some_price_0.lte(price_0)
    money_2 = money_0.__add__(money_0)
    money_3 = money_1.subtract(money_0)
    int_1 = None
    currency_type_0 = module_2.CurrencyType.METAL
    decimal_0 = module_1.Decimal()
    int_2 = 486
    currency_0 = module_2.Currency(str_2, str_1, int_1, currency_type_0, decimal_0, int_2)

def test_case_29():
    str_0 = '\npIa-7\x0cvY?SjX-{a'
    int_0 = -24
    list_0 = [str_0, int_0, str_0]
    some_price_0 = module_0.SomePrice(*list_0)
    price_0 = some_price_0.abs()
    none_money_0 = module_0.NoneMoney()
    price_1 = price_0.subtract(price_0)
    price_2 = price_0.__add__(price_1)
    bool_0 = price_2.__le__(price_1)

def test_case_30():
    str_0 = '\npIa-\x0cvY?SjX-{a'
    int_0 = -18
    list_0 = [str_0, int_0, str_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    money_0 = some_money_0.positive()
    bool_0 = some_money_0.gt(money_0)
    bool_1 = some_money_0.lt(money_0)
    int_1 = money_0.__int__()
    money_1 = some_money_0.floor_divide(bool_1)
    money_2 = money_0.subtract(money_0)
    dict_0 = {}
    decimal_0 = module_1.Decimal(**dict_0)
    money_3 = money_1.negative()
    bool_2 = money_2.__le__(money_2)

def test_case_31():
    str_0 = '\npIa-7\x0cvY?SjX-{a'
    int_0 = -24
    list_0 = [int_0, int_0, int_0]
    some_price_0 = module_0.SomePrice(*list_0)
    price_0 = some_price_0.abs()
    none_money_0 = module_0.NoneMoney()
    price_1 = price_0.negative()
    price_2 = price_1.subtract(price_1)
    price_3 = price_0.__add__(price_2)
    bool_0 = price_3.__ge__(price_3)
    str_1 = None
    int_1 = 2665
    currency_type_0 = module_2.CurrencyType.ALTERNATIVE
    decimal_0 = None
    int_2 = 12
    currency_0 = module_2.Currency(str_0, str_1, int_1, currency_type_0, decimal_0, int_2)

def test_case_32():
    str_0 = ''
    int_0 = -18
    list_0 = [str_0, int_0, str_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    some_price_0 = module_0.SomePrice(*list_0)
    price_0 = some_price_0.round()
    bool_0 = price_0.__eq__(some_price_0)
    none_price_0 = module_0.NonePrice()
    price_1 = price_0.subtract(price_0)
    bool_1 = False
    price_2 = some_price_0.floor_divide(bool_1)
    price_3 = some_price_0.positive()
    price_4 = some_price_0.abs()
    bool_2 = price_4.__le__(price_3)
    money_0 = some_money_0.positive()
    price_5 = price_2.positive()
    price_6 = price_4.__add__(price_4)
    bool_3 = some_money_0.gt(money_0)
    bool_4 = price_4.__lt__(price_4)
    bool_5 = some_money_0.lt(money_0)
    int_1 = money_0.__int__()
    money_1 = money_0.__add__(money_0)
    money_2 = some_money_0.floor_divide(bool_5)
    money_3 = money_0.subtract(money_1)
    bool_6 = price_5.__gt__(price_5)
    bool_7 = price_3.gte(price_1)
    bool_8 = price_4.__le__(price_3)

def test_case_33():
    price_0 = module_0.Price()
    bool_0 = price_0.__bool__()

def test_case_34():
    price_0 = module_0.Price()
    price_1 = price_0.__sub__(price_0)

def test_case_35():
    price_0 = module_0.Price()
    bool_0 = price_0.gte(price_0)

def test_case_36():
    price_0 = module_0.Price()
    price_1 = price_0.__neg__()

def test_case_37():
    price_0 = module_0.Price()
    price_1 = price_0.__add__(price_0)

def test_case_38():
    price_0 = module_0.Price()
    bool_0 = True
    price_1 = price_0.__mul__(bool_0)

def test_case_39():
    price_0 = module_0.Price()
    float_0 = price_0.__float__()

def test_case_40():
    price_0 = module_0.Price()
    var_0 = None
    price_1 = price_0.__truediv__(var_0)

def test_case_41():
    price_0 = module_0.Price()
    bool_0 = price_0.lte(price_0)

def test_case_42():
    price_0 = module_0.Price()
    bool_0 = price_0.__gt__(price_0)

def test_case_43():
    price_0 = module_0.Price()
    bool_0 = price_0.__eq__(price_0)

def test_case_44():
    int_0 = -24
    list_0 = [int_0, int_0, int_0]
    some_money_0 = module_0.SomeMoney(*list_0)
    some_price_0 = module_0.SomePrice(*list_0)
    price_0 = some_price_0.abs()
    money_0 = some_money_0.abs()
    none_money_0 = module_0.NoneMoney()
    bool_0 = some_money_0.gte(money_0)
    price_1 = price_0.negative()
    money_1 = some_money_0.positive()
    price_2 = price_1.subtract(price_1)
    money_2 = some_money_0.positive()
    price_3 = price_0.__add__(price_2)
    bool_1 = some_money_0.gt(money_2)
    bool_2 = some_money_0.lt(money_2)
    float_0 = some_money_0.as_float()
    some_price_1 = module_0.SomePrice(*list_0)
    str_0 = 'Cabo Verde Escudo'
    price_4 = some_price_0.divide(str_0)

def test_case_45():
    price_0 = module_0.Price()
    int_0 = price_0.__int__()

def test_case_46():
    price_0 = module_0.Price()
    bool_0 = price_0.gt(price_0)