# Automatically generated by Pynguin.
import ansible.plugins.loader as module_0

def test_case_0():
    try:
        var_0 = module_0.get_all_plugin_loaders()
        bool_0 = False
        str_0 = '/usr/share/ansible/plugins/doc_fragments/windows'
        plugin_path_context_0 = module_0.PluginPathContext(bool_0, str_0)
        plugin_load_context_0 = module_0.PluginLoadContext()
        str_1 = 'q'
        dict_0 = {plugin_load_context_0: str_1}
        var_1 = module_0.get_shell_plugin(str_1, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        var_0 = module_0.get_shell_plugin()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'c%xN"n[S<Q&G]?\x0bI'
        var_0 = module_0.get_shell_plugin(str_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'z;E1#&*'
        float_0 = 2197.97556
        bytes_0 = b'\x1e\x11\xeevE\x8b\x91\x0f@\xa8\x8enq\xfa\xbd'
        bytes_1 = b'\xb1gS\xbd\x89'
        bool_0 = False
        set_0 = {bool_0}
        plugin_loader_0 = module_0.PluginLoader(float_0, bytes_0, bytes_1, set_0)
        list_0 = [str_0, plugin_loader_0]
        float_1 = 449.306674
        list_1 = [bool_0, float_1]
        var_0 = module_0.add_dirs_to_loader(list_0, list_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '/input/ansible/plugins/doc_fragments/windows'
        int_0 = 4481
        dict_0 = {}
        jinja2_loader_0 = module_0.Jinja2Loader(int_0, dict_0, dict_0, dict_0)
        var_0 = jinja2_loader_0.find_plugin(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = "d^4&6'm"
        list_0 = [str_0, str_0, str_0, str_0]
        int_0 = None
        list_1 = [list_0, int_0, list_0]
        bytes_0 = b'l\x99K\x00\xb0<\xc1\xf4'
        plugin_loader_0 = module_0.PluginLoader(str_0, list_0, list_1, bytes_0, str_0)
        var_0 = plugin_loader_0.print_paths()
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = False
        dict_0 = {bool_0: bool_0}
        plugin_load_context_0 = module_0.PluginLoadContext()
        var_0 = plugin_load_context_0.redirect(dict_0)
        plugin_load_context_1 = module_0.PluginLoadContext()
        plugin_load_context_2 = module_0.PluginLoadContext()
        float_0 = -2704.148275
        var_1 = module_0.get_shell_plugin(float_0)
    except BaseException:
        pass

def test_case_7():
    try:
        plugin_load_context_0 = module_0.PluginLoadContext()
        str_0 = 'R_'
        list_0 = []
        var_0 = module_0.get_shell_plugin(list_0, str_0)
        str_1 = '\x0b?fY'
        bytes_0 = b'\xc4o\xae\xd3\xba\x0c\xe7\xe6\xdf\xd4\x7f\xa0\xc5t\x80'
        jinja2_loader_0 = module_0.Jinja2Loader(bytes_0, str_1, str_1, plugin_load_context_0)
        var_1 = jinja2_loader_0.all()
    except BaseException:
        pass

def test_case_8():
    try:
        list_0 = []
        str_0 = '\nThe **urls** utils module offers a replacement for the urllib2 python library.\n\nurllib2 is the python stdlib way to retrieve files from the Internet but it\nlacks some security features (around verifying SSL certificates) that users\nshould care about in most situations. Using the functions in this module corrects\ndeficiencies in the urllib2 module wherever possible.\n\nThere are also third-party libraries (for instance, requests) which can be used\nto replace urllib2 with a more ]ecure library. However, all third party libraries\nrequire that the library be installed on the managed machine. That is an extra step\nfor users making use of a module. If possible, avoid third party libraries by using\nthis code instead.\n'
        bool_0 = False
        float_0 = -1018.48
        str_1 = 'H4~+8n'
        tuple_0 = ()
        plugin_loader_0 = module_0.PluginLoader(bool_0, float_0, list_0, str_1, tuple_0)
        var_0 = plugin_loader_0.get(str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        list_0 = []
        bool_0 = False
        float_0 = -1034.4327115881188
        str_0 = 'H4~+8n'
        tuple_0 = ()
        plugin_loader_0 = module_0.PluginLoader(bool_0, float_0, list_0, str_0, tuple_0)
        plugin_load_context_0 = module_0.PluginLoadContext()
        int_0 = 1512
        var_0 = plugin_loader_0.has_plugin(plugin_load_context_0, int_0)
        bytes_0 = None
        set_0 = {bytes_0, bytes_0}
        list_1 = []
        dict_0 = {}
        plugin_loader_1 = module_0.PluginLoader(set_0, list_1, dict_0, bool_0, bool_0)
    except BaseException:
        pass

def test_case_10():
    try:
        plugin_load_context_0 = module_0.PluginLoadContext()
        str_0 = 'R_'
        list_0 = []
        var_0 = module_0.get_shell_plugin(list_0, str_0)
        list_1 = [var_0, plugin_load_context_0, list_0, str_0]
        str_1 = '\x0b?fY'
        float_0 = -4005.15196
        bool_0 = False
        tuple_0 = (bool_0, str_1)
        plugin_loader_0 = module_0.PluginLoader(plugin_load_context_0, float_0, list_1, tuple_0, bool_0)
        dict_0 = {var_0: float_0, plugin_load_context_0: plugin_loader_0}
        int_0 = 4318
        var_1 = plugin_load_context_0.record_deprecation(list_1, dict_0, int_0)
        var_2 = plugin_loader_0.add_directory(str_1)
        var_3 = plugin_loader_0.__getstate__()
        var_4 = module_0.add_all_plugin_dirs(plugin_load_context_0)
        var_5 = plugin_loader_0.format_paths(dict_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '0xlhhJ]h'
        bool_0 = False
        str_1 = ':D '
        str_2 = "0\\T*p{' VD,\x0b~D%1EH'"
        dict_0 = {str_1: str_1, str_2: str_1, str_1: str_1, str_1: str_1}
        str_3 = '+k`TwHRMh+(19%^k_xG/'
        int_0 = -712
        dict_1 = {str_3: str_3, int_0: str_3}
        int_1 = -3682
        jinja2_loader_0 = module_0.Jinja2Loader(str_3, int_0, dict_1, int_1)
        tuple_0 = (jinja2_loader_0,)
        jinja2_loader_1 = module_0.Jinja2Loader(bool_0, bool_0, dict_0, tuple_0)
        var_0 = jinja2_loader_1.get(str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        list_0 = []
        bool_0 = False
        str_0 = '<string>'
        int_0 = 384
        set_0 = {int_0, bool_0, int_0}
        bool_1 = False
        float_0 = 797.41
        str_1 = 'Ti<a|_6UV|\x0bWcKz'
        dict_0 = {str_1: bool_1, str_1: bool_0}
        plugin_loader_0 = module_0.PluginLoader(bool_1, float_0, dict_0, dict_0, list_0)
        plugin_load_context_0 = module_0.PluginLoadContext()
        plugin_loader_1 = module_0.PluginLoader(int_0, set_0, list_0, plugin_loader_0, plugin_load_context_0)
        var_0 = plugin_loader_1.__setstate__(str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        plugin_load_context_0 = module_0.PluginLoadContext()
        str_0 = 'QQ03L.\x0c'
        tuple_0 = None
        var_0 = module_0.get_shell_plugin(str_0, tuple_0)
    except BaseException:
        pass

def test_case_14():
    try:
        plugin_load_context_0 = module_0.PluginLoadContext()
        str_0 = 'R_'
        list_0 = []
        var_0 = module_0.get_shell_plugin(list_0, str_0)
        list_1 = [var_0, plugin_load_context_0, list_0, str_0]
        str_1 = '\x0b?fY'
        float_0 = -4005.15196
        bool_0 = False
        tuple_0 = (bool_0, str_1)
        plugin_loader_0 = module_0.PluginLoader(plugin_load_context_0, float_0, list_1, tuple_0, bool_0)
        dict_0 = {var_0: float_0, plugin_load_context_0: plugin_loader_0}
        int_0 = 4318
        var_1 = plugin_load_context_0.record_deprecation(list_1, dict_0, int_0)
        var_2 = plugin_loader_0.add_directory(str_1)
        var_3 = module_0.add_all_plugin_dirs(str_1)
        bytes_0 = b'd~\x9a\xa6\x13<\xbf\xaf\xd6\x95B\xa6\x87\x14\x9b'
        int_1 = 660
        plugin_path_context_0 = module_0.PluginPathContext(bytes_0, int_1)
        bool_1 = True
        str_2 = 'Dx'
        plugin_load_context_1 = module_0.PluginLoadContext()
        var_4 = plugin_loader_0.find_plugin_with_context(bool_1, str_2, plugin_load_context_1)
    except BaseException:
        pass

def test_case_15():
    try:
        plugin_load_context_0 = module_0.PluginLoadContext()
        str_0 = '_'
        list_0 = []
        var_0 = module_0.get_shell_plugin(list_0, str_0)
        list_1 = [var_0, plugin_load_context_0, list_0, str_0]
        str_1 = '\x0b?fY'
        float_0 = -4005.15196
        bool_0 = False
        str_2 = '$4?YEzK'
        tuple_0 = (bool_0, str_2)
        plugin_loader_0 = module_0.PluginLoader(plugin_load_context_0, float_0, list_1, tuple_0, bool_0)
        dict_0 = {}
        int_0 = 4318
        var_1 = plugin_load_context_0.record_deprecation(list_1, dict_0, int_0)
        bytes_0 = b'\xc4\xb9\x91\xf8\x13'
        list_2 = [bytes_0, list_0, list_1]
        plugin_path_context_0 = module_0.PluginPathContext(list_2, list_0)
        jinja2_loader_0 = module_0.Jinja2Loader(tuple_0, plugin_path_context_0, tuple_0, bool_0)
        jinja2_loader_1 = module_0.Jinja2Loader(plugin_loader_0, plugin_load_context_0, jinja2_loader_0, str_1)
        var_2 = jinja2_loader_1.all()
    except BaseException:
        pass

def test_case_16():
    try:
        bytes_0 = b'S8x\x02w>'
        str_0 = 'all_slaves_active'
        set_0 = None
        float_0 = None
        dict_0 = {set_0: float_0}
        int_0 = -2071
        jinja2_loader_0 = module_0.Jinja2Loader(bytes_0, str_0, set_0, dict_0, int_0)
        plugin_load_context_0 = module_0.PluginLoadContext()
        int_1 = 1514
        dict_1 = {}
        bool_0 = False
        jinja2_loader_1 = module_0.Jinja2Loader(plugin_load_context_0, int_1, dict_1, bool_0)
        var_0 = jinja2_loader_1.find_plugin(jinja2_loader_0)
    except BaseException:
        pass

def test_case_17():
    try:
        plugin_load_context_0 = module_0.PluginLoadContext()
        str_0 = 'R_'
        list_0 = []
        var_0 = module_0.get_shell_plugin(list_0, str_0)
        list_1 = [var_0, plugin_load_context_0, list_0, str_0]
        float_0 = -4005.15196
        bool_0 = False
        tuple_0 = (bool_0, str_0)
        plugin_loader_0 = module_0.PluginLoader(plugin_load_context_0, float_0, list_1, tuple_0, bool_0)
        dict_0 = {}
        int_0 = 4318
        var_1 = plugin_load_context_0.record_deprecation(list_1, dict_0, int_0)
        var_2 = plugin_loader_0.add_directory(str_0)
        dict_1 = {}
        var_3 = plugin_loader_0.add_directory(str_0)
        var_4 = module_0.add_all_plugin_dirs(list_1)
        float_1 = 2080.1
        int_1 = 308
        plugin_loader_1 = module_0.PluginLoader(dict_1, tuple_0, float_1, dict_1, int_1)
    except BaseException:
        pass

def test_case_18():
    try:
        plugin_load_context_0 = module_0.PluginLoadContext()
        set_0 = {plugin_load_context_0, plugin_load_context_0}
        str_0 = '!qe'
        int_0 = -332
        plugin_loader_0 = module_0.PluginLoader(plugin_load_context_0, set_0, str_0, int_0)
        var_0 = plugin_loader_0.print_paths()
    except BaseException:
        pass

def test_case_19():
    try:
        plugin_load_context_0 = module_0.PluginLoadContext()
        str_0 = 'R_'
        list_0 = []
        var_0 = module_0.get_shell_plugin(list_0, str_0)
        list_1 = [var_0, plugin_load_context_0, list_0, str_0]
        str_1 = '\x0b?fY'
        float_0 = -4005.15196
        bool_0 = False
        str_2 = '$4?YEzK'
        tuple_0 = (bool_0, str_2)
        plugin_loader_0 = module_0.PluginLoader(plugin_load_context_0, float_0, list_1, tuple_0, bool_0)
        dict_0 = {var_0: float_0, plugin_load_context_0: plugin_loader_0}
        int_0 = 4294
        var_1 = plugin_load_context_0.record_deprecation(list_1, dict_0, int_0)
        var_2 = plugin_loader_0.add_directory(str_1)
        bool_1 = False
        var_3 = module_0.add_all_plugin_dirs(bool_1)
        bytes_0 = b'>[\xe1\xd4"A\x93\x1e\x89\x13R\x02\x13\x07\xc4\xa9\xd9'
        var_4 = plugin_loader_0.format_paths(bytes_0)
    except BaseException:
        pass

def test_case_20():
    try:
        plugin_load_context_0 = module_0.PluginLoadContext()
        str_0 = 'R_'
        list_0 = []
        var_0 = module_0.get_shell_plugin(list_0, str_0)
        list_1 = [var_0, plugin_load_context_0, list_0, str_0]
        float_0 = -1138.8
        plugin_load_context_1 = module_0.PluginLoadContext()
        var_1 = plugin_load_context_1.redirect(float_0)
        float_1 = -4005.15196
        bool_0 = False
        float_2 = 851.5
        var_2 = plugin_load_context_0.nope(float_2)
        str_1 = '-3'
        tuple_0 = (bool_0, str_1)
        plugin_loader_0 = module_0.PluginLoader(plugin_load_context_0, float_1, list_1, tuple_0, bool_0)
        var_3 = plugin_loader_0.has_plugin(list_0)
        str_2 = '{Dc[R"SvmS7<guuwdKr'
        dict_0 = {str_1: var_3, str_2: str_1}
        var_4 = plugin_loader_0.__setstate__(dict_0)
        str_3 = '\nZDTjQ\x0bB'
        jinja2_loader_0 = module_0.Jinja2Loader(dict_0, str_3, list_1, list_1, tuple_0)
    except BaseException:
        pass

def test_case_21():
    try:
        plugin_load_context_0 = module_0.PluginLoadContext()
        str_0 = '1'
        list_0 = []
        var_0 = module_0.get_shell_plugin(list_0, str_0)
        list_1 = [var_0, plugin_load_context_0, list_0, str_0]
        float_0 = -4005.15196
        bool_0 = True
        str_1 = "c'djg+,'r"
        tuple_0 = (bool_0, str_1)
        plugin_loader_0 = module_0.PluginLoader(plugin_load_context_0, float_0, list_1, tuple_0, bool_0)
        var_1 = plugin_loader_0.has_plugin(list_0)
        str_2 = 'found interpreters: {0}'
        set_0 = {tuple_0, str_2}
        plugin_path_context_0 = module_0.PluginPathContext(list_0, set_0)
        var_2 = plugin_loader_0.add_directory(str_2, plugin_path_context_0)
    except BaseException:
        pass

def test_case_22():
    try:
        plugin_load_context_0 = module_0.PluginLoadContext()
        plugin_path_context_0 = module_0.PluginPathContext(plugin_load_context_0, plugin_load_context_0)
        set_0 = {plugin_path_context_0, plugin_load_context_0}
        plugin_load_context_1 = module_0.PluginLoadContext()
        str_0 = "Q+~Q.n\r1\nOU6`'"
        bytes_0 = b',\x1f\xb4\xb5K\xc5\x9f\x90\xa7'
        int_0 = 456
        dict_0 = {}
        plugin_loader_0 = module_0.PluginLoader(plugin_load_context_1, str_0, bytes_0, int_0, dict_0)
        var_0 = plugin_loader_0.find_plugin_with_context(set_0)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = 'sh'
        set_0 = {str_0, str_0, str_0}
        dict_0 = {}
        dict_1 = {}
        int_0 = 384
        int_1 = None
        int_2 = -1303
        tuple_0 = (int_1, int_2)
        tuple_1 = (tuple_0,)
        bool_0 = False
        str_1 = 'Ff.@%Q-;Hh~ze'
        list_0 = [tuple_0, str_1]
        plugin_load_context_0 = module_0.PluginLoadContext()
        jinja2_loader_0 = module_0.Jinja2Loader(bool_0, str_1, bool_0, tuple_0, list_0, plugin_load_context_0)
        bytes_0 = b'\xefg\x84\xf5`\xee\xf2V\xfdZ\x1f\xb5\xea'
        bytes_1 = b"\x1d\xf1-\xd8I\x13\x9cv\xedi\x97\xed\xc0I\xbc>'"
        list_1 = [int_1, bool_0, bool_0]
        bytes_2 = b'#\xca\x9bD\xe9M\xfb\xbd'
        float_0 = 1219.399
        plugin_path_context_0 = module_0.PluginPathContext(jinja2_loader_0, float_0)
        plugin_loader_0 = module_0.PluginLoader(bytes_1, list_1, int_1, jinja2_loader_0, bytes_2, plugin_path_context_0)
        bool_1 = True
        int_3 = 3930
        get_with_context_result_0 = module_0.get_with_context_result(*list_0)
        jinja2_loader_1 = module_0.Jinja2Loader(plugin_load_context_0, get_with_context_result_0, jinja2_loader_0, bool_1)
        complex_0 = None
        dict_2 = {tuple_0: jinja2_loader_1, str_1: complex_0}
        plugin_loader_1 = module_0.PluginLoader(plugin_loader_0, bool_1, int_3, dict_2)
        str_2 = 'W[+'
        plugin_loader_2 = module_0.PluginLoader(plugin_loader_1, dict_2, str_2, complex_0)
        plugin_loader_3 = module_0.PluginLoader(tuple_1, jinja2_loader_0, bytes_0, plugin_loader_2)
        var_0 = plugin_loader_3.find_plugin_with_context(set_0, dict_0, dict_1, int_0)
    except BaseException:
        pass

def test_case_24():
    try:
        plugin_load_context_0 = module_0.PluginLoadContext()
        str_0 = 'h'
        list_0 = []
        var_0 = module_0.get_shell_plugin(list_0, str_0)
        list_1 = [var_0, plugin_load_context_0, list_0, str_0]
        float_0 = -4005.15196
        bool_0 = True
        str_1 = "c'djg+,'r"
        tuple_0 = (bool_0, str_1)
        plugin_loader_0 = module_0.PluginLoader(plugin_load_context_0, float_0, list_1, tuple_0, bool_0)
        dict_0 = {var_0: float_0, plugin_load_context_0: plugin_loader_0}
        var_1 = plugin_loader_0.has_plugin(list_0)
        str_2 = '$+\n]\n%^-88dR8%.!T'
        bytes_0 = b'\x16 \x0f7'
        plugin_path_context_0 = module_0.PluginPathContext(bytes_0, dict_0)
        bool_1 = False
        set_0 = {str_0, plugin_load_context_0}
        jinja2_loader_0 = module_0.Jinja2Loader(plugin_path_context_0, bool_1, set_0, plugin_path_context_0)
        var_2 = jinja2_loader_0.get(str_2)
    except BaseException:
        pass