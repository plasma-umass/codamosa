# Automatically generated by Pynguin.
import ansible.plugins.shell.powershell as module_0

def test_case_0():
    pass

def test_case_1():
    shell_module_0 = module_0.ShellModule()
    var_0 = shell_module_0.env_prefix()

def test_case_2():
    shell_module_0 = module_0.ShellModule()
    str_0 = 'C:\\windows\\temp\\testfile'
    var_0 = shell_module_0.get_remote_filename(str_0)

def test_case_3():
    shell_module_0 = module_0.ShellModule()
    var_0 = None
    str_0 = '#!powershell'
    str_1 = 'rI!06E\x0b95NXDs?Pn?'
    var_1 = shell_module_0.remove(str_0, str_1)
    str_2 = 'echo 1'
    str_3 = 'C:\\Users\\username\\ansible-test\\test.ps1'
    var_2 = shell_module_0.build_module_command(var_0, str_0, str_2, str_3)

def test_case_4():
    shell_module_0 = module_0.ShellModule()
    var_0 = shell_module_0.expand_user(shell_module_0)

def test_case_5():
    shell_module_0 = module_0.ShellModule()
    int_0 = -2144
    var_0 = shell_module_0.checksum(int_0)

def test_case_6():
    shell_module_0 = module_0.ShellModule()
    str_0 = '#!powershell'
    str_1 = 'C:\\Users\\username\\ansible-test\\test.ps1'
    var_0 = shell_module_0.build_module_command(str_1, str_0, str_0, str_1)

def test_case_7():
    shell_module_0 = module_0.ShellModule()
    var_0 = None
    str_0 = '#!powUershell'
    str_1 = 'echo 1'
    str_2 = 'C:\\sers\\username\\ansible,test\\test.ps1'
    var_1 = shell_module_0.build_module_command(var_0, str_0, str_1, str_2)

def test_case_8():
    str_0 = '[c(:\x0c+3]D2m)\rbq'
    str_1 = 'v\'o";\r`Uq~/B/pgx\'v'
    str_2 = ''
    dict_0 = {str_0: str_0, str_1: str_0, str_1: str_1, str_2: str_1}
    str_3 = None
    bytes_0 = b'\x9d\xc2\xa5\x8dCvu\x0b0\xaf\x86\xaaIK\xe8\x8c\xcc\xe7'
    shell_module_0 = module_0.ShellModule()
    var_0 = shell_module_0.build_module_command(str_3, bytes_0, str_2)
    shell_module_1 = module_0.ShellModule()
    var_1 = shell_module_1.wrap_for_exec(dict_0)
    list_0 = None
    shell_module_2 = module_0.ShellModule()
    var_2 = shell_module_1.checksum(list_0)

def test_case_9():
    float_0 = None
    shell_module_0 = module_0.ShellModule()
    var_0 = shell_module_0.expand_user(float_0)
    list_0 = []
    str_0 = '\r$Yjc)ES9f'
    shell_module_1 = module_0.ShellModule()
    var_1 = shell_module_0.checksum(list_0)
    bool_0 = True
    var_2 = shell_module_0.build_module_command(bool_0, str_0, str_0)

def test_case_10():
    shell_module_0 = module_0.ShellModule()
    list_0 = [shell_module_0]
    list_1 = [list_0]
    shell_module_1 = module_0.ShellModule()
    var_0 = shell_module_1.mkdtemp(shell_module_0, shell_module_0, list_0, list_1)
    shell_module_2 = module_0.ShellModule()
    bool_0 = None
    var_1 = shell_module_2.expand_user(bool_0)

def test_case_11():
    shell_module_0 = module_0.ShellModule()
    str_0 = '~'
    var_0 = shell_module_0.expand_user(str_0)
    str_1 = '~\\foo'
    var_1 = shell_module_0.expand_user(str_1)
    str_2 = 'bar'
    var_2 = shell_module_0.expand_user(str_2)

def test_case_12():
    shell_module_0 = module_0.ShellModule()
    int_0 = -2086
    str_0 = '7^=k.8$'
    str_1 = '-g#kC0&'
    dict_0 = {str_0: str_0, str_0: int_0, str_1: str_1}
    var_0 = shell_module_0.expand_user(dict_0)
    var_1 = None
    str_2 = '#!powershell'
    str_3 = 'C:\\Users\\username\\ansible-test\\test.ps1'
    var_2 = shell_module_0.build_module_command(var_1, str_2, str_3, str_3)

def test_case_13():
    shell_module_0 = module_0.ShellModule()
    str_0 = 'test_module'
    var_0 = shell_module_0.get_remote_filename(str_0)
    str_1 = 'test_module.ps1'
    var_1 = shell_module_0.get_remote_filename(str_1)
    str_2 = 'test_module.py'
    var_2 = shell_module_0.get_remote_filename(str_2)
    str_3 = 'test_module.exe'
    var_3 = shell_module_0.get_remote_filename(str_3)