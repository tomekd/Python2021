"""
Sprawdź czy tekst 'aAaAaA' znajduje się w tablicy passwords.
W zależności czy znajduje się czy też nie, wyświetl na ekranie odpowiedni komunikat.
"""

passwords = ['aaAaa', 'aAAAaa', 'aaaaaaA', 'aaaAAAAA', 'aaAAAaa', 'aAaAaA', 'aAaAaAA']

if 'aAaAaA' in passwords:
    print('Jest')
else:
    print('Nie jest')
