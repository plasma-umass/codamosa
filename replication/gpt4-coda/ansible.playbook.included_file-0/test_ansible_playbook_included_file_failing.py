# Automatically generated by Pynguin.
import ansible.playbook.included_file as module_0
import ansible.playbook.task_include as module_1

def test_case_0():
    try:
        int_0 = 398
        bytes_0 = b'e\xb4\xdb\xfe\x05\x13'
        float_0 = -40.57
        bool_0 = False
        str_0 = 'l%6{#.*05lK?[la'
        included_file_0 = module_0.IncludedFile(bytes_0, float_0, bool_0, str_0)
        var_0 = included_file_0.__eq__(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -1421
        tuple_0 = (int_0,)
        list_0 = [int_0, int_0, int_0]
        set_0 = set()
        int_1 = 250000
        str_0 = 'zq~'
        str_1 = ' returns the value of last ini entry found '
        included_file_0 = module_0.IncludedFile(set_0, int_1, str_0, str_1)
        var_0 = included_file_0.process_include_results(tuple_0, list_0, list_0, list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = -4314
        task_include_0 = module_1.TaskInclude()
        float_0 = 0.5
        dict_0 = {}
        included_file_0 = module_0.IncludedFile(float_0, dict_0, dict_0, task_include_0)
        str_0 = ''
        set_0 = {float_0, int_0}
        str_1 = '\t-wT2,@O1[;\\\t8wvMNIg'
        var_0 = included_file_0.process_include_results(str_0, int_0, set_0, str_1)
        var_1 = included_file_0.process_include_results(str_1, int_0, task_include_0, int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '7A_=&Y@IP7L'
        str_1 = '.T*U}jDZ~b`mR$c8'
        float_0 = 3442.89
        bytes_0 = b'i\x13m\x13\x81\x91Tn\xd6G\x84)\x81b\x18\xebs_U'
        str_2 = '+dr#6rF6 V'
        bool_0 = True
        str_3 = 'No variable found with this name: %s'
        bool_1 = None
        float_1 = 4097.578
        tuple_0 = (float_1,)
        int_0 = 5923
        dict_0 = {str_3: str_3}
        set_0 = {float_0, tuple_0}
        bool_2 = True
        included_file_0 = module_0.IncludedFile(dict_0, bool_2, dict_0, bool_0, int_0)
        included_file_1 = module_0.IncludedFile(float_1, set_0, tuple_0, included_file_0, included_file_0)
        int_1 = None
        bytes_1 = b'+*eG{\x84\xd7\xc9e\x0e\xe7\x100\xb3\x8eJY0\xa6\xf5'
        str_4 = 'Zc)Fs`0'
        included_file_2 = module_0.IncludedFile(included_file_1, int_1, bytes_1, str_4, bytes_1)
        int_2 = -391
        included_file_3 = module_0.IncludedFile(int_2, dict_0, bool_0, tuple_0)
        var_0 = included_file_3.add_host(included_file_3)
        str_5 = 'R2XjKgx(|?P'
        var_1 = included_file_1.__eq__(included_file_0)
        included_file_4 = module_0.IncludedFile(dict_0, tuple_0, str_5, dict_0)
        var_2 = included_file_4.add_host(int_0)
        list_0 = [tuple_0, str_3, str_3, str_3]
        tuple_1 = (bool_1, tuple_0, list_0)
        int_3 = 389
        included_file_5 = module_0.IncludedFile(str_2, bool_0, str_3, tuple_1, included_file_0)
        included_file_6 = module_0.IncludedFile(bytes_0, included_file_5, dict_0, int_3)
        var_3 = included_file_6.process_include_results(str_0, str_1, float_0, list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        task_include_0 = module_1.TaskInclude()
        included_file_0 = None
        bool_0 = True
        int_0 = 1180
        dict_0 = {}
        tuple_0 = (int_0, dict_0)
        included_file_1 = module_0.IncludedFile(included_file_0, included_file_0, bool_0, tuple_0)
        var_0 = included_file_1.__eq__(included_file_1)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'dummy_file.yml'
        var_0 = {}
        var_1 = {}
        task_include_0 = module_1.TaskInclude()
        included_file_0 = module_0.IncludedFile(str_0, var_0, var_1, task_include_0)
        str_1 = 'host1'
        var_2 = included_file_0.add_host(str_1)
        str_2 = 'host2'
        var_3 = included_file_0.add_host(str_2)
        str_3 = 'host1'
        var_4 = included_file_0.add_host(str_3)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'dummy_file.yml'
        task_include_0 = module_1.TaskInclude()
        included_file_0 = module_0.IncludedFile(str_0, task_include_0, task_include_0, task_include_0)
        var_0 = included_file_0.__eq__(included_file_0)
    except BaseException:
        pass