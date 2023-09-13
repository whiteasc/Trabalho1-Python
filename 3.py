# Receber os três números decimais
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

# Descobrir o menor número
menor = n1

if (n2 < menor):
    menor = n2
if (n3 < menor):
    menor = n3

# Exibir o menor número
print('O menor número é:',menor)