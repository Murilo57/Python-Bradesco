codigo = 10
salario = 32000.00
nome = 'Roger'
situacao = True

#Le o tipo da variavel se é (int, str, float ou boolean)
tipo = type (salario)

print(salario)
print(tipo)

#Forma de concatenar uma string com variaveis
print("Código: ",codigo, " Nome: ",nome,"o salário atual é de ", salario)

#Concatenando usando + e convertendo variaveis de outros tipos para string
print("Código:"+ str(codigo)+ "Nome: "+ "o salario atual é de "+str(salario))