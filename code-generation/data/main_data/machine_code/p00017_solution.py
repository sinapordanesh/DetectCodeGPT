def caesar_cipher(text):
    for shift in range(26):
        decoded_text = ''
        for char in text:
            if char.islower():
                decoded_text += chr((ord(char) - shift - 97) % 26 + 97)
            else:
                decoded_text += char
        if 'the' in decoded_text or 'this' in decoded_text or 'that' in decoded_text:
            return decoded_text

# Read input
import sys
for line in sys.stdin:
    print(caesar_cipher(line.strip()))