import math



def findPrimeNumbs(numb):
    dNumb = 2
    facts = []
    while dNumb * dNumb <= numb:
        if numb % dNumb:
            dNumb += 1
        else:
            numb / 1
            facts.append(dNumb)
    return facts


    print (findPrimeNumbs(36))