# Automatically generated by Pynguin.
import flutes.iterator as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'I'
    lazy_list_0 = module_0.LazyList(str_0)
    var_0 = lazy_list_0.__iter__()

def test_case_2():
    int_0 = 46
    int_1 = 3
    int_2 = [int_0, int_0, int_1]
    lazy_list_0 = module_0.LazyList(int_2)
    var_0 = list(lazy_list_0)

def test_case_3():
    int_0 = -1797
    bool_0 = True
    list_0 = [int_0, int_0]
    range_0 = module_0.Range(*list_0)
    var_0 = range_0.__getitem__(bool_0)
    iterator_0 = range_0.__iter__()

def test_case_4():
    dict_0 = {}
    list_0 = [dict_0, dict_0]
    tuple_0 = None
    map_list_0 = module_0.MapList(list_0, tuple_0)

def test_case_5():
    int_0 = 2
    int_1 = 3
    int_2 = 5
    int_3 = 7
    int_4 = 11
    int_5 = 13
    int_6 = [int_0, int_1, int_2, int_3, int_4, int_5]
    var_0 = lambda x: x * x
    map_list_0 = module_0.MapList(var_0, int_6)
    int_7 = -1
    var_1 = map_list_0[::int_7]

def test_case_6():
    bool_0 = False
    str_0 = 'split_by'
    set_0 = {str_0, bool_0, str_0}
    str_1 = 'm @~{,).\r'
    bool_1 = True
    dict_0 = {str_1: bool_1, str_1: set_0, str_1: str_0}
    var_0 = module_0.scanr(set_0, dict_0)
    iterator_0 = module_0.split_by(str_0)
    int_0 = -807
    str_2 = 'get_worker_id'
    iterator_1 = module_0.take(int_0, str_2)
    iterator_2 = None
    var_1 = module_0.scanl(bool_0, iterator_2)

def test_case_7():
    int_0 = -1797
    bool_0 = True
    list_0 = [int_0, int_0]
    range_0 = module_0.Range(*list_0)
    var_0 = range_0.__getitem__(bool_0)

def test_case_8():
    int_0 = 3
    list_0 = [int_0]
    range_0 = module_0.Range(*list_0)
    var_0 = range_0.__getitem__(int_0)

def test_case_9():
    int_0 = 3
    var_0 = range(int_0)
    iterator_0 = module_0.chunk(int_0, var_0)
    var_1 = list(iterator_0)

def test_case_10():
    int_0 = 3
    int_1 = 10
    list_0 = [int_0]
    lazy_list_0 = module_0.LazyList(list_0)
    var_0 = lazy_list_0.__iter__()
    var_1 = range(int_1)
    iterator_0 = module_0.chunk(int_0, var_1)
    var_2 = list(iterator_0)

def test_case_11():
    int_0 = 10
    var_0 = range(int_0)
    var_1 = lambda x: x % int_0 == int_0
    str_0 = ' Split by: '
    bool_0 = True
    str_1 = '.'
    iterator_0 = module_0.split_by(str_0, bool_0, separator=str_1)
    var_2 = list(iterator_0)

def test_case_12():
    int_0 = 2
    int_1 = [int_0, int_0, int_0]
    iterator_0 = module_0.drop(int_0, int_1)
    var_0 = list(iterator_0)

def test_case_13():
    str_0 = 'abcd'
    int_0 = 0
    iterator_0 = module_0.take(int_0, str_0)
    var_0 = list(iterator_0)
    int_1 = 100
    iterator_1 = module_0.take(int_1, str_0)
    var_1 = list(iterator_1)

def test_case_14():
    int_0 = 3
    int_1 = 0
    var_0 = lambda x: x % int_0 == int_1
    var_1 = range(int_1)
    iterator_0 = module_0.split_by(var_1, separator=int_0)
    var_2 = list(iterator_0)
    str_0 = ' Split by: '
    bool_0 = True
    str_1 = ' '
    iterator_1 = module_0.split_by(str_0, bool_0, separator=str_1)
    var_3 = list(iterator_1)

def test_case_15():
    int_0 = 10
    var_0 = range(int_0)
    int_1 = 3
    int_2 = 0
    var_1 = lambda x: x % int_1 == int_2
    var_2 = range(int_0)
    iterator_0 = module_0.split_by(var_2, separator=int_1)
    var_3 = list(iterator_0)
    str_0 = ' Split by: '
    bool_0 = False
    str_1 = ' '
    iterator_1 = module_0.split_by(str_0, bool_0, separator=str_1)
    var_4 = list(iterator_1)

def test_case_16():
    int_0 = 1709
    list_0 = [int_0]
    range_0 = module_0.Range(*list_0)
    float_0 = -1805.0
    var_0 = range_0.__getitem__(float_0)

def test_case_17():
    int_0 = -7
    var_0 = lambda x: x > int_0
    var_1 = range(int_0)
    iterator_0 = module_0.drop_until(var_0, var_1)
    var_2 = list(iterator_0)

def test_case_18():
    int_0 = 1000000
    var_0 = range(int_0)
    lazy_list_0 = module_0.LazyList(var_0)
    int_1 = 5
    iterator_0 = module_0.take(int_1, lazy_list_0)
    var_1 = list(iterator_0)
    var_2 = list(lazy_list_0)
    var_3 = range(int_0)
    var_4 = list(var_3)
    int_2 = 1
    int_3 = 3
    int_4 = 4
    int_5 = [int_2, int_4, int_3, int_4]
    lazy_list_1 = module_0.LazyList(int_5)
    var_5 = list(lazy_list_1)
    var_6 = list(lazy_list_1)

def test_case_19():
    int_0 = 10
    var_0 = range(int_0)
    lazy_list_0 = module_0.LazyList(var_0)
    int_1 = 0
    var_1 = None
    var_2 = lazy_list_0[int_1:var_1:var_1]
    int_2 = 5
    var_3 = range(int_2, int_0)
    var_4 = list(var_3)
    int_3 = -1
    var_5 = lazy_list_0[int_1:int_3]

def test_case_20():
    var_0 = lambda s, x: x + s
    str_0 = 'a'
    str_1 = 'b'
    str_2 = 'c'
    str_3 = 'd'
    str_4 = [str_0, str_1, str_2, str_3]
    var_1 = module_0.scanl(var_0, str_4)
    var_2 = tuple(var_1)