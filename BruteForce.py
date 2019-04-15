import zipfile

nome_arquivo = input("Insira o nome do arquivo: ")
nome_wordlist = input("Insira o nome do arquivo wordlist: ")

arquivo = zipfile.ZipFile(nome_arquivo, "r")
wordlist = open(nome_wordlist, "r")

for i in wordlist.readlines():
	try:
		arquivo.extractall("./content", pwd=i.strip("\n"))
		print "Senha encontrada:",i
		break
	except:
		continue
arquivo.close()
wordlist.close()
