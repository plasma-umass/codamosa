# Automatically generated by Pynguin.
import ansible.vars.fact_cache as module_0

def test_case_0():
    pass

def test_case_1():
    fact_cache_0 = module_0.FactCache()

def test_case_2():
    fact_cache_0 = module_0.FactCache()
    var_0 = fact_cache_0.__iter__()

def test_case_3():
    list_0 = []
    fact_cache_0 = module_0.FactCache(*list_0)
    var_0 = fact_cache_0.__len__()

def test_case_4():
    fact_cache_0 = module_0.FactCache()
    var_0 = fact_cache_0.keys()

def test_case_5():
    float_0 = 902.7
    bool_0 = False
    fact_cache_0 = module_0.FactCache()
    var_0 = fact_cache_0.keys()
    list_0 = [float_0]
    var_1 = fact_cache_0.flush()
    var_2 = fact_cache_0.first_order_merge(bool_0, list_0)