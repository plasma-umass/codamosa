# Automatically generated by Pynguin.
import ansible.executor.stats as module_0

def test_case_0():
    try:
        aggregate_stats_0 = module_0.AggregateStats()
        bool_0 = None
        int_0 = -2135
        dict_0 = {int_0: aggregate_stats_0}
        var_0 = aggregate_stats_0.set_custom_stats(int_0, dict_0)
        float_0 = -363.558
        tuple_0 = (float_0, float_0, bool_0)
        var_1 = aggregate_stats_0.update_custom_stats(int_0, tuple_0)
        var_2 = aggregate_stats_0.set_custom_stats(dict_0, int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        aggregate_stats_0 = None
        bool_0 = False
        aggregate_stats_1 = module_0.AggregateStats()
        var_0 = aggregate_stats_1.update_custom_stats(aggregate_stats_0, bool_0, bool_0)
        int_0 = 4096
        str_0 = '#s9q^l=J~)'
        var_1 = aggregate_stats_1.set_custom_stats(int_0, str_0)
        str_1 = 'Archarm'
        var_2 = aggregate_stats_1.decrement(bool_0, str_1)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        set_0 = {bool_0, bool_0, bool_0}
        tuple_0 = (set_0,)
        aggregate_stats_0 = module_0.AggregateStats()
        var_0 = aggregate_stats_0.update_custom_stats(bool_0, tuple_0)
        aggregate_stats_1 = module_0.AggregateStats()
        str_0 = 'ok'
        var_1 = aggregate_stats_1.decrement(str_0, str_0)
        var_2 = aggregate_stats_0.decrement(str_0, tuple_0)
    except BaseException:
        pass