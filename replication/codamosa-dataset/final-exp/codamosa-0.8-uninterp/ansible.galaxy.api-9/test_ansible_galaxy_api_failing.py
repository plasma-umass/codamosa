# Automatically generated by Pynguin.
import ansible.galaxy.api as module_0

def test_case_0():
    try:
        bool_0 = False
        float_0 = -1762.03884
        galaxy_error_0 = module_0.GalaxyError(bool_0, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = -4630.222
        str_0 = '3w#:6xjt'
        str_1 = ''
        str_2 = '@M'
        dict_0 = {str_0: str_1, str_2: str_1}
        list_0 = [str_1, str_2, str_0, dict_0]
        bool_0 = False
        collection_version_metadata_0 = module_0.CollectionVersionMetadata(dict_0, str_0, list_0, float_0, float_0, bool_0)
        str_3 = 'N(M2'
        float_1 = -181.75192
        galaxy_error_0 = module_0.GalaxyError(str_3, float_1)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = ''
        var_0 = module_0.is_rate_limit_exception(str_0)
        list_0 = [str_0]
        float_0 = 2475.0
        str_1 = 'crDEnWXQ\n>c'
        dict_0 = {}
        str_2 = 'j6@E?L'
        collection_metadata_0 = None
        tuple_0 = ()
        collection_version_metadata_0 = module_0.CollectionVersionMetadata(dict_0, list_0, str_2, collection_metadata_0, collection_metadata_0, tuple_0)
        int_0 = 2211
        set_0 = {int_0, str_2, float_0}
        bytes_0 = b''
        str_3 = 'SLUi{1+O;KTy-h/Gg'
        str_4 = 'W*Yg}\rd_'
        str_5 = 'bg*,X@FZk7,gFYD'
        dict_1 = {str_3: str_1, str_4: collection_version_metadata_0, str_1: collection_metadata_0, str_5: str_5}
        galaxy_a_p_i_0 = module_0.GalaxyAPI(collection_metadata_0, set_0, bytes_0, collection_version_metadata_0, bytes_0, dict_1)
        bool_0 = False
        galaxy_a_p_i_1 = module_0.GalaxyAPI(str_1, collection_version_metadata_0, int_0, collection_version_metadata_0, galaxy_a_p_i_0, set_0, str_5, list_0, set_0, bool_0)
        tuple_1 = (list_0, float_0, galaxy_a_p_i_1, galaxy_a_p_i_1)
        bool_1 = True
        galaxy_a_p_i_2 = module_0.GalaxyAPI(tuple_1, list_0, collection_metadata_0, list_0, galaxy_a_p_i_1, bool_1)
        list_1 = [bytes_0, tuple_0, tuple_0, str_4]
        var_1 = module_0.cache_lock(list_1)
        galaxy_error_0 = None
        galaxy_error_1 = module_0.GalaxyError(set_0, galaxy_error_0)
    except BaseException:
        pass

def test_case_3():
    try:
        list_0 = []
        float_0 = 2475.0
        str_0 = 'crD>nWXQ\n>Sc'
        tuple_0 = (list_0,)
        var_0 = module_0.is_rate_limit_exception(tuple_0)
        dict_0 = {}
        str_1 = 'j6@E?L'
        collection_metadata_0 = None
        tuple_1 = ()
        collection_version_metadata_0 = module_0.CollectionVersionMetadata(dict_0, list_0, str_1, collection_metadata_0, collection_metadata_0, tuple_1)
        int_0 = 2211
        set_0 = {int_0, str_1, float_0}
        bytes_0 = b''
        str_2 = 'W*h(}\rd_'
        str_3 = 'bg*,X@FZk7,gFYD'
        dict_1 = {str_3: str_0, str_2: collection_version_metadata_0, str_0: collection_metadata_0, str_3: str_3}
        galaxy_a_p_i_0 = module_0.GalaxyAPI(collection_metadata_0, set_0, bytes_0, collection_version_metadata_0, bytes_0, dict_1)
        bool_0 = False
        galaxy_a_p_i_1 = module_0.GalaxyAPI(str_0, collection_version_metadata_0, int_0, collection_version_metadata_0, galaxy_a_p_i_0, set_0, str_3, list_0, set_0, bool_0)
        tuple_2 = (list_0, float_0, galaxy_a_p_i_1, galaxy_a_p_i_1)
        var_1 = module_0.get_cache_id(collection_metadata_0)
        bool_1 = False
        galaxy_a_p_i_2 = module_0.GalaxyAPI(tuple_2, list_0, collection_metadata_0, list_0, galaxy_a_p_i_1, bool_1)
        var_2 = galaxy_a_p_i_2.__repr__()
        var_3 = galaxy_a_p_i_2.__lt__(galaxy_a_p_i_0)
    except BaseException:
        pass