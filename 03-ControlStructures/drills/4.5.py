plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
        # read the character's code (use ord())
        orginal_char_code = ord(char)
        # add one to the character's code
        encrypted_char_code = orginal_char_code + 1
        # replace new character code with its
        orgiginal_char_code = encrypted_char_code
        # corresponding character (use chr())
        encrypted_char = chr(orgiginal_char_code)
        # add encrypted character to encrypted text
        encrypted_text += encrypted_char

print(plain_text)
print(encrypted_text)