# Automatically generated by Pynguin.
import ansible.executor.play_iterator as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '%rEFO*\t.u8+\'"dV[^:w'
    list_0 = [str_0]
    host_state_0 = module_0.HostState(list_0)

def test_case_2():
    str_0 = '%rEFO*\t.u8+\'"dV[^:w'
    list_0 = [str_0]
    host_state_0 = module_0.HostState(list_0)
    var_0 = host_state_0.__repr__()
    var_1 = host_state_0.__str__()

def test_case_3():
    int_0 = 303
    bytes_0 = b'%'
    host_state_0 = module_0.HostState(bytes_0)
    var_0 = host_state_0.__eq__(int_0)

def test_case_4():
    bytes_0 = b'\x02\xac\x83\x88\xa7.\x9e\xdaO}\x8a\x18\x0co\x1f\xe6d\xaeM'
    int_0 = None
    tuple_0 = (bytes_0, int_0)
    host_state_0 = module_0.HostState(tuple_0)
    var_0 = host_state_0.copy()
    var_1 = host_state_0.get_current_block()

def test_case_5():
    var_0 = []
    host_state_0 = module_0.HostState(var_0)
    var_1 = host_state_0.copy()

def test_case_6():
    str_0 = '!?TO'
    host_state_0 = module_0.HostState(str_0)
    var_0 = host_state_0.__str__()