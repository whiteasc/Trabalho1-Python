# Ler um número inteiro
num = int(input("Digite um número inteiro: "))

# Mostrar os 50 números anteriores
print("\n 50 Números Anteriores:")
for i in range(num - 1, num - 51, -1):
    print(i)

# Mostrar os próximos 50 números
print("\n Próximos 50 números:")
for i in range(num + 1, num + 51):
    print(i)
