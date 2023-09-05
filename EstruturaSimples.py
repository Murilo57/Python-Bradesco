#Condição simples (if)
A = input("Informe um valor para a variavel A: ")
B = input("Informe um valor para a variavel B: ")

if (A > B):
    aux = A;
    A = B;
    B = aux;

print("O valor da variavel A agora é: ", A)
print("O valor da variavel B agora é: ", B)

#Condição composta (if/else)
idade = int(input("Digite a idade da pessoa: "))
if idade > 18:
    print("Maior Idade")
else:
    print("Menor Idade")