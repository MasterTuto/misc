# *-* coding: utf-8 *-*

'''

Sequência de Fibbonacci  em Python,
Primeira tentativa

'''

# Necessárias

def fibo(x):
	a = 0
	b = 1
	for i in range(0, x+1):
		a, b = b, a + b
		print a,


numero  = 13
fibo(numero)