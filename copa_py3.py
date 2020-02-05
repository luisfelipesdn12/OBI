#!/usr/bin/env python

# campeonato
# obi2018 - Fase 2

a = int(input())
b = int(input())

a = a + 15
b = b + 15
fase = 0

while a != b:
    a = a//2
    b = b//2
    fase = fase + 1

if fase == 1:
    print('oitavas')
elif fase == 2:
    print('quartas')
elif fase == 3:
    print('semifinal')
else:
    print('final')
 
