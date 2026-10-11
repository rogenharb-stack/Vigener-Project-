# Vigenère Cipher Project

A simple Python program that implements a classic Vigenère cipher combined with multi-round row and column permutations for enhanced data security.

How to Run
1. Make sure you have Python installed on your computer.
2. Open your terminal or command prompt in the project folder.

Follow the interactive menu in the console: choose option 1 to encrypt or option 2 to decrypt, then enter your message and secret key when prompted.

How It Works (Permutation Logic)
Substitution: The program first applies a standard Vigenère cipher using your secret keyword to shift letters.

Multi-Round Permutation: It then runs additional transposition rounds—rearranging characters across structured columns and rows to mix up patterns and increase security.

Reversibility: During decryption, the code reverses these exact steps in the opposite order (reversing rows first, then columns, and finally undoing the substitution) so your message is accurately restored.

Example Test Cases
1. Encryption Cycle
Mode: Encrypt (1)

Message: HELLO

Secret Key: KEY

Result: Final ciphertext is JRIVS.

2. Decryption Cycle
Mode: Decrypt (2)

Message: HELLO

Secret Key: KEY

Result: Original message is successfully recovered as UHJBK.
