# Receber a idade da pessoa
anos = int(input("Digite quantos anos você tem: "))
meses = int(input("Digite quantos meses você tem: "))
dias = int(input("Digite quantos dias você tem: "))

# Converter anos e meses em dias
anos_conv = anos * 365
meses_conv = meses * 30

# Calcular os dias totais
idadefinal = anos_conv + meses_conv + dias

#Exibir os dias
print("Você já viveu ", idadefinal, "dias")