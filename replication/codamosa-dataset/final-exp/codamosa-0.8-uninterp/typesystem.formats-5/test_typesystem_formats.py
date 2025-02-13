# Automatically generated by Pynguin.
import typesystem.formats as module_0
import datetime as module_1

def test_case_0():
    date_time_format_0 = module_0.DateTimeFormat()

def test_case_1():
    bool_0 = None
    list_0 = []
    dict_0 = {}
    time_format_0 = module_0.TimeFormat()
    bool_1 = time_format_0.is_native_type(list_0)
    time_format_1 = module_0.TimeFormat(*list_0, **dict_0)
    bool_2 = time_format_1.is_native_type(bool_0)

def test_case_2():
    time_format_0 = module_0.TimeFormat()
    str_0 = '09:15'
    time_0 = time_format_0.validate(str_0)

def test_case_3():
    time_format_0 = module_0.TimeFormat()
    str_0 = '09:15:57'
    time_0 = time_format_0.validate(str_0)
    str_1 = '09:15'
    time_1 = time_format_0.validate(str_1)
    str_2 = '09:15:57.123456'
    time_2 = time_format_0.validate(str_2)
    str_3 = '09:15:57.1234'
    time_3 = time_format_0.validate(str_3)

def test_case_4():
    time_0 = module_1.time()
    time_format_0 = module_0.TimeFormat()
    str_0 = 'TimeFormat.serialize: '
    optional_0 = time_format_0.serialize(time_0)
    var_0 = str_0 + optional_0
    var_1 = print(var_0)

def test_case_5():
    date_time_format_0 = module_0.DateTimeFormat()
    str_0 = '2017-03-30T12:24:35Z'
    datetime_0 = date_time_format_0.validate(str_0)
    str_1 = '2017-03-30T12:24:35.123456Z'
    datetime_1 = date_time_format_0.validate(str_1)
    datetime_2 = date_time_format_0.validate(str_1)
    str_2 = '2017-03-30T12:24:35.123456-05:30'
    datetime_3 = date_time_format_0.validate(str_2)

def test_case_6():
    str_0 = '2020-08-18T10:34:56.123456Z'
    date_time_format_0 = module_0.DateTimeFormat()
    datetime_0 = date_time_format_0.validate(str_0)
    var_0 = print(datetime_0)

def test_case_7():
    date_time_format_0 = module_0.DateTimeFormat()
    str_0 = '2019-12-17T14:12:31Z'
    datetime_0 = date_time_format_0.validate(str_0)

def test_case_8():
    int_0 = 1
    date_time_format_0 = module_0.DateTimeFormat()
    str_0 = '2009-01-12T01:30:00+01:00'
    datetime_0 = date_time_format_0.validate(str_0)
    timedelta_0 = module_1.timedelta()

def test_case_9():
    str_0 = '2009-01-12T01:30:00Z'
    list_0 = []
    date_time_format_0 = module_0.DateTimeFormat(*list_0)
    datetime_0 = date_time_format_0.validate(str_0)
    optional_0 = date_time_format_0.serialize(datetime_0)

def test_case_10():
    date_time_format_0 = module_0.DateTimeFormat()
    str_0 = '2019-06-18T07:55:10'
    datetime_0 = date_time_format_0.validate(str_0)

def test_case_11():
    date_time_format_0 = module_0.DateTimeFormat()
    str_0 = '2019-11-22T10:14:37Z'
    datetime_0 = date_time_format_0.validate(str_0)
    str_1 = '2019-11-22T10:14:37+07'
    datetime_1 = date_time_format_0.validate(str_1)
    str_2 = '2019-11-22T10:14:37'
    datetime_2 = date_time_format_0.validate(str_2)