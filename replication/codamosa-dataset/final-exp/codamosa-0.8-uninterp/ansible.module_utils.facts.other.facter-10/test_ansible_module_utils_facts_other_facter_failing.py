# Automatically generated by Pynguin.
import ansible.module_utils.facts.other.facter as module_0

def test_case_0():
    try:
        facter_fact_collector_0 = module_0.FacterFactCollector()
        float_0 = -789.732
        var_0 = facter_fact_collector_0.collect(float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        set_0 = set()
        int_0 = 764
        facter_fact_collector_0 = module_0.FacterFactCollector()
        var_0 = facter_fact_collector_0.run_facter(set_0, int_0)
    except BaseException:
        pass