# Automatically generated by Pynguin.
import docstring_parser.numpydoc as module_0
import docstring_parser.common as module_1

def test_case_0():
    try:
        str_0 = 'QKa!JyP+]#\r54cf'
        str_1 = 'Q0*tpvz1wXn\x0bX1tlK\x0c}'
        deprecation_section_0 = module_0.DeprecationSection(str_0, str_1)
        numpydoc_parser_0 = module_0.NumpydocParser(deprecation_section_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '        A test sentence.\n\n        A longer sentence.\n\n        Parameters\n        ----------\n        a : bool\n            A bool\n        b, optional\n            A bool\n\n        Other Parameters\n        ----------------\n        b : int, optional\n            A bool\n\n        Returns\n        -------\n        bool\n            A bool\n\n        Yields\n        ------\n        x : bool, optional\n            A bool\n\n        Raises\n        ------\n        ValueError\n            A bool\n\n        Examples\n        --------\n        A bool\n\n        Warnings\n        --------\n        A bool\n\n        See Also\n        --------\n        A bool\n\n        Notes\n        -----\n        A bool\n\n        References\n        ----------\n        A bool\n\n        Example\n        -------\n        A bool\n        '
        deprecation_section_0 = module_0.DeprecationSection(str_0, str_0)
        k_v_section_0 = module_0._KVSection(str_0, str_0)
        str_1 = 'vpPYS'
        str_2 = 'value'
        deprecation_section_1 = module_0.DeprecationSection(str_1, str_2)
        iterable_0 = k_v_section_0.parse(str_0)
        numpydoc_parser_0 = module_0.NumpydocParser(iterable_0)
        docstring_0 = numpydoc_parser_0.parse(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'deprecated'
        str_1 = 'deprecation'
        deprecation_section_0 = module_0.DeprecationSection(str_0, str_1)
        str_2 = '.. deprecated:: 0.2.2\n   Test'
        iterable_0 = deprecation_section_0.parse(str_2)
        int_0 = 0
        var_0 = next(iterable_0)[int_0]
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '8deprecated'
        str_1 = 'deprecation'
        deprecation_section_0 = module_0.DeprecationSection(str_0, str_1)
        iterable_0 = deprecation_section_0.parse(str_0)
        int_0 = -33
        numpydoc_parser_0 = module_0.NumpydocParser()
        var_0 = next(iterable_0)[int_0]
    except BaseException:
        pass

def test_case_4():
    try:
        numpydoc_parser_0 = module_0.NumpydocParser()
        docstring_0 = module_1.Docstring()
        str_0 = '5{khT['
        str_1 = 'raise'
        str_2 = 'E'
        str_3 = 'c@\r7^*nd'
        raises_section_0 = module_0.RaisesSection(str_3, str_0)
        str_4 = 'Attributes'
        docstring_1 = module_0.parse(str_4)
        docstring_2 = module_0.parse(str_2)
        str_5 = 'RyQhL/Nm'
        str_6 = '3)e1UA'
        k_v_section_0 = module_0._KVSection(str_6, str_1)
        iterable_0 = k_v_section_0.parse(str_5)
        numpydoc_parser_1 = module_0.NumpydocParser(iterable_0)
    except BaseException:
        pass