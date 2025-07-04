def clean_text(text):
    """Удаляет пробелы по краям и приводит к нижнему регистру"""
    return text.strip().lower()

# Пример использования:
dirty_email = "  HeLLo@Email.COM  "
print(clean_text(dirty_email))  # => hello@email.com
