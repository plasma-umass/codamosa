# Automatically generated by Pynguin.
import ansible.modules.apt_repository as module_0

def test_case_0():
    pass

def test_case_1():
    dict_0 = None
    var_0 = module_0.main()
    dict_1 = {}
    ubuntu_sources_list_0 = module_0.UbuntuSourcesList(dict_1)
    str_0 = 'zRSPavJ'
    sources_list_0 = module_0.SourcesList(str_0)
    var_1 = sources_list_0.save()
    sources_list_1 = module_0.SourcesList(ubuntu_sources_list_0)
    var_2 = sources_list_1.save()
    float_0 = -167.788129
    sources_list_2 = module_0.SourcesList(float_0)
    str_1 = "o3V%mEP*m#''llj"
    ubuntu_sources_list_1 = module_0.UbuntuSourcesList(str_1)
    str_2 = 'o]z7@jKjO'
    var_3 = sources_list_2.dump()
    bytes_0 = b'\xd3\x1e\x18\xbe\x95\x9d'
    dict_2 = {str_2: bytes_0}
    list_0 = [float_0, bytes_0, sources_list_2]
    invalid_source_0 = module_0.InvalidSource(*list_0)
    tuple_0 = (str_1, ubuntu_sources_list_1, dict_2, invalid_source_0)
    bool_0 = False
    ubuntu_sources_list_2 = module_0.UbuntuSourcesList(bool_0)
    var_4 = ubuntu_sources_list_2.remove_source(tuple_0)
    var_5 = sources_list_2.remove_source(dict_0)