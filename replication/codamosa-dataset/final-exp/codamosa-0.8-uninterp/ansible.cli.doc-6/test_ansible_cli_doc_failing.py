# Automatically generated by Pynguin.
import ansible.cli.doc as module_0

def test_case_0():
    try:
        bytes_0 = b'\xb8h:b +\xbf\x81'
        doc_c_l_i_0 = module_0.DocCLI(bytes_0)
        var_0 = doc_c_l_i_0.init_parser()
    except BaseException:
        pass

def test_case_1():
    try:
        complex_0 = None
        bytes_0 = b'\xa6_"\xfaN+\x80\xa2'
        doc_c_l_i_0 = module_0.DocCLI(bytes_0)
        var_0 = doc_c_l_i_0.display_plugin_list(complex_0)
    except BaseException:
        pass

def test_case_2():
    try:
        role_mixin_0 = module_0.RoleMixin()
        doc_c_l_i_0 = module_0.DocCLI(role_mixin_0)
        var_0 = doc_c_l_i_0.run()
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = -2296
        role_mixin_0 = module_0.RoleMixin()
        bool_0 = False
        var_0 = module_0.add_collection_plugins(role_mixin_0, bool_0)
        str_0 = '2AdM\rR\n;bsNdiy,Ju'
        dict_0 = {str_0: str_0, str_0: int_0}
        doc_c_l_i_0 = module_0.DocCLI(dict_0)
        str_1 = '54t2bKj'
        doc_c_l_i_1 = module_0.DocCLI(str_1)
        var_1 = doc_c_l_i_1.get_all_plugins_of_type(doc_c_l_i_0)
    except BaseException:
        pass

def test_case_4():
    try:
        complex_0 = None
        list_0 = [complex_0]
        doc_c_l_i_0 = module_0.DocCLI(list_0)
        doc_c_l_i_1 = module_0.DocCLI(doc_c_l_i_0)
        list_1 = [doc_c_l_i_0, complex_0, complex_0]
        plugin_not_found_0 = module_0.PluginNotFound(*list_1)
        float_0 = 0.2
        role_mixin_0 = module_0.RoleMixin()
        var_0 = doc_c_l_i_0.get_plugin_metadata(float_0, role_mixin_0)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = -1576.62372
        str_0 = '_R?>JA['
        list_0 = [str_0, float_0, float_0, str_0]
        str_1 = '8nuF8;i59'
        doc_c_l_i_0 = module_0.DocCLI(str_1)
        var_0 = doc_c_l_i_0.format_snippet(float_0, str_0, list_0)
        bytes_0 = b'\x1d6bZ\xc8Z3\\\xfc\xe7\xfd\x89\xff\x13\xdeZ>'
        set_0 = {str_1, var_0, doc_c_l_i_0}
        int_0 = 1965
        var_1 = doc_c_l_i_0.namespace_from_plugin_filepath(bytes_0, set_0, int_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'CZU*p)q$](9lX^|'
        str_1 = '}l(<IY'
        plugin_not_found_0 = module_0.PluginNotFound()
        str_2 = ''
        float_0 = -965.03
        dict_0 = {str_2: str_0, str_0: str_2, str_2: float_0}
        dict_1 = None
        tuple_0 = (float_0, dict_0, dict_1)
        str_3 = 'socket path %s does not exist or cannot be found. See Troubleshooting socket path issues in the Network Debug and Troubleshooting Guide'
        dict_2 = {str_3: str_3}
        list_0 = [dict_2, dict_2, dict_2, dict_2]
        doc_c_l_i_0 = module_0.DocCLI(list_0)
        var_0 = doc_c_l_i_0.format_plugin_doc(str_0, str_1, plugin_not_found_0, str_2, tuple_0, float_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = -2296
        doc_c_l_i_0 = module_0.DocCLI(int_0)
        set_0 = set()
        var_0 = doc_c_l_i_0.get_man_text(set_0)
    except BaseException:
        pass

def test_case_8():
    try:
        float_0 = -1570.9696894754056
        str_0 = 'R?>J[k'
        list_0 = [str_0, float_0, float_0, str_0]
        str_1 = '8nuF8;i59'
        doc_c_l_i_0 = module_0.DocCLI(str_1)
        var_0 = doc_c_l_i_0.format_snippet(float_0, str_0, list_0)
        dict_0 = {var_0: float_0}
        list_1 = None
        var_1 = doc_c_l_i_0.get_role_man_text(dict_0, list_1)
    except BaseException:
        pass

def test_case_9():
    try:
        float_0 = 2351.3983
        str_0 = 'aZFJ)j:TxWA~ID>A0'
        bool_0 = False
        bool_1 = True
        doc_c_l_i_0 = module_0.DocCLI(bool_1)
        var_0 = doc_c_l_i_0.find_plugins(float_0, str_0, str_0, bool_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bool_0 = True
        role_mixin_0 = module_0.RoleMixin()
        list_0 = [bool_0, role_mixin_0, role_mixin_0]
        doc_c_l_i_0 = module_0.DocCLI(role_mixin_0)
        doc_c_l_i_1 = None
        set_0 = {doc_c_l_i_1, doc_c_l_i_1}
        doc_c_l_i_2 = module_0.DocCLI(set_0)
        var_0 = doc_c_l_i_2.add_fields(bool_0, role_mixin_0, role_mixin_0, list_0, doc_c_l_i_0)
    except BaseException:
        pass

def test_case_11():
    try:
        bytes_0 = b'aV\xa0>\xfcJ\x88t\xd5}#K'
        var_0 = module_0.jdump(bytes_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'ansible_collections.'
        role_mixin_0 = module_0.RoleMixin()
        str_1 = '9000/785'
        doc_c_l_i_0 = module_0.DocCLI(str_1)
        var_0 = doc_c_l_i_0.run()
        str_2 = 'I]5ws\t_9(NPetl:=ho>'
        str_3 = 'RbtG-v$zP8i{'
        dict_0 = {str_2: var_0, str_2: str_2, str_1: role_mixin_0, str_3: str_2}
        tuple_0 = (str_0, dict_0)
        doc_c_l_i_1 = module_0.DocCLI(role_mixin_0)
        var_1 = doc_c_l_i_1.find_plugins(str_0, doc_c_l_i_0, tuple_0)
        str_4 = "d?Y}I;ntT^1C#5U'$V"
        tuple_1 = (str_4, doc_c_l_i_0, str_4)
        dict_1 = {doc_c_l_i_0: str_0, str_1: tuple_1, doc_c_l_i_0: doc_c_l_i_0}
        list_0 = [dict_1, str_4, str_4]
        var_2 = module_0.add_collection_plugins(dict_1, list_0, role_mixin_0)
    except BaseException:
        pass

def test_case_13():
    try:
        float_0 = -3758.43
        plugin_not_found_0 = None
        var_0 = module_0.add_collection_plugins(float_0, plugin_not_found_0)
        bytes_0 = b'\x03\xc4\x17\xac\x91\x8c3\x8b'
        doc_c_l_i_0 = module_0.DocCLI(bytes_0)
        list_0 = []
        str_0 = '/=qq>27~\\6<'
        set_0 = set()
        str_1 = 'i##TL_09"I1'
        doc_c_l_i_1 = module_0.DocCLI(str_1)
        var_1 = doc_c_l_i_1.add_fields(list_0, str_0, set_0, float_0)
    except BaseException:
        pass

def test_case_14():
    try:
        list_0 = []
        plugin_not_found_0 = module_0.PluginNotFound(*list_0)
        role_mixin_0 = module_0.RoleMixin()
        bool_0 = True
        str_0 = ',\n,jOE-'
        float_0 = 999.579481
        doc_c_l_i_0 = module_0.DocCLI(float_0)
        var_0 = doc_c_l_i_0.find_plugins(bool_0, str_0, role_mixin_0)
        doc_c_l_i_1 = module_0.DocCLI(str_0)
        dict_0 = {}
        role_mixin_1 = module_0.RoleMixin(*list_0, **dict_0)
        str_1 = 'st_%s'
        dict_1 = {str_1: str_1}
        var_1 = doc_c_l_i_1.format_snippet(doc_c_l_i_1, plugin_not_found_0, dict_1)
        int_0 = -2398
        set_0 = set()
        bytes_0 = b'\x1f\xc1\x1d\xfa\xdb\xca\xd8w\x0c\x15k'
        var_2 = doc_c_l_i_0.add_fields(list_0, set_0, bytes_0, list_0)
        str_2 = '(MMSAcZlO'
        var_3 = module_0.add_collection_plugins(float_0, int_0, str_2)
        var_4 = doc_c_l_i_1.run()
        plugin_not_found_1 = module_0.PluginNotFound(*list_0)
        var_5 = doc_c_l_i_0.display_plugin_list(str_2)
    except BaseException:
        pass

def test_case_15():
    try:
        dict_0 = {}
        str_0 = '?{~NniHLEm+S\x0bg"'
        bytes_0 = b'X\xe9\r\xd3\xad\xb0\r\xe1\x17\xa7'
        plugin_loader_0 = None
        float_0 = 4418.3846
        tuple_0 = (bytes_0, plugin_loader_0, float_0)
        doc_c_l_i_0 = module_0.DocCLI(tuple_0)
        var_0 = doc_c_l_i_0.get_man_text(dict_0, str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        list_0 = []
        plugin_not_found_0 = module_0.PluginNotFound(*list_0)
        role_mixin_0 = module_0.RoleMixin()
        bool_0 = True
        str_0 = ',\n,jOE-'
        float_0 = 999.579481
        doc_c_l_i_0 = module_0.DocCLI(float_0)
        var_0 = doc_c_l_i_0.find_plugins(bool_0, str_0, role_mixin_0)
        doc_c_l_i_1 = module_0.DocCLI(str_0)
        dict_0 = {}
        role_mixin_1 = module_0.RoleMixin(*list_0, **dict_0)
        str_1 = 'st_%s'
        dict_1 = {str_1: str_1}
        var_1 = doc_c_l_i_1.format_snippet(doc_c_l_i_1, plugin_not_found_0, dict_1)
        int_0 = -2398
        set_0 = set()
        bytes_0 = b'\x1f\xc1\x1d\xfa\xdb\xca\xd8w\x0c\x15k'
        var_2 = doc_c_l_i_0.add_fields(list_0, set_0, bytes_0, list_0)
        str_2 = '(MMSAcZlO'
        var_3 = module_0.add_collection_plugins(dict_1, dict_0)
        var_4 = module_0.add_collection_plugins(float_0, int_0, str_2)
        var_5 = doc_c_l_i_1.run()
        dict_2 = {var_2: dict_0}
        var_6 = doc_c_l_i_0.get_role_man_text(str_0, dict_2)
    except BaseException:
        pass