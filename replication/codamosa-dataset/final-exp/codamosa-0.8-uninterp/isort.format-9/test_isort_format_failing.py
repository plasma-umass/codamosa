# Automatically generated by Pynguin.
import isort.format as module_0
import typing as module_1
import pathlib as module_2

def test_case_0():
    try:
        colorama_printer_0 = module_0.ColoramaPrinter()
        str_0 = 'fS.'
        str_1 = module_0.format_natural(str_0)
        str_2 = '2\r8zy({Eh@<.cc"c\r'
        colorama_printer_0.diff_line(str_2)
        str_3 = colorama_printer_0.style_text(str_1, str_1)
        list_0 = []
        text_i_o_0 = module_1.TextIO(*list_0)
        text_i_o_1 = text_i_o_0.__enter__()
        text_i_o_2 = text_i_o_1.__enter__()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'p'
        str_1 = module_0.format_simplified(str_0)
        str_2 = None
        set_0 = None
        var_0 = module_0.show_unified_diff(file_input=str_2, file_output=str_0, file_path=set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'l%y'
        path_0 = module_2.Path()
        text_i_o_0 = module_1.TextIO()
        text_i_o_1 = text_i_o_0.__enter__()
        var_0 = module_0.show_unified_diff(file_input=str_0, file_output=str_0, file_path=path_0, output=text_i_o_1)
        text_i_o_2 = text_i_o_1.__enter__()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'Q\'-l&I\x0cx(m"8WQRl\'_>'
        bool_0 = module_0.ask_whether_to_apply_changes_to_file(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '{fM{PX~\x0b3(:'
        str_1 = 'U6j{\nSHh(\rUmZ|eo\n'
        str_2 = module_0.format_natural(str_0)
        str_3 = '\roA2i><IN+pI%<\n'
        list_0 = [str_1, str_0]
        var_0 = module_0.show_unified_diff(file_input=str_3, file_output=str_0, file_path=list_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '6L6'
        str_1 = module_0.format_natural(str_0)
        text_i_o_0 = module_1.TextIO()
        colorama_printer_0 = module_0.ColoramaPrinter(text_i_o_0)
        text_i_o_1 = text_i_o_0.__enter__()
        bool_0 = True
        var_0 = module_0.create_terminal_printer(bool_0)
        colorama_printer_1 = module_0.ColoramaPrinter(text_i_o_1)
        str_2 = None
        bool_1 = module_0.ask_whether_to_apply_changes_to_file(str_2)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'import os, sys, re'
        str_1 = module_0.format_simplified(str_0)
        str_2 = 'import os , sys.path, re'
        str_3 = module_0.format_simplified(str_2)
        str_4 = 'import os , sys.path as path, re'
        str_5 = module_0.format_simplified(str_4)
        str_6 = module_0.format_simplified(str_4)
        str_7 = 'import os , sys . path as path, re'
        str_8 = module_0.format_simplified(str_7)
        str_9 = 'from sys import path'
        str_10 = module_0.format_simplified(str_9)
        str_11 = '--nsl'
        bool_0 = module_0.ask_whether_to_apply_changes_to_file(str_11)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'from foo import bar'
        str_1 = module_0.format_natural(str_0)
        str_2 = "?*s=JiT6=u',"
        bool_0 = module_0.ask_whether_to_apply_changes_to_file(str_2)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'from foo import bar'
        str_1 = module_0.format_natural(str_0)
        str_2 = 'import foo'
        str_3 = module_0.format_natural(str_2)
        bool_0 = module_0.ask_whether_to_apply_changes_to_file(str_3)
    except BaseException:
        pass