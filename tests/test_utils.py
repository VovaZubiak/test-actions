import uuid
from src.my_app.utils import generate_id, check_for_urgent


def test_generate_id_format():

    gen_id = generate_id()

    assert isinstance(gen_id, str)

    assert len(gen_id) == 36

    try:
        uuid.UUID(gen_id, version=4)
        is_valid_uuid = True
    except ValueError:
        is_valid_uuid = False

    assert is_valid_uuid is True, "Згенерований ID не є валідним UUID v4"


def test_check_for_urgent():
    assert check_for_urgent("Це дуже urgent завдання") is True
    assert check_for_urgent("Зроби це asap") is True
    assert check_for_urgent("Тут є 123") is True
    assert check_for_urgent("Звичайний текст") is False
