# Automatically generated by Pynguin.
import youtube_dl.postprocessor.metadatafromtitle as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'hy'
    str_1 = ':R(}>u$[\x0c'
    metadata_from_title_p_p_0 = module_0.MetadataFromTitlePP(str_0, str_1)
    var_0 = metadata_from_title_p_p_0.format_to_regex(str_0)

def test_case_2():
    str_0 = 'title'
    str_1 = {str_0: str_0}
    metadata_from_title_p_p_0 = module_0.MetadataFromTitlePP(str_1, str_0)
    var_0 = metadata_from_title_p_p_0.run(str_1)

def test_case_3():
    var_0 = None
    str_0 = '%(artist)s - %(title)s'
    metadata_from_title_p_p_0 = module_0.MetadataFromTitlePP(var_0, str_0)
    var_1 = metadata_from_title_p_p_0.format_to_regex(str_0)
    str_1 = '%(title)s - %(artist)s'
    var_2 = metadata_from_title_p_p_0.format_to_regex(str_1)