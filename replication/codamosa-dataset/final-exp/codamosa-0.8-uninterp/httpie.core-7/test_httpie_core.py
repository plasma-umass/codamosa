# Automatically generated by Pynguin.
import httpie.core as module_0
import httpie.context as module_1

def test_case_0():
    pass

def test_case_1():
    exit_status_0 = module_0.main()

def test_case_2():
    str_0 = 'rw'
    exit_status_0 = module_0.main(str_0)

def test_case_3():
    environment_0 = module_1.Environment()
    var_0 = module_0.print_debug_info(environment_0)

def test_case_4():
    str_0 = 'hjtp://example.org'
    str_1 = [str_0, str_0]
    exit_status_0 = module_0.main(str_1)
    exit_status_1 = module_0.main()

def test_case_5():
    str_0 = 'http://example.org'
    str_1 = [str_0, str_0]
    exit_status_0 = module_0.main(str_1)

def test_case_6():
    str_0 = '--version'
    str_1 = '--debug'
    str_2 = [str_0, str_1]
    exit_status_0 = module_0.main(str_2)
    str_3 = '--output-file=-'
    str_4 = [str_0, str_1, str_3]
    exit_status_1 = module_0.main(str_4)
    str_5 = '--output-file'
    str_6 = '-'
    str_7 = [str_0, str_1, str_5, str_6]
    exit_status_2 = module_0.main(str_7)
    str_8 = 'example.org'
    str_9 = [str_0, str_1, str_5, str_6, str_8]
    exit_status_3 = module_0.main(str_9)