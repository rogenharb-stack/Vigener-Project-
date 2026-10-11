
def encrypt_vigenere(message, key):
    result = ""
    key_position = 0
    key = key.upper()

    for letter in message:
        if letter.isascii() and letter.isalpha():
            message_number = ord(letter.upper()) - ord('A')
            key_number = ord(key[key_position % len(key)]) - ord('A')

            new_number = (message_number + key_number) % 26
            new_letter = chr(new_number + ord('A'))

            if letter.islower():
                new_letter = new_letter.lower()

            result += new_letter
            key_position += 1
        else:
            result += letter

    return result


def decrypt_vigenere(message, key):
    result = ""
    key_position = 0
    key = key.upper()

    for letter in message:
        if letter.isascii() and letter.isalpha():
            message_number = ord(letter.upper()) - ord('A')
            key_number = ord(key[key_position % len(key)]) - ord('A')

            new_number = (message_number - key_number + 26) % 26
            new_letter = chr(new_number + ord('A'))

            if letter.islower():
                new_letter = new_letter.lower()

            result += new_letter
            key_position += 1
        else:
            result += letter

    return result


def make_rows(message):
    rows = []

    for i in range(0, len(message), 4):
        rows.append(message[i:i + 4])

    return rows


def join_rows(rows):
    return "".join(rows)


def change_columns(message, decrypt=False):
    rows = make_rows(message)

    column_order = [2, 0, 1, 3]

    if decrypt:
        column_order = [1, 2, 0, 3]

    for i in range(len(rows)):
        if len(rows[i]) == 4:
            old_row = rows[i]
            new_row = ""

            for position in column_order:
                new_row += old_row[position]

            rows[i] = new_row

    return join_rows(rows)


def change_rows(message, decrypt=False):
    rows = make_rows(message)

    row_order = [2, 0, 1]

    if decrypt:
        row_order = [1, 2, 0]

    start = 0

    while start + 3 <= len(rows):
        group = rows[start:start + 3]

        if all(len(row) == 4 for row in group):
            new_group = []

            for position in row_order:
                new_group.append(group[position])

            rows[start:start + 3] = new_group

        start += 3

    return join_rows(rows)


def main():
    print("Vigenere Cipher")
    print("1. Encrypt")
    print("2. Decrypt")

    choice = input("Choose an option: ").strip()

    if choice not in ["1", "2"]:
        print("Invalid choice.")
        return

    message = input("Enter your message: ")
    key = input("Enter your secret key: ").strip()

    if not key or not key.isascii() or not key.isalpha():
        print("The key must contain English letters only.")
        return

    if choice == "1":
        result = encrypt_vigenere(message, key)
        print("After Vigenere:", result)

        result = change_columns(result)
        print("After columns:", result)

        result = change_rows(result)
        print("After rows:", result)

        print("Final ciphertext:", result)

    else:
        result = change_rows(message, decrypt=True)
        print("After reversing rows:", result)

        result = change_columns(result, decrypt=True)
        print("After reversing columns:", result)

        result = decrypt_vigenere(result, key)
        print("Original message:", result)


if __name__ == "__main__":
    main()
