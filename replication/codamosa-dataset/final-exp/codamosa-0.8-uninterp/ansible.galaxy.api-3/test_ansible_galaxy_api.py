# Automatically generated by Pynguin.
import ansible.galaxy.api as module_0
import urllib.error as module_1

def test_case_0():
    pass

def test_case_1():
    bool_0 = True
    var_0 = module_0.is_rate_limit_exception(bool_0)

def test_case_2():
    str_0 = 'LnC'
    var_0 = module_0.get_cache_id(str_0)

def test_case_3():
    str_0 = 'http\x0b://example.com/galaxy/api/v3/s*rvers'
    int_0 = 403
    var_0 = {}
    h_t_t_p_error_0 = module_1.HTTPError(str_0, int_0, str_0, var_0, str_0)
    galaxy_error_0 = module_0.GalaxyError(h_t_t_p_error_0, str_0)

def test_case_4():
    bool_0 = True
    dict_0 = {}
    galaxy_a_p_i_0 = module_0.GalaxyAPI(bool_0, bool_0, dict_0)

def test_case_5():
    str_0 = 'luserdel'
    list_0 = [str_0, str_0, str_0, str_0]
    str_1 = 'Funtoo'
    str_2 = 'KEI(<'
    dict_0 = {str_0: str_0, str_1: str_0, str_2: str_2, str_2: list_0}
    dict_1 = {str_0: str_1}
    galaxy_a_p_i_0 = module_0.GalaxyAPI(str_0, list_0, dict_0, str_2, dict_1)
    var_0 = galaxy_a_p_i_0.__repr__()

def test_case_6():
    bool_0 = True
    dict_0 = {}
    galaxy_a_p_i_0 = module_0.GalaxyAPI(bool_0, bool_0, dict_0)
    var_0 = galaxy_a_p_i_0.__unicode__()

def test_case_7():
    str_0 = ''
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    float_0 = -95.88980418391408
    bytes_0 = b'\xb4\x04\xa1'
    galaxy_a_p_i_0 = module_0.GalaxyAPI(dict_0, str_0, float_0, str_0, bytes_0)
    var_0 = galaxy_a_p_i_0.__lt__(str_0)

def test_case_8():
    str_0 = 'G~\x0bUGO#=u8kR"'
    collection_metadata_0 = None
    float_0 = 1.5
    list_0 = []
    bytes_0 = b'K\xc82\xbd\xa4,\\X'
    set_0 = {collection_metadata_0, float_0, bytes_0, float_0}
    float_1 = -4119.765
    float_2 = 611.0
    float_3 = -3604.29
    list_1 = [float_3, float_2, float_0]
    str_1 = '_]rW_g\r!I;:1\n\x0bw#'
    str_2 = '-mbsf\x0cuN*~eBec'
    dict_0 = {str_1: str_0, str_2: collection_metadata_0, str_0: list_0, str_0: float_3}
    bool_0 = True
    galaxy_a_p_i_0 = module_0.GalaxyAPI(set_0, float_1, float_2, float_3, list_1, dict_0, bool_0, bool_0, set_0)

def test_case_9():
    str_0 = 'Cb=\to'
    int_0 = 403
    var_0 = {}
    h_t_t_p_error_0 = module_1.HTTPError(str_0, int_0, str_0, var_0, str_0)
    galaxy_error_0 = module_0.GalaxyError(h_t_t_p_error_0, str_0)

def test_case_10():
    str_0 = 'https://localhost:443/api/v2/'
    var_0 = module_0.get_cache_id(str_0)

def test_case_11():
    str_0 = 'https://localhost:44$/api/v2/'
    var_0 = module_0.get_cache_id(str_0)

def test_case_12():
    list_0 = []
    bytes_0 = b'\x95\x0f\xb1\xfb^,\x81\xb9\x83\xf2\x12'
    list_1 = [bytes_0]
    float_0 = -1812.81128
    list_2 = [bytes_0, list_1, list_1, bytes_0, list_1]
    str_0 = 'hi_id'
    galaxy_a_p_i_0 = module_0.GalaxyAPI(list_1, float_0, list_2, str_0)
    var_0 = module_0.get_cache_id(str_0)
    var_1 = galaxy_a_p_i_0.__lt__(list_0)
    var_2 = galaxy_a_p_i_0.__unicode__()
    str_1 = 'https://example.com/galaxy/api/v3/servers'
    int_0 = 403
    bytes_1 = b'p'
    var_3 = galaxy_a_p_i_0.__repr__()
    bool_0 = True
    bool_1 = False
    set_0 = set()
    h_t_t_p_error_0 = module_1.HTTPError(bytes_1, bool_0, bool_1, float_0, set_0)
    bytes_2 = b'r\x98\xe1\xca\xf3\xa9\x94\xc5\x07KJ\x96\xbe\x03\xd2\x13r-=\xa2'
    tuple_0 = (h_t_t_p_error_0, bytes_2)
    var_4 = module_0.cache_lock(tuple_0)
    h_t_t_p_error_1 = module_1.HTTPError(str_1, int_0, str_1, h_t_t_p_error_0, str_1)
    galaxy_error_0 = module_0.GalaxyError(h_t_t_p_error_1, set_0)
    var_5 = module_0.is_rate_limit_exception(galaxy_error_0)
    galaxy_error_1 = module_0.GalaxyError(h_t_t_p_error_1, tuple_0)