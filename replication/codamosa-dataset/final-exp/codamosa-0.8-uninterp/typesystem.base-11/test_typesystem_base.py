# Automatically generated by Pynguin.
import typesystem.base as module_0

def test_case_0():
    none_type_0 = None
    validation_result_0 = module_0.ValidationResult(value=none_type_0)

def test_case_1():
    int_0 = -1592
    position_0 = module_0.Position(int_0, int_0, int_0)

def test_case_2():
    float_0 = -443.0
    int_0 = 515
    position_0 = module_0.Position(int_0, int_0, int_0)
    bool_0 = position_0.__eq__(float_0)
    bool_1 = position_0.__eq__(position_0)
    str_0 = 'Sx3q]s?'
    message_0 = module_0.Message(text=str_0, key=int_0)
    int_1 = message_0.__hash__()

def test_case_3():
    int_0 = 6
    position_0 = module_0.Position(int_0, int_0, int_0)
    str_0 = position_0.__repr__()
    str_1 = 'e:o#U_sbN\x0bf(gX`\t'
    str_2 = 'g;xX]*;GY89'
    message_0 = module_0.Message(text=str_2)
    bool_0 = message_0.__eq__(str_1)
    str_3 = 'SAf1&A'
    base_error_0 = module_0.BaseError(text=str_3, code=str_3, key=str_3)
    int_1 = base_error_0.__len__()
    iterator_0 = base_error_0.__iter__()

def test_case_4():
    int_0 = 6
    position_0 = module_0.Position(int_0, int_0, int_0)
    str_0 = 'e:o#U_sbN\x0bf(gX`\t'
    message_0 = module_0.Message(text=str_0)
    str_1 = 'SAf1&A'
    base_error_0 = module_0.BaseError(text=str_1, code=str_1, key=str_1)
    int_1 = base_error_0.__len__()
    iterator_0 = base_error_0.__iter__()

def test_case_5():
    str_0 = ''
    base_error_0 = module_0.BaseError(text=str_0)

def test_case_6():
    str_0 = '+{*qTaV8%'
    base_error_0 = module_0.BaseError(text=str_0, code=str_0)
    int_0 = base_error_0.__hash__()

def test_case_7():
    validation_result_0 = module_0.ValidationResult()
    bool_0 = validation_result_0.__bool__()

def test_case_8():
    str_0 = 'pc-UHP'
    message_0 = module_0.Message(text=str_0)
    bool_0 = message_0.__eq__(message_0)
    validation_result_0 = module_0.ValidationResult()
    str_1 = validation_result_0.__repr__()
    str_2 = validation_result_0.__repr__()
    int_0 = -2703
    int_1 = -220
    position_0 = module_0.Position(int_0, int_1, int_0)

def test_case_9():
    validation_result_0 = None
    str_0 = 'KtkBbK$Ye\ru](Q'
    base_error_0 = module_0.BaseError(text=str_0, code=str_0)
    iterator_0 = base_error_0.__iter__()
    str_1 = 'm?G,@rv8LO*'
    list_0 = [str_1, str_1, str_1, str_1]
    message_0 = module_0.Message(text=str_1, code=str_1, index=list_0)
    bool_0 = message_0.__eq__(iterator_0)
    str_2 = 'fm(dW4|'
    int_0 = 2070
    int_1 = 186
    int_2 = -114
    position_0 = module_0.Position(int_0, int_1, int_2)
    message_1 = module_0.Message(text=str_2, code=str_2, start_position=position_0)
    bool_1 = message_1.__eq__(validation_result_0)
    bool_2 = position_0.__eq__(bool_1)
    int_3 = -243
    dict_0 = {validation_result_0: validation_result_0, int_3: validation_result_0, validation_result_0: int_3}
    validation_result_1 = module_0.ValidationResult(error=dict_0)
    bool_3 = validation_result_1.__bool__()
    str_3 = validation_result_1.__repr__()
    iterator_1 = validation_result_1.__iter__()

def test_case_10():
    str_0 = 'pc-UHP'
    message_0 = module_0.Message(text=str_0)
    list_0 = [message_0, message_0]
    bool_0 = message_0.__eq__(message_0)
    base_error_0 = module_0.BaseError(messages=list_0)
    str_1 = base_error_0.__repr__()
    validation_result_0 = module_0.ValidationResult()
    str_2 = validation_result_0.__repr__()
    base_error_1 = module_0.BaseError(text=str_1)
    str_3 = base_error_1.__str__()
    int_0 = -1768
    int_1 = -220
    position_0 = module_0.Position(int_0, int_1, int_0)
    bool_1 = position_0.__eq__(base_error_0)
    str_4 = base_error_0.__str__()
    bool_2 = base_error_0.__eq__(str_0)
    base_error_2 = module_0.BaseError(text=str_3, key=str_0)
    str_5 = base_error_2.__str__()
    message_1 = module_0.Message(text=str_0)
    str_6 = message_1.__repr__()
    int_2 = 2
    int_3 = 3
    position_1 = module_0.Position(int_2, int_0, int_3)
    bool_3 = position_0.__eq__(str_1)
    base_error_3 = module_0.BaseError(text=str_0)

def test_case_11():
    int_0 = 1
    int_1 = 2
    int_2 = 3
    position_0 = module_0.Position(int_0, int_1, int_2)
    int_3 = 4
    int_4 = 5
    int_5 = 6
    position_1 = module_0.Position(int_3, int_4, int_5)
    position_2 = module_0.Position(int_0, int_1, int_2)
    position_3 = module_0.Position(int_1, int_1, int_2)
    position_4 = module_0.Position(int_0, int_2, int_2)
    position_5 = module_0.Position(int_0, int_1, int_3)
    bool_0 = position_0.__eq__(position_1)
    bool_1 = position_0.__eq__(position_3)
    bool_2 = position_0.__eq__(position_4)
    bool_3 = position_0.__eq__(position_5)

def test_case_12():
    str_0 = 'A'
    str_1 = 'custom'
    message_0 = module_0.Message(text=str_0, code=str_1)
    message_1 = module_0.Message(text=str_0, code=str_1)
    var_0 = message_0 == message_1
    message_2 = module_0.Message(text=str_0, code=str_1)
    str_2 = 'B'
    message_3 = module_0.Message(text=str_2, code=str_1)
    message_4 = module_0.Message(text=str_0, code=str_1)
    str_3 = 'bar'
    message_5 = module_0.Message(text=str_0, code=str_3)
    var_1 = message_4 == message_5
    message_6 = module_0.Message(text=str_0, code=str_1)
    message_7 = module_0.Message(text=str_0, code=str_1, key=str_1)
    var_2 = message_6 == message_7
    message_8 = module_0.Message(text=str_0)
    message_9 = module_0.Message(text=str_0)
    var_3 = message_8 == message_9
    int_0 = 1
    int_1 = 2
    int_2 = 3
    position_0 = module_0.Position(int_0, int_1, int_2)
    message_10 = module_0.Message(text=str_0, position=position_0)
    position_1 = module_0.Position(int_0, int_1, int_2)
    position_2 = module_0.Position(int_0, int_1, int_2)
    message_11 = module_0.Message(text=str_0, start_position=position_1, end_position=position_2)
    var_4 = message_10 == message_11

def test_case_13():
    str_0 = 'A'
    str_1 = 'custom'
    message_0 = module_0.Message(text=str_0, code=str_1)
    message_1 = module_0.Message(text=str_0, code=str_1)
    var_0 = message_0 == message_1
    message_2 = module_0.Message(text=str_0, code=str_1)
    str_2 = 'B'
    message_3 = module_0.Message(text=str_2, code=str_1)
    var_1 = message_2 == message_3
    message_4 = module_0.Message(text=str_0, code=str_1)
    str_3 = 'bar'
    message_5 = module_0.Message(text=str_0, code=str_3)
    var_2 = message_4 == message_5
    message_6 = module_0.Message(text=str_0, code=str_1)
    str_4 = 'foo'
    message_7 = module_0.Message(text=str_0, code=str_1, key=str_4)
    var_3 = message_6 == message_7
    message_8 = module_0.Message(text=str_0)
    message_9 = module_0.Message(text=str_0)
    var_4 = message_8 == message_9
    int_0 = 1
    int_1 = 2
    int_2 = 3
    position_0 = module_0.Position(int_0, int_1, int_2)
    message_10 = module_0.Message(text=str_0, position=position_0)
    position_1 = module_0.Position(int_0, int_1, int_2)
    position_2 = module_0.Position(int_0, int_1, int_2)
    message_11 = module_0.Message(text=str_0, start_position=position_1, end_position=position_2)
    var_5 = message_10 == message_11

def test_case_14():
    str_0 = 'A'
    str_1 = 'custom'
    message_0 = module_0.Message(text=str_0, code=str_1)
    message_1 = module_0.Message(text=str_0, code=str_1)
    var_0 = message_0 == message_1
    message_2 = module_0.Message(text=str_0, code=str_1)
    str_2 = 'B'
    message_3 = module_0.Message(text=str_2, code=str_1)
    var_1 = message_2 == message_3
    message_4 = module_0.Message(text=str_0, code=str_1)
    str_3 = 'bar'
    message_5 = module_0.Message(text=str_0, code=str_3)
    var_2 = message_4 == message_5
    message_6 = module_0.Message(text=str_0, code=str_1)
    str_4 = 'foo'
    message_7 = module_0.Message(text=str_0, code=str_1, key=str_4)
    var_3 = message_6 == message_7
    message_8 = module_0.Message(text=str_0)
    var_4 = message_4 == message_8
    int_0 = 1
    int_1 = 2
    int_2 = 3
    position_0 = module_0.Position(int_0, int_1, int_2)
    position_1 = module_0.Position(int_0, int_1, int_2)
    position_2 = module_0.Position(int_0, int_1, int_2)
    message_9 = module_0.Message(text=str_0, start_position=position_1, end_position=position_2)
    list_0 = [message_3]
    base_error_0 = module_0.BaseError(messages=list_0)
    iterator_0 = base_error_0.__iter__()
    var_5 = message_2 == message_9