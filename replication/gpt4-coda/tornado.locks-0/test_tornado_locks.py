# Automatically generated by Pynguin.
import tornado.locks as module_0

def test_case_0():
    pass

def test_case_1():
    event_0 = module_0.Event()
    event_0.set()

def test_case_2():
    event_0 = module_0.Event()
    bool_0 = event_0.is_set()
    event_0.clear()
    event_0.clear()

def test_case_3():
    lock_0 = module_0.Lock()
    str_0 = lock_0.__repr__()

def test_case_4():
    semaphore_0 = module_0.Semaphore()
    semaphore_0.release()