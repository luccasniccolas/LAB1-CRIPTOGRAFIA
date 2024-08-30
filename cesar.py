import sys

def cesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha(): # verifica que el caracter actual sea alfabetico
            shift_amount = shift % 26 # calculamos el corrimiento, cuando es mayor a 26 aplica el modulo para ver cual es el corrimiento correcto
            shifted = ord(char) + shift_amount
            if char.islower():
                if shifted > ord('z'): # cuando la suma de la posicion actual más el corrimiento es mayor a 26, la letra encriptada se calcula como la resta de la suma -26
                    shifted -= 26
                result += chr(shifted)
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                result += chr(shifted)
        else:
            result += char
    return result

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 cesar_cipher.py <text> <shift>")
        sys.exit(1)

    text = sys.argv[1]
    shift = int(sys.argv[2])

    encrypted_text = cesar_cipher(text, shift)
    print(f"{encrypted_text}")
