# Automatically generated by Pynguin.
import ansible.playbook.block as module_0
import ansible.errors as module_1

def test_case_0():
    try:
        list_0 = None
        list_1 = [list_0, list_0]
        block_0 = module_0.Block(list_1, list_1)
        var_0 = block_0.get_include_params()
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = -2857.7
        block_0 = module_0.Block(float_0)
        var_0 = block_0.get_include_params()
        bytes_0 = b'w|\x9a\xf8]3'
        block_1 = module_0.Block(bytes_0)
        list_0 = [block_1, bytes_0, bytes_0, block_1]
        var_1 = block_1.copy(list_0)
        var_2 = block_1.preprocess_data(bytes_0)
        var_3 = block_1.get_vars()
        float_1 = -896.093
        var_4 = block_1.__repr__()
        var_5 = block_1.__eq__(float_1)
    except BaseException:
        pass

def test_case_2():
    try:
        tuple_0 = ()
        block_0 = module_0.Block(tuple_0)
        var_0 = block_0.__ne__(tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        float_0 = -1152.4033
        int_0 = 3
        block_0 = module_0.Block(bool_0, float_0, int_0)
        var_0 = block_0.get_vars()
    except BaseException:
        pass

def test_case_4():
    try:
        block_0 = module_0.Block()
        str_0 = 'ne\twIb\nFJ[y"d'
        var_0 = block_0.load(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'w'
        block_0 = module_0.Block(str_0)
        bool_0 = True
        block_1 = module_0.Block(block_0, bool_0)
        var_0 = block_1.serialize()
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'L&;dR">^1'
        str_1 = ''
        block_0 = module_0.Block(str_0, str_1)
        str_2 = 'R;3ag\\85{16~i'
        block_1 = module_0.Block(block_0, str_2)
        var_0 = block_1.copy()
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = False
        int_0 = 41
        bool_1 = False
        str_0 = '+'
        block_0 = module_0.Block(str_0)
        tuple_0 = (int_0, bool_1, block_0, int_0)
        str_1 = '`U \x0cCfBt@QkjI'
        float_0 = 492.5345
        int_1 = 120
        tuple_1 = (float_0,)
        set_0 = None
        tuple_2 = (int_1, tuple_1, set_0)
        set_1 = {str_1, bool_0, tuple_2, tuple_2}
        tuple_3 = (float_0, set_1, float_0)
        block_1 = module_0.Block(str_1, tuple_3)
        var_0 = block_1.set_loader(tuple_0)
    except BaseException:
        pass

def test_case_8():
    try:
        block_0 = None
        bool_0 = True
        str_0 = None
        tuple_0 = (block_0, bool_0, bool_0, str_0)
        bool_1 = True
        dict_0 = {bool_0: bool_0, str_0: str_0, bool_0: tuple_0}
        block_1 = module_0.Block(tuple_0, bool_1, dict_0)
        var_0 = block_1.serialize()
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'P/Adyh2\r.1y3iWIE;$sz'
        block_0 = module_0.Block()
        var_0 = block_0.get_dep_chain()
        block_1 = module_0.Block()
        var_1 = block_1.set_loader(str_0)
        var_2 = block_1.get_include_params()
        var_3 = block_1.serialize()
        list_0 = [var_2]
        tuple_0 = ()
        float_0 = 5937.72788
        float_1 = None
        var_4 = block_0.load(list_0, tuple_0, float_0, float_1)
    except BaseException:
        pass

def test_case_10():
    try:
        set_0 = set()
        str_0 = '0242ac11-0018-38eb-9331-000000001198'
        block_0 = module_0.Block(set_0, str_0)
        var_0 = block_0.all_parents_static()
    except BaseException:
        pass

def test_case_11():
    try:
        block_0 = module_0.Block()
        var_0 = block_0.copy()
        bool_0 = True
        var_1 = block_0.get_first_parent_include()
        var_2 = block_0.set_loader(bool_0)
        var_3 = block_0.get_first_parent_include()
        var_4 = block_0.copy()
        var_5 = block_0.serialize()
        dict_0 = None
        tuple_0 = (dict_0,)
        list_0 = [tuple_0, dict_0, tuple_0]
        str_0 = ';PvWSuu`53qPdx'
        block_1 = module_0.Block(list_0, str_0)
        var_6 = block_1.get_first_parent_include()
    except BaseException:
        pass

def test_case_12():
    try:
        list_0 = []
        list_1 = [list_0, list_0, list_0]
        list_2 = [list_1]
        bytes_0 = b'\x92\x81$j\x0e\x04\xa3\x92l\x92\xfb\x12\xc4%\x82\x1fR~3'
        block_0 = module_0.Block(list_2, bytes_0)
        var_0 = block_0.get_first_parent_include()
    except BaseException:
        pass

def test_case_13():
    try:
        tuple_0 = ()
        float_0 = 2484.106
        block_0 = module_0.Block(float_0)
        block_1 = module_0.Block(block_0, tuple_0, tuple_0)
        var_0 = block_1.serialize()
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'SDtChR/2?s>Q>mv7>+'
        float_0 = 0.5
        block_0 = module_0.Block(float_0, float_0)
        var_0 = block_0.__repr__()
        block_1 = module_0.Block(str_0)
        var_1 = block_1.copy()
        str_1 = '9W2'
        var_2 = block_1.__repr__()
        var_3 = block_1.is_block(str_1)
        var_4 = block_1.get_first_parent_include()
        var_5 = block_0.has_tasks()
        var_6 = block_1.copy()
        dict_0 = None
        tuple_0 = (dict_0,)
        bool_0 = True
        block_2 = module_0.Block(tuple_0, var_6)
        var_7 = block_1.all_parents_static()
        str_2 = '0242ac11-0018-38eb-9331-0000000017ca'
        int_0 = -1250
        block_3 = module_0.Block(bool_0, str_2, int_0, block_0)
        var_8 = block_3.serialize()
    except BaseException:
        pass

def test_case_15():
    try:
        float_0 = None
        ansible_parser_error_0 = module_1.AnsibleParserError()
        list_0 = [ansible_parser_error_0, ansible_parser_error_0]
        bool_0 = False
        float_1 = 3427.194154
        block_0 = module_0.Block(list_0, bool_0, float_1)
        var_0 = block_0.set_loader(float_0)
    except BaseException:
        pass