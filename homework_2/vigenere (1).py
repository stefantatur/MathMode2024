def encrypt_vigenere(plaintext: str, keyword: str) -> str:
   
    ciphertext = ""

    name_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']
    name_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']

    k = 0
    fullkeyword = keyword * (len(plaintext) // len(keyword) + 1)

    for i in plaintext:
        if i in name_lower:
            ciphertext += name_lower[(name_lower.index(i) + name_lower.index(fullkeyword[k].lower())) % 26]
        elif i in name_upper:
            ciphertext += name_upper[(name_upper.index(i) + name_upper.index(fullkeyword[k].upper())) % 26]
        else:
            ciphertext += i
        k += 1

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:


    plaintext = ""

    name_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']
    name_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']

    k = 0
    fullkeyword = keyword * (len(ciphertext) // len(keyword) + 1)

    for i in ciphertext:
        if i in name_lower:
            plaintext += name_lower[(name_lower.index(i) - name_lower.index(fullkeyword[k].lower())) % 26]
        elif i in name_upper:
            plaintext += name_upper[(name_upper.index(i) - name_upper.index(fullkeyword[k].upper())) % 26]
        else:
            plaintext += i
        k += 1

    return plaintext
