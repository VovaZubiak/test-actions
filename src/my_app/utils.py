import uuid


def generate_id() -> str:
    return str(uuid.uuid4())


def check_for_urgent(text: str) -> bool:

    if "123" in text:
        return True

    return "urgent" in text.lower() or "asap" in text.lower()
