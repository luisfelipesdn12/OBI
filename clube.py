#Clube do cinco
#https://olimpiada.ic.unicamp.br/pratique/p1/2016/f1/clube/

n = int(input()) #Coleta n de associados
abcdefg = input().split() #coleta as outras

#transforma o input de (str) para (int)
for i in range(0, len(abcdefg)):
  abcdefg[i] = int(abcdefg[i])

#define cada (abcdefg)
a = abcdefg[0]
b = abcdefg[1]
c = abcdefg[2]
d = abcdefg[3]
e = abcdefg[4]
f = abcdefg[5]
g = abcdefg[6]

if (n==a+b+c-d-e-f+g):
  print("N")
else: print("S")