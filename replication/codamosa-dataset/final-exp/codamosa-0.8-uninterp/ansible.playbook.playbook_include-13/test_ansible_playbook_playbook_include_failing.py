# Automatically generated by Pynguin.
import ansible.playbook.playbook_include as module_0

def test_case_0():
    try:
        playbook_include_0 = module_0.PlaybookInclude()
        var_0 = playbook_include_0.load(playbook_include_0, playbook_include_0)
    except BaseException:
        pass

def test_case_1():
    try:
        playbook_include_0 = module_0.PlaybookInclude()
        dict_0 = {}
        var_0 = playbook_include_0.load_data(dict_0, playbook_include_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'p[$ 6\tr]>'
        var_0 = dict(import_playbook=str_0, vars=str_0)
        playbook_include_0 = module_0.PlaybookInclude()
        var_1 = playbook_include_0.preprocess_data(var_0)
    except BaseException:
        pass

def test_case_3():
    try:
        playbook_include_0 = module_0.PlaybookInclude()
        dict_0 = {playbook_include_0: playbook_include_0, playbook_include_0: playbook_include_0}
        int_0 = 5
        bytes_0 = b'\xe0\xba2\xc3_=\x0c^\xbb\x14/\x8eed\xd2\xd4]'
        var_0 = playbook_include_0.load_data(dict_0, int_0, bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        playbook_include_0 = module_0.PlaybookInclude()
        int_0 = -2245
        var_0 = playbook_include_0.load_data(dict_0, playbook_include_0, int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'path/to/pb1.yml'
        int_0 = 1
        var_0 = dict(import_playbook=str_0, vars=int_0)
        playbook_include_0 = module_0.PlaybookInclude()
        var_1 = playbook_include_0.preprocess_data(var_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'path/to/pb1.yml'
        int_0 = 2
        var_0 = dict(one=str_0, two=int_0)
        var_1 = dict(import_playbook=var_0, vars=str_0)
        playbook_include_0 = module_0.PlaybookInclude()
        playbook_include_1 = module_0.PlaybookInclude()
        var_2 = playbook_include_0.preprocess_data(var_1)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = ''
        int_0 = 26
        var_0 = dict(one=str_0, two=int_0)
        var_1 = dict(import_playbook=str_0, vars=var_0)
        playbook_include_0 = module_0.PlaybookInclude()
        var_2 = playbook_include_0.preprocess_data(var_1)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'test.yam'
        var_0 = dict(import_playbook=str_0)
        playbook_include_0 = module_0.PlaybookInclude()
        str_1 = '/home/ansible/playbooks/'
        var_1 = playbook_include_0.load_data(var_0, str_1)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '\x0c/N+X=?4L#-u}FWh'
        var_0 = dict(import_playbook=str_0)
        playbook_include_0 = module_0.PlaybookInclude()
        str_1 = '/home/ansible/playbooks/'
        var_1 = playbook_include_0.load_data(var_0, str_1)
    except BaseException:
        pass