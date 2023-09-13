# Receber os três números decimais
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

# Descobrir o maior número
maior = n1

if (n2 > maior):
    maior = n2
if (n3 > maior):
    maior = n3

# Exibir o maior número
print('O maior número é:',maior)