# Automatically generated by Pynguin.
import ansible.plugins.lookup.csvfile as module_0

def test_case_0():
    try:
        int_0 = 2374
        c_s_v_recoder_0 = module_0.CSVRecoder(int_0)
        var_0 = c_s_v_recoder_0.__next__()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'Sel\x0bL>%:yh13&'
        c_s_v_reader_0 = module_0.CSVReader(str_0)
        var_0 = c_s_v_reader_0.__next__()
    except BaseException:
        pass

def test_case_2():
    try:
        lookup_module_0 = module_0.LookupModule()
        float_0 = 149.84952110272272
        var_0 = lookup_module_0.read_csv(lookup_module_0, float_0, lookup_module_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'PLK]tUT2\x0c\nR0\\3Mm!Z<'
        list_0 = [str_0, str_0]
        set_0 = set()
        str_1 = 'ol{.9/BPKn'
        bytes_0 = b'<\x84\x13N\x01\x9c\xf6\xcf\xde<\xae\x9c\xf5<\x9aS\xf8'
        dict_0 = {str_1: list_0, str_1: bytes_0}
        str_2 = 'subprocess'
        lookup_module_0 = module_0.LookupModule(str_2)
        var_0 = lookup_module_0.run(set_0, **dict_0)
    except BaseException:
        pass