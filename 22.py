#a = int(input("Pirmais skaitlis: "))
#b = int(input("Otrais skaitlis: "))
#print(a + b) 
# programma izdrukāja skaitli 55
# programma izdrukāja skaitli 10, pirmais un otrais skaitlis tika saskaitīts, taču pirmajā variantā skaitļi tika salikti kopā

vards = input("Vārds: ")
hp = int(input("Dzīvības punkti: "))
jauda = float(input("Uzbrukuma jauda: "))
bojajums = hp * jauda
print(vards)
print(hp)
print(bojajums)
#kļudas nosaukums ir ValueError
# bīstamākā ievade no šīm iepriekš minētajām ir negatīva HP vērtība, jo tad gala rezultātā sanāk negatīvs skaitlis, kas ir galīgi neloģiski. Pārējās kļūdas nav tik bīstamas, jo vienkārši met ārā ValueError vai 0.