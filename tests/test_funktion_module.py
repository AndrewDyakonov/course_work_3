import funktion as funk


def test_get_json():
    """Тест get_json_to_list"""
    assert type(funk.get_json_to_list()) == list
    assert funk.get_json_to_list() is not None


def test_create_ex_class():
    """Тест функции создания списка экземпляра класса класса"""
    assert type(funk.create_ex_class()) == list
    assert funk.create_ex_class() is not None
