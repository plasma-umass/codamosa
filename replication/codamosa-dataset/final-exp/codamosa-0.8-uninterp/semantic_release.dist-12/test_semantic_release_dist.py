# Automatically generated by Pynguin.
import semantic_release.dist as module_0

def test_case_0():
    var_0 = module_0.should_remove_dist()

def test_case_1():
    str_0 = 'U'
    var_0 = module_0.remove_dists(str_0)
    var_1 = module_0.should_build()