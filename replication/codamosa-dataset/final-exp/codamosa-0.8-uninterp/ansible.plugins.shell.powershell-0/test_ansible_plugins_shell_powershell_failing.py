# Automatically generated by Pynguin.
import ansible.plugins.shell.powershell as module_0

def test_case_0():
    try:
        str_0 = None
        dict_0 = {str_0: str_0, str_0: str_0}
        dict_1 = {}
        list_0 = []
        list_1 = [list_0, str_0, dict_0]
        shell_module_0 = module_0.ShellModule()
        var_0 = shell_module_0.join_path(*list_1)
        str_1 = '\r$Yj)ES9f'
        shell_module_1 = module_0.ShellModule()
        var_1 = shell_module_1.build_module_command(dict_1, list_0, str_1)
    except BaseException:
        pass

def test_case_1():
    try:
        shell_module_0 = module_0.ShellModule()
        var_0 = shell_module_0.path_has_trailing_slash(shell_module_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\xf1\x8b\x04\xbc\x9cu\x13\xa06\x9d\x8b\xc2\x11'
        dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
        set_0 = None
        shell_module_0 = module_0.ShellModule()
        var_0 = shell_module_0.chmod(dict_0, set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        int_0 = None
        tuple_0 = (bool_0, int_0, bool_0)
        str_0 = '6*UEh4K:3$s9Cc}l#e'
        dict_0 = {str_0: str_0}
        shell_module_0 = module_0.ShellModule()
        var_0 = shell_module_0.chown(tuple_0, dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        shell_module_0 = module_0.ShellModule()
        complex_0 = None
        var_0 = shell_module_0.expand_user(complex_0)
        str_0 = '76DK*XY\t}f84'
        bool_0 = True
        str_1 = '*7e\tz)>O\tqR*g\nk5<'
        var_1 = shell_module_0.set_user_facl(str_0, bool_0, str_1)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'^gGH\xdfP\x0bK\x1a][\xc1\xe6\xcfu\xa1M\x08W'
        shell_module_0 = module_0.ShellModule()
        var_0 = shell_module_0.remove(bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        shell_module_0 = module_0.ShellModule()
        var_0 = shell_module_0.mkdtemp()
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '\n            If (Test-Path -PathType Leaf \'subdirs\')\n            {\n                $sp = new-object -TypeName System.Security.Cryptography.SHA1CryptoServiceProvider;\n                $fp = [System.IO.File]::Open(\'subdirs\', [System.IO.Filemode]::Open, [System.IO.FileAccess]::Read);\n                [System.BitConverter]::ToString($sp.ComputeHash($fp)).Replace("-", "").ToLower();\n                $fp.Dispose();\n            }\n            ElseIf (Test-Path -PathType Container \'subdirs\')\n            {\n                Write-Output "3";\n            }\n            Else\n            {\n                Write-Output "1";\n            }\n        '
        bool_0 = True
        shell_module_0 = module_0.ShellModule()
        var_0 = shell_module_0.wrap_for_exec(bool_0)
        shell_module_1 = module_0.ShellModule()
        var_1 = shell_module_1.expand_user(str_0, shell_module_0)
        shell_module_2 = module_0.ShellModule()
        var_2 = shell_module_2.exists(shell_module_1)
        set_0 = {shell_module_2, shell_module_0}
        var_3 = shell_module_2.path_has_trailing_slash(set_0)
    except BaseException:
        pass

def test_case_8():
    try:
        dict_0 = {}
        list_0 = []
        str_0 = '\r$Yj)ES9f'
        shell_module_0 = module_0.ShellModule()
        var_0 = shell_module_0.build_module_command(dict_0, list_0, str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = "git version '%s' is too old to use 'single-branch'. Ignoring."
        set_0 = {str_0}
        tuple_0 = (str_0, set_0)
        shell_module_0 = module_0.ShellModule()
        var_0 = shell_module_0.wrap_for_exec(tuple_0)
    except BaseException:
        pass

def test_case_10():
    try:
        shell_module_0 = module_0.ShellModule()
        int_0 = 196
        var_0 = shell_module_0.mkdtemp(int_0)
    except BaseException:
        pass

def test_case_11():
    try:
        shell_module_0 = module_0.ShellModule()
        set_0 = set()
        var_0 = shell_module_0.path_has_trailing_slash(set_0)
    except BaseException:
        pass

def test_case_12():
    try:
        shell_module_0 = module_0.ShellModule()
        str_0 = 'C:/Windows//\\'
        bytes_0 = b'\xec2N\x13p:9\xbe\xb6\xf5/'
        str_1 = 'using -c ssh on certain older ssh versions may not support ControlPersist, set ANSIBLE_SSH_ARGS="" (or ssh_args in [ssh_connection] section of the config file) before running again'
        var_0 = shell_module_0.wrap_for_exec(str_1)
        list_0 = [str_0, str_0, str_0]
        var_1 = shell_module_0.remove(list_0)
        var_2 = shell_module_0.path_has_trailing_slash(bytes_0)
        dict_0 = {bytes_0: str_0, shell_module_0: shell_module_0, str_0: shell_module_0}
        dict_1 = {str_0: dict_0}
        var_3 = shell_module_0.path_has_trailing_slash(dict_1)
    except BaseException:
        pass

def test_case_13():
    try:
        shell_module_0 = module_0.ShellModule()
        var_0 = set()
        str_0 = '/Lath/foo.s1'
        var_1 = shell_module_0.get_remote_filename(str_0)
        str_1 = '"path"'
        var_2 = shell_module_0.path_has_trailing_slash(str_1)
    except BaseException:
        pass