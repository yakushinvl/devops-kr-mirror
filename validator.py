import re

def validate_phone(phone: str) -> bool:
    """Валидация российского номера телефона."""
    pattern = r'^\+?7\d{10}$'
    return bool(re.match(pattern, phone.replace('-', '').replace(' ', '')))

def validate_snils(snils: str) -> bool:
    """Валидация номера СНИЛС."""
    cleaned = snils.replace('-', '').replace(' ', '')
    return len(cleaned) == 11 and cleaned.isdigit()

def validate_email(email: str) -> bool:
    """Валидация email адреса."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
