import random
import string as s
import sys

def converter_base(num, base):
	num = int(num)
	lista1 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"
	lista = []
	while num != 0:
		dec1 = int(num % base)
		num = num / base
		lista.append(lista1[dec1])
	lista.reverse()
	return "".join(lista).lstrip("0")


def desconverter_base(num, base=10):
	numeros = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"
	num = str(num)[::-1] if base > 36 else str(num)[::-1].upper()
	if any([i in num for i in numeros[base:]]): raise TypeError('Invalid input number for this base!')
	resultado = 0

	for i in range(len(num)):
		resultado += (base**i) * (int(numeros.index(num[i])))

	return resultado


def expanded_form(num):
    num = str(num)[::-1]
    result = []
    
    for i in range(len(num)):
        half_result = 10**i * int(num[i])
        if half_result > 0: result.append(str(half_result))
    
    return ' + '.join(result[::-1])

'''
for i in range(2000):
	string = ''
	for k in range(50):
		string += random.choice([c for c in s.ascii_lowercase])
	print(string, int(string, base=23))
'''

print (eval("eval(sys.argv[1])(sys.argv[2], int(sys.argv[3]))"))