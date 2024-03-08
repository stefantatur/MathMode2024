import typing as tp
import unittest

def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    abc = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(0, len(plaintext)):
        a = plaintext[i].lower()
        if a not in abc:
            ciphertext += a
            continue
        ind = abc.index(a) + shift
        if ind > 25: ind=ind-26
        
        if plaintext[i].isupper():
            let = abc[ind].upper()
        else:
            let = abc[ind]
        ciphertext += let

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    abc = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(0, len(ciphertext)):
        a = ciphertext[i].lower()
        if a not in abc:
            plaintext += a
            continue
        ind=abc.index(a) - shift
        if ind<0: ind=26+ind

        if ciphertext[i].isupper():
            let = abc[ind].upper()
        else:
            let = abc[ind]
        plaintext += let

    return plaintext



def caesar_breaker_brute_force(ciphertext: str, dictionary: str) -> int:
    """
    Brute force breaking a Caesar cipher.
    """

    best_shift = 0
    d = dictionary
    abc = 'abcdefghijklmnopqrstuvwxyz'
    for shift in range(26):
        slovo = ""
        for smbl in ciphertext:
            if smbl.isupper():
                flag = 1
            else:
                flag = 0
            new_smbl = smbl.lower()
            if new_smbl not in abc:
                slovo += new_smbl
                continue
            index = abc.index(new_smbl) + shift
            if index > 25:
                index = index - 26
            if flag:
                slovo += abc[index].upper()
            else:
                slovo += abc[index]
        if slovo in d:
            best_shift = shift
    if 26 - best_shift < best_shift:
        best_shift = 26 - best_shift
    return best_shift

print(caesar_breaker_brute_force("sbwkrq", "python"))


import random
import string

class CaesarTestCase(unittest.TestCase):
    def test_encrypt(self):
        cases = [
            ("", 0, ""),
            ("python", 0, "python"),
            ("PYTHON", 0, "PYTHON"),
            ("Python", 0, "Python"),
            ("Python3.6", 0, "Python3.6"),
            ("", 3, ""),
            ("PYTHON", 3, "SBWKRQ"),
            ("python", 3, "sbwkrq"),
            ("Python", 3, "Sbwkrq"),
            ("Python3.6", 3, "Sbwkrq3.6"),
        ]

        for i, (plaintext, shift, chiphertext) in enumerate(cases):
            with self.subTest(case=i, plaintext=plaintext, chiphertext=chiphertext):
                self.assertEqual(chiphertext, encrypt_caesar(plaintext, shift=shift))

    def test_decrypt(self):
        cases = [
            ("", 0, ""),
            ("python", 0, "python"),
            ("PYTHON", 0, "PYTHON"),
            ("Python", 0, "Python"),
            ("Python3.6", 0, "Python3.6"),
            ("", 3, ""),
            ("SBWKRQ", 3, "PYTHON"),
            ("sbwkrq", 3, "python"),
            ("Sbwkrq", 3, "Python"),
            ("Sbwkrq3.6", 3, "Python3.6"),
        ]

        for i, (chiphertext, shift, plaintext) in enumerate(cases):
            with self.subTest(case=i, chiphertext=chiphertext, plaintext=plaintext):
                self.assertEqual(plaintext, decrypt_caesar(chiphertext, shift=shift))

    def test_randomized(self):
        shift = random.randint(8, 24)
        plaintext = "".join(random.choice(string.ascii_letters + " -,") for _ in range(64))
        ciphertext = encrypt_caesar(plaintext, shift=shift)
        self.assertEqual(
            plaintext,
            decrypt_caesar(ciphertext, shift=shift),
            msg=f"shift={shift}, ciphertext={ciphertext}",
        )

if __name__ == "__main__":       
    unittest.main()