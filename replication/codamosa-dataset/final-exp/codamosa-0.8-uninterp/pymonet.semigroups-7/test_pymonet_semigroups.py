# Automatically generated by Pynguin.
import pymonet.semigroups as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'VK#4{K%=?'
    first_0 = module_0.First(str_0)

def test_case_2():
    bool_0 = False
    set_0 = {bool_0, bool_0}
    sum_0 = module_0.Sum(set_0)
    sum_1 = module_0.Sum(sum_0)
    str_0 = sum_1.__str__()

def test_case_3():
    str_0 = 'Hac$$v'
    all_0 = module_0.All(str_0)
    str_1 = all_0.__str__()

def test_case_4():
    float_0 = 657.41
    one_0 = module_0.One(float_0)
    max_0 = module_0.Max(one_0)
    str_0 = max_0.__str__()

def test_case_5():
    set_0 = set()
    semigroup_0 = module_0.Semigroup(set_0)
    list_0 = [semigroup_0, semigroup_0, semigroup_0]
    bytes_0 = b'i\x84S\xe9%\x880\xe7\xdc\x99\xab\xac\x03|\x11\x1e'
    first_0 = module_0.First(bytes_0)
    one_0 = module_0.One(first_0)
    all_0 = module_0.All(one_0)
    one_1 = module_0.One(all_0)
    var_0 = one_1.concat(list_0)

def test_case_6():
    int_0 = 8
    max_0 = module_0.Max(int_0)
    list_0 = [int_0]
    first_0 = module_0.First(list_0)
    str_0 = first_0.__str__()
    int_1 = 6
    max_1 = module_0.Max(int_1)
    var_0 = max_0.concat(max_1)
    max_2 = module_0.Max(int_0)

def test_case_7():
    int_0 = 8
    max_0 = module_0.Max(int_0)
    int_1 = 7
    max_1 = module_0.Max(int_1)
    var_0 = max_0.concat(max_1)
    max_2 = module_0.Max(int_0)

def test_case_8():
    str_0 = '\x0c2WKPv\x0b\\sX&.MLM,Bu'
    min_0 = module_0.Min(str_0)
    str_1 = min_0.__str__()

def test_case_9():
    int_0 = 5
    min_0 = module_0.Min(int_0)
    int_1 = 10
    min_1 = module_0.Min(int_1)
    var_0 = min_0.concat(min_1)

def test_case_10():
    set_0 = set()
    semigroup_0 = module_0.Semigroup(set_0)
    sum_0 = module_0.Sum(semigroup_0)
    all_0 = None
    all_1 = module_0.All(set_0)
    all_2 = all_1.concat(all_0)
    list_0 = [set_0, all_2, all_2, all_1]
    min_0 = module_0.Min(all_2)
    tuple_0 = (sum_0, all_2, list_0, min_0)
    tuple_1 = (tuple_0, all_1)
    list_1 = [tuple_1]
    min_1 = module_0.Min(list_1)
    str_0 = min_1.__str__()

def test_case_11():
    min_0 = None
    float_0 = 2384.61538189501
    bool_0 = False
    all_0 = module_0.All(bool_0)
    bytes_0 = b'\xdc\xc9K\xfd\x8e\xd0\t\xf0c'
    all_1 = module_0.All(min_0)
    dict_0 = {}
    semigroup_0 = module_0.Semigroup(float_0)
    one_0 = module_0.One(semigroup_0)
    var_0 = one_0.concat(one_0)
    all_2 = all_1.concat(all_1)
    map_0 = module_0.Map(dict_0)
    var_1 = map_0.concat(bytes_0)

def test_case_12():
    int_0 = 1
    max_0 = module_0.Max(int_0)
    int_1 = 2
    max_1 = module_0.Max(int_1)
    var_0 = max_0.concat(max_1)
    max_2 = module_0.Max(int_1)

def test_case_13():
    int_0 = 567
    min_0 = module_0.Min(int_0)
    int_1 = 23
    min_1 = module_0.Min(int_1)
    var_0 = min_0.concat(min_1)
    min_2 = module_0.Min(int_1)