# Automatically generated by Pynguin.
import ansible.playbook.role.requirement as module_0

def test_case_0():
    pass

def test_case_1():
    role_requirement_0 = module_0.RoleRequirement()

def test_case_2():
    role_requirement_0 = module_0.RoleRequirement()
    str_0 = 'MQ'
    var_0 = role_requirement_0.role_yaml_parse(str_0)

def test_case_3():
    str_0 = 'r#}[@0 /w'
    role_requirement_0 = module_0.RoleRequirement()
    var_0 = role_requirement_0.repo_url_to_role_name(str_0)

def test_case_4():
    role_requirement_0 = module_0.RoleRequirement()
    str_0 = '/8/5RiEe\x0c&)wk"\tYH@r'
    var_0 = role_requirement_0.role_yaml_parse(str_0)
    var_1 = role_requirement_0.role_yaml_parse(var_0)
    role_requirement_1 = module_0.RoleRequirement()
    str_1 = 'p.%Co|z5-\n<q\rp9\n'
    var_2 = role_requirement_0.repo_url_to_role_name(str_1)

def test_case_5():
    str_0 = 'N_Port Port World Wide Name'
    role_requirement_0 = module_0.RoleRequirement()
    var_0 = role_requirement_0.role_yaml_parse(str_0)
    str_1 = ''
    var_1 = role_requirement_0.role_yaml_parse(str_1)
    role_requirement_1 = module_0.RoleRequirement()
    str_2 = 'N,Y`%<mZ&r'
    var_2 = role_requirement_1.role_yaml_parse(str_2)

def test_case_6():
    role_requirement_0 = module_0.RoleRequirement()
    dict_0 = {role_requirement_0: role_requirement_0, role_requirement_0: role_requirement_0}
    var_0 = role_requirement_0.role_yaml_parse(dict_0)
    str_0 = '/8/5RiEe\x0c&)wk"\tYH@r'
    role_requirement_1 = module_0.RoleRequirement()
    var_1 = role_requirement_0.role_yaml_parse(str_0)
    str_1 = 'jj? Qs'
    role_requirement_2 = module_0.RoleRequirement()
    str_2 = 'evg,i;Fyz'
    var_2 = role_requirement_0.role_yaml_parse(str_2)
    role_requirement_3 = module_0.RoleRequirement()
    var_3 = role_requirement_3.repo_url_to_role_name(str_1)
    role_requirement_4 = module_0.RoleRequirement()
    role_requirement_5 = module_0.RoleRequirement()
    str_3 = "`8\t@@6Z':vK,6dAS^_"
    var_4 = role_requirement_5.repo_url_to_role_name(str_3)

def test_case_7():
    role_requirement_0 = module_0.RoleRequirement()
    str_0 = 'https://gitlab.example.com/ansible/ansible-role-example.git'
    var_0 = role_requirement_0.repo_url_to_role_name(str_0)