# Automatically generated by Pynguin.
import ansible.plugins.lookup.csvfile as module_0

def test_case_0():
    try:
        float_0 = -756.0443
        c_s_v_recoder_0 = module_0.CSVRecoder(float_0)
        list_0 = [c_s_v_recoder_0, float_0]
        str_0 = 'lNo95['
        str_1 = '-l<k\n,\x0c&=f5iP9`8'
        dict_0 = {str_0: float_0, str_0: float_0, str_0: float_0, str_1: list_0}
        str_2 = None
        list_1 = [dict_0, c_s_v_recoder_0, float_0, c_s_v_recoder_0]
        var_0 = c_s_v_recoder_0.__iter__()
        tuple_0 = (list_1,)
        list_2 = [list_1, float_0, tuple_0, dict_0]
        c_s_v_reader_0 = module_0.CSVReader(list_2)
        var_1 = c_s_v_reader_0.__iter__()
        lookup_module_0 = module_0.LookupModule()
        var_2 = lookup_module_0.read_csv(list_0, dict_0, str_2)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'detached from'
        c_s_v_recoder_0 = module_0.CSVRecoder(str_0)
        var_0 = c_s_v_recoder_0.__next__()
    except BaseException:
        pass

def test_case_2():
    try:
        lookup_module_0 = module_0.LookupModule()
        str_0 = '\t'
        var_0 = lookup_module_0.read_csv(str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        list_0 = None
        int_0 = -2000
        c_s_v_reader_0 = module_0.CSVReader(list_0, int_0)
        lookup_module_0 = module_0.LookupModule()
        c_s_v_recoder_0 = module_0.CSVRecoder(lookup_module_0)
        list_1 = [c_s_v_recoder_0, c_s_v_reader_0, list_0, list_0]
        lookup_module_1 = module_0.LookupModule()
        dict_0 = None
        set_0 = {dict_0}
        tuple_0 = (int_0, set_0, c_s_v_reader_0, set_0)
        str_0 = 'q1={\x0c>E<7F;:nWlo'
        str_1 = 'XEXt?4'
        str_2 = 'vb~uBI'
        dict_1 = {lookup_module_1: str_0, c_s_v_reader_0: list_0, lookup_module_1: str_2}
        dict_2 = {str_0: dict_0, str_1: dict_0, str_2: dict_1, str_0: lookup_module_1}
        lookup_module_2 = module_0.LookupModule(lookup_module_1, tuple_0, **dict_2)
        var_0 = lookup_module_2.run(list_1)
    except BaseException:
        pass