# Automatically generated by Pynguin.
import pytutils.env as module_0

def test_case_0():
    pass

def test_case_1():
    generator_0 = module_0.parse_env_file_contents()
    str_0 = "\n    Turn a function to a bound method on an instance\n\n    >>> class Foo(object):\n    ...     def __init__(self, x, y):\n    ...         self.x = x\n    ...         self.y = y\n    >>> foo = Foo(2, 3)\n    >>> my_unbound_method = lambda self: self.x * self.y\n    >>> bind(foo, my_unbound_method, 'multiply')\n    >>> foo.multiply()  # noinspection PyUnresolvedReferences\n    6\n\n    :param object instance: some object\n    :param callable func: unbound method (i.e. a function that takes `self` argument, that you now\n        want to be bound to this class as a method)\n    :param str as_name: name of the method to create on the object\n    "
    str_1 = module_0.expand(str_0)

def test_case_2():
    str_0 = '/\r3hi&'
    ordered_dict_0 = module_0.load_env_file(str_0)

def test_case_3():
    str_0 = 'FOO =bar'
    str_1 = 'H{LLO= world'
    str_2 = 'SPACED = both '
    str_3 = [str_0, str_1, str_2]
    generator_0 = module_0.parse_env_file_contents(str_3)
    var_0 = list(generator_0)
    str_4 = "SINGLE='single_quotes'"
    str_5 = 'DOUBLE="double_quotes"'
    str_6 = [str_4, str_5]
    generator_1 = module_0.parse_env_file_contents(str_6)
    var_1 = list(generator_1)

def test_case_4():
    str_0 = 'THISIS=~/a/test'
    str_1 = 'YOLO=~/swaggins/$NONEXISTENT_VA_THAT_DOES_NOT_EXIT'
    str_2 = [str_1, str_0, str_1]
    var_0 = dict()
    ordered_dict_0 = module_0.load_env_file(str_2, var_0)