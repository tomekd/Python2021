"""
Poniżej znajduje się lista `websites`. 
 * Pod jakim indeksem znajduje się wartość 'pinterest.com'?
 * Zamień wartość piątego elementu na 'yahoo.com'.
 * Dodaj na koniec listy nowy element: 'bing.com'
 * Korzytając z indeksowania stwórz podlistę składającą się z elementów 'facebook.com', 'twitter.com'. Wynik przypisz do zmniennej `social_networks`.
 * Rozszesz listę `websites` o elementy z listy `polish_websites`.
 * Ile elementów liczy teraz lista `websites`?
"""


websites = ['google.com', 'facebook.com', 'twitter.com', 'pinterest.com', 'python.org']

polish_websites = ['onet.pl', 'interia.pl', 'wp.pl']

# -> pinteres znajduje się pod indeksem 3
websites[4] = 'yahoo.com'
websites.append('bing.com')
social_networks = websites[1:3]
websites.extend(polish_websites)

print(len(websites))