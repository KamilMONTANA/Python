# 🔐 Day 8: Caesar Cipher

A classic Caesar Cipher program implemented in Python. The application enables users to both encrypt (encode) and decrypt (decode) messages using a customizable numerical shift key.

## 🎯 Project Goal
To practice alphabet array index lookups, function scoping, input checking, and the mathematical modulo `%` operator to safely wrap indexing.

## ✨ Features
- **Bi-directional Cipher:** Supports both message encryption (`encrypt`) and decryption (`decrypt`).
- **Flexible Shift Parameter:** Accepts shift integers between 1 and 25.
- **Space & Symbol Preservation:** Keeps whitespace characters intact during shift procedures, ensuring the resulting layout is highly readable.
- **Index Wrap Protection:** Uses modulo arithmetic to prevent index overflows when shifting letters at the end of the alphabet.

## 📂 Project Structure
- `CaesarCipher.py` – the singular console application script containing all shift math and interactive menu options.

## 🎓 Key Learnings
- Finding a character's index position in an array using the `.index()` method.
- Applying modular arithmetic (`% 26`) to wrap shifted letters back around the alphabet.
- Creating reusable parameterized functions that adjust behaviors based on function arguments.
- Designing standard verification checks to reject invalid shift keys or mode requests.

## 🚀 How to Run the Project
Make sure you have Python installed. Then run the following in your terminal:
```bash
python CaesarCipher.py
```
