# Automatically generated by Pynguin.
import ansible.playbook.role.requirement as module_0

def test_case_0():
    role_requirement_0 = module_0.RoleRequirement()

def test_case_1():
    role_requirement_0 = module_0.RoleRequirement()
    str_0 = 'JW38d}\nH&\n^h^'
    var_0 = role_requirement_0.repo_url_to_role_name(str_0)
    role_requirement_1 = module_0.RoleRequirement()

def test_case_2():
    str_0 = '9@\x0bC Mn\x0cHn6l=<%'
    role_requirement_0 = module_0.RoleRequirement()
    var_0 = role_requirement_0.role_yaml_parse(str_0)

def test_case_3():
    role_requirement_0 = module_0.RoleRequirement()
    role_requirement_1 = module_0.RoleRequirement()
    float_0 = 560.3
    dict_0 = {float_0: role_requirement_1}
    var_0 = role_requirement_0.role_yaml_parse(dict_0)

def test_case_4():
    role_requirement_0 = module_0.RoleRequirement()
    str_0 = 'W '
    var_0 = role_requirement_0.role_yaml_parse(str_0)
    var_1 = role_requirement_0.role_yaml_parse(var_0)
    role_requirement_1 = module_0.RoleRequirement()
    role_requirement_2 = module_0.RoleRequirement()
    role_requirement_3 = module_0.RoleRequirement()
    role_requirement_4 = module_0.RoleRequirement()

def test_case_5():
    str_0 = 'http://git.example.com/repos/repo.git'
    list_0 = [str_0, str_0, str_0, str_0]
    role_requirement_0 = module_0.RoleRequirement()
    var_0 = role_requirement_0.repo_url_to_role_name(list_0)
    str_1 = 'https://git.example.com/repos/repo.git'
    role_requirement_1 = module_0.RoleRequirement()
    var_1 = role_requirement_1.role_yaml_parse(str_1)

def test_case_6():
    role_requirement_0 = module_0.RoleRequirement()
    role_requirement_1 = module_0.RoleRequirement()
    int_0 = None
    str_0 = 'p{q4FZK-\r\r3L\r,=GZ,im'
    bytes_0 = b'\xfe\xb8'
    bytes_1 = b"\x08'a\xa4K\xf1\x13K7\x1e\xf8\xde\x07\x95T9\xdc>@m"
    dict_0 = {bytes_1: int_0, role_requirement_1: bytes_0, int_0: bytes_1, bytes_1: int_0}
    var_0 = role_requirement_1.role_yaml_parse(dict_0)
    str_1 = '<TG(@@VnO]v'
    var_1 = role_requirement_1.repo_url_to_role_name(str_1)
    var_2 = role_requirement_0.role_yaml_parse(str_0)
    var_3 = role_requirement_1.role_yaml_parse(var_2)