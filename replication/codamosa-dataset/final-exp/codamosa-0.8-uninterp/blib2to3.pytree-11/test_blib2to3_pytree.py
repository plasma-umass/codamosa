# Automatically generated by Pynguin.
import blib2to3.pytree as module_0
import blib2to3.pgen2.grammar as module_1

def test_case_0():
    pass

def test_case_1():
    int_0 = 1226
    list_0 = []
    node_0 = module_0.Node(int_0, list_0)

def test_case_2():
    str_0 = 'N$eu<J;B'
    int_0 = 59
    leaf_0 = module_0.Leaf(int_0, str_0)
    leaf_1 = leaf_0.clone()

def test_case_3():
    int_0 = 15
    str_0 = '9:%! tSJ>egrc'
    leaf_0 = module_0.Leaf(int_0, str_0)
    str_1 = leaf_0.__repr__()

def test_case_4():
    negated_pattern_0 = module_0.NegatedPattern()

def test_case_5():
    str_0 = 'Bp}\x0c5+K<mB'
    int_0 = 0
    wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0, int_0)
    leaf_pattern_0 = module_0.LeafPattern(int_0, str_0)
    bool_0 = wildcard_pattern_0.match(wildcard_pattern_0)

def test_case_6():
    str_0 = '=\thJ{6p\nH,\tFnl<;VG'
    wildcard_pattern_0 = module_0.WildcardPattern(str_0)

def test_case_7():
    str_0 = 'E ZOiFo)!PkLDX{['
    wildcard_pattern_0 = module_0.WildcardPattern(str_0)
    any_0 = wildcard_pattern_0.optimize()

def test_case_8():
    grammar_0 = module_1.Grammar()
    int_0 = -3417
    str_0 = None
    leaf_0 = None
    list_0 = [leaf_0]
    tuple_0 = (int_0, str_0, int_0, list_0)
    var_0 = module_0.convert(grammar_0, tuple_0)

def test_case_9():
    int_0 = 1226
    list_0 = []
    node_0 = module_0.Node(int_0, list_0)
    optional_0 = node_0.remove()
    int_1 = node_0.depth()
    node_1 = node_0.clone()
    int_2 = None
    grammar_0 = None
    tuple_0 = None
    node_2 = node_1.clone()
    list_1 = [node_2, node_1]
    tuple_1 = (int_0, int_2, tuple_0, list_1)
    var_0 = module_0.convert(grammar_0, tuple_1)
    node_0.append_child(node_1)
    optional_1 = node_0.remove()

def test_case_10():
    int_0 = 390
    list_0 = []
    node_0 = module_0.Node(int_0, list_0)
    node_1 = node_0.clone()

def test_case_11():
    int_0 = 1225
    list_0 = []
    node_0 = module_0.Node(int_0, list_0)
    optional_0 = node_0.remove()
    node_1 = node_0.clone()
    node_0.append_child(node_1)
    optional_1 = node_1.remove()

def test_case_12():
    int_0 = 1226
    list_0 = []
    node_0 = module_0.Node(int_0, list_0)
    optional_0 = node_0.get_lineno()
    int_1 = node_0.depth()
    node_1 = node_0.clone()
    str_0 = '.8Qm}h'
    wildcard_pattern_0 = module_0.WildcardPattern(str_0)
    any_0 = wildcard_pattern_0.optimize()
    node_0.append_child(node_1)
    int_2 = node_0.depth()
    optional_1 = node_1.remove()
    node_1.insert_child(int_0, node_0)

def test_case_13():
    int_0 = 0
    str_0 = 'Grammar.txt'
    int_1 = 1225
    leaf_0 = module_0.Leaf(int_0, str_0)
    leaf_1 = leaf_0.clone()
    leaf_2 = leaf_1.clone()
    leaf_3 = leaf_2.clone()
    leaf_4 = leaf_3.clone()
    list_0 = [leaf_4, leaf_3, leaf_0]
    list_1 = [leaf_3, str_0, leaf_4, leaf_4]
    node_0 = module_0.Node(int_1, list_0, str_0, list_1)
    node_1 = node_0.clone()
    node_1.update_sibling_maps()

def test_case_14():
    str_0 = 'bare_name'
    wildcard_pattern_0 = module_0.WildcardPattern(str_0)
    list_0 = []
    bool_0 = wildcard_pattern_0.match_seq(list_0)

def test_case_15():
    str_0 = 'Bp}\x0c5+K<mB'
    int_0 = 0
    wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0, int_0)
    leaf_pattern_0 = module_0.LeafPattern(int_0, str_0)
    leaf_0 = module_0.Leaf(int_0, str_0)
    var_0 = leaf_pattern_0.match(leaf_0)

def test_case_16():
    str_0 = 'Bp}\x0c5+K<mB'
    int_0 = 0
    wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0, int_0)
    bool_0 = wildcard_pattern_0.match(wildcard_pattern_0)

def test_case_17():
    str_0 = 'Bp}\x0c5+K<mB'
    int_0 = 0
    wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0, int_0)
    leaf_pattern_0 = module_0.LeafPattern(int_0, str_0)
    str_1 = None
    bool_0 = wildcard_pattern_0.match(wildcard_pattern_0, leaf_pattern_0)
    leaf_0 = module_0.Leaf(int_0, str_1)
    var_0 = leaf_pattern_0.match(leaf_0)

def test_case_18():
    str_0 = 'Bp}\x0c5+K<mB'
    int_0 = 0
    wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0, int_0)
    leaf_pattern_0 = module_0.LeafPattern(int_0, str_0)
    bool_0 = wildcard_pattern_0.match(wildcard_pattern_0, leaf_pattern_0)
    str_1 = ' \\4ho\\wPz8gF/-h'
    leaf_0 = module_0.Leaf(int_0, str_1)
    var_0 = leaf_pattern_0.match(leaf_0, str_0)

def test_case_19():
    str_0 = 'Bp}\x0c5+Kd<mB'
    int_0 = 1
    wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0, int_0)
    leaf_pattern_0 = module_0.LeafPattern(int_0, str_0)
    any_0 = wildcard_pattern_0.optimize()

def test_case_20():
    str_0 = 'Bp}\x0c5+K<mB'
    int_0 = 0
    wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0, int_0)
    leaf_pattern_0 = module_0.LeafPattern(int_0, str_0)
    str_1 = None
    leaf_pattern_1 = module_0.LeafPattern(str_1)
    leaf_0 = module_0.Leaf(int_0, str_1)
    var_0 = leaf_pattern_1.match(leaf_0)

def test_case_21():
    str_0 = '+'
    wildcard_pattern_0 = module_0.WildcardPattern(str_0)
    any_0 = wildcard_pattern_0.optimize()

def test_case_22():
    str_0 = "<U$o]I'%Du:\x0c|\tJ6v"
    wildcard_pattern_0 = module_0.WildcardPattern(str_0)
    bool_0 = False
    dict_0 = {}
    set_0 = {str_0, str_0, bool_0, str_0}
    bool_1 = wildcard_pattern_0.match_seq(dict_0, set_0)

def test_case_23():
    int_0 = 1226
    list_0 = []
    node_0 = module_0.Node(int_0, list_0)
    optional_0 = node_0.remove()

def test_case_24():
    str_0 = 'q]|X\\pU'
    int_0 = 0
    wildcard_pattern_0 = module_0.WildcardPattern(str_0, int_0, int_0)
    leaf_pattern_0 = module_0.LeafPattern(int_0, str_0)
    leaf_0 = module_0.Leaf(int_0, str_0)
    var_0 = leaf_pattern_0.match(leaf_0, str_0)

def test_case_25():
    int_0 = 1234
    list_0 = []
    node_0 = module_0.Node(int_0, list_0)
    optional_0 = node_0.get_lineno()

def test_case_26():
    int_0 = 1211
    list_0 = []
    node_0 = module_0.Node(int_0, list_0)
    int_1 = node_0.depth()

def test_case_27():
    int_0 = 1
    str_0 = ''
    leaf_0 = module_0.Leaf(int_0, str_0)
    iterator_0 = leaf_0.post_order()
    var_0 = next(iterator_0)

def test_case_28():
    int_0 = 1226
    list_0 = []
    node_0 = module_0.Node(int_0, list_0)
    optional_0 = node_0.remove()
    node_1 = node_0.clone()
    node_0.append_child(node_1)
    node_1.replace(node_0)

def test_case_29():
    int_0 = 1226
    list_0 = []
    node_0 = module_0.Node(int_0, list_0)
    optional_0 = node_0.remove()
    int_1 = node_0.depth()
    optional_1 = node_0.get_lineno()
    node_1 = node_0.clone()
    int_2 = None
    node_0.append_child(node_1)
    str_0 = 'wR~ZoxS=(m7/PUlV.m['
    tuple_0 = (int_1, int_2)
    tuple_1 = (str_0, tuple_0)
    leaf_0 = module_0.Leaf(int_1, str_0, tuple_1, str_0)
    leaf_1 = leaf_0.clone()
    leaf_2 = leaf_1.clone()
    node_1.replace(list_0)

def test_case_30():
    int_0 = 1225
    list_0 = []
    node_0 = module_0.Node(int_0, list_0)
    optional_0 = node_0.remove()
    int_1 = node_0.depth()
    optional_1 = node_0.get_lineno()
    node_1 = node_0.clone()
    node_0.append_child(node_1)
    optional_2 = node_0.get_lineno()

def test_case_31():
    int_0 = 1225
    list_0 = []
    node_0 = module_0.Node(int_0, list_0)
    optional_0 = node_0.remove()
    int_1 = node_0.depth()
    optional_1 = node_0.get_lineno()
    node_1 = node_0.clone()
    node_0.append_child(node_1)
    node_2 = node_0.clone()
    node_0.append_child(node_2)
    str_0 = 'wR~ZoxS=(m7/PUlV.m['
    int_2 = 273
    tuple_0 = (int_1, int_2)
    tuple_1 = (str_0, tuple_0)
    leaf_0 = module_0.Leaf(int_1, str_0, tuple_1, str_0)
    optional_2 = node_2.remove()
    leaf_pattern_0 = module_0.LeafPattern()
    var_0 = leaf_pattern_0.match(node_0)

def test_case_32():
    int_0 = 1225
    list_0 = []
    node_0 = module_0.Node(int_0, list_0)
    optional_0 = node_0.remove()
    int_1 = node_0.depth()
    node_1 = node_0.clone()
    node_0.append_child(node_1)
    node_0.append_child(node_0)
    str_0 = 'wR~ZoxS=(m7/PUlV.m'
    int_2 = 273
    tuple_0 = (int_1, int_2)
    tuple_1 = (str_0, tuple_0)
    leaf_0 = module_0.Leaf(int_1, str_0, tuple_1, str_0)
    node_1.replace(node_1)

def test_case_33():
    int_0 = 1226
    list_0 = []
    node_0 = module_0.Node(int_0, list_0)
    optional_0 = node_0.remove()
    int_1 = node_0.depth()
    node_1 = node_0.clone()
    str_0 = 'F>'
    wildcard_pattern_0 = module_0.WildcardPattern(str_0)
    any_0 = wildcard_pattern_0.optimize()
    node_0.append_child(node_1)
    int_2 = node_1.depth()
    optional_1 = node_1.remove()