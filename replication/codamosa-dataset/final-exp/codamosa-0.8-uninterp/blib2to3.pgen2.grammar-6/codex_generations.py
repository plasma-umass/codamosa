

# Generated at 2022-06-13 17:50:00.183735
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.dfas = {256: ([[]], {1: 1}), 257: ([[]], {1: 1})}
    grammar.labels = [
        (256, "EMPTY"),
        (1, None),
        (257, "EMPTY"),
        (1, None),
    ]
    grammar.number2symbol = {256: "start", 257: "end"}
    grammar.symbol2number = {"end": 257, "start": 256}
    grammar.symbol2label = {256: 2, 257: 4}
    grammar.start = 257
    grammar.tokens = {1: 2}

    grammar.dump("temp.pkl")
    grammar = Grammar()
    grammar.load("temp.pkl")

# Generated at 2022-06-13 17:50:10.486863
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import io
    import pickle
    import unittest

    class Test(unittest.TestCase):
        def test_Grammar_dump_pickle(self):
            g = Grammar()
            g.tokens[token.NUMBER] = 1
            g.symbol2number["test_symbol"] = 2

            f = io.BytesIO()
            g.dump(f)
            f.seek(0)
            g2 = Grammar()
            g2.loads(f.read())
            self.assertEqual(g2.tokens[token.NUMBER], 1)
            self.assertEqual(g2.symbol2number["test_symbol"], 2)

    unittest.main(verbosity=0, exit=False)



# Generated at 2022-06-13 17:50:20.565345
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()

# Generated at 2022-06-13 17:50:21.837335
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load(__file__.replace('.py', '.pickle'))

# Generated at 2022-06-13 17:50:30.227281
# Unit test for method load of class Grammar
def test_Grammar_load():

    import pytest
    from . import pygram

    p = pygram.python_grammar
    filename = "./test.pkl"

    try:
        # test dump
        p.dump(filename)

        # test load
        q = Grammar()
        q.load(filename)

    finally:
        os.remove(filename)

    assert p.symbol2number == q.symbol2number
    assert p.number2symbol == q.number2symbol
    assert p.states == q.states
    assert p.dfas == q.dfas
    assert p.labels == q.labels
    assert p.keywords == q.keywords
    assert p.tokens == q.tokens
    assert p.symbol2label == q.symbol2label

# Generated at 2022-06-13 17:50:34.796693
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    class SubGrammar(Grammar):
        def __init__(self, numbers) -> None:
            super().__init__()

# Generated at 2022-06-13 17:50:40.066068
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()

    with tempfile.NamedTemporaryFile(mode="rb", delete=False) as f:
        g.dump(f.name)

    with open(f.name, "rb") as f:
        g2 = Grammar()
        g2.loads(f.read())
        assert g.dfas == g2.dfas
        assert g.states == g2.states
        assert g.keywords == g2.keywords

# Generated at 2022-06-13 17:50:46.371186
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    """
    Verify that Grammar.dump() works.
    """
    g = Grammar()
    g.number2symbol = {256: "start"}
    g.start = 256
    g.states = [[[(256, 257)], [(0, 0)]]]
    with tempfile.NamedTemporaryFile() as f:
        g.dump(f.name)
        os.fsync(f.file)
        f.seek(0)
        pickle.load(f)
    # Because the pickle module is so complicated, we just check that
    # dump() does *something*, rather than checking the accuracy of
    # the dump itself.
    # Also, we checked to be sure that the resulting pickle can be
    # read.

# Generated at 2022-06-13 17:50:56.604049
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    grammar = Grammar()
    grammar.symbol2number = {'and': 257, 'yield': 258, 'break': 259, 'not': 260}
    grammar.number2symbol = {257: 'and', 258: 'yield', 259: 'break', 260: 'not'}
    grammar.states = [
        [
            [(257, 1), (260, 2), (0, None)],
            [(258, 3), (0, None)],
            [(257, 2), (259, 4), (0, None)],
            [(0, None)],
            [(0, None)]
        ]
    ]
    grammar.dfas = {257: ([[(0, 1)]], {257: 1}), 258: ([[(0, 2)]], {256: 1})}

# Generated at 2022-06-13 17:51:04.418297
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pickle
    from io import BytesIO
    g1 = Grammar()

# Generated at 2022-06-13 17:51:13.327166
# Unit test for method load of class Grammar
def test_Grammar_load():
    # We use a known pickle dumps of class Grammar
    # to test the method load
    # This pickle was obtained from a previous version of this module
    # using this code:
    #   ...
    #   with open(filename, 'wb') as f:
    #       pickle.dump(gr.__dict__, f, pickle.HIGHEST_PROTOCOL)
    #   ...
    # In the future, this test can be update by using the method dump
    # and by testing against the pickle dumps generated by this method.
    from . import conv
    from . import pgen2
    from . import drivers
    from . import token


# Generated at 2022-06-13 17:51:18.855442
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .conv import convert
    from .pgen import tokenize

    g = Grammar()
    convert(tokenize("Grammar.txt"), g)
    dumpfile = tempfile.NamedTemporaryFile(delete=False)
    g.dump(dumpfile.name)

    g2 = Grammar()
    g2.load(dumpfile.name)

    dumpfile.close()

# Generated at 2022-06-13 17:51:22.479382
# Unit test for method load of class Grammar
def test_Grammar_load():
    from . import grammar
    from .pgen2 import tokenize

    g = grammar.Grammar()
    g.load(tokenize.__file__.replace(".py", ".pgen"))
    assert g.states[0][0] == [(g.symbol2label["newline"], 1)]



# Generated at 2022-06-13 17:51:24.167826
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.dump('Grammar.g')

# Generated at 2022-06-13 17:51:34.169616
# Unit test for method dump of class Grammar
def test_Grammar_dump():

    # This stdlib module has a few token constants defined in it.
    import _ast

    # Create a fake grammar.
    g = Grammar()
    g.symbol2number = {"foo": 257, "bar": 258}
    g.number2symbol = {257: "foo", 258: "bar"}
    g.start = 257
    g.dfas = {257: ([[(0, 1)], [(258, 2), (0, 1)], [(0, 1)]], {258: 1}), 258: ([[(0, 1)], [(0, 1)]], {})}
    g.labels = [(257, "foo"), (258, "bar"), (0, "EMPTY")]

# Generated at 2022-06-13 17:51:43.023557
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # Just call the method with some arguments.
    # This serves as a regression test for issue #359.
    # Issue #359 is fixed by a method _update added to class Grammar.
    # We'll test that method here, as well.
    class MyGrammar(Grammar):
        def __init__(self):
            super().__init__()
            # add a couple of attributes to MyGrammar
            self.another_attribute = "value2"
            self.yet_another_attribute = ["value3"]
    g = MyGrammar()
    with tempfile.NamedTemporaryFile(delete=False) as f:
        g.dump(f.name)
    # Now read back the pickle
    g2 = MyGrammar()
    g2.load(f.name)
    # the extra attributes should

# Generated at 2022-06-13 17:51:46.961746
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    filename = tempfile.mktemp(suffix=".pickle")
    try:
        g.dump(filename)
        g2 = Grammar()
        g2.load(filename)
    finally:
        try:
            os.unlink(filename)
        except OSError:
            pass

# Generated at 2022-06-13 17:51:50.214300
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.load(parse_table)
    assert isinstance(grammar, Grammar)
    assert grammar.async_keywords is False

# Generated at 2022-06-13 17:51:53.302960
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    assert not grammar.symbol2number
    grammar.load("Grammar.pickle")
    assert grammar.symbol2number


# Generated at 2022-06-13 17:52:02.070019
# Unit test for method load of class Grammar
def test_Grammar_load():
    # Create a dictionary that looks like the grammar data.
    d = {}
    for dict_attr in (
        "symbol2number",
        "number2symbol",
        "dfas",
        "keywords",
        "tokens",
        "symbol2label",
    ):
        d[dict_attr] = {}
    d["labels"] = []
    d["states"] = []
    d["start"] = 256

    # Normal code initializes with this dictionary and then updates the
    # Grammar instance with it, so we will do the same thing.
    g = Grammar()
    g._update(d)

# Generated at 2022-06-13 17:52:14.166474
# Unit test for method load of class Grammar
def test_Grammar_load():
    import re

    g = Grammar()
    g.load("Grammar/Grammar.pkl")

    assert g.start == 256
    assert 8 <= len(g.symbol2number) <= 11
    assert 257 in g.symbol2number.values()

    assert re.search(r"(\(\d+, \d+\),)+\(0, \d+\)", str(g.states[0]))
    assert re.search(r"(\(\d+, \d+\),)+\(0, \d+\)", str(g.states[1]))
    assert re.search(r"(\(\d+, \d+\),)+\(0, \d+\)", str(g.states[2]))

# Generated at 2022-06-13 17:52:15.860381
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g1 = g.load("pgen/python.g")
    assert g is g1

# Generated at 2022-06-13 17:52:21.546265
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .conv import convert

    g = Grammar()
    convert(g)

    with tempfile.NamedTemporaryFile() as f:
        g.dump(f.name)

        # create a new grammar and load the pickled version.
        g2 = Grammar()
        g2.load(f.name)

    assert repr(g) == repr(g2)



# Generated at 2022-06-13 17:52:31.538329
# Unit test for method load of class Grammar
def test_Grammar_load():
    """Test Grammar.load"""
    import os
    import glob
    import pickle
    from . import pgen2

    path = os.path.dirname(__file__)
    for fn in glob.glob(os.path.join(path, "Grammar*.bin")):
        with open(fn, "rb") as f:
            g = pickle.load(f)
        assert isinstance(g, Grammar)
        g2 = pgen2.parse_grammar(os.path.splitext(fn)[0])
        assert isinstance(g2, pgen2.Grammar)
        assert g.dfas == g2.dfas
        assert g.keywords == g2.keywords
        assert g.labels == g2.labels
        assert g.number2symbol == g2

# Generated at 2022-06-13 17:52:38.694480
# Unit test for method load of class Grammar
def test_Grammar_load():
    import pytest
    g = Grammar()
    t = tempfile.NamedTemporaryFile()
    g.dump(t.name)
    g2 = Grammar()
    g2.load(t.name)
    assert g.tokens == g2.tokens
    assert g.symbol2number == g2.symbol2number
    assert g.number2symbol == g2.number2symbol
    assert g.states == g2.states
    assert g.dfas == g2.dfas
    assert g.labels == g2.labels
    assert g.start == g2.start
    assert g.keywords == g2.keywords



# Generated at 2022-06-13 17:52:40.496531
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    gr = Grammar()
    gr.dump("this.gram")



# Generated at 2022-06-13 17:52:47.384007
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import os
    import pathlib
    from . import conv, pgen

    tempfile = pathlib.Path(str(pathlib.Path.cwd()) + "/temp.pickle")
    if tempfile.exists():
        os.remove(tempfile)

    g = conv.parse_grammar(pgen.graminit.grammar)
    g.dump(tempfile)
    assert tempfile.exists()

    os.remove(tempfile)

# Generated at 2022-06-13 17:52:51.060973
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .parse import Parser
    from .pgen2 import driver
    g = driver.load_grammar("Grammar.txt")
    assert isinstance(g, Grammar)
    assert isinstance(Parser(g), Parser)

# Generated at 2022-06-13 17:53:02.642531
# Unit test for method load of class Grammar
def test_Grammar_load():
    """Unit test for method load of class Grammar."""
    g = Grammar()
    g.loads(GRAMMAR_PICKLE)
    assert g.keywords['async'] == 401

# Module test =
#     parser = Parser()
#     print(parser.parse(textwrap.dedent("""
#     def f():
#         '''async'''
#         pass
#     """)))


# Generated at 2022-06-13 17:53:04.706733
# Unit test for method load of class Grammar
def test_Grammar_load():
    gram = Grammar()
    gram.load('/home/zengfeng/pythondev/mygrammar.py')


# Generated at 2022-06-13 17:53:13.242510
# Unit test for method load of class Grammar
def test_Grammar_load():
    assert Grammar()._update({'symbol2number':{}, 'number2symbol':{}, 'states':[], 'dfas':{}, 'labels':[(0, 'EMPTY')], 'keywords':{}, 'tokens':{}, 'symbol2label':{}, 'start': 256}) == None


# Generated at 2022-06-13 17:53:24.397848
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # use a temp directory
    import tempfile
    import os
    import shutil
    import glob

    temp_dir = tempfile.mkdtemp()
    # create a Grammar object
    g = Grammar()
    g.symbol2number = {"a": 1}
    g.number2symbol = {1: "a"}
    g.states = [[(1, 2)], [(2, 3)], [(3, 4)]]
    g.dfas = {1: ([(1, 2)], {0: 1})}
    g.labels = [(0, "EMPTY"), (1, None), (2, None), (3, None)]
    g.keywords = {}
    g.tokens = {}
    g.symbol2label = {"symbol": 1}
    g.start = 256
   

# Generated at 2022-06-13 17:53:32.188940
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import py
    import sys
    import re
    import tempfile
    import os
    import io

    new_out = io.StringIO()
    old_stdout, sys.stdout = sys.stdout, new_out
    # The module 'py' may be missing
    try:
        py.test.skip('This test is failing at the moment')
    finally:
        sys.stdout = old_stdout
    test_file = re.sub('sre_parse.pyc?', 'Test_sre_parse.py', __file__)
    if not os.path.exists(test_file):
        test_file = re.sub('sre_parse.pyc?', 'test_sre_parse.py', __file__)
    assert os.path.exists(test_file)
    test

# Generated at 2022-06-13 17:53:36.906950
# Unit test for method load of class Grammar
def test_Grammar_load():
    import unittest

    class TestCase(unittest.TestCase):
        """Unit test for class Grammar"""

        def test_load(self):
            test_text = b"123"
            g = Grammar()
            g.loads(test_text)

    unittest.main(
        None, None, [unittest.__file__, TestCase.__name__], failfast=True, buffer=False
    )

# Generated at 2022-06-13 17:53:46.461174
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()

# Generated at 2022-06-13 17:53:50.913501
# Unit test for method load of class Grammar
def test_Grammar_load():
    import py_gdb
    filename = os.path.join(py_gdb.__path__[0], "Grammar.pickle")
    g = Grammar()
    g.load(filename)

if __name__ == '__main__':
    test_Grammar_load()

# Generated at 2022-06-13 17:53:58.165520
# Unit test for method load of class Grammar
def test_Grammar_load():
    # Create a Grammar object
    grammar = Grammar()

    # Make sure instance variables are set to the expected values
    assert grammar.symbol2number == {}
    assert grammar.number2symbol == {}
    assert grammar.states == []
    assert grammar.dfas == {}
    assert grammar.labels == [(0, "EMPTY")]
    assert grammar.keywords == {}
    assert grammar.tokens == {}
    assert grammar.symbol2label == {}
    assert grammar.start == 256
    assert grammar.async_keywords == False

# Generated at 2022-06-13 17:54:01.653329
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.symbol2number = {'foo': 3, 'bar': 4}
    grammar.load(os.path.join(os.path.dirname(__file__), 'Grammar.pickle'))
    assert grammar.symbol2number['foo'] == 'foo'

# Generated at 2022-06-13 17:54:06.688504
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load('data/Grammar.pickle')
    assert g.async_keywords
    g.dump('test.pickle')
    g.load('test.pickle')
    assert g.async_keywords

# Generated at 2022-06-13 17:54:14.912024
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    def process_dump_file(dump_file: Path, full_dump_file: Path) -> None:
        if not os.path.isfile(dump_file):
            dump_file = full_dump_file
        gram = Grammar()
        gram.load(dump_file)
        gram.start = 1
        gram.dump(dump_file)
    import sys
    from . import pgen2
    from . import pgen2_unittest_support
    def dump_Grammar(PythonVersion: Tuple[int, int]) -> None:
        test_dir = pgen2_unittest_support.get_test_dir(PythonVersion)
        dump_file = os.path.join(test_dir, "Grammar.pkl")

# Generated at 2022-06-13 17:54:29.497711
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .conv import Conv
    from .pgen import pgen
    from .parse import parse_grammar
    import io

    f = io.StringIO()
    # Set up grammar object from pgen
    pgen(f)
    f.seek(0)
    conv = Conv(f)

    # Initialize grammar object from conv
    grammar = parse_grammar(conv.readline, conv.get_all_symbol_names())

    # Dump pickle file to memory
    f = io.BytesIO()
    grammar.dump(f)

    # Initialize grammar object from pickle file
    grammar = Grammar()
    grammar.loads(f.getvalue())

    # Load dump to memory (and test file-like object)
    f = io.BytesIO(f.getvalue())
    grammar.load(f)


# Generated at 2022-06-13 17:54:35.583146
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from .conv import convert
    import sys
    from .pgen2 import driver
    from .pgen2 import tokenize

    g = Grammar()
    dirname = os.path.dirname(__file__)
    convert(g, dirname)
    g.dump(sys.argv[1])
    g = Grammar()
    g.load(sys.argv[1])
    driver.load_grammar(g)
    with open(sys.argv[2]) as f:
        t = tokenize.generate_tokens(f.readline)
        while 1:
            try:
                token_type, token_string, _, _, _ = next(t)
            except tokenize.TokenError:
                break
            driver.addtoken(token_type, token_string)

# Generated at 2022-06-13 17:54:38.034550
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    filename = "TEST_GRAMMAR_DUMP"
    g = Grammar()
    g.dump(filename)



# Generated at 2022-06-13 17:54:45.885822
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.tokens[2] = 3
    g.tokens[5] = 3
    g.keywords = {'a': 1, 'b': 2}
    g.labels = [(0, 'EMPTY'), (4, 'foo'), (4, None), (4, None), (4, 'bar')]
    g.start = 4
    g.number2symbol = {1: 'a', 2: 'b', 4: 'bar'}
    g.symbol2number = {'a': 1, 'b': 2, 'bar': 4}
    g.symbol2label = {'bar': 4}
    states = [[], [[(2, 1)], [(5, 1)]], [], []]
    states[1][0].append((1, 1))

# Generated at 2022-06-13 17:54:51.325316
# Unit test for method load of class Grammar
def test_Grammar_load():
    t = Grammar()
    assert t.symbol2number == {}
    assert t.number2symbol == {}
    assert t.states == []
    assert t.dfas == {}
    assert t.labels == [(0, "EMPTY")]
    assert t.keywords == {}
    assert t.tokens == {}
    assert t.symbol2label == {}
    assert t.start == 256


# Generated at 2022-06-13 17:54:58.196393
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # Test issue #2839: dump() doesn't work on older versions of Python.
    # In Python 3.5 and older, Pickle can't create the protocol 5 version of
    # pickle.DEFAULT_PROTOCOL, which results in an argument error.
    # This test is skipped on 3.5 and older.
    from sys import version_info as ver
    from unittest import SkipTest

    if ver.major == 3 and ver.minor <= 5:
        raise SkipTest("test not implemented for Python 3.5 and older")

    from .conv import parse_grammar
    from .pgen2 import tokenize

    g = parse_grammar("Grammar.txt", "Grammar.pickle", create_tables=True)

# Generated at 2022-06-13 17:55:00.817344
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load(__file__.replace(".py", ".pkl"))
    return g

# Generated at 2022-06-13 17:55:16.289267
# Unit test for method load of class Grammar
def test_Grammar_load():
    t = Grammar()
    t.load('Grammar.pickle')
    assert len(t.states) == 18
    assert len(t.tokens) == 40
    assert len(t.labels) == 143
    assert t.states[0][0][0][0] == 258  # ('START', 0)
    assert t.states[-1][0][0][0] == 261  # ('single_input', 2)
    assert t.tokens[token.NAME] == 261
    assert t.states[-1][1][0][0] == 261  # ('single_input', 2)
    assert t.tokens[token.NEWLINE] == 266
    assert t.states[-1][2][0][0] == 261  # ('single_input', 2)
    assert t.tok

# Generated at 2022-06-13 17:55:24.332968
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import unittest
    import unittest.mock

    g = Grammar()
    dump_result = unittest.mock.MagicMock()
    with unittest.mock.patch("pickle.dump", dump_result):
        with unittest.mock.patch("tempfile.NamedTemporaryFile", spec=True) as tf:
            f = tf.return_value.__enter__.return_value
            f.name = "tempfile_name"

            g.dump("filename.pkl")
            tf.assert_called_once_with(dir=".", delete=False)
            dump_result.assert_called_once_with(f, g.__getstate__(), pickle.HIGHEST_PROTOCOL)
            f.close.assert_called_once_with()

# Generated at 2022-06-13 17:55:30.524132
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    class FakeFile(object):
        def __init__(self):
            self.contents = b""
        def write(self, s):
            self.contents += s
        def close(self):
            pass
    fake_file = FakeFile()
    g = Grammar()
    g.dump(fake_file)
    if not fake_file.contents or b"Grammar" not in fake_file.contents:
        raise AssertionError("Grammar dump test failed: did not write 'Grammar' to file")

# Generated at 2022-06-13 17:55:40.113567
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import re
    import pickle
    f = tempfile.NamedTemporaryFile(delete=False)
    f.close()
    os.unlink(f.name)
    a = Grammar()
    a.dump(f.name)
    a = pickle.dumps(a, pickle.HIGHEST_PROTOCOL)
    b = pickle.dumps(Grammar(), pickle.HIGHEST_PROTOCOL)
    assert a == b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    test_Grammar_dump()

# Generated at 2022-06-13 17:55:43.180845
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    test_file = tempfile.NamedTemporaryFile(delete=False)
    g.dump(test_file.name)
    g.load(test_file.name)
    os.unlink(test_file.name)

# Generated at 2022-06-13 17:55:53.728989
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.symbol2number = {"hello": -1}
    g.number2symbol = {-1: "hello"}
    g.start = 1
    g.keywords = {"and": 2}
    g.tokens = {3: 4}
    g.symbol2label = {"def": 5}
    td = tempfile.mkdtemp()
    g.dump(os.path.join(td, "table.pkl"))

    g2 = Grammar()
    g2.load(os.path.join(td, "table.pkl"))
    assert g2.symbol2number == g.symbol2number
    assert g2.number2symbol == g.number2symbol
    assert g2.start == g.start

# Generated at 2022-06-13 17:55:54.965835
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.dump("foo")


# Generated at 2022-06-13 17:56:02.408969
# Unit test for method load of class Grammar
def test_Grammar_load():
    gr = Grammar()

    def load(filename, expected_start):
        gr.load(filename)
        assert gr.start == expected_start

    load("Grammar/Grammar25.pkl", 256)
    load("Grammar/Grammar27.pkl", 269)
    load("Grammar/Grammar30.pkl", 272)
    load("Grammar/Grammar32.pkl", 273)
    load("Grammar/Grammar33.pkl", 274)
    load("Grammar/Grammar34.pkl", 276)
    load("Grammar/Grammar35.pkl", 275)
    load("Grammar/Grammar36.pkl", 278)
    load("Grammar/Grammar37.pkl", 279)

# Generated at 2022-06-13 17:56:11.157557
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    g = Grammar()
    g.start = 2
    g.states = [[[(1, 2)], [(1, 3)]]]
    g.labels = [(1, "x"), (2, None)]
    g.symbol2number = {"a": 1}
    g.number2symbol = {1: "a"}
    g.keywords = {"if": 1}
    g.tokens = {1: 2}
    filename = "c:\\temp\\tmp.txt"
    g.dump(filename)
    g.load(filename)

# Generated at 2022-06-13 17:56:21.535758
# Unit test for method load of class Grammar
def test_Grammar_load():
    # build a grammar
    gr = Grammar()
    gr.symbol2number = {'a':1}
    gr.number2symbol = {1:'a'}
    gr.labels = [(1,None), (2,None)]
    gr.states = [[(1,1), (2,2)]]
    gr.dfas = {1:(gr.states[0],{1:1, 2:2})}
    gr.keywords = {}
    gr.tokens = {}
    gr.symbol2label = {'a':1}
    gr.start = 256
    gr.async_keywords = False
    # dump the grammar
    fd, fn = tempfile.mkstemp(dir=os.curdir, suffix='.pickle')

# Generated at 2022-06-13 17:56:29.047352
# Unit test for method load of class Grammar
def test_Grammar_load():
    def check(name: str, value: Any) -> None:
        assert getattr(g, name) == value

    g = Grammar()
    d = {
        "symbol2number": {"a": 1},
        "number2symbol": {1: "a"},
        "states": [[]],
        "dfas": {},
        "labels": [1],
        "keywords": {},
        "tokens": {},
        "symbol2label": {},
    }
    g.loads(pickle.dumps(d))
    check("symbol2number", {"a": 1})
    check("number2symbol", {1: "a"})
    check("states", [[]])
    check("dfas", {})
    check("labels", [1])

# Generated at 2022-06-13 17:56:39.221038
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.load("Grammar.pickle")

    assert grammar.symbol2number == {
        "STRING": 258,
        "NUMBER": 259,
        "ASYNC": 260,
        "AWAIT": 261,
    }
    assert grammar.number2symbol == {
        258: "STRING",
        259: "NUMBER",
        260: "ASYNC",
        261: "AWAIT",
    }

# Generated at 2022-06-13 17:56:51.218812
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import os
    import shutil
    import sys
    import unittest

    try:
        import conv
        import pgen
    except ImportError:
        return

    if sys.version_info[0] >= 3 and sys.version_info[1] <= 3:
        # These tests did not run on Python 3.3 because the pickled
        # file cannot be unpickled on Python 3
        return

    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch

    class GrammarTestCase(unittest.TestCase):
        """Test Grammar.dump"""

        def setUp(self) -> None:
            self.testdir = tempfile.mkdtemp(prefix="py-test-")

        def tearDown(self) -> None:
            shutil.rmtree

# Generated at 2022-06-13 17:57:02.860237
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    def test_pickle_file(filename):
        with open(filename, "rb") as f:
            pickle.load(f)

    g = Grammar()
    g.symbol2number["foo"] = 12
    g.number2symbol[2] = "bar"
    g.dfas[1] = [], {}
    g.labels = [
        (1, "NOOP"), (2, None), (3, "bar"), (4, "bar"), (5, "bar"), (6, "bar")
    ]
    g.keywords = {"foo": 1, "bar": 0}
    g.tokens = {1: 1, 2: 0, 3: 3}
    g.symbol2label = {"foo": 2, "bar": 3}
    g.start = 100

    tmp_file

# Generated at 2022-06-13 17:57:16.987518
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    class DumpTestGrammar(Grammar):
        def __init__(self):
            super().__init__()
            self.symbol2number = dict(a=257)

# Generated at 2022-06-13 17:57:18.843444
# Unit test for method load of class Grammar
def test_Grammar_load():
    import re
    assert re.match("^[a-f0-9]{32}$", Grammar().load(""))

# Generated at 2022-06-13 17:57:33.840018
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import pickle
    from .parse import Grammar

    Grammar().dump("Grammar.dump")
    with open("Grammar.dump", "rb") as f:
        dump = pickle.load(f)

# Generated at 2022-06-13 17:57:41.710175
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import doctest
    import typing
    from . import pgen2
    from .pgen2 import tokenize, token

    token_map = dict((y, x) for x, y in token.__dict__.items() if isinstance(y, int))

    # Test cases for dump and loads.
    def table(name: str) -> None:
        """
        Print a nice table of the grammar rules contained in the
        grammar module / pickle file named NAME.
        """
        print("Symbol", ":", "Production")
        print("-" * 10, ":", "-" * 20)
        g = pgen2.driver.load_grammar(name)

# Generated at 2022-06-13 17:57:56.058491
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from . import pgen2
    from . import token

    class MockClose(object):
        def __init__(self) -> None:
            self.name = "tmpfile"
            self.data = b""

        def write(self, data: bytes) -> int:
            self.data += data
            return len(data)

    path = "tmp"
    original_NamedTemporaryFile = tempfile.NamedTemporaryFile
    tempfile.NamedTemporaryFile = MockClose
    with open("Grammar.pickle", "rb") as f:
        gram = pgen2.load_grammar(f.read())
    tempfile.NamedTemporaryFile = original_NamedTemporaryFile
    gram.dump(path)


# Generated at 2022-06-13 17:58:05.733954
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    from . import pgen

    # Create a subclass of Grammar, with a very simple grammar
    class SimpleGrammar(Grammar):
        def __init__(self) -> None:
            super().__init__()
            self.start = 256
            self.dfas = {
                self.start: (
                    [[(256, 1), (257, 2)], [(257, 3), (0, 3)], [(0, 2)]],
                    {0: 1, 256: 1, 257: 1},
                )
            }
            self.async_keywords = False
            self.symbol2number = {"A": 256, "B": 257}
            self.number2symbol = {256: "A", 257: "B"}

# Generated at 2022-06-13 17:58:15.605476
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    # Test for a subclass of Grammar (python and python2 use a
    # different subclass)
    from .pgen2 import driver

    # We are currently only testing the dump and load methods and the
    # report method is not used or tested.
    # pylint: disable=W0612
    def report(_self) -> None:
        pass  # pragma: no cover

    # Make a dummy Grammar
    g = Grammar()
    g.symbol2number = {"foo": 1}
    g.number2symbol = {1: "foo"}
    g.states = [[[(1, 0)], [(1, 0), (2, 1)]]]
    g.dfas = {1: (g.states[0], {})}

# Generated at 2022-06-13 17:58:17.126460
# Unit test for method load of class Grammar
def test_Grammar_load():
	gram = Grammar()
	gram.load("Python/Grammar.pkl")

# Generated at 2022-06-13 17:58:18.767181
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    grammar = Grammar()
    with tempfile.NamedTemporaryFile(delete=False) as f:
        grammar.dump(f.name)

# Generated at 2022-06-13 17:58:44.941969
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    dfas: List[DFA] = []
    states = [
        [(0, 0), (1, 1)],
        [(0, 1), (1, 1)],
        [(0, 1), (1, 2)],
        [(0, 2), (1, 3)],
        [(0, 3), (1, 4)],
        [(0, 4), (1, 5)],
        [(0, 5), (1, 0)],
    ]
    # states of dfas
    dfas.append(states)
    dfas.append([[(0, 0), (1, 1)]])
    dfas.append([[(0, 1), (1, 0)]])

    grammar.dfas[0] = (dfas[0], {0: 1})
    grammar.df

# Generated at 2022-06-13 17:58:51.168257
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()

# Generated at 2022-06-13 17:58:53.807715
# Unit test for method load of class Grammar
def test_Grammar_load():
    filename = "hello"
    g = Grammar()
    g.load(filename) # The name of the file must be the same as the test function



# Generated at 2022-06-13 17:58:59.791338
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()

# Generated at 2022-06-13 17:59:09.253825
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import textwrap
    import pathlib
    from io import StringIO
    from . import pgen2

    g = pgen2.generate_grammar()
    s = StringIO()
    g.dump(s)

    g2 = Grammar()
    g2.loads(s.getvalue())
    assert g2 is not None

    # Test method dump_to_file
    g3 = Grammar()
    s = StringIO()
    g.dump_to_file(s)
    g3.loads(s.getvalue())

# Unit tests for methods load (and loads) and copy of class Grammar

# Generated at 2022-06-13 17:59:11.839871
# Unit test for method load of class Grammar
def test_Grammar_load():
    g = Grammar()
    g.load(os.path.join(os.path.dirname(__file__), "Grammar.txt"))
    g.report()

# Generated at 2022-06-13 17:59:23.655210
# Unit test for method load of class Grammar
def test_Grammar_load():
    grammar = Grammar()
    grammar.states.append([(0, 1)])
    grammar.states.append([(1, 3)])
    grammar.states.append([(2, 2)])
    grammar.states.append([])
    grammar.keywords.update({"yield": 0})
    assert grammar.keywords["yield"] == 0
    assert grammar.states[0][0] == (0, 1)
    assert grammar.states[1][0] == (1, 3)
    assert grammar.states[2][0] == (2, 2)
    with tempfile.TemporaryDirectory() as tempdir:
        filename = os.path.join(tempdir, "testgrammar.py")
        grammar.dump(filename)
        grammar2 = Grammar()
        grammar2.load(filename)
        assert grammar

# Generated at 2022-06-13 17:59:32.074307
# Unit test for method load of class Grammar
def test_Grammar_load():
    from .pgen2 import driver

    tokens = driver.tokenize_file(driver.grammar_file)
    grammar = driver.parse_tokens(tokens, symbols=driver.symbol2number)

    # Write the grammar obtained from parsing to a temporary file
    _, name = tempfile.mkstemp()
    grammar.dump(name)

    # Load the grammar from the temporary file and compare it with the
    # original
    loaded = Grammar()
    loaded.load(name)

    # Compare the grammar obtained from parsing with the grammar loaded
    # from the temporary file
    assert loaded.symbol2number == grammar.symbol2number
    assert loaded.number2symbol == grammar.number2symbol
    assert loaded.states == grammar.states
    assert loaded.dfas == grammar.dfas
    assert loaded.lab

# Generated at 2022-06-13 17:59:33.392864
# Unit test for method load of class Grammar
def test_Grammar_load():
    pass


# Generated at 2022-06-13 17:59:35.650800
# Unit test for method dump of class Grammar
def test_Grammar_dump():
    import os
    pkgdir = os.path.dirname(os.path.dirname(__file__))
    g = Grammar()
    g.dump(pkgdir + '/Grammar.txt')
    g.loads(open(pkgdir + '/Grammar.txt', "rb").read())

# Generated at 2022-06-13 17:59:46.322887
# Unit test for method load of class Grammar
def test_Grammar_load():
    tables = Grammar()
    tables.load('Grammar.pkl')
    assert(len(tables.labels) == 3)
    assert(tables.labels[1][1] == 'AT')
    assert(tables.labels[2][1] == ':')