from footballanalysis.module_2 import module_2


def test_print_a_string():
    assert isinstance(module_2.type_an_object('Hello Newton!'), type(str))
