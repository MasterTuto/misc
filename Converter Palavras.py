# -*- coding: utf-8 -*-

from os import system
lista = []
lista2 = []


def inputar():
    palavra = raw_input("Palavra>> ")
    tipo = raw_input("""
    Digite o número corresponde do que quer fazer:
    \t\t[1] Converter a palavra
    \t\t[2] Desconverter a palavra
                     """)
    return palavra, tipo

def converter(palavra):
    for i in palavra:
        novo_i = chr(ord(i) + 10)
        lista.append(novo_i)
    print "".join(lista)

def desconverter(lista):
    for i in lista:
        novo_i = chr(ord(i) - 10)
        lista2.append(novo_i)
    print "".join(lista2)

while True:
    palavra, tipo = inputar()
    if tipo == '1':
        system('cls')
        converter(palavra)
    elif tipo == '2':
        desconverter(palavra)
