# Automatically generated by Pynguin.
import ansible.modules.pip as module_0
import tempfile as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = '!!&UX'
    str_1 = 'yeAax+Hr6C%~0eFv'
    package_0 = module_0.Package(str_0, str_1)

def test_case_2():
    str_0 = '__main__'
    package_0 = module_0.Package(str_0)

def test_case_3():
    var_0 = module_0.main()

def test_case_4():
    str_0 = 'VUp!hY`X+'
    str_1 = 'n5>ZtXJ$R}i'
    package_0 = module_0.Package(str_1)
    package_1 = module_0.Package(str_0)
    var_0 = package_0.__str__()
    var_1 = module_0.main()
    var_2 = package_1.__str__()

def test_case_5():
    str_0 = 'foo'
    package_0 = module_0.Package(str_0)
    package_1 = module_0.Package(str_0, str_0)
    str_1 = 'foo==1.0'
    package_2 = module_0.Package(str_1)
    package_3 = module_0.Package(str_1)
    var_0 = package_3.has_version_specifier
    str_2 = 'foo>=1.0'
    package_4 = module_0.Package(str_2)
    var_1 = package_4.has_version_specifier
    str_3 = 'foo<1.0'
    package_5 = module_0.Package(str_3)
    var_2 = package_5.has_version_specifier
    package_6 = module_0.Package(str_0)
    var_3 = package_6.has_version_specifier
    package_7 = module_0.Package(str_0, str_3)
    var_4 = package_7.has_version_specifier
    package_8 = module_0.Package(str_0)
    var_5 = package_8.is_satisfied_by(str_3)
    package_9 = module_0.Package(str_1)

def test_case_6():
    str_0 = 'foo'
    package_0 = module_0.Package(str_0)
    str_1 = '1.0'
    package_1 = module_0.Package(str_0, str_1)
    str_2 = 'foo==1.0'
    package_2 = module_0.Package(str_2)
    package_3 = module_0.Package(str_2)
    str_3 = 'foo>=1.0'
    package_4 = module_0.Package(str_3)
    var_0 = package_4.has_version_specifier
    str_4 = 'foo<1.0'
    package_5 = module_0.Package(str_4)
    var_1 = package_5.has_version_specifier
    package_6 = module_0.Package(str_1)
    var_2 = package_6.has_version_specifier
    package_7 = module_0.Package(str_0, str_1)
    var_3 = package_7.has_version_specifier
    package_8 = module_0.Package(str_0)
    var_4 = package_8.is_satisfied_by(str_1)
    package_9 = module_0.Package(str_2)

def test_case_7():
    str_0 = 'str'
    str_1 = 'distribute'
    package_0 = module_0.Package(str_1)
    var_0 = package_0.__str__()
    var_1 = dict(type=str_0, default=str_0)
    var_2 = module_1.gettempdir()
    var_3 = dict(type=str_0, default=var_2)