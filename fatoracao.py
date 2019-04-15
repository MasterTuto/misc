#-*- coding: utf-8 -*-

def fatorar(num):
	used_numbers = []
	for number in range(2, num):
		while num % number == 0:
			num = num / number
			used_numbers.append(number)
	return used_numbers if len(used_numbers) > 0 else "%s é primo, logo deve-se retornar ele mesmo." % num

print fatorar(56)


def dec2bin(num):
	lista = []
	while num != 0:
		dec1 = str(num % 2)
		num = num / 2
		lista.append(dec1)
	lista.reverse()
	return "".join(lista)

def dec2hex(num):
	lista1 = "0123456789ABCDEF"
	lista = []
	while num != 0:
		dec1 = num % 16
		num = num / 16
		lista.append(lista1[dec1])
	lista.reverse()
	return "".join(lista)

def dec2ter(num):
	lista = []
	while num != 0:
		dec1 = str(num % 3)
		num = num / 3
		lista.append(dec1)
	lista.reverse()
	return "".join(lista)

def fatorial(num):
	k = 1
	for i in range(1, num+1):
		k *= i
	return k


def primeFactors(n):
    result = 0
    used_numbers = {}
    i = 2
    string = ''
    while n > 1:
            used_numbers[str(i)] = 0
            while n % i == 0:
                n = n / i
                result += n
                used_numbers[str(i)] += 1
            i += 1
    used_numbers = {k: used_numbers[k] for k in used_numbers if used_numbers[k] > 0}
    ordered_used_numbers = sorted([int(c) for c in used_numbers])
    for i in ordered_used_numbers:
    	string += "(%s**%s)" % (i, used_numbers[str(i)]) if used_numbers[str(i)] > 1 else "(%s)" % i
    return string
