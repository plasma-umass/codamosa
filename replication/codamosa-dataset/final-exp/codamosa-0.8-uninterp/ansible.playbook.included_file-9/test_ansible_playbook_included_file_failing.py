# Automatically generated by Pynguin.
import ansible.playbook.included_file as module_0

def test_case_0():
    try:
        str_0 = 'test_file'
        str_1 = 'test_host'
        included_file_0 = module_0.IncludedFile(str_0, str_1, str_1, str_1)
        var_0 = included_file_0.add_host(str_1)
        var_1 = included_file_0.add_host(str_1)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 1674.64
        tuple_0 = ()
        bool_0 = False
        included_file_0 = module_0.IncludedFile(float_0, bool_0, tuple_0, bool_0)
        var_0 = included_file_0.__eq__(included_file_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '1;xy>Q5eHp:F'
        str_1 = "g\r6mBt(xD'dW1=P"
        int_0 = 1012
        dict_0 = {int_0: str_0}
        included_file_0 = module_0.IncludedFile(str_1, int_0, int_0, dict_0)
        bytes_0 = b'n\x07\x16\xce\xb8\xb9\x89S'
        str_2 = 'error'
        str_3 = '\n---\nauthor: Ansible Core Team (@ansible)\nmodule: include_role\nshort_description: Load and execute a role\ndescription:\n  - Dynamically loads and executes a specified role as a task.\n  - May be used only where Ansible tasks are allowed - inside C(pre_tasks), C(tasks), or C(post_tasks) play objects, or as a task inside a role.\n  - Task-level keywords, loops, and conditionals apply only to the C(include_role) statement itself.\n  - To apply keywords to the tasks within the role, pass them using the C(apply) option or use M(ansible.builtin.import_role) instead.\n  - Ignores some keywords, like C(until) and C(retries).\n  - This module is also supported for Windows targets.\n  - Does not work in handlers.\nversion_added: "2.2"\noptions:\n  apply:\n    description:\n      - Accepts a hash of task keywords (e.g. C(tags), C(become)) that will be applied to all tasks within the included role.\n    version_added: \'2.7\'\n  name:\n    description:\n      - The name of the role to be executed.\n    type: str\n    required: True\n  tasks_from:\n    description:\n      - File to load from a role\'s C(tasks/) directory.\n    type: str\n    default: main\n  vars_from:\n    description:\n      - File to load from a role\'s C(vars/) directory.\n    type: str\n    default: main\n  defaults_from:\n    description:\n      - File to load from a role\'s C(defaults/) directory.\n    type: str\n    default: main\n  allow_duplicates:\n    description:\n      - Overrides the role\'s metadata setting to allow using a role more than once with the same parameters.\n    type: bool\n    default: yes\n  public:\n    description:\n      - This option dictates whether the role\'s C(vars) and C(defaults) are exposed to the play. If set to C(yes)\n        the variables will be available to tasks following the C(include_role) task. This functionality differs from\n        standard variable exposure for roles listed under the C(roles) header or C(import_role) as they are exposed\n        to the play at playbook parsing time, and available to earlier roles and tasks as well.\n    type: bool\n    default: no\n    version_added: \'2.7\'\n  handlers_from:\n    description:\n      - File to load from a role\'s C(handlers/) directory.\n    type: str\n    default: main\n    version_added: \'2.8\'\n  rolespec_validate:\n    description:\n      - Perform role argument spec validation if an argument spec is defined.\n    type: bool\n    default: yes\n    version_added: \'2.11\'\nextends_documentation_fragment:\n    - action_common_attributes\n    - action_common_attributes.conn\n    - action_common_attributes.flow\n    - action_core\n    - action_core.include\nattributes:\n    check_mode:\n        support: full\n    diff_mode:\n        support: none\nnotes:\n  - Handlers and are made available to the whole play.\n  - After Ansible 2.4, you can use M(ansible.builtin.import_role) for C(static) behaviour and this action for C(dynamic) one.\nseealso:\n- module: ansible.builtin.import_playbook\n- module: ansible.builtin.import_role\n- module: ansible.builtin.import_tasks\n- module: ansible.builtin.include_tasks\n- ref: playbooks_reuse_includes\n  description: More information related to including and importing playbooks, roles and tasks.\n'
        str_4 = 'R+%B7[w`+\\#Zy\nBFD(t'
        str_5 = '[ljCDI4m%nT$D\n\nj'
        bool_0 = True
        included_file_1 = module_0.IncludedFile(str_3, str_4, str_5, bool_0)
        var_0 = included_file_1.process_include_results(str_0, included_file_0, bytes_0, str_2)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = None
        float_0 = 60.0
        int_0 = -698
        str_1 = '1\x0cq9!kocG1'
        bytes_0 = b'?\x8d \xc6\xe5M\xbc\xfd\x02\x0e>'
        included_file_0 = module_0.IncludedFile(float_0, int_0, str_1, bytes_0, str_1)
        bool_0 = True
        int_1 = 3003
        dict_0 = {int_1: str_1, int_1: int_1}
        included_file_1 = module_0.IncludedFile(bool_0, int_1, str_0, dict_0)
        var_0 = included_file_1.__eq__(included_file_0)
        list_0 = [str_0]
        var_1 = included_file_0.__eq__(list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        str_0 = "2yLOW'd4"
        float_0 = 583.6878394926803
        tuple_0 = (float_0, str_0)
        bool_0 = True
        bytes_0 = b"\x1d\xf56'\x99\xe4;\xf4\xc2\xfe\xd2\xc2\xa4\xcf\xa9\xe6\xd7"
        set_0 = {tuple_0, bool_0}
        included_file_0 = module_0.IncludedFile(tuple_0, bool_0, bytes_0, set_0)
        bytes_1 = b'\xb6\xdbd'
        var_0 = included_file_0.add_host(bytes_0)
        var_1 = included_file_0.process_include_results(dict_0, float_0, float_0, dict_0)
        included_file_1 = module_0.IncludedFile(dict_0, bool_0, str_0, float_0)
        str_1 = '#(\x0cd\\bNbxx<r6`'
        int_0 = -1797
        set_1 = {str_1, bytes_1, str_1}
        var_2 = included_file_1.process_include_results(str_1, int_0, set_1, set_1)
    except BaseException:
        pass