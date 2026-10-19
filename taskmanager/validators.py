VALID_PRIORITIES = ("low", "medium", "high")


def validate_title(title):
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Judul tugas tidak boleh kosong")
    if len(title) > 100:
        raise ValueError("Judul tugas maksimal 100 karakter")
    return title.strip()


def validate_priority(priority):
    if priority not in VALID_PRIORITIES:
        raise ValueError(f"Prioritas harus salah satu dari {VALID_PRIORITIES}")
    return priority