# Automatically generated by Pynguin.
import ansible.executor.stats as module_0

def test_case_0():
    try:
        float_0 = 1.0
        set_0 = {float_0, float_0}
        aggregate_stats_0 = module_0.AggregateStats()
        var_0 = aggregate_stats_0.decrement(float_0, set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -1587
        str_0 = '\x0b'
        dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0, int_0: str_0}
        aggregate_stats_0 = module_0.AggregateStats()
        var_0 = aggregate_stats_0.summarize(dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 2821
        bool_0 = False
        aggregate_stats_0 = module_0.AggregateStats()
        var_0 = aggregate_stats_0.update_custom_stats(int_0, bool_0)
        str_0 = 'fHi9{D'
        bool_1 = False
        var_1 = aggregate_stats_0.update_custom_stats(str_0, bool_1)
        aggregate_stats_1 = module_0.AggregateStats()
        int_1 = -1794
        aggregate_stats_2 = module_0.AggregateStats()
        var_2 = aggregate_stats_2.update_custom_stats(int_1, int_1)
        bool_2 = True
        var_3 = aggregate_stats_0.decrement(str_0, bool_2)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '$Z*wLau@,TbWA.\x0c0+"-2'
        list_0 = [str_0]
        float_0 = 1626.76
        tuple_0 = (float_0, list_0)
        aggregate_stats_0 = module_0.AggregateStats()
        var_0 = aggregate_stats_0.set_custom_stats(list_0, tuple_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 2815
        bool_0 = True
        aggregate_stats_0 = module_0.AggregateStats()
        var_0 = aggregate_stats_0.update_custom_stats(int_0, bool_0)
        str_0 = 't5|j@zxW'
        str_1 = '\rAE38L3dTxGP`u+'
        aggregate_stats_1 = module_0.AggregateStats()
        var_1 = aggregate_stats_1.increment(str_0, str_1)
    except BaseException:
        pass

def test_case_5():
    try:
        set_0 = None
        aggregate_stats_0 = module_0.AggregateStats()
        var_0 = aggregate_stats_0.summarize(set_0)
        str_0 = 'I=bO<B\x0bF.\x0cWP;+hU'
        float_0 = 60.0
        bytes_0 = b'\xef\xc4\x86U\xbe\xfb\xac\xfb`~'
        tuple_0 = (float_0, set_0, bytes_0, set_0)
        bytes_1 = None
        int_0 = -723
        tuple_1 = (tuple_0, bytes_1, int_0, str_0)
        var_1 = aggregate_stats_0.update_custom_stats(str_0, tuple_1)
        aggregate_stats_1 = module_0.AggregateStats()
        aggregate_stats_2 = module_0.AggregateStats()
        var_2 = aggregate_stats_0.update_custom_stats(str_0, float_0, set_0)
        bool_0 = True
        var_3 = aggregate_stats_2.decrement(tuple_0, bool_0)
    except BaseException:
        pass

def test_case_6():
    try:
        aggregate_stats_0 = module_0.AggregateStats()
        str_0 = 'custom'
        var_0 = aggregate_stats_0.decrement(str_0, str_0)
        set_0 = {str_0}
        var_1 = aggregate_stats_0.decrement(str_0, set_0)
    except BaseException:
        pass