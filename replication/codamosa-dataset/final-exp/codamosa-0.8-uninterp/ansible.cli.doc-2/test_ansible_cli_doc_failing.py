# Automatically generated by Pynguin.
import ansible.cli.doc as module_0

def test_case_0():
    try:
        role_mixin_0 = module_0.RoleMixin()
        var_0 = module_0.jdump(role_mixin_0)
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = None
        doc_c_l_i_0 = module_0.DocCLI(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'd\xac\x15\x1btI\x10G\xca\xe8e'
        str_0 = '$W7\x0cS`?o$'
        doc_c_l_i_0 = module_0.DocCLI(str_0)
        var_0 = doc_c_l_i_0.display_plugin_list(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 1.5
        list_0 = [float_0, float_0]
        float_1 = 1.0
        doc_c_l_i_0 = module_0.DocCLI(float_1)
        str_0 = 'Nm4%|9'
        dict_0 = {str_0: str_0}
        var_0 = module_0.add_collection_plugins(float_0, list_0, dict_0)
        list_1 = []
        role_mixin_0 = module_0.RoleMixin(*list_1)
        doc_c_l_i_1 = module_0.DocCLI(dict_0)
        float_2 = -1651.7
        doc_c_l_i_2 = module_0.DocCLI(float_2)
        var_1 = doc_c_l_i_2.get_plugin_metadata(doc_c_l_i_1, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '\n_raw:\n  description:\n    - a password\n  type: list\n  elements: str\n'
        bytes_0 = b'\xb0\xc2\xf5\x90l\n\x9b\x98\r\xcb\x1c\xb6\xe6'
        set_0 = {bytes_0}
        plugin_not_found_0 = module_0.PluginNotFound()
        doc_c_l_i_0 = module_0.DocCLI(plugin_not_found_0)
        var_0 = doc_c_l_i_0.namespace_from_plugin_filepath(str_0, bytes_0, set_0)
    except BaseException:
        pass

def test_case_5():
    try:
        role_mixin_0 = module_0.RoleMixin()
        str_0 = 'w.5RC]C= Z '
        str_1 = "\nname: powershell\nversion_added: historical\nshort_description: Windows PowerShell\ndescription:\n- The only option when using 'winrm' or 'psrp' as a connection plugin.\n- Can also be used when using 'ssh' as a connection plugin and the C(DefaultShell) has been configured to PowerShell.\nextends_documentation_fragment:\n- shell_windows\n"
        dict_0 = {str_1: str_1, str_1: str_1}
        doc_c_l_i_0 = module_0.DocCLI(dict_0)
        list_0 = [doc_c_l_i_0, str_0]
        list_1 = []
        set_0 = {str_0, str_0}
        float_0 = 1388.1
        var_0 = doc_c_l_i_0.format_plugin_doc(list_0, list_1, doc_c_l_i_0, set_0, list_1, float_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'sFl^wZaOr(7^@Cs4&'
        doc_c_l_i_0 = module_0.DocCLI(str_0)
        var_0 = doc_c_l_i_0.run()
        set_0 = set()
        bytes_0 = b'%\xffHB\xba\x001\\\xe1\xe6W\x925\xbf'
        list_0 = []
        tuple_0 = (set_0, bytes_0, list_0)
        list_1 = None
        var_1 = doc_c_l_i_0.add_fields(tuple_0, bytes_0, list_1, tuple_0)
    except BaseException:
        pass

def test_case_7():
    try:
        dict_0 = {}
        float_0 = -292.08
        doc_c_l_i_0 = module_0.DocCLI(float_0)
        var_0 = doc_c_l_i_0.get_man_text(dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        set_0 = None
        bool_0 = True
        list_0 = []
        str_0 = 'Q7|p}5_4bMbf@$AN\r;\tk'
        doc_c_l_i_0 = module_0.DocCLI(str_0)
        var_0 = doc_c_l_i_0.run()
        list_1 = [str_0, set_0, list_0]
        doc_c_l_i_1 = module_0.DocCLI(list_1)
        str_1 = None
        set_1 = {set_0, bool_0}
        list_2 = [list_1, doc_c_l_i_1, set_1, doc_c_l_i_0]
        var_1 = doc_c_l_i_1.get_role_man_text(str_1, list_2)
    except BaseException:
        pass

def test_case_9():
    try:
        float_0 = 876.401628
        role_mixin_0 = module_0.RoleMixin()
        bytes_0 = b'\xa1\xcc\xa6\xe5g\x8f\x87R\x84\xfb\xfd\xdf\xf0\xd7\x9c\x01\xa1\xd6U'
        bool_0 = True
        doc_c_l_i_0 = module_0.DocCLI(bool_0)
        str_0 = '\t[/\nw"^qEHlWU?PRclx!'
        str_1 = ']'
        dict_0 = {str_1: bytes_0, str_1: str_1, str_1: float_0}
        var_0 = doc_c_l_i_0.get_role_man_text(str_0, dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = "5<Lv8~O@z%'="
        int_0 = 20
        dict_0 = {str_0: int_0, str_0: str_0}
        list_0 = [int_0, dict_0, str_0, int_0]
        str_1 = ''
        list_1 = [int_0, dict_0, str_0]
        doc_c_l_i_0 = module_0.DocCLI(list_1)
        str_2 = 'YWi(Z4,p@9.1Z}_$I'
        str_3 = '#'
        tuple_0 = (str_3,)
        str_4 = '(\\/sTO?-/-\rK'
        doc_c_l_i_1 = module_0.DocCLI(str_4)
        var_0 = doc_c_l_i_1.add_fields(list_0, str_1, doc_c_l_i_0, str_2, tuple_0)
        tuple_1 = (str_0, int_0, dict_0)
        role_mixin_0 = module_0.RoleMixin()
        int_1 = None
        bytes_0 = b'\xba\xf0\x85s\x91s\xc2'
        doc_c_l_i_2 = module_0.DocCLI(bytes_0)
        var_1 = doc_c_l_i_2.add_fields(list_0, dict_0, tuple_1, role_mixin_0, int_1, list_0)
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = -1542
        bool_0 = True
        plugin_not_found_0 = module_0.PluginNotFound()
        var_0 = module_0.add_collection_plugins(bool_0, plugin_not_found_0)
        int_1 = 969
        list_0 = [var_0, int_1, int_0]
        doc_c_l_i_0 = module_0.DocCLI(list_0)
        var_1 = doc_c_l_i_0.get_all_plugins_of_type(plugin_not_found_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = ''
        str_1 = 'YWi(Z4,p@9.1Z}_$I'
        doc_c_l_i_0 = module_0.DocCLI(str_1)
        str_2 = 'r'
        var_0 = doc_c_l_i_0.run()
        plugin_not_found_0 = module_0.PluginNotFound()
        dict_0 = {str_0: str_0}
        var_1 = doc_c_l_i_0.get_man_text(dict_0, str_2)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = "5<Lv8~O@3aIz%'="
        dict_0 = {}
        role_mixin_0 = module_0.RoleMixin(**dict_0)
        dict_1 = None
        list_0 = [role_mixin_0, dict_0]
        var_0 = module_0.add_collection_plugins(role_mixin_0, dict_1, list_0)
        int_0 = 20
        list_1 = [int_0, dict_1, str_0, int_0]
        str_1 = ''
        list_2 = [int_0, dict_1, str_0]
        doc_c_l_i_0 = module_0.DocCLI(list_2)
        str_2 = 'YWi(Z4,p@9.1Z}_$I'
        str_3 = '#'
        tuple_0 = (str_3,)
        str_4 = 'j:V'
        doc_c_l_i_1 = module_0.DocCLI(str_4)
        var_1 = doc_c_l_i_1.add_fields(list_1, str_1, doc_c_l_i_0, str_2, tuple_0)
        tuple_1 = (str_0, int_0, dict_1)
        list_3 = [tuple_0, str_2]
        int_1 = None
        str_5 = 'F#KEP'
        str_6 = '/r'
        dict_2 = {str_2: str_4, str_2: tuple_1, doc_c_l_i_0: str_0}
        doc_c_l_i_2 = module_0.DocCLI(dict_2)
        var_2 = doc_c_l_i_2.namespace_from_plugin_filepath(str_5, str_6, str_4)
        str_7 = '}p#Hnly,xz'
        doc_c_l_i_3 = module_0.DocCLI(doc_c_l_i_0)
        plugin_not_found_0 = module_0.PluginNotFound(*list_3)
        set_0 = {str_7, int_1, str_4}
        str_8 = '<[\x0bNBx'
        float_0 = -950.01
        var_3 = doc_c_l_i_1.add_fields(set_0, str_8, list_2, float_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'H\x0b v3 V0NV(\n'
        dict_0 = {}
        dict_1 = {str_0: dict_0}
        bytes_0 = None
        float_0 = -1354.0
        tuple_0 = (float_0, float_0, float_0)
        doc_c_l_i_0 = module_0.DocCLI(tuple_0)
        int_0 = 16
        doc_c_l_i_1 = module_0.DocCLI(int_0)
        var_0 = doc_c_l_i_1.add_fields(dict_1, dict_1, bytes_0, doc_c_l_i_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'yNKhD =_l1e'
        str_1 = 'n7=TrNJ9#oC9-hVZn'
        doc_c_l_i_0 = module_0.DocCLI(str_1)
        doc_c_l_i_1 = module_0.DocCLI(doc_c_l_i_0)
        complex_0 = None
        var_0 = doc_c_l_i_0.init_parser()
        list_0 = [doc_c_l_i_1, str_0, doc_c_l_i_1, complex_0]
        var_1 = doc_c_l_i_0.run()
        list_1 = []
        plugin_not_found_0 = module_0.PluginNotFound()
        str_2 = 'PLUGIN_PATH_CACHE'
        var_2 = doc_c_l_i_0.format_snippet(list_0, list_1, str_2)
        str_3 = 'lookup'
        var_3 = doc_c_l_i_0.get_plugin_metadata(str_3, doc_c_l_i_0)
    except BaseException:
        pass