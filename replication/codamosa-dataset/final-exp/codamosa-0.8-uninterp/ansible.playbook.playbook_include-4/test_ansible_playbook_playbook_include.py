# Automatically generated by Pynguin.
import ansible.parsing.yaml.objects as module_0
import ansible.playbook.playbook_include as module_1

def test_case_0():
    pass

def test_case_1():
    ansible_mapping_0 = module_0.AnsibleMapping()
    playbook_include_0 = module_1.PlaybookInclude()
    var_0 = playbook_include_0.preprocess_data(ansible_mapping_0)

def test_case_2():
    playbook_include_0 = module_1.PlaybookInclude()
    str_0 = 'import_playbook'
    str_1 = {str_0: str_0}
    var_0 = playbook_include_0.preprocess_data(str_1)

def test_case_3():
    playbook_include_0 = module_1.PlaybookInclude()
    str_0 = 'import_playbook'
    str_1 = 'playbook.yml vars:my_var="Hello world"'
    str_2 = {str_0: str_1}
    var_0 = playbook_include_0.preprocess_data(str_2)