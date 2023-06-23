def backpack(capacity: int, stuff: dict) -> list[str]:
    packaging_option = []
    summary = []
    for key, value in stuff.items():
        if value <= capacity:
            capacity -= value
            packaging_option.append(key)
    return packaging_option