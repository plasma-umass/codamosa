# Automatically generated by Pynguin.
import pypara.dcc as module_0
import datetime as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = '\x0c'
    d_c_c_registry_machinery_0 = module_0.DCCRegistryMachinery()
    optional_0 = d_c_c_registry_machinery_0.find(str_0)

def test_case_2():
    int_0 = 2
    list_0 = [int_0, int_0, int_0]
    date_0 = module_1.date(*list_0)
    decimal_0 = module_0.dcfc_act_act(date_0, date_0, date_0)
    d_c_c_registry_machinery_0 = module_0.DCCRegistryMachinery()
    decimal_1 = module_0.dcfc_nl_365(date_0, date_0, date_0)
    decimal_2 = module_0.dcfc_30_360_german(date_0, date_0, date_0)
    decimal_3 = module_0.dcfc_30_e_360(date_0, date_0, date_0)
    decimal_4 = module_0.dcfc_act_365_f(date_0, date_0, date_0)
    decimal_5 = module_0.dcfc_30_360_us(date_0, date_0, date_0, decimal_1)

def test_case_3():
    int_0 = 7
    int_1 = 1
    list_0 = [int_0, int_0, int_1]
    date_0 = module_1.date(*list_0)
    decimal_0 = module_0.dcfc_act_act(date_0, date_0, date_0)

def test_case_4():
    int_0 = 7
    int_1 = 1
    list_0 = [int_0, int_0, int_1]
    date_0 = module_1.date(*list_0)
    str_0 = 'Balance'
    decimal_0 = module_0.dcfc_nl_365(date_0, date_0, date_0)
    d_c_c_registry_machinery_0 = module_0.DCCRegistryMachinery()
    d_c_c_registry_machinery_1 = module_0.DCCRegistryMachinery()
    optional_0 = d_c_c_registry_machinery_1.find(str_0)

def test_case_5():
    int_0 = 7
    int_1 = 1
    list_0 = [int_0, int_0, int_1]
    date_0 = module_1.date(*list_0)
    decimal_0 = module_0.dcfc_30_360_german(date_0, date_0, date_0)
    decimal_1 = module_0.dcfc_30_360_us(date_0, date_0, date_0)

def test_case_6():
    int_0 = 7
    int_1 = 1
    list_0 = [int_0, int_0, int_1]
    date_0 = module_1.date(*list_0)
    decimal_0 = module_0.dcfc_act_365_a(date_0, date_0, date_0)

def test_case_7():
    int_0 = 12
    list_0 = [int_0, int_0, int_0]
    date_0 = module_1.date(*list_0)
    decimal_0 = module_0.dcfc_act_act(date_0, date_0, date_0)
    decimal_1 = module_0.dcfc_act_365_a(date_0, date_0, date_0, decimal_0)
    decimal_2 = module_0.dcfc_30_e_plus_360(date_0, date_0, date_0)
    decimal_3 = module_0.dcfc_30_e_360(date_0, date_0, date_0, decimal_0)
    d_c_c_registry_machinery_0 = module_0.DCCRegistryMachinery()
    decimal_4 = module_0.dcfc_nl_365(date_0, date_0, date_0, decimal_0)
    decimal_5 = module_0.dcfc_30_360_german(date_0, date_0, date_0, decimal_1)
    decimal_6 = module_0.dcfc_30_e_360(date_0, date_0, date_0)
    decimal_7 = module_0.dcfc_30_360_isda(date_0, date_0, date_0)
    decimal_8 = module_0.dcfc_act_365_l(date_0, date_0, date_0)
    decimal_9 = module_0.dcfc_30_360_us(date_0, date_0, date_0)