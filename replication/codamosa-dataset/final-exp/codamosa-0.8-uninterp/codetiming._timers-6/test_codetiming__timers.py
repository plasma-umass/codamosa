# Automatically generated by Pynguin.
import codetiming._timers as module_0

def test_case_0():
    timers_0 = module_0.Timers()

def test_case_1():
    str_0 = 'milliseconds'
    float_0 = -2797.48
    timers_0 = module_0.Timers()
    timers_0.add(str_0, float_0)

def test_case_2():
    timers_0 = module_0.Timers()
    timers_0.clear()

def test_case_3():
    timers_0 = module_0.Timers()
    str_0 = 'timing'
    float_0 = 1.0
    timers_0.add(str_0, float_0)
    float_1 = timers_0.min(str_0)

def test_case_4():
    str_0 = 'Test mean of Timers class'
    timers_0 = module_0.Timers()
    int_0 = 10
    timers_0.add(str_0, int_0)
    float_0 = timers_0.mean(str_0)

def test_case_5():
    timers_0 = module_0.Timers()
    str_0 = 'foobar'
    int_0 = 4
    timers_0.add(str_0, int_0)
    float_0 = timers_0.max(str_0)

def test_case_6():
    timers_0 = module_0.Timers()
    str_0 = '^9tpYz)\x0b\x0c{KjL%sKa'
    float_0 = 1164.94
    timers_0.add(str_0, float_0)
    float_1 = timers_0.median(str_0)