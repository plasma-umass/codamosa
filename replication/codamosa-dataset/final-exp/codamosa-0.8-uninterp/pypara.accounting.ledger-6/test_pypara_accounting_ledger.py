# Automatically generated by Pynguin.
import pypara.accounting.ledger as module_0
import pypara.commons.zeitgeist as module_1
import pypara.accounting.journaling as module_2

def test_case_0():
    pass

def test_case_1():
    read_initial_balances_0 = None
    var_0 = None
    var_1 = module_0.compile_general_ledger_program(read_initial_balances_0, var_0)
    date_0 = None
    date_range_0 = module_1.DateRange(date_0, date_0)
    dict_0 = {}
    dict_1 = {}
    var_2 = module_0.build_general_ledger(date_range_0, dict_0, dict_1)
    var_3 = date_range_0.__hash__()

def test_case_2():
    date_0 = None
    date_range_0 = module_1.DateRange(date_0, date_0)
    dict_0 = {}
    dict_1 = {}
    var_0 = module_0.build_general_ledger(date_range_0, dict_0, dict_1)

def test_case_3():
    date_0 = None
    date_range_0 = module_1.DateRange(date_0, date_0)
    dict_0 = {}
    str_0 = '#&5nLLvm'
    journal_entry_0 = module_2.JournalEntry(date_0, str_0, date_0)
    list_0 = [journal_entry_0]
    var_0 = module_0.build_general_ledger(date_range_0, list_0, dict_0)