# Automatically generated by Pynguin.
import isort.format as module_0
import pathlib as module_1
import typing as module_2

def test_case_0():
    try:
        str_0 = 'filename.py'
        bool_0 = module_0.ask_whether_to_apply_changes_to_file(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ' is not included in `sections` config option: '
        str_1 = module_0.format_natural(str_0)
        str_2 = 'S:q?VqMvo!)'
        str_3 = 'buck-out'
        colorama_printer_0 = module_0.ColoramaPrinter()
        colorama_printer_0.diff_line(str_3)
        list_0 = [str_2]
        str_4 = module_0.format_simplified(str_1)
        path_0 = module_1.Path()
        var_0 = module_0.show_unified_diff(file_input=str_1, file_output=str_0, file_path=path_0)
        basic_printer_0 = module_0.BasicPrinter(list_0)
        basic_printer_0.success(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'n\rC3+G6NKvOb =mclF '
        str_1 = 'node_modules'
        text_i_o_0 = module_2.TextIO()
        text_i_o_1 = text_i_o_0.__enter__()
        var_0 = module_0.show_unified_diff(file_input=str_0, file_output=str_1, file_path=text_i_o_1)
        str_2 = '/tmp/test.py'
        bool_0 = module_0.ask_whether_to_apply_changes_to_file(str_2)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'i5I[='
        str_1 = '\nA{RDk'
        set_0 = None
        list_0 = [str_1]
        str_2 = '{'
        dict_0 = {str_1: set_0, str_1: str_0, str_0: list_0, str_2: list_0}
        basic_printer_0 = module_0.BasicPrinter(dict_0)
        basic_printer_0.diff_line(str_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = ' is not n.luded in `sectins` config option: '
        str_1 = module_0.format_natural(str_0)
        str_2 = 'S:q?VqMvo!)'
        str_3 = 'buck-out'
        colorama_printer_0 = module_0.ColoramaPrinter()
        colorama_printer_1 = module_0.ColoramaPrinter()
        colorama_printer_1.diff_line(str_3)
        str_4 = module_0.format_simplified(str_1)
        path_0 = module_1.Path()
        text_i_o_0 = module_2.TextIO()
        text_i_o_1 = text_i_o_0.__enter__()
        bool_0 = True
        var_0 = module_0.show_unified_diff(file_input=str_1, file_output=str_2, file_path=path_0, output=text_i_o_1, color_output=bool_0)
        str_5 = None
        basic_printer_0 = module_0.BasicPrinter()
        str_6 = '6}7q!MlVA'
        var_1 = module_0.show_unified_diff(file_input=str_3, file_output=str_6, file_path=path_0, output=text_i_o_1, color_output=bool_0)
        bool_1 = module_0.ask_whether_to_apply_changes_to_file(str_5)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'Given a string value that represents True or False, returns the Boolean equivalent.\n    Heavily inspired from distutils strtobool.\n    '
        str_1 = module_0.format_natural(str_0)
        str_2 = 'S:q?Vqvo!)'
        str_3 = 'buck-out'
        colorama_printer_0 = module_0.ColoramaPrinter()
        colorama_printer_0.diff_line(str_3)
        str_4 = module_0.format_simplified(str_1)
        path_0 = module_1.Path()
        str_5 = '~:gHmz%U5U\\\x0c'
        basic_printer_0 = module_0.BasicPrinter()
        str_6 = 'R'
        str_7 = module_0.format_simplified(str_6)
        dict_0 = {}
        path_1 = module_1.Path(**dict_0)
        basic_printer_1 = module_0.BasicPrinter()
        basic_printer_0.success(str_2)
        str_8 = module_0.format_natural(str_1)
        str_9 = None
        bool_0 = True
        var_0 = module_0.show_unified_diff(file_input=str_5, file_output=str_9, file_path=path_1, color_output=bool_0)
    except BaseException:
        pass