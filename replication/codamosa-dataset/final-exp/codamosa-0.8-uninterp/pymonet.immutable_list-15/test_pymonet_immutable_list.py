# Automatically generated by Pynguin.
import pymonet.immutable_list as module_0
import builtins as module_1

def test_case_0():
    immutable_list_0 = module_0.ImmutableList()

def test_case_1():
    immutable_list_0 = module_0.ImmutableList()
    object_0 = module_1.object()
    bool_0 = immutable_list_0.__eq__(object_0)

def test_case_2():
    bool_0 = True
    immutable_list_0 = module_0.ImmutableList(bool_0)
    str_0 = immutable_list_0.__str__()
    var_0 = immutable_list_0.__len__()

def test_case_3():
    set_0 = None
    immutable_list_0 = module_0.ImmutableList()
    var_0 = immutable_list_0.unshift(set_0)

def test_case_4():
    immutable_list_0 = module_0.ImmutableList()
    var_0 = immutable_list_0.__len__()
    var_1 = immutable_list_0.__len__()
    var_2 = None
    var_3 = immutable_list_0.unshift(var_2)
    var_4 = immutable_list_0.unshift(immutable_list_0)

def test_case_5():
    bool_0 = True
    immutable_list_0 = module_0.ImmutableList(bool_0)
    var_0 = immutable_list_0.to_list()

def test_case_6():
    object_0 = None
    bool_0 = True
    immutable_list_0 = module_0.ImmutableList(bool_0)
    bool_1 = immutable_list_0.__eq__(object_0)
    immutable_list_1 = module_0.ImmutableList()
    callable_0 = None
    optional_0 = immutable_list_1.find(callable_0)

def test_case_7():
    object_0 = None
    str_0 = "2t=5|mV]ImUwwS=w}t'A"
    bytes_0 = b'\xf3&\xae\xf3\x98\xcb\xb8\xa29\xaa/\x9e\x1b\x82\xdf\xf8\xa8\x90J\xba'
    str_1 = 'E4gT9T`}{y0i9|_'
    str_2 = None
    dict_0 = {str_0: str_0, str_0: bytes_0, str_1: str_0, str_2: bytes_0}
    immutable_list_0 = module_0.ImmutableList()
    bool_0 = immutable_list_0.__eq__(object_0)
    immutable_list_1 = module_0.ImmutableList(dict_0, bool_0)
    var_0 = None
    var_1 = immutable_list_1.append(var_0)
    var_2 = immutable_list_0.__add__(var_1)
    bool_1 = False
    immutable_list_2 = module_0.ImmutableList(bool_1)
    immutable_list_3 = module_0.ImmutableList(var_0)
    var_3 = immutable_list_2.__len__()
    var_4 = immutable_list_3.to_list()

def test_case_8():
    set_0 = set()
    float_0 = -747.93929
    immutable_list_0 = module_0.ImmutableList()
    object_0 = module_1.object()
    bool_0 = immutable_list_0.__eq__(object_0)
    var_0 = immutable_list_0.append(float_0)
    var_1 = None
    var_2 = immutable_list_0.append(var_1)
    bool_1 = False
    immutable_list_1 = module_0.ImmutableList(set_0, var_0, bool_1)
    var_3 = immutable_list_1.__len__()

def test_case_9():
    bool_0 = True
    immutable_list_0 = module_0.ImmutableList(bool_0)
    bool_1 = True
    immutable_list_1 = module_0.ImmutableList(bool_1)
    bool_2 = True
    immutable_list_2 = module_0.ImmutableList(bool_2)
    bool_3 = True
    immutable_list_3 = module_0.ImmutableList(bool_3)
    var_0 = immutable_list_2 != immutable_list_3

def test_case_10():
    int_0 = 1
    int_1 = 2
    int_2 = 3
    immutable_list_0 = module_0.ImmutableList(int_2)
    immutable_list_1 = module_0.ImmutableList(int_1, immutable_list_0)
    immutable_list_2 = module_0.ImmutableList(int_0, immutable_list_1)
    immutable_list_3 = module_0.ImmutableList(int_2)
    immutable_list_4 = module_0.ImmutableList(int_1, immutable_list_3)
    immutable_list_5 = module_0.ImmutableList(int_0, immutable_list_4)
    immutable_list_6 = module_0.ImmutableList(int_2)
    immutable_list_7 = module_0.ImmutableList(int_1, immutable_list_6)
    immutable_list_8 = module_0.ImmutableList(int_0, immutable_list_7)
    int_3 = 4
    immutable_list_9 = module_0.ImmutableList(int_3)
    immutable_list_10 = module_0.ImmutableList(int_1, immutable_list_9)
    immutable_list_11 = module_0.ImmutableList(int_0, immutable_list_10)
    var_0 = immutable_list_8 == immutable_list_11
    immutable_list_12 = module_0.ImmutableList(int_2)
    immutable_list_13 = module_0.ImmutableList(int_1, immutable_list_12)
    immutable_list_14 = module_0.ImmutableList(int_0, immutable_list_13)
    immutable_list_15 = module_0.ImmutableList(int_2)
    immutable_list_16 = module_0.ImmutableList(int_3, immutable_list_15)
    immutable_list_17 = module_0.ImmutableList(int_0, immutable_list_16)
    var_1 = immutable_list_14 == immutable_list_17
    immutable_list_18 = module_0.ImmutableList(int_2)
    immutable_list_19 = module_0.ImmutableList(int_1, immutable_list_18)
    immutable_list_20 = module_0.ImmutableList(int_0, immutable_list_19)
    immutable_list_21 = module_0.ImmutableList(int_2)
    immutable_list_22 = module_0.ImmutableList(int_1, immutable_list_21)
    immutable_list_23 = module_0.ImmutableList(int_3, immutable_list_22)
    var_2 = immutable_list_20 == immutable_list_23
    immutable_list_24 = module_0.ImmutableList(int_2)
    immutable_list_25 = module_0.ImmutableList(int_1, immutable_list_24)
    immutable_list_26 = module_0.ImmutableList(int_0, immutable_list_25)
    immutable_list_27 = module_0.ImmutableList(int_0)
    var_3 = immutable_list_26 == immutable_list_27