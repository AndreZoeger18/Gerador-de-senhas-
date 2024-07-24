
"""
Security = chave 
5ecurt1ty = senha 

"""

"""
hex 

1 = 1
2 = 2
ate 9 = 9
10 = A 
11 = B 
12 = C 
13 = D
14 = E
15 = F

"""

chave = input("digite a base da seua senha")

senha = ""
for letra in chave:
    if letra in "Aa": senha =senha + "10"
    elif letra in "Bb": senha = senha + "11"
    elif letra in "Cc": senha = senha + "13"
    elif letra in "Dc": senha = senha + "14"
    elif letra in "Ee": senha = senha + "15"
    elif letra in "Ff": senha = senha + "#"
    elif letra in "Rr": senha = senha + "%"
    elif letra in "Ss": senha = senha + "$"
    else: senha = senha + letra
print(senha)
        