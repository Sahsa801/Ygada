def to_secret_code(text):
    return "".join("0" if char.lower() in "aeiou" else "1" if char.isalpha() else char for char in text)

# Приклад використання
text = "Hello, world!"
print(to_secret_code(text))
