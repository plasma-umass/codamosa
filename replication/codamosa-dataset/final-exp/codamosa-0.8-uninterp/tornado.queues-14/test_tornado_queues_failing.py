# Automatically generated by Pynguin.
import tornado.queues as module_0

def test_case_0():
    try:
        var_0 = None
        queue_iterator_0 = module_0._QueueIterator(var_0)
        awaitable_0 = queue_iterator_0.__anext__()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -1901
        int_1 = 3037
        priority_queue_0 = module_0.PriorityQueue(int_1)
        queue_0 = module_0.Queue(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        queue_0 = module_0.Queue()
        queue_1 = module_0.Queue()
        int_0 = 3630
        queue_2 = module_0.Queue(int_0)
        int_1 = queue_2.qsize()
        var_0 = None
        future_0 = queue_0.put(var_0)
    except BaseException:
        pass

def test_case_3():
    try:
        queue_0 = module_0.Queue()
        str_0 = queue_0.__str__()
        var_0 = None
        queue_0.put_nowait(var_0)
        var_1 = queue_0.__aiter__()
        awaitable_0 = queue_0.get()
    except BaseException:
        pass

def test_case_4():
    try:
        queue_0 = module_0.Queue()
        var_0 = queue_0.get_nowait()
    except BaseException:
        pass

def test_case_5():
    try:
        queue_0 = module_0.Queue()
        queue_0.task_done()
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = None
        queue_0 = module_0.Queue()
        queue_1 = module_0.Queue()
        var_0 = queue_1.__aiter__()
        awaitable_0 = queue_0.join(bytes_0)
    except BaseException:
        pass

def test_case_7():
    try:
        queue_0 = module_0.Queue()
        bool_0 = queue_0.full()
        queue_1 = module_0.Queue()
        queue_2 = module_0.Queue()
        lifo_queue_0 = module_0.LifoQueue()
        var_0 = queue_2.get_nowait()
    except BaseException:
        pass

def test_case_8():
    try:
        queue_0 = module_0.Queue()
        str_0 = queue_0.__str__()
        var_0 = None
        queue_0.put_nowait(var_0)
        var_1 = queue_0.__aiter__()
        queue_0.task_done()
        var_2 = queue_0.__aiter__()
        var_3 = queue_0.get_nowait()
        var_4 = queue_0.get_nowait()
    except BaseException:
        pass

def test_case_9():
    try:
        queue_0 = module_0.Queue()
        str_0 = queue_0.__str__()
        var_0 = None
        queue_0.put_nowait(var_0)
        var_1 = None
        queue_iterator_0 = module_0._QueueIterator(var_1)
        var_2 = queue_0.__aiter__()
        var_3 = queue_0.get_nowait()
        int_0 = None
        queue_1 = module_0.Queue(int_0)
    except BaseException:
        pass

def test_case_10():
    try:
        int_0 = 2
        queue_0 = module_0.Queue(int_0)
        int_1 = 1
        queue_0.put_nowait(int_1)
        queue_0.put_nowait(int_0)
        int_2 = 3
        queue_0.put_nowait(int_2)
    except BaseException:
        pass