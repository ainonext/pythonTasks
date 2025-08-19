
import string as st

digits = st.digits
lowercase = st.ascii_lowercase
uppercase = st.ascii_uppercase
special = "_!@#$%^&"

all_allowed = digits + lowercase + uppercase + special


def check_password(password: str) -> tuple[bool, str]:
    """
    Проверка пароля.
    """
    reasons = []

    if not (8 <= len(password) <= 15):
        reasons.append("Длина пароля от 8 до 15 символов.")

    for ch in password:
        if ch not in all_allowed:
            reasons.append(f"Недопустимый символ: '{ch}'")
            break

    if not any(ch in digits for ch in password):
        reasons.append("Пароль должен содержать хотя бы одну цифру.")

    if not any(ch in lowercase for ch in password):
        reasons.append("Пароль должен содержать хотя бы одну строчную букву.")

    if not any(ch in uppercase for ch in password):
        reasons.append("Пароль должен содержать хотя бы одну прописную букву.")

    if not any(ch in special for ch in password):
        reasons.append("Пароль должен содержать хотя бы один спецсимвол из набора '_!@#$%^&'.")

    if reasons:
        return False, " ".join(reasons)
    else:
        return True, "Пароль принят."


def main():
    max_attempts = 5
    for attempt in range(1, max_attempts + 1):
        password = input(f"Попытка {attempt}/{max_attempts}. Введите пароль: ")
        ok, msg = check_password(password)
        print(msg)
        if ok:
            print("Доступ разрешён.")
            break
    else:
        print("Превышено количество попыток. Доступ запрещён.")


if __name__ == "__main__":
    main()

