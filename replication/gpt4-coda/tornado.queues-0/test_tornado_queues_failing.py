# Automatically generated by Pynguin.
import tornado.queues as module_0

def test_case_0():
    try:
        bytes_0 = b'\x98\x9dR\x8b\xc0\x83\xcf\x9a\xb8\x87'
        queue_0 = module_0.Queue()
        queue_1 = module_0.Queue()
        bool_0 = queue_1.full()
        str_0 = queue_0.__str__()
        queue_iterator_0 = module_0._QueueIterator(bytes_0)
        awaitable_0 = queue_iterator_0.__anext__()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = None
        queue_0 = module_0.Queue(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = -1672
        queue_0 = module_0.Queue(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        queue_0 = module_0.Queue()
        var_0 = queue_0.get_nowait()
    except BaseException:
        pass

def test_case_4():
    try:
        queue_0 = module_0.Queue()
        str_0 = queue_0.__repr__()
        var_0 = None
        queue_1 = module_0.Queue()
        future_0 = queue_1.put(var_0)
    except BaseException:
        pass

def test_case_5():
    try:
        queue_0 = module_0.Queue()
        awaitable_0 = queue_0.get()
    except BaseException:
        pass

def test_case_6():
    try:
        queue_0 = module_0.Queue()
        queue_0.task_done()
    except BaseException:
        pass

def test_case_7():
    try:
        queue_0 = module_0.Queue()
        str_0 = queue_0.__repr__()
        awaitable_0 = queue_0.join()
    except BaseException:
        pass

def test_case_8():
    try:
        queue_0 = module_0.Queue()
        int_0 = queue_0.qsize()
        lifo_queue_0 = module_0.LifoQueue()
        bool_0 = queue_0.empty()
        awaitable_0 = queue_0.get()
    except BaseException:
        pass

def test_case_9():
    try:
        queue_0 = module_0.Queue()
        bool_0 = queue_0.full()
        var_0 = None
        queue_0.put_nowait(var_0)
        str_0 = queue_0.__str__()
        var_1 = queue_0.get_nowait()
        queue_0.put_nowait(var_1)
        int_0 = 3646
        queue_1 = module_0.Queue(int_0)
        queue_1.put_nowait(var_1)
        bool_1 = queue_1.empty()
        awaitable_0 = queue_1.get()
    except BaseException:
        pass

def test_case_10():
    try:
        queue_0 = module_0.Queue()
        bool_0 = queue_0.full()
        var_0 = None
        queue_0.put_nowait(var_0)
        str_0 = queue_0.__str__()
        queue_1 = module_0.Queue()
        var_1 = queue_0.__aiter__()
        queue_2 = module_0.Queue()
        str_1 = queue_2.__repr__()
        var_2 = queue_1.get_nowait()
    except BaseException:
        pass

def test_case_11():
    try:
        queue_0 = module_0.Queue()
        bool_0 = queue_0.full()
        var_0 = None
        str_0 = queue_0.__str__()
        queue_0.put_nowait(var_0)
        str_1 = queue_0.__str__()
        var_1 = queue_0.get_nowait()
        queue_0.put_nowait(var_1)
        int_0 = 3646
        queue_1 = module_0.Queue(int_0)
        queue_0.task_done()
        bool_1 = queue_1.empty()
        awaitable_0 = queue_1.get()
    except BaseException:
        pass

def test_case_12():
    try:
        queue_0 = module_0.Queue()
        bool_0 = queue_0.full()
        var_0 = None
        str_0 = queue_0.__str__()
        queue_0.put_nowait(var_0)
        str_1 = queue_0.__str__()
        var_1 = queue_0.get_nowait()
        int_0 = 3646
        queue_1 = module_0.Queue(int_0)
        queue_0.task_done()
        bool_1 = queue_1.empty()
        awaitable_0 = queue_1.get()
    except BaseException:
        pass