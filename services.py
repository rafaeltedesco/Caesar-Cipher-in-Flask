from string import ascii_lowercase

def cipher(message, key, mode='encrypt'):
  cipher_message = ''
  for letter in message.lower():
    idx = 0
    if letter in ascii_lowercase:
      idx = ascii_lowercase.find(letter)
      if mode == 'encrypt':
        idx += key
        if idx >= len(ascii_lowercase):
          idx -= len(ascii_lowercase)
      elif mode == 'decrypt':
        idx -= key
        if idx < 0:
          idx += len(ascii_lowercase)
      cipher_message += ascii_lowercase[idx]
    else:
      cipher_message += letter
  return cipher_message
