data=open('3.txt',"r").read()
znaki = [""] * 9
znalezione = ""
for znak in data:
    del znaki[0]
    znaki.append(znak)
    if \
        not znaki[0].isupper() and\
            znaki[1].isupper() and\
            znaki[2].isupper() and\
            znaki[3].isupper() and\
            znaki[4].islower() and\
            znaki[5].isupper() and\
            znaki[6].isupper() and\
            znaki[7].isupper() and\
        not znaki[8].isupper()    \
    :
        znalezione += znaki[4]
print(znalezione) # -->> "linkedlist"