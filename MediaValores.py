qtde = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while (valor > 0.0):
    soma = soma + valor
    qtde = qtde + 1
    #Entrada de valores
    valor = float(input("Digite um valor: "))

#Caso digite um valor negativo o laço encerra
media = soma / qtde
print("\n Total da Soma: ", soma)
print("\n Quantidade de valores digitados: ",qtde)
print("\n Média dos valores: ",media)