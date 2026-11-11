a = "5"
b = 5
c = 5.5
print(type(a))
print(type(b))
print(type(c))
print(a + a)
vards = input("Ievadi varoņa vārdu: ")
punkti = int(input("Ievadi bāzes punktus: "))
reizinatajs = float(input("Ievadi reizinātāju: "))
aprēķinu_kopa = punkti * reizinatajs
print(vards, "ieguva", aprēķinu_kopa, "punktus")
# kļūda atrodas devītajā rindā
# ievadot ar komatu, arī rāda valuEerror
