#Abre o arquivo
arquivo = open('arqText.txt','w')

#Grava no arquivo
arquivo.write('Curso de Python garai \n')
arquivo.write('Praticando')
arquivo.close() #Fecha o arquivo

#Leitura do arquivo de text

leitura = open('arqText.txt','r')
print(leitura.read())
leitura.close()