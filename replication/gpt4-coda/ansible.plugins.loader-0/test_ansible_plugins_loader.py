# Automatically generated by Pynguin.
import ansible.plugins.loader as module_0

def test_case_0():
    pass

def test_case_1():
    plugin_load_context_0 = module_0.PluginLoadContext()
    var_0 = module_0.add_all_plugin_dirs(plugin_load_context_0)

def test_case_2():
    str_0 = '/another/path/to/plugins'
    str_1 = [str_0, str_0]
    str_2 = 'module'
    var_0 = module_0.add_dirs_to_loader(str_2, str_1)

def test_case_3():
    bool_0 = True
    plugin_load_context_0 = module_0.PluginLoadContext()
    var_0 = plugin_load_context_0.redirect(bool_0)

def test_case_4():
    str_0 = '\r\x0b|fR`g'
    list_0 = []
    float_0 = None
    int_0 = -431
    dict_0 = None
    str_1 = 'id'
    set_0 = None
    bytes_0 = b'\x08\x8f\xb8\xf5:^\x98\xa4g\xab\x04YS\xc7g'
    jinja2_loader_0 = module_0.Jinja2Loader(int_0, dict_0, str_1, set_0, bytes_0)
    plugin_load_context_0 = None
    plugin_loader_0 = module_0.PluginLoader(float_0, jinja2_loader_0, jinja2_loader_0, plugin_load_context_0)
    dict_1 = {str_1: plugin_loader_0, str_1: plugin_loader_0, str_1: set_0, str_0: int_0}
    tuple_0 = (plugin_loader_0, dict_1)
    plugin_loader_1 = module_0.PluginLoader(str_0, list_0, tuple_0, dict_0, int_0)
    var_0 = plugin_loader_1.__getstate__()

def test_case_5():
    str_0 = '\th'
    bytes_0 = None
    var_0 = module_0.get_shell_plugin(bytes_0, str_0)

def test_case_6():
    int_0 = -2727
    bool_0 = False
    str_0 = '/pynguin/\udc92\udcb7A*\udc8b\udcbc>E\udc9b\udce7\r,(U>\udc83\udc8b\udc9e<\x03/windows'
    var_0 = module_0.get_all_plugin_loaders()
    float_0 = -1112.332
    plugin_load_context_0 = module_0.PluginLoadContext()
    str_1 = '&ZF'
    plugin_loader_0 = module_0.PluginLoader(bool_0, str_0, float_0, plugin_load_context_0, str_1)
    var_1 = plugin_loader_0.has_plugin(int_0)

def test_case_7():
    var_0 = module_0.get_all_plugin_loaders()
    str_0 = '\th'
    bytes_0 = None
    var_1 = module_0.get_shell_plugin(bytes_0, str_0)

def test_case_8():
    plugin_load_context_0 = module_0.PluginLoadContext()
    var_0 = module_0.add_all_plugin_dirs(plugin_load_context_0)
    str_0 = 'basAh'
    get_with_context_result_0 = None
    list_0 = [plugin_load_context_0, str_0]
    var_1 = module_0.get_shell_plugin(get_with_context_result_0, list_0)

def test_case_9():
    str_0 = '/another/path/to/plugns'
    str_1 = [str_0, str_0]
    str_2 = 'module'
    var_0 = module_0.add_dirs_to_loader(str_2, str_1)

def test_case_10():
    str_0 = '~NL8\t 4'
    str_1 = 'D}IO'
    plugin_load_context_0 = module_0.PluginLoadContext()
    bool_0 = True
    bool_1 = False
    tuple_0 = ()
    str_2 = '\tX'
    float_0 = -1994.8497
    jinja2_loader_0 = module_0.Jinja2Loader(tuple_0, str_2, plugin_load_context_0, float_0)
    str_3 = '|F1#UrQ)e9\x0cPf!'
    dict_0 = {bool_1: str_0, bool_1: str_3}
    plugin_loader_0 = module_0.PluginLoader(bool_1, jinja2_loader_0, str_3, dict_0)
    plugin_loader_1 = module_0.PluginLoader(str_1, plugin_load_context_0, bool_0, plugin_load_context_0, plugin_loader_0)
    var_0 = plugin_loader_1.add_directory(str_0)

def test_case_11():
    str_0 = 'a'
    int_0 = -348
    dict_0 = {str_0: int_0, int_0: int_0}
    plugin_load_context_0 = module_0.PluginLoadContext()
    var_0 = plugin_load_context_0.record_deprecation(int_0, dict_0, str_0)

def test_case_12():
    plugin_load_context_0 = module_0.PluginLoadContext()
    int_0 = -330
    str_0 = '__init__'
    bytes_0 = None
    var_0 = module_0.get_shell_plugin(bytes_0, str_0)
    str_1 = 'Z4eH$LLz%}[&~cHhaw'
    plugin_loader_0 = module_0.PluginLoader(str_0, int_0, str_1, str_1)
    float_0 = 2.0
    var_1 = plugin_loader_0.has_plugin(float_0, str_0)

def test_case_13():
    plugin_load_context_0 = module_0.PluginLoadContext()
    var_0 = module_0.add_all_plugin_dirs(plugin_load_context_0)
    str_0 = 'sh'
    var_1 = module_0.get_shell_plugin(str_0)

def test_case_14():
    plugin_load_context_0 = module_0.PluginLoadContext()
    var_0 = module_0.add_all_plugin_dirs(plugin_load_context_0)
    get_with_context_result_0 = None
    str_0 = 'a'
    bytes_0 = None
    var_1 = module_0.get_shell_plugin(bytes_0, str_0)
    dict_0 = {str_0: get_with_context_result_0, str_0: var_1}
    str_1 = '+<P?Gq$hh'
    int_0 = 353
    str_2 = 'auf\n;'
    str_3 = 'Z4eH$LLz%}[&~cHhaw'
    plugin_loader_0 = module_0.PluginLoader(str_1, int_0, str_2, str_3)
    var_2 = plugin_loader_0.has_plugin(dict_0)
    float_0 = 2.0
    dict_1 = {}
    bool_0 = False
    plugin_loader_1 = module_0.PluginLoader(float_0, dict_1, plugin_load_context_0, bool_0)
    list_0 = []
    var_3 = plugin_loader_0.__setstate__(dict_1)
    bool_1 = True
    set_0 = {var_1, var_1, get_with_context_result_0}
    float_1 = -980.6
    float_2 = -149.86
    plugin_load_context_1 = None
    int_1 = -649
    str_4 = '/pynguin/\udcfbW\udcbe[-\udca3X\udcd3\x12W\udca1\udcd5\x07^\x03/windows'
    str_5 = 'Alp[l]Z|Q,pFR\x0bsd/~T'
    dict_2 = {str_0: bytes_0, str_4: plugin_load_context_0, str_5: set_0}
    jinja2_loader_0 = module_0.Jinja2Loader(float_2, get_with_context_result_0, plugin_load_context_1, int_1, dict_2)
    bytes_1 = b'\xc0k\x9c\x0e\xe3\xd3\x86\x17\x9c\x95'
    plugin_path_context_0 = module_0.PluginPathContext(jinja2_loader_0, bytes_1)
    jinja2_loader_1 = module_0.Jinja2Loader(plugin_load_context_0, plugin_path_context_0, get_with_context_result_0, str_5)
    plugin_loader_2 = module_0.PluginLoader(str_0, set_0, float_1, jinja2_loader_1)
    bool_2 = True
    jinja2_loader_2 = module_0.Jinja2Loader(bool_1, bool_1, plugin_loader_2, bool_2)
    var_4 = module_0.get_shell_plugin(list_0, jinja2_loader_2)

def test_case_15():
    plugin_load_context_0 = module_0.PluginLoadContext()
    var_0 = module_0.add_all_plugin_dirs(plugin_load_context_0)
    get_with_context_result_0 = None
    int_0 = -330
    str_0 = '__init__'
    bytes_0 = None
    var_1 = module_0.get_shell_plugin(bytes_0, str_0)
    dict_0 = {str_0: get_with_context_result_0, str_0: var_1}
    str_1 = '+<P?Gq$hh'
    str_2 = 'auf\n;'
    str_3 = 'Z4eH$LLz%}[&~cHhaw'
    plugin_loader_0 = module_0.PluginLoader(str_1, int_0, str_2, str_3)
    var_2 = plugin_loader_0.has_plugin(dict_0)
    list_0 = []
    bool_0 = True
    set_0 = {var_1, var_1, get_with_context_result_0}
    float_0 = -980.6
    float_1 = -149.86
    plugin_load_context_1 = None
    int_1 = -649
    str_4 = '/pynguin/\udcfbW\udcbe[-\udca3X\udcd3\x12W\udca1\udcd5\x07^\x03/windows'
    str_5 = 'Alp[l]Z|Q,pFR\x0bsd/~T'
    dict_1 = {str_0: bytes_0, str_4: plugin_load_context_0, str_5: set_0}
    jinja2_loader_0 = module_0.Jinja2Loader(float_1, get_with_context_result_0, plugin_load_context_1, int_1, dict_1)
    bytes_1 = b'\xc0k\x9c\x0e\xe3\xd3\x86\x17\x9c\x95'
    plugin_path_context_0 = module_0.PluginPathContext(jinja2_loader_0, bytes_1)
    jinja2_loader_1 = module_0.Jinja2Loader(plugin_load_context_0, plugin_path_context_0, get_with_context_result_0, str_5)
    plugin_loader_1 = module_0.PluginLoader(str_0, set_0, float_0, jinja2_loader_1)
    bool_1 = True
    jinja2_loader_2 = module_0.Jinja2Loader(bool_0, bool_0, plugin_loader_1, bool_1)
    var_3 = module_0.get_shell_plugin(list_0, jinja2_loader_2)

def test_case_16():
    plugin_load_context_0 = module_0.PluginLoadContext()
    var_0 = module_0.add_all_plugin_dirs(plugin_load_context_0)
    get_with_context_result_0 = None
    int_0 = -330
    str_0 = 'powershell'
    bytes_0 = None
    var_1 = module_0.get_shell_plugin(bytes_0, str_0)
    dict_0 = {str_0: get_with_context_result_0, str_0: var_1}
    str_1 = '+<P?Gq$hh'
    str_2 = 'auf\n;'
    str_3 = 'Z4eH$LLz%}[&~cHhaw'
    plugin_loader_0 = module_0.PluginLoader(str_1, int_0, str_2, str_3)
    var_2 = plugin_loader_0.has_plugin(dict_0)
    list_0 = []
    bool_0 = True
    set_0 = {var_1, var_1, get_with_context_result_0}
    float_0 = -980.6
    float_1 = -149.86
    plugin_load_context_1 = None
    int_1 = -649
    str_4 = '/pynguin/\udcfbW\udcbe[-\udca3X\udcd3\x12W\udca1\udcd5\x07^\x03/windows'
    str_5 = 'Alp[l]Z|Q,pFR\x0bsd/~T'
    dict_1 = {str_0: bytes_0, str_4: plugin_load_context_0, str_5: set_0}
    jinja2_loader_0 = module_0.Jinja2Loader(float_1, get_with_context_result_0, plugin_load_context_1, int_1, dict_1)
    bytes_1 = b'\xc0k\x9c\x0e\xe3\xd3\x86\x17\x9c\x95'
    plugin_path_context_0 = module_0.PluginPathContext(jinja2_loader_0, bytes_1)
    jinja2_loader_1 = module_0.Jinja2Loader(plugin_load_context_0, plugin_path_context_0, get_with_context_result_0, str_5)
    plugin_loader_1 = module_0.PluginLoader(str_0, set_0, float_0, jinja2_loader_1)
    bool_1 = True
    jinja2_loader_2 = module_0.Jinja2Loader(bool_0, bool_0, plugin_loader_1, bool_1)
    var_3 = module_0.get_shell_plugin(list_0, jinja2_loader_2)

def test_case_17():
    str_0 = '/@3pu\x0b?e\x0b9c1'
    bytes_0 = None
    str_1 = ''
    set_0 = {bytes_0, str_0, str_0}
    plugin_load_context_0 = module_0.PluginLoadContext()
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0]
    str_2 = '/pynguin/\udc92\udcb7A*\udc8b\udcbc>E\udc9b\udce7\r,(U>\udc83\udc8b\udc9e<\x03/windows'
    plugin_loader_0 = module_0.PluginLoader(plugin_load_context_0, tuple_0, list_0, str_2)
    var_0 = plugin_loader_0.has_plugin(set_0)
    list_1 = [str_0, bytes_0, bytes_0]
    dict_0 = {}
    int_0 = -846
    plugin_loader_1 = module_0.PluginLoader(str_0, list_1, dict_0, int_0, str_1)
    int_1 = -269
    plugin_path_context_0 = module_0.PluginPathContext(str_1, int_1)
    float_0 = 2593.0
    int_2 = -2443
    dict_1 = {str_0: str_1, str_1: str_0}
    plugin_load_context_1 = module_0.PluginLoadContext()
    var_1 = plugin_load_context_1.resolve(plugin_path_context_0, float_0, int_2, dict_1)
    var_2 = module_0.get_shell_plugin(bytes_0, str_0)

def test_case_18():
    plugin_load_context_0 = module_0.PluginLoadContext()
    str_0 = 'warning_text'
    str_1 = 'removal_date'
    str_2 = 'removal_version'
    str_3 = 'This plugin will be removed in a future release.'
    str_4 = '2022-12-31'
    str_5 = '3.0.0'
    str_6 = {str_0: str_3, str_1: str_4, str_2: str_5}
    str_7 = 'test_plugin'
    str_8 = 'test_collection'
    var_0 = plugin_load_context_0.record_deprecation(str_7, str_6, str_8)

def test_case_19():
    plugin_load_context_0 = module_0.PluginLoadContext()
    str_0 = 'test_plugin'
    str_1 = 'test.collection'
    str_2 = 'warning_text'
    str_3 = 'removal_version'
    str_4 = 'This plugin will be removed in a future release.'
    str_5 = '2023-12-31'
    str_6 = '3.0.0'
    str_7 = {str_2: str_4, str_3: str_5, str_3: str_6}
    var_0 = plugin_load_context_0.record_deprecation(str_0, str_7, str_1)
    var_1 = plugin_load_context_0.deprecation_warnings
    var_2 = len(var_1)

def test_case_20():
    plugin_load_context_0 = module_0.PluginLoadContext()
    str_0 = 'warning_text'
    str_1 = 'This plugin will be removed in a future release.'
    str_2 = '2022-12-31'
    str_3 = '3.0.0'
    str_4 = {str_0: str_1, str_1: str_2, str_3: str_3}
    str_5 = 'test_plugin'
    str_6 = 'test_collection'
    var_0 = plugin_load_context_0.record_deprecation(str_5, str_4, str_6)

def test_case_21():
    bytes_0 = b'3\x05V\x99)O\xa4\xd9\xdfc\xf2*\xcc9\x1bt\x0c\xcf'
    list_0 = [bytes_0]
    bytes_1 = b'0}3\x8f_\x98\xea'
    int_0 = -1980
    str_0 = 'sudo: a password is required'
    str_1 = 'S"=^Y\t-s4pLA`^3f;'
    dict_0 = {str_0: bytes_1, str_1: int_0, str_1: int_0}
    plugin_loader_0 = module_0.PluginLoader(bytes_1, int_0, dict_0, dict_0)
    var_0 = plugin_loader_0.has_plugin(list_0)
    plugin_load_context_0 = module_0.PluginLoadContext()
    var_1 = module_0.add_all_plugin_dirs(plugin_load_context_0)
    int_1 = -330
    bytes_2 = None
    var_2 = module_0.get_shell_plugin(bytes_2, str_0)
    str_2 = '+<P?Gq$hh'
    str_3 = 'auf\n;'
    str_4 = 'Z4eH$LLz%}[&~cHhaw'
    plugin_loader_1 = module_0.PluginLoader(str_2, int_1, str_3, str_4)
    str_5 = '/pynguin/\udcfbW\udcbe[-\udca3X\udcd3\x12W\udca1\udcd5\x07^\x03/windows'
    var_3 = plugin_loader_1.has_plugin(str_4, str_5)