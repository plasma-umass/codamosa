# Automatically generated by Pynguin.
import ansible.galaxy.api as module_0
import urllib.error as module_1

def test_case_0():
    try:
        float_0 = -2127.64881
        float_1 = -3436.09323
        dict_0 = {float_0: float_0, float_0: float_1}
        galaxy_error_0 = module_0.GalaxyError(float_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'http://example.com'
        bytes_0 = b',Z\x08\x93#@M\x16\xbc\xf9\xaa='
        list_0 = [str_0, bytes_0, str_0, bytes_0]
        var_0 = module_0.is_rate_limit_exception(list_0)
        str_1 = '~\tAcCUh/L0Pt5W-n3s('
        set_0 = {bytes_0}
        list_1 = [str_1, set_0, set_0]
        dict_0 = {}
        galaxy_a_p_i_0 = module_0.GalaxyAPI(set_0, bytes_0, str_1, list_1, dict_0)
        int_0 = 500
        str_2 = 'Internal Server Error'
        set_1 = set()
        var_1 = galaxy_a_p_i_0.__lt__(set_1)
        h_t_t_p_error_0 = module_1.HTTPError(str_0, int_0, str_2, bytes_0, bytes_0)
        str_3 = 'HTTP rror'
        galaxy_error_0 = module_0.GalaxyError(h_t_t_p_error_0, str_3)
        var_2 = galaxy_a_p_i_0.__repr__()
        var_3 = galaxy_a_p_i_0.__lt__(galaxy_a_p_i_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'http://example.com'
        bytes_0 = b',Z\x08\x93#@M\x16\xbc\xf9\xaa='
        list_0 = [str_0, bytes_0, str_0, bytes_0]
        var_0 = module_0.is_rate_limit_exception(list_0)
        str_1 = '~\tAcCUh/L0Pt5W-n3s('
        set_0 = {bytes_0}
        list_1 = [str_1, set_0, set_0]
        dict_0 = {}
        galaxy_a_p_i_0 = module_0.GalaxyAPI(set_0, bytes_0, str_1, list_1, dict_0)
        int_0 = 500
        str_2 = 'In3ernal Server Error'
        h_t_t_p_error_0 = module_1.HTTPError(str_0, int_0, str_2, bytes_0, bytes_0)
        str_3 = 'HTTP rror'
        galaxy_error_0 = module_0.GalaxyError(h_t_t_p_error_0, str_3)
        var_1 = galaxy_error_0.url
        var_2 = galaxy_a_p_i_0.__lt__(str_1)
        var_3 = galaxy_a_p_i_0.__unicode__()
        var_4 = galaxy_a_p_i_0.__lt__(galaxy_a_p_i_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b',Z\x08\x93#@M\x16\xbc\xf9\xaa='
        str_0 = '~\tAcCUh/L0Pt5W-n3s('
        set_0 = {bytes_0}
        list_0 = [str_0, set_0, set_0]
        dict_0 = {}
        galaxy_a_p_i_0 = module_0.GalaxyAPI(set_0, bytes_0, str_0, list_0, dict_0)
        var_0 = galaxy_a_p_i_0.__lt__(str_0)
        var_1 = galaxy_a_p_i_0.__lt__(galaxy_a_p_i_0)
    except BaseException:
        pass

def test_case_4():
    try:
        tuple_0 = ()
        collection_version_metadata_0 = None
        dict_0 = {tuple_0: tuple_0}
        var_0 = module_0.is_rate_limit_exception(tuple_0)
        int_0 = -505
        var_1 = module_0.is_rate_limit_exception(int_0)
        str_0 = '%fRZN%;Mxdbc89'
        bool_0 = False
        bytes_0 = b'\xb7ucf\x16\xab'
        collection_version_metadata_1 = module_0.CollectionVersionMetadata(dict_0, dict_0, str_0, bool_0, bytes_0, dict_0)
        str_1 = 'O+X?'
        bytes_1 = b'\x82\x1fJ\xb7k\xf1M`\xd4\x15\xa6'
        list_0 = [tuple_0, str_0, bytes_1, bool_0]
        dict_1 = {str_0: bool_0, str_1: dict_0, str_0: str_0}
        galaxy_a_p_i_0 = module_0.GalaxyAPI(dict_1, int_0, collection_version_metadata_1, tuple_0, str_1, dict_1)
        list_1 = [tuple_0, bytes_1, tuple_0, collection_version_metadata_0]
        set_0 = {collection_version_metadata_0}
        galaxy_a_p_i_1 = module_0.GalaxyAPI(list_0, dict_1, galaxy_a_p_i_0, list_0, tuple_0, list_1, set_0, collection_version_metadata_0, bytes_0)
        var_2 = galaxy_a_p_i_0.__lt__(galaxy_a_p_i_1)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'g'
        str_1 = '#[yK1"'
        tuple_0 = ()
        var_0 = module_0.get_cache_id(tuple_0)
        collection_version_metadata_0 = None
        dict_0 = {tuple_0: var_0}
        var_1 = module_0.is_rate_limit_exception(tuple_0)
        str_2 = '%fRZN%;Mxdbc89'
        bool_0 = True
        bytes_0 = b'\xb7ucf\x16\xab'
        collection_version_metadata_1 = module_0.CollectionVersionMetadata(dict_0, dict_0, str_2, bool_0, bytes_0, dict_0)
        bytes_1 = b'\x82\x1fJ\xb7k\xf1M\xff\xae\x15\xa6'
        list_0 = [tuple_0, str_2, bytes_1, bool_0]
        dict_1 = {str_2: bool_0, str_1: dict_0, str_2: str_2}
        int_0 = -2339
        galaxy_a_p_i_0 = module_0.GalaxyAPI(dict_1, int_0, collection_version_metadata_1, tuple_0, str_0, dict_1)
        list_1 = [tuple_0, bytes_1, tuple_0, collection_version_metadata_0]
        set_0 = {collection_version_metadata_0}
        galaxy_a_p_i_1 = module_0.GalaxyAPI(list_0, dict_1, galaxy_a_p_i_0, list_0, tuple_0, list_1, set_0, bytes_0, bytes_0)
        var_2 = galaxy_a_p_i_1.__lt__(str_2)
        var_3 = galaxy_a_p_i_0.__lt__(galaxy_a_p_i_1)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = 500
        str_0 = 'Internal eervew Error'
        h_t_t_p_error_0 = module_1.HTTPError(str_0, int_0, str_0, str_0, str_0)
        str_1 = "'2t_>`;0]'px-9BJTF"
        galaxy_error_0 = module_0.GalaxyError(h_t_t_p_error_0, str_1)
        var_0 = str_0.message
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'http://github.com'
        int_0 = 500
        str_1 = 'server error'
        var_0 = None
        h_t_t_p_error_0 = module_1.HTTPError(str_0, int_0, str_1, var_0, var_0)
        galaxy_error_0 = module_0.GalaxyError(h_t_t_p_error_0, str_0)
    except BaseException:
        pass