# Automatically generated by Pynguin.
import builtins as module_0
import isort.exceptions as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = ']Op|df\x0b{'
    exception_0 = module_0.Exception()
    literal_parsing_failure_0 = module_1.LiteralParsingFailure(str_0, exception_0)
    str_1 = 'Sorts the literal present within the provided code against the provided sort type,\n    returning the sorted representation of the source code.\n    '
    formatting_plugin_does_not_exist_0 = module_1.FormattingPluginDoesNotExist(str_1)
    invalid_settings_path_0 = module_1.InvalidSettingsPath(str_0)
    str_2 = 'X_DY='
    existing_syntax_errors_0 = module_1.ExistingSyntaxErrors(str_2)

def test_case_2():
    str_0 = None
    existing_syntax_errors_0 = module_1.ExistingSyntaxErrors(str_0)
    assignments_format_mismatch_0 = module_1.AssignmentsFormatMismatch(str_0)
    str_1 = 'qs'
    assignments_format_mismatch_1 = module_1.AssignmentsFormatMismatch(str_1)

def test_case_3():
    str_0 = 'bHJ'
    introduced_syntax_errors_0 = module_1.IntroducedSyntaxErrors(str_0)
    missing_section_0 = module_1.MissingSection(str_0, str_0)

def test_case_4():
    str_0 = 'ttI'
    file_skip_setting_0 = module_1.FileSkipSetting(str_0)

def test_case_5():
    str_0 = 'Q{\t[?tsp]\n4]8}w'
    str_1 = ')~6aB"5D"lt::*g\r$r\\@'
    str_2 = 'oF1Z`\x0cKoU\r\r$AL.1dp'
    str_3 = '\n`Cg*T>a `zrZJW|J}'
    str_4 = 'cfmfile'
    invalid_settings_path_0 = module_1.InvalidSettingsPath(str_4)
    missing_section_0 = module_1.MissingSection(str_2, str_3)
    file_skip_setting_0 = module_1.FileSkipSetting(str_1)
    file_skip_comment_0 = module_1.FileSkipComment(str_0)
    file_skip_comment_1 = module_1.FileSkipComment(str_0)

def test_case_6():
    str_0 = 't'
    str_1 = 'V'
    existing_syntax_errors_0 = module_1.ExistingSyntaxErrors(str_1)
    assignments_format_mismatch_0 = module_1.AssignmentsFormatMismatch(str_0)
    str_2 = '\\^5+*'
    profile_does_not_exist_0 = module_1.ProfileDoesNotExist(str_2)
    unsupported_encoding_0 = module_1.UnsupportedEncoding(str_0)
    i_sort_error_0 = module_1.ISortError()

def test_case_7():
    str_0 = '\rz.,t@\tY'
    str_1 = None
    type_0 = None
    literal_sort_type_mismatch_0 = module_1.LiteralSortTypeMismatch(type_0, type_0)
    exception_0 = module_0.Exception()
    literal_parsing_failure_0 = module_1.LiteralParsingFailure(str_1, exception_0)
    profile_does_not_exist_0 = module_1.ProfileDoesNotExist(str_0)
    formatting_plugin_does_not_exist_0 = module_1.FormattingPluginDoesNotExist(str_1)
    profile_does_not_exist_1 = module_1.ProfileDoesNotExist(str_0)

def test_case_8():
    str_0 = 'qs'
    assignments_format_mismatch_0 = module_1.AssignmentsFormatMismatch(str_0)

def test_case_9():
    str_0 = 'force_to_top'
    str_1 = 'value'
    str_2 = 'source'
    str_3 = 'test'
    str_4 = 'test2'
    str_5 = {str_1: str_3, str_2: str_4}
    str_6 = {str_0: str_5}
    unsupported_settings_0 = module_1.UnsupportedSettings(str_6)